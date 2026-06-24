# DISABLEMENT_TIERS_MODEL.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 4 of 17 — Disablement Tiers Model
# Type: Design-only governance report. No code.
# Date: 2026-06-17
# Status: Design only. Human owner is final authority (EH-0010).

---

## 1. Purpose

Define what "disabled" means precisely, and assign the **strongest feasible tier** to each Hermes surface.
"Disabled" without a tier is ambiguous and leaves back doors.

## 2. The five tiers (strongest → weakest)

| Tier | Name | Mechanism | Bypass resistance |
|---|---|---|---|
| **T1** | Process-level disabled | Feature/process never starts (listener never boots, backend never launches) | Strongest — nothing runs to reach |
| **T2** | Module import disabled | Module never imported; its code is never in memory | Very strong — no code to invoke |
| **T3** | Tool registration disabled | Module may load but tool never registered into the dispatch registry | Strong — not selectable/callable |
| **T4** | Dispatch-level blocked | Tool registered; dispatch checks policy and refuses | Moderate — guards one path only |
| **T5** | Config-level disabled | A flag says "off"; relies on every path honoring it | Weakest — easy to miss a path |

## 3. Why process/module/registration beats dispatch-only

The Sprint 2 `ACTION_DISPATCH_MAP` proved Hermes reaches capabilities through **many** paths
(`tools/registry.py::dispatch`, agent-owned `_AGENT_LOOP_TOOLS`, `cron/scheduler.py::run_job`, gateway/API,
`acp_adapter/tools.py`, plugin/MCP registration, `agent/background_review.py`). Dispatch-level blocking (T4)
guards **one** of those paths; the rest stay open. Config (T5) is weaker still — one path that forgets the
flag is a hole. **T1–T3 remove the capability from existence**, so there is nothing to bypass by *any* path.

> Rule: the most dangerous surfaces (remote backends, direct-script cron, background self-improvement,
> messaging, listeners, cloud, dynamic plugin/MCP) must be **removed or disabled at T1–T3**, never merely T4/T5.

## 4. Tier assignment per Hermes surface (@ 33b1d144)

| Surface | Tier | Mechanism (evidence) |
|---|---|---|
| API server listener | **T1** | `gateway/platforms/api_server.py::connect` never started |
| Messaging gateways | **T1** | `gateway/platforms/*`, `plugins/platforms/*` not launched |
| Remote execution backends | **T1/T2** (prefer remove) | `tools/environments/modal.py`, `daytona.py`, `ssh.py` not imported |
| Background self-improvement | **T1/T2** (remove) | `agent/background_review.py::spawn_background_review_thread` not started/imported |
| Direct script cron (`no_agent`) | **T1/T2** (remove) | `cron/scheduler.py::run_job` no_agent path removed |
| Cloud providers | **T2** | `providers/*`, `plugins/model-providers/*` not imported until enabled |
| External memory sync | **T1/T2** | `agent/memory_manager.py::on_memory_write`/`sync_all` disabled |
| Plugin/MCP dynamic loading | **T2/T3** | `tools/mcp_tool.py`, `hermes_cli/plugins/*` loader off unless signed allowlist |
| Subagent delegation | **T3** | `tools/delegate_tool.py` not registered in MVP |
| Cron scheduler (execution) | **T3 + report-only** | `cron/scheduler.py::tick/run_job` execution disabled; schedules become report objects |
| Curator/self-review | **T3 + report-only** | `agent/curator.py` execution paths replaced by report generation |
| Browser actions | **T3/T4** | `tools/browser_tool.py` action handlers unregistered or gated |
| Terminal/code execution | **T4 + gate** (retained, off by default) | `tools/terminal_tool.py`, `tools/code_execution_tool.py` registered but `approval_required` |

## 5. Defense in depth

Disablement tiers and default-deny are complementary: remove/disable at the strongest feasible tier **and**
still deny at the policy gate. No single layer is trusted alone. Retained-but-gated capabilities (terminal,
code, memory drafts) rely on the gate; everything dangerous-and-unneeded is removed so the gate never matters.

## 6. Boundaries

Design only. No code disabled/removed in Sprint 3 — this report tells Sprint 4 **which tier** to apply to
each surface when the fork is built. Removal vs. disable choices feed `HERMES_SURFACE_GOVERNANCE_MATRIX.md`.
