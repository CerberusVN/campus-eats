# AGENTS.md — rules for members and AI agents

## File owners
| Module | Folder | Owner |
|--------|--------|-------|
| ACC    | acc/   | An    |
| MENU   | menu/  | Minh  |
| ORD    | ord/   | Hà    |

## Rules
1. Every change is made on a branch named member-name/short-topic, never on main.
2. The diff is read by a person before every commit.
3. Only files in the requested scope are changed; other files are restored with git restore.
4. Never commit .env, secrets, real personal data or hand-edited seed files.
5. Commits containing agent-generated work are recorded in docs/ai-use-log.md.
6. Agents never run: git push --force, git reset --hard, git tag -d.

Commit message: <MODULE> <FR-ID>: <what changed and why>
