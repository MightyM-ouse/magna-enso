# Magna Enso Reuse Recommendation

## Purpose

Provide the final technical recommendation on whether Hermes Agent is suitable as the future Sprint 4 clean governed Hermes fork baseline for Magna Enso.

## Files Inspected

- `README.md`
- `run_agent.py`
- `agent/conversation_loop.py`
- `agent/tool_executor.py`
- `agent/background_review.py`
- `agent/memory_manager.py`
- `model_tools.py`
- `toolsets.py`
- `tools/registry.py`
- `tools/approval.py`
- `tools/write_approval.py`
- `tools/memory_tool.py`
- `tools/skill_manager_tool.py`
- `tools/terminal_tool.py`
- `tools/code_execution_tool.py`
- `tools/browser_tool.py`
- `tools/cronjob_tools.py`
- `cron/jobs.py`
- `cron/scheduler.py`
- `gateway/run.py`
- `gateway/platforms/api_server.py`
- `providers/*`
- `plugins/*`

## Findings

Final recommendation: conditionally suitable.

Hermes is technically strong enough to serve as a future governed fork baseline, but not in its current default form. It has useful architecture, modular tool registration, provider abstractions, approval primitives, and write-staging primitives. It also has high-risk autonomy and external surface area that must be disabled, staged, or removed before adoption.

## Top Reusable Parts

- Agent loop and orchestration pattern: `run_agent.py`, `agent/conversation_loop.py`
- Tool registry and schemas: `tools/registry.py`, `model_tools.py`
- Toolset grouping concept: `toolsets.py`
- Approval primitives for terminal/code execution: `tools/approval.py`
- Write-staging concept for memory/skills: `tools/write_approval.py`
- Memory and skill abstractions, only if forced through draft policy: `tools/memory_tool.py`, `tools/skill_manager_tool.py`
- Provider adapter concept, not default provider list: `providers/`, `plugins/model-providers/`
- Scheduler data model as report-only reference: `cron/jobs.py`

## Parts To Preserve With Governance

- Registry and dispatcher pattern.
- Typed tool schemas and toolset names.
- Existing terminal/code approval primitives.
- Write approval staging mechanisms.
- Prompt/session/workflow separation in the core agent loop.

## Parts To Disable By Default

- Background self-improvement and curator loops.
- Cron execution and cron delivery.
- Messaging gateways and API server listeners.
- MCP and plugin dynamic registration.
- Cloud provider calls and fallbacks.
- Browser action tools.
- Terminal/process/code execution.
- External memory providers.
- Subagent delegation.

## Parts To Remove If Ungovernable

- `cron/scheduler.py` direct script/no-agent execution.
- External memory plugins that cannot stage writes.
- Platform adapters not needed for Magna MVP.
- Remote execution backends such as Modal, Daytona, SSH, and managed gateways.
- Dynamic MCP/plugin loading if a signed allowlist is not implemented.

## Major Risks

- No single complete policy chokepoint exists yet.
- Default capabilities are much broader than Magna MVP needs.
- Autonomous background and scheduled paths can create hidden side effects.
- Cloud/messaging/browser/terminal surfaces require explicit privacy and approval policies.
- Optional dependencies and plugins enlarge the supply-chain review burden.

## Recommendation For Sprint 3

Do not implement Hermes adoption. Sprint 3 should be a governance-design sprint:

- Define Magna capability states and default-deny policy.
- Specify policy insertion points across dispatcher, registry, cron, gateway, provider, memory, skill, ACP, plugin, and MCP paths.
- Decide which Hermes modules are excluded from the Sprint 4 fork.
- Define draft-only memory/skill behavior and report-only scheduler behavior.
- Produce an Antigravity validation review of this audit.

## Recommendation For Sprint 4

Only create a clean governed Hermes fork after Sprint 3 approves the policy architecture. The fork should start from a pinned audited SHA, remove or disable risky surfaces at the boundary, and prove that memory/skill writes, terminal execution, browser actions, cloud calls, messaging, and scheduling cannot bypass policy.

## Evidence Paths

- `tools/registry.py`
- `model_tools.py`
- `agent/tool_executor.py`
- `tools/write_approval.py`
- `tools/approval.py`
- `agent/background_review.py`
- `cron/scheduler.py`
- `gateway/platforms/api_server.py`
- `tools/terminal_tool.py`
- `tools/code_execution_tool.py`
- `tools/browser_tool.py`

## Confidence Level

Medium-high. The recommendation is based on source inspection of major architecture and risk surfaces, with plugin-level depth intentionally bounded by Sprint 2 scope.

## Risks

- Suitability could change if Sprint 4 targets a newer Hermes commit.
- A future fork could become unsafe if governance is added only to the happy-path dispatcher.

## Open Questions

- Which exact module subset should Sprint 4 include?
- Should Magna remove all messaging and remote execution code from the first fork instead of disabling it?
- Should Antigravity perform a second independent source audit before human acceptance?

## Recommendation

Hermes Agent is conditionally suitable as a technical base for a future Sprint 4 clean governed fork. It is not suitable for direct adoption, activation, or implementation in Magna Enso at this stage.
