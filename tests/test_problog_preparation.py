"""Prepared clauses are reusable; executions and sampled worlds remain isolated."""
from concurrent.futures import ThreadPoolExecutor
from random import Random
from threading import Barrier

import pytest
from typing_extensions import override

from pypddl_datasets.generators._problog.engine import sample_source
from pypddl_datasets.generators._problog.prepared import clear_prepared_cache, prepared_program

SOURCE = "0.5::coin. query(coin)."


def test_completed_preparation_reuses_static_clauses() -> None:
    clear_prepared_cache()
    with prepared_program(SOURCE) as first:
        original_engine = first.engine
    with prepared_program(SOURCE) as second:
        assert second.engine is original_engine
    with prepared_program(SOURCE, accelerated=False) as reference:
        assert reference.engine is not original_engine


def test_reentrant_borrow_does_not_share_an_executing_engine() -> None:
    with prepared_program(SOURCE) as outer:
        with prepared_program(SOURCE) as inner:
            assert outer.engine is not inner.engine
            assert outer.database is not inner.database
    with prepared_program(SOURCE) as later:
        assert later.engine is outer.engine


def test_threads_have_separate_engines_and_databases() -> None:
    barrier = Barrier(2)

    def borrow(_: int) -> tuple[int, int]:
        with prepared_program(SOURCE) as prepared:
            barrier.wait(timeout=5)
            return id(prepared.engine), id(prepared.database)

    with ThreadPoolExecutor(max_workers=2) as pool:
        first, second = pool.map(borrow, range(2))
    assert first[0] != second[0]
    assert first[1] != second[1]


def test_failed_execution_is_evicted_and_next_sample_is_clean() -> None:
    class AbortedRandom(Random):
        @override
        def random(self) -> float:
            raise RuntimeError("interrupted draw")

    clear_prepared_cache()
    with prepared_program(SOURCE) as before:
        old_engine = before.engine
    with pytest.raises(RuntimeError, match="interrupted draw"):
        sample_source(SOURCE, AbortedRandom())
    with prepared_program(SOURCE) as after:
        assert after.engine is not old_engine
    resumed = sample_source(SOURCE, Random(1))
    clear_prepared_cache()
    assert resumed == sample_source(SOURCE, Random(1))


def test_cache_reuse_does_not_keep_previous_random_choices() -> None:
    clear_prepared_cache()
    first = sample_source(SOURCE, Random(1))
    second = sample_source(SOURCE, Random(0))
    assert first != second
    assert first == sample_source(SOURCE, Random(1))
