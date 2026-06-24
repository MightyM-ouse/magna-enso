---
document: technical-specifications/12_CONFIGURATION_AND_ENVIRONMENTS
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Configuration model and the four local-first environments
current_vs_target: Local/dev + test partly evidenced; UAT/prod PLANNED
date: 2026-06-21
evidence_sources: [08,10 of evidence-completion; package 13]
change_control: Cloud optional/decision-gated. Governed; nothing deleted.
---

# Spec 12 — Configuration and Environments

## Human ToC
1. Purpose/Scope/Non-goals 2. Configuration model 3. The four environments (MAG-OPS-001) 4. Secrets per env
5. Promotion/rollback 6. Acceptance/testing 7. Status/Open 8. Change-control

## AI navigation index
- `config` → §2 (MAG-ENV) · `environments` → §3 · `promotion` → §5

## 1. Purpose/Scope/Non-goals
**Purpose:** deterministic, local-first config across environments. **Non-goals:** mandatory cloud/SaaS; config
flags as authority boundaries (rejected — config cannot raise capability state past `approval_required`).

## 2. Configuration model
Layered local config (defaults → env file → runtime overrides); **config never grants capability** (default-
deny holds); secrets separated from config. PROPOSED config keys validated at startup; invalid ⇒ fail-closed.

## 3. The four environments (MAG-OPS-001)
Local Development · Isolated Test/CI · Release Candidate/UAT · Local Production — full matrix (purpose, data
isolation, secrets, model access, network, test data, logging, backup, promotion, rollback, evidence) in
`13_ENVIRONMENT_DEPLOYMENT_AND_OPERATIONS.md` §2. Cloud staging optional + decision-gated.

## 4. Secrets per env
Each env has scoped local secrets; **never** committed; never in TRACE/evidence; UAT/prod secrets isolated.

## 5. Promotion / rollback (MAG-OPS-003)
Promotion gated on green tests + (for UAT/prod) human sign-off. Rollback: dev = discard branch; UAT/prod =
restore snapshot + replay. **Tags are not releases** (`10`).

## 6. Acceptance / testing
Acceptance: config cannot grant capability; invalid config fails closed; each env's isolation holds. Testing:
config-validation tests; isolation checks.

## 7. Status / Open decisions
Status: dev/test `IMPLEMENTED_VALIDATED`/partial; UAT/prod `PLANNED`. Open: ADR-R9 env topology; OD-13.2 backup
standard; OD-13.3 cloud staging (default no).

## 8. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. PROPOSED marks config keys. Governed; nothing deleted.
