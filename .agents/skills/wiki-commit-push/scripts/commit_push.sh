#!/usr/bin/env bash
# Commit and push wiki changes using the ndjordjevic GitHub account.
# Usage: commit_push.sh "<commit message>"
set -euo pipefail

if [ $# -lt 1 ] || [ -z "$1" ]; then
  echo "Usage: $0 \"<commit message>\"" >&2
  exit 1
fi

MSG="$1"
REQUIRED_ACCOUNT="ndjordjevic"

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

if [ -z "$(git status --porcelain)" ]; then
  echo "Nothing to commit — working tree is clean." >&2
  exit 1
fi

git add -A
git status --porcelain

git commit -m "$MSG"

ACTIVE_ACCOUNT="$(gh auth status 2>&1 | grep -o "account [A-Za-z0-9_-]*" | head -1 | awk '{print $2}')"

if [ "$ACTIVE_ACCOUNT" != "$REQUIRED_ACCOUNT" ]; then
  echo "Active gh account is '$ACTIVE_ACCOUNT', switching to '$REQUIRED_ACCOUNT'..." >&2
  gh auth switch -u "$REQUIRED_ACCOUNT"
fi

git push origin HEAD

echo "Committed and pushed as $REQUIRED_ACCOUNT: $MSG"
