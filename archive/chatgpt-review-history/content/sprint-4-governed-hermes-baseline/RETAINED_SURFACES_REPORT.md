# Retained Surfaces Report

## Purpose

Record the surfaces retained as metadata/design targets in the Sprint 4 baseline.

## Honesty Statement

This baseline is structurally safe / not runtime-enforced. Retained risky capabilities remain disabled until Sprint 5. No Hermes runtime, build, package script, or dependency install was performed.

## Retained Surface States

| Surface | State | Runtime source imported? | Notes |
|---|---|---:|---|
| Local safe status read | `active_safe` | No | Metadata-only state record. |
| Local sensitive read | `read_only` | No | Future gated local read model; no read implementation imported. |
| Project metadata/status | `active_safe` | No | Metadata-only state record. |
| Memory write model | `draft_only` | No | Candidate Hermes runtime files reference active/external contexts, so source excluded. |
| Skill write model | `draft_only` | No | Candidate Hermes runtime files reference curator/background-review and registry paths, so source excluded. |
| Scheduler metadata | `report_only` | No | Runtime cron source excluded due direct-script/scheduler execution references. |
| Browser snapshot model | `read_only_if_privacy_gated` | No | Browser runtime source excluded; actions disabled/excluded. |
| Terminal/code model | `approval_required_disabled` | No | Execution source excluded; no runtime path imported. |

## Evidence

- `vendor/hermes/retained/RETAINED_SURFACE_STATES.yaml`
- `vendor/hermes/retained/README.md`
- `vendor/hermes/README.md`

## Findings

- Retained means "state recorded for future governed wiring," not "available now."
- No retained surface is executable.
- No retained surface is package-discovered.
- No retained surface has runtime enforcement in Sprint 4.

## Confidence Level

High.

## Risks

- Future implementation must not treat metadata states as enforcement.
- Executable source import remains a future approval and review task.

## Recommendation

Use this retained-state metadata as the Sprint 4 baseline for Antigravity validation. Defer executable retained modules until a future, separately approved task can sever dependencies and implement policy enforcement.
