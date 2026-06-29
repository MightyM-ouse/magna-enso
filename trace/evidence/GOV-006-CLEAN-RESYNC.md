# GOV-006 Clean Resynchronization Evidence

Status: `CLEAN_BRANCH_CREATED`

## Reason

The original GOV-006 PR was stacked on `codex/GOV-005-multi-agent-governance`. After GOV-005 was squash-merged into `main`, the old GOV-006 branch appeared divergent and included historical GOV-005 branch content in comparison views.

## Action

A fresh branch was created from current `main`:

`chatgpt/GOV-006-clean-main`

Only the confirmed GOV-006 files from the original PR were reapplied.

## Reapplied files

- `docs/governance/AGENT_ROUTING_AND_DISPATCH.md`
- `docs/governance/chatgpt-project-source/RESPONSE_CONTRACT.md`
- `docs/governance/chatgpt-project-source/RESPONSE_TEMPLATES.md`
- `scripts/validate_agent_routing_and_responses.py`
- `trace/AGENT_ROUTING_MATRIX.yaml`
- `trace/evidence/GOV-006_LIGHT_CURVE.md`
- `trace/tasks/GOV-006.md`

## Verification

Compare against `main` shows the branch is ahead only by GOV-006 routing/response files and behind by zero commits.

No runtime, product behavior, Hermes activation, Sprint 5, HELIX, SGN-01, or old GOV-005 correction artifacts were carried into the clean branch.
