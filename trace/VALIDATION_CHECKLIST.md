# VALIDATION_CHECKLIST.md — Spectrometer (Magna Enso)

> The Spectrometer validates outputs before they are trusted. Governance checks are **mandatory gates**,
> not advisory. Run the relevant section before concluding a task; record results in the Light Curve.

## A. Universal governance gates (every task)

- [ ] No auto-commit and no auto-push occurred.
- [ ] No change was made to the existing Magna / HELIX repository.
- [ ] No Hermes source was cloned or copied into this repository.
- [ ] No public-facing surface was created or enabled (local-first / LAN-first preserved).
- [ ] No cloud execution was enabled by default.
- [ ] No silent memory mutation; no skill auto-activation.
- [ ] Material/irreversible actions were paused for human approval.
- [ ] A Light Curve was produced and the Star Map updated.
- [ ] Material decisions were logged to the Event Horizon.

## B. Context discipline (Route phase)

- [ ] Only the relevant `CELESTIAL_INDEX.json` area(s) were loaded (no full-repo scan).
- [ ] The task stayed within its Constellation's Allowed Scope.

## C. Documentation / skeleton tasks (Sprint 1 type)

- [ ] New/changed docs follow the TRACE Documentation Standard where applicable.
- [ ] Artifacts are internally consistent and consistent with frozen decisions (EH-0001…EH-0011).
- [ ] No runtime code, no integrations, no speculative structure introduced.
- [ ] Cross-references and file paths resolve.

## D. Runtime / code tasks (Sprint 4+ — not applicable in Sprint 1)

- [ ] Every capability call passes the policy gate; no bypass path (proven by negative tests).
- [ ] Default-deny posture holds; approval-required capabilities block pending human approval.
- [ ] Network binding is LAN-only and off by default; no public listener (binding test).
- [ ] Secrets redacted in any captured execution; nothing leaves the machine.
- [ ] Provenance recorded for any reused upstream code (source repo + commit SHA + license).
- [ ] Build / unit / integration / smoke tests run; results are real (not estimated).

## Honest data contract
Record **real** results (what was actually checked/observed). Mark any token/cost/effort figure as
**approximate**. A blocked safety gate is expected behavior, not a failure.
