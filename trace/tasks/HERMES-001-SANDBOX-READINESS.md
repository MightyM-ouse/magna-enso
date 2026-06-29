# HERMES-001 — Hermes Sandbox Readiness Design

Status: `PLANNED`
Agent: Hermes planning only
Assigned branch: `hermes/HERMES-001-sandbox-readiness`
Base recommendation: current `main` at launch time
Instruction authority: ChatGPT / System Architect
Product Owner authority: required before launch and merge

## Goal

Prepare a sandbox-readiness and activation-design report for future Hermes use in Magna. This task does not activate Hermes as an operational worker and does not authorize Hermes to modify repository code or execute autonomous actions.

## Outcome-oriented requirement

The worker must design practical activation boundaries for Hermes by inspecting existing governance context and identifying safe uses, prohibited uses, logging requirements, evidence requirements, network/download limits, and escalation gates.

## Allowed outputs

The worker may create or update only:

```text
trace/reviews/HERMES-001-SANDBOX-READINESS.md
trace/evidence/HERMES-001-HANDOFF.md
trace/evidence/HERMES-001-HANDOFF.json
```

## Allowed actions

The worker may:

- Review existing Hermes-related repository documents and archived Hermes audit materials.
- Define possible future Hermes use cases.
- Define sandbox boundaries and prohibited actions.
- Define logging, provenance, and review requirements.
- Recommend activation prerequisites.
- Commit and push only to `hermes/HERMES-001-sandbox-readiness`.
- Open a draft PR targeting `main`, unless launch prompt specifies another base.

## Protected paths and forbidden actions

The worker must not:

- Activate Hermes as an operational worker.
- Modify repository code, workflows, validators, schemas, GOV-005, GOV-006, ARCH-001, runtime, HELIX, SGN-01, or product behavior.
- Access credentials, private services, paid services, or system files.
- Execute external actions beyond bounded public research explicitly approved in the launch prompt.
- Modify another agent branch.
- Push to `main`.
- Merge, close issues, delete branches, force-push, or mark Hermes accepted.

## Required report sections

The readiness report must include:

1. Proposed Hermes role in Magna.
2. Allowed future use cases.
3. Prohibited actions.
4. Sandbox boundaries.
5. Network and download rules.
6. Credential and system-access rules.
7. Logging and provenance requirements.
8. Review and approval gates.
9. Integration with GOV-005 bounded autonomy.
10. Activation prerequisites and open decisions.

## Handoff contract

The final chat response from the worker must be short and include:

- Branch and final commit.
- Draft PR link.
- Readiness verdict.
- Evidence paths.
- Product Owner decisions required.

Detailed readiness analysis must stay in the repository.
