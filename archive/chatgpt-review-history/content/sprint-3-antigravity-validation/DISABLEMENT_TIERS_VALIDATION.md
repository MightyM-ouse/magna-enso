# DISABLEMENT_TIERS_VALIDATION.md
# Magna Enso — Sprint 3 Capability Governance Design
# Disablement Tiers Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Validate that the 5-tier disablement model assigns the strongest feasible tier to each
dangerous Hermes surface, that process/module/registration disablement is preferred over
dispatch/config, and that all required surfaces are explicitly tiered.

---

## 2. Tier Model Assessment

The 5 tiers (T1–T5, strongest to weakest):

| Tier | Name | Mechanism | Bypass resistance | Assessment |
|---|---|---|---|---|
| T1 | Process-level disabled | Feature/process never starts | Strongest | CORRECT — nothing in memory, no code path exists |
| T2 | Module import disabled | Module never imported | Very strong | CORRECT — code unreachable; cannot be called |
| T3 | Tool registration disabled | Module may load; tool never registered | Strong | CORRECT — not in dispatch registry; most paths blocked |
| T4 | Dispatch-level blocked | Tool registered; dispatch checks policy and refuses | Moderate | CORRECT — guards ONE path only; bypass risk acknowledged |
| T5 | Config-level disabled | A flag says off; relies on every path honoring it | Weakest | CORRECT — explicitly labeled as weakest; the Sprint 2 gap |

The tier model correctly establishes the ordering and rationale. The key insight —
"T1–T3 remove the capability from existence, so there is nothing to bypass by any path" —
is the correct design principle.

The critical design rule is stated as: "The most dangerous surfaces must be removed or
disabled at T1–T3, never merely T4/T5." This directly addresses Sprint 2 VA-07.

---

## 3. Tier Assignment Per Surface — Detailed Assessment

| Surface | Assigned Tier | Required? | Assessment |
|---|---|---|---|
| API server listener | T1 (not started) | T1 required | CORRECT — listener must never start; nothing to intercept |
| Messaging gateways | T1 (not launched) | T1 required | CORRECT — 10+ platform adapters must never boot |
| Remote execution backends | T1/T2 (prefer remove) | T1 or T2 required | CORRECT — prefer remove is exactly right; cloud/SSH must not be reachable |
| Background self-improvement | T1/T2 (remove) | T1 required | CORRECT — daemon thread must not spawn |
| Direct script cron (no_agent) | T1/T2 (remove) | T1 required | CORRECT — remove is the only safe option for script execution without LLM |
| Cloud providers | T2 (not imported) | T2 required | CORRECT — provider module must not load |
| External memory sync | T1/T2 | T1/T2 required | CORRECT — sync must not start |
| Plugin/MCP dynamic loading | T2/T3 | T2/T3 acceptable | CORRECT — T2 is preferred (import disabled); T3 acceptable if signed allowlist mechanism still not imported |
| Subagent delegation | T3 (not registered) | T3 acceptable | CORRECT — delegation tool unregistered; agent-owned/ACP path also denied (chokepoint map) |
| Cron scheduler (execution) | T3 + report-only | T3 minimum | CORRECT — execution disabled at registration level; schedule metadata preserved |
| Curator/self-review | T3 + report-only | T3 minimum | CORRECT — execution paths replaced by report generation |
| Browser actions | T3/T4 | T3 preferred, T4 acceptable | ACCEPTABLE — T3 (unregister action handlers) is preferred; T4 acceptable for initial MVP |
| Terminal/code execution | T4 + gate | T4 acceptable | CORRECT — retained capability; T4 appropriate when bypass paths are closed (see §4) |

Assessment: All dangerous surfaces correctly assigned T1–T3. Terminal/code execution
correctly assigned T4 with explicit bypass closure. No surface assigned only T5.

---

## 4. T4 Terminal/Code Exception Assessment

Terminal and code execution are the only retained capabilities assigned T4 (dispatch-level
blocked with gate). This is acceptable because:
1. They are explicitly retained capabilities (not removed/disabled)
2. The design requires closing ALL bypass paths (cron no_agent removed, remote backends
   removed, gateway listener off, agent-owned/ACP routed through same gate)
3. The unified approval engine provides per-action human approval
4. Full audit logging at evidence_required=full

The risk is that T4 is only as strong as the bypass path closure. If any bypass path
remains open in Sprint 4 implementation, T4 is insufficient. This is acknowledged in
TERMINAL_CODE_APPROVAL_REQUIRED_MODEL.md §3: "Bypass paths must be closed."

Antigravity Assessment: The T4 + gate assignment for terminal/code is correctly justified
given the bypass path closure requirement. Sprint 4 must verify bypass closure before
terminal/code may be considered as approval_required (rather than effectively disabled).
Until proven, terminal/code should be treated as effectively disabled in the fork.

---

## 5. "Prefer Remove" Validation for High-Risk Surfaces

The report uses "prefer remove" language for:
- Remote execution backends: T1/T2 (prefer remove)
- Background self-improvement: T1/T2 (remove)
- Direct script cron: T1/T2 (remove)

This answers Sprint 2 VA-09 (remote execution backends should be removed not just disabled)
and Sprint 2 VA-12 open item (direct-script cron should be remove-only).

ANTIGRAVITY ASSESSMENT: CONFIRMED CORRECT AND SUFFICIENT.
"Remove" is stronger than even T1 — it means the module/file is not present in the
Sprint 4 fork baseline, not merely "not started." This is the appropriate choice for
surfaces where even an unstarted process or importable module poses risk (e.g., a
misconfig could start it; a dependency could import it).

---

## 6. Why T5 Must Not Be Used (Validation of Design Rule)

§3 of DISABLEMENT_TIERS_MODEL.md correctly explains why T5 is inadequate:
"The Sprint 2 ACTION_DISPATCH_MAP proved Hermes reaches capabilities through many paths...
T4 guards one of those paths; the rest stay open. Config (T5) is weaker still — one path
that forgets the flag is a hole."

This is the exact finding from Sprint 2 validation (confirmed: dispatch alone insufficient;
6+ bypass paths exist). The design rule ("most dangerous surfaces at T1–T3") directly
implements the Sprint 2 recommendation.

VALIDATION: The design rule is stated correctly, justified correctly, and applied
correctly to the tier assignments. No surface that should be T1-T3 is assigned T4 or T5.

---

## 7. Disablement Tiers Verdict

```
5-tier model:                   Correctly defined, ordered, justified — PASS
Dangerous surfaces at T1-T3:    ALL correct — remote backends, messaging, listeners,
                                background, direct-script cron, cloud, external memory,
                                plugin/MCP — ALL at T1-T3 — PASS
T4 terminal/code:               Correctly justified with bypass closure requirement — PASS
"Prefer remove" for highest-risk: CONFIRMED — resolves Sprint 2 VA-09 — PASS
No T5-only assignments:         CONFIRMED — no surface assigned config-only disablement — PASS
No code:                        CONFIRMED — design specification only — PASS

DISABLEMENT TIERS VALIDATION: PASS
Strongest tiers correctly applied. Design correctly prioritizes removal over disablement.
```
