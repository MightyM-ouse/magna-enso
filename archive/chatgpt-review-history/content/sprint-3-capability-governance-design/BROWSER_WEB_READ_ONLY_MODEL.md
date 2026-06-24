# BROWSER_WEB_READ_ONLY_MODEL.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 9 of 17 — Browser & Web Read-Only Model
# Type: Design-only governance report. No code.
# Date: 2026-06-17
# Status: Design only. Human owner is final authority (EH-0010).

---

## 1. Purpose

Define governance for browser observation (C-08), browser actions (C-09), and web/network access (C-10).
Separate **reading** (low risk) from **acting** (high risk).

## 2. Model

| Capability | State | Rationale |
|---|---|---|
| Browser snapshot / read | `read_only` | Observation only; no navigation/mutation |
| Browser actions (navigate/click/type/press/scroll) | `approval_required` or `disabled` | Active external side effects |
| Web search / extract / fetch | `read_only` with **privacy gate**, or `disabled` | Queries can leak user data to providers |

## 3. Hermes binding (@ 33b1d144)

- `browser_snapshot` is **separable** from action handlers — keep as `read_only`
  (`tools/browser_tool.py` registry entry `browser_snapshot`).
- Action handlers `browser_navigate`, `browser_click`, `browser_type`, `browser_press`, `browser_scroll`
  (`tools/browser_tool.py`, `tools/browser_cdp_tool.py`) → `approval_required`, or unregistered (T3) for MVP.
  Note: even `browser_navigate` initiates outbound activity → treated as an action, not a read.
- Web: `tools/web_search_tool.py`, `tools/web_extract_tool.py` → `read_only` **only** behind a privacy gate
  (no sensitive prompt/user data egress); otherwise `disabled`.

## 4. Rules

1. Reads (`browser_snapshot`, gated web fetch) may be `read_only`; **no** mutation/side effect.
2. Browser **actions** are `approval_required` per action, or `disabled` in MVP if not needed.
3. Web access is `read_only` only with a **privacy gate**; default `disabled` until that gate exists.
4. A read capability may **never** silently become an action (no "navigate as part of snapshot").
5. All browser actions and web calls (if enabled) are logged.

## 5. Why split read vs. act

Observation is reversible and low-risk; action and outbound web access touch the outside world and can leak
data or take real-world effects (R-05, R-04). Splitting lets Magna keep useful inspection while gating/denying
the dangerous half.

## 6. Boundaries (RC-04 — implementation timing)

- This document is **only a governance model produced in Sprint 3**. It is **not implementation** and does
  not enable, build, or run any browser/web capability.
- No browser/web code is created, modified, or activated in Sprint 3 (or by accepting this model).
- **Future implementation of browser/web capabilities must be separately approved in a later sprint**, after
  the policy gate (Sprint 5) and, for web access, a privacy gate exist. Until then the MVP posture stands:
  browser **actions** `disabled`/`approval_required`, browser **snapshot** `read_only`, web/network access
  `disabled` until a privacy gate exists.
- Accepting this model authorizes the *posture*, not the *implementation*.
