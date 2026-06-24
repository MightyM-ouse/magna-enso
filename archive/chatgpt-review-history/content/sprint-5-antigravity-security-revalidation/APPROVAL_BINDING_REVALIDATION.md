# APPROVAL_BINDING_REVALIDATION.md
# Magna Enso — Sprint 5 Exact Approval Binding Targeted Security Revalidation

## 1. Validation Findings: Gap 2 — Exact Approval Binding

The corrected approval package specifies a robust approval fingerprint binding process that ensures each approval token is tied to one exact invocation.

### Key Points Confirmed:
- **Comprehensive Binding Fields:** The fingerprint binds the following fields:
  - `approval_id` + `nonce` (unguessable single-use nonce)
  - `capability_id`
  - `invocation_path` (explicitly checking how it reached the gate)
  - `proposed_action`
  - `parameters` (complete, normalized)
  - `affected_resources`
  - `caller_context_id`
  - `policy_version` or `policy_record_hash`
  - `expiry` (monotonic-based expiry time)
- **Deterministic Hashing:** The fingerprint is computed as a SHA-256 hash over a deterministic **canonical JSON** representation (sorted keys, no extraneous whitespace, standard UTF-8 encoding).
- **Atomic Serialized Comparison:** Complete fingerprint comparison happens **inside the serialized critical section** before marking the approval consumed.
- **Fail-closed Verification:** Any missing field, parameter mismatch, mutation, duplicate, expired, or replayed approval results in a `DENY`.
- **Concurrency Security:** Locking rules guarantee that only one concurrent consumer can mark an approval consumed. Subsequent consumers read it as consumed and return `DENY`.
- **Sensitive Data Redaction:** Raw sensitive payload values (like credentials or private file data) are redacted or hashed in audit logs to protect data privacy. Crucially, the fingerprint is computed over the complete *unredacted* values beforehand, ensuring the cryptographic binding remains fully intact.

---

## 2. Adversarial Fingerprint Challenges

We challenge the fingerprint computation with common signature-bypass techniques:

### A. Ambiguous Parameter Normalization and Collisions
- **Threat:** If parameters are normalized poorly (e.g. converting a dictionary to a string using Python's default `str()`), different parameter structures could produce identical string representations, leading to hash collisions.
- **Analysis:** The specification mandates **canonical JSON serialization** (e.g., standardizing on sorting keys and using standard separators like `json.dumps(obj, sort_keys=True, separators=(',', ':'))`). This guarantees a unique, bijective byte representation for any given data structure.

### B. Collection Reordering (Lists vs. Dicts)
- **Threat:** If parameters contain lists or sets, their order might vary between the request and the execution, causing a false rejection or enabling bypasses if order matters.
- **Analysis:** JSON objects (dictionaries) have keys sorted deterministically during canonicalization. For lists, order is preserved exactly as supplied. If list elements represent unordered items, they must be normalized (e.g. sorted if appropriate, or treated as elements of a deterministic list) to prevent mismatch.

### C. Path Normalization Bypasses
- **Threat:** If `invocation_path` or `affected_resources` contains relative segments (`../`), Unicode normalization differences, or trailing slashes, an agent could bypass matching constraints (e.g., requesting `/safe/path` and executing `/safe/path/../../unsafe/path`).
- **Analysis:** Paths and resource identifiers must be fully resolved and normalized (e.g. resolving symlinks and relative directories to absolute paths via POSIX-equivalent path resolution) before the fingerprint is computed. Any relative or un-normalized input in resource targets must fail-closed and return `DENY`.

### D. Encoding Differences (UTF-8 vs ASCII / Unicode Normalization)
- **Threat:** Different Unicode forms (NFD vs NFC) for the same string yield different byte sequences and different SHA-256 hashes.
- **Analysis:** The engine must enforce Unicode normalization (e.g. normalizing to NFC via Python standard library `unicodedata.normalize('NFC', text)`) during canonicalization, ensuring identical strings always produce identical fingerprints.

### E. Argument Substitution
- **Threat:** A capability execution might accept default arguments that are omitted from the request parameter list but populated at execution time, modifying the action.
- **Analysis:** The specification checks the *complete* normalized parameters. If a parameter is filled at runtime, it must be present in the fingerprint; any discrepancy between requested parameters and actual invocation parameters results in a fingerprint mismatch and a `DENY`.
