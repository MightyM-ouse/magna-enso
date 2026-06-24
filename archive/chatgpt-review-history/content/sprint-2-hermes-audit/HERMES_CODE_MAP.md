# Hermes Code Map

## Purpose

Map Hermes Agent source architecture and identify modules relevant or risky for Magna Enso.

## Files Inspected

- `README.md`
- `run_agent.py`
- `agent/conversation_loop.py`
- `agent/tool_executor.py`
- `agent/background_review.py`
- `agent/memory_manager.py`
- `agent/curator.py`
- `model_tools.py`
- `toolsets.py`
- `tools/registry.py`
- `tools/memory_tool.py`
- `tools/skill_manager_tool.py`
- `tools/write_approval.py`
- `tools/terminal_tool.py`
- `tools/code_execution_tool.py`
- `tools/browser_tool.py`
- `tools/browser_cdp_tool.py`
- `tools/cronjob_tools.py`
- `tools/send_message_tool.py`
- `cron/jobs.py`
- `cron/scheduler.py`
- `gateway/run.py`
- `gateway/platforms/api_server.py`
- `providers/base.py`
- `providers/__init__.py`
- `plugins/model-providers/*`
- `plugins/platforms/*`
- `plugins/browser/*`

## Findings

Hermes is a Python-first agent platform with multiple outer shells and integration planes:

- Core agent: `run_agent.py::AIAgent`, `agent/conversation_loop.py::run_conversation`, `agent/tool_executor.py`
- Tool registry: `tools/registry.py::ToolRegistry`, `model_tools.py::handle_function_call`, tool modules under `tools/`
- Toolset policy grouping: `toolsets.py`
- Skills: local skill material under `skills/`, agent-writeable skills via `tools/skill_manager_tool.py`
- Memory: built-in memory files via `tools/memory_tool.py`, external memory provider orchestration via `agent/memory_manager.py`
- Scheduling: `tools/cronjob_tools.py`, `cron/jobs.py`, `cron/scheduler.py`
- Terminal/code execution: `tools/terminal_tool.py`, `tools/code_execution_tool.py`, `tools/environments/*`
- Browser/computer use: `tools/browser_tool.py`, `tools/browser_cdp_tool.py`, `agent/browser_registry.py`, `plugins/browser/*`
- Messaging/API gateways: `gateway/run.py`, `gateway/platforms/*`, `plugins/platforms/*`
- Provider/model adapters: `providers/*`, `plugins/model-providers/*`, model adapters under `agent/`
- UI surfaces: `web/`, `ui-tui/`, `tui_gateway/`, `apps/desktop/`
- Protocol adapters: `acp_adapter/`, MCP discovery under `tools/mcp_tool.py`

## Relevant Modules For Magna Enso

- `tools/registry.py` and `model_tools.py` are useful as a capability catalog and dispatch abstraction.
- `toolsets.py` is useful as a starting point for Magna capability grouping.
- `agent/tool_executor.py` is a likely policy insertion point.
- `tools/write_approval.py` is directly relevant to draft-only memory and skill staging.
- `tools/memory_tool.py` and `tools/skill_manager_tool.py` contain reusable persistence/write abstractions if forced through policy.
- `cron/jobs.py` has reusable job metadata mechanics, but execution must be report-only initially.
- `tools/terminal_tool.py` and `tools/code_execution_tool.py` are useful only behind approval-required gates.
- Provider/plugin abstractions are useful, but cloud providers must be disabled by default.

## Risky Modules

- Autonomous self-improvement: `agent/background_review.py`, `agent/curator.py`
- Scheduled execution: `cron/scheduler.py`, `tools/cronjob_tools.py`
- Tool execution and side effects: `agent/tool_executor.py`, `model_tools.py`, `tools/registry.py`
- Terminal/code execution: `tools/terminal_tool.py`, `tools/code_execution_tool.py`, `tools/environments/*`
- Browser/computer use: `tools/browser_tool.py`, `tools/browser_cdp_tool.py`, `tools/computer_use_tool.py`
- Messaging and listeners: `gateway/run.py`, `gateway/platforms/*`, `plugins/platforms/*`, `tools/send_message_tool.py`
- External memory: `agent/memory_manager.py`, `plugins/memory/honcho/__init__.py`
- MCP/plugin dynamic registration: `tools/mcp_tool.py`, `hermes_cli/plugins/*`

## Evidence Paths

- `README.md` describes self-improvement, memory, scheduling, delegation, terminal backends, and messaging gateways.
- `tools/registry.py::discover_builtin_tools`, `ToolRegistry.register`, `ToolRegistry.dispatch`
- `model_tools.py::handle_function_call`
- `agent/tool_executor.py::execute_tool_calls_sequential`, `execute_tool_calls_concurrent`
- `toolsets.py::_HERMES_CORE_TOOLS`
- `cron/scheduler.py::tick`, `cron/scheduler.py::run_job`
- `gateway/platforms/api_server.py::connect`

## Confidence Level

Medium-high. The core architecture and main surfaces were mapped from source. Not every plugin implementation was deeply inspected.

## Risks

- Hermes has multiple dispatch and execution paths, so a single registry gate is not enough.
- Optional plugins and MCP tools can change available capabilities at runtime.
- Scheduler and gateway paths can invoke agent runs outside a direct user interaction.

## Open Questions

- Which UI/runtime shells would be retained in a governed Sprint 4 fork?
- Whether plugin discovery should be removed entirely or replaced by an allowlist.
- Whether external memory providers should be deleted instead of governed.

## Recommendation

Hermes has a useful architecture for a governed fork, but only if Sprint 3 defines a default-deny capability layer before Sprint 4 copies or forks any code.
