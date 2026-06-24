# DISABLEMENT_TIERS_PROPOSAL.md
# Magna Enso — Disablement Tiers Proposal
# Type: Local-only approval package
# Date: 2026-06-17
# Status: PROPOSAL for human approval. Design-only.

---

## 1. Purpose

Define what "disabled" actually means, because the word is ambiguous and a weak interpretation leaves back
doors. Magna Enso proposes **five tiers**, from strongest (the capability does not exist in the process) to
weakest (one call site is blocked).

## 2. The five tiers (strongest → weakest)

| Tier | Name | What it means | Strength |
|---|---|---|---|
| T1 | **Process-level disabled** | The capability/feature is not started; the process never brings it into being (e.g. the API server/listener never boots; remote backend process never launches). | Strongest |
| T2 | **Module import disabled** | The module is not imported/loaded at all — its code is never in memory (e.g. cloud provider SDK, plugin/MCP loader not imported). | Very strong |
| T3 | **Tool registration disabled** | The module may load, but the tool is never registered into the dispatch registry, so it cannot be selected/called. | Strong |
| T4 | **Dispatch-level blocked** | The tool is registered, but the dispatch path checks policy and refuses to invoke it. | Moderate |
| T5 | **Config-level disabled** | A config flag says "off"; relies on every code path honoring the flag. | Weakest |

## 3. Why process/module/registration disablement beats dispatch-only blocking

The Sprint 2 audit found Hermes has **multiple execution paths** to its capabilities (dispatch, startup,
scheduler, gateway, provider, ACP, plugin, MCP). Dispatch-level blocking (T4) only guards **one** of those
paths — if the capability can also be triggered by the scheduler, a gateway, a plugin, or at startup, those
paths are still open. Config flags (T5) are weaker still: any code path that forgets to check the flag is a
hole.

By contrast:
- **T1/T2 (process/module)** remove the capability from existence — there is *no code in memory* to reach,
  by *any* path. Bypass is impossible because there is nothing to bypass.
- **T3 (registration)** means even if code is loaded, no dispatch/registry path can select it.

> Rule of thumb: **the most dangerous surfaces should be removed or disabled at T1–T3, not merely T4/T5.**
> Dispatch/config blocking is acceptable only for lower-risk capabilities, and even then as one layer of
> defense-in-depth, not the only one.

## 4. Recommended tier per high-risk surface (MVP)

| Surface | Recommended disablement | Tier |
|---|---|---|
| Remote execution backends | **Remove** (not just disable) | T1/T2 |
| Background self-improvement | Remove / process-disabled | T1/T2 |
| Direct script cron execution | **Remove** | T1/T2 |
| API server listener / messaging gateways | Process-disabled (not started) | T1 |
| Cloud / provider SDKs | Module import disabled | T2 |
| Plugin / MCP dynamic loading | Loader disabled unless signed allowlist | T2/T3 |
| External memory sync | Disabled or forced through staging | T1/T2 |
| Subagent delegation | Registration disabled in MVP | T3 |
| Lower-risk gated tools (e.g. terminal) | Registered but `approval_required` at dispatch | T4 + gate |

## 5. Defense in depth

Disablement tiers and the default-deny gate are **complementary**: remove/disable dangerous surfaces at the
strongest feasible tier *and* still deny at the policy gate. No single layer is trusted alone.

## 6. Decision linkage

Feeds Decisions 5–8 (remove-vs-disable for plugin/MCP, remote backends, messaging, cloud). Recommendation
captured per surface in `HERMES_SURFACE_GOVERNANCE_PLAN.md`.
