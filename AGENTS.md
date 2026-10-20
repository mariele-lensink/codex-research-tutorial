# Research tutorial workflow

The main chat collaborates with the researcher on questions, code, experiments,
and interpretation. Use NumPy for the Poisson mutation-count model. Dependencies are in requirements.txt.

Explicitly delegate meaningful checkpoint documentation to `lab_notebook` and
repository maintenance to `repo_steward`. These are checkpoint tasks, not an
assumption that agents continuously monitor the workspace. If a custom agent
is unavailable, report that fact and offer the same role as a bounded task;
never claim delegation occurred when it did not.

At each research checkpoint:
1. Main agent finishes code edits and runs relevant checks and the experiment.
2. Give lab_notebook the question, rationale, exact command, output, parameters,
   seeds, artifact paths, starting commit, and working-tree status.
3. Wait for notebook edits to finish. Then ask repo_steward to review the final
   diff and validation evidence and handle the authorized Git operations.
4. Main agent reports findings, limitations, notebook path, and repository state.

The steward may inspect during coding, but all Git mutations must be serialized
after file edits finish. Only the steward performs Git mutations during delegated
work. File ownership instructions are coordination rules, not sandbox boundaries.

Read research/overview.md and recent notebook entries when starting a session.
Record hypotheses before running comparisons. Preserve negative findings.
Never present simulated data as empirical evidence or an estimate as known truth.
Never invent runs, validation results, notebook history, or GitHub publication.

For this tutorial, local inspection and file edits are authorized. Commit when
the researcher requests a checkpoint commit. Push and create PRs when requested;
repository visibility changes and destructive Git operations need explicit scope.
Do not commit secrets, private datasets, or generated results by default.

Validation: `python3 -m unittest discover -s tests -v`
Baseline: `python3 src/recover_rates.py --seed 42 --bins 100 --opportunities-per-bin 1000`
