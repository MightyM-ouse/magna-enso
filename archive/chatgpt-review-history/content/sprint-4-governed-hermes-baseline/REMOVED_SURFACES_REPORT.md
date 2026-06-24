# Removed Surfaces Report

## Purpose

Confirm dangerous Hermes surfaces were removed by non-import under Option C.

## Honesty Statement

This baseline is structurally safe / not runtime-enforced. Retained risky capabilities remain disabled until Sprint 5. No Hermes runtime, build, package script, or dependency install was performed.

## Findings

The following dangerous surfaces are absent from `vendor/hermes/`:

| Surface | Status | Evidence |
|---|---|---|
| Background review/self-improvement | Removed by non-import | No `agent/` directory, no `background_review.py`. |
| Curator execution | Removed by non-import | No `agent/curator.py`. |
| Direct script cron | Removed by non-import | No `cron/` directory, no `scheduler.py`, no active `jobs.py`. |
| Executable scheduler | Removed by non-import | No scheduler runtime source. |
| Messaging gateways | Removed by non-import | No `gateway/` or `plugins/platforms/`. |
| Outbound delivery | Removed by non-import | No `tools/send_message_tool.py`. |
| Cloud provider activation | Removed by non-import | No `providers/` or `plugins/model-providers/`. |
| External memory sync | Removed by non-import | No `agent/memory_manager.py` or external memory plugins. |
| Plugin/MCP dynamic loading | Removed by non-import | No `tools/mcp_tool.py`, `hermes_cli/plugins`, or `optional-mcps/`. |
| Remote execution backends | Removed by non-import | No `tools/environments/`. |
| Subagent delegation | Removed by non-import | No `tools/delegate_tool.py`. |
| Browser actions | Removed by non-import | No `tools/browser_tool.py` or browser plugins. |
| Terminal/code execution activation | Removed by non-import | No `tools/terminal_tool.py`, `tools/code_execution_tool.py`, or executable code. |
| API listeners | Removed by non-import | No `gateway/platforms/api_server.py`; no listener source. |
| File transfer activation | Removed by non-import | No messaging/browser/media transfer source. |

## Static Checks

- `find vendor/hermes -type f` returns six files only.
- `find vendor/hermes -type f` found no `.py`, active package manifests, setup files, `__init__.py`, or plugin manifests.
- `find vendor/hermes -type d` found no Hermes runtime directories such as `agent`, `tools`, `cron`, `gateway`, `plugins`, `providers`, `web`, `ui-tui`, or `apps`.

## Confidence Level

High.

## Risks

- Text manifest references mention removed surfaces as historical upstream dependency metadata; they are not active code.
- Future executable source imports could reintroduce surfaces if not revalidated.

## Recommendation

Keep removed surfaces absent. Do not import executable Hermes runtime modules until a separate approval and policy-engine readiness review.
