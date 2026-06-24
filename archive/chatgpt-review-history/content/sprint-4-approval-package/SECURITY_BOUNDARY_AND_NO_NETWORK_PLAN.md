# SECURITY_BOUNDARY_AND_NO_NETWORK_PLAN.md
# Magna Enso — Security Boundary and No-Network Plan
# Type: Local-only approval package
# Date: 2026-06-17
# Status: PLAN. No baseline built; no network surface created.

---

## 1. Purpose

Define the security posture the Sprint 4 baseline must hold: **local-first, no network by default, nothing
reachable, nothing reaching out.** This preserves the frozen governance principles (EH-0008) at the source level.

## 2. The no-network requirements

| Requirement | Meaning | How the baseline meets it |
|---|---|---|
| No network by default | The baseline opens no sockets, makes no outbound calls when present | Network surfaces removed/disabled; nothing wired to run |
| No cloud provider calls | No provider SDK calls | Cloud providers disabled at import (T2); not in active path |
| No messaging | No gateway/outbound delivery | Messaging gateways + outbound delivery **removed** (T1) |
| No API listener | No inbound server/port | API listener **removed / not started** (T1) |
| No telemetry | No usage/data sent anywhere | No telemetry code active; nothing phones home |
| No external memory | No memory sync off-machine | External memory sync **removed** (T1/T2) |
| No auto-update | No self-update fetch | No updater wired; not in baseline active path |
| No remote plugin loading | No dynamic remote code | Plugin/MCP dynamic loader **removed** (T2/T3) |

## 3. Validation (Sprint 4 output: `NO_NETWORK_VALIDATION.md`)

The baseline must be shown to have **no active network surface**:
- Inventory check: removed network surfaces are **absent** from the baseline.
- Static check: no retained module opens listeners / makes outbound calls in an active path.
- (Because the baseline does **not run** in Sprint 4, this is a *static/structural* validation, not a runtime
  packet capture — stated honestly in the report.)

## 4. Defense in depth

- **Structural:** dangerous network surfaces are not imported (Option C) or are import-disabled.
- **Hygiene:** `.gitignore` excludes secrets/credentials; no API keys imported.
- **Posture record:** the baseline documents "no network by default" as an invariant for Sprint 5 to preserve.

## 5. The honesty boundary

"No network" in Sprint 4 means **the baseline contains no active network surface and does not run**. It does
**not** mean a running, runtime-firewalled system — that is later. Reports must not overstate this.

## 6. Boundaries

Plan only. No baseline, network surface, listener, or outbound capability is created by this package.
