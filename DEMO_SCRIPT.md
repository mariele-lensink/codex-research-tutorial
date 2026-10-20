# Presenter script: investigating tissue environments

## Introduction: why use multiple agents?

Say: “Research involves more than writing an analysis. We need to remember why
we ran a test, what we found, which questions remain open, and which version of
the code produced the result. Those responsibilities compete with the science
for our attention.

“In this demo, I keep the research discussion in one main chat and delegate two
recurring responsibilities. The notebook agent maintains a concise scientific
record and a Follow up list. The Git steward helps identify useful checkpoints
and organizes saving the code, figures, and reasoning together.

“The goal is less cleanup at the end of a session and less reconstruction when
I return. I invoke these agents at meaningful checkpoints, rather than after
every message. They work when given a task; they aren't continuously watching
the project.

“This small experiment could be handled by one agent. Separate roles give each
responsibility dedicated attention, but also require clear handoffs. They don't
guarantee correctness, and I still make the scientific decisions and review
what gets published. For a larger project, I might also ask an independent
reviewer to challenge an important result, or delegate a separate data check
while I develop the analysis.

“Let's see whether this arrangement helps us move from a question to a result
that is documented, reproducible, and ready to save.”

Presenter setup: this is research inside a synthetic toy world, not a claim
about real tissues. Within that world, call the orange points our observations
and the blue boxes model predictions. The source contains the mechanism we
will inspect; we are testing an explanation, not independently discovering an
unknown biological cause. Existing preparation runs remain labelled as such.

## 1. Meet the research team

Say: “Our project asks why skin accumulates more mutations than liver.
I'll work with the main agent on the science. A notebook agent will maintain
our experimental record, and a Git steward will organize research checkpoints.
I give instructions here; the main agent sends each specialist the relevant
context and evidence, then brings their work back to this conversation.”

Enter:
> Read AGENTS.md and the latest lab_notebook.txt entries. Briefly explain our
> research question and current model without running it or revealing previous
> test outcomes. Review unresolved items in the notebook's Follow up section.
> Use lab_notebook for concise scientific records and
> git_steward for repository checkpoints. Keep our discussion here.

Show: the Python model and the two active agent definitions in `.codex/agents/`.
Explain that these agents act when invoked, not as continuous background watchers.

## 2. Inspect our observations

Say: “We have measurements from liver and skin. Before explaining the
pattern, let's visualize it. I'm asking the main agent to run the analysis;
it will give the actual output to the notebook agent for recording.”

Enter:
> Run python3 ToyModel1_recover_underlying_mrates.py --stage observe and show
> figures/observed_rates.png. Compare our observed tissue rates with the model
> predictions. Explain the sampling distributions without assuming a cause.
> Have lab_notebook record only the command, essential parameters, results,
> and artifact paths. Keep the entry concise.

Show: the figure. Orange diamonds are observations in our toy world; blue boxes
are 500 simulated experiments per tissue. Equal callable opportunities let us
compare rates rather than confusing mutation burden with available exposure.
Here callable opportunities are measurement denominators, distinct from
mutagenic environmental exposure.

## 3. Propose an environmental explanation

Say: “Skin has a higher mutation rate. Is its biology intrinsically different,
or is its environment more mutagenic? My hypothesis is that environment drives
the difference. I want the hypothesis written down before we test it.”

Enter:
> My hypothesis is that greater environmental exposure, motivated by sunlight/UV, explains the skin's higher
> mutation rate. Have lab_notebook record that hypothesis and a short test plan
> before running anything. Inspect the exposure mechanism and propose an
> intervention that equalizes exposure while holding intrinsic biology and
> callable opportunities fixed. State the prediction; do not run the test yet.

Show: the notebook's hypothesis and prediction. Explain: “The main agent is
helping design the test; the notebook agent preserves what we predicted before
seeing its outcome. It receives our reasoning, rather than guessing from code.”

## 4. Perform the intervention in the model

Say: “We cannot observe these tissues under equal exposure in our dataset.
We can ask our model a counterfactual question: what would happen if exposure
were equal? This panel must contain predictions only.”

Enter:
> Run python3 ToyModel1_recover_underlying_mrates.py --stage test and show
> figures/exposure_test.png. Compare the mean skin-minus-liver rate difference
> across the original and equalized environments over 500 simulations. Run
> python3 -m unittest discover -s tests -v. Explain whether the prediction holds
> within our model. Have lab_notebook append the result, validation, command,
> and artifact paths to the planned test without repeating the whole history.

Show: the two panels. Discuss the actual values returned, not memorized results.
If the gap shrinks as predicted, say: “Within this model, changing environment
is sufficient to remove the tissue difference. Our conclusion depends on the
model's assumed exposure mechanism; we have not established real-world causality.”

## 5. Inspect the research record

Say: “The experiment is only useful if someone can reproduce it. Let's inspect
what the specialist recorded, rather than write a second summary ourselves.”

Enter:
> Show the concise hypothesis, test, and result entries lab_notebook just wrote.
> Confirm that the reproduction commands and figure/data paths are present.
> If something is missing, delegate a small correction; do not add a duplicate
> summary or rerun the experiment.

Show: `lab_notebook.txt`, followed by a result JSON if detailed parameters are
needed. Explain: “The notebook holds the science; the output files hold the
full numerical detail. Our main conversation stays focused on interpretation.”

To park a question during the discussion, enter:
> Have lab_notebook add this to Follow up, with today's date: [my deferred
> test, concern, or question]. Keep it open for our next session; do not run it now.

## 6. Save a research checkpoint

Say: “We now have a result worth preserving with its code and reasoning.
The main agent waits for notebook edits to finish, then asks the Git steward
to review the completed work. That keeps repository operations coordinated.”

Enter:
> Have git_steward review the completed code, notebook, figures, data, tests,
> tracking, branch, and remote. Update GIT_CHECKPOINT.md with the exact files,
> proposed commit message, and prompts for committing and pushing a research
> branch to GitHub. Treat the existing setup commit as the baseline and include
> only new demo changes and generated results. Do not commit or push yet.

Show: the steward's proposed scope and commit message. Explain: “The steward
organizes the checkpoint and identifies what will be published. I review that
concrete proposal before authorizing the Git operations.”

## 7. Authorize the Git process when ready

These prompts perform real operations, even during a rehearsal. Skip them if
you are demonstrating the proposal without actually committing or publishing.

Say: “I'm now authorizing the steward to save the reviewed local checkpoint.”

Enter:
> Have git_steward create research/exposure-demo, stage only the reviewed
> checkpoint scope, inspect the staged diff, and commit it. Report the hash
> and status. Do not push yet. Preserve unrelated work and inspect any existing
> branch before proceeding.

Say: “The commit exists locally. I'll separately authorize publication.”

Enter:
> Have git_steward verify origin is the intended GitHub repository, push
> research/exposure-demo, set its upstream, and verify the remote commit.
> Report the GitHub branch link. Do not force-push. After successful publication,
> have lab_notebook record only the submission command, commit hash, and URL.

Optional:
> Have git_steward open a draft PR describing the question, intervention,
> results, figure, limitations, and reproduction commands. Report its URL.

Show: verified Git output or GitHub page. Describe a commit, push, or PR as
completed only after the steward has verified it.
