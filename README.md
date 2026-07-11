# Clone

Install Git LFS, then clone the repository:

```sh
git lfs install
git clone git@github.com:planning-and-learning/planning-benchmarks.git
```

# Add large PDDL files

Track PDDL files larger than 10 MiB before staging them:

```sh
find suites -type f -name '*.pddl' -size +10M -print0 \
  | xargs -0 git lfs track --filename

git add .gitattributes suites
git lfs status
```

Commit `.gitattributes` together with the tracked files.
