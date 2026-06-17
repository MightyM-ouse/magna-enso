# FEATURE_TRACKER.md — Magna Enso

> The durable, repository-native feature source of truth. Template & field definitions:
> `../planning/MAGNA_ENSO_FEATURE_TRACKER_TEMPLATE.md`.
> Status: `PLANNED · IN_DESIGN · IN_PROGRESS · IN_REVIEW · BLOCKED · DONE · DEFERRED`
> (Honest-status rule: never mark `DONE` without a human-approved Light Curve.)

## Master Tracker

| Feature ID | Release | Sprint | Feature | Status | Owner | Reviewer | Risk | Evidence |
|---|---|---|---|---|---|---|---|---|
| ENSO-F-0101 | v1.0-enso | 1 | TRACE skeleton + AGENTS.md entry point | DONE | Claude+Codex | Antigravity + Human | LOW | Light |
| ENSO-F-0201 | v1.0-enso | 2 | Hermes read-only audit report | PLANNED | Codex | Grok + Human | MEDIUM | Full |
| ENSO-F-0301 | v1.0-enso | 3 | Capability taxonomy + policy schema | PLANNED | Claude | Antigravity + Human | HIGH | Full |
| ENSO-F-0401 | v1.0-enso | 4 | Clean governed Hermes fork boot baseline | PLANNED | Codex | Antigravity + Human | HIGH | Full |
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
