---
document: 18_ARCHITECTURE_DIAGRAM_MANIFEST
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Exact manifest of all 22 architecture views for later Draw.io conversion (no Draw.io/SVG/HTML here)
current_vs_target: Manifest spans current and target; each diagram carries the distinction
date: 2026-06-21
evidence_sources: [all package documents 00-17]
change_control: Superseding changes require a governed decision. Do not delete or silently rewrite.
---

# 18 — Architecture Diagram Manifest

> 22 required views. Each has a stable ID, a source document (with the Mermaid block), and node→status→colour
> mappings so Codex can convert **without architectural interpretation**. **No Draw.io XML/SVG/HTML is
> generated here.** Colour model is defined in `02` §5.

## Human table of contents
1. Diagram register (DIAG-01 … DIAG-22)
2. Node status/colour convention
3. Conversion rules for Codex
4. Open decisions
5. Change-control note

## AI navigation index
- `diagram_register` → §1
- `colour_convention` → §2 (`02` §5)
- `conversion_rules` → §3

## 1. Diagram register

| ID | View | Source doc (Mermaid lives here) | Plane | Current/Target |
|---|---|---|---|---|
| DIAG-01 | Program logical layers | `03` §4 | both | both |
| DIAG-02 | Human authority & governance hierarchy | `03` §3 | both | both |
| DIAG-03 | Repository & versioning | `04` §4 | both | current+target |
| DIAG-04 | Current verified Command Center | `05` §1 | runtime | current |
| DIAG-05 | Current Magna Enso (harness) | `05` §2 | runtime | current |
| DIAG-06 | Target Magna Enso logical | `06` §2 | runtime | target |
| DIAG-07 | Request-to-action pipeline | `07` §1 | runtime | target |
| DIAG-08 | Sensory/attention/reflex/cognition/routing | `07` §2 | runtime | target |
| DIAG-09 | Event bus / workflow / orchestration | `07` §3 | runtime | current+target |
| DIAG-10 | Policy / risk / authorization / approval | `08` §2 | runtime | current+target |
| DIAG-11 | Identity / HELIX / Cosmos relationship | `02` §6 | both | both |
| DIAG-12 | Memory / persistence / evidence | `10` §2 | runtime | current+target |
| DIAG-13 | Agents / models / tools / adapters | `11` §2 | runtime | current+target |
| DIAG-14 | TRACE engineering plane | `09` §2 | engineering | current |
| DIAG-15 | TRACE runtime plane | `09` §3 | runtime | target |
| DIAG-16 | TRACE cross-plane interoperability | `09` §4 | both | target |
| DIAG-17 | UX ten-tab information architecture | `12` §2 | runtime | current |
| DIAG-18 | Local environments & release | `13` §3 | both | current+target |
| DIAG-19 | Security zones & trust boundaries | `14` §2 | both | both |
| DIAG-20 | Observability / replay / recovery / audit | `10` §4 | runtime | current+target |
| DIAG-21 | Current-to-target capability transition | `15` §3 | both | both |
| DIAG-22 | Enso-to-Beyond evolutionary architecture | `16` §3 | both | target |

All 22 views are present and accounted for. Each Mermaid block tags nodes with architecture IDs (`MAG-*`) and,
where status differs from the diagram default, an inline status word.

> **Corrected (C1/C6):** diagrams contain **two kinds of node**. **Component nodes** carry a **full component
> ID** (`MAG-XXX-0NN`) that resolves to `registries/MAGNA_COMPONENT_REGISTRY.yaml` (the authoritative map).
> **Non-component nodes** — actors (e.g. Vinay), states (`AUDIT_CONFIRMED`, `EXECUTION_STARTED`), outcomes
> (`DENY_POLICY`, `UNAVAILABLE`, …), repositories (`magna-enso`, `magna-satori`, …), external systems
> (Hermes, cloud providers), and grouping subgraphs — **do not and need not** carry a component ID. Validation
> therefore checks that **every component node** resolves, **not** that every node is a component (see
> `validation/ID_AND_REFERENCE_VALIDATION_REPORT.md`, which reports total nodes and component nodes
> separately). DIAG-03, DIAG-06 and DIAG-22 reflect the corrected repository model (magna-enso = forward Enso
> repo; future stages = separate repos; "Kensho" → KENOSHA).
>
> **Supplementary state/outcome diagrams (not part of the 22 architecture views):** `DIAG-S1` audit-before-
> effect order (`technical-specifications/18` §1), `DIAG-S2` outcome decision (`technical-specifications/19`
> §4), `DIAG-S3` restart/recovery (`10` §4). These are behavioural state machines, listed here for
> completeness; the **22 required architecture views remain DIAG-01…DIAG-22**.

## 2. Node status/colour convention (apply per node)
Map each node's status word to the colour model in `02` §5. Plane distinction: **engineering-plane** nodes
(MAG-TRC-201 engineering) get Blue; **runtime-plane** nodes keep their status colour. **Current** nodes get a solid
border; **target/conceptual** nodes get a dashed border.

Default status by diagram (override inline where a node says otherwise):

| ID | Default node status | Notes |
|---|---|---|
| DIAG-04 | `IMPLEMENTED_VALIDATED` (light green, solid) | verified MCC |
| DIAG-05 | `IN_PROGRESS` (amber, solid) | Enso harness, not accepted |
| DIAG-06, 07, 08 | `PLANNED` (grey, dashed) | target |
| DIAG-09, 10, 12, 20 | mixed: MCC nodes light green/solid, Enso/target grey/dashed | current+target |
| DIAG-14 | `IMPLEMENTED_VALIDATED` template; Blue for TRACE | UI-build node `IN_PROGRESS` |
| DIAG-15, 16, 22 | `PLANNED` (grey, dashed); Blue for TRACE/governance | target |
| DIAG-17 | `IMPLEMENTED_VALIDATED` (light green, solid) | frozen shell |
| Hermes nodes (DIAG-06/11/13/19/21) | `EXTERNAL`/`BLOCKED` (purple/red, dashed) | inactive 0/6 |
| SGN nodes (wherever shown) | `BLOCKED` (red) | stays blocked |

## 3. Conversion rules for Codex (no interpretation)
1. Use the exact Mermaid block in the cited source doc; do not redraw or re-layout semantically.
2. Apply colour strictly from node status per `02` §5 and §2 above.
3. Preserve every architecture ID label verbatim.
4. Solid border = current/implemented; dashed border = target/conceptual.
5. Mark human-approval edges/nodes (those touching MAG-GOV-001 approval) distinctly (e.g. Blue border).
6. Do **not** add nodes, capabilities, or statuses not present in the source doc.
7. Hermes nodes must never be coloured as active.

## 4. Open decisions
- OD-18.1 — Confirm colour model before Draw.io generation (`02` §5 is a proposal).
- OD-18.2 — Whether DIAG-11 should also be duplicated into `technical-specifications/07_...` for spec readers.

## 5. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Manifest only; no Draw.io/SVG/HTML generated. Changes governed; nothing deleted.
