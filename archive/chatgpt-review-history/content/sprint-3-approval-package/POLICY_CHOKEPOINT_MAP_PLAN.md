# POLICY_CHOKEPOINT_MAP_PLAN.md
# Magna Enso — Policy Chokepoint Map Plan
# Type: Local-only approval package
# Date: 2026-06-17
# Status: PLAN for Sprint 3 execution. Design-only.

---

## 1. Purpose

Plan how Sprint 3 will identify **every** point where a capability can be reached, and ensure **each** is
governed by the policy gate. The Sprint 2 audit's headline risk: Hermes has **no single complete
chokepoint** and **registry dispatch alone is insufficient**. This map closes that gap on paper.

## 2. Paths that must be mapped

Sprint 3 must locate and gate the policy boundary across **all** of these execution paths:

- agent tool execution
- registry dispatch
- agent-owned tools
- cron / scheduler
- gateway / API
- ACP tools
- plugin / MCP loading
- providers
- memory / skill persistence
- outbound delivery

## 3. Mapping method

For each path:
1. **Identify** where, in the Sprint 2 code map (Hermes @ `33b1d144`), the path can invoke a capability.
2. **Decide the gate placement** — ideally a *single* chokepoint the path funnels through.
3. **Assign** the required capability state / approval requirement.
4. **Check coverage** — does this path share the chokepoint with others, or is it a separate door?
5. **Flag gaps** — any path that cannot be funneled to the gate is a bypass risk (escalate).

## 4. Chokepoint coverage matrix (to be filled in Sprint 3)

| Path | Reaches which capabilities | Gate placement | Default state | Covered? |
|---|---|---|---|---|
| agent tool execution | … | … | deny unless classified | ☐ |
| registry dispatch | … | … | deny | ☐ |
| agent-owned tools | … | … | deny | ☐ |
| cron / scheduler | … | report_only | report_only | ☐ |
| gateway / API | … | disabled (T1) | disabled | ☐ |
| ACP tools | … | … | deny | ☐ |
| plugin / MCP loading | … | disabled unless signed allowlist | disabled | ☐ |
| providers | … | disabled (T2) | disabled | ☐ |
| memory / skill persistence | … | draft_only staging | draft_only | ☐ |
| outbound delivery | … | shutdown | disabled | ☐ |

## 5. The single-chokepoint goal vs. reality

Ideal: **one** gate all sensitive actions pass through. Reality (per Sprint 2): Hermes spreads invocation
across many paths. Sprint 3's job is to (a) consolidate as many paths as possible to a single gate, and
(b) for paths that cannot be consolidated, **remove or process-disable** the surface (T1/T2) so there is no
ungated door. The design is only accepted when **every** path is either gated or removed.

## 6. Bypass-resistance (Sprint 4 readiness gate 10)

The map must support a bypass-resistance argument: for each capability, list *all* paths and show each is
gated or removed. "Mostly covered" is not acceptable — one open path defeats the control.

## 7. Output

`POLICY_CHOKEPOINT_MAP.md` (the filled matrix + per-path notes), feeding `SPRINT_4_READINESS_GATES.md`.
Design-only; no instrumentation is added to any code in Sprint 3.
