# PLUGIN_MCP_GOVERNANCE_MODEL.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 12 of 17 — Plugin & MCP Governance Model
# Type: Design-only governance report. No code.
# Date: 2026-06-17
# Status: Design only. Human owner is final authority (EH-0010).

---

## 1. Purpose

Define governance for plugin/MCP dynamic expansion (C-15): **disabled unless a signed allowlist applies**.
Dynamic loading can change the capability surface *after* review — the most insidious bypass of a governance
design.

## 2. The core threat

The Sprint 2 audit found dynamic registration changes the runtime tool surface
(`tools/mcp_tool.py`, `tui_gateway/entry.py` background discovery, `hermes_cli/plugins/*`). A capability set
that was reviewed and gated at startup can be **silently extended** at runtime by a plugin/MCP server —
defeating default-deny, the chokepoint map, and the approval engine in one move. The audit also warns plugin
pre-tool-call hooks must **not** be relied on as the primary security boundary.

## 3. Model

```text
default: dynamic plugin/MCP loading = DISABLED  (T2/T3 — loader not imported / not registered)
        │
   signed allowlist present?
   ├─ no  → stays disabled; no dynamic tools
   └─ yes → load ONLY allowlisted, signature-verified entries
              → each loaded tool is still classified by the policy gate (default-deny)
              → no loaded tool may arrive `active`; it enters at its category default state
```

## 4. Rules

1. Default: dynamic plugin/MCP loading **disabled** (loader off — T2/T3).
2. Loading permitted **only** for entries on a **signed allowlist** (signature-verified, human-curated).
3. **No plugin/MCP may self-register an active capability** — loaded tools enter at default-deny and are
   classified by the policy gate like any other capability.
4. Plugin pre-tool-call hooks are **not** treated as a security boundary (defense-in-depth only).
5. The capability surface is **fixed at startup** unless the allowlist mechanism explicitly adds an entry; no
   silent post-startup surface change.
6. Allowlist changes require explicit human approval + Event Horizon entry.

## 5. Removal vs. disable

- **MVP recommendation:** remove/disable the dynamic loader (T2/T3). A signed-allowlist mechanism is a
  *future* capability, not MVP — until it exists, dynamic loading stays off.
- If retained as source for later, it must be import-disabled (T2) so it cannot run.

## 6. Why this matters most

Every other control assumes the capability set is known. Dynamic loading breaks that assumption. Governing it
is what keeps the rest of the design honest — hence "disabled unless signed allowlist," never "on by default."

## 7. Boundaries

Design only. Loader removal/disable is a Sprint 4 fork action; a signed-allowlist mechanism, if ever wanted,
is a separate later sprint with its own approval.
