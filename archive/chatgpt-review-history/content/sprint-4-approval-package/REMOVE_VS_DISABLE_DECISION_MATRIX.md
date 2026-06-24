# REMOVE_VS_DISABLE_DECISION_MATRIX.md
# Magna Enso — Remove vs Disable Decision Matrix
# Type: Local-only approval package
# Date: 2026-06-17
# Inputs: Sprint 3 HERMES_SURFACE_GOVERNANCE_MATRIX + DISABLEMENT_TIERS_MODEL (Hermes @ 33b1d144)
# Status: PROPOSAL for human approval. No surface removed/disabled now.

---

## 1. Purpose

For each dangerous Hermes surface, propose whether Sprint 4 should **REMOVE**, **DISABLE**, or **DEFER**, with
the Sprint 3 disablement tier. "Remove" = not imported / deleted (T1/T2). "Disable" = imported but
import/registration off (T2/T3). "Defer" = decide later (kept out of MVP either way).

## 2. Matrix

| Surface | Decision | Tier | Hermes evidence (@ 33b1d144) | Rationale |
|---|---|---|---|---|
| Background self-improvement review | **REMOVE** | T1/T2 | `agent/background_review.py` | Autonomous off-turn mutation; never wanted in MVP |
| Curator / self-review | **DISABLE** (report-only later) | T3 | `agent/curator.py` | Useful as analysis; execution off |
| Direct script cron (`no_agent`) | **REMOVE** | T1/T2 | `cron/scheduler.py::run_job` no_agent | Runs scripts w/o LLM or per-action gate |
| Executable scheduler | **DISABLE** (report-only) | T3 | `cron/scheduler.py::tick/run_job` | Schedules → report objects only |
| Messaging gateways | **REMOVE** | T1 | `gateway/platforms/*`, `plugins/platforms/*` | Inbound/outbound network surface; no MVP value |
| Outbound delivery | **REMOVE** | T1 | `tools/send_message_tool.py`, `cron/scheduler.py::_deliver_result` | No outbound in MVP; close cron/gateway delivery too |
| Cloud providers | **DISABLE** | T2 | `providers/*`, `plugins/model-providers/*` | Disabled at import/resolution; data-egress risk (R-04) |
| External memory sync | **REMOVE** | T1/T2 | `agent/memory_manager.py::on_memory_write`, `sync_all` | Drafts must never leave the machine |
| Plugin/MCP dynamic loading | **REMOVE** (loader) | T2/T3 | `tools/mcp_tool.py`, `hermes_cli/plugins/*` | Runtime surface change; no signed allowlist in MVP |
| Remote execution backends | **REMOVE** | T1/T2 | `tools/environments/modal.py`, `daytona.py`, `ssh.py` | Networked execution; highest risk |
| Subagent delegation | **DISABLE** | T3 | `tools/delegate_tool.py`, `_dispatch_delegate_task` | Autonomy multiplier; unregister in MVP |
| Browser actions | **DISABLE** | T3/T4 | `tools/browser_tool.py`, `browser_cdp_tool.py` | Active external effects; snapshot kept read-only |
| Terminal / code execution | **DISABLE** (retain, off) | T4 + gate | `tools/terminal_tool.py`, `tools/code_execution_tool.py` | Retained but **off until policy engine** (Sprint 5) |
| API listeners | **REMOVE / not started** | T1 | `gateway/platforms/api_server.py::connect` | No inbound listener by default |
| File transfer | **DISABLE** | T3/T4 | `tools/send_message_tool.py` media, gateway/browser media | Approval-required later; off in baseline |

## 3. Summary

- **REMOVE (T1/T2):** background self-improvement, direct script cron, messaging gateways, outbound delivery,
  external memory sync, plugin/MCP dynamic loader, remote execution backends, API listeners.
- **DISABLE (T2/T3/T4):** curator (report-only), executable scheduler (report-only), cloud providers, subagent
  delegation, browser actions, terminal/code (retained-but-off), file transfer.
- **DEFER:** none required for MVP — every surface above is decided.

## 4. Guiding rule

**Remove what MVP will never want; disable what MVP might want later but not now.** For retained-but-off
capabilities (terminal/code), the disable is structural in Sprint 4; the *gate* that would ever turn them on
is Sprint 5. Removed surfaces are simply never imported under Option C (selective vendor import).

## 5. Boundaries

Proposal only. Nothing is removed or disabled by this package; Sprint 4 executes this matrix only after
approval, and Antigravity validates the result.
