# Your research checkpoint

Use this optional guide after the exercise in [DEMO_SCRIPT.md](DEMO_SCRIPT.md).
This file is a template for your steward's current review, not evidence that a
commit, push, test, or submission has happened. Existing notebook entries and
Git history do not authorize new operations.

## Review before saving

Ask in the main chat:

> Wait for notebook edits to finish. Have git_steward inspect status, diffs,
> branch, tracking, remotes, generated artifacts, and available validation
> evidence. Replace the review section below with the actual proposed file
> list, commit message, and any unresolved issues. Do not commit or push.
> Preserve unrelated work. If no Git repository exists, explain local setup.

Potential experiment artifacts, to include only if present and relevant:

```text
lab_notebook.txt
figures/observed_rates.png
figures/observed_rates.csv
figures/observed_rates.json
figures/observed_rates_observations.csv
figures/exposure_test.png
figures/exposure_test.csv
figures/exposure_test.json
figures/exposure_test_observations.csv
```

Include code, tests, or documentation only when they belong to your reviewed
change. Record validation that was actually performed; do not copy historical
pass counts. A ZIP-based repository's first commit may also need the source and
agent definitions. The steward should propose that scope explicitly.

## Current review

Not prepared for this learner's session. Ask the steward to fill in:

- Current branch, baseline, and status.
- Explicit changed paths to stage and any unrelated work to exclude.
- Proposed commit message.
- Actual validation evidence, or checks still needed.
- Intended publication remote, if publication is requested.

## Optional local commit

After reviewing the proposal, paste:

> Have git_steward create research/exposure-demo if absent, inspecting an
> existing branch before using it. Stage only the reviewed explicit paths,
> inspect the staged diff, and commit with the reviewed message. Preserve
> unrelated work. Report the resulting hash and status. Do not push.

A commit requires a configured Git identity. If Git reports that one is missing,
configure your own identity locally before retrying; do not use the author's.

## Optional GitHub publication

Cloning the source repository normally points `origin` to the author's repository.
You need your own fork or another repository you can write to. Have the steward
inspect the actual destination; do not assume push permission. A ZIP download has
no configured remote. Set a destination only after choosing your own repository.

Replace the bracketed URL before pasting:

> Have git_steward verify that the publication destination is [my fork or
> repository URL]. If remote configuration needs changing, show the proposed
> change before applying it. Once the destination is verified, push the reviewed
> research branch, set its upstream, and verify the remote commit. Do not
> force-push. Report the branch URL and local status. After successful
> publication, have lab_notebook record only the actual submission command,
> commit hash, and URL. Explain whether that new notebook entry remains uncommitted.

Optional follow-up:

> Have git_steward open a draft pull request from my published branch against
> my chosen base repository and branch. Include the research question, actual
> results, limitations, and reproduction commands. Verify and report the URL.

Keep failed or planned operations distinguishable from completed submissions.
If authentication or permissions block publication, retain the local checkpoint
and report the blocker accurately.
