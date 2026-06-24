# SOURCE_SHA_AND_PROVENANCE_VALIDATION.md
# Magna Enso — Sprint 4 Clean Governed Hermes Baseline Preparation
# Source SHA and Provenance Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-18

---

## 1. Purpose

Confirm that the Hermes reference SHA used is exactly 33b1d144590a211100f42aa911fd7f91ba031507,
that no newer upstream main was used, and that no hidden source update occurred.

---

## 2. Clone SHA Verification

| Check | Expected | Observed | Result |
|---|---|---|---|
| Hermes clone HEAD | 33b1d144590a211100f42aa911fd7f91ba031507 | 33b1d144590a211100f42aa911fd7f91ba031507 | PASS |
| Source path | <MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/ | Same (confirmed) | PASS |
| Approved SHA used in manifest | 33b1d144590a211100f42aa911fd7f91ba031507 | 33b1d144590a211100f42aa911fd7f91ba031507 | PASS |
| Moving upstream main used | NO | NO — fixed SHA from Sprint 2 clone | PASS |

The clone is the same Sprint 2 read-only clone from `33b1d144590a211100f42aa911fd7f91ba031507`.
It was not re-cloned, not updated, not reset to a newer SHA. PASS.

---

## 3. SHA-256 Artifact Verification (Independently Computed)

All three upstream-derived artifacts were independently SHA-256 hashed by Antigravity
and cross-verified against both the HERMES_SOURCE_PROVENANCE_MANIFEST.md manifest and
the original Hermes clone files at the approved SHA.

| Artifact | Vendor Path | Claimed SHA (manifest) | Actual SHA (Antigravity) | Clone SHA | Result |
|---|---|---|---|---|---|
| LICENSE → UPSTREAM_LICENSE.txt | vendor/hermes/UPSTREAM_LICENSE.txt | 821556e6...2a5ab6 | 821556e6...2a5ab6 | 821556e6...2a5ab6 | EXACT MATCH |
| pyproject.toml → UPSTREAM_PYPROJECT.toml.source.txt | vendor/hermes/provenance/ | 65c9bc65...a3269 | 65c9bc65...a3269 | 65c9bc65...a3269 | EXACT MATCH |
| package.json → UPSTREAM_PACKAGE.json.source.txt | vendor/hermes/provenance/ | 07b1b0c8...ad4ad1c0 | 07b1b0c8...ad4ad1c0 | 07b1b0c8...ad4ad1c0 | EXACT MATCH |

Full SHA-256 values:
- UPSTREAM_LICENSE.txt:                821556e6336796450ab852d375117b48a4887e71d255794fd6318d99982a5ab6
- UPSTREAM_PYPROJECT.toml.source.txt:  65c9bc6521fdeee289fa07fe10c82473f6228e46cca1e7ba9a380f5da6ca3269
- UPSTREAM_PACKAGE.json.source.txt:    07b1b0c8d196c93cc4876092907e7350cfc8b04db18ce34debb522aead4ad1c0

All three files match exactly: vendor copy = manifest claim = original Hermes clone at approved SHA.
This is the strongest possible provenance check — byte-level identity confirmed.

---

## 4. No Newer Upstream SHA

The provenance manifest states "Source branch at local clone: main" — this refers to the
local clone's branch name at the time of Sprint 2 (when the clone was made at that SHA).
The clone SHA is fixed at `33b1d144590a211100f42aa911fd7f91ba031507`, not pointing to a
live upstream main. No `git pull` or `git fetch` was performed on the clone during Sprint 4.

Evidence:
- Clone HEAD = `33b1d144590a211100f42aa911fd7f91ba031507` at validation time
- Sprint 4 PRE_IMPLEMENTATION_REPORT.md §4: "Source must not use moving main or a newer SHA."
- No network activity needed for Sprint 4 (static file import from local clone only)

---

## 5. Provenance Chain Summary

```
Origin: https://github.com/nousresearch/hermes-agent
         ↓
Sprint 2 clone at SHA 33b1d144590a211100f42aa911fd7f91ba031507
         ↓
Sprint 4 static file copy (3 upstream artifacts)
         ↓
vendor/hermes/provenance/*.source.txt (renamed; non-active)
vendor/hermes/UPSTREAM_LICENSE.txt
         ↓
SHA-256 hashed; recorded in HERMES_SOURCE_PROVENANCE_MANIFEST.md
         ↓
Antigravity independently verified: EXACT MATCH
```

Provenance chain is complete, documented, and independently verified at SHA-256 level.

---

## 6. Source SHA and Provenance Verdict

```
Approved SHA used:           CONFIRMED EXACT — 33b1d144590a211100f42aa911fd7f91ba031507
No newer upstream SHA:       CONFIRMED — clone not updated since Sprint 2
SHA-256 artifact match:      CONFIRMED EXACT for all 3 upstream artifacts
Three-way hash verification: vendor file = manifest claim = clone original — ALL MATCH
Provenance chain:            Complete and auditable

SOURCE SHA AND PROVENANCE VALIDATION: PASS — Highest confidence
```
