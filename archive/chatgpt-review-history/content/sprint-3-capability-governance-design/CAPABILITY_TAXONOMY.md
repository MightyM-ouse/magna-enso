# CAPABILITY_TAXONOMY.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 1 of 17 — Capability Taxonomy
# Type: Design-only governance report
# Date: 2026-06-17
# Inputs: Sprint 2 audit (Hermes @ 33b1d144) — ACTION_DISPATCH_MAP, AUTONOMY_ENTRY_POINT_MAP, EXTERNAL_SURFACE_MAP, CAPABILITY_GATING_FEASIBILITY
# Status: Design only. No code. No fork. Human owner is final authority (EH-0010).

---

## 1. Purpose

Define the capability **categories** Magna Enso governs. Every Hermes-derived action maps to exactly one
category; each category carries a default posture. Categories are the vocabulary the policy schema, the
default-deny model, and the surface matrix all build on.

## 2. Capability categories

| # | Category | Definition | Default state | Primary Hermes evidence (@ 33b1d144) |
|---|---|---|---|---|
| C-01a | **local_safe_status_read** | Read non-sensitive local status/metadata | `active_safe` | health/status metadata, capability status, project status labels, non-sensitive UI state |
| C-01b | **local_sensitive_read** | Read local content that may expose private data | `read_only` | file reads, session search, memory inspection, local content inspection |
| C-02 | **local_write** | Mutate local non-memory files/state | `draft_only` / `approval_required` | file write/patch tools |
| C-03 | **persistent_memory** | Write/persist agent memory | `draft_only` | `tools/memory_tool.py`, `MemoryStore.save_to_disk` |
| C-04 | **skill_mutation** | Create/edit agent skills | `draft_only` | `tools/skill_manager_tool.py::skill_manage` |
| C-05 | **file_mutation** | Create/modify/delete files | `draft_only` / `approval_required` | ACP edit approval, write paths |
| C-06 | **terminal_execution** | Run shell/processes | `approval_required` (off by default) | `tools/terminal_tool.py`, `tools/process_registry.py` |
| C-07 | **code_execution** | Execute arbitrary code | `approval_required` (off by default) | `tools/code_execution_tool.py::execute_code` |
| C-08 | **browser_observation** | Read/snapshot browser state | `read_only` | `tools/browser_tool.py::browser_snapshot` |
| C-09 | **browser_action** | Navigate/click/type/press/scroll | `approval_required` / `disabled` | `tools/browser_tool.py`, `tools/browser_cdp_tool.py` |
| C-10 | **web_network_access** [†] | Outbound web search/extract/fetch | `disabled` (MVP) → `read_only` w/ privacy gate | `tools/web_search_tool.py`, `tools/web_extract_tool.py` |
| C-11 | **cloud_provider_access** | Calls to cloud model/data providers | `disabled` | `providers/*`, `plugins/model-providers/*` |
| C-12 | **messaging_outbound** | Send messages / deliver results outward | `disabled` | `tools/send_message_tool.py`, `cron/scheduler.py::_deliver_result` |
| C-13 | **scheduler_background** | Timed/triggered background execution | `report_only` | `tools/cronjob_tools.py`, `cron/scheduler.py::tick/run_job` |
| C-14 | **delegation_subagent** | Spawn subagents / delegate tasks | `disabled` (MVP) | `tools/delegate_tool.py`, `run_agent.py::_dispatch_delegate_task` |
| C-15 | **plugin_mcp_expansion** | Dynamically load plugins/MCP tools | `disabled` unless signed allowlist | `tools/mcp_tool.py`, `hermes_cli/plugins/*` |
| C-16 | **external_memory_sync** | Mirror/sync memory to external providers | `disabled` | `agent/memory_manager.py::on_memory_write`, `sync_all` |
| C-17 | **remote_execution_backend** | Execute on networked backends | `disabled` (prefer remove) | `tools/environments/modal.py`, `daytona.py`, `ssh.py` |

### 2.1 C-01 split — safe-status vs. sensitive local reads (RC-01)

`local_read` is split because "reading locally" spans two very different risk levels:

- **C-01a `local_safe_status_read`** — default `active_safe`.
  - Examples: health/status metadata, non-sensitive UI state, capability status, project status labels.
  - Boundary: **no file contents, no session contents, no user data, no external access.** If any of those
    are touched, it is not C-01a — it is C-01b (or higher).
- **C-01b `local_sensitive_read`** — default `read_only`.
  - Examples: file reads, session search, memory inspection, local content inspection.
  - Boundary: may expose user/project/private data; must remain **read-only and audit-visible**; never
    mutates or triggers external side effects.

### 2.2 C-10 web/network note (RC-02) [†]

[†] **`web_network_access` is externally sensitive.** It may be *locally* non-mutating, but it can
**externalize query/context data** (sending user/project content to a search/extract provider). Therefore:
- **MVP default is `disabled`** until a privacy gate exists.
- **After** a privacy gate is in place, *limited* use may become `read_only` (no sensitive data egress).
- It is never `active_safe` — outbound reach is always treated as an external side effect.

## 3. Cross-cutting autonomy categories (from AUTONOMY_ENTRY_POINT_MAP)

Some behaviors are not single tools but **autonomous loops**; they are governed as capabilities too:

| # | Category | Definition | Default state | Evidence |
|---|---|---|---|---|
| C-18 | **background_self_improvement** | Self-spawned review/improvement threads | `disabled` (remove) | `agent/background_review.py::spawn_background_review_thread` |
| C-19 | **curator_self_review** | Self-review/curation loop | `report_only` | `agent/curator.py` |
| C-20 | **inbound_trigger** | Gateway/API-initiated runs | `disabled` | `gateway/run.py`, `gateway/platforms/api_server.py` |

## 4. Category → risk linkage

| Category | Externality | Persistence | Irreversibility | Linked risk |
|---|---|---|---|---|
| C-01a local_safe_status_read | none | none | none | low |
| C-01b local_sensitive_read | none | none | none (read-only) | low–medium (data exposure) |
| C-03 persistent_memory / C-04 skill_mutation | none (if local) | yes | reversible (draft) | R-07, R-08, R-09 |
| C-06/C-07 terminal/code | high | possible | often irreversible | R-06 |
| C-09 browser_action / C-10 web [†] | high | none | possible | R-04, R-05 |
| C-11 cloud / C-16 external_memory | high | external | data leak | R-04 |
| C-12 messaging / C-20 inbound | high | external | irreversible send | R-05 |
| C-13 scheduler / C-18 background | high | possible | acts off-turn | R-10 |
| C-14 delegation | high | possible | recursion | R-06 |
| C-15 plugin/MCP | high (dynamic) | possible | surface change | R-02, R-06 |
| C-17 remote_backend | high | external | irreversible | R-05, R-06 |

## 5. Design rules

- Every governed action **must** map to exactly one capability category before it can be classified.
- An **unmapped** action is treated as `disabled` (default-deny; see DEFAULT_DENY_MODEL).
- Category default states are the **starting** posture; per-capability policy may only make them *more*
  restrictive without human approval (never less).

## 6. Output usage

This taxonomy is consumed by `CAPABILITY_POLICY_SCHEMA.md` (per-capability records), the
`HERMES_SURFACE_GOVERNANCE_MATRIX.md` (surface postures), and `POLICY_CHOKEPOINT_MAP.md` (where each
category is gated).

## 7. Boundaries (RC-03)

This taxonomy is a **design artifact only**. Specifically:

- It is **design-only** — a vocabulary and classification, not running configuration.
- It is **not an implementation allowlist** — listing a category here does not enable it.
- It **does not grant capability activation** — default states are *starting postures*, not switches that
  are "on".
- **Unknown capability = `disabled`** — anything not mapped to a category (or reached by an unmapped path)
  is denied (default-deny; see `DEFAULT_DENY_MODEL.md`).
- **External content cannot raise capability state** — inbound messages, web content, memory contents,
  instruction packages, or model output can never promote a category to a less restrictive state (R-07).
- **Sprint 4 cannot use this taxonomy as a build spec until it is human-accepted.** Acceptance of the
  Sprint 3 design (and Antigravity validation) is required first; this document authorizes nothing on its own.
