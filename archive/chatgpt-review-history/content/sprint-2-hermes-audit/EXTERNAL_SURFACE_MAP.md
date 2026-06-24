# External Surface Map

## Purpose

Map Hermes network, cloud, browser, terminal, messaging, upload/download, and listener surfaces for governance classification.

## Files Inspected

- `gateway/run.py`
- `gateway/platforms/api_server.py`
- `gateway/platforms/webhook.py`
- `gateway/platforms/*`
- `plugins/platforms/*`
- `tools/send_message_tool.py`
- `tools/browser_tool.py`
- `tools/browser_cdp_tool.py`
- `agent/browser_registry.py`
- `plugins/browser/*`
- `tools/terminal_tool.py`
- `tools/code_execution_tool.py`
- `tools/environments/*`
- `tools/web_search_tool.py`
- `tools/web_extract_tool.py`
- `providers/*`
- `plugins/model-providers/*`
- `pyproject.toml`

## Findings

| Surface | Evidence | Classification | Notes |
|---|---|---:|---|
| API server listener | `gateway/platforms/api_server.py::connect` | Disabled by default | Exposes run/session/job/approval APIs; requires `API_SERVER_KEY`, but still a major remote surface. |
| Messaging gateways | `gateway/platforms/*`, `plugins/platforms/*` | Disabled by default | Telegram, Discord, Slack, WhatsApp, Signal, email, Matrix, SMS, Teams, LINE, Mattermost, and others. |
| Webhooks | `gateway/platforms/webhook.py`, platform webhook adapters | Disabled by default | Public listener behavior requires strong deployment controls. |
| Outbound messaging | `tools/send_message_tool.py`, `cron/scheduler.py::_deliver_result` | Disabled by default | Agent-callable note says `send_message` is intentionally not registered, but cron/gateway can still deliver. |
| Browser automation | `tools/browser_tool.py`, `tools/browser_cdp_tool.py`, `plugins/browser/*` | Read-only for snapshot; approval-required for action | Navigation/click/type/press/scroll are active external actions. |
| Web search/extract | `tools/web_search_tool.py`, `tools/web_extract_tool.py`, provider plugins | Read-only with privacy gate | Queries may reveal user data to providers. |
| Terminal execution | `tools/terminal_tool.py`, `tools/environments/*` | Approval-required | Supports local, Docker, Singularity, Modal, Daytona, and SSH backends. |
| Python code execution | `tools/code_execution_tool.py` | Approval-required | Runs user/model-provided Python with RPC back to selected tools. |
| Remote execution backends | `tools/environments/modal.py`, `managed_modal.py`, `daytona.py`, `ssh.py` | Disabled by default | Networked execution environments need separate approval. |
| Cloud model providers | `providers/*`, `plugins/model-providers/*`, `agent/*_adapter.py` | Disabled by default | Broad provider set includes OpenAI-compatible, Anthropic, Bedrock, Gemini, OpenRouter, xAI, and others. |
| MCP tools | `tools/mcp_tool.py`, `tui_gateway/entry.py` | Disabled by default | Dynamically expands available external and local actions. |
| File/media upload/download | `tools/send_message_tool.py`, gateway media helpers, browser media helpers | Approval-required | File movement across platform boundaries. |

## Evidence Paths

- `gateway/platforms/api_server.py::connect`
- `gateway/platforms/api_server.py::_handle_runs`
- `gateway/platforms/api_server.py::_handle_run_approval`
- `tools/send_message_tool.py`
- `tools/browser_tool.py` registry entries for `browser_navigate`, `browser_click`, `browser_type`, `browser_press`, `browser_snapshot`
- `tools/terminal_tool.py::terminal_tool`
- `tools/code_execution_tool.py::execute_code`
- `tools/environments/docker.py`
- `tools/environments/modal.py`
- `tools/environments/daytona.py`
- `tools/environments/ssh.py`
- `plugins/model-providers/*`
- `plugins/platforms/*`

## Confidence Level

Medium-high. Major external surfaces were mapped; individual platform adapters were not exhaustively threat-modeled.

## Risks

- Hermes supports many inbound and outbound network paths.
- Some surfaces are safe only with configuration, credentials, and runtime environment assumptions.
- Browser and terminal tools can convert read-only tasks into active side effects.
- Cloud provider calls can leak sensitive prompt data unless Magna privacy policy gates them.

## Open Questions

- Should Magna keep any messaging gateway code in the Sprint 4 fork baseline?
- Should browser tools be retained as source but policy-disabled, or removed until a later sprint?
- Should remote execution backends be removed entirely from the first governed fork?

## Recommendation

For Magna Enso, default all external surfaces to disabled. Allow only explicitly approved read-only web/browser inspection in audit contexts, and require human approval for terminal, browser actions, file transfer, cloud calls, and messaging.
