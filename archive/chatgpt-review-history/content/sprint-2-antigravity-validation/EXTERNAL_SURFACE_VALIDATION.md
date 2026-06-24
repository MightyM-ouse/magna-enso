# EXTERNAL_SURFACE_VALIDATION.md
# Magna Enso — Sprint 2 Hermes Read-Only Audit
# External Surface Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Validate Codex's mapping of Hermes external surfaces (network, cloud, browser, terminal,
messaging, upload/download, and listener surfaces) and the Magna Enso governance
recommendations for each.

---

## 2. External Surface Coverage Matrix

EXTERNAL_SURFACE_MAP.md identifies 12 external surfaces. Validating each:

| Surface | Files Cited | Classification | Antigravity Assessment |
|---|---|---|---|
| API server listener | gateway/platforms/api_server.py::connect, _handle_runs, _handle_run_approval | Disabled by default | CONFIRMED CORRECT — exposes run/session/job/approval APIs; major remote surface |
| Messaging gateways | gateway/platforms/*, plugins/platforms/* | Disabled by default | CONFIRMED CORRECT — Telegram/Discord/Slack/WhatsApp/Signal/email/Matrix/SMS/Teams/LINE/Mattermost + others; extremely broad surface |
| Webhooks | gateway/platforms/webhook.py, platform webhook adapters | Disabled by default | CONFIRMED CORRECT — inbound listener behavior; deployment controls critical |
| Outbound messaging | tools/send_message_tool.py, cron/_deliver_result | Disabled by default | CONFIRMED CORRECT — note about send_message not being registered is important nuance; cron/gateway delivery path remains |
| Browser automation | browser_tool.py, browser_cdp_tool.py, plugins/browser/* | Read-only for snapshot; approval-required for action | CONFIRMED CORRECT — browser_snapshot separability is accurate; navigate/click/type/press/scroll are active external actions |
| Web search/extract | web_search_tool.py, web_extract_tool.py, provider plugins | Read-only with privacy gate | CONFIRMED CORRECT — data exfiltration risk via query content is real |
| Terminal execution | terminal_tool.py, environments/* | Approval-required | CONFIRMED CORRECT — wide backend support (local/Docker/Singularity/Modal/Daytona/SSH) is an underappreciated surface expansion |
| Python code execution | code_execution_tool.py | Approval-required | CONFIRMED CORRECT — model-provided code execution is highest-risk local capability |
| Remote execution backends | environments/modal.py, managed_modal.py, daytona.py, ssh.py | Disabled by default | CONFIRMED CORRECT — cloud/remote execution must be disabled before any local policy applies |
| Cloud model providers | providers/*, plugins/model-providers/*, agent adapters | Disabled by default | CONFIRMED CORRECT — data privacy risk; cloud call may bypass local logging |
| MCP tools | tools/mcp_tool.py, tui_gateway/entry.py | Disabled by default | CONFIRMED CORRECT — dynamic expansion of available external actions is incompatible with default-deny |
| File/media upload/download | send_message_tool.py, gateway media helpers, browser media helpers | Approval-required | CONFIRMED CORRECT — file movement across platform boundaries requires explicit approval |

Coverage: 12/12 required surfaces — COMPLETE.

---

## 3. Surface Classification Validation

### 3.1 "Disabled by default" classification

For Magna Enso, "disabled by default" means the capability must be:
- Not started at process startup
- Not registered in the tool registry
- Not accessible via config without explicit human approval

Surfaces correctly classified as "disabled by default":
- API server listener (correct — inbound remote trigger is off by default)
- Messaging gateways (correct — 10+ platform plugins; all must be off)
- Webhooks (correct — public listener behavior)
- Outbound messaging (correct — agent-initiated external communication)
- Remote execution backends (correct — cloud compute is externally exposing)
- Cloud model providers (correct — all cloud data routing must be opt-in)
- MCP tools (correct — dynamic surface expansion incompatible with default-deny)

Assessment: All 7 "disabled by default" classifications are CORRECT and appropriately
conservative. The Magna posture requirement (public_exposure_default: false,
cloud_execution_default: false) is fully consistent with these classifications.

### 3.2 "Approval-required" classification

Surfaces classified as "approval-required":
- Terminal execution (correct — humans must approve each terminal invocation)
- Python code execution (correct — model-provided code is highest-risk)
- Browser action (correct — active external side effects beyond snapshot)
- File/media upload/download (correct — data leaves the machine)

Assessment: All 4 "approval-required" classifications are CORRECT. These are surfaces
that have legitimate use cases in Magna but carry irreversible side effects.

### 3.3 "Read-only with privacy gate" classification

Web search/extract:
- Classified as "read-only with privacy gate"
- Risk noted: "Queries may reveal user data to providers"
- This classification is CORRECT and appropriately nuanced

### 3.4 "Read-only for snapshot; approval-required for action"

Browser automation split:
- browser_snapshot: read-only for snapshot — CORRECT (passive page capture)
- browser_navigate, browser_click, browser_type, browser_press, browser_scroll: approval-required — CORRECT
- This distinction is architecturally important and correctly documented

---

## 4. Surface Coverage Completeness Check

Checking against the required validation categories:

| Required Category | Covered in EXTERNAL_SURFACE_MAP? | Assessment |
|---|---|---|
| API server listener | YES | PASS |
| Messaging gateways | YES (10+ platforms listed) | PASS |
| Webhooks | YES | PASS |
| Outbound messaging | YES | PASS |
| Browser automation | YES (read/action split) | PASS |
| Web search/extract | YES | PASS |
| Terminal execution | YES | PASS |
| Python code execution | YES | PASS |
| Remote execution backends | YES (Modal/Daytona/SSH/SSH named) | PASS |
| Cloud model providers | YES | PASS |
| MCP tools | YES | PASS |
| File/media transfer | YES | PASS |

All 12 required categories covered.

---

## 5. Notable Findings from External Surface Review

### 5.1 send_message_tool not directly registered but delivery paths remain

ACTION_DISPATCH_MAP.md notes: "agent callable note says send_message is intentionally not
registered, but cron/gateway can still deliver."

This is an important governance gap: even if send_message_tool is not directly callable
by the model, the cron scheduler's _deliver_result path and gateway platform adapters can
still trigger outbound delivery. A governed fork must disable delivery at ALL outbound paths,
not just at the tool registration level.

Antigravity Assessment: This finding directly informs Sprint 3 governance design.
The disablement must be enforced at scheduler, gateway, and delivery layers — not just
at the tool registry.

### 5.2 Remote execution backends significantly expand the terminal surface

Terminal execution covers: local, Docker, Singularity, Modal, Daytona, and SSH.
Each backend changes the threat model:
- Local: process on same machine as Magna
- Docker: container isolation (partial mitigation)
- Singularity: similar to Docker
- Modal/Daytona: cloud compute (data leaves machine — high risk)
- SSH: remote machine access (extremely high risk)

Antigravity Assessment: The Sprint 3 governance design must classify each environment
backend separately. "Approval-required" for terminal is necessary but not sufficient —
cloud and remote backends should be DISABLED by default, not merely approval-required.

### 5.3 Cloud provider calls can leak prompt/context data

EXTERNAL_SURFACE_MAP.md notes: "Cloud provider calls can leak sensitive prompt data unless
Magna privacy policy gates them." This is correct and important. Even with approval-required
classification, the data content sent to cloud providers must be governed by a privacy policy.

This is a Sprint 3 governance design requirement — beyond tool approval into data governance.

---

## 6. External Surface Verdict

```
Surface coverage:     12/12 — COMPLETE
Classifications:      All correct for Magna Enso governance requirements
Notable findings:     3 confirmed (delivery paths, backend diversity, cloud privacy)
Missed surfaces:      None significant at Sprint 2 scope

EXTERNAL SURFACE VALIDATION: PASS
Report is accurate and appropriate for Sprint 3 governance design input.
```
