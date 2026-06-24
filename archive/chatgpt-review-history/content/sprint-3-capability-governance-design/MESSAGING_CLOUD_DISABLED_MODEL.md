# MESSAGING_CLOUD_DISABLED_MODEL.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 11 of 17 — Messaging & Cloud Disabled-by-Default Model
# Type: Design-only governance report. No code.
# Date: 2026-06-17
# Status: Design only. Human owner is final authority (EH-0010).

---

## 1. Purpose

Define governance for messaging/outbound (C-12), cloud/provider access (C-11), external memory sync (C-16),
inbound triggers (C-20), and the API listener — all **disabled by default** at strong tiers. These protect
local-first/LAN-first posture and prevent data egress (R-04, R-05).

## 2. Model: disabled at the strongest feasible tier

| Surface | State | Tier | Hermes evidence (@ 33b1d144) |
|---|---|---|---|
| API server listener | `disabled` | T1 (not started) | `gateway/platforms/api_server.py::connect` |
| Messaging gateways (Telegram/Discord/Slack/WhatsApp/Signal/email/Matrix/SMS/Teams/LINE/Mattermost…) | `disabled` | T1 (not launched) | `gateway/platforms/*`, `plugins/platforms/*` |
| Webhooks | `disabled` | T1 | `gateway/platforms/webhook.py` |
| Outbound messaging / delivery | `disabled` | T1/removed | `tools/send_message_tool.py`, `cron/scheduler.py::_deliver_result` |
| Cloud model/data providers | `disabled` | T2 (not imported) | `providers/*`, `plugins/model-providers/*`, `agent/*_adapter.py` |
| External memory sync | `disabled` | T1/T2 | `agent/memory_manager.py::on_memory_write`, `sync_all` |
| Inbound gateway-triggered runs | `disabled` | T1 | `gateway/run.py`, `gateway/platforms/api_server.py` |

## 3. Rules

1. All of the above default `disabled` at **T1/T2** (process not started / module not imported) — not merely
   a config flag (T5), which the audit warns can be bypassed.
2. **No public-facing surface by default** — no listener boots; nothing is internet-reachable (R-05).
3. **No cloud/provider call by default** — disabled at provider resolution + import; prevents data egress (R-04).
4. **No outbound delivery** — `send_message` not registered *and* cron/gateway delivery paths removed/disabled
   (the audit notes `send_message` is "intentionally not registered, but cron/gateway can still deliver" —
   those paths must also be closed).
5. **No external memory sync** — drafts never leave the machine.
6. Enabling any of these requires explicit human policy + Event Horizon entry, and even then routes through
   the unified approval engine per action.

## 4. Why disabled (and at strong tiers)

Messaging, cloud, listeners, and external sync are the surfaces that turn a local assistant into an
internet-exposed, data-leaking, remotely-triggerable system. For an MVP whose whole point is governed,
local-first safety, they add risk without MVP value — so they are disabled at the strongest tier, and the
worst (remote backends, direct delivery) are removed.

## 5. Boundaries

Design only. Disablement/removal is applied in the Sprint 4 fork (tiers per `DISABLEMENT_TIERS_MODEL.md`);
any future enablement is a separate, gated decision.
