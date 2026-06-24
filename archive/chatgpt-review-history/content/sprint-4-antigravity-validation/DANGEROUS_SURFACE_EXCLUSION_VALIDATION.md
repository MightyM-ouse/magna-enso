# DANGEROUS_SURFACE_EXCLUSION_VALIDATION.md
# Magna Enso — Sprint 4 Clean Governed Hermes Baseline Preparation
# Dangerous Surface Exclusion Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-18

---

## 1. Purpose

Confirm that all 15 required dangerous Hermes surfaces are excluded by non-import.
Verify each against the vendor/hermes/ file inventory and the RETAINED_SURFACE_STATES.yaml
excluded_surfaces list.

---

## 2. Required Surface Exclusion Assessment

All 15 required dangerous surfaces:

| # | Required Exclusion | Absent from vendor/hermes/? | In excluded_surfaces YAML? | Sprint 2 Hermes file(s) | Antigravity Assessment |
|---|---|---|---|---|---|
| 1 | Background review | YES — no agent/ dir; no background_review.py | YES — "background_review" | agent/background_review.py | EXCLUDED |
| 2 | Curator/self-review | YES — no agent/curator.py | YES — "curator_execution" | agent/curator.py | EXCLUDED |
| 3 | Direct script cron | YES — no cron/ dir; no scheduler.py; no jobs.py | YES — "direct_script_cron" | cron/jobs.py (no_agent path), cron/scheduler.py | EXCLUDED |
| 4 | Executable scheduler | YES — no scheduler runtime source | YES — "executable_scheduler" | cron/scheduler.py::tick, run_job | EXCLUDED |
| 5 | Messaging/outbound delivery | YES — no gateway/ dir; no send_message_tool.py | YES — "messaging_gateways", "outbound_delivery" | gateway/platforms/*, tools/send_message_tool.py | EXCLUDED |
| 6 | Cloud providers | YES — no providers/ dir; no model-provider plugins | YES — "cloud_provider_activation" | providers/*, plugins/model-providers/* | EXCLUDED |
| 7 | External memory sync | YES — no agent/memory_manager.py; no sync source | YES — "external_memory_sync" | agent/memory_manager.py::sync_all | EXCLUDED |
| 8 | Plugin/MCP loading | YES — no tools/mcp_tool.py; no hermes_cli/plugins; no optional-mcps/ | YES — "plugin_mcp_dynamic_loading" | tools/mcp_tool.py, hermes_cli/plugins/* | EXCLUDED |
| 9 | Remote execution backends | YES — no tools/environments/ | YES — "remote_execution_backends" | tools/environments/modal.py, daytona.py, ssh.py | EXCLUDED |
| 10 | Subagent delegation | YES — no tools/delegate_tool.py | YES — "subagent_delegation" | tools/delegate_tool.py | EXCLUDED |
| 11 | Browser actions | YES — no tools/browser_tool.py or browser plugins | YES — "browser_actions" | tools/browser_tool.py, browser_cdp_tool.py | EXCLUDED |
| 12 | Terminal/code execution activation | YES — no tools/terminal_tool.py; no code_execution_tool.py | YES — "terminal_code_execution_activation" | tools/terminal_tool.py, tools/code_execution_tool.py | EXCLUDED |
| 13 | API listeners | YES — no gateway/platforms/api_server.py | YES — "api_listeners" | gateway/platforms/api_server.py, gateway/run.py | EXCLUDED |
| 14 | File transfer activation | YES — no messaging/browser/media transfer source | YES — "file_transfer_activation" | browser/messaging file transfer paths | EXCLUDED |
| 15 | Messaging gateways | YES — no gateway/platforms/ or platform plugins | YES — "messaging_gateways" | gateway/platforms/* (10+ platform adapters) | EXCLUDED |

All 15/15 required dangerous surfaces: EXCLUDED by non-import. PASS.

---

## 3. Exclusion Mechanism Assessment

The exclusion mechanism is "non-import" — the source modules simply do not exist under
vendor/hermes/. This is the correct and strongest exclusion strategy:

- Non-import is stronger than disablement (T4 config-only): no code path exists to invoke
- Non-import is equivalent to T1/T2 (remove/module import disabled) in Sprint 3 governance model
- Non-import cannot be accidentally bypassed by a config change
- Non-import cannot be reversed by a misconfig of an active module

The Sprint 3 design principle "prefer remove" for high-risk surfaces is correctly
implemented here as non-import for ALL 15 dangerous surfaces.

---

## 4. Cross-Check: excluded_surfaces in RETAINED_SURFACE_STATES.yaml

The YAML excluded_surfaces list contains 15 entries:
```yaml
excluded_surfaces:
  - "background_review"
  - "curator_execution"
  - "direct_script_cron"
  - "executable_scheduler"
  - "messaging_gateways"
  - "outbound_delivery"
  - "cloud_provider_activation"
  - "external_memory_sync"
  - "plugin_mcp_dynamic_loading"
  - "remote_execution_backends"
  - "subagent_delegation"
  - "browser_actions"
  - "terminal_code_execution_activation"
  - "api_listeners"
  - "file_transfer_activation"
```

Count: 15/15 required surfaces listed. All entries verified against required exclusion list.
No required surface is missing from the YAML. PASS.

---

## 5. Terminal/Code Special Case Assessment

Terminal/code execution is in the excluded_surfaces list as "terminal_code_execution_activation" —
the word "activation" is the key. This is consistent with the Sprint 3 governance model where
terminal/code is a retained surface at state `approval_required_disabled` (the design target is
retained, but the execution path is excluded). The RETAINED_SURFACE_STATES.yaml correctly shows:
- terminal_code_model: state = "approval_required_disabled"; imported_runtime_source = false

So terminal/code appears both in excluded_surfaces (execution activation excluded) and in
retained_surfaces (design model retained as metadata). This is consistent and correct.

---

## 6. Outbound Delivery — All 3 Paths Confirmed Excluded

Sprint 3 VN-11 required all 3 outbound delivery paths to be closed:
1. Tool path (send_message_tool.py) — NO tools/ directory under vendor/hermes/ → EXCLUDED
2. Cron delivery path (cron/scheduler.py::_deliver_result) — NO cron/ directory → EXCLUDED
3. Gateway path (gateway listener) — NO gateway/ directory → EXCLUDED

All 3 paths excluded. PASS.

---

## 7. Dangerous Surface Exclusion Verdict

```
All 15 required surfaces excluded:      PASS (15/15)
Exclusion mechanism:                    Non-import (strongest — equivalent to T1/T2 remove)
excluded_surfaces YAML list:            15/15 entries present — PASS
No dangerous directory imported:        14 dangerous directories all absent — PASS
Terminal/code special case:             Correctly excluded (activation) + retained (model) — PASS
Outbound delivery all 3 paths:          All excluded — PASS

DANGEROUS SURFACE EXCLUSION VALIDATION: PASS
All required dangerous surfaces excluded by non-import.
```
