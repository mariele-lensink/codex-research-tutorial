# Setup checkpoint and end-of-demo handoff

Reviewed 2026-10-20 (Europe/London). Setup parent: main at c84e528.
Configured fetch/push remote: origin,
https://github.com/mariele-lensink/codex-research-tutorial.git.
Remote reachability and authentication have not been checked.

The researcher authorized a local setup commit on the current branch:
`Prepare research demo and specialist agent workflow`.
No push is requested now. Review, commit, and push new results at the end of
the demo, after code and notebook updates finish.

## Setup scope

Include reusable science code, tests, dependencies, agent policies, presenter
guide, and concise historical preparation record. figures/ is empty and archive/
is absent; neither generated results nor an archive backup is included.
The previous tutorial files are removed from the working setup and remain in
Git history at c84e528. The missing pre-condensation notebook backup is not
claimed to be preserved. Notebook results are historical preparation results;
the listed output paths can be regenerated during the live demo.

Explicit setup paths:

```text
.codex/agents/lab_notebook.toml
.codex/agents/git_steward.toml
.gitignore
AGENTS.md
README.md
requirements.txt
ToyModel1_recover_underlying_mrates.py
tests/test_exposure.py
lab_notebook.txt
DEMO_SCRIPT.md
GIT_CHECKPOINT.md
```

Explicit tracked deletions:

```text
.codex/agents/repo_steward.toml
src/recover_rates.py
tests/test_recover_rates.py
research/overview.md
research/lab-notebook/2026-10-19-setup.md
research/lab-notebook/2026-10-19-poisson-model.md
research/lab-notebook/TEMPLATE.md
results/README.md
```

Current-tree validation: `python3 -m unittest discover -s tests -v` passed
3 tests (0.027s). No figure regeneration occurred. Whitespace and staged-diff
review precede the commit. The parent navigation AGENTS.md is outside this repo.

## End-of-demo checkpoint

Reproduction commands:

```sh
python3 ToyModel1_recover_underlying_mrates.py --stage observe
python3 ToyModel1_recover_underlying_mrates.py --stage test
python3 -m unittest discover -s tests -v
```

Expected generated paths, to inspect for actual existence and content then:

```text
figures/observed_rates.png
figures/observed_rates.csv
figures/observed_rates.json
figures/observed_rates_observations.csv
figures/exposure_test.png
figures/exposure_test.csv
figures/exposure_test.json
figures/exposure_test_observations.csv
```

Blue distributions are simulations. Orange fake measurements exist only in the
original environments; the equalized panel contains predictions alone. Both
come from the assumed synthetic mechanism and establish no biological causality.
Record actual rerun outputs rather than treating preparation results as new.

Copyable end-of-demo prompt:

> Have git_steward review the completed demo against the setup commit, wait for
> notebook edits, and inspect the code, scientific record, eight generated
> figure/data files, and validation. Create research/exposure-demo if absent;
> inspect an existing branch before using it. Stage only explicit reviewed
> changed paths, inspect the staged diff, and commit with message "Record tissue
> exposure demo results". Verify origin is
> https://github.com/mariele-lensink/codex-research-tutorial.git, then push the
> research branch and set its upstream. Do not force-push. Verify the remote
> commit and report its hash, branch URL, and final local status. Preserve
> unrelated work and report authentication or divergence problems accurately.

No remote push or PR has been performed as part of the setup checkpoint.
