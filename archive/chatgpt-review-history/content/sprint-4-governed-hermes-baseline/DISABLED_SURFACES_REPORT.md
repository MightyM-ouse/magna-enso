# Disabled Surfaces Report

## Purpose

Record surfaces that Sprint 3 considered disable-able and how Sprint 4 keeps them disabled in the baseline.

## Honesty Statement

This baseline is structurally safe / not runtime-enforced. Retained risky capabilities remain disabled until Sprint 5. No Hermes runtime, build, package script, or dependency install was performed.

## Disabled / Not Active Surfaces

| Surface | Sprint 3 state | Sprint 4 posture |
|---|---|---|
| Curator/self-review | report-only later | Not imported. |
| Scheduler execution | report-only | Not imported; metadata state only. |
| Cloud providers | disabled | Not imported; upstream manifest retained only as text. |
| Subagent delegation | disabled | Not imported. |
| Browser actions | disabled | Not imported. |
| Terminal/code execution | approval-required but disabled | Not imported as executable source; state recorded only. |
| File transfer | disabled | Not imported. |
| Plugin/MCP loading | removed/disabled | Not imported. |

## How Disabled Is Achieved

Disablement is structural:

- No executable Hermes module source is present.
- No package discovery files are active.
- No tool registration code is imported.
- No CLI/UI/runtime path references `vendor/hermes/`.
- Retained states are recorded in `vendor/hermes/retained/RETAINED_SURFACE_STATES.yaml`.

## Confidence Level

High.

## Risks

- This is not runtime enforcement; it is absence/quarantine.
- A future worker must not infer the presence of a policy gate from this baseline.

## Recommendation

Keep all disabled surfaces off until Sprint 5 or later explicitly implements and validates enforcement.
