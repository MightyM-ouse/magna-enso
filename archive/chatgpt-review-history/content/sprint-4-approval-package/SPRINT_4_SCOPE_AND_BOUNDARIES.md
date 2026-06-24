# SPRINT_4_SCOPE_AND_BOUNDARIES.md
# Magna Enso — Sprint 4 Scope and Boundaries
# Type: Local-only approval package
# Date: 2026-06-17
# Status: FOR HUMAN APPROVAL. Sprint 4 NOT started.

---

> **Terminology note (C-01).** "Clean governed Hermes fork baseline" is the **historical sprint name**. The
> recommended implementation is a **Hermes-derived governed baseline through selective vendor import**
> (Option C), not a full fork.

## 1. What Sprint 4 IS (if later approved)

A **Hermes-derived governed baseline preparation sprint** (historical name "clean governed Hermes fork
baseline"): produce an isolated, governed baseline from
selected, retained Hermes source — provenance-recorded, license-preserved, dangerous surfaces removed/disabled
per the Sprint 3 design — plus a baseline report. It is **baseline preparation**, not a running system.

## 2. What Sprint 4 MAY include (if approved, under the chosen option)

- Creating a **fork/baseline location** (isolated branch or separate baseline path) — per the approved Baseline Strategy option.
- **Copying selected (retained) Hermes source** only — never wholesale.
- **Removing** high-risk surfaces (strong tiers T1/T2) and **disabling** others (T2/T3) per the Sprint 3 matrix.
- Applying **repository hygiene** (structure, .gitignore scope, no secrets).
- **Recording provenance** (source repo + SHA `33b1d144` + file inventory + manifest).
- Creating a **baseline report** (what was imported, removed, disabled, retained).

## 3. What Sprint 4 is STILL NOT allowed to do

- **No runtime activation.** The baseline does not run as a live system.
- **No production use.**
- **No autonomous execution.**
- **No cloud activation.** No provider calls.
- **No messaging activation.** No gateways, no outbound delivery.
- **No plugin/MCP activation.** No dynamic loading.
- **No remote execution backends.**
- **No policy-engine implementation** unless separately approved (that is Sprint 5).
- **No EH-0005B promotion**; no Hermes Agent activation.
- **No Sprint 5 work**; no default-deny *enforcement* (Sprint 4 can structurally remove/isolate, not enforce at runtime).

## 4. Hard boundaries (this preparation task)

- No fork, no clone (beyond reading existing local audit references), no source copy, no Hermes build/run,
  no dependency install, no runtime/source folders (`src/`, `policy/`, `tests/`, `ui/`), no commit/push, no
  branches. This task produces **only** the 18 approval documents under
  `ChatGPTReview/sprint-4-approval-package/`.

## 5. The retain / remove / disable frame

Sprint 4 acts on the Sprint 3 **Hermes Surface Governance Matrix**: **retain** a minimal set behind the
(future) gate at draft-only/read-only/approval-required-but-off; **remove** the worst surfaces (T1/T2);
**disable** the rest (T2/T3). See `REMOVE_VS_DISABLE_DECISION_MATRIX.md`, `DANGEROUS_SURFACE_REMOVAL_PLAN.md`,
`MVP_RETAINED_SURFACES_PLAN.md`.

## 5a. Branch / baseline-path isolation (C-04)

If Sprint 4 is later approved, it runs in an **isolated branch or an approved baseline path** and **must not
directly mutate `main` without review**. Merges to `main` go only through a human-reviewed review-package
(Light Curve); no auto-commit/auto-push/force-push (EH-0008). The imported (vendored) source is additionally
**inert/quarantined** (not wired/imported/executable/registered/discovered) — see
`SOURCE_ISOLATION_AND_PROVENANCE_PLAN.md` §3a.

## 6. The enforcement caveat (critical)

Sprint 4 can **remove or isolate** risky surfaces and **prepare** structure/manifests, but it **cannot claim
runtime enforcement exists** — there is no policy engine until Sprint 5. Retained risky capabilities
(terminal/code) stay **disabled** in the baseline; "approval-required" is a *posture*, enforced later.
See `POLICY_ENFORCEMENT_PRECONDITION_CHECKLIST.md`.

## 7. Definition of done (Sprint 4, if approved)

The retained baseline exists in isolation with provenance + license preserved, dangerous surfaces removed/
disabled, a no-network posture, the Sprint 4 reports produced, Antigravity validation passed, a
`SPRINT_4_LIGHT_CURVE.md` written, and the human owner accepts. **Then Sprint 4 stops** — it does not roll
into Sprint 5 (policy engine).
