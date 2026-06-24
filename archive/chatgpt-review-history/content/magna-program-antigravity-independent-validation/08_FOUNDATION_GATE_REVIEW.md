# 08 — Foundation Gate Review

This report documents an architectural audit of the proposed foundation gates in the Codex evidence-completion package, evaluating their completeness, practicality, and alignment with project constraints.

## 1. Practicality and Bureaucracy Assessment

For a single-user, local-first desktop application, several of the proposed gates (specifically under Gates 5 and 6) are excessively bureaucratic and reflect enterprise cloud service biases:
- **Disaster Recovery (DR) and Rollback Rehearsal:** A single-user desktop application running locally against a SQLite database does not require a formal DR site or complex rollback rehearsal procedures. Standard file backups (e.g. database copying or git commits) are sufficient.
- **Performance Budget and Responsive Breakpoint Matrix:** While general UI performance is important to prevent lags, a formal "performance budget" and multi-device responsive layout matrix are excessive for a local macOS Electron/React app.

**Recommendation:** Simplify Gates 5 (UX) and 6 (Environment) to focus exclusively on local installer creation, local data backup, and basic UI responsiveness on desktop viewports.

---

## 2. Alignment with Core Rules

### A. Prevention of Premature Autonomy and Hermes Activation
- **SGN-01 Block (Gate 2):** SGN-01 represents broad capability intelligence and autonomous execution. Keeping this block explicit prevents any worker from self-activating capabilities without a human decision.
- **Hermes Adoption Control (Gate 9):** Ensures that the inert upstream Hermes vendor baseline cannot be activated or imported without explicit human-approved policy constraints.

### B. Prevention of Self-Certification
- **TRACE Dual-Plane Gate (Gate 4):** This gate enforces the crucial rule that **Magna must not certify its own output**. The runtime plane (Magna) emits facts and events, but the verification of those events against expectations must be conducted by an independent identity (or external process) in the engineering plane. This prevents a compromised runtime from fabricating its own verification status.

### C. Separate Repository Architecture
- **Authority Gate (Gate 1):** Codifies stage naming (Kenosha) and enforces that Enso, Satori, Kenosha, and SGN remain in separate repositories. This prevents repository pollution and preserves clean historical codebases.

---

## 3. Missing Gates (Recommended Additions)

We recommend adding two critical gates to the list before authorizing repository creation:

1. **Security Vulnerability Closeout Gate:**
   - *Rule:* The directory-traversal vulnerability (relative path bypass) and the regex bypass vulnerabilities discovered in the Command Center policy engine must be resolved. Automated regression tests must verify that relative paths (e.g. `../../etc/passwd`) are canonicalized and rejected at the route level.
2. **Test Package Isolation Gate:**
   - *Rule:* The project must enforce strict package layout constraints (avoiding `__init__.py` files in test roots) to prevent namespace shadowing defects (such as the Enso pytest collection failure).
