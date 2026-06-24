# CAPABILITY_POLICY_SCHEMA.md
# Magna Enso — Sprint 3 Capability Governance Design
# Report 2 of 17 — Capability Policy Schema (design concept)
# Type: Design-only governance report. NO executable code. Schema design only.
# Date: 2026-06-17
# Status: Design only. No fork. Human owner is final authority (EH-0010).

---

## 1. Purpose

Define the **schema concept** for a per-capability policy record. This is a *shape and field
specification*, not a parser, validator, or engine. Sprint 5+ implements; Sprint 3 designs.

## 2. Field specification

| Field | Type | Meaning |
|---|---|---|
| `capability_id` | string (stable) | Unique id, e.g. `terminal.exec`, `memory.write` |
| `name` | string | Human-readable name |
| `category` | enum | One of C-01…C-20 (`CAPABILITY_TAXONOMY.md`) |
| `default_state` | enum | Starting state; default `disabled` |
| `allowed_states` | list<enum> | States this capability may ever hold |
| `risk_level` | enum | `low` / `medium` / `high` / `critical` |
| `side_effect_type` | enum | `none` / `local_write` / `external` / `irreversible` |
| `persistence_scope` | enum | `none` / `session` / `local_disk` / `external` |
| `externality_scope` | enum | `none` / `lan` / `internet` |
| `approval_required` | bool | Must route through the unified approval engine to act |
| `audit_required` | bool | Outcome must be logged (Event Horizon / Light Curve) |
| `human_visible` | bool | Action and its result are surfaced to the human |
| `reversible` | bool | Effect can be undone (e.g. draft discard) |
| `owner` | string | Accountable role (Galaxy Catalog) |
| `evidence_required` | enum | `light` / `standard` / `full` |
| `blocked_until` | string | Condition that must clear before any non-disabled state (e.g. `sprint_5`, `signed_allowlist`) |
| `enforcement_tier` | enum | T1…T5 (`DISABLEMENT_TIERS_MODEL.md`) when `disabled` |
| `paths_covered` | list<enum> | All execution paths that can reach it (chokepoint coverage) |
| `notes` | string | Rationale / caveats |

## 3. Illustrative records (design artifacts — NOT code, NOT parsed by anything)

```yaml
# SKETCH ONLY — Sprint 3 design artifact, not executed.
- capability_id: terminal.exec
  name: Terminal / shell execution
  category: terminal_execution            # C-06
  default_state: disabled
  allowed_states: [disabled, approval_required]
  risk_level: critical
  side_effect_type: irreversible
  persistence_scope: local_disk
  externality_scope: lan
  approval_required: true
  audit_required: true
  human_visible: true
  reversible: false
  owner: builder
  evidence_required: full
  blocked_until: sprint_5_policy_engine
  enforcement_tier: T4_plus_gate
  paths_covered: [dispatch, agent_owned, cron, gateway, acp, plugin, mcp, startup]
  notes: "Off by default. Every invocation gated + logged. Block cron no_agent + remote backend bypass."

- capability_id: memory.write
  name: Persistent memory write
  category: persistent_memory             # C-03
  default_state: draft_only
  allowed_states: [disabled, draft_only]
  risk_level: high
  side_effect_type: local_write
  persistence_scope: local_disk
  externality_scope: none
  approval_required: true                  # to PERSIST a staged draft
  audit_required: true
  human_visible: true
  reversible: true
  owner: builder
  evidence_required: standard
  blocked_until: null
  enforcement_tier: null
  paths_covered: [dispatch, agent_owned, acp, cron]
  notes: "Staged via write-approval; external mirroring (C-16) disabled separately."

- capability_id: cloud.provider.call
  name: Cloud/provider model call
  category: cloud_provider_access          # C-11
  default_state: disabled
  allowed_states: [disabled, approval_required]
  risk_level: high
  side_effect_type: external
  persistence_scope: external
  externality_scope: internet
  approval_required: true
  audit_required: true
  human_visible: true
  reversible: false
  owner: validator_safety
  evidence_required: full
  blocked_until: explicit_human_enable
  enforcement_tier: T2_module_import_disabled
  paths_covered: [provider, dispatch, gateway, plugin, mcp]
  notes: "Disabled at provider resolution + module import. Prevent data egress (R-04)."
```

## 4. Schema invariants

- `default_state` defaults to `disabled`; an unknown capability without a record is `disabled`.
- `allowed_states` must **not** include a state less restrictive than the surface's risk justifies; widening
  requires explicit human approval + an Event Horizon entry.
- If `side_effect_type ∈ {external, irreversible}` then `approval_required = true` and `audit_required = true`.
- If `category == disabled-by-default surface` then `enforcement_tier` must be set (no vague "disabled").
- `paths_covered` must list **all** ways the capability can be reached (validated against `POLICY_CHOKEPOINT_MAP.md`).

## 5. Boundaries

Schema design only. No engine, no validation code, no file written into `magna-enso/`. The implementing
engine and a real policy file format are Sprint 5 work, separately approved.
