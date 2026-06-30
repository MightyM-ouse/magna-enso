# MAG-US-HERMES-001 — Magna-Branded Hermes Runtime Identity

Status: READY_FOR_REFINEMENT
Epic: Magna-Hermes Runtime Adoption
Sprint Group: Sprint 1 — Control Foundation
Capability Area: Identity / Command / Governance Visibility
Product Owner: Vinay / Product Owner
Priority: P0
Source: `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`

## User Story

As a Magna user, I want Hermes runtime interactions to appear under the Magna Enso identity, so that I experience one coherent Magna command environment instead of separate underlying tools.

## User Value

The user experiences Magna as the single product surface, even when selected Hermes runtime capabilities operate underneath. This protects product identity, reduces confusion, and keeps governance, approvals, TRACE evidence, and command language aligned to Magna rather than exposing multiple disconnected tool identities.

## User Flow

1. User initiates or receives a runtime interaction through Magna.
2. Magna presents the interaction using Magna Enso product language and branding.
3. If runtime evidence needs to mention Hermes, Magna records Hermes as the runtime provider in evidence rather than replacing the user-facing product identity.
4. User can understand that Magna is the governed experience and Hermes is only an underlying runtime capability provider.

## Acceptance Criteria

- [ ] User-facing runtime messages use Magna / Magna Enso language.
- [ ] Internal evidence may record Hermes as the runtime provider.
- [ ] The distinction between Magna identity and Hermes runtime is documented for Product Owner review.
- [ ] No existing Magna governance terminology is replaced by Hermes terminology.
- [ ] The user can understand that Magna remains the command experience and authority surface.
- [ ] Runtime-provider details are not exposed in a way that makes the product feel like separate tools.

## Out of Scope

- Replacing Magna branding with Hermes branding.
- Replacing Magna governance terms with Hermes terms.
- Creating runtime implementation tasks.
- Creating technical subtasks.
- Assessing Hermes code integration.

## Branding Dependency — PR #33

PR #33 is a branding dependency for this story. It must not be assumed merged or accepted unless GitHub confirms it.

- If PR #33 is not merged, this story remains dependent on branding acceptance before animated identity or loading behavior can be specified.
- Magna identity rules must be preserved regardless of PR #33 status.
- Hermes must not replace Magna identity in any surface.
- Any animated identity or loading behavior must follow approved Magna branding.
- If animated identity behavior is included, a reduced-motion fallback is required where applicable.

## Dependencies

- Product dependency: Magna Enso product identity and brand rules.
- Product dependency: PR #33 — Animated Magna identity branding. **Status: unresolved dependency until GitHub confirms merge.** Story 001 remains dependent on branding acceptance if PR #33 is not merged.
- Architecture dependency: Not created yet.
- Governance dependency: Not created yet.
- Data/runtime dependency: Not created yet.

## Open Questions

- Which user-facing messages are allowed to mention Hermes by name, if any?
- Should an About/System screen disclose Hermes as a runtime provider while keeping Magna as the main identity?

## Downstream Work

No sprint implementation tasks or technical subtasks are created in this story. Downstream work must be created only after Product Owner review and approval.

## Validation Notes

Validation must confirm that the user experiences Magna as one coherent product identity and that Hermes is represented only as an underlying runtime provider where evidence or transparency requires it.
