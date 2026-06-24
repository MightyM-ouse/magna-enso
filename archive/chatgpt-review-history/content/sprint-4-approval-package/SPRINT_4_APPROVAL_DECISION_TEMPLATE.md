# SPRINT_4_APPROVAL_DECISION_TEMPLATE.md
# Magna Enso — Sprint 4 Approval Decision Template
# Type: Local-only approval package
# Date: 2026-06-17
# Status: READY FOR HUMAN OWNER. Fill in; Sprint 4 begins only within these bounds, if approved.

---

## 1. Top-level decision

| Option | Meaning | Choose |
|---|---|---|
| **Approve — baseline preparation only** | Start Sprint 4 as a clean governed baseline prep sprint (no runtime) | ☐ |
| **Approve with corrections** | Approve, but apply listed corrections first | ☐ |
| **Defer Sprint 4** | Do the transitive license/dependency review first (Option D), then revisit | ☐ |
| **Reject Sprint 4** | Do not proceed now | ☐ |
| **Keep Hermes reference-only** | Option A — no import; read-only references only | ☐ |

Corrections (if "approve with corrections"): ________________________________________

## 2. Sub-decisions (if approving)

| # | Decision | Recommendation | Your choice |
|---|---|---|---|
| 1 | Baseline strategy option | **C — selective vendor import of retained modules** | ☐ A ☐ B ☐ C ☐ D |
| 2 | Import mechanism | **Selective vendor import** (provenance-tracked) | ☐ vendor ☐ patch-based ☐ other |
| 3 | License/SBOM timing | **Mandatory pre-import gate** — static review before any source is committed; STOP on incompatible/unclear | ☐ pre-import gate ☐ before-approval (defer) |
| 4 | Source SHA | **`33b1d144590a211100f42aa911fd7f91ba031507`** (Sprint 2 audited) | ☐ confirm ☐ other: ____ |
| 5 | Target area (if approved) | `magna-enso/vendor/hermes/` (isolated) | ☐ approve ☐ other: ____ |
| 6 | Executor | **Codex** (executes import/removal) | ☐ Codex ☐ Claude ☐ other |
| 7 | Governance/review | **Claude** governs; **Antigravity** validates after execution | ☐ yes ☐ amend |
| 8 | Grok second opinion | **Yes** (challenge isolation + removal completeness) | ☐ yes ☐ no |
| 9 | Commit/push | **No commit/push without separate human approval** | ☐ confirm ☐ amend |
| 10 | Remove vs disable matrix | **Approve as proposed** | ☐ approve ☐ amend |

## 3. Ready-to-sign approval block

```text
I approve Sprint 4 — Clean Governed Hermes Fork Baseline — as BASELINE PREPARATION ONLY.

Approved scope:
- Baseline strategy: Option C (selective vendor import of retained modules only)
- Source: github.com/nousresearch/hermes-agent @ 33b1d144590a211100f42aa911fd7f91ba031507
- Target (isolated): magna-enso/vendor/hermes/
- Import ONLY retained modules (allowlist); remove dangerous surfaces; disable the rest per the matrix
- Imported source is INERT/QUARANTINED: not wired into runtime, not imported by app code, not exposed via
  CLI/UI, not executable, not registered as tools, not package-discovered as active code
- Preserve MIT license + provenance manifest + file inventory
- License/SBOM is a MANDATORY PRE-IMPORT GATE: static review before any source is committed; no Hermes
  run/build; no runtime dependency install unless separately approved; incompatible/unclear = STOP
- No-network static validation required
- Work in an ISOLATED branch or approved baseline path; do NOT directly mutate main without review
- Executor: Codex; Governance: Claude; Validation: Antigravity; Second opinion: Grok

This approval DOES NOT authorize:
- runtime execution or production use
- policy engine implementation (Sprint 5)
- autonomous operation
- cloud / messaging / plugin-MCP / remote-backend activation
- enabling retained risky capabilities (terminal/code stay disabled)
- EH-0005B promotion or Hermes Agent activation
- Sprint 5 work
- commit or push without separate explicit approval

Stop after the Sprint 4 baseline reports + Antigravity validation; pause for my acceptance.

Approved by (human owner): ____________________
Date: ____________________
```

## 4. What approval explicitly does NOT authorize (restated)

Runtime execution · production use · policy-engine implementation · autonomous operation ·
cloud/messaging/plugin activation · EH-0005B promotion · Hermes Agent activation · Sprint 5 · commit/push.

## 5. If you do not approve

Nothing happens. Baseline stays at `966629a`; Hermes stays un-forked / reference-only; Sprint 4 remains blocked.
