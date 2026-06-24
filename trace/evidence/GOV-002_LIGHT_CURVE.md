# GOV-002 Light Curve

## Status

`IMPLEMENTED_AWAITING_REVIEW`

## Scope

Documentation-only replacement of redundant ChatGPT project-source instructions with a
thin GitHub-first bootstrap and concise response contract.

## Source audit

| Legacy source | Finding | Disposition |
|---|---|---|
| Existing `SKILL.md` | Unrelated generic frontend-design skill | Replace |
| Agent-output usage prompt | Duplicates review instructions | Supersede |
| Agent-output review template | Rigid and percentage-heavy; duplicates TRACE review | Supersede |
| Mentor-template README | Describes the legacy bundle only | Replace |
| Prompt response format | Requires oversized pasted prompts and stale local paths | Supersede |
| Mentor operating model | Useful role/teaching rules already governed in GitHub | Consolidate |
| Review/next-step format | Duplicates evidence and review rules; forces long output | Consolidate |

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
| GitHub-source files vs upload-package files | 4/4 byte-identical |
| Package file count | 4 files plus one directory entry |
| ZIP integrity | PASS; no CRC errors |
| ZIP hygiene | PASS; no macOS metadata or unexpected files |
| Legacy/stale active references in package | None; `frontend-design` appears only in removal guidance |
| SHA-256 | `73eef1a8ae93869ced186e4345292a45218351f0566102a842335257288a4bad` |

Repository Gitleaks, allowed-path diff, and governance CI results remain pending until the
GitHub branch and pull request are complete.

## Limitations

- The Product Owner must upload the package because ChatGPT project-source administration
  is outside repository automation.
- Legacy files are not deleted before replacement validation.

## Recommendation

`REVIEW_AFTER_VALIDATION`
