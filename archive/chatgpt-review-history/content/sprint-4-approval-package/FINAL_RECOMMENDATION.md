# FINAL_RECOMMENDATION.md
# Magna Enso — Sprint 4 Approval Package — Final Recommendation
# Type: Local-only approval package
# Prepared by: Claude (architecture / governance)
# Date: 2026-06-17
# Status: RECOMMENDATION for human owner. Sprint 4 NOT started. No fork/copy/run. No commits.

---

> **Terminology note (C-01).** "Clean governed Hermes fork baseline" is the **historical sprint name**. The
> recommended implementation is a **Hermes-derived governed baseline through selective vendor import**
> (Option C) — not a full fork.

## 1. Recommendation

```
RECOMMENDATION

  Approve Sprint 4:   YES — as CLEAN GOVERNED BASELINE PREPARATION ONLY, after you sign the approval block.
  Baseline option:    C — selective vendor import of retained modules only (provenance-tracked).
  Mechanism:          selective vendor import (patch-based as secondary).
  License/SBOM:        MANDATORY PRE-IMPORT GATE — static review before any imported source is committed;
                       no Hermes run/build; no runtime dep install unless separately approved;
                       incompatible license OR unclear dependency status = STOP (resolves R-02 before commit).
  Source:             github.com/nousresearch/hermes-agent @ 33b1d144 (Sprint 2 audited SHA).
  Remove:             background self-improvement, direct-script cron, messaging+outbound, external memory sync,
                      plugin/MCP dynamic loader, remote execution backends, API listeners.
  Disable:            curator (report-only), scheduler execution (report-only), cloud providers, delegation,
                      browser actions, terminal/code (retained but OFF), file transfer.
  Retain (off/limited): local safe-status (active_safe), sensitive read (read_only), memory/skill (draft_only),
                      scheduler metadata (report_only), browser snapshot (read_only if privacy-gated),
                      terminal/code (approval_required but DISABLED until Sprint 5).
  Quarantine:         Imported source is INERT — not wired/imported/exposed/executable/tool-registered/
                       package-discovered. Present as governed reference only.
  Isolation:          Run in an ISOLATED branch or approved baseline path; no direct mutation of main
                       without review; no auto-commit/push/force-push.
  Enforcement:        NONE in Sprint 4 — structurally safe, not runtime-enforced; engine is Sprint 5.
  Executor:           Codex.   Governance: Claude.   Validation: Antigravity (mandatory).   2nd opinion: Grok.
  Confidence:         High      Blocking issues: None (license/SBOM handled as precondition).

  Alternative if you prefer maximum caution: DEFER (Option D) — full transitive license/dependency review first.
```

## 2. Why approve (under Option C)

It is the natural next step after an accepted governance design, and Option C is the safest way to take it:
import only the danger-stripped allowlist, with provenance and license preserved, never touching the removed
surfaces. The baseline makes real progress toward a runtime base while remaining **incapable of acting**
(nothing wired to run; terminal/code off; no network). Risk is bounded by *absence* and *off-state*, not by a
not-yet-existing gate.

## 3. Why it is safe

- Option C imports the **allowlist**, not the denylist — dangerous surfaces never enter.
- Provenance + inventory + license/SBOM + no-network validation are mandatory outputs.
- Retained risky capabilities stay **disabled**; no runtime, no enforcement claim.
- Separation of duties (Codex executes, Antigravity validates, human decides); EH-0005B untouched.

## 4. Key approval decisions required (summary)

Full form in `SPRINT_4_APPROVAL_DECISION_TEMPLATE.md`: approve/defer/reject; baseline **Option C**; import
mechanism; **license/SBOM as precondition**; confirm SHA `33b1d144`; target `vendor/hermes/`; Codex executes,
Antigravity validates, Grok second opinion; **no commit/push** without separate approval; approve the
remove/disable matrix.

## 5. Key risks

Accidental Hermes activation (S4-R1), incomplete source isolation (S4-R2), license/dependency (S4-R3/R-02),
dangerous surface retained accidentally (S4-R4), **false sense of enforcement (S4-R5)**, scope creep into
Sprint 5 (S4-R6), EH-0005B accidental promotion (S4-R7), network/cloud/messaging leakage (S4-R8), dynamic
plugin loading (S4-R9). Mitigations in `SPRINT_4_RISK_AND_GOVERNANCE_CHECKLIST.md`.

## 6. Files in this package (18)

Brief · Scope/Boundaries · Learning · Readiness Review · Baseline Strategy · Fork-vs-Copy-vs-Vendor ·
Source Isolation/Provenance · Remove-vs-Disable Matrix · Default-Deny Baseline Requirements · Policy
Enforcement Precondition Checklist · Dangerous Surface Removal · MVP Retained Surfaces · License/Dependency/SBOM ·
Security Boundary/No-Network · Output Reports Spec · Risk/Governance Checklist · Approval Decision Template ·
this Final Recommendation.

## 7. Confirmations (this task)

- **Approval package only.** Sprint 4 execution **not started**.
- **No Hermes fork created; no Hermes source copied; no Hermes run/build; no dependencies installed.**
- **No runtime/source code created; no `src/`, `policy/`, `tests/`, `ui/`, or implementation folders.**
- **No commit, no push, no branches.** Baseline remains `966629a`.
- **EH-0005B remains PROPOSED**; Hermes Agent not activated; **Sprint 5 not started**.
- All files under `ChatGPTReview/sprint-4-approval-package/` (local-only).

## 8. Single next action

Review and sign `SPRINT_4_APPROVAL_DECISION_TEMPLATE.md` (or choose Defer). Until then, Sprint 4 stays blocked
and the repository is unchanged.
