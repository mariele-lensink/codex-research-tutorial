# Practice research with multiple agents

Learn to work with agents through a small research exercise. You discuss a
mutation-rate model with the main agent while two helpers keep the scientific
notebook and review Git changes.

You can start with ordinary requests like “Show me the observations” or
“Save these questions for next time.” The included instructions tell the
agents how to handle their jobs. You still review their work and decide what
to investigate.

## Start here

You need Python 3.10–3.12, Git for the checkpoint exercises, and a signed-in
Codex client with subagent support. Python 3.12 is a suitable choice for the
pinned dependencies. Agent use requires access through your own account;
Python simulations run locally without an API key. GitHub is needed only for
forking or optional publication.

For a local exercise, clone the repository:

```sh
git clone https://github.com/mariele-lensink/codex-research-tutorial.git
cd codex-research-tutorial
python3 -m venv .venv
```

Activate the environment on macOS/Linux:

```sh
source .venv/bin/activate
```

Or in Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Then install dependencies:

```sh
python -m pip install -r requirements.txt
```

On Windows, use `py -3` instead of `python3` to create the environment if needed.
Run commands from this repository's root. Open **this folder** as your Codex
workspace, and ask the agent to use `.venv` for Python commands.

If you want to publish your work, fork the repository on GitHub first and clone
**your fork's URL** instead. A GitHub ZIP download also works for the science
exercises; it has no Git history or remote. For that route, initialize a local
repository with `git init` if you want to practice local checkpoints. You can
skip Git entirely and still practice the research and notebook handoffs.

Continue with [DEMO_SCRIPT.md](DEMO_SCRIPT.md), the step-by-step exercise.
It contains short example prompts and explains what to look for after each step.
Use your own words and ask follow-up questions as you go.

## How the team works

| Role | Responsibility | Definition |
|---|---|---|
| Main agent | Discuss science with you, run analysis, coordinate handoffs | [AGENTS.md](AGENTS.md) |
| `lab_notebook` | Record plans and verified evidence concisely; preserve open questions | [.codex/agents/lab_notebook.toml](.codex/agents/lab_notebook.toml) |
| `git_steward` | Review changes and propose checkpoints; perform authorized Git operations | [.codex/agents/git_steward.toml](.codex/agents/git_steward.toml) |

Project agents are defined in `.codex/agents/`, as described in the
[official subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).
The main agent should tell you if it cannot use these profiles. It may pass
their instructions to other subagents instead. If it cannot delegate at all,
check your client's subagent support using the documentation above. Agents
work during active chat sessions; they do not watch files while the chat is idle.

## The scientific exercise

Can we distinguish an intrinsic tissue difference from an exposure effect?
Both liver and skin have samples at exposure levels 0, 0.25, 0.5, 0.75, and 1.
This overlap lets us compare tissues at the same exposure and exposure levels
within the same tissue. Exposure is measured without error in this toy world.

The generator uses an additive rate: baseline + tissue effect + exposure effect
× exposure. Counts are Poisson draws with known callable opportunities. These
are teaching assumptions, not realistic measurements or evidence about UV.

Learners compare tissue-only, exposure-only, and combined explanations. Each
candidate estimates nonnegative additive rate coefficients from training counts
by Poisson likelihood, accounting for the number of opportunities. The baseline
is positive; the tissue and exposure effects cannot be negative. A separate
held-out sample set evaluates prediction using mean Poisson deviance (lower is
better). Small differences in scores do not by themselves establish an effect;
repeat across seeds or examine uncertainty before making a strong claim.

Each split has 20 samples per tissue/exposure cell, 200 samples total, with
10,000 opportunities each. Training uses seed 2026; held-out samples use 2027.
The observe stage neither fits models nor generates held-out samples. The test
stage regenerates the same training set, fits three models, and evaluates the
held-out set. Choosing among these models is an inference exercise, not a causal
experiment. The candidate models still simplify biology and omit interactions.

Start with the walkthrough if you want to make your own prediction. Generator
parameters are visible in the code and JSON for teaching transparency, but are
never passed to the fitting functions. Held-out samples should not guide model
tuning; use a new evaluation set if you start tuning after seeing their scores.

The [lab_notebook.txt](lab_notebook.txt) starts empty so your agents can record
your own hypotheses, experiments, and follow-up questions. Generate the figures
and data as you work through the tutorial; completed outputs are not bundled.
Fixed seeds reproduce a run; rerunning overwrites its corresponding files.

## Files and outputs

- [ToyModel1_recover_underlying_mrates.py](ToyModel1_recover_underlying_mrates.py): model and command-line entry point.
- [lab_notebook.txt](lab_notebook.txt): scientific record and persistent Follow up list.
- [GIT_CHECKPOINT.md](GIT_CHECKPOINT.md): optional local checkpoint and publication guide.
- [tests/test_exposure.py](tests/test_exposure.py): checks of model behavior and reproducibility.
- [requirements.txt](requirements.txt): pinned Python dependencies.

For manual execution after activating `.venv`:

```sh
python ToyModel1_recover_underlying_mrates.py --stage observe
python ToyModel1_recover_underlying_mrates.py --stage test
python -m unittest discover -s tests -v
```

The observe stage writes `figures/inference_training.csv`,
`figures/inference_observations.png`, and `figures/inference_observations.json`.
The test stage also writes `figures/inference_heldout.csv`,
`figures/inference_comparison.png`, and `figures/inference_comparison.json`.
CSV rows contain sample ID (local to each split), tissue indicator (`skin`),
exposure, opportunities, and mutation count. JSON contains design parameters;
comparison JSON also records fitted coefficients and held-out scores.

Observation plots show individual training rates against exposure. Comparison
plots show held-out rates, combined-model predictions fitted on training data,
and the three predictive scores. Scatter is sampling variability, not a
confidence interval. No counterfactual intervention measurements are generated.

If imports fail, check that dependencies were installed in the same interpreter
your agent uses. If no figure appears in chat, open the PNG directly in your
editor or file browser; plotting saves files without opening a GUI window.
