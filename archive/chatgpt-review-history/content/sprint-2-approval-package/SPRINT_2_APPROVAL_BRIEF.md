# SPRINT_2_APPROVAL_BRIEF.md
# Magna Enso — Sprint 2 Approval Brief
# Type: Local-only approval package (planning / approval-preparation)
# Prepared by: Claude (architecture / governance)
# Date: 2026-06-17
# Status: FOR HUMAN APPROVAL. Sprint 2 NOT started. No Hermes clone. No commits.

---

## 1. One-paragraph summary

Sprint 2 is a **read-only audit** of the Hermes codebase to decide whether it is a sound technical
base for the Magna Enso runtime (the Sprint 4 "clean governed Hermes fork baseline"). It produces
**reports only** — no code, no fork, no integration. This brief, plus the nine companion documents in
this folder, is what the human owner reviews to approve (or amend) Sprint 2. Nothing in Sprint 2 runs
until that approval is given.

## 2. Where we are (baseline)

| Item | State |
|---|---|
| Sprint 1 | Accepted; `ENSO-F-0101` DONE; `ENSO-0001_LIGHT_CURVE.md` exists |
| Git | Initialized at `magna-enso/`, branch `main`, first commit `e0a28d4` |
| Remotes | None (no push possible) |
| Hermes | **Not cloned**; no Hermes source anywhere |
| HELIX repo | Untouched |
| ChatGPTReview/ | Local-only, outside Git |
| EH-0005B | PROPOSED (Hermes Agent = candidate UI/E2E worker, not promoted) |

## 3. What this package contains

| # | File | Purpose |
|---|---|---|
| 1 | `SPRINT_2_APPROVAL_BRIEF.md` | This overview |
| 2 | `SPRINT_2_SCOPE_AND_BOUNDARIES.md` | What Sprint 2 is / is not |
| 3 | `SPRINT_2_LEARNING_BRIEF.md` | The professional-delivery concepts being taught |
| 4 | `HERMES_AUDIT_PLAN.md` | The 14 audit questions and how to answer them |
| 5 | `SCRATCH_WORKSPACE_RECOMMENDATION.md` | Where the read-only clone lives |
| 6 | `WORKER_ASSIGNMENT_RECOMMENDATION.md` | Who does what |
| 7 | `SPRINT_2_OUTPUT_REPORTS_SPEC.md` | The reports Sprint 2 will produce |
| 8 | `SPRINT_2_RISK_AND_GOVERNANCE_CHECKLIST.md` | Gates that must hold |
| 9 | `SPRINT_2_APPROVAL_DECISION_TEMPLATE.md` | The 10 decisions + ready-to-sign approval block |
| 10 | `FINAL_RECOMMENDATION.md` | The consolidated recommendation |

## 4. Headline recommendation

**Proceed to Sprint 2 — but only as a read-only audit, in a separate scratch workspace, after you sign
the approval block.** Recommended specifics:

- **Start Sprint 2:** Yes (it de-risks the Sprint 4 fork decision before any code is written).
- **Scratch workspace:** `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/` (outside both repos).
- **Audit branch:** Defer — Sprint 2 needs no branch; reports stay local first (see Decision 3 & 8).
- **Inspector:** **Codex** (code map) with **Antigravity** (safety/validation) and **Claude** (governance interpretation); **ChatGPT** continuity. **Hermes Agent stays candidate and does NOT perform the audit.**
- **Remote:** keep unconfigured. **No commit / no push** remain mandatory.
- **License verification:** mandatory before Sprint 4.
- **Antigravity validates** Sprint 2 output before acceptance; human owner is final authority.

## 5. Why now

Auditing before forking is standard professional practice: you do not adopt a dependency as your base
without first mapping its architecture, provenance, license, and risk surface. Sprint 2 produces exactly
the evidence needed to make the Sprint 3 governance design and the Sprint 4 fork decision **informed
rather than blind** — at zero risk to the `magna-enso/` baseline, because it touches nothing inside it.

## 6. What approval does NOT authorize

Approving Sprint 2 does **not** authorize: forking, copying Hermes into `magna-enso/`, runtime code,
integrations, Sprint 3/4 work, promoting EH-0005B, or activating Hermes Agent. Those remain separately gated.
