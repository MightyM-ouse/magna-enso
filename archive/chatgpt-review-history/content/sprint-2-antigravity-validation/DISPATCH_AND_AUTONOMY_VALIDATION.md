# DISPATCH_AND_AUTONOMY_VALIDATION.md
# Magna Enso — Sprint 2 Hermes Read-Only Audit
# Dispatch and Autonomy Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Validate Codex's claims about Hermes action dispatch chokepoints and autonomy entry points.
Assess whether the finding that "Hermes does not have one complete policy chokepoint" is
accurate, and whether all significant autonomy entry points were covered.

---

## 2. Action Dispatch Coverage Validation

### 2.1 Main Dispatch Chain Claimed

ACTION_DISPATCH_MAP.md identifies this dispatch chain:
  1. run_agent.py::AIAgent._execute_tool_calls
  2. agent/tool_executor.py::execute_tool_calls_sequential / execute_tool_calls_concurrent
  3. run_agent.py::AIAgent._invoke_tool
  4. agent/agent_runtime_helpers.py::invoke_tool
  5. model_tools.py::handle_function_call
  6. tools/registry.py::ToolRegistry.dispatch
  7. Concrete tool handler

Assessment: This is a complete and credible main-path dispatch chain for a Python agent
framework of this type. The chain correctly identifies the standard model-tool-call path
from the outer agent loop down through the registry dispatcher.

### 2.2 Non-Registry / Agent-Owned Exception Paths Claimed

ACTION_DISPATCH_MAP.md identifies these bypass paths:
  - model_tools.py: _AGENT_LOOP_TOOLS = {"todo", "memory", "session_search", "delegate_task"}
    These are handled specially, bypassing or pre-empting registry dispatch.
  - acp_adapter/tools.py: handles delegate_task, memory, cronjob, send_message independently
  - cron/scheduler.py::run_job: constructs AIAgent; can run "no_agent" scripts directly
  - Gateway/API surfaces: create runs and resolve approvals outside the CLI path

Assessment: These non-registry paths are precisely the most dangerous from a governance
perspective. The identification of agent-owned tools (_AGENT_LOOP_TOOLS) as a bypass
category is an important and non-obvious finding. A naive policy implementation that only
gates the registry would miss these. The report is correct.

### 2.3 Existing Gates and Approvals in Hermes

ACTION_DISPATCH_MAP.md documents:
  - agent/tool_executor.py: request middleware, plugin pre-tool-call hooks, guardrails
  - model_tools.py::handle_function_call: Tool Search unwrapping, request middleware,
    plugin pre-tool-call block hooks, ACP edit approval for file mutation
  - tools/approval.py: gates terminal and execute_code operations
  - tools/write_approval.py: staging for memory/skill writes (configurable, not default)
  - tools/terminal_tool.py: calls tools.approval.check_all_command_guards
  - tools/code_execution_tool.py: calls tools.approval.check_execute_code_guard

Assessment: Correct identification of Hermes' partial approval infrastructure. The critical
finding — that write_approval.py is configurable and not a guaranteed default — is
substantively important for Magna Sprint 3 governance design. This is accurate.

### 2.4 Chokepoint Insufficiency Claim Validation

CLAIM: "A single policy chokepoint does not currently exist. Registry dispatch is necessary
but insufficient because agent-loop tools, cron scripts, gateways, ACP tools, MCP
registration, and background review have separate paths."

VALIDATION:
- registry dispatch covers: standard model tool-call path
- DOES NOT cover: agent-owned tools (todo, memory, session_search, delegate_task)
- DOES NOT cover: cron/scheduler.py direct script execution (no_agent path)
- DOES NOT cover: gateway/API run creation
- DOES NOT cover: acp_adapter independent handling
- DOES NOT cover: background_review thread spawning
- DOES NOT cover: dynamic MCP registration at startup

Assessment: The claim is ACCURATE and appropriately conservative. A policy engine that
only wraps ToolRegistry.dispatch would miss at least 6 significant paths. The required
multi-point policy layer identified in the report (tool_executor, model_tools, agent-owned
handlers, cron, gateway, ACP, plugin/MCP registration) is the correct architectural
prescription.

Antigravity Assessment of Chokepoint Gap Severity: HIGH
This is the most important architectural finding of Sprint 2. It directly drives Sprint 3
scope and shapes the Sprint 4 fork risk profile.

---

## 3. Autonomy Entry Point Coverage Validation

### 3.1 Entry Points Claimed by Codex

AUTONOMY_ENTRY_POINT_MAP.md documents 12 autonomy entry points:

| # | Entry Point | Evidence Cited | Classification | Validation |
|---|---|---|---|---|
| 1 | Background self-improvement | agent/background_review.py::spawn_background_review_thread | Needs disable | CREDIBLE — daemon thread + memory/skill write capability |
| 2 | Curator/self-review loop | agent/curator.py daemon paths | Needs report-only | CREDIBLE — self-review loops are a known autonomy pattern |
| 3 | Autonomous skill creation/editing | tools/skill_manager_tool.py::skill_manage | Needs draft-only | CREDIBLE — skill writes are persistent and model-driven |
| 4 | Memory writes | tools/memory_tool.py::memory_tool, MemoryStore.save_to_disk | Needs draft-only | CREDIBLE — disk-persistent memory without guaranteed gating |
| 5 | External memory mirroring | agent/memory_manager.py::on_memory_write, sync_all | Needs disable | CREDIBLE — external provider writes are high-risk |
| 6 | Scheduled jobs | cron/scheduler.py::tick, run_job | Needs report-only | CREDIBLE — scheduler can invoke full agent runs |
| 7 | Direct script cron path | cron/scheduler.py::run_job no_agent path | Needs removal or approval-required | CREDIBLE — script execution without LLM gateway |
| 8 | Subagent spawning | tools/delegate_tool.py, _dispatch_delegate_task | Approval-required or disabled | CREDIBLE — expands autonomy scope unpredictably |
| 9 | Background processes | tools/terminal_tool.py, process_registry.py | Approval-required | CREDIBLE — long-running processes without turn boundary |
| 10 | Browser actions | tools/browser_tool.py click/type/navigate/press/scroll | Approval-required | CREDIBLE — active external side effects |
| 11 | Dynamic MCP tools | tools/mcp_tool.py, tui_gateway/entry.py background discovery | Needs disable | CREDIBLE — runtime capability surface expansion |
| 12 | Gateway-triggered agent runs | gateway/run.py, api_server.py | Disabled by default | CREDIBLE — external trigger for autonomous runs |
| 13 | Unsolicited outbound delivery | tools/send_message_tool.py, cron/_deliver_result | Disabled by default | CREDIBLE — agent-initiated outbound messaging |

Note: 13 entry points are listed in the table, though the report describes 12. The table
includes "Unsolicited outbound delivery" as entry 13/row 13. This is a minor counting
discrepancy, not a gap — all entries are substantively correct.

### 3.2 Coverage Assessment

All mandatory autonomy categories from the validation checklist are covered:

| Required Category | Covered? | Evidence |
|---|---|---|
| Background self-improvement | YES | entry 1 |
| Curator/self-review | YES | entry 2 |
| Autonomous skill creation | YES | entry 3 |
| Memory writes | YES | entry 4 |
| External memory sync | YES | entry 5 |
| Scheduled jobs | YES | entry 6 |
| Direct script cron path | YES | entry 7 |
| Subagent spawning | YES | entry 8 |
| Background processes | YES | entry 9 |
| Browser actions | YES | entry 10 |
| Dynamic MCP tools | YES | entry 11 |
| Gateway-triggered runs | YES | entry 12 |
| Outbound delivery | YES | entry 13 |

Coverage: 13/13 required categories — COMPLETE.

### 3.3 Classification Quality Assessment

| Classification | Antigravity Assessment |
|---|---|
| Background review: Needs disable | CORRECT — daemon thread creating state changes post-turn is unacceptable in Magna MVP |
| Curator: Needs report-only | CORRECT — analysis-only is appropriate if execution is bypassed |
| Skill writes: Needs draft-only | CORRECT — model-driven persistent writes need staging gate |
| Memory writes: Needs draft-only | CORRECT — consistent with write_approval.py intent |
| External memory: Needs disable | CORRECT — external provider sync is high risk (R-07, R-08) |
| Scheduled jobs: Needs report-only | CORRECT — metadata creation is acceptable; execution is not |
| Direct script cron: Needs removal or approval | CORRECT — script execution without LLM is an ungated autonomy path |
| Subagent spawning: Approval-required or disabled | CORRECT — scope expansion must require human approval |
| Background processes: Approval-required | CORRECT — consistent with terminal/code approval pattern |
| Browser actions: Approval-required | CORRECT — active external side effects, but separable from snapshot |
| Dynamic MCP: Needs disable | CORRECT — runtime capability expansion is incompatible with default-deny |
| Gateway runs: Disabled by default | CORRECT — external triggers for autonomous runs must be off-by-default |
| Outbound delivery: Disabled by default | CORRECT — agent-initiated messaging must not be active |

All classifications are CORRECTLY CALIBRATED to Magna governance requirements.

---

## 4. Partial Autonomy Coverage Gap

One category that may warrant deeper analysis in Sprint 3:

- Autonomous subagent chains (multi-level delegation): delegate_tool.py spawns a full
  AIAgent, which itself can spawn further delegates. The report documents this correctly
  but the classification ("approval-required or disabled") should ideally clarify that
  in Magna MVP, multi-level delegation must be DISABLED not merely approval-required,
  because approving one level does not bound the recursion depth.

This is a Sprint 3 governance design question, not a Sprint 2 audit gap. The Sprint 2
finding is accurate; the distinction is a refinement for Sprint 3.

---

## 5. Dispatch and Autonomy Verdict

```
Main dispatch chain:       ACCURATELY MAPPED
Non-registry bypass paths: ACCURATELY IDENTIFIED
Existing gates:            ACCURATELY ASSESSED (partial, not complete)
Chokepoint gap finding:    CONFIRMED — Hermes does NOT have one complete policy chokepoint
Autonomy entry points:     13/13 categories covered — COMPLETE
Classifications:           All 13 classifications are correctly calibrated

DISPATCH AND AUTONOMY VALIDATION: PASS
Substantive findings are correct and important for Sprint 3 scope definition.
```
