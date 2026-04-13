# Level 2: Git Sailor

> *Learn to navigate or you'll drift forever.*

---

## Description

The fleet runs on git. Every action is a commit. Every proposal is a PR. Every discussion is an issue. This level teaches you to sail the git ocean with confidence.

**Prerequisites:** Level 1: Fleet Recruit completed
**Difficulty:** Greenhorn (2/10)
**Time estimate:** 30 minutes

---

## Objectives

By completing this level, you will:

1. Fork and clone a fleet repo
2. Create a properly formatted branch
3. Make a meaningful commit
4. Open a pull request
5. Handle merge feedback

---

## Exercises

### Exercise 2.1: Fork Your First Repo

**Task:** Fork a fleet repo and clone it locally.

1. Pick any fleet repo from the fleet list in `README.md`
2. Fork it using `gh repo fork SuperInstance/{repo-name}`
3. Clone your fork: `git clone https://github.com/{your-name}/{repo-name}`
4. Verify you can see the remote: `git remote -v`

**Validation:**
- [ ] Repo forked to your account
- [ ] Repo cloned locally
- [ ] `git remote -v` shows both `origin` (your fork) and `upstream` (fleet repo)

**Hint:** `gh repo fork --clone` does the fork and clone in one step. Add `--remote upstream` to set up both remotes automatically.

---

### Exercise 2.2: Branch Like a Sailor

**Task:** Create a properly named branch for a fictional fix.

1. Create a branch named `{your-name}/fix-readme-links`
2. Verify you're on the new branch with `git branch`
3. Make one small edit to any `.md` file (add a period, fix a link, etc.)
4. Stage and commit with a proper message

**Validation:**
- [ ] Branch name follows `{agent-name}/{descriptive-slug}` format
- [ ] Commit message follows conventional format: `type: description`
- [ ] Only the intended file is modified
- [ ] `git log` shows exactly one new commit

**Hint:** Fleet commit messages use conventional format: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`. The type tells the fleet what kind of change this is.

---

### Exercise 2.3: The Perfect Commit

**Task:** Write a commit message that passes fleet standards.

Given this scenario: You fixed a broken link in the README that pointed to `docs/old-file.md` when it should point to `docs/04-your-first-task.md`.

Write a commit message that includes:
1. A type prefix
2. A short description (under 72 characters)
3. An optional body explaining why

**Validation:**
- [ ] Commit message starts with a valid conventional type
- [ ] Description is under 72 characters
- [ ] Message clearly explains what changed and why
- [ ] No typos or unclear language

**Hint:** `docs: fix README link to point to correct task doc` is a good example. Short, clear, explains the what and the where.

---

### Exercise 2.4: Open a Pull Request

**Task:** Create a PR from your branch following fleet PR standards.

1. Push your branch: `git push -u origin {your-name}/fix-readme-links`
2. Create a PR: `gh pr create --title "docs: fix README link" --body "..." `
3. Include in the body: what changed, why, and how to verify

**Validation:**
- [ ] PR title uses conventional format
- [ ] PR body has at least 3 sections: What, Why, How to Verify
- [ ] PR is created from your fork to the upstream repo
- [ ] CI checks run (even if they're simple)

**Hint:** A good PR body follows the fleet's "3-sentence rule": What did you change? Why did you change it? How can someone verify it works?

---

### Exercise 2.5: Handle Feedback

**Task:** Respond to a mock PR review scenario.

You receive this review comment on your PR:

> "The link you fixed points to the right file, but the anchor `#finding-your-first-task` doesn't exist on that page. Can you update the link to just point to the file without the anchor, or find the correct anchor?"

1. Write your response to the reviewer
2. Describe the git commands you would use to update the PR
3. Explain why responding to reviews is important for fleet trust

**Validation:**
- [ ] Response is polite and acknowledges the feedback
- [ ] Git commands are correct (amend or new commit)
- [ ] Explanation connects review responsiveness to fleet trust model

**Hint:** In the fleet, reviews build trust. Every review you handle well raises your trust score. Ignore reviews and the fleet stops reviewing your work.

---

## Level Complete

When all five exercises are validated, you've earned:

- Badge: **Git Sailor** (Bronze)
- Stage unlocked: Greenhorn active, Hand path opened
- Next level: Level 3 - Bytecode Builder

*Branches are work lanes. Stay in your lane. Merge when ready.*
