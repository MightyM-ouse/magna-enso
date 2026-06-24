---
document: 14_SECURITY_PRIVACY_AND_TRUST_BOUNDARIES
package: magna-enso-architecture-technical-specification-corrected
status: DRAFT_FOR_HUMAN_REVIEW
authority_level: SUBORDINATE_DRAFT
scope: Security zones, trust boundaries, privacy-first defaults, secrets, audit-file security
current_vs_target: Enso secure-audit verified at harness; runtime trust boundaries are target
date: 2026-06-21
evidence_sources: [05_POLICY_ENGINE_COMPARATIVE_AUDIT.md, 02_CANONICAL_MAGNA_DIRECT_READ.md, 07_RUNTIME_TRACEABILITY_CONTRACT_MAP.md]
change_control: Superseding changes require a governed decision. Do not delete or silently rewrite.
---

# 14 — Security, Privacy, and Trust Boundaries

## Human table of contents
1. Security principles
2. Security zones & trust boundaries (DIAG-19)
3. Secrets & privacy classes
4. Audit-file security (honest limits)
5. Open decisions
6. Change-control note

## AI navigation index
- `principles` → §1 (MAG-SEC-202)
- `zones` → §2 (DIAG-19)
- `secrets_privacy` → §3 (MAG-SEC-202)
- `audit_security` → §4 (MAG-SEC-202)

## 1. Security principles
Privacy-first defaults; default-deny; fail-closed; explicit local/cloud consent; minimal necessary context;
no secrets in TRACE/evidence; durable lineage; **integrity-detecting (not tamper-proof)** audit; independent
verification; no self-certification.

## 2. Security zones & trust boundaries (DIAG-19)

```mermaid
flowchart TB
  subgraph TRUSTED["Trusted zone - local owner - MAG-SEC-202"]
    VINAY["Vinay - authenticated owner"]
    GATE["Capability gate + approvals - MAG-GOV-001"]
    CORE["Runtime core + persistence + audit - MAG-ORC-001 MAG-MEM-001 MAG-SEC-202"]
  end
  subgraph SEMI["Semi-trusted - workers/models - MAG-AGT-001"]
    WORKERS["Workers - propose only, no self-approve"]
    LOCALM["Local models"]
  end
  subgraph UNTRUSTED["Untrusted/external - EXTERNAL"]
    CLOUD["Cloud providers - consent-gated"]
    WEB["Web/search - default mock"]
    HERMES["Hermes-derived - INACTIVE"]
  end
  VINAY --> GATE --> CORE
  WORKERS -. requests through .-> GATE
  LOCALM -. behind gate .-> GATE
  CLOUD -. consent + gate .-> GATE
  WEB -. gate .-> GATE
  HERMES -. blocked until governed activation .-> GATE
  CORE -. read-only facts .-> VERIFIER["Independent verifier - MAG-TRC-201"]
```

Trust decreases left/top→right/bottom; **every** boundary crossing into the trusted zone goes through the gate.

## 3. Secrets & privacy classes
- Secrets live in local `.env`/OS keychain scope; **never** ingested into TRACE/evidence (`07`).
- Provider calls record provider/model/config **digest** + local/cloud classification + consent reference;
  **never** raw secrets or full sensitive payloads by default.
- Audit redaction: store fingerprint/per-field **hashes**, not raw payloads, while preserving verification
  (`05`). Redaction must not weaken the binding.
- Privacy classes are carried in the cross-plane schema (`privacy_class`, `09`).

## 4. Audit-file security (honest limits — `05`)
`0600` owner-only; atomic restrictive creation (no permissive intermediate); owner-UID verification;
regular-file verification; symlink refusal; re-checked at startup **and before each use**. Any failure ⇒
initialization failure ⇒ **DENY-all**. **Limit:** detects but cannot prevent same-user tampering; a signed/
external tamper-evident store is future work. On non-POSIX platforms, apply closest owner-only ACL and
**document the gap**; if the secure property cannot be established, **fail closed**.

## 5. Open decisions
- OD-14.1 — Adoption of a signed/external tamper-evident audit store (future).
- OD-14.2 — Independent verifier identity/process and its read-only access model (`12` item 3).
- OD-14.3 — Cloud-data consent policy formalization (`13` gate 9).

## 6. Change-control note
`DRAFT_FOR_HUMAN_REVIEW`. Audit is integrity-detecting, not tamper-proof. Changes governed; no deletion.
