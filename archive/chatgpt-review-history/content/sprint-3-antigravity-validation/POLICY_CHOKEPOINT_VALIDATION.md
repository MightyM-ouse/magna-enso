# POLICY_CHOKEPOINT_VALIDATION.md
# Magna Enso — Sprint 3 Capability Governance Design
# Policy Chokepoint Map Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Validate that all 13 required policy boundaries are covered in POLICY_CHOKEPOINT_MAP.md,
that the bypass-resistance argument is correct, and that the consolidation strategy
adequately addresses the Sprint 2 central finding (no single complete chokepoint).

---

## 2. All 13 Required Boundaries — Assessment

| # | Required Boundary | Chokepoint | Required policy action | Default | Assessment |
|---|---|---|---|---|---|
| P-01 | startup | run_agent.py, toolsets.py::_HERMES_CORE_TOOLS | Build active toolset from Magna policy, not Hermes config | deny | CORRECT — startup is the first and most important gate; Hermes default (broad toolset) must be replaced |
| P-02 | tool registry | tools/registry.py::register, discover_builtin_tools | Register only policy-allowed tools; dangerous tools not registered (T3) | deny | CORRECT — registry is the T3 enforcement point for unregistered capabilities |
| P-03 | model tool dispatch | model_tools.py::handle_function_call, agent/tool_executor.py | Primary gate: classify + enforce capability state | deny | CORRECT — main dispatch path; policy engine's primary hook |
| P-04 | agent-owned tools | model_tools.py::_AGENT_LOOP_TOOLS = {todo, memory, session_search, delegate_task} | Route through same policy path (cannot rely on registry alone) | deny | CORRECT AND CRITICAL — Sprint 2's finding that agent-owned tools bypass registry; must be explicitly routed through P-03 gate |
| P-05 | cron / scheduler | cron/scheduler.py::tick, run_job, cron/jobs.py | Execution disabled; schedules → report-only objects | report_only | CORRECT — scheduler execution must be blocked; no_agent path removed |
| P-06 | gateway / API | gateway/run.py, gateway/platforms/api_server.py | Listener not started (T1); inbound runs denied | disabled | CORRECT — T1 is the right tier; listener must never start |
| P-07 | ACP tools | acp_adapter/tools.py (delegate_task, memory, cronjob, send_message) | Map to same policy; no independent capability grant | deny | CORRECT AND CRITICAL — ACP is a separate dispatch path that must not grant capabilities independently |
| P-08 | provider / model calls | providers/*, plugins/model-providers/*, agent adapters | Disabled at provider resolution + import (T2) | disabled | CORRECT — module import disabled (T2); no cloud calls possible |
| P-09 | memory persistence | tools/memory_tool.py::MemoryStore.save_to_disk, agent/memory_manager.py | draft-only staging; external mirror disabled | draft_only | CORRECT — staging gate; external sync separately disabled |
| P-10 | skill persistence | tools/skill_manager_tool.py::skill_manage | draft-only staging; no auto-activation | draft_only | CORRECT — consistent with P-09; no auto-activation |
| P-11 | plugin loading | hermes_cli/plugins/*, plugin pre-tool-call hooks | Loader disabled unless signed allowlist; not a security boundary itself | disabled | CORRECT AND IMPORTANT — explicitly notes plugins hooks are NOT a security boundary (Sprint 2 confirmed: plugin hooks can be bypassed) |
| P-12 | MCP loading | tools/mcp_tool.py, tui_gateway/entry.py background discovery | Dynamic registration disabled; surface fixed at startup | disabled | CORRECT — dynamic discovery must not run; surface must be fixed |
| P-13 | outbound delivery | tools/send_message_tool.py, cron/scheduler.py::_deliver_result | Shutdown; no outbound in MVP | disabled | CORRECT — all 3 outbound paths disabled (tool, cron delivery, gateway) |

All 13 required boundaries: MAPPED AND CORRECTLY ASSIGNED. PASS.

---

## 3. Coverage Matrix Assessment

§3 provides illustrative rows for high-risk capabilities:

| Capability | Boundaries listed | Assessment |
|---|---|---|
| terminal_execution (C-06) | P-03, P-04, P-05 (cron), P-07 (ACP), P-06 (gateway) | CORRECT — all paths from Sprint 2 ACTION_DISPATCH_MAP covered; cron no_agent and gateway are also listed |
| persistent_memory (C-03) | P-03, P-04, P-05, P-07, P-09 | CORRECT — includes agent-owned path (P-04) and ACP path (P-07) |
| cloud_provider (C-11) | P-08, P-03, P-06, P-11/P-12 | CORRECT — P-08 is the primary T2 gate; plugin/MCP are additional paths |
| messaging_outbound (C-12) | P-13, P-05, P-06 | CORRECT — all 3 outbound delivery paths covered (tool, cron, gateway) |
| delegation (C-14) | P-04, P-07 | CORRECT — delegation is an agent-owned tool and ACP tool; both covered |
| plugin/MCP (C-15) | P-11, P-12 | CORRECT — both plugin loader and MCP dynamic discovery covered |

All illustrative coverage rows are correct and consistent with Sprint 2 ACTION_DISPATCH_MAP.

---

## 4. Consolidation Strategy Assessment

§4 (single-chokepoint goal vs. reality) correctly states the three-part strategy:

1. CONSOLIDATE paths onto P-03 (including agent-owned P-04 and ACP P-07 routed through same gate)
2. REMOVE OR PROCESS-DISABLE paths that cannot be consolidated (P-05 cron, P-06 gateway, P-08 providers, P-11/P-12 plugin/MCP, P-13 outbound)
3. Accept the design only when EVERY boundary is gated or removed — no "mostly covered"

Assessment: This three-part strategy is the correct and only adequate response to the
Sprint 2 finding. "No mostly covered" is exactly the right acceptance criterion.

The consolidation of agent-owned tools (P-04) and ACP tools (P-07) through the same
policy gate as model dispatch (P-03) is the critical architectural decision that closes
the most dangerous bypass paths from Sprint 2. This is correctly stated.

---

## 5. Bypass-Resistance Argument Assessment (Sprint 4 Gate G-15)

§5 claims: "For each capability the design lists all boundaries it can be reached through
and shows each is gated or removed. A capability reachable by any uncovered boundary is
treated as disabled (default-deny) and the boundary flagged for removal before that
capability may be enabled."

ANTIGRAVITY ASSESSMENT:

The bypass-resistance argument is structurally correct:
- If a capability has all its paths listed in paths_covered AND each path is either gated
  (P-03/P-04 consolidated) or removed (P-05 cron no_agent, P-06 gateway, P-08 providers,
  P-11/P-12 plugin/MCP, P-13 outbound) → the capability cannot be reached via an ungated path
- If a path is missed → default-deny (Rule 7) catches it; the missed path is safe-by-default
- If a path is removed (T1/T2) → the path literally doesn't exist; bypass is structurally impossible

The combination of: consolidation (P-03/P-04/P-07 unified gate) + removal (T1-T3 for
dangerous surfaces) + default-deny (catch-all) constitutes a valid multi-layer bypass
resistance argument.

ONE LIMITATION: The bypass-resistance is a design-time argument only at Sprint 3.
Sprint 4 implementation must demonstrate that the paths are actually gated/removed in
the fork code. G-15 (bypass-resistance argued) is "designed; pending Antigravity validation"
— this is the correct status. Full bypass-resistance proof is a Sprint 4 verification task.

---

## 6. Policy Chokepoints Verdict

```
13/13 required boundaries covered:      PASS
Agent-owned tools (P-04) explicitly covered: CRITICAL — PASS
ACP tools (P-07) explicitly covered:    CRITICAL — PASS
Plugin hooks noted as non-security:     CORRECT (P-11 note) — PASS
All 3 outbound paths closed (P-13):     CONFIRMED — PASS
Consolidation strategy:                 Correct — PASS
Removal of un-consolidatable paths:     Correct — PASS
Bypass-resistance argument:             Valid design-time argument — PASS
  (Sprint 4 must prove at implementation time)

POLICY CHOKEPOINT VALIDATION: PASS
All 13 boundaries gated or removed. Bypass-resistance correctly argued at design level.
```
