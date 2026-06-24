# POLICY_CHOKEPOINT_MAP.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 6 of 17 — Policy Chokepoint Map
# Type: Design-only governance report. No code.
# Date: 2026-06-17
# Inputs: Sprint 2 ACTION_DISPATCH_MAP, AUTONOMY_ENTRY_POINT_MAP, EXTERNAL_SURFACE_MAP (Hermes @ 33b1d144)
# Status: Design only. Human owner is final authority (EH-0010).

---

## 1. Purpose

Map **every** point where a capability can be reached and define **where policy must be enforced**. The
Sprint 2 audit's central finding: Hermes has **no single complete chokepoint** and **registry dispatch
alone is insufficient**. This map closes that gap — on paper — by enumerating all paths and assigning each
a gate (or a removal).

## 2. The thirteen policy boundaries

| # | Boundary | Hermes evidence (@ 33b1d144) | Required policy action | Default |
|---|---|---|---|---|
| P-01 | **startup** | `run_agent.py`, toolset assembly `toolsets.py::_HERMES_CORE_TOOLS` | Build active toolset from Magna policy, not Hermes config; deny-by-default | deny |
| P-02 | **tool registry** | `tools/registry.py::register`, `discover_builtin_tools` | Register only policy-allowed tools; dangerous tools not registered (T3) | deny |
| P-03 | **model tool dispatch** | `model_tools.py::handle_function_call`, `agent/tool_executor.py` | Primary gate: classify + enforce capability state | deny |
| P-04 | **agent-owned tools** | `model_tools.py::_AGENT_LOOP_TOOLS = {todo, memory, session_search, delegate_task}` | Route through same policy path (cannot rely on registry alone) | deny |
| P-05 | **cron / scheduler** | `cron/scheduler.py::tick`, `run_job`, `cron/jobs.py` | Execution disabled; schedules → report-only objects | report_only |
| P-06 | **gateway / API** | `gateway/run.py`, `gateway/platforms/api_server.py::connect/_handle_runs/_handle_run_approval` | Listener not started (T1); inbound runs denied | disabled |
| P-07 | **ACP tools** | `acp_adapter/tools.py` (delegate_task, memory, cronjob, send_message) | Map to same policy; no independent capability grant | deny |
| P-08 | **provider / model calls** | `providers/*`, `plugins/model-providers/*`, `agent/*_adapter.py` | Disabled at provider resolution + import (T2) | disabled |
| P-09 | **memory persistence** | `tools/memory_tool.py::MemoryStore.save_to_disk`, `agent/memory_manager.py` | draft-only staging; external mirror disabled | draft_only |
| P-10 | **skill persistence** | `tools/skill_manager_tool.py::skill_manage` | draft-only staging; no auto-activation | draft_only |
| P-11 | **plugin loading** | `hermes_cli/plugins/*`, plugin pre-tool-call hooks | Loader disabled unless signed allowlist; not a security boundary itself | disabled |
| P-12 | **MCP loading** | `tools/mcp_tool.py`, `tui_gateway/entry.py` background discovery | Dynamic registration disabled; surface fixed at startup | disabled |
| P-13 | **outbound delivery** | `tools/send_message_tool.py`, `cron/scheduler.py::_deliver_result` | Shutdown; no outbound in MVP | disabled |

## 3. Coverage matrix (capability category × boundary)

For each capability category (C-01…C-20), the design must show every boundary it can be reached through is
gated or removed. Illustrative high-risk rows:

| Capability | Reaches via | Gate/removal |
|---|---|---|
| terminal_execution (C-06) | P-03, P-04, P-05 (cron), P-07 (ACP), P-06 (gateway) | gate at P-03/P-04; **remove** cron no_agent + remote backend; listener off (P-06) |
| persistent_memory (C-03) | P-03, P-04, P-05, P-07, P-09 | draft-only at P-09; route P-04/P-07 to same gate |
| cloud_provider (C-11) | P-08, P-03, P-06, P-11/P-12 | disable at P-08 (T2); plugin/MCP off |
| messaging_outbound (C-12) | P-13, P-05, P-06 | shutdown P-13; cron delivery removed; listener off |
| delegation (C-14) | P-04, P-07 | unregister (T3); ACP mapping denied |
| plugin/MCP (C-15) | P-11, P-12 | loader off unless signed allowlist |

## 4. The single-chokepoint goal vs. reality

Ideal: one gate. Reality (Sprint 2): Hermes spreads invocation across P-01…P-13. The design therefore:
1. **Consolidates** as many paths as possible onto the P-03 model-dispatch gate (including agent-owned P-04
   and ACP P-07, which must be routed through the same policy path — not left to registry dispatch alone).
2. **Removes or process-disables** paths that cannot be consolidated (P-05 cron execution, P-06 gateway,
   P-08 providers, P-11/P-12 plugin/MCP, P-13 outbound) at tiers T1–T3.
3. Accepts the design **only when every boundary is gated or removed** — no "mostly covered".

## 5. Bypass-resistance (feeds Sprint 4 gate 10)

For each capability the design lists all boundaries it can be reached through and shows each is gated or
removed. A capability reachable by any uncovered boundary is treated as `disabled` (default-deny) and the
boundary flagged for removal before that capability may be enabled.

## 6. Boundaries

Design only. No instrumentation added to any code. This map tells Sprint 4 exactly where to place the
policy gate and what to remove.
