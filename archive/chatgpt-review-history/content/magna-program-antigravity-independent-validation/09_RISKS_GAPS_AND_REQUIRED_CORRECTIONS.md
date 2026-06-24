# 09 — Risks, Gaps, and Required Corrections

This report consolidates the outstanding security risks, code defects, and documentation gaps identified during independent validation, along with the required prompt corrections.

## 1. Critical Security Gaps

### A. Relative Path Directory Traversal (Command Center)
- *Risk:* Passing relative paths with parent directory traversal segments (e.g., `../../../../etc/passwd`) bypasses the `_assess_path` workspace zone classification, labeling the request as `APPROVED` with no approval required.
- *Required Correction:* Update `_assess_path` to resolve paths to their absolute canonical form (e.g. using `os.path.abspath` or `Path.resolve()`) before comparing them against workspace roots.

### B. Regex Bypasses (Command Center)
- *Risk:* Simple string splits or synonyms (e.g., `unlink` instead of `delete`, `cat .e'nv'` instead of `cat .env`) bypass prompt filters.
- *Required Correction:* Move away from parsing raw prompt strings; enforce policy against structured, typed parameters as specified in Enso's schemas.

### C. Loopback Trust Assumption (Command Center)
- *Risk:* Untrusted processes on the same host can access loopback and gain administrative control without a token check.
- *Required Correction:* Harden the loopback dependency to require a local paired token or process verification.

### D. Same-User Audit Tampering (Enso)
- *Risk:* A local process running as the same OS user can rewrite the SHA-256 hash-chained JSONL log, erasing tampering evidence.
- *Required Correction:* Re-verify the hash-chain against an independent off-host log or lock the log using OS-level permissions that the app user cannot write to.

---

## 2. Functional Gaps and Code Defects

### A. Pytest Import Shadowing (Enso)
- *Defect:* The file [tests/policy/__init__.py](file://<MAGNA_LOCAL_ROOT>/magna-enso/tests/policy/__init__.py) shadows the production `policy/` package, breaking the standard `pytest` collection path.
- *Required Correction:* Remove `tests/policy/__init__.py` or configure pytest to prioritize the root directory for production module lookup.

### B. Rollup Compile Block (TRACE UI)
- *Defect:* Frontend build fails locally due to a missing platform-specific Rollup package (`@rollup/rollup-darwin-arm64`).
- *Required Correction:* Run `npm install --save-optional @rollup/rollup-darwin-arm64` in the TRACE UI environment.

### C. CSF-01 Capability Registry Drift
- *Defect:* The file `capability_registry.py` marks governed Ollama execution as disabled, while the service implements it.
- *Required Correction:* Align registry metadata with current runtime code.

### D. Lack of BRS-01 Acceptance Record
- *Defect:* BRS-01 has green test coverage but lacks a signed human acceptance freeze.
- *Required Correction:* Vinay must explicitly accept and freeze BRS-01.
