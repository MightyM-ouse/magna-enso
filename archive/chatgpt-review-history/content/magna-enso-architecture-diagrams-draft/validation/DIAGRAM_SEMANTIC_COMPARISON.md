# Independent Mermaid ↔ Draw.io Semantic Comparison

The comparator independently parses each accepted Mermaid block and each native Draw.io XML file. It compares node identifiers and labels, component-ID tuples, grouping identifiers and labels, and the exact multiset of connector tuples: `(source, target, label, dashed|solid)`. Direction is therefore part of the tuple; reversing an edge fails.

| Diagram | Nodes M/D | Groups M/D | Edges M/D | Node IDs/labels | Component IDs | Edge tuples | Result |
|---|---:|---:|---:|---|---|---|---|
| DIAG-01 | 11/11 | 7/7 | 12/12 | YES | YES | YES | PASS |
| DIAG-02 | 6/6 | 0/0 | 7/7 | YES | YES | YES | PASS |
| DIAG-03 | 10/10 | 2/2 | 10/10 | YES | YES | YES | PASS |
| DIAG-04 | 12/12 | 0/0 | 13/13 | YES | YES | YES | PASS |
| DIAG-05 | 8/8 | 0/0 | 7/7 | YES | YES | YES | PASS |
| DIAG-06 | 10/10 | 7/7 | 11/11 | YES | YES | YES | PASS |
| DIAG-07 | 21/21 | 0/0 | 23/23 | YES | YES | YES | PASS |
| DIAG-08 | 5/5 | 0/0 | 6/6 | YES | YES | YES | PASS |
| DIAG-09 | 5/5 | 0/0 | 6/6 | YES | YES | YES | PASS |
| DIAG-10 | 18/18 | 0/0 | 20/20 | YES | YES | YES | PASS |
| DIAG-11 | 6/6 | 0/0 | 8/8 | YES | YES | YES | PASS |
| DIAG-12 | 7/7 | 0/0 | 7/7 | YES | YES | YES | PASS |
| DIAG-13 | 8/8 | 0/0 | 7/7 | YES | YES | YES | PASS |
| DIAG-14 | 4/4 | 0/0 | 3/3 | YES | YES | YES | PASS |
| DIAG-15 | 4/4 | 0/0 | 4/4 | YES | YES | YES | PASS |
| DIAG-16 | 5/5 | 0/0 | 6/6 | YES | YES | YES | PASS |
| DIAG-17 | 11/11 | 0/0 | 10/10 | YES | YES | YES | PASS |
| DIAG-18 | 5/5 | 0/0 | 5/5 | YES | YES | YES | PASS |
| DIAG-19 | 9/9 | 3/3 | 8/8 | YES | YES | YES | PASS |
| DIAG-20 | 10/10 | 0/0 | 7/7 | YES | YES | YES | PASS |
| DIAG-21 | 6/6 | 2/2 | 5/5 | YES | YES | YES | PASS |
| DIAG-22 | 7/7 | 0/0 | 7/7 | YES | YES | YES | PASS |
| DIAG-S1 | 16/16 | 0/0 | 18/18 | YES | YES | YES | PASS |
| DIAG-S2 | 19/19 | 0/0 | 18/18 | YES | YES | YES | PASS |
| DIAG-S3 | 10/10 | 0/0 | 7/7 | YES | YES | YES | PASS |

Result: **25/25 PASS**. No missing/extra nodes, no node-label or component-ID mismatch, no unresolved Draw.io endpoints, and no missing/extra edge tuples. `semantic_match=true` was written only after these checks passed. Raw evidence: `raw-validation-output/semantic-comparison.json`.
