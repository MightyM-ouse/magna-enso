# AUDIT_FILE_SECURITY_REVALIDATION.md
# Magna Enso — Sprint 5 Audit File Security Targeted Security Revalidation

## 1. Validation Findings: Gap 3 — Audit File Security

The corrected approval package establishes strict security constraints for the audit file in `FAILURE_MODES_AND_FAIL_CLOSED_BEHAVIOR.md` §3d.

### Key Points Confirmed:
- **Owner-only `0600` permissions:** The file must reside under mode `0600` (read/write by owner only). Permissive modes are rejected.
- **Atomically Restrictive Creation:** Creation uses exclusive atomic creation flag combinations (`O_CREAT | O_EXCL` with mode `0o600` via stdlib `os.open`). This ensures there is **no permissive intermediate state** (such as creating the file and then running `chmod`), avoiding a window of exposure.
- **Owner Verification:** The UID of the audit file owner is explicitly verified against the UID of the running process. If they differ, the engine fails initialization.
- **Regular-File and Symlink Checks:** The path is verified to be a regular file. It refuses symlinks (using `O_NOFOLLOW` flag during file open operations).
- **Continuous Pre-Use Verification:** Security properties (owner, permissions, regular file type) are checked **at startup AND before every write**, preventing time-of-check to time-of-use (TOCTOU) file modification attacks.
- **Fail-Closed on Unsafe Platforms:** On environments without full POSIX permission schemas (such as Windows), the engine must apply the closest secure ACL equivalent and document the gap. If the security properties cannot be established, the system must fail-closed and return `DENY` for all capability requests.
- **Codex Tests:** The Codex prompt requires building tests specifically asserting that insecure permissions, wrong owners, symlink paths, or non-regular paths fail-closed and result in `DENY-all`.

---

## 2. Adversarial File Security Challenges

We challenge the audit log file boundaries with filesystem-level attacks:

### A. Symlink Swapping and Path Replacement (TOCTOU)
- **Threat:** An attacker replaces the log file path with a symlink targeting a sensitive system file (e.g. `/etc/passwd` or system files) in the split second between the check and the write.
- **Analysis:** By combining `O_NOFOLLOW` during the atomic open and verifying the file descriptor metadata (using `os.fstat(fd)` rather than `os.stat(path)` after opening), path-swapping attacks are completely mitigated. The file descriptor remains bound to the target checked during the open operation.

### B. Permission Changes after Startup
- **Threat:** A local process changes the file permissions to `0666` while the engine is running.
- **Analysis:** Since the engine re-verifies ownership and permission bits on the file descriptor before *every* write operation (pre-use verification), runtime permission changes are immediately detected, halting further allowances.

### C. Lock Failure and Concurrency
- **Threat:** If the local lock file is deleted or locking fails, concurrent writer threads could overwrite the audit tail or interleave log lines, corrupting the chain.
- **Analysis:** The design requires that any locking or serialization failure is treated as a hard failure. The gate returns `DENY` immediately without writing or executing.

### D. File Replacement via Directory Write Access
- **Threat:** If the parent directory `<CHATGPT_REVIEW_SOURCE>/` has weak permissions, an attacker could delete the audit file and create a new one under their ownership.
- **Analysis:** Owner UID verification on startup and before each write prevents the engine from writing to a file owned by another user.
