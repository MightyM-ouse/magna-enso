# HERMES_SURFACE_GOVERNANCE_MATRIX.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 14 of 17 — Hermes Surface Governance Matrix
# Type: Design-only governance report. No code.
# Date: 2026-06-17
# Inputs: Sprint 2 audit (Hermes @ 33b1d144)
# Status: Design only. Human owner is final authority (EH-0010).

---

## 1. Purpose

The consolidated decision table: for every Hermes surface, its **MVP state**, **future state**,
**enforcement tier**, and the **Sprint 4 action** (keep-and-gate / disable / remove). This matrix is the
single reference Sprint 4 implements against.

## 2. Matrix

| Surface | MVP state | Future state | Enforcement tier | Sprint 4 action |
|---|---|---|---|---|
| Background review (`agent/background_review.py`) | `disabled` | `report_only` (maybe) | T1/T2 | **Remove** |
| Curator / self-review (`agent/curator.py`) | `report_only` | `report_only` | T3 | Keep code, execution off; emit reports only |
| Memory writes (`tools/memory_tool.py`) | `draft_only` | `draft_only` | gate (P-09) | Keep; force non-bypassable staging |
| Skill writes (`tools/skill_manager_tool.py`) | `draft_only` | `draft_only` | gate (P-10) | Keep; force staging; no auto-activation |
| External memory (`agent/memory_manager.py` sync) | `disabled` | `disabled` | T1/T2 | **Remove** mirroring/sync |
| Cron scheduler (`cron/scheduler.py`) | `report_only` | `report_only` | T3 | Disable execution; schedules → reports |
| Direct script cron (`run_job` `no_agent`) | `disabled` | `disabled` | T1/T2 | **Remove** |
| Subagent delegation (`tools/delegate_tool.py`) | `disabled` | `approval_required` (maybe) | T3 | Unregister in MVP |
| Browser snapshot (`tools/browser_tool.py::browser_snapshot`) | `read_only` | `read_only` | gate | Keep as read-only |
| Browser actions (navigate/click/type/press/scroll) | `approval_required` / `disabled` | `approval_required` | T3/T4 | Disable or gate per action |
| Terminal / code (`tools/terminal_tool.py`, `tools/code_execution_tool.py`) | `approval_required`, off by default | `approval_required` | T4 + gate | Keep; close all bypass paths |
| Remote execution backends (`tools/environments/modal.py`, `daytona.py`, `ssh.py`) | `disabled` | `disabled` | T1/T2 | **Remove** (prefer) |
| Messaging gateways (`gateway/platforms/*`, `plugins/platforms/*`) | `disabled` | `disabled` | T1 | **Remove / not launched** |
| API server listener (`gateway/platforms/api_server.py`) | `disabled` | `disabled` | T1 | Not started |
| Cloud providers (`providers/*`, `plugins/model-providers/*`) | `disabled` | `approval_required` (maybe) | T2 | Disable at import/resolution |
| Plugin / MCP loading (`tools/mcp_tool.py`, `hermes_cli/plugins/*`) | `disabled` unless signed allowlist | `disabled`/allowlist | T2/T3 | Disable dynamic loader |
| Outbound delivery (`tools/send_message_tool.py`, `cron/scheduler.py::_deliver_result`) | `disabled` | `disabled` | T1/removed | Shutdown all delivery paths |

## 3. Retain / remove summary (for Sprint 4)

**Retain (behind gate / staged):** agent loop & orchestration (`run_agent.py`, `agent/conversation_loop.py`,
`agent/tool_executor.py`), tool registry (`tools/registry.py`), approval/staging primitives
(`tools/approval.py`, `tools/write_approval.py`), memory (`draft_only`), skills (`draft_only`),
terminal/code (`approval_required`, off by default), browser snapshot (`read_only`), curator (`report_only`).

**Remove:** background review, external memory sync, direct-script cron (`no_agent`), remote execution
backends, messaging gateways + outbound delivery, dynamic plugin/MCP loader (until signed allowlist).

**Disable (not started / not imported):** API listener, gateways, cloud providers, inbound triggers,
delegation (MVP).

## 4. Enforcement note

Every retained capability is governed by default-deny + the policy gate (P-03/P-04) and, where it acts,
the unified approval engine. Every removed/disabled surface uses the strongest feasible tier (T1–T3), not
config-only (T5). This matrix + `POLICY_CHOKEPOINT_MAP.md` together must show **no ungated path** to any
non-`disabled` capability.

## 5. Boundaries

Design only. Sprint 4 implements this matrix in the clean governed fork; nothing is removed/disabled in Sprint 3.
