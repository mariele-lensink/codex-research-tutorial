# Self-guided exercise: a research team of agents

Follow these steps in one main Codex conversation after completing the setup in
[README.md](README.md). Paste one prompt at a time, inspect the response and
changed files, and decide when to continue. You make the scientific decisions;
the main agent coordinates the two specialists.

The aim is to practice clear delegation, evidence-based records, and coordinated
checkpoints. This small model could be handled by one agent; separate roles
make handoffs visible but add coordination work and do not guarantee correctness.

## 1. Orient the team

Paste:

> Read AGENTS.md and the latest lab_notebook.txt entries. Briefly explain our
> research question and current model without running it or revealing previous
> test outcomes. Review unresolved items in Follow up. Use lab_notebook for
> concise scientific records and git_steward for repository checkpoints. Keep
> our discussion here. Use the repository's .venv Python interpreter. Confirm
> whether you can invoke the two project agent profiles; disclose any fallback.
> Have git_steward inspect the repository without changing it. Do not commit or
> publish anything.

Check: the response explains the question and roles, acknowledges any historical
records, and reports repository status. A ZIP download may have no Git repository;
that is expected. Open `AGENTS.md` and both `.codex/agents/*.toml` files yourself.
Notice each role's editing boundaries and requirement to use verified evidence.
No introduction or file inspection needs a new scientific notebook entry.

If profile selection is unavailable but subagents work, ask the main agent to
pass each role's instructions to a bounded delegate. If subagents are unavailable,
resolve client setup using the official documentation linked from the README
before continuing with the multi-agent exercise.

## 2. Inspect synthetic observations

Paste:

> Run python ToyModel1_recover_underlying_mrates.py --stage observe with .venv
> and show figures/observed_rates.png. Compare the observed tissue rates with
> the model predictions. Explain the sampling distributions without assuming a
> cause. Have lab_notebook record only the actual command, essential parameters,
> results, and artifact paths. Keep the entry concise.

Check: inspect the PNG and new notebook entry. Orange diamonds are synthetic
observations, blue boxes are 500 simulated experiments per tissue. Each experiment
uses 100 bins of 1,000 callable opportunities. Callable opportunities are the
measurement denominator; they are distinct from environmental mutagen exposure.
The central 95% of simulations describes variability across experiments, not
uncertainty in the simulated mean. Both datasets use the same assumed mechanism,
with separate random seeds.

Ask yourself: does a tissue difference alone distinguish an intrinsic biological
difference from an environmental explanation?

## 3. Record a hypothesis before testing

Paste, or substitute your own hypothesis:

> My hypothesis is that greater environmental mutagen exposure, motivated by
> sunlight/UV, explains the higher skin mutation rate. Inspect the mechanism
> and propose an intervention that equalizes exposure while holding intrinsic
> biology and callable opportunities fixed. State the prediction and have
> lab_notebook record the hypothesis and a short test plan before running
> anything. Do not run the test yet.

Check: read the hypothesis and prediction in `lab_notebook.txt` before continuing.
The main agent should explain which assumptions the script imposes. This is an
exercise in testing an assumed mechanism inside a synthetic world; the notebook
must distinguish your prediction from an observed result.

## 4. Test the intervention

Paste:

> Run python ToyModel1_recover_underlying_mrates.py --stage test with .venv and
> show figures/exposure_test.png. Compare the mean skin-minus-liver difference
> in the original and equalized environments across 500 simulations. Run
> python -m unittest discover -s tests -v in the same environment. Explain
> whether our prediction holds within this model and what remains unproven.
> Have lab_notebook append actual results, validation, commands, and artifact
> paths to the planned experiment without repeating the whole history.

Check: use the values actually returned by your run. The equalized-exposure panel
contains simulations only; there are no observed intervention measurements.
Software tests check the implementation, not biological validity. Ask the main
agent to explain why agreement between synthetic measurements and simulations
cannot independently validate the mechanism that generated both.

## 5. Audit the handoff and preserve an open question

Paste:

> Show the concise hypothesis, test, and result entries lab_notebook just wrote.
> Check them against the actual commands and output. Confirm reproduction
> commands and artifact paths are present, and predictions are distinguishable
> from results. Delegate a small correction if needed; do not add a duplicate
> summary or rerun the experiment.

Check: compare the entry with `figures/exposure_test.json`. The notebook should
preserve essential evidence without copying the whole JSON or chat transcript.

Choose a question you actually want to revisit, then replace the bracketed text:

> Have lab_notebook add this to Follow up, with today's date: [my deferred
> test, concern, or question]. Keep it open for the next session; do not run it now.

For example, you could ask how changing the number of callable opportunities
would affect sampling variability. Add it only if you intend to revisit it.

## 6. Review a checkpoint

Git is optional. If you downloaded a ZIP, follow the initialization guidance in
[README.md](README.md), or skip to step 8.

Paste:

> Wait for notebook edits to finish. Have git_steward review the current code,
> notebook, figures, data, validation evidence, branch, and remotes. Update
> GIT_CHECKPOINT.md with an explicit proposed file list and commit message for
> my current work. Distinguish existing baseline files from new changes and
> preserve unrelated edits. Do not commit or push yet.

Check: inspect the proposed scope and diff yourself. The steward should identify
which files actually changed, rather than assume that every listed output is new.
The notebook agent finishes before the steward prepares repository mutations.
See [GIT_CHECKPOINT.md](GIT_CHECKPOINT.md) for optional commit and publication prompts.
A local commit is sufficient to complete this exercise; publishing is optional.

## 7. Optional: save and publish your work

Follow the checkpoint guide one prompt at a time. Use your own fork or repository
if you publish. Review the destination and file list before authorizing a push.
Do not reuse publication authorization from the repository's historical records.

Check: a commit, a push, and a pull request are separate operations. Ask for
verified evidence of each operation you actually requested.

## 8. Resume and explore independently

Start a new conversation in this workspace and paste:

> Read AGENTS.md and the latest notebook entries. Summarize the current research
> state and unresolved Follow up items. Have git_steward inspect the repository.
> Do not run experiments yet. Help me select one next question and state a
> prediction before delegating its notebook record.

You have completed the core exercise when you can locate a prediction written
before its test, reproduce a run from its record, explain the limits of the
synthetic evidence, and identify which work each agent performed.

For further practice, choose one change: vary sampling effort, compare random
seeds, or introduce a tissue-specific baseline to challenge the current model.
Discuss the scientific question first, record the hypothesis and plan, then
change and test the code. Keep each experiment's artifacts distinguishable and
ask the steward to propose a checkpoint when the notebook is complete.
