# DEFAULT_DENY_VALIDATION.md
# Magna Enso — Sprint 3 Capability Governance Design
# Default-Deny Model Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Validate that the default-deny model (DEFAULT_DENY_MODEL.md) is correctly designed,
complete, and adequate as the foundational posture for Magna Enso.

---

## 2. The Seven Rules — Individual Assessment

| Rule | Text | Antigravity Assessment |
|---|---|---|
| R1 | Default state = disabled. Every capability starts disabled. | CORRECT — this is the base posture. No capability is "opt-out of disability"; all are opt-in to enable. |
| R2 | Explicit allowlist only. A capability becomes non-disabled only via an explicit, human-approved policy record. | CORRECT — requires a written policy record (CAPABILITY_POLICY_SCHEMA.md). Closes the "undocumented permission" gap. |
| R3 | No implicit activation. Nothing is enabled as a side effect of being imported, registered, scheduled, or referenced. | CORRECT AND CRITICAL — directly prevents the Hermes toolset assembly (toolsets.py::_HERMES_CORE_TOOLS) from implicitly enabling capabilities. |
| R4 | No external content can raise capability level. Inbound messages, fetched web content, memory contents, instruction packages, or model output can never promote a capability. | CORRECT — this is the primary prompt-injection defense (R-07). Exactly the right rule. |
| R5 | No plugin can self-register an active capability. Plugin/MCP modules may not arrive active; dynamic registration is disabled unless a signed allowlist applies. | CORRECT — closes the dynamic surface expansion bypass identified in Sprint 2. |
| R6 | No config can bypass human approval. A config flag may make something more restrictive but can never set approval_required capabilities to auto-run. | CORRECT — directly addresses the Sprint 2 finding that config-based disablement (T5) is the weakest tier and can be accidentally bypassed. |
| R7 | Unknown capability = disabled. Any capability without a policy record, or reached by an unmapped path, is denied. | CORRECT — this is the most important safety net. Sprint 2's 6+ bypass paths (agent-owned, ACP, cron, gateway, background, MCP) are all denied by default under this rule even if the chokepoint map misses them. |

Assessment: All 7 rules are correctly stated and together form a complete default-deny posture. PASS.

---

## 3. Evaluation Flow Assessment

The conceptual evaluation flow (§3) correctly shows:
- No record → DENY (Rule 7)
- Path not in paths_covered → DENY + ESCALATE (closes unmapped path attacks)
- State disabled → DENY (and ideally enforcement tier removes even the ability to try)
- read_only → ALLOW read; DENY mutate/side-effect
- report_only → ALLOW report; DENY execute
- draft_only → ALLOW stage; DENY persist (until human accepts)
- approval_required → HOLD → unified approval engine → ALLOW once if human approves
- active_safe → ALLOW (no external/persistent effect)
- All outcomes → log

This flow is complete and well-structured. Notable strengths:
1. The "path not in paths_covered → DENY + ESCALATE" case is important — it requires that
   all execution paths are enumerated in the policy record's paths_covered field. Any
   undiscovered bypass path becomes a DENY by default, and escalates rather than silently failing.
2. "DENY is normal, expected behaviour" is correctly framed — denials should be frequent and logged,
   not treated as errors.

---

## 4. Fail-Closed Assessment

§4 specifies three fail-closed behaviors:
- Policy engine unavailable/errored/uncertain → DENY
- Capability reachable by path not in paths_covered → DENY + escalate
- A blocked/denied call is expected, logged behavior (not an error)

Assessment: CORRECT. The fail-closed posture means governance failures fail safe.
This is especially important for the Sprint 4 fork period when the policy engine
will not yet exist (Sprint 5) — the fork must operate without a runtime engine,
relying on T1-T3 disablement to be the primary safety layer.

One note: the report does not explicitly address the "policy engine does not yet
exist" (pre-Sprint 5) scenario. For Sprint 4, the fail-closed posture is enforced
by T1-T3 disablement (remove/process-disable), not by an evaluation engine.
This is correct — the DISABLEMENT_TIERS_MODEL makes the engine's absence safe.
The connection could be clearer, but the content across the two reports is consistent.

---

## 5. Promotion Model Assessment

§5 (Promotion) correctly requires:
- Explicit human decision + new Event Horizon entry
- No worker self-promotes (consistent with EH-0010)
- No silent state change
- External content cannot trigger promotion
- blocked_until conditions must clear first

Assessment: COMPLETE AND CORRECT. The Event Horizon entry requirement creates an audit
trail for every capability promotion. The blocked_until mechanism (e.g. signed_allowlist,
sprint_5_policy_engine) is the correct way to gate capabilities on preconditions.

---

## 6. "Neutralizes Sprint 2 Risk" Claim Assessment

§6 claims: "Under default-deny, every one of those paths resolves to DENY unless
an explicit, path-covered policy says otherwise — so an ungoverned path is safe by
default, not dangerous."

ANTIGRAVITY VALIDATION: CONFIRMED CORRECT.

The Sprint 2 audit found that capabilities were reachable via 6+ paths (dispatch,
agent-owned tools, cron, gateway, ACP, background review, plugin/MCP). Under the
default-deny model:
- If no policy record exists for a capability → it is denied at all paths (Rule 7)
- If a policy record exists but doesn't list a path → that path is denied + escalated
- If a capability is T1/T2 removed → the path literally doesn't exist

This is defense-in-depth: even if the chokepoint implementation misses a path,
the default-deny rule catches it. The claim is correct.

---

## 7. Default-Deny Verdict

```
Seven rules:          All 7 correctly designed — PASS
Evaluation flow:      Complete; handles all 6 states + unknown + uncovered path — PASS
Fail-closed:          Correctly specified — PASS
Promotion model:      Human-only; Event Horizon required; blocked_until supported — PASS
Sprint 2 risk claim:  CONFIRMED — ungoverned paths are safe by default — PASS
No code:              CONFIRMED — design concept only — PASS

DEFAULT-DENY MODEL: VALIDATED — PASS
This is the foundational safety property. It is correctly and completely designed.
```
