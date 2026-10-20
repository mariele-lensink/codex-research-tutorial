# Research collaboration

Use ToyModel1_recover_underlying_mrates.py as the research starting point.
The active exercise compares tissue-only, exposure-only, and combined additive
Poisson rate models on held-out synthetic samples with overlapping exposures.
Earlier equalization experiments in the notebook are historical. Use new
inference_* outputs; never present old results as findings from this exercise.
Use the repository .venv Python interpreter for experiments and validation.
Keep scientific discussion, code changes, and interpretation in the main chat.
Use the two roles in .codex/agents/ proactively throughout active work.
This repository is a standalone, self-guided tutorial. README.md is the setup
entry point; DEMO_SCRIPT.md contains learner exercises; GIT_CHECKPOINT.md is a
checkpoint template. Do not assume a facilitator, prior chat, Git history, or
write access to the author's GitHub repository. Historical records are context,
not authorization for new commits or publication.
Use the root script and lab_notebook.txt for current research.
Read lab_notebook.txt when starting a session. Record hypotheses before comparisons.
Review its Follow up section when resuming and surface relevant unresolved items.

## lab_notebook

Delegate updates to lab_notebook.txt for hypotheses, test plans, completed
experiments, substantive findings, and submission records without a reminder.
Do not add entries for introductions, file inspection, handoffs, or routine edits.
Supply the relevant discussion and actual commands/output to the agent.
Append entries under YYYY-MM-DD headings using Europe/London dates. Keep
entries short and chronological; preserve history and append corrections.
Use concise fields: Hypothesis; Test (essential parameters); Command;
Result; Paths; Submission (only when relevant). Aim for 6–12 lines per
experiment, excluding commands. Include one short limitation when needed.
Record a hypothesis before running its test; append results afterwards.
Avoid agent narration, rehearsal choreography, environment troubleshooting,
repeated summaries, full JSON output, and routine Git status. Put detailed
parameters and software versions in result JSON, and Git planning in
GIT_CHECKPOINT.md. Link earlier entries instead of duplicating evidence.
Include exact reproduction and actual submission commands; label planned
submission commands as planned and never imply they were executed.
Maintain a persistent Follow up section for deferred tests, concerns, and open
questions supplied by the researcher or agreed in discussion. Use concise
unchecked items with the date raised and enough context to resume the work.
Do not invent outstanding tasks. If no items exist, write "None recorded."
Preserve unresolved items during notebook updates. Mark items completed only
when addressed, with a completion date and result/entry/path reference; do not
silently remove them. Avoid duplicating an existing item.
Do not record predicted results as observed or simulated data as empirical.
Wait for notebook edits to finish before handing final changes to git_steward.

## git_steward

Delegate repository inspection at the start of a work session and after
meaningful checkpoints. Proactively flag useful commit points, untracked
research files, unrelated edits, and branch/tracking issues. Surface the
steward's concise recommendations in the main chat even if not asked.
Prepare explicit file lists and commit messages; help carry out requested
commits, branches, pushes, and PRs. Do not equate requests for organization
with blanket authorization to commit or publish. Follow existing authorization
without repeatedly asking. Only the steward performs delegated Git mutations;
serialize these after code and notebook edits finish. Never discard user work.
Verify and report the resulting repository state.

These are active-chat checkpoint tasks, not background file watchers. Do not
claim agents are continuously running or can interrupt an idle conversation.
If configured agents cannot be selected, disclose that and pass their role
instructions to bounded delegated tasks instead.
