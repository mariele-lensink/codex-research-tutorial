# Practice research with multiple agents

A self-guided tutorial for using a main research agent with two specialist
agents: a scientific notebook keeper and a Git steward. You will explore a
small mutation-rate model, record a prediction before testing it, inspect the
evidence, and optionally save and publish your own research checkpoint.
No facilitator or previous conversation is required.

## Start here

You need Python 3.10 or newer, Git for the checkpoint exercises, and a signed-in
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
It contains the prompts to paste into your main chat and checks for each step.

## How the team works

| Role | Responsibility | Definition |
|---|---|---|
| Main agent | Discuss science with you, run analysis, coordinate handoffs | [AGENTS.md](AGENTS.md) |
| `lab_notebook` | Record plans and verified evidence concisely; preserve open questions | [.codex/agents/lab_notebook.toml](.codex/agents/lab_notebook.toml) |
| `git_steward` | Review changes and propose checkpoints; perform authorized Git operations | [.codex/agents/git_steward.toml](.codex/agents/git_steward.toml) |

Project agents are defined in `.codex/agents/`, as described in the
[official subagent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents).
Ask the main agent to confirm whether it can invoke these profiles. If it
cannot, it should disclose this and pass their instructions to bounded
subagents. If delegation itself is unavailable, use a client that supports it
to practice multiple agents; completing all roles in one chat is a fallback,
but does not demonstrate delegation. Agents work when invoked during an active
session; they do not watch files while the chat is idle.

## The scientific exercise

Why might skin have a higher mutation rate than liver? The script generates
synthetic measurements and model predictions for two tissues, then provides an
equalized-exposure scenario to investigate an assumed mechanism. All data are
synthetic. A tissue difference alone cannot identify its cause, and agreement
with this model does not establish real biological causality.

Start with the walkthrough before reading the implementation if you want to
make your own prediction. The existing [lab_notebook.txt](lab_notebook.txt)
contains historical preparation and run records, including outcomes. Preserve
these as history; your agent should append your own runs and avoid presenting
old results as newly executed experiments. Fixed seeds intentionally make runs
reproducible. Generated files may already exist; rerunning a stage overwrites
that stage's output files.

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

Each stage writes a PNG, a CSV of simulated replicate rates, a JSON summary,
and an `_observations.csv` file under `figures/`. The prefixes are
`observed_rates` and `exposure_test`. JSON includes seeds, parameters, package
versions, and summaries. Orange diamonds are synthetic measurements from one
sample per tissue; blue boxes represent repeated model experiments. Measurements
exist only for the original environments. Whiskers show the central 95% of
simulated rate estimates, not a confidence interval for their mean.

If imports fail, check that dependencies were installed in the same interpreter
your agent uses. If no figure appears in chat, open the PNG directly in your
editor or file browser; plotting saves files without opening a GUI window.
