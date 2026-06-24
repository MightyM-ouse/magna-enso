# ARCH-001 Source-to-Target Migration Matrix

## Status

`PRELIMINARY_BLOCKED_MISSING_INPUTS`

| Source ID / artifact | Proposed target | Action | Gate |
|---|---|---|---|
| ARCH-SRC-01 `00_MASTER_FOUNDATION_SUMMARY.md` | `docs/architecture/README.md` plus `foundation/` as content dictates | Curate; do not copy blindly | Exact content and links required |
| ARCH-SRC-01 `06_MAGNA_ENSO_TARGET_ARCHITECTURE.md` | `docs/architecture/runtime/` or `system-context/` | Split only when traceability is preserved | Architecture review |
| ARCH-SRC-01 `16_EVOLUTION_STAGE_CONTRACTS.md` | `docs/technical-specifications/evolution/` | Reconcile with EH-0017 and EH-0018 | Product Owner decision on conflicts |
| ARCH-SRC-01 requirement registry | `docs/technical-specifications/requirements/` | Import as normative registry candidate | Structured parse and ID uniqueness |
| ARCH-SRC-01 traceability matrix | `docs/technical-specifications/traceability/` | Recalculate against accepted targets | 52/52 claim must be independently reproduced |
| ARCH-SRC-01 remaining 54 reported files | Undetermined | MISSING_INPUT; no mapping attempted | Full manifest and contents required |
| DIAG-SRC-01 Draw.io sources | `docs/architecture/diagrams/source/` | Authenticated candidate; import only after normative reconciliation | ZIP checksum verified; per-file manifest present |
| DIAG-SRC-01 SVG previews | `docs/architecture/diagrams/rendered/` | Derived candidates; regenerate from accepted Draw.io sources where possible | Package validation passes; repository claim review pending |
| DIAG-SRC-01 HTML viewer | GitHub Actions artifact or optional documentation tooling | Generated artifact; do not make canonical architecture source | Separate security and maintenance justification required |
| DIAG-SRC-01 behavioral diagrams | `docs/architecture/diagrams/behavioral/` | Three authenticated candidate views; map to contracts/requirements | Normative architecture package required |
| GOV-SRC-01 Sprint 3 reports | Architecture/governance target determined per document | Reference or curate; avoid duplication | Compare against ARCH-SRC-01 |
| `trace/DECISION_LOG.md` | Remains in `trace/` | Reference only | No migration |
| `trace/FEATURE_TRACKER.md` | Remains in `trace/` | Reference only | No migration |
| `trace/evidence/` | Remains in `trace/` | Reference only | No migration |
| `docs/governance/` | Remains in `docs/governance/` | Reference only | No migration |
| `vendor/hermes/` | Remains in `vendor/hermes/` | Reference inert boundary only | No migration or activation |
| HELIX doctrine/contracts | Separate repository with versioned link | Reference, do not copy | Exact contract/version required |
| Draft/corrected ZIP files | Outside source tree or Actions artifacts | Transport only | Never canonical source |

## Phase B sequence

1. Acquire exact source packages and verify top-level and per-file checksums.
2. Produce a complete manifest and machine-readable file inventory.
3. Compare package decisions/requirements with Event Horizon and accepted evidence.
4. Resolve blocking conflicts with recorded Product Owner decisions.
5. Import native text and diagram sources additively into target paths.
6. Regenerate derived SVG/viewer artifacts from accepted native sources.
7. Validate links, YAML/JSON, requirement IDs, diagram parity, secrets, and provenance.
8. Obtain architecture review and independent evidence validation.
9. Present one bounded final diff for Product Owner acceptance and squash merge.

## Rollback

Before acceptance, rollback is branch deletion. After acceptance, corrections use a new
task and explicit supersession; accepted history is not rewritten.
