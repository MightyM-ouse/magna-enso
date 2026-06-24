# POLICY_ENFORCEMENT_PRECONDITION_CHECKLIST.md
# Magna Enso — Policy Enforcement Precondition Checklist
# Type: Local-only approval package
# Date: 2026-06-17
# Status: CLARIFICATION of what Sprint 4 can/cannot do before a policy engine exists.

---

## 1. Purpose

Draw a hard line between **structural safety** (what Sprint 4 can do without code that runs) and **runtime
enforcement** (Sprint 5's policy engine). This prevents the most dangerous mistake: believing the baseline is
"protected" when nothing is actually enforcing anything.

## 2. Sprint 4 MAY (before policy engine exists)

- [ ] Remove or isolate risky surfaces (REMOVE/DISABLE per the matrix).
- [ ] Selectively import only retained modules (Option C).
- [ ] Prepare baseline structure (directory layout, vendor area, hygiene).
- [ ] Define manifests (provenance, file inventory, SBOM, retained-state mapping).
- [ ] Sever import-time self-registration so retained tools are not wired to run.
- [ ] Record each retained surface's intended capability state (as metadata/docs).
- [ ] Produce the Sprint 4 reports + a no-network validation.

## 3. Sprint 4 MAY NOT (no policy engine yet)

- [ ] **Claim runtime enforcement exists.** It does not until Sprint 5.
- [ ] Activate any retained risky capability (terminal/code stay **off**).
- [ ] Run the baseline as a live system; no execution, no autonomy.
- [ ] Implement the policy engine, the gate, or the approval engine (Sprint 5+).
- [ ] Enable network, cloud, messaging, plugins, or remote backends.
- [ ] Rely on a config flag as the safety mechanism for a dangerous surface.
- [ ] Promote EH-0005B or activate Hermes Agent.

## 4. The key statement (must appear in Sprint 4 reports)

> "This baseline is **structurally safe** — dangerous surfaces are removed or disabled and nothing is wired
> to run. It is **NOT runtime-enforced** — there is no policy engine yet. Retained risky capabilities remain
> **disabled** until the Sprint 5 policy engine is implemented and separately approved."

## 5. Why this matters

A "false sense of enforcement" is itself a critical risk (see risk checklist). If a future worker reads the
baseline and assumes "the gate will catch it," they may enable something unsafe. The baseline's safety comes
from **absence** (removed) and **off-state** (disabled), not from an active guard. This checklist makes that
explicit and testable.

## 6. Boundaries

Clarification only. No enforcement, engine, or activation is created by this package or by Sprint 4.
