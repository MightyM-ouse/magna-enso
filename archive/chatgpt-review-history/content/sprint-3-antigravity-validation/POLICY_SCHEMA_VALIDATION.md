# POLICY_SCHEMA_VALIDATION.md
# Magna Enso — Sprint 3 Capability Governance Design
# Policy Schema Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-17

---

## 1. Purpose

Validate that the CAPABILITY_POLICY_SCHEMA.md field specification is sufficient for
governing risk, externality, persistence, approval, audit, reversibility, ownership,
evidence, blocked-until gates, and path coverage. Validate that the illustrative YAML
records are design sketches only (not executable code).

---

## 2. Field Coverage Assessment

Required dimensions and the fields that cover them:

| Required Dimension | Schema Fields | Sufficient? | Assessment |
|---|---|---|---|
| Risk | risk_level (low/medium/high/critical) | YES | Enum covers all Magna risk levels |
| Externality | externality_scope (none/lan/internet), side_effect_type (none/local_write/external/irreversible) | YES | Two-field combination correctly captures both scope and type |
| Persistence | persistence_scope (none/session/local_disk/external) | YES | Covers all Hermes persistence patterns |
| Approval | approval_required (bool) + enforcement_tier | YES | Bool gates the engine; tier specifies disablement strength |
| Audit | audit_required (bool) + evidence_required (light/standard/full) | YES | Two-level audit spec: whether to log, and how much |
| Reversibility | reversible (bool) | YES | Simple; sufficient for capability-level policy |
| Ownership | owner (string — Galaxy Catalog role) | YES | Aligns with STAR_MAP.md role registry |
| Evidence | evidence_required (light/standard/full) | YES | Three levels match Magna Light Curve evidence system |
| Blocked-until gates | blocked_until (string condition) | YES | Flexible string allows sprint-based, approval-based, and allowlist-based gates |
| Path coverage | paths_covered (list<enum> — P-01 through P-13) | YES | Directly references POLICY_CHOKEPOINT_MAP.md boundary identifiers |

All 9 required dimensions are covered. PASS.

---

## 3. Field-by-Field Assessment

| Field | Assessment |
|---|---|
| capability_id | CORRECT — stable unique identifier; allows machine-readable policy lookup |
| name | CORRECT — human-readable reference |
| category | CORRECT — references CAPABILITY_TAXONOMY.md C-01…C-20 enum |
| default_state | CORRECT — starts disabled; invariant in §4 enforces this |
| allowed_states | CORRECT — bounds what states a capability may ever enter |
| risk_level | CORRECT — 4-level enum aligns with Magna risk register |
| side_effect_type | CORRECT — external and irreversible both require approval=true (invariant) |
| persistence_scope | CORRECT — session/local_disk/external correctly captures Hermes state models |
| externality_scope | CORRECT — none/lan/internet covers all Hermes surfaces |
| approval_required | CORRECT — bool; the invariant (§4) requires true if side_effect_type ∈ {external, irreversible}) |
| audit_required | CORRECT — bool |
| human_visible | CORRECT — surfaces to the human even if they don't approve (situational awareness) |
| reversible | CORRECT — drives presentation in unified approval engine |
| owner | CORRECT — Galaxy Catalog role (builder, validator_safety, etc.) |
| evidence_required | CORRECT — light/standard/full; drives Light Curve evidence depth |
| blocked_until | CORRECT — sprint conditions, allowlist conditions, explicit_human_enable |
| enforcement_tier | CORRECT — T1…T5 from DISABLEMENT_TIERS_MODEL.md |
| paths_covered | CRITICAL — must list all paths through which the capability can be reached |
| notes | CORRECT — rationale field; human-readable |

Total: 19 fields covering all required governance dimensions.

---

## 4. Schema Invariants Assessment

§4 defines four binding invariants:

| Invariant | Assessment |
|---|---|
| default_state defaults to disabled; unknown capability without record = disabled | CORRECT — enforces Rule 7 (default-deny) at the schema level |
| allowed_states must not include state less restrictive than risk justifies; widening requires human approval + Event Horizon | CORRECT — prevents accidental capability promotion via schema edit |
| If side_effect_type ∈ {external, irreversible} then approval_required=true AND audit_required=true | CORRECT AND IMPORTANT — closes the risk that a high-risk capability forgets to require approval |
| If category == disabled-by-default surface then enforcement_tier must be set (no vague "disabled") | CORRECT — directly resolves the Sprint 2 validation note (VA-07) about undefined disablement enforcement tier |

All four invariants are correctly stated and together enforce:
1. Default-deny at schema level
2. No silent capability widening
3. External/irreversible actions always gated and audited
4. Disablement enforcement tier always specified (no ambiguous config-flag disablement)

Assessment: INVARIANTS ARE COMPLETE AND CORRECTLY DESIGNED. PASS.

---

## 5. YAML Design Sketch Assessment

Three illustrative records are provided: terminal.exec, memory.write, cloud.provider.call.

| Record | Design-sketch quality | Key field values | Assessment |
|---|---|---|---|
| terminal.exec | LABELED "# SKETCH ONLY — Sprint 3 design artifact, not executed." | default=disabled; allowed=[disabled, approval_required]; risk=critical; side_effect_type=irreversible; paths_covered=[dispatch, agent_owned, cron, gateway, acp, plugin, mcp, startup]; blocked_until=sprint_5_policy_engine | CORRECT AND THOROUGH — paths_covered correctly lists all major dispatch paths; enforcement_tier=T4_plus_gate is consistent with terminal being retained |
| memory.write | Same label | default=draft_only; allowed=[disabled, draft_only]; approval_required=true (to persist); reversible=true; paths_covered=[dispatch, agent_owned, acp, cron] | CORRECT — correctly shows only draft_only in allowed states; approval required to persist; external sync (C-16) disabled separately |
| cloud.provider.call | Same label | default=disabled; allowed=[disabled, approval_required]; enforcement_tier=T2_module_import_disabled; paths_covered=[provider, dispatch, gateway, plugin, mcp] | CORRECT — T2 (module import) is the right tier; blocked_until=explicit_human_enable is appropriately stringent |

Assessment: All three illustrative records are high quality, correctly labeled as non-executed
design artifacts, and consistent with the field specification and invariants. PASS.

---

## 6. Completeness Note on paths_covered

The paths_covered field requires enumerating all ways a capability can be reached.
This is the hardest field to get right in practice — Sprint 4 implementation must
verify that every path_covered entry corresponds to an actual gated or removed boundary
in the fork, and that no additional paths exist.

The terminal.exec example lists 8 paths. If any are missed in the fork implementation,
the default-deny model (Rule 7: path not in paths_covered → DENY + ESCALATE) provides
the safety net. This is the correct defense-in-depth design.

---

## 7. Policy Schema Verdict

```
All 9 required dimensions covered:    PASS (19 fields total)
Field specifications complete:        PASS
4 schema invariants:                  CORRECT — close Sprint 2 VA-07 gap
YAML records are design sketches:     CONFIRMED (labeled; not executable)
paths_covered field:                  CRITICAL field correctly present
Invariant 4 (enforcement_tier):       Directly resolves Sprint 2 VA-07 concern
No code:                              CONFIRMED

POLICY SCHEMA VALIDATION: PASS
```
