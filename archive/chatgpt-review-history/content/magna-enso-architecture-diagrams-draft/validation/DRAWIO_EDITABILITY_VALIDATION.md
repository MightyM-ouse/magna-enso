# Draw.io Editability and Edge-Tuple Validation

All 25 files parse as native `mxGraphModel` XML with editable node, grouping, legend, and connector `mxCell` elements; no flattened image cells are present. Semantic cells carry `sourceNodeId`, `diagramId`, `nodeKind`, and component metadata. Grouping containers also carry their Mermaid source identifier.

The independent comparator resolves every Draw.io edge's cell endpoints back to Mermaid identifiers and verifies source, target, direction, label, and dashed/solid relationship as an exact multiset. Result: **25/25 edge-tuple equivalence PASS**. See `DIAGRAM_SEMANTIC_COMPARISON.md` and `raw-validation-output/semantic-comparison.json`.
