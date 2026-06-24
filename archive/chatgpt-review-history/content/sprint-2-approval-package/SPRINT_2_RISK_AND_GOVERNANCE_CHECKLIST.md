# SPRINT_2_RISK_AND_GOVERNANCE_CHECKLIST.md
# Magna Enso — Sprint 2 Risk and Governance Checklist
# Type: Local-only approval package
# Date: 2026-06-17
# Status: Gates that MUST hold throughout Sprint 2.

---

## 1. Governance gates (must all stay TRUE for the whole sprint)

- [ ] No modification to Hermes (clone is read-only; not edited, built, or run).
- [ ] No modification to the existing Magna / HELIX repo.
- [ ] No Hermes source inside `magna-enso/` (reports cite identifiers only).
- [ ] No commits and no pushes (without separate explicit human approval).
- [ ] No new branches (unless Decision 3 approves one).
- [ ] No runtime code, no integrations.
- [ ] No Sprint 3 (governance design) or Sprint 4 (fork) work started.
- [ ] Scratch workspace stays outside both repos and is never committed.
- [ ] EH-0005B remains PROPOSED; Hermes Agent not activated.
- [ ] Human owner remains final authority; Antigravity validates before acceptance.

## 2. Risks engaged by Sprint 2 (from the Risk Register)

| Risk | Why Sprint 2 touches it | Sprint 2 mitigation |
|---|---|---|
| R-01 Hermes reuse/coupling | Audit decides reuse | Read-only; keep/rebuild/exclude per module, not "clone all" |
| R-02 License/dependency/ToS | Audit reviews licenses | `LICENSE_AND_DEPENDENCY_REVIEW.md`; license verification mandatory before Sprint 4 |
| R-04 Cloud/provider creep | Audit maps cloud integrations | `EXTERNAL_SURFACE_MAP.md` flags them for default-deny in Sprint 3 |
| R-05 Public exposure | Audit maps network surfaces | Identify-only; nothing run/exposed; LAN/local posture unaffected |
| R-06 Policy bypass | Audit maps dispatch chokepoints | `CAPABILITY_GATING_FEASIBILITY.md` assesses gateability before any build |
| R-07 Prompt-injection persistence | Audit maps memory/skill writes | `AUTONOMY_ENTRY_POINT_MAP.md`; no execution, so no injection runs |
| R-11 Fork maintenance | Audit informs fork decision | Provenance + SHA recorded; minimal-reuse recommendation |
| R-13 Overengineering | Audit could over-map | Bounded to the 14 questions; reports only |
| R-15 UI/E2E worker feasibility | Hermes Agent candidacy | Hermes Agent does NOT perform audit; stays candidate |

## 3. New Sprint-2-specific risks to watch

| ID | Risk | Mitigation |
|---|---|---|
| S2-W1 | Hermes source accidentally copied into `magna-enso/` | Scratch outside repo; `.gitignore` defensive patterns; reports cite identifiers only; Antigravity checks |
| S2-W2 | Scope creep into "let me fix/integrate it" | Non-goals list; "reports only, stop after"; reviewer gate |
| S2-W3 | Running Hermes (executing capabilities) during "inspection" | Read-only rule: clone is never built or run |
| S2-W4 | Pasting large source blocks into reports | Identifier-only quoting rule |
| S2-W5 | Auditing the wrong/unpinned version | Record exact commit SHA first (`HERMES_PROVENANCE.md`) |

## 4. Stop conditions (halt and escalate to human)

Stop immediately and ask the human owner if any of these occur:
- The Hermes license is **not** as expected (e.g. not MIT) or has copyleft/ToS conflicts.
- A surface cannot be placed behind any chokepoint (serious R-06 implication).
- The audit would require running or modifying Hermes to answer a question.
- Any pressure to begin Sprint 3/4 work, fork, or copy source into `magna-enso/`.

## 5. Acceptance gate

Sprint 2 is accepted **only** when: all reports exist, Antigravity validation passes, the
`SPRINT_2_LIGHT_CURVE.md` is written, and the **human owner signs off**. No worker self-approves.
