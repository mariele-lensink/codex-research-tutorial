# Try a research team of agents

Complete the setup in [README.md](README.md), then work through these prompts
in one Codex chat. You can use your own words. The project instructions already
explain the agents' jobs; you don't need to repeat those rules in every message.

You discuss the science with the main agent. It delegates scientific records to
`lab_notebook` and repository reviews to `git_steward`. Watch for those handoffs
and inspect their work as you go. Agents act during the conversation, not while
the workspace is closed.

## 1. Get oriented

> Read AGENTS.md and the notebook. What are we studying? Don't run anything
> yet. Use .venv for Python.

Look for a short explanation of the model and any open questions. The agent
should also arrange a Git review and disclose if it cannot use the project
agent profiles. Open `.codex/agents/` to see their instructions.

If subagents are unavailable, use the setup help linked in the README. Having
one agent perform every role won't give you practice with delegation.

## 2. Look at the observations

> Run the observation stage and show me the figure. How do mutation rates
> vary with tissue and exposure?

The command is `python ToyModel1_recover_underlying_mrates.py --stage observe`.
Open `figures/inference_observations.png`. Each dot is a synthetic training
sample's mutation count divided by its callable opportunities. Both tissues
have the same exposure levels. Look for trends within tissues and differences
at matching exposure levels. Scatter reflects Poisson sampling variability.
Check that `lab_notebook` recorded the actual run.

## 3. Make a prediction

> Could tissue, exposure, or both explain the pattern? Help me plan a fair
> comparison and record our prediction before running it.

Discuss the tissue-only, exposure-only, and combined models. Each estimates
its own rates from training data; it isn't given the generator's coefficients.
The comparison uses separate held-out samples and mean Poisson deviance (lower
is better). Predict which explanation will generalize best and why. Read the
notebook plan before continuing. Avoid inspecting held-out scores at this step.

## 4. Compare explanations

> Fit the three models and compare their held-out predictions. Show the
> figure and run the unit tests. What does the evidence support?

The commands are:

```sh
python ToyModel1_recover_underlying_mrates.py --stage test
python -m unittest discover -s tests -v
```

Inspect `figures/inference_comparison.png`. Which omitted effect harms
prediction? How large are the score differences? Model coefficients are
estimates, and a single split does not establish their uncertainty. The fitted
models restrict effects to be nonnegative and omit interactions. These are
synthetic observational comparisons, not evidence of a biological cause.
Check that the notebook now contains actual results.

## 5. Check the record and choose what comes next

> Show me the notebook entry. Does it match what we actually ran and found?

Look for the hypothesis, prediction, commands, results, and artifact paths.
Compare the numbers with `figures/inference_comparison.json`. Ask for a correction
if needed; a record check doesn't require another experiment.

Then discuss your concerns:

> What concerns should we investigate next? Help me turn them into a few
> research questions. Let me choose before adding them to Follow up.

For example, ask whether the ranking changes across seeds, whether effects
could be negative, or what happens when tissue and exposure no longer overlap.
These are ideas to discuss, not tasks you must adopt.

After choosing, you can simply say:

> Save those questions for next time. Don't run them yet.

Check the notebook's Follow up section. It should preserve your agreed questions
with enough context to resume, alongside any existing unresolved items.

## 6. Review your changes

Git is optional; skip this step if you're only practicing the science.

> Have git_steward review our changes and suggest a checkpoint.
> Don't commit or push yet.

Read the proposed file list and commit message. The notebook should be complete
before the steward prepares the checkpoint. Existing files and unrelated edits
should be distinguished from this session's changes.

For optional saving and publication, follow [GIT_CHECKPOINT.md](GIT_CHECKPOINT.md).
A commit saves locally; a push publishes to a remote. Publish to your own fork
or repository, and review the destination first.

## 7. Pick up next time

Start a fresh conversation in this workspace:

> Read the notebook. Where did we leave off, and which questions did we save
> for next time? Don't run anything yet.

Choose a question, discuss a prediction, and repeat the plan–test–record cycle.
You have practiced the workflow when you can find a prediction recorded before
its test, reproduce the experiment, explain its limitations, and identify what
each agent contributed.
