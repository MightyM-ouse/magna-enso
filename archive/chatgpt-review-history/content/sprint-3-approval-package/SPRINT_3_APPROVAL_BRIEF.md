# SPRINT_3_APPROVAL_BRIEF.md
# Magna Enso — Sprint 3 Approval Brief
# Type: Local-only approval package (planning / approval-preparation)
# Prepared by: Claude (architecture / governance)
# Date: 2026-06-17
# Status: FOR HUMAN APPROVAL. Sprint 3 NOT started. No implementation. No commits.

---

## 1. One-paragraph summary

Sprint 3 is a **governance-design sprint**. Before any Hermes fork (Sprint 4) or runtime code, it defines
**how Magna Enso will control every Hermes-derived capability** through a **default-deny** model:
a capability taxonomy, capability states, disablement tiers, a unified approval-engine concept, a policy
chokepoint map, per-surface MVP postures, and explicit Sprint 4 readiness gates. **Design only — no code.**
This brief plus the 13 companion documents is what the human owner reviews to approve (or amend) Sprint 3.

## 2. Where we are (baseline)

| Item | State |
|---|---|
| Sprint 1 | Accepted & committed — `e0a28d4` |
| Sprint 2 | Accepted & committed — `94d63ed` (Hermes read-only audit) |
| Hermes audited | `github.com/nousresearch/hermes-agent` @ `33b1d144590a211100f42aa911fd7f91ba031507` |
| Sprint 2 conclusion | Hermes **conditionally suitable only** for future *governed fork consideration* — NOT approved for adoption/activation/build/run/fork/implementation/integration |
| Key audit finding | Hermes has **no single complete policy chokepoint**; registry dispatch alone is insufficient |
| EH-0005B | PROPOSED (Hermes Agent candidate; not promoted) |
| Sprint 3 / Sprint 4 | NOT started |
| Risk posture | R-01, R-02, R-06 remain OPEN (per `magna-enso/trace/RISK_REGISTER.md` Sprint 2 note) |

## 3. What this package contains

| # | File | Purpose |
|---|---|---|
| 1 | `SPRINT_3_APPROVAL_BRIEF.md` | This overview |
| 2 | `SPRINT_3_SCOPE_AND_BOUNDARIES.md` | What Sprint 3 is / is not |
| 3 | `SPRINT_3_LEARNING_BRIEF.md` | Safety-architecture concepts being taught |
| 4 | `CAPABILITY_GOVERNANCE_DESIGN_PLAN.md` | The 15 design deliverables and method |
| 5 | `CAPABILITY_STATES_PROPOSAL.md` | The six capability states |
| 6 | `DEFAULT_DENY_POLICY_MODEL.md` | Why/how default-deny + policy schema shape |
| 7 | `DISABLEMENT_TIERS_PROPOSAL.md` | Five tiers of "disabled" and their strength |
| 8 | `UNIFIED_APPROVAL_ENGINE_CONCEPT.md` | One auditable approval path (concept only) |
| 9 | `POLICY_CHOKEPOINT_MAP_PLAN.md` | How to map every execution path to a gate |
| 10 | `HERMES_SURFACE_GOVERNANCE_PLAN.md` | Per-surface proposed MVP posture |
| 11 | `SPRINT_3_OUTPUT_REPORTS_SPEC.md` | The design reports Sprint 3 will produce |
| 12 | `SPRINT_3_RISK_AND_GOVERNANCE_CHECKLIST.md` | Gates that must hold |
| 13 | `SPRINT_3_APPROVAL_DECISION_TEMPLATE.md` | The 14 decisions + ready-to-sign block |
| 14 | `FINAL_RECOMMENDATION.md` | Consolidated recommendation |

## 4. Headline recommendation

**Proceed to Sprint 3 — design-only, default-deny — after you sign the approval block.** Specifics:

- **Start Sprint 3:** Yes. It is the mandatory safety-architecture step before any fork.
- **Design-only:** Yes; **illustrative schema sketches allowed** as design artifacts, but **no executable code**.
- **Default-deny: mandatory.** Every capability is `disabled`/`approval_required` unless proven `active_safe`.
- **Highest-risk surfaces:** plugin/MCP dynamic loading, remote execution backends, messaging gateways,
  cloud providers, background self-improvement → **removed or disabled by default** (see decisions 5–8).
- **Worker model:** Claude leads (governance architecture); Antigravity validates before acceptance; Grok
  challenges; Codex advises feasibility from the Sprint 2 map (no code); ChatGPT continuity.
- **Sprint 4 is blocked** until Sprint 3 is accepted and answers the 10 readiness gates.

## 5. Why Sprint 3 before Sprint 4

You design the safety architecture **before** you build (or fork) the thing it governs. The Sprint 2 audit
proved Hermes has powerful capabilities but **no single complete chokepoint** — so adopting it without a
governance design first would mean importing ungoverned execution paths. Sprint 3 turns "conditionally
suitable" into a concrete, enforceable control model, and defines exactly what must be retained, removed,
disabled, or gated before a single line of fork code exists.

## 6. What approval does NOT authorize

Approving Sprint 3 does **not** authorize: forking, implementation, runtime/policy-engine/UI code, Hermes
activation/build/run, Sprint 4, promoting EH-0005B, or activating Hermes Agent. All remain separately gated.
