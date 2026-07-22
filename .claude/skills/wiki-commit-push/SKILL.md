---
name: wiki-commit-push
description: "Commit and push wiki changes after a /pin-llm-wiki ingest/refresh/lint/remove, using the commit message that pin-llm-wiki suggested. Invoke with /wiki-commit-push"
trigger: "/wiki-commit-push"
---

# /wiki-commit-push

Commits and pushes changes in this repo (agentic-ai-wiki) using the suggested
commit message from a `/pin-llm-wiki` subcommand (`ingest`, `refresh`, `lint`,
`remove`, etc.), without spending tokens re-deriving git/gh commands each time.

`pin-llm-wiki`'s own policy is to never commit or push — it only prints a
suggested message, e.g. `ingest: <slug>` or `refresh: <slug>` (see
`ingest.md`). This skill is the human-invoked follow-up step that acts on
that suggestion.

## When to use

- The human just ran a `/pin-llm-wiki` subcommand that printed a suggested
  commit message, and now asks to commit/push (or says "yes, commit that").
- The human explicitly asks to commit and push wiki changes, and a commit
  message is available (from a prior suggestion or given directly).

Never invoke this on your own initiative — only when the human has explicitly
asked to commit/push in this conversation. This matches the repo's `AGENTS.md`
git policy.

## What it does

Runs `scripts/commit_push.sh "<message>"`, which:

1. `git add -A` and stages everything in the wiki repo.
2. `git commit -m "<message>"`.
3. Checks `gh auth status`; if the active account isn't `ndjordjevic`, runs
   `gh auth switch -u ndjordjevic` first (per `AGENTS.md` push policy).
4. `git push origin HEAD`.

## Usage

Pass the exact commit message suggested by pin-llm-wiki (or given by the
human) as the single argument:

```bash
.claude/skills/wiki-commit-push/scripts/commit_push.sh "ingest: openai-symphony"
```

If the working tree is clean, the script exits with an error and does
nothing. If the push fails with a 403 for the wrong user, the script has
already attempted the account switch — investigate rather than retrying
blindly.

## Notes

- Do not fabricate a commit message. If none was suggested and the human
  didn't provide one, ask, or derive a `type: slug` message consistent with
  recent `git log` entries (e.g. `ingest: <slug>`, `refresh: <slug>`,
  `lint: fix <slug>`, `remove: <slug>`).
- This skill only handles committing/pushing. It does not run ingest, lint,
  or any other wiki-content step — that's `/pin-llm-wiki`'s job.
