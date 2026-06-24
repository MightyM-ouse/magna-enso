# Magna Enso Architecture Diagram Package — Corrected Draft

This documentation/artifact package converts the accepted architecture source into editable Draw.io, rendered SVG, and an offline static HTML viewer. It does not alter the accepted source or grant architecture acceptance.

## Contents

- `html/index.html`: offline diagram viewer.
- `DIAGRAM_INDEX.json`: machine index with registry-derived requirements, decisions, provenance, and semantic-match gates.
- `drawio/`: native editable diagram sources.
- `svg/`: Mermaid-rendered diagrams.
- `validation/`: validation and correction evidence.
- `raw-validation-output/`: parsers, detailed machine results, command logs, repository snapshots, and hashes.

## Portability boundary

The viewer, SVGs, Draw.io files, search, filters, and zoom implementation have no runtime network dependency and remain usable offline. The accepted Markdown source is intentionally not duplicated. Links labelled **Source Markdown (requires sibling accepted package)** work only when `magna-enso-architecture-technical-specification-corrected` remains beside the extracted diagram-package folder. Those links are not claimed to be standalone or self-contained.

## Derivation and semantic gates

Requirements come only from exact component-to-requirement rows in `MAGNA_TRACEABILITY_REGISTRY.yaml`, and every result is checked against the 52 IDs in `MAGNA_REQUIREMENT_REGISTRY.yaml`. Decisions come only from the exact Mermaid block, exact manifest entry, and traceability rows related through the diagram's components. Draw.io semantics pass only after independent comparison of node IDs/labels/component IDs and connector source/target/direction/label/dashed-solid tuples.

## Browser status

Automated static checks pass. Interactive browser QA remains **HUMAN_REVIEW_PENDING** and is not represented as completed.

## Rendering tool

Mermaid CLI `11.15.0` is installed outside all Git repositories at `<MAGNA_LOCAL_ROOT>/Tools/mermaid-cli/`.
