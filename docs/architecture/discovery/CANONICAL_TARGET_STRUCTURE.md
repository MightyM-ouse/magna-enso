# ARCH-001 Proposed Canonical Target Structure

## Status

`PROPOSED_NOT_ACCEPTED`

This is an information-architecture proposal. No target folders other than
`docs/architecture/discovery/` are created in Phase A.

```text
docs/
  architecture/
    README.md
    foundation/
    system-context/
    runtime/
    governance-boundaries/
    evolution/
    decisions/
    diagrams/
      source/
      rendered/
      behavioral/
    discovery/
  technical-specifications/
    README.md
    requirements/
    contracts/
    interfaces/
    data/
    security/
    governance/
    evolution/
    traceability/
  archive/
    architecture/
```

## Folder responsibilities

| Path | Responsibility | Excludes |
|---|---|---|
| `docs/architecture/README.md` | Navigation, authority, version, status vocabulary | Full specifications and delivery claims |
| `foundation/` | Product identity, principles, scope and architecture drivers | Mutable sprint status |
| `system-context/` | Actors, external systems, trust boundaries, context views | Component implementation details |
| `runtime/` | Intended runtime containers/components and flows | Claims that unimplemented behavior exists |
| `governance-boundaries/` | Architecture-level policy chokepoints and human authority | Duplicated governance procedures |
| `evolution/` | Enso contracts and versioned cross-stage interfaces | Code or doctrine copied from other stage repositories |
| `decisions/` | Architecture Decision Records linked to Event Horizon decisions | Rewriting the append-only Event Horizon |
| `diagrams/source/` | Native editable Draw.io sources | Generated previews |
| `diagrams/rendered/` | Reviewable SVG exports generated from sources | Independent hand-edited truth |
| `diagrams/behavioral/` | Sequence/state/journey diagram sources and renders | Unrelated UI mockups |
| `technical-specifications/requirements/` | Normative requirement definitions and registry | Feature delivery status |
| `contracts/` | Versioned behavioral and cross-boundary contracts | Implementation code |
| `interfaces/` | API, event, message, CLI and UI contracts | Runtime deployment evidence |
| `data/` | Schemas, persistence, retention and migration contracts | Live/private data |
| `security/` | Threat model and technical security requirements | Secrets or operational credentials |
| `governance/` | Technical enforcement requirements mapped to governance authority | Governance policy duplication |
| `traceability/` | Requirement-to-decision-to-design-to-test mapping | Unsupported percentages |
| `archive/architecture/` | Superseded active documents with provenance | Accepted historical TRACE evidence |

## Naming rules

1. Use stable descriptive names; numeric prefixes are migration metadata, not permanent
   identity unless a package contract requires them.
2. Every normative document declares ID, version, status, authority, source, supersedes,
   and last-reviewed date.
3. Mermaid may live in Markdown for semantic diagrams. Draw.io is the native source for
   editable visual assets; SVG is a generated review artifact.
4. Filenames use uppercase snake case only where the existing repository convention makes
   stable identifiers useful. ADRs use `ADR-NNNN-short-title.md`.
5. No document may use `current`, `implemented`, or `verified` without repository
   evidence and an explicit status field.
6. Cross-stage references use versioned contracts and repository links, not copied folders.

## Authority model

- Event Horizon decisions remain authoritative in `trace/DECISION_LOG.md`.
- Architecture documents describe intended structure.
- Technical specifications define normative behavior.
- Code/tests/configuration prove implemented behavior.
- Light Curves prove task evidence.
- The Star Map summarizes verified delivery state.

## Rollback and supersession

Phase B imports must be additive until review. Superseded candidate files move only after
Product Owner acceptance and retain a manifest containing original path, checksum, source,
replacement, decision, and date. Generated renders can be regenerated; native sources and
normative text cannot be discarded.
