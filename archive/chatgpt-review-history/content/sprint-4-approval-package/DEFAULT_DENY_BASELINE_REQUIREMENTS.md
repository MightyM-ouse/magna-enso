# DEFAULT_DENY_BASELINE_REQUIREMENTS.md
# Magna Enso — Default-Deny Baseline Requirements
# Type: Local-only approval package
# Date: 2026-06-17
# Status: REQUIREMENTS for the Sprint 4 baseline (if approved). No code.

---

## 1. Purpose

Define the default-deny properties the Sprint 4 baseline must **structurally** preserve, even though runtime
enforcement (the policy engine) does not exist until Sprint 5. Sprint 4 achieves default-deny by **what it
omits** (removed surfaces) and **what it leaves off** (disabled/retained-but-off), not by a running gate.

## 2. Requirements (the baseline must satisfy all)

1. **Unknown capability disabled.** Nothing the design did not explicitly retain exists in an active form.
2. **No implicit tool activation.** No tool self-activates at import/startup; retained tools are present but
   not wired to run (Sprint 2: tool modules self-register at import — this must be broken/controlled).
3. **No plugin self-registration.** The dynamic plugin/MCP loader is removed; no plugin can register a tool.
4. **No external-content capability escalation.** Nothing in the baseline lets inbound/web/memory content
   change capability state (anti prompt-injection, R-07).
5. **No config-only bypass.** Dangerous surfaces are removed or import-disabled (T1/T2), not merely flagged
   off — so a config flip cannot re-enable them.
6. **No dispatch-only protection for dangerous modules.** Dangerous capabilities are not "protected" by a
   single dispatch check; they are removed or import-disabled so no alternate path (cron/gateway/ACP/plugin)
   can reach them.
7. **Retained capabilities mapped to states.** Every retained surface carries its Sprint 3 state
   (active_safe / read_only / draft_only / report_only / approval_required-but-off) recorded in the baseline.

## 2a. Vendor import quarantine requirement (C-03)

Any imported (vendored) Hermes source must be **inert / quarantined** — present but unable to act:

- not wired into runtime; not imported by application code; not exposed through CLI/UI;
- not executable; not registered as tools; not package-discovered as active code.

This is how requirement #2 ("no implicit tool activation") is satisfied at the source level: the vendored
code physically cannot self-activate because nothing imports, discovers, registers, or runs it.

## 3. How Sprint 4 satisfies these without a running engine

| Requirement | Sprint 4 mechanism (structural) |
|---|---|
| Unknown disabled | Selective vendor import — only retained modules exist |
| No implicit activation | Sever/neutralize import-time self-registration; no run wiring |
| No plugin self-registration | Loader removed (T2/T3) |
| No escalation from content | No code path present that maps content → capability state |
| No config bypass | Removed/import-disabled at T1/T2 (not T5 flags) |
| No dispatch-only protection | Dangerous surfaces absent, not gated |
| States mapped | Recorded in `RETAINED_SURFACES_REPORT.md` + baseline manifest |

## 4. The honesty boundary

The baseline is **default-deny by construction** (dangerous things are gone or off), but it is **not
"default-deny enforced at runtime"** — there is no engine making allow/deny decisions yet. Sprint 4 reports
must say "structurally safe / not yet enforced," never "enforcement exists." (See
`POLICY_ENFORCEMENT_PRECONDITION_CHECKLIST.md`.)

## 5. Validation (Sprint 4, post-execution)

Antigravity confirms: no removed surface is present; no retained tool is wired to run; no plugin loader; no
network/cloud/messaging code active; every retained surface has a recorded state. A `DEFAULT_DENY_BASELINE_REPORT.md`
captures this.

## 6. Boundaries

Requirements only. No baseline built by this package.
