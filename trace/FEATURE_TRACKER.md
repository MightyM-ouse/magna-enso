# FEATURE_TRACKER.md — Magna Enso

> Repository-native historical feature tracker. Existing accepted rows remain evidence; future planned rows are provisional until reconciled with the accepted architecture and Product Owner backlog.
> Status: `PLANNED · IN_DESIGN · IN_PROGRESS · IN_REVIEW · BLOCKED · DONE · DEFERRED`
> (Honest-status rule: never mark `DONE` without a human-approved Light Curve.)

## Master Tracker

| Feature ID | Release | Sprint | Feature | Status | Owner | Reviewer | Risk | Evidence |
|---|---|---|---|---|---|---|---|---|
| ENSO-F-0101 | v1.0-enso | 1 | TRACE skeleton + AGENTS.md entry point | DONE | Claude+Codex | Antigravity + Human | LOW | Light |
| ENSO-F-0201 | v1.0-enso | 2 | Hermes read-only audit report | DONE | Codex | Antigravity + Human | MEDIUM | Full |
| ENSO-F-0301 | v1.0-enso | 3 | Capability governance design (taxonomy + policy schema + models) | DONE | Claude | Antigravity + Human | HIGH | Full |
| ENSO-F-0401 | v1.0-enso | 4 | Clean governed Hermes baseline preparation | DONE | Codex | Antigravity + Human | HIGH | Full |
| ENSO-F-0501 | v1.0-enso | 5 | Default-deny capability gate | PLANNED | Codex | Antigravity + Human | HIGH | Full |
| ENSO-F-0502 | v1.0-enso | 5 | Approval-request flow + logging | PLANNED | Codex | Antigravity + Human | HIGH | Full |
| ENSO-F-0601 | v1.0-enso | 6 | Magna Enso identity + version stamp | PLANNED | Codex | Human | LOW | Light |
| ENSO-F-0701 | v1.0-enso | 7 | Profiles + Galaxy Catalog wiring | PLANNED | Claude+Codex | Human | MEDIUM | Standard |
| ENSO-F-0801 | v1.0-enso | 8 | Memory-write approval + change log | PLANNED | Codex | Antigravity + Human | HIGH | Full |
| ENSO-F-0802 | v1.0-enso | 8 | Skill registry + activation gate | PLANNED | Codex | Antigravity + Human | HIGH | Full |
| ENSO-F-0901 | v1.0-enso | 9 | Report-only scheduler | PLANNED | Codex | Antigravity + Human | MEDIUM | Standard |
| ENSO-F-1001 | v1.0-enso | 10 | LAN-bound mobile control | PLANNED | Codex | Antigravity + Human | HIGH | Full |
| ENSO-F-1101 | v1.0-enso | 11 | Remote instruction package importer | PLANNED | Codex | Antigravity + Human | HIGH | Full |
| ENSO-F-1201 | v1.0-enso | 12 | Local execution capture + redaction | PLANNED | Codex | Antigravity + Human | MEDIUM | Standard |
| ENSO-F-1301 | v1.0-enso | 13 | Capability Control UI (Observatory) | PLANNED | Codex | Human | MEDIUM | Full |
| ENSO-F-1401 | v1.0-enso | 14 | Review-package generator + completeness score | PLANNED | Claude | Antigravity + Human | MEDIUM | Standard |
| ENSO-F-1501 | v1.0-enso | 15 | Governance audit + RC tag | PLANNED | All | Human | HIGH | Full |

## Active feature detail

### ENSO-F-0101 — TRACE skeleton + AGENTS.md entry point
- Release: v1.0-enso · Sprint: 1 · Status: **DONE** (human-approved 2026-06-17)
- Owner: Claude + Codex · Reviewer: Antigravity + Human owner · Risk: LOW
- Description: Establish the `magna-enso/` TRACE operating instance and project-entry files. No runtime code.
- Acceptance Criteria:
  - [x] `AGENTS.md` entry point + thin bridges (`CLAUDE.md`, `CODEX.md`, `ANTIGRAVITY.md`) exist.
  - [x] `trace/` instance complete: config, onboarding, status, context index, roles, workflows,
        task-packet & evidence templates, decision log, feature tracker, risk register, validation checklist, `evidence/`.
  - [x] Artifacts consistent with frozen Sprint 0 decisions (EH-0001…EH-0011).
  - [x] Human owner reviewed and **approved** the skeleton (2026-06-17). Antigravity recommended
        acceptance (9.2/10 review, no blocking issues); human owner is final authority (EH-0010).
- Evidence Required: Light Curve (Light) — delivered as `trace/evidence/ENSO-0001_LIGHT_CURVE.md` (human-approved).
- Linked Decisions: EH-0006, EH-0007, EH-0011 · Linked Risks: R-13 (overengineering — keep skeleton lean).

### ENSO-F-0201 — Hermes read-only audit report
- Release: v1.0-enso · Sprint: 2 · Status: **DONE** (human-approved 2026-06-17)
- Owner: Codex · Reviewer: Antigravity + Human owner · Risk: MEDIUM
- Description: Read-only source audit of `nousresearch/hermes-agent` to determine whether Hermes is suitable as a future Sprint 4 clean governed fork baseline candidate. No implementation, fork, build, run, activation, dependency install, or Hermes source copy.
- Audited Hermes SHA: `33b1d144590a211100f42aa911fd7f91ba031507`
- Acceptance Criteria:
  - [x] Codex read-only audit completed in approved scratch workspace.
  - [x] Antigravity validation completed with no blocking issues.
  - [x] Light Curve format correction completed.
  - [x] Autonomy count correction completed.
  - [x] Hermes assessed as **conditionally suitable only** for future governed fork consideration.
  - [x] Hermes remains **not approved** for direct adoption, activation, build, run, fork, or implementation.
  - [x] EH-0005B remains **PROPOSED**.
  - [x] Sprint 3 and Sprint 4 remain **NOT STARTED**.
- Evidence Required: Light Curve (Full audit closeout) — delivered as `trace/evidence/ENSO-0002_LIGHT_CURVE.md` (human-approved). Detailed audit and validation reports remain local-only under `../../ChatGPTReview/`.
- Linked Decisions: EH-0005A, EH-0013 · Linked Risks: R-01, R-02, R-06.

### ENSO-F-0301 — Capability governance design (taxonomy + policy schema + models)
- Release: v1.0-enso · Sprint: 3 · Status: **DONE** (human-approved 2026-06-17, **design/report-only**)
- Owner: Claude · Reviewer: Antigravity + Human owner · Risk: HIGH
- Description: Design-only capability-governance model defining how Magna Enso will control Hermes-derived capabilities under default-deny, before any Sprint 4 fork. No implementation, no runtime code, no policy-engine code, no Hermes fork/build/run/modification.
- Acceptance Criteria:
  - [x] 17 design reports produced (taxonomy, policy schema, default-deny, disablement tiers, unified approval engine, chokepoint map, memory/skill draft-only, scheduler report-only, browser/web read-only, terminal/code approval-required, messaging/cloud disabled, plugin/MCP governance, delegation control, surface matrix, Sprint 4 readiness gates, Light Curve, final recommendation).
  - [x] Antigravity validation completed (verdict ACCEPTED_FOR_HUMAN_REVIEW).
  - [x] RC-01 through RC-05 corrections applied.
  - [x] Human owner accepted Sprint 3 as **design/report-only** (2026-06-17); no implementation approved.
  - [x] EH-0005B remains **PROPOSED**; Hermes Agent not activated.
  - [x] Sprint 4 remains **blocked / NOT STARTED**; requires a separate approval package.
- Evidence Required: Light Curve (Full) — delivered as `trace/evidence/ENSO-0003_LIGHT_CURVE.md` (human-approved). Design and validation reports remain local-only under `../../ChatGPTReview/sprint-3-capability-governance-design/` and `../../ChatGPTReview/sprint-3-antigravity-validation/`.
- Linked Decisions: EH-0014 · Linked Risks: R-04, R-05, R-06, R-07, R-08, R-09, R-10.

### ENSO-F-0401 — Clean governed Hermes baseline preparation
- Release: v1.0-enso · Sprint: 4 · Status: **DONE** (human-approved 2026-06-20; inert baseline only)
- Owner: Codex · Reviewer: Antigravity + Human owner · Risk: HIGH
- Description: Bounded, selective, inert Hermes-derived vendor baseline preparation from audited SHA `33b1d144590a211100f42aa911fd7f91ba031507`. No runtime activation, no Hermes run/build, no dependency install, no policy-engine implementation, no Sprint 5 work.
- Acceptance Criteria:
  - [x] Isolated branch used: `audit/sprint-4-governed-hermes-baseline`.
  - [x] Pre-implementation report created local-only.
  - [x] Static license/dependency review completed before import.
  - [x] Inert vendor baseline created under `vendor/hermes/`.
  - [x] Dangerous Hermes runtime surfaces excluded by non-import.
  - [x] Local-only Sprint 4 reports created.
  - [x] EH-0005B remains **PROPOSED**; Hermes Agent not activated.
  - [x] Sprint 5 not started.
  - [x] Antigravity validation completed with verdict **ACCEPTED_FOR_HUMAN_REVIEW**, 9.8/10, no blocking issues, and no required corrections.
  - [x] Human owner accepted Sprint 4 on 2026-06-20.
- Evidence Required: Light Curve (Full) — delivered as `trace/evidence/ENSO-0004_LIGHT_CURVE.md` (human-approved). Local reports remain under `../../ChatGPTReview/sprint-4-governed-hermes-baseline/` and `../../ChatGPTReview/sprint-4-antigravity-validation/`.
- Linked Decisions: EH-0014, EH-0015 · Linked Risks: R-01, R-02, R-04, R-05, R-06, R-11, R-13.
