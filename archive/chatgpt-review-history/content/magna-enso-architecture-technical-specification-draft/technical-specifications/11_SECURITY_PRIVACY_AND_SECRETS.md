---
document: technical-specifications/11_SECURITY_PRIVACY_AND_SECRETS
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Security controls, privacy defaults, secrets handling, audit-file security
current_vs_target: Enso secure audit verified at harness; runtime trust boundaries TARGET
date: 2026-06-21
evidence_sources: [05,07 of evidence-completion; package 14]
change_control: Audit integrity-detecting, NOT tamper-proof. Governed; nothing deleted.
---

# Spec 11 — Security, Privacy, and Secrets

## Human ToC
1. Purpose/Scope/Non-goals 2. Security requirements (MAG-SEC) 3. Secrets & privacy 4. Audit-file security
5. Failure/recovery 6. Acceptance/testing 7. Status/Open 8. Change-control

## AI navigation index
- `sec_requirements` → §2 · `secrets` → §3 · `audit_file` → §4

## 1. Purpose/Scope/Non-goals
**Purpose:** enforce privacy-first, fail-closed, no-bypass security. **Non-goals:** claiming tamper-proof
audit; remote/multi-user threat surface (local single-user).

## 2. Security requirements (MAG-SEC-001..008)
Default-deny (001); secure audit file (002); integrity-detecting hash-chain, not tamper-proof (003); no secrets
in evidence + hash redaction (004); explicit local/cloud consent (005); no self-approval, human authority for
approvals (006); monotonic expiry, clock-rollback ⇒ DENY (007); no capability bypass / single chokepoint —
**TARGET, R-06 OPEN** (008).

## 3. Secrets & privacy (MAG-SEC-004)
Secrets in local `.env`/keychain scope, never ingested into TRACE/evidence; provider metadata as digest;
audit stores fingerprint/per-field **hashes**, not raw payloads; redaction must not weaken binding.

## 4. Audit-file security (MAG-SEC-002/003 — `05`)
`0600` owner-only; atomic restrictive creation (no permissive intermediate); owner-UID + regular-file
verification; symlink refusal; re-checked at startup **and before each use**; any failure ⇒ init failure ⇒
DENY-all. **Limit:** detects but cannot prevent same-user tampering; signed/external store = future. Non-POSIX:
closest owner-only ACL + **documented gap**; else fail closed.

## 5. Failure / recovery
Any security-property failure ⇒ DENY-all init; recovery only after secure file re-established; resting
default-deny.

## 6. Acceptance / testing
Acceptance: insecure perms/owner/symlink/non-regular ⇒ DENY-all; no secret in logs; clock-rollback ⇒ DENY.
Testing: audit-file security tests; redaction tests; consent test (`14`).

## 7. Status / Open decisions
Status: Enso secure audit `IN_PROGRESS/IN_REVIEW`; chokepoint completeness `PLANNED` (R-06 OPEN). Open: OD-14.1
tamper-evident store; OD-14.2 verifier identity; OD-14.3 cloud-consent policy.

## 8. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. NOT tamper-proof. Governed; nothing deleted.
