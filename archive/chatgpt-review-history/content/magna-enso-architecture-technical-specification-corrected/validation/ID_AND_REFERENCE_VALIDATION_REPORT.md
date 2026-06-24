---
document: validation/ID_AND_REFERENCE_VALIDATION_REPORT
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Architecture/requirement ID + cross-reference + Mermaid-node-label validation (actually run)
date: 2026-06-21
change_control: Results from actual scans this session.
---

# ID and Reference Validation Report (Corrections 6 & 7)

## ID scheme
- Components: **full IDs** `MAG-XXX-0NN`. Count **30**, **0 duplicates**.
- Requirements: **52**, **0 duplicates**.
- `MAG-UX-*` requirement-only; UX architecture components use `MAG-EXP-*`.
- `MAG-SEC`/`MAG-TRC` are both requirement and architecture families → **components use a 200-block**
  (`MAG-SEC-2NN`, `MAG-TRC-2NN`) so they never collide with requirement IDs. PASS.

## Cross-reference integrity (registries)
| Check | Result |
|---|---|
| Requirement `component:` → component registry `id:` | **0 missing** |
| Interface `between:` member IDs → component registry | **0 missing** |
| Traceability `component:` → component registry | **0 missing** |

## Mermaid node validation (scans actual diagram nodes; classifies component vs non-component)
Method: parse each fenced mermaid block in every `.md` (lines between a mermaid fence open and close), extract
each flowchart node label, and **classify it**:
- **Component node** — its label contains a full component ID (`MAG-XXX-0NN`); validated against
  `registries/MAGNA_COMPONENT_REGISTRY.yaml`.
- **Non-component node** — an actor (e.g. Vinay), a state (`AUDIT_CONFIRMED`, `EXECUTION_STARTED`), an outcome
  (`DENY_POLICY`, `UNAVAILABLE`, …), a repository (`magna-enso`, `magna-satori`, …), an external system
  (Hermes, cloud providers), or a grouping subgraph. These **are not required** to carry a component ID.

> **We do NOT claim every node maps to a component ID.** Only **component nodes** must resolve.

| Metric | Result |
|---|---|
| Total flowchart node labels scanned | **227** |
| Component nodes (carry a full component ID) | **128** |
| Non-component nodes (actors / states / outcomes / repositories / external / grouping) | **99** |
| Component-ID tokens validated against registry (incl. multi-ID labels) | **146** |
| Component-ID tokens NOT present in registry | **0 (NONE)** |
| Bare family tokens (e.g. `MAG-GOV`) inside Mermaid blocks | **0** |
| Legacy 2-digit IDs (`MAG-TRC-01`, `MAG-MEM-02`, `MAG-ENV-01`, `MAG-COG-01`) in any doc | **0** |

(`stateDiagram-v2` blocks in spec 18 use state names + transition annotations; component IDs there appear in
transition text and are included in the 146-token check.)

Fixes applied across this and the prior pass: bare family tokens and legacy 2-digit IDs replaced with full
registry IDs; `MAG-SEC-002` (a requirement-ID form) used as a component label in spec 18 corrected to the
audit-sink component `MAG-SEC-202`; spec 18 governed execution adapter corrected `MAG-TOL-002` → `MAG-TOL-001`;
spec 18 §8 bare `MAG-OPS` replaced with full requirement IDs `MAG-OPS-002/003/004`.

Note: family-**definition** tables (e.g. `02` §2) intentionally still list bare family prefixes in backticks
(`​`MAG-GOV`​`) — those are family declarations, not component references, and are correctly preserved.

## Cross-registry acceptance consistency (Correction 5)
- MAG-FR-011, MAG-FR-016, MAG-UX-001 reconciled to `acceptance_status: NOT_SUBMITTED` across requirement
  registry, traceability registry, and the matrix. **Acceptance mismatches: 0.**

## Verdict: PASS — no duplicate IDs; all registry refs resolve; all 146 Mermaid node-label IDs valid;
acceptance reconciled (0 mismatches).
