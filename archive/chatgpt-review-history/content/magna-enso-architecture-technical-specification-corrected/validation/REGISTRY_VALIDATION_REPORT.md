---
document: validation/REGISTRY_VALIDATION_REPORT
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: YAML/JSON parse + enum + coverage validation results (actually run)
date: 2026-06-21
change_control: Results are from actual tool runs this session.
---

# Registry Validation Report

> Tools used: **Ruby/Psych** (`ruby -ryaml`) for YAML, **python3 json** for JSON. PyYAML was **not** installed
> (no dependency installs permitted); Ruby/Psych was used instead and is noted as the parser.

## YAML parse (6/6 VALID)
| File | Result |
|---|---|
| registries/MAGNA_ARCHITECTURE_STATUS.yaml | VALID |
| registries/MAGNA_REQUIREMENT_REGISTRY.yaml | VALID |
| registries/MAGNA_COMPONENT_REGISTRY.yaml | VALID |
| registries/MAGNA_INTERFACE_REGISTRY.yaml | VALID |
| registries/MAGNA_OPEN_DECISIONS.yaml | VALID |
| registries/MAGNA_TRACEABILITY_REGISTRY.yaml | VALID |

## JSON parse (1/1 VALID)
- FOUNDATION_EVIDENCE_INDEX.json — VALID.

## Enum validation (Correction 5)
- Declared dimensions: `implementation_status`, `acceptance_status`, `decision_status`, `evidence_status`,
  `reuse_status` (sets in `MAGNA_ARCHITECTURE_STATUS.yaml:status_dimensions`).
- Scan of all registries for any value outside the declared sets: **NONE undeclared.** PASS.

## Coverage
- Requirements in `MAGNA_REQUIREMENT_REGISTRY.yaml`: **52**.
- Rows in `MAGNA_TRACEABILITY_REGISTRY.yaml`: **52**.
- Rows in `technical-specifications/17` matrix: **52**. PASS (52=52=52).

## Status dimension applied
Every component in `MAGNA_COMPONENT_REGISTRY.yaml` (30) and every requirement (52) carries the applicable
dimensions; target components carry implementation/acceptance/decision/evidence/reuse where applicable. PASS.

## Verdict: PASS (YAML 6/6, JSON 1/1, enums clean, coverage 52/52/52).
