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

pb.list_suites()                      # ['autoscale-agile-strips', ..., 'ipc-optimal-strips', ...]
paths = pb.fetch_suite("ipc-optimal-strips")   # list[Path], downloaded once and cached
gripper = pb.fetch_domain("classical/downward-benchmarks/gripper")
sorted(gripper.iterdir())             # domain.pddl, prob01.pddl, ...
```

Most suites have a `-test` companion (e.g. `"ipc-optimal-strips-test"`) whose
entries are one representative problem file per domain — a cheap smoke run
before committing to a full suite.

`pb.list_domains()` lists every individually fetchable domain. The cache
location defaults to the platform cache dir and can be overridden with the
`PYPDDL_DATASETS_CACHE` environment variable.

## Repository layout

- `src/pypddl_datasets/` — the package: fetch API, suite definitions, and the
  instance generators (including the train/valid/test split configurations).
- `data/` — all benchmark data, organized as `<formalism>/<collection>/<domain>`
  (`classical/`, `numeric/`). Not shipped in the package;
  released as per-domain tarballs.
- `data/classical/generated/<domain>-{train,valid,test}/` — fixed learning
  splits produced by the generators. These committed instances are the
  reproducibility contract; regenerate with
  `python -m pypddl_datasets.generators.classical.<domain>.generate_instances`.
- `scripts/package_data.py` — turns `data/` into release tarballs + registry.
- `validate.py` — parses every domain/problem with pypddl; must pass for a
  release to go out.

## Releasing

Bump `version` in `pyproject.toml`, tag `v<version>`, and push the tag. The
release workflow validates all PDDL, uploads per-domain tarballs to a GitHub
release, and publishes the package to PyPI — in that order, so a validation
failure stops anything from being published.

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
`scripts/package_data.py` discovers them), and directory names must not
contain `--`. Run `pytest tests` to check suite definitions stay consistent.
