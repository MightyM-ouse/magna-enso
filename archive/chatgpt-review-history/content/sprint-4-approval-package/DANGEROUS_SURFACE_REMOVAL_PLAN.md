# DANGEROUS_SURFACE_REMOVAL_PLAN.md
# Magna Enso — Dangerous Surface Removal Plan
# Type: Local-only approval package
# Date: 2026-06-17
# Status: PRELIMINARY recommendation. No surface removed now.

---

## 1. Purpose

Name the surfaces that should be **removed** (not merely disabled) in the MVP baseline, and how Option C
(selective vendor import) makes removal the default — you simply never import them.

## 2. Surfaces to REMOVE in MVP

| Surface | Hermes evidence (@ 33b1d144) | Why remove (not disable) |
|---|---|---|
| Direct script cron (`no_agent`) | `cron/scheduler.py::run_job` no_agent path | Executes scripts with no LLM and no per-action gate; no safe disabled form |
| Remote execution backends | `tools/environments/modal.py`, `daytona.py`, `ssh.py`, `managed_modal.py` | Networked code execution; highest blast radius; never wanted in local-first MVP |
| Messaging gateways + outbound delivery | `gateway/platforms/*`, `plugins/platforms/*`, `tools/send_message_tool.py`, `cron/scheduler.py::_deliver_result` | Inbound/outbound network surface; multiple delivery paths to close |
| Plugin/MCP dynamic loading | `tools/mcp_tool.py`, `hermes_cli/plugins/*`, `tui_gateway/entry.py` discovery | Can change capability surface at runtime; defeats the whole governance design |
| External memory sync | `agent/memory_manager.py::on_memory_write`, `sync_all` | Sends memory off-machine; drafts must never leave |
| Background self-improvement | `agent/background_review.py::spawn_background_review_thread`, `_background_review_worker` | Autonomous off-turn mutation; the opposite of human-approval-driven |

## 3. Why removal beats disablement for these

These surfaces are (a) high blast radius, (b) reachable by **multiple** paths (Sprint 2), and (c) **not
wanted** in MVP at all. Disabling leaves the code present to be re-enabled or reached by a forgotten path;
removal eliminates the risk. Under **Option C (selective vendor import)**, removal is the natural default:
they are simply **never imported** — the strongest possible "removal" (the code never enters the repo).

## 4. Removal method (Sprint 4, if approved)

- **Primary (Option C):** do not include these modules in the retained import allowlist — they never enter.
- **If any retained module references a removed surface:** sever the import / stub the call; record in the
  diff report. A retained module must not transitively pull a removed surface back in.
- **Verify absence:** `REMOVED_SURFACES_REPORT.md` lists each removed surface and confirms it is absent from
  the baseline (grep/inventory check); Antigravity validates.

## 5. Boundaries

Plan only. No surface is removed by this package. Removal happens in Sprint 4 (by non-import under Option C),
validated by Antigravity, and recorded in the Sprint 4 reports.
