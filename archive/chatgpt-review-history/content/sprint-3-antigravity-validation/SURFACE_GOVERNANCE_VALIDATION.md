# SURFACE_GOVERNANCE_VALIDATION.md
# Magna Enso — Sprint 3 Capability Governance Design
# Surface Governance Matrix Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Validate that HERMES_SURFACE_GOVERNANCE_MATRIX.md correctly assigns an MVP state, future
state, enforcement tier, and Sprint 4 action to every Hermes surface. Validate the
special focus items for remote execution backends, direct-script cron, plugin/MCP,
delegation, and outbound delivery.

---

## 2. Full Matrix Assessment

All 17 surfaces in the matrix:

| Surface | MVP State | Future State | Tier | S4 Action | Antigravity Assessment |
|---|---|---|---|---|---|
| Background review | disabled | report_only (maybe) | T1/T2 | **Remove** | CORRECT — remove is required; daemon thread must not exist |
| Curator/self-review | report_only | report_only | T3 | Keep, execution off, reports only | CORRECT — reporting is useful; execution is denied |
| Memory writes | draft_only | draft_only | gate (P-09) | Keep; force non-bypassable staging | CORRECT — gate reference to chokepoint map is correct |
| Skill writes | draft_only | draft_only | gate (P-10) | Keep; force staging; no auto-activation | CORRECT — no-auto-activation rule is critical |
| External memory | disabled | disabled | T1/T2 | **Remove** mirroring/sync | CORRECT — external sync must not be reachable |
| Cron scheduler | report_only | report_only | T3 | Disable execution; schedules → reports | CORRECT — T3 is correct; execution disabled |
| Direct script cron (no_agent) | disabled | disabled | T1/T2 | **Remove** | CORRECT — remove-only is the right choice |
| Subagent delegation | disabled | approval_required (maybe) | T3 | Unregister in MVP | CORRECT — disabled in MVP; post-MVP requires separate design |
| Browser snapshot | read_only | read_only | gate | Keep as read-only | CORRECT — separable from action handlers |
| Browser actions | approval_required / disabled | approval_required | T3/T4 | Disable or gate per action | CORRECT — T3 unregistering preferred; T4 acceptable with bypass closure |
| Terminal / code | approval_required, off by default | approval_required | T4 + gate | Keep; close all bypass paths | CORRECT — explicit bypass path closure requirement |
| Remote execution backends | disabled | disabled | T1/T2 | **Remove** (prefer) | CORRECT — "prefer remove" resolves Sprint 2 VA-09 |
| Messaging gateways | disabled | disabled | T1 | **Remove / not launched** | CORRECT — T1 is mandatory for external listeners |
| API server listener | disabled | disabled | T1 | Not started | CORRECT — T1; never boots |
| Cloud providers | disabled | approval_required (maybe) | T2 | Disable at import/resolution | CORRECT — T2 (import disabled); post-MVP enable path requires separate gate |
| Plugin/MCP loading | disabled unless signed allowlist | disabled/allowlist | T2/T3 | Disable dynamic loader | CORRECT — dynamic loader off; signed allowlist is a future capability |
| Outbound delivery | disabled | disabled | T1/removed | Shutdown all delivery paths | CORRECT — "all delivery paths" is the key phrase; 3 paths confirmed covered |

17/17 surfaces assessed. All MVP states, future states, enforcement tiers, and Sprint 4
actions are correctly specified. PASS.

---

## 3. Special Focus Items — Detailed Assessment

### 3.1 Remote Execution Backends: Remove, Not Merely Disabled

Matrix entry: `disabled | disabled | T1/T2 | **Remove** (prefer)`

ANTIGRAVITY ASSESSMENT: CONFIRMED CORRECT AND COMPLETE.

"Prefer remove" means Modal, Daytona, SSH environment modules are not present in the
Sprint 4 fork baseline. This is stronger than T1 (not started) — even an accidentally-started
or misconfigured process cannot reach a removed module. The "prefer" qualifier appropriately
acknowledges that removal may have dependency implications; T2 (import disabled) is the
minimum acceptable if removal is infeasible.

Sprint 2 VA-09 (remote execution should be removed not just disabled): RESOLVED.

### 3.2 Direct-Script Cron: Remove-Only

Matrix entry: `disabled | disabled | T1/T2 | **Remove**`

ANTIGRAVITY ASSESSMENT: CONFIRMED CORRECT.

The no_agent path in cron/scheduler.py::run_job is the one path where Hermes can execute
arbitrary scripts without an LLM, without a tool registry check, and without any approval
gate. There is no legitimate MVP use case for this. Remove-only is the correct decision.

Sprint 2 open item (direct-script cron should be remove-only): RESOLVED.

### 3.3 Plugin/MCP Dynamic Loading: Remove/Disabled Until Signed Allowlist

Matrix entry: `disabled unless signed allowlist | disabled/allowlist | T2/T3 | Disable dynamic loader`

PLUGIN_MCP_GOVERNANCE_MODEL.md §5 recommends: "MVP recommendation: remove/disable the
dynamic loader (T2/T3). A signed-allowlist mechanism is a future capability, not MVP —
until it exists, dynamic loading stays off."

ANTIGRAVITY ASSESSMENT: CONFIRMED CORRECT.

The recommendation to remove the dynamic loader for MVP is the right choice. The signed
allowlist mechanism is correctly deferred to a future sprint. The key governance invariant —
"no plugin/MCP may self-register an active capability; loaded tools enter at default-deny" —
is also correctly stated.

Sprint 2 open item (plugin/MCP dynamic loading should be remove/disabled until signed allowlist): RESOLVED.

### 3.4 Delegation: Must Remain Disabled in MVP

Matrix entry: `disabled | approval_required (maybe) | T3 | Unregister in MVP`

DELEGATION_RECURSION_CONTROL_MODEL.md §3 and §4:
- MVP: delegation disabled (T3 — not registered)
- Rules: delegate_task unregistered; agent-owned and ACP paths both denied (P-04/P-07)
- Recursion: no subagent-spawning-subagents in MVP
- Post-MVP: approval_required + hard recursion depth limit + no privilege escalation

ANTIGRAVITY ASSESSMENT: CONFIRMED CORRECT AND COMPLETE.

Sprint 2 VA-12 (delegation must be disabled not approval-required in MVP, to bound recursion): RESOLVED.

The distinction between "MVP: disabled" and "post-MVP: approval_required" is correctly
maintained. The post-MVP design (hard depth limit, no privilege escalation, per-spawn
approval) is correctly specified as a future design, not an MVP requirement.

### 3.5 Outbound Delivery: All Three Paths Covered

Matrix entry: `disabled | disabled | T1/removed | Shutdown all delivery paths`

MESSAGING_CLOUD_DISABLED_MODEL.md §3 Rule 4:
"No outbound delivery — send_message not registered AND cron/gateway delivery paths
removed/disabled (the audit notes send_message is 'intentionally not registered, but
cron/gateway can still deliver' — those paths must also be closed)."

ANTIGRAVITY ASSESSMENT: CONFIRMED COMPLETE.

The audit note about send_message_tool being "intentionally not registered" but cron/gateway
delivery paths remaining is explicitly addressed. All three paths are closed:
1. Tool registration: send_message not registered (tool path)
2. Cron delivery: cron/scheduler.py::_deliver_result disabled/removed (cron path)
3. Gateway delivery: listener not started (T1) (gateway path)

Sprint 2 VA-11 (outbound delivery must be closed at all 3 paths): RESOLVED.

---

## 4. Retain / Remove / Disable Summary Assessment

### Retain (behind gate / staged)
agent loop, tool registry, approval/staging primitives, memory (draft_only), skills (draft_only),
terminal/code (approval_required, off by default), browser snapshot (read_only), curator (report_only).

Assessment: All retained capabilities are correctly designated. The retention decision for
terminal/code is the most consequential — it is justified by the bypass path closure requirement.

### Remove
background review, external memory sync, direct-script cron, remote execution backends,
messaging gateways, outbound delivery, dynamic plugin/MCP loader (until signed allowlist).

Assessment: All removed items are correctly identified. The removal list directly maps to
the highest-risk, lowest-MVP-value surfaces from Sprint 2.

### Disable (not started / not imported)
API listener, gateways, cloud providers, inbound triggers, delegation (MVP).

Assessment: Correctly identified. "Disable" here means T1/T2 (not T5 config). The
distinction between "Remove" and "Disable" in the matrix is correctly applied.

---

## 5. Enforcement Note Assessment

§4 notes: "Every removed/disabled surface uses the strongest feasible tier (T1–T3), not
config-only (T5). This matrix + POLICY_CHOKEPOINT_MAP.md together must show no ungated
path to any non-disabled capability."

Assessment: This is the correct design criterion. The "no ungated path" requirement is
the enforcement standard. It is stated here as a design goal and will be verified as a
Sprint 4 implementation requirement (Gate G-15).

---

## 6. Surface Governance Verdict

```
17/17 surfaces covered:              PASS
MVP state per surface:               CORRECT for all 17 surfaces — PASS
Future state per surface:            CORRECT for all 17 surfaces — PASS
Enforcement tier per surface:        CORRECT (T1-T3 for dangerous; T4+gate for terminal/code) — PASS
Sprint 4 action per surface:         CORRECT — PASS

Special focus items:
  Remote execution backends (remove): CONFIRMED — VA-09 RESOLVED — PASS
  Direct-script cron (remove-only):   CONFIRMED — PASS
  Plugin/MCP (remove/disable until):  CONFIRMED — PASS
  Delegation disabled MVP:            CONFIRMED — VA-12 RESOLVED — PASS
  Outbound delivery all 3 paths:      CONFIRMED — VA-11 RESOLVED — PASS

Retain/remove/disable summary:       Correctly categorized — PASS

SURFACE GOVERNANCE MATRIX VALIDATION: PASS
Single-reference design document for Sprint 4 implementation is correct and complete.
```
