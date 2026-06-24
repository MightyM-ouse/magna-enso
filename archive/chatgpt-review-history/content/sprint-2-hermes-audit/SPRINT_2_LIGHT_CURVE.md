# Sprint 2 Light Curve

## Purpose

Record the Sprint 2 Hermes read-only audit evidence package and governance status.

Format note: This Sprint 2 Light Curve uses an audit-specific structure rather than the exact `EVIDENCE_TEMPLATE.md` section layout. Required evidence content is present under Task Metadata, Source Audited, Files And Reports Created, Governance Gates, Validation Results, What Was Not Done, Risks, Open Questions, and Recommendation.

## Task Metadata

- Task ID: `ENSO-F-0201`
- Sprint: Sprint 2
- Mode: Read-only audit
- Status: `IN_REVIEW`
- Human acceptance: Pending
- Primary worker: Codex primary code inspector
- Recommended next worker: Antigravity validation
- Hermes Agent use: Not used

## Source Audited

- Hermes repo URL: `https://github.com/nousresearch/hermes-agent`
- Clone path: `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/`
- Audited branch: `main`
- Audited commit SHA: `33b1d144590a211100f42aa911fd7f91ba031507`
- Clone timestamp: `2026-06-17T18:58:13Z` clone initiated

## Files And Reports Created

Reports created under `<CHATGPT_REVIEW_SOURCE>/sprint-2-hermes-audit/`:

- `HERMES_PROVENANCE.md`
- `LICENSE_AND_DEPENDENCY_REVIEW.md`
- `HERMES_CODE_MAP.md`
- `ACTION_DISPATCH_MAP.md`
- `AUTONOMY_ENTRY_POINT_MAP.md`
- `EXTERNAL_SURFACE_MAP.md`
- `CAPABILITY_GATING_FEASIBILITY.md`
- `MAGNA_ENSO_REUSE_RECOMMENDATION.md`
- `SPRINT_2_LIGHT_CURVE.md`

## Governance Gates

- Sprint 2 was executed as read-only source investigation.
- Hermes source was cloned only into the approved scratch path.
- Reports were written only into the approved local reports folder.
- No Hermes source was copied into `magna-enso/`.
- No `magna-enso/docs/audit/` folder was created.
- No implementation, fork, commit, push, branch, build, dependency install, or Hermes runtime activation was performed.
- EH-0005B remains `PROPOSED`.

## Findings Summary

- Hermes has a modular agent architecture with a core loop, tool registry, toolsets, provider adapters, gateway surfaces, scheduler, memory, skills, terminal/code execution, browser tooling, and plugin/MCP extension points.
- Hermes includes useful governance primitives, especially terminal/code approval and memory/skill write staging.
- Hermes does not currently have one complete policy chokepoint.
- High-risk surfaces include background self-improvement, scheduled execution, direct script cron jobs, messaging gateways, API listeners, cloud providers, browser actions, remote execution backends, external memory, subagents, and dynamic MCP/plugin loading.
- Reuse recommendation is `CONDITIONALLY SUITABLE`, not direct adoption.

## Validation Results

- Hermes clone exists at the approved path: `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/`.
- Hermes clone Git status is clean.
- No Hermes directories or `docs/audit/` directory were found inside `<MAGNA_LOCAL_ROOT>/magna-enso/` at max depth 3.
- `magna-enso/` Git status is clean.
- `magna-enso/` remains on branch `main`.
- `magna-enso/` HEAD remains `e0a28d4a0d50e5107392ae6bacfbdec52080487e`.
- Reports folder contains only Markdown report files.
- Reports folder contains the nine required reports.
- `trace/DECISION_LOG.md` still records `EH-0005B` as `PROPOSED`.
- No commit or push was performed.
- Hermes was not run or built.

## What Was Not Done

- Hermes was not run.
- Hermes was not built.
- Dependencies were not installed.
- Hermes source was not modified.
- Magna Enso source was not modified.
- No Hermes source was copied into Magna Enso.
- No fork was created.
- No branch was created.
- No commit was created.
- No push was performed.
- Sprint 3 was not started.
- Sprint 4 was not started.
- Hermes Agent was not activated.
- EH-0005B was not promoted.

## Confidence Level

Medium-high. The audit inspected primary architecture, dispatch, autonomy, external surface, license, and dependency evidence. Full plugin-by-plugin threat modeling remains open for validation.

## Risks

- A future audit is required if Sprint 4 uses a different Hermes commit.
- Independent validation should verify that no source path or autonomous entry point was missed.

## Open Questions

- Should the Sprint 4 fork remove risky modules or retain them disabled?
- Should all plugin/MCP loading be removed until a signed allowlist exists?
- Should Antigravity perform an independent dependency/SBOM scan?

## Recommendation

Keep Sprint 2 in `IN_REVIEW` pending human acceptance and Antigravity validation. Do not start implementation or fork work until governance design is approved.
