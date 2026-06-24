# CAPABILITY_TAXONOMY_VALIDATION.md
# Magna Enso — Sprint 3 Capability Governance Design
# Capability Taxonomy Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Validate the 20-category capability taxonomy (CAPABILITY_TAXONOMY.md) for completeness,
correctness of default states, coverage of all Hermes Sprint 2 surfaces, and the two
special focus items: local_read ambiguity and web_network_access classification.

---

## 2. Category Inventory Assessment

All 20 capability categories:

| # | Category | Default state | Sprint 2 Hermes evidence | Antigravity Assessment |
|---|---|---|---|---|
| C-01 | local_read | active_safe / read_only | session search, file read, status | SEE NOTE VN-01 — dual state |
| C-02 | local_write | draft_only / approval_required | file write/patch | ACCEPTABLE — dual default reflects two sub-cases |
| C-03 | persistent_memory | draft_only | memory_tool.py, MemoryStore.save_to_disk | CORRECT |
| C-04 | skill_mutation | draft_only | skill_manager_tool.py::skill_manage | CORRECT |
| C-05 | file_mutation | draft_only / approval_required | ACP edit approval, write paths | ACCEPTABLE — file mutation is a subset of write patterns |
| C-06 | terminal_execution | approval_required (off by default) | terminal_tool.py, process_registry.py | CORRECT |
| C-07 | code_execution | approval_required (off by default) | code_execution_tool.py::execute_code | CORRECT |
| C-08 | browser_observation | read_only | browser_tool.py::browser_snapshot | CORRECT |
| C-09 | browser_action | approval_required / disabled | browser_tool.py, browser_cdp_tool.py | CORRECT |
| C-10 | web_network_access | read_only w/ privacy gate / disabled | web_search_tool.py, web_extract_tool.py | SEE NOTE VN-02 — dual default |
| C-11 | cloud_provider_access | disabled | providers/*, plugins/model-providers/* | CORRECT |
| C-12 | messaging_outbound | disabled | send_message_tool.py, cron::_deliver_result | CORRECT |
| C-13 | scheduler_background | report_only | cronjob_tools.py, scheduler.py::tick/run_job | CORRECT |
| C-14 | delegation_subagent | disabled (MVP) | delegate_tool.py, _dispatch_delegate_task | CORRECT |
| C-15 | plugin_mcp_expansion | disabled unless signed allowlist | mcp_tool.py, hermes_cli/plugins/* | CORRECT |
| C-16 | external_memory_sync | disabled | memory_manager.py::on_memory_write, sync_all | CORRECT |
| C-17 | remote_execution_backend | disabled (prefer remove) | environments/modal.py, daytona.py, ssh.py | CORRECT |
| C-18 | background_self_improvement | disabled (remove) | background_review.py::spawn_background_review_thread | CORRECT |
| C-19 | curator_self_review | report_only | agent/curator.py | CORRECT |
| C-20 | inbound_trigger | disabled | gateway/run.py, api_server.py | CORRECT |

---

## 3. Sprint 2 Surface Coverage Check

Every high-risk Hermes surface from Sprint 2 must map to a category:

| Sprint 2 Surface (from EXTERNAL_SURFACE_MAP, AUTONOMY_ENTRY_POINT_MAP) | Category | Mapped? |
|---|---|---|
| API server listener (api_server.py) | C-20 (inbound_trigger) | YES |
| Messaging gateways (platforms/*) | C-12 (messaging_outbound) | YES |
| Webhooks | C-20 (inbound_trigger) or C-12 | YES |
| Outbound messaging (send_message_tool, cron/deliver) | C-12 | YES |
| Browser snapshot | C-08 (browser_observation) | YES |
| Browser actions (navigate/click/type/press/scroll) | C-09 (browser_action) | YES |
| Web search/extract | C-10 (web_network_access) | YES |
| Terminal execution | C-06 (terminal_execution) | YES |
| Code execution | C-07 (code_execution) | YES |
| Remote execution backends (Modal/Daytona/SSH) | C-17 (remote_execution_backend) | YES |
| Cloud model providers | C-11 (cloud_provider_access) | YES |
| Plugin/MCP dynamic loading | C-15 (plugin_mcp_expansion) | YES |
| File/media upload/download | C-05 (file_mutation) / C-02 (local_write) | YES |
| Background review (background_review.py) | C-18 (background_self_improvement) | YES |
| Curator/self-review | C-19 (curator_self_review) | YES |
| Memory writes | C-03 (persistent_memory) | YES |
| Skill writes | C-04 (skill_mutation) | YES |
| External memory sync | C-16 (external_memory_sync) | YES |
| Subagent delegation | C-14 (delegation_subagent) | YES |
| Scheduled jobs / cron execution | C-13 (scheduler_background) | YES |
| Direct-script cron (no_agent path) | C-13 + remove action | YES |
| Process/background processes | C-06 (terminal_execution, via process_registry.py) | YES |

Coverage: 22/22 surfaces mapped. COMPLETE.

---

## 4. VN-01: local_read (C-01) Dual Default State

ISSUE: C-01 lists default state as "active_safe / read_only" — two different states.
This is the only category with a dual default. The taxonomy comment says:
"session search, file read, status" — which of these is active_safe vs read_only is unclear.

Analysis:
- "active_safe" means: always allowed, no external/persistent effect, no approval needed
- "read_only" means: allowed for reads, denied for mutate/side-effects, gated

The distinction matters because:
- Status queries (no FS access, just in-memory state) → active_safe is appropriate
- File reads (FS access, could read sensitive data, could log content) → read_only is more appropriate
- Session search (query local session state) → read_only is appropriate

If left ambiguous, Sprint 4 implementation might default all local reads to active_safe
(overly permissive) or all to read_only (unnecessarily restrictive). More importantly,
a file read tool that reads sensitive content should not be active_safe.

RECOMMENDATION (VN-01): Split C-01 into:
- C-01a: local_safe_status_read — in-memory/runtime status, no FS, no sensitive data → active_safe
- C-01b: local_sensitive_read — file reads, session search, metadata → read_only

This aligns with the distinction made in the policy schema (active_safe vs read_only states)
and prevents the ambiguity from propagating into Sprint 4 implementation.

BLOCKING: NO — the design is safe-by-default (neither read_only nor active_safe allows
mutation or external access). However the ambiguity should be resolved before Sprint 4
uses the taxonomy as a build specification.

---

## 5. VN-02: web_network_access (C-10) Default State

ISSUE: C-10 default is listed as "read_only w/ privacy gate / disabled" — dual default.

Analysis:
- BROWSER_WEB_READ_ONLY_MODEL.md §4 Rule 3: "Web access is read_only only with a
  privacy gate; default disabled until that gate exists."
- This is the correct resolution: for MVP (Sprint 4), no privacy gate exists yet →
  web_network_access is disabled.
- The taxonomy's "read_only w/ privacy gate" is the eventual target state, not the MVP default.

The BROWSER_WEB_READ_ONLY_MODEL correctly treats C-10 as disabled in MVP. The taxonomy
header is slightly ambiguous because it shows both states in the same field without
indicating that "disabled" is the MVP default and "read_only w/ privacy gate" is future.

RECOMMENDATION (VN-02): Update C-10 in CAPABILITY_TAXONOMY.md to:
  "Default state: disabled (MVP) | read_only w/ privacy gate (future)"
  or add a footnote: "MVP default: disabled. Privacy gate required for read_only access."

BLOCKING: NO — the surface model report is unambiguous. The taxonomy ambiguity is a
documentation note, not a safety risk (the MVP default is disabled in either reading).

---

## 6. Risk Linkage Assessment

§4 (Category → risk linkage) correctly maps:
- C-06/C-07 terminal/code → R-06 (policy bypass) — CORRECT
- C-09 browser_action / C-10 web → R-05 (exposure) — CORRECT
- C-11 cloud / C-16 external_memory → R-04 (data egress) — CORRECT
- C-03 persistent_memory / C-04 skill_mutation → R-07, R-08, R-09 (prompt injection persistence) — CORRECT
- C-13/C-18 scheduler/background → R-10 (off-turn autonomous action) — CORRECT
- C-14 delegation → R-06 (policy bypass, recursion) — CORRECT
- C-15 plugin/MCP → R-02, R-06 (supply chain, bypass) — CORRECT

All risk linkages are correctly identified. PASS.

---

## 7. Taxonomy Verdict

```
20 categories defined:       PASS
All Sprint 2 surfaces mapped: 22/22 — PASS
local_read dual state:        MEDIUM NOTE (VN-01) — split recommended before Sprint 4
web_network_access:           LOW NOTE (VN-02) — MVP = disabled; model is correct
Risk linkage:                 CORRECT for all categories
No code in taxonomy:          CONFIRMED

CAPABILITY TAXONOMY VALIDATION: PASS with 2 non-blocking recommendations
```
