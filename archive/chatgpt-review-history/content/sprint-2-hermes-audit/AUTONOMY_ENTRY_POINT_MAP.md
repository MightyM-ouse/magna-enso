# Autonomy Entry Point Map

## Purpose

Identify Hermes behaviors that can act without a direct one-shot user command and classify them for Magna Enso governance.

## Files Inspected

- `agent/background_review.py`
- `agent/curator.py`
- `agent/memory_manager.py`
- `tools/memory_tool.py`
- `tools/skill_manager_tool.py`
- `tools/write_approval.py`
- `tools/cronjob_tools.py`
- `cron/jobs.py`
- `cron/scheduler.py`
- `tools/delegate_tool.py`
- `run_agent.py`
- `gateway/run.py`
- `tui_gateway/entry.py`
- `tools/mcp_tool.py`

## Findings

Count clarification: This audit identifies 13 autonomy entry points. Earlier wording referring to 12 entry points should be treated as an approximation; the table contains the authoritative count.

| Entry Point | Evidence | Classification | Notes |
|---|---|---:|---|
| Background self-improvement review | `agent/background_review.py::spawn_background_review_thread`, `_background_review_worker` | Needs disable | Forks an agent in a daemon thread and can write memory/skills unless staging is forced. |
| Curator/self-review loop | `agent/curator.py` daemon review paths | Needs report-only | Useful as analysis only; not acceptable as active mutation in Magna MVP. |
| Autonomous skill creation/editing | `tools/skill_manager_tool.py::skill_manage` | Needs draft-only | Has validation and optional staging; default must be forced to draft/staged. |
| Memory writes | `tools/memory_tool.py::memory_tool`, `MemoryStore.save_to_disk` | Needs draft-only | Built-in write approval exists but is not guaranteed default. |
| External memory mirroring | `agent/memory_manager.py::on_memory_write`, `sync_all` | Needs disable | Can perform external provider writes/background sync. |
| Scheduled jobs | `tools/cronjob_tools.py::cronjob_tool`, `cron/scheduler.py::tick`, `run_job` | Needs report-only | Scheduler can launch agents, scripts, provider calls, tools, and delivery. |
| Direct script cron path | `cron/scheduler.py::run_job` `no_agent` path | Needs removal or approval-required | Runs scripts without LLM. Not acceptable in governed MVP without explicit approval. |
| Subagent spawning | `tools/delegate_tool.py`, `run_agent.py::_dispatch_delegate_task` | Approval-required or disabled | Delegation expands autonomy and tool-use scope. |
| Background processes | `tools/terminal_tool.py`, `tools/process_registry.py` | Approval-required | Long-running processes require explicit human approval and tracking. |
| Browser actions | `tools/browser_tool.py` registered click/type/navigate/press/scroll | Approval-required | Read-only browser snapshot may be governable separately. |
| Dynamic MCP tools | `tools/mcp_tool.py`, `tui_gateway/entry.py` background discovery | Needs disable | Runtime tool surface can change after startup. |
| Gateway-triggered agent runs | `gateway/run.py`, `gateway/platforms/api_server.py` | Disabled by default | Inbound messages/API runs are external autonomy entry points. |
| Unsolicited outbound delivery | `tools/send_message_tool.py`, `cron/scheduler.py::_deliver_result` | Disabled by default | Outbound messages must not be active in Magna MVP. |

## Evidence Paths

- `agent/background_review.py::_background_review_worker`
- `agent/background_review.py::spawn_background_review_thread`
- `tools/skill_manager_tool.py::skill_manage`
- `tools/memory_tool.py::MemoryStore.save_to_disk`
- `tools/write_approval.py::stage_write`
- `cron/scheduler.py::tick`
- `cron/scheduler.py::run_job`
- `tools/delegate_tool.py`
- `gateway/run.py`
- `tools/send_message_tool.py`

## Confidence Level

Medium-high. The main autonomy paths were identified. Some plugin-specific background workers may remain unclassified.

## Risks

- Background review and scheduler can create state changes after the user-visible turn.
- Cron jobs can execute scripts directly through `no_agent`.
- External memory providers may sync/write outside built-in memory staging.
- Gateway surfaces can accept remote triggers if enabled.

## Open Questions

- Should Sprint 4 delete background review and curator code or leave it disabled behind policy?
- Should all cron creation become report-only metadata in Magna rather than executable jobs?
- Should external memory providers be removed entirely from the fork baseline?

## Recommendation

For a governed Magna fork, disable background review, curator, cron execution, external memory, dynamic MCP, messaging, and subagents by default. Permit memory and skill mutations only as draft-only staged artifacts until a human accepts them.
