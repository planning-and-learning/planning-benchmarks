# planning-benchmarks

PDDL planning benchmark suites — classical, numeric, profiling, and generated
learning splits — published as the [`pypddl-datasets`](https://pypi.org/project/pypddl-datasets/)
Python package. The package itself is small: benchmark data is downloaded on
first use from the matching GitHub release and cached locally.

## Usage

```sh
pip install pypddl-datasets
```

```python
import pypddl_datasets as pb

pb.list_suites()          # ['autoscale-agile-strips', ..., 'ipc-optimal-strips', ...]

task = pb.fetch_task("classical/tests/gripper/test-1.pddl")
task.domain_path          # .../gripper/domain.pddl   (correct also where instances
task.task_path            # .../gripper/test-1.pddl    carry their own domain files)
task.domain, task.problem # "classical-tests-gripper", "test-1.pddl" — lab-safe display names

domain = pb.fetch_domain("classical/downward-benchmarks/gripper")
domain.path               # the domain directory
domain.tasks              # list[Task], downloaded once and cached

suite = pb.fetch_suite("ipc-optimal-strips")   # Suite(path, domains)
for domain in suite.domains:
    for task in domain.tasks:
        run_planner(task.domain_path, task.task_path)
```

Most suites have a `-test` companion (e.g. `"ipc-optimal-strips-test"`) whose
entries are one representative task per domain — a cheap smoke run before
committing to a full suite. `pb.export_suite(suite, dest)` materializes a
suite as a plain directory tree for non-Python tools.

Domains can be filtered by their declared PDDL requirements — `supported` is
a capability ceiling (keep what your planner handles), `requires` a feature
floor (keep what exercises a feature). The data declares exactly the atomic
requirements each file uses (strict-validated; aggregates like `:adl` never
appear), and all queries are metadata-only (no download):

```python
from pypddl_datasets import Requirement as R

SUPPORTED = {R.STRIPS, R.TYPING, R.ACTION_COSTS, R.NEGATIVE_PRECONDITIONS}

pb.task_requirements("classical/tests/gripper/test-1.pddl")  # frozenset({R.STRIPS})
pb.domain_requirements("classical/tests/gripper")     # union over the domain's tasks
pb.find_tasks(requires={R.CONDITIONAL_EFFECTS})       # task names, per-task precision
pb.find_domains(suite="ipc-satisficing-strips", supported=SUPPORTED)
pb.find_suites(supported=SUPPORTED)                   # suites runnable in full
pb.fetch_suite("ipc-satisficing-strips", supported=SUPPORTED)   # filtered fetch
```

`pb.list_domains()` lists every individually fetchable domain. The cache
location defaults to the platform cache dir and can be overridden with the
`PYPDDL_DATASETS_CACHE` environment variable. On machines without internet
access, set `PYPDDL_DATASETS_DATA` to a local checkout's `data/` directory
and domains resolve there without downloading.

## Repository layout

- `src/pypddl_datasets/` — the package: fetch API, suite definitions, and the
  instance generators (including the train/valid/test split configurations).
- `data/` — all benchmark data, organized as `<formalism>/<collection>/<domain>`
  (`classical/`, `numeric/`). Not shipped in the package; released as a single
  archive on `data-v*` GitHub releases, downloaded and unpacked once per
  machine on first use.
- `data/classical/generated/<domain>-{train,valid,test}/` — fixed learning
  splits produced by the generators. These committed instances are the
  reproducibility contract; regenerate with
  `python -m pypddl_datasets.generators.classical.<domain>.generate_instances`.
- `scripts/package_data.py` — turns `data/` into the byte-reproducible
  `data.tar.gz` release archive.
- `scripts/extract_requirements.py` — regenerates the committed
  `requirements.{tasks,domains,suites}.json` metadata files (run after
  changing data; a test guards freshness).
- `validate.py` — parses every domain/problem with pypddl; must pass for a
  data release to go out.

## Releasing

Data and package releases are decoupled; data releases are permanent
(published package versions pin them by tag).

1. **Data changed?** Tag and push `data-v<N>`. The workflow validates all
   PDDL (aborting the release on failure), packages `data.tar.gz`, and
   uploads it to the `data-v<N>` GitHub release. Copy the sha256 it prints
   into `DATA_SHA256` (and bump `DATA_VERSION`) in
   `src/pypddl_datasets/__init__.py`.
2. **Package release:** bump `version` in `pyproject.toml`, tag and push
   `v<version>`. The workflow verifies the tag matches the version and that
   the pinned data release exists with the pinned hash, then builds and
   publishes to PyPI via trusted publishing. No assets are uploaded — code
   releases cost nothing in storage.

## Contributing data

Clone with Git LFS (large instances are LFS-tracked):

```sh
git lfs install
git clone git@github.com:planning-and-learning/planning-benchmarks.git
cd planning-benchmarks && git lfs pull
```

Track PDDL files larger than 10 MiB before staging them:

```sh
find data -type f -name '*.pddl' -size +10M -print0 | xargs -0 git lfs track --filename
git add .gitattributes data
```

Domain directories must contain their `.pddl` files directly (that is how
`scripts/package_data.py` discovers them), and domain names flattened with
`/` → `-` must stay unique (Task.domain; test-guarded). Run `pytest tests`
to check suite definitions stay consistent.
