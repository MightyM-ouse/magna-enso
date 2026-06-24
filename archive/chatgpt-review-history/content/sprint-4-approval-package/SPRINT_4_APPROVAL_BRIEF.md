# SPRINT_4_APPROVAL_BRIEF.md
# Magna Enso — Sprint 4 Approval Brief
# Type: Local-only approval package (approval-preparation)
# Prepared by: Claude (architecture / governance)
# Date: 2026-06-17
# Status: FOR HUMAN APPROVAL. Sprint 4 NOT started. No fork. No source copy. No commits.

---

> **Terminology note (C-01).** "Clean governed Hermes fork baseline" is the **historical sprint name**. The
> recommended implementation path is more accurately a **Hermes-derived governed baseline through selective
> vendor import** (Option C) — not a full fork. "Fork" is retained only as the sprint's label.

## 1. One-paragraph summary

Sprint 4 would establish a **Hermes-derived governed baseline** (historical name: "clean governed Hermes fork
baseline"), built via **selective vendor import**: a new, isolated baseline that preserves
upstream provenance and license, removes/disables dangerous surfaces per the Sprint 3 design, and records a
baseline report — **before** any runtime, policy engine, or production use. This is the first sprint that
would bring Hermes-derived **source** into the Magna Enso world, so it is the most sensitive gate so far.
This package is **step 1 only (approval preparation)**; it starts nothing.

## 2. Why Sprint 4 is sensitive

- It is the first time Hermes **source** would enter (or be vendored into) the Magna Enso project.
- Hermes carries high-risk surfaces (remote execution, messaging, cloud, dynamic plugins, autonomous loops).
- A careless fork imports those surfaces **and** their ungoverned execution paths (Sprint 2: "no single
  complete chokepoint").
- Mistakes here (accidental activation, incomplete isolation, license slip) are expensive to undo once
  committed to history.

## 3. Why it must not begin automatically

Accepting the Sprint 3 **design** means "the governance plan is agreed." It does **not** mean "build it."
Sprint 4 touches real source and repository history, so it requires its **own** explicit human approval,
reviewed against this package. Default posture remains: blocked.

## 4. Sprint 3 acceptance ≠ implementation approval

| Sprint 3 accepted (EH-0014) | Sprint 4 (this package) |
|---|---|
| The governance **design** is approved as the plan | Whether to **act** on that plan |
| Design/report-only | Would bring source + repo changes |
| No code, no fork | Possible fork/vendor of selected source |
| A design input | A separate, explicit go-ahead |

## 5. What human approval of Sprint 4 WOULD authorize (if granted, under the chosen option)

- Creating an **isolated baseline** (branch or separate location) — per the approved option.
- **Selective** import of *retained* Hermes modules only (not wholesale).
- **Removing** high-risk surfaces and **disabling** others at the Sprint 3 tiers.
- **Repository hygiene** + **provenance manifest** + **license preservation** + a **baseline report**.

## 6. What human approval would STILL NOT authorize

- No runtime activation, production use, or autonomous execution.
- No cloud / messaging / plugin-MCP / remote-backend activation.
- No policy-engine implementation (that is Sprint 5, separately approved).
- No claim that runtime enforcement exists.
- No EH-0005B promotion; no Hermes Agent activation.
- No Sprint 5 work.

## 7. The four clearly separated steps

```text
1. Approval-package preparation   ← THIS TASK (no execution)
2. Sprint 4 execution             ← only after explicit human approval of this package
3. Future implementation          ← runtime/policy engine = Sprint 5+, separate approval
4. Future policy enforcement      ← live default-deny enforcement, separate approval
```

## 8. Files in this package

1. `SPRINT_4_APPROVAL_BRIEF.md` · 2. `SPRINT_4_SCOPE_AND_BOUNDARIES.md` · 3. `SPRINT_4_LEARNING_BRIEF.md` ·
4. `SPRINT_4_READINESS_REVIEW.md` · 5. `HERMES_BASELINE_STRATEGY.md` · 6. `FORK_VS_COPY_VS_VENDOR_DECISION.md` ·
7. `SOURCE_ISOLATION_AND_PROVENANCE_PLAN.md` · 8. `REMOVE_VS_DISABLE_DECISION_MATRIX.md` ·
9. `DEFAULT_DENY_BASELINE_REQUIREMENTS.md` · 10. `POLICY_ENFORCEMENT_PRECONDITION_CHECKLIST.md` ·
11. `DANGEROUS_SURFACE_REMOVAL_PLAN.md` · 12. `MVP_RETAINED_SURFACES_PLAN.md` ·
13. `LICENSE_DEPENDENCY_AND_SBOM_PLAN.md` · 14. `SECURITY_BOUNDARY_AND_NO_NETWORK_PLAN.md` ·
15. `SPRINT_4_OUTPUT_REPORTS_SPEC.md` · 16. `SPRINT_4_RISK_AND_GOVERNANCE_CHECKLIST.md` ·
17. `SPRINT_4_APPROVAL_DECISION_TEMPLATE.md` · 18. `FINAL_RECOMMENDATION.md`.

## 9. Headline recommendation

**Approve Sprint 4 as clean governed baseline preparation only, under Option C (selective vendor import of
retained modules), with a license/SBOM precondition** — or defer if you prefer a fuller dependency review
first. Details in `FINAL_RECOMMENDATION.md`. Until you sign, Sprint 4 stays blocked.
