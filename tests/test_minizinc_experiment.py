"""Independent output checks for the bounded MiniZinc experiment; no solver required."""
from __future__ import annotations

from collections.abc import Callable
from copy import deepcopy
import json
import os
from pathlib import Path
from runpy import run_path
import signal
import sys
from threading import Event, Timer
from time import monotonic, sleep
from typing import Any, cast

import pytest

EXPERIMENT = Path(__file__).parents[1] / "experiments/minizinc"
BENCHMARK = run_path(str(EXPERIMENT / "benchmark.py"))
run = cast(Callable[[list[str], float, int], dict[str, Any]], BENCHMARK["run"])
validate = cast(Callable[[dict[str, Any], int], dict[str, Any]], BENCHMARK["validate"])
parse_minizinc = cast(Callable[[dict[str, Any], int, int, int, bool], dict[str, Any]], BENCHMARK["parse_minizinc"])
sample_graphs = cast(Callable[..., dict[str, Any]], run_path(str(EXPERIMENT / "problog_baseline.py"))["sample_graphs"])


def solution(*, graph_only: bool = True) -> dict[str, Any]:
    """A connected two-edge visibility tree and two connected rover subgraphs."""
    return {
        "n": 3, "nr": 2, "graph_only": graph_only,
        "src": [1, 1, 2], "dst": [2, 3, 3],
        "visible": [True, True, False], "move": [True, True, False] * 2,
        "rover_at": [1, 3], "lander_at": 2,
        "soil_sample": [False, False, False] if graph_only else [True, False, True],
        "soil_goal": [False, False, False] if graph_only else [False, False, True],
        "soil_capable": [False, False] if graph_only else [True, False],
    }


@pytest.mark.parametrize("graph_only", [True, False])
def test_minizinc_validator_accepts_connected_graph_and_soil_fragments(graph_only: bool) -> None:
    checked = validate(solution(graph_only=graph_only), 1)
    assert checked["validated"]
    assert checked["visibility_edges"] == 2
    assert checked["movement_edges"] == [2, 2]
    assert checked["soil_goals"] == int(not graph_only)


@pytest.mark.parametrize("field,value", [
    ("src", [1, 1, 2, 99]),  # zip must not silently discard an unmatched tail.
    ("dst", [2, 3]),
    ("visible", [True, False]),
    ("move", [True, True, False]),
    ("visible", [True, False, False]),  # Visibility is disconnected.
    ("move", [True, False, False, True, True, False]),  # One rover is disconnected.
    ("move", [True, True, False, True, False, True]),  # Connected movement outside visibility.
    ("rover_at", [1]),
    ("lander_at", 4),
    ("visible", [1, True, False]),  # Boolean arrays must contain booleans.
    ("soil_sample", [False, False]),
    ("soil_goal", [False, False, False, False]),
    ("soil_capable", [False]),
    ("soil_sample", [True, False, False]),  # Graph-only fragment fixes soil arrays false.
])
def test_minizinc_validator_rejects_invalid_graph_output(field: str, value: Any) -> None:
    candidate = solution()
    candidate[field] = value
    with pytest.raises(ValueError):
        validate(candidate, 1)


@pytest.mark.parametrize("field,value", [
    ("soil_goal", [True, False, True]),
    ("soil_sample", [True, False, False]),
    ("soil_capable", [False, False]),
    ("soil_sample", [True, False]),
    ("soil_goal", [False, False, True, False]),
    ("soil_capable", [True]),
    ("soil_goal", [False, False, 1]),
])
def test_minizinc_validator_rejects_invalid_soil_output(field: str, value: Any) -> None:
    candidate = solution(graph_only=False)
    candidate[field] = value
    with pytest.raises(ValueError):
        validate(candidate, 1)


def test_minizinc_parser_validates_every_materialized_solution() -> None:
    first = solution()
    second = deepcopy(first)
    second["visible"] = [True, False, False]
    stdout = "\n".join(json.dumps(item, separators=(",", ":")) for item in [first, second])
    with pytest.raises(ValueError):
        parse_minizinc({"stdout": stdout, "stderr": "", "status": "completed"}, 1, 3, 2, True)


@pytest.mark.parametrize("n,nr,graph_only", [(4, 2, True), (3, 1, True), (3, 2, False)])
def test_minizinc_parser_checks_requested_configuration(n: int, nr: int, graph_only: bool) -> None:
    stdout = json.dumps(solution(), separators=(",", ":"))
    with pytest.raises(ValueError):
        parse_minizinc({"stdout": stdout, "stderr": "", "status": "completed"}, 1, n, nr, graph_only)


def test_problog_graph_baseline_materializes_forced_joint_graphs() -> None:
    sampled = sample_graphs(3, 2, edge_probability=1)
    triangle = [[0, 1], [0, 2], [1, 2]]
    assert sampled["status"] == "success"
    assert sampled["visibility"] == triangle
    assert sampled["movement"] == [triangle, triangle]
    assert sampled["visibility_density"] == 1
    assert sampled["movement_connected"] == [True, True]


def test_problog_graph_baseline_keeps_finite_failure_outcome() -> None:
    sampled = sample_graphs(3, 2, graph_budget=0)
    assert sampled["status"] == "failure"
    assert sampled["failure"] == ["failure(graph_exhausted)"]
    assert "visibility" not in sampled and "movement" not in sampled


def test_problog_graph_baseline_reuses_preparation_without_reusing_worlds() -> None:
    first = sample_graphs(3, 2, seed=7)
    sample_graphs(3, 2, seed=8)
    repeated = sample_graphs(3, 2, seed=7)
    assert first["graph_sha256"] == repeated["graph_sha256"]
    assert first["visibility"] == repeated["visibility"]
    assert first["movement"] == repeated["movement"]


def _live_recorded_child(record: Path) -> int | None:
    """Check process identity, allowing an already-dead zombie awaiting reaping."""
    try:
        pid, birth = json.loads(record.read_text(encoding="utf-8"))
        fields = Path(f"/proc/{pid}/stat").read_text(encoding="ascii").rsplit(")", 1)[1].split()
        return int(pid) if fields[19] == birth and fields[0] not in {"Z", "X"} else None
    except (FileNotFoundError, ProcessLookupError, json.JSONDecodeError):
        return None


def test_minizinc_timeout_kills_child_that_started_a_new_session(tmp_path: Path) -> None:
    record = tmp_path / "child.json"
    child_code = (
        "import json, os, time; from pathlib import Path\n"
        "pid = os.getpid()\n"
        "birth = Path(f'/proc/{pid}/stat').read_text().rsplit(')', 1)[1].split()[19]\n"
        f"Path({str(record)!r}).write_text(json.dumps([pid, birth]))\n"
        "print(pid, flush=True)\n"
        "time.sleep(30)\n"
    )
    parent_code = (
        "import subprocess, sys, time\n"
        f"subprocess.Popen([sys.executable, '-c', {child_code!r}], start_new_session=True)\n"
        "time.sleep(30)\n"
    )
    # A broken process-group-only cleanup otherwise leaves the child holding the
    # stdout pipe open. Bound that failure and clean only our recorded process.
    watchdog_used = Event()

    def watchdog_cleanup() -> None:
        pid = _live_recorded_child(record)
        if pid is not None:
            watchdog_used.set()
            try:
                os.kill(pid, signal.SIGKILL)
            except ProcessLookupError:
                pass

    watchdog = Timer(5, watchdog_cleanup)
    watchdog.daemon = True
    watchdog.start()
    try:
        result = run([sys.executable, "-c", parent_code], 0.5, 0)
        assert result["status"] == "timeout"
        assert record.exists(), "child must start before the timeout to exercise cleanup"
        deadline = monotonic() + 1
        while _live_recorded_child(record) is not None and monotonic() < deadline:
            sleep(0.01)
        assert not watchdog_used.is_set(), "harness cleanup required the test watchdog"
        assert _live_recorded_child(record) is None, "detached child survived the timeout"
    finally:
        watchdog.cancel()
        watchdog_cleanup()
