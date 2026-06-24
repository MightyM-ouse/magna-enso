# SPRINT_4_RISK_AND_GOVERNANCE_CHECKLIST.md
# Magna Enso — Sprint 4 Risk and Governance Checklist
# Type: Local-only approval package
# Date: 2026-06-17
# Status: Gates that MUST hold if Sprint 4 is approved and executed.

---

## 1. Governance gates (must all stay TRUE throughout Sprint 4)

- [ ] No Hermes build, run, or dependency install (beyond a **static** license/SBOM review that does not execute Hermes).
- [ ] **License/SBOM is a mandatory pre-import gate** — review completes (static source/manifest/license read)
      **before any imported source is committed**; incompatible license or unclear dependency status = **STOP**.
- [ ] No runtime dependency install unless separately approved.
- [ ] Only **retained** modules imported (Option C); no removed surface enters the repo.
- [ ] Provenance + inventory account for every imported file (no hidden copy).
- [ ] MIT license preserved; stop on any incompatible-license finding.
- [ ] Dangerous surfaces removed/disabled per the matrix; verified absent/off.
- [ ] No network/cloud/messaging/plugin/remote-backend surface active.
- [ ] Retained risky capabilities (terminal/code) remain **disabled** (no policy engine yet).
- [ ] No claim of runtime enforcement; "structurally safe / not enforced" stated.
- [ ] No Sprint 5 work; no policy-engine implementation.
- [ ] EH-0005B remains PROPOSED; Hermes Agent not activated.
- [ ] No commit/push without separate human approval; Antigravity validates before acceptance.

## 2. Sprint-4-specific risks

| ID | Risk | Mitigation |
|---|---|---|
| S4-R1 | **Accidental Hermes activation** | Baseline does not run; retained tools not wired; terminal/code off; Antigravity verifies |
| S4-R2 | **Incomplete source isolation** | Allowlist-only import; provenance + inventory cover every file; diff reviewed |
| S4-R3 | **License/dependency risk** (R-02) | License/SBOM scan as precondition/first task; stop-condition on incompatibility |
| S4-R4 | **Dangerous surface retained accidentally** | Removed-surfaces report confirms absence; remove/disable matrix checked |
| S4-R5 | **False sense of enforcement** | Mandatory honesty statement; precondition checklist; retained risky surfaces disabled |
| S4-R6 | **Scope creep into Sprint 5** | "No policy engine / no enforcement" boundary; reviewer gate; stop after baseline |
| S4-R7 | **EH-0005B accidental promotion** | Only human owner changes EH-0005B; not touched in Sprint 4 |
| S4-R8 | **Network/cloud/messaging leakage** | Those surfaces removed (T1); no-network static validation |
| S4-R9 | **Dynamic plugin loading** | Loader removed (T2/T3); no plugin self-registration |

## 3. Linkage to project risk register

R-01 (reuse/coupling) — Sprint 4 imports the minimum; R-02 (license/deps) — addressed by SBOM plan; R-04
(cloud creep) / R-05 (public exposure) — removed surfaces + no-network; R-06 (policy bypass) — structural
removal + retained-off (enforcement deferred to Sprint 5); R-11 (fork maintenance) — provenance + minimal
surface; R-13 (overengineering) — minimal retained set.

## 4. Stop conditions (halt + escalate to human)

- Any incompatible/copyleft/ToS license on a retained dependency.
- A retained module cannot be isolated without pulling in a removed surface.
- The baseline would need to run/build to complete a task.
- Pressure to implement the policy engine, enable a risky surface, promote EH-0005B, or start Sprint 5.

## 5. Acceptance gate

Sprint 4 is accepted only when: reports complete, removed surfaces verified absent, no-network validated,
license/SBOM clean, default-deny baseline confirmed structurally, `SPRINT_4_LIGHT_CURVE.md` written,
Antigravity validation passed, and the **human owner signs off**. No worker self-approves.
