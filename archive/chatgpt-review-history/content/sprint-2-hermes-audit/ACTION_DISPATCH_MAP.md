# Action Dispatch Map

## Purpose

Identify where Hermes registers tools/actions, dispatches calls, applies approvals/gates, and performs side effects.

## Files Inspected

- `run_agent.py`
- `agent/conversation_loop.py`
- `agent/tool_executor.py`
- `agent/agent_runtime_helpers.py`
- `model_tools.py`
- `tools/registry.py`
- `toolsets.py`
- `tools/approval.py`
- `tools/write_approval.py`
- `tools/terminal_tool.py`
- `tools/code_execution_tool.py`
- `tools/memory_tool.py`
- `tools/skill_manager_tool.py`
- `tools/cronjob_tools.py`
- `tools/send_message_tool.py`
- `acp_adapter/tools.py`

## Findings

### Registration

- Built-in tool registration is centralized through `tools/registry.py::ToolRegistry.register`.
- `tools/registry.py::discover_builtin_tools` imports tool modules that contain top-level `registry.register(...)` calls.
- Tool modules self-register, including `tools/terminal_tool.py`, `tools/code_execution_tool.py`, `tools/browser_tool.py`, `tools/cronjob_tools.py`, `tools/memory_tool.py`, and `tools/skill_manager_tool.py`.
- Tool grouping is defined in `toolsets.py`; `_HERMES_CORE_TOOLS` grants broad default capability to many platform toolsets.

### Main Dispatch Path

The normal model tool-call path is:

1. `run_agent.py::AIAgent._execute_tool_calls`
2. `agent/tool_executor.py::execute_tool_calls_sequential` or `execute_tool_calls_concurrent`
3. `run_agent.py::AIAgent._invoke_tool`
4. `agent/agent_runtime_helpers.py::invoke_tool`
5. `model_tools.py::handle_function_call`
6. `tools/registry.py::ToolRegistry.dispatch`
7. Concrete tool handler

### Non-Registry Or Agent-Owned Exceptions

- `model_tools.py` defines `_AGENT_LOOP_TOOLS = {"todo", "memory", "session_search", "delegate_task"}`. These require special handling and cannot be governed by registry dispatch alone.
- ACP tool handling in `acp_adapter/tools.py` maps capabilities independently and includes `delegate_task`, `memory`, `cronjob`, and `send_message`.
- Cron execution in `cron/scheduler.py::run_job` constructs an `AIAgent` and can also run `no_agent` scripts directly.
- Gateway/API surfaces create runs and resolve approvals outside the CLI path.

### Existing Gates And Approvals

- `agent/tool_executor.py` applies request middleware, plugin pre-tool-call hooks, tool-loop guardrails, and checkpoint logic before invocation.
- `model_tools.py::handle_function_call` applies Tool Search unwrapping, request middleware, plugin pre-tool-call block hooks, ACP edit approval for file mutation, and registry dispatch.
- `tools/approval.py` gates dangerous terminal and `execute_code` operations.
- `tools/write_approval.py` can stage memory and skill writes, but the report found this is configurable and not a guaranteed default.
- `tools/terminal_tool.py::terminal_tool` calls `tools.approval.check_all_command_guards`.
- `tools/code_execution_tool.py::execute_code` calls `tools.approval.check_execute_code_guard`.

### Side-Effect Locations

- Terminal and process execution: `tools/terminal_tool.py`, `tools/process_registry.py`
- Python code execution: `tools/code_execution_tool.py`
- Memory writes: `tools/memory_tool.py`, external provider mirroring in `agent/memory_manager.py`
- Skill writes: `tools/skill_manager_tool.py`
- Scheduled jobs: `tools/cronjob_tools.py`, `cron/jobs.py`, `cron/scheduler.py`
- Browser actions: `tools/browser_tool.py`, `tools/browser_cdp_tool.py`
- Messaging delivery: `tools/send_message_tool.py`, `cron/scheduler.py::_deliver_result`, gateway platform adapters
- Dynamic MCP/plugin tools: `tools/mcp_tool.py`, `hermes_cli/plugins/*`

## Evidence Paths

- `tools/registry.py::discover_builtin_tools`
- `tools/registry.py::ToolRegistry.register`
- `tools/registry.py::ToolRegistry.dispatch`
- `model_tools.py::handle_function_call`
- `agent/tool_executor.py`
- `toolsets.py::_HERMES_CORE_TOOLS`
- `tools/terminal_tool.py::terminal_tool`
- `tools/code_execution_tool.py::execute_code`
- `tools/write_approval.py::evaluate_gate`
- `tools/cronjob_tools.py::cronjob_tool`

## Confidence Level

High for the main dispatch path. Medium for plugin/MCP edge paths because all plugin hooks were not exhaustively traced.

## Risks

- A single policy chokepoint does not currently exist.
- Registry dispatch is necessary but insufficient because agent-loop tools, cron scripts, gateways, ACP tools, MCP registration, and background review have separate paths.
- Plugin pre-tool-call hooks can block calls, but a governed fork should not depend on plugin hooks as the primary security boundary.

## Open Questions

- Should Magna Enso replace Hermes dispatch with a single policy engine wrapper, or patch all known entry points?
- Should agent-owned tools like `memory` and `delegate_task` be moved behind the same registry policy path?
- Should MCP and plugin tool registration be disabled until there is a signed allowlist?

## Recommendation

Classify Hermes as governable only with a multi-point policy layer. Required chokepoints are `agent/tool_executor.py`, `model_tools.py`, agent-owned tool handlers, `cron/scheduler.py`, gateway/API run creation, ACP tools, and dynamic plugin/MCP registration.
