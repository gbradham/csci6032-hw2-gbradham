---
name: blackboard-submission
description: Preflight, package, and submit CSCI 6032 Homework 2 (repository gbradham/csci6032-hw2-gbradham) to Blackboard. Supports a dry run that performs every local check without opening a browser. Use only when the student asks to dry-run or submit this homework.
---

# Blackboard submission for CSCI 6032 Homework 2

Constants:

- Expected remote: `https://github.com/gbradham/csci6032-hw2-gbradham.git`
- Repository URL to submit: `https://github.com/gbradham/csci6032-hw2-gbradham`
- Archive: `csci6032-hw2-gbradham.tar.gz` (written outside the repository, e.g. `../`)
- Required files: `CSCI6032_hw2.ipynb`, `README.md`, `AGENTS.md`, `sample.txt`,
  `Dockerfile`, `src/text_stats.py`, `tests/test_text_stats.py`,
  `.github/skills/blackboard-submission/SKILL.md`
- Submission text:
  > I used my blackboard-submission skill, reviewed the staged artifacts, explicitly
  > approved the final submission action, and verified Blackboard's confirmation.

Mode: if the student says "dry run" (or does not say "submit"), run steps 1–5 only
and never open or control a browser.

Every shell and browser action goes through the normal permission prompt. Do not
ask for, or rely on, preapproved tools.

## 1. Confirm the repository

Run `git rev-parse --show-toplevel` and `git remote get-url origin`. Stop if the
remote is not the expected remote above.

## 2. Preflight

Run and show the output of:

```bash
git branch --show-current
git status --porcelain
git log --oneline -8
git fetch origin
git status -sb
```

Check that every required file exists in `HEAD` with `git ls-tree -r --name-only HEAD`.

## 3. Stop conditions

Stop and report the problem (do not try to "fix" it silently) if any of these hold:

- the working tree is not clean (`git status --porcelain` prints anything);
- a required file is missing from `HEAD`;
- the branch is not the default branch (`main`), or `HEAD` differs from `origin/main`;
- `git grep -nIiE '(api[_-]?key|secret|token|password|BEGIN [A-Z ]*PRIVATE KEY|ghp_|gho_|github_pat_)' HEAD`
  finds anything that is not clearly documentation; show each hit to the student
  and let them decide;
- the tree contains browser data, `.env` files, credential directories, or
  Blackboard screenshots/receipts.

## 4. Confirm the branch is pushed

`git rev-parse HEAD` must equal `git rev-parse origin/main`. Stop otherwise and ask
the student to push; do not push yourself.

## 5. Build and show the archive

Build from the committed `HEAD` only (this excludes `.git`, untracked files, and
anything ignored):

```bash
git archive --format=tar.gz --prefix=csci6032-hw2-gbradham/ \
  -o ../csci6032-hw2-gbradham.tar.gz HEAD
tar -tzf ../csci6032-hw2-gbradham.tar.gz
```

Stop if the listing contains `__pycache__`, `*.pyc`, `.git/`, credentials, or
unrelated files. Then show the student exactly:

- notebook: `CSCI6032_hw2.ipynb` (at commit `<HEAD sha>`)
- archive: `../csci6032-hw2-gbradham.tar.gz` and its size
- repository URL
- submission text

**Dry run ends here.** Report "dry run complete" and the list of any problems.

## 6. Ask before touching the browser

Ask: "May I use the connected Blackboard tab now?" Wait for a clear yes.

## 7. Student authenticates

Ask the student to log in to Blackboard themselves. Never request, read, type,
store, or display credentials, MFA codes, or cookies. Continue only after the
student says they are logged in.

## 8. Navigate and stage

Navigate only to the CSCI 6032 Homework 2 submission page. Attach the notebook and
the archive, enter the repository URL and the submission text. Do not open other
courses, grades, messages, or unrelated pages.

## 9. Stop before the irreversible action

Do not click Submit. Show the student what is staged on the page: file names,
the repository URL, and the comment text. Ask: "Submit these exact items now? (yes/no)".
A previous general approval does not count. Only the literal answer to this
question counts.

## 10. Submit and verify

After an explicit "yes", click the final submit control once. Read the
confirmation page or receipt and report the confirmation details to the student.
If the automation cannot click safely, tell the student to click it themselves
and verify the confirmation together.

## Never

- commit or save Blackboard screenshots, receipts, page contents, or browser data to the repository;
- change Git history, commit, or push;
- submit during a dry run.
