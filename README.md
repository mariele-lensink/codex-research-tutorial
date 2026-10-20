# Codex research tutorial: code, notebook, and GitHub

Work with one main coding chat in VS Code and delegate two checkpoint roles:
`lab_notebook` records scientific reasoning and evidence; `repo_steward` organizes
Git history and authorized GitHub publication.

The exercise is inspired by the parent filename
`ToyModel1_recover_underlying_mrates.py`, which now contains a NumPy Poisson model for liver and colon mutation counts.
The tutorial follows that model and adds pooled rate estimation. The original script is untouched.

## 1. Open the workspace

In VS Code choose **File → Open Folder** and select this
`codex-research-tutorial` folder. This makes its project instructions and custom
agent definitions the working context. Install the official Codex extension,
sign in, and open its sidebar. Start a fresh project chat after adding agents.
Use Python 3.9 or later. Install the recorded dependency with
`python3 -m pip install -r requirements.txt` (preferably in a virtual environment).

Current official documentation supports project agents in `.codex/agents/`.
If delegation is unavailable in your installed client, update it and check
workspace policy. Do not assume that naming an agent proves it was invoked.
Inspect the subagent activity/results in the client.

Sources checked on 19 October 2026:
- [VS Code extension](https://learn.chatgpt.com/docs/codex/ide)
- [Subagents and custom agent configuration](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Project instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

## 2. Establish the working agreement

Paste into the main chat:

> Read AGENTS.md, research/overview.md, and recent lab notebook entries.
> You are my coding and research collaborator. Use the lab_notebook custom
> agent at research checkpoints and repo_steward for Git operations. Confirm
> which roles are available. Keep our research discussion in this main chat.
> Start by explaining the assumptions of the teaching model. Do not change it yet.

The agents work when invoked. Their durable record is in files; do not rely on
a continuously running observer or a subagent remembering every conversation.
The main chat must pass decisions and evidence to the notebook agent.
All agents inherit parent permissions. File ownership is a coordination rule.

## 3. Run and understand a baseline

In the VS Code terminal, from this folder:

```sh
python3 -m unittest discover -s tests -v
python3 src/recover_rates.py --seed 42 --bins 100 --opportunities-per-bin 1000 --output results/baseline.json
```

Ask the main chat:

> Explain the difference between the simulated true mutation rate and its estimate.
> Identify the assumptions that would fail with incomplete observation or
> changing rates. Use the baseline output as evidence. Keep conclusions limited
> to this synthetic model.

The estimator is total mutation counts divided by total callable opportunities.
For each bin, Y is Poisson with mean L times r. The original script reports
mean counts; this tutorial additionally recovers the underlying r. Its liver
simulation typo is corrected in the tutorial copy only.
Generated JSON is ignored by Git. Commands and selected numerical results belong
in the notebook so a reader can regenerate the output.

## 4. Delegate the first checkpoint

> Delegate to lab_notebook. Record our question, hypothesis, rationale, exact
> baseline command, Python version, parameters, seed, results, artifact path,
> limitations, starting commit, and working-tree status. Use the actual output,
> and flag anything missing. Wait for its entry, then have repo_steward inspect
> the final diff and checks. Report what would go into the first commit.
> Do not commit or publish yet.

Read the notebook entry and staged-file proposal. Check that the agent recorded
observed values, rather than predicted outcomes or a fabricated experiment.

Then authorize the local checkpoint:

> Have repo_steward create a local baseline commit containing the reviewed
> tutorial files and notebook. Inspect the staged diff first. Report the commit
> hash and final status. Do not push yet.

## 5. Make one research change

> Before coding, have lab_notebook record this comparison plan: compare sample
> sizes of 10, 100, and 1000 bins at 1000 opportunities per bin over seeds 0 through 29. Then help me implement a
> repeatable comparison using the existing simulator. Summarize mean absolute
> error separately for each tissue and bin count, and include variability.
> Add checks that verify aggregation against known small examples. Run the
> comparison and explain whether the results support our hypothesis. Do not
> assume every individual run improves with sample size.

This extension is intentionally left as the learner's coding task. Discuss the
statistical question in the main chat while it helps implement the analysis.
Use the checkpoint sequence again after the experiment, including failed runs.

## 6. Publish a research checkpoint

First prepare a concrete review:

> Have repo_steward inspect the current branch, remote configuration, final
> diff, ignored files, and validation evidence. Prepare a publication summary
> with the proposed branch, exact files, commit message, and PR description.
> Check for private data, credentials, and unnecessary generated artifacts.

Choose or create the intended GitHub repository. Configure its actual URL;
replace OWNER and REPOSITORY below before running anything:

```sh
git remote add origin https://github.com/OWNER/REPOSITORY.git
```

If `origin` already exists, inspect it before making changes. Git authentication
must work. Creating a PR additionally needs an authenticated GitHub tool such as
the GitHub CLI or an available connector. A connected chat app does not by
itself prove local Git push authentication is configured.

After reviewing the proposed publication:

> Have repo_steward create a research/sample-size branch if needed, commit the
> reviewed changes, push that branch to origin, and open a draft pull request.
> Include the scientific question, assumptions, results, limitations, and exact
> reproduction commands. Verify the push and report the PR URL.

No remote repository is created or configured by this starter. Local commits,
remote pushes, and PR creation are separate steps with separately verifiable
outcomes. Do not force-push or include private research data by default.

## 7. Resume in a new chat

> Read AGENTS.md, research/overview.md, the latest notebook entries, Git status,
> and recent commits. Tell me the current scientific question, latest verified
> finding, unresolved limitations, repository state, and suggested next experiment.
> Use the notebook and repo steward roles at the next checkpoint.

You have completed the exercise when another person can understand the notebook,
rerun the experiment, and locate the corresponding code checkpoint.
