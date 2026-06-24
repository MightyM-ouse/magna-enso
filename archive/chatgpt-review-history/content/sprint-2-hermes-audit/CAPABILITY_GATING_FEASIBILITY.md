# Capability Gating Feasibility

## Purpose

Evaluate whether Hermes capabilities can be mapped to Magna Enso capability states: `disabled`, `read_only`, `draft_only`, `report_only`, `approval_required`, and `active_safe`.

## Files Inspected

- `toolsets.py`
- `tools/registry.py`
- `model_tools.py`
- `agent/tool_executor.py`
- `tools/tool_guardrails.py`
- `tools/approval.py`
- `tools/write_approval.py`
- `tools/memory_tool.py`
- `tools/skill_manager_tool.py`
- `tools/cronjob_tools.py`
- `cron/scheduler.py`
- `tools/terminal_tool.py`
- `tools/code_execution_tool.py`
- `tools/browser_tool.py`
- `gateway/platforms/api_server.py`
- `tools/send_message_tool.py`

## Findings

Hermes is conditionally governable. It already has useful abstractions, but the default posture is not Magna-safe.

### Central Chokepoint Assessment

- There is a central registry dispatch path in `tools/registry.py::ToolRegistry.dispatch`.
- There is a main model tool-call dispatch path through `agent/tool_executor.py` and `model_tools.py::handle_function_call`.
- There is no single complete policy chokepoint because memory/delegation/session tools, cron scripts, gateways, ACP tools, plugin/MCP registration, and background review have additional paths.

### Capability State Mapping

| Magna State | Hermes Examples | Feasibility |
|---|---|---:|
| `disabled` | Messaging gateways, external memory, cloud providers, MCP, background review, cron execution | High if enforced at registration and startup. |
| `read_only` | File reads/search, session search, browser snapshot, web fetch/search with privacy checks | Medium-high; browser/web require privacy and navigation limits. |
| `draft_only` | Memory writes, skill writes, file writes/patches | Medium; `tools/write_approval.py` supports staging for memory/skills but must be mandatory. |
| `report_only` | Cron schedules, background review, curator suggestions | Medium; execution must be bypassed and replaced by report generation. |
| `approval_required` | Terminal, process, execute_code, browser actions, file transfer, cloud model calls, messaging | Medium-high; terminal/code already have approval primitives, but policy must cover all paths. |
| `active_safe` | Local status, non-mutating UI state, clarify, selected task metadata | High, but should remain narrow. |

### Specific Feasibility Questions

- Can memory writes be staged? Yes for built-in memory via `tools/write_approval.py`, but external memory providers must be disabled or separately staged.
- Can skill writes be draft-only? Yes in principle through `tools/write_approval.py`, but the fork must force the gate on and review all write paths.
- Can scheduler be report-only? Yes if `tools/cronjob_tools.py` can create draft/report objects and `cron/scheduler.py::tick`/`run_job` are disabled.
- Can browser/web be read-only? Partially. `browser_snapshot` is separable from click/type/press/scroll, but `browser_navigate` still initiates outbound activity and needs privacy/approval rules.
- Can terminal be approval-required? Yes, `tools/terminal_tool.py` and `tools/code_execution_tool.py` already call approval guards. Magna must prevent bypasses via cron/no-agent scripts and remote backends.
- Can messaging/cloud be disabled? Yes, but disablement must happen at startup, config, provider resolution, toolset registration, and gateway launch boundaries.

## Evidence Paths

- `toolsets.py::_HERMES_CORE_TOOLS`
- `tools/tool_guardrails.py::MUTATING_TOOL_NAMES`
- `tools/registry.py::ToolRegistry.dispatch`
- `model_tools.py::handle_function_call`
- `agent/tool_executor.py`
- `tools/write_approval.py::stage_write`
- `tools/memory_tool.py::_apply_write_gate`
- `tools/skill_manager_tool.py::_apply_skill_write_gate`
- `cron/scheduler.py::tick`
- `cron/scheduler.py::run_job`
- `gateway/platforms/api_server.py::connect`

## Confidence Level

Medium-high. The feasibility path is clear, but implementation risk remains high because the policy layer must cover multiple entry points.

## Risks

- A registry-only gate will miss autonomy and gateway paths.
- Existing write approval is optional and must be made non-bypassable.
- Dynamic plugin/MCP registration can change capability surface after review.
- Cloud provider selection and fallback logic can route data externally if not disabled.

## Open Questions

- Should Magna enforce policy through a new central capability engine before importing tool modules?
- Should active toolsets be generated from Magna policy instead of Hermes config?
- Should all dynamic plugin/MCP loading be removed from the first fork baseline?

## Recommendation

Proceed only with a Sprint 3 governance design that creates a default-deny capability policy engine and binds it to every dispatch, startup, scheduler, gateway, provider, memory, and skill path before any Sprint 4 fork is approved.
