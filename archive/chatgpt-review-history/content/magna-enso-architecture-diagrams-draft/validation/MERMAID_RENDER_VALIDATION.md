# Mermaid Render Validation

Renderer: `@mermaid-js/mermaid-cli` **11.15.0** using its bundled Chromium renderer. Actual rendering was performed; static parsing was not treated as render proof.

Exact command form (the full absolute command is repeated in every raw log):

```bash
<MAGNA_LOCAL_ROOT>/Tools/mermaid-cli/node_modules/.bin/mmdc -i <absolute-input.mmd> -o <absolute-output.svg> -b transparent -t dark
```

Result: **25/25 artifact renders PASS; 24/24 unique Mermaid blocks PASS; 0 parse/render failures.** DIAG-S3 intentionally renders the same source/digest as DIAG-20 because the accepted manifest defines it as a supplementary behavioural view of that block.

| Diagram | Source location | Digest | Exit | Result | Output | Raw log |
|---|---|---:|---:|---|---|---|
| DIAG-01 | `03_MAGNA_PROGRAM_ARCHITECTURE.md:72` | `4e9c82062fc5` | 0 | PASS | `svg/DIAG-01-program-logical-layers.svg` | `raw-validation-output/mermaid-logs/DIAG-01-program-logical-layers.log` |
| DIAG-02 | `03_MAGNA_PROGRAM_ARCHITECTURE.md:50` | `5fd4734a96ee` | 0 | PASS | `svg/DIAG-02-human-authority-governance-hierarchy.svg` | `raw-validation-output/mermaid-logs/DIAG-02-human-authority-governance-hierarchy.log` |
| DIAG-03 | `04_EVOLUTION_AND_REPOSITORY_ARCHITECTURE.md:64` | `8295b7d5cda1` | 0 | PASS | `svg/DIAG-03-repository-versioning.svg` | `raw-validation-output/mermaid-logs/DIAG-03-repository-versioning.log` |
| DIAG-04 | `05_CURRENT_VERIFIED_ARCHITECTURE.md:37` | `b5fe7a2805b2` | 0 | PASS | `svg/DIAG-04-current-verified-command-center.svg` | `raw-validation-output/mermaid-logs/DIAG-04-current-verified-command-center.log` |
| DIAG-05 | `05_CURRENT_VERIFIED_ARCHITECTURE.md:64` | `3691d05c837d` | 0 | PASS | `svg/DIAG-05-current-magna-enso-harness.svg` | `raw-validation-output/mermaid-logs/DIAG-05-current-magna-enso-harness.log` |
| DIAG-06 | `06_MAGNA_ENSO_TARGET_ARCHITECTURE.md:44` | `31bd4dfe5a65` | 0 | PASS | `svg/DIAG-06-target-magna-enso-logical.svg` | `raw-validation-output/mermaid-logs/DIAG-06-target-magna-enso-logical.log` |
| DIAG-07 | `07_REQUEST_TO_ACTION_AND_COGNITION.md:38` | `dd2fbccf9652` | 0 | PASS | `svg/DIAG-07-request-to-action-pipeline.svg` | `raw-validation-output/mermaid-logs/DIAG-07-request-to-action-pipeline.log` |
| DIAG-08 | `07_REQUEST_TO_ACTION_AND_COGNITION.md:84` | `db166c067bbf` | 0 | PASS | `svg/DIAG-08-sensory-attention-reflex-cognition-routing.svg` | `raw-validation-output/mermaid-logs/DIAG-08-sensory-attention-reflex-cognition-routing.log` |
| DIAG-09 | `07_REQUEST_TO_ACTION_AND_COGNITION.md:99` | `6ecaa99368a4` | 0 | PASS | `svg/DIAG-09-event-bus-workflow-orchestration.svg` | `raw-validation-output/mermaid-logs/DIAG-09-event-bus-workflow-orchestration.log` |
| DIAG-10 | `08_GOVERNANCE_POLICY_AND_APPROVAL.md:43` | `99a4a07069ea` | 0 | PASS | `svg/DIAG-10-policy-risk-authorization-approval.svg` | `raw-validation-output/mermaid-logs/DIAG-10-policy-risk-authorization-approval.log` |
| DIAG-11 | `02_TERMINOLOGY_AND_DOMAIN_MODEL.md:143` | `b33b38a6244a` | 0 | PASS | `svg/DIAG-11-identity-helix-cosmos-relationship.svg` | `raw-validation-output/mermaid-logs/DIAG-11-identity-helix-cosmos-relationship.log` |
| DIAG-12 | `10_MEMORY_DATA_EVIDENCE_AND_REPLAY.md:37` | `514c16ce026d` | 0 | PASS | `svg/DIAG-12-memory-persistence-evidence.svg` | `raw-validation-output/mermaid-logs/DIAG-12-memory-persistence-evidence.log` |
| DIAG-13 | `11_AGENTS_MODELS_TOOLS_AND_HERMES.md:34` | `3a7dc4eeddbc` | 0 | PASS | `svg/DIAG-13-agents-models-tools-adapters.svg` | `raw-validation-output/mermaid-logs/DIAG-13-agents-models-tools-adapters.log` |
| DIAG-14 | `09_TRACE_DUAL_PLANE_ARCHITECTURE.md:51` | `c5cd245bd2be` | 0 | PASS | `svg/DIAG-14-trace-engineering-plane.svg` | `raw-validation-output/mermaid-logs/DIAG-14-trace-engineering-plane.log` |
| DIAG-15 | `09_TRACE_DUAL_PLANE_ARCHITECTURE.md:64` | `3156738275ac` | 0 | PASS | `svg/DIAG-15-trace-runtime-plane.svg` | `raw-validation-output/mermaid-logs/DIAG-15-trace-runtime-plane.log` |
| DIAG-16 | `09_TRACE_DUAL_PLANE_ARCHITECTURE.md:74` | `f70951927fce` | 0 | PASS | `svg/DIAG-16-trace-cross-plane-interoperability.svg` | `raw-validation-output/mermaid-logs/DIAG-16-trace-cross-plane-interoperability.log` |
| DIAG-17 | `12_UX_INFORMATION_ARCHITECTURE.md:37` | `72cdb71c2ff6` | 0 | PASS | `svg/DIAG-17-ux-ten-tab-information-architecture.svg` | `raw-validation-output/mermaid-logs/DIAG-17-ux-ten-tab-information-architecture.log` |
| DIAG-18 | `13_ENVIRONMENT_DEPLOYMENT_AND_OPERATIONS.md:43` | `87936473db87` | 0 | PASS | `svg/DIAG-18-local-environments-release.svg` | `raw-validation-output/mermaid-logs/DIAG-18-local-environments-release.log` |
| DIAG-19 | `14_SECURITY_PRIVACY_AND_TRUST_BOUNDARIES.md:37` | `35a56f32add9` | 0 | PASS | `svg/DIAG-19-security-zones-trust-boundaries.svg` | `raw-validation-output/mermaid-logs/DIAG-19-security-zones-trust-boundaries.log` |
| DIAG-20 | `10_MEMORY_DATA_EVIDENCE_AND_REPLAY.md:60` | `1107a8c4fa08` | 0 | PASS | `svg/DIAG-20-observability-replay-recovery-audit.svg` | `raw-validation-output/mermaid-logs/DIAG-20-observability-replay-recovery-audit.log` |
| DIAG-21 | `15_REUSE_AND_MIGRATION_ARCHITECTURE.md:58` | `f12564eab534` | 0 | PASS | `svg/DIAG-21-current-to-target-capability-transition.svg` | `raw-validation-output/mermaid-logs/DIAG-21-current-to-target-capability-transition.log` |
| DIAG-22 | `16_EVOLUTION_STAGE_CONTRACTS.md:75` | `b3b288fe09b7` | 0 | PASS | `svg/DIAG-22-enso-to-beyond-evolutionary-architecture.svg` | `raw-validation-output/mermaid-logs/DIAG-22-enso-to-beyond-evolutionary-architecture.log` |
| DIAG-S1 | `technical-specifications/18_STATE_MACHINE_SPECIFICATIONS.md:26` | `4ded97acee5c` | 0 | PASS | `svg/DIAG-S1-audit-before-effect-order.svg` | `raw-validation-output/mermaid-logs/DIAG-S1-audit-before-effect-order.log` |
| DIAG-S2 | `technical-specifications/19_FAILURE_AND_OUTCOME_TAXONOMY.md:55` | `2e770ffe653e` | 0 | PASS | `svg/DIAG-S2-failure-and-outcome-decision.svg` | `raw-validation-output/mermaid-logs/DIAG-S2-failure-and-outcome-decision.log` |
| DIAG-S3 | `10_MEMORY_DATA_EVIDENCE_AND_REPLAY.md:60` | `1107a8c4fa08` | 0 | PASS | `svg/DIAG-S3-restart-recovery.svg` | `raw-validation-output/mermaid-logs/DIAG-S3-restart-recovery.log` |

The initial sandbox-blocked Chromium failure is preserved in `raw-validation-output/mermaid-initial-sandbox-failure.log`. Authoritative per-diagram logs contain exit code 0 and renderer output. No Mermaid source required semantic changes.
