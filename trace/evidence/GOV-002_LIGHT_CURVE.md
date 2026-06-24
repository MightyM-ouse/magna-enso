# GOV-002 Light Curve

## Status

`ACCEPTED_COMPLETE`

## Scope

Documentation-only replacement of redundant ChatGPT project-source instructions with a
thin GitHub-first bootstrap and concise response contract.

## Source audit

| Legacy source | Finding | Disposition |
|---|---|---|
| Existing `SKILL.md` | Unrelated generic frontend-design skill | Replaced |
| Agent-output usage prompt | Duplicated review instructions | Superseded |
| Agent-output review template | Rigid and percentage-heavy; duplicated TRACE review | Superseded |
| Mentor-template README | Described the legacy bundle only | Replaced |
| Prompt response format | Required oversized pasted prompts and stale local paths | Superseded |
| Mentor operating model | Useful role/teaching rules already governed in GitHub | Consolidated |
| Review/next-step format | Duplicated evidence and review rules; forced long output | Consolidated |

Useful principles retained: Product Owner authority, senior-architect mentoring, evidence
discipline, no invented state, worker boundaries, practical learning, and analogy-based
explanation.

## Implemented artifacts

- `docs/governance/chatgpt-project-source/SKILL.md`
- `docs/governance/chatgpt-project-source/PROJECT_BOOTSTRAP.md`
- `docs/governance/chatgpt-project-source/RESPONSE_CONTRACT.md`
- `docs/governance/chatgpt-project-source/README.md`
- Matching external upload ZIP generated from those four files

## Validation

| Check | Result |
|---|---|
| `trace/CELESTIAL_INDEX.json` parse | PASS |
| GitHub-source files vs upload-package files | PASS - 4/4 byte-identical |
| Package file count | PASS - 4 files plus one directory entry |
| ZIP integrity | PASS - no CRC errors |
| ZIP hygiene | PASS - no macOS metadata or unexpected files |
| Allowed-path branch diff | PASS - 10/10 files within GOV-002 scope |
| GitHub Governance validation | PASS - workflow run 7 |
| Legacy/stale active references in package | PASS - none |
| SHA-256 | `73eef1a8ae93869ced186e4345292a45218351f0566102a842335257288a4bad` |
| Fresh-conversation Product Owner validation | PASS - 2026-06-24 |

## Acceptance evidence

- Product Owner confirmed the four replacement files were active.
- Product Owner confirmed the seven legacy files were removed.
- The four validation questions produced acceptable GitHub-first responses.
- PR #5 was squash-merged as `af8c73a1ccd4478d09dd9e52ef424d7ecf1bc769`.
- Issue #4 closed as completed.
- The task branch was deleted after merge.

## Residual risk

No GOV-002 delivery risk remains. Future changes to project-source behavior must use a new
governed task and preserve GitHub as the canonical changing source.

## Verdict

`ACCEPTED_COMPLETE`
