# THREAT_AND_BYPASS_MODEL_VALIDATION.md
# Magna Enso — Sprint 5 Threat Model and Bypass Analysis Validation

## 1. Threat Coverage Assessment (T-1 through T-12)

The approval package provides a comprehensive, structured threat model in `THREAT_MODEL_AND_BYPASS_ANALYSIS.md`. Unlike naive designs that claim "no bypass" universally, this model categorizes each threat class and defines realistic, verified mitigations.

### Threat Class Categorization:

| Class | Threat | Validation Check Type | Sprint 5 Posture |
|---|---|---|---|
| **T-1** | Uncovered Path | **Deferred (Real)** + Harness testable | Harness tests call around the mock gate to prove denial. Real mainline bypass testing is **deferred** since no runtime exists. |
| **T-2** | Missing Policy | **Executable Deny-Test** | Unknown capability ⇒ DENY. |
| **T-3** | Input-Driven Escalation | **Executable Deny-Test** | Request payload privilege assertions are ignored by evaluator. |
| **T-4** | Self-Approval | **Executable (Test-Provider)** | Programmatic stubs return simulated decisions in tests; prod is absent ⇒ DENY. |
| **T-5** | Config Bypass | **Executable Deny-Test** | Config flags cannot alter `approval_required` capabilities to auto-run. |
| **T-6** | Dynamic Registration | **Absence Assertion** | No dynamic loaders, plugin registries, or registration paths exist. |
| **T-7** | Fail-Open on Error | **Executable Deny-Test** | Evaluator/store/log errors ⇒ DENY. |
| **T-8** | TOCTOU / Race | **Executable (Partial)** | Serialized locks prevent concurrent/double-use approval consumption. |
| **T-9** | Approval Replay | **Executable Deny-Test** | Expired/consumed approvals ⇒ DENY. |
| **T-10**| Log Tampering | **Split (Review + Executable)** | Every outcome logged (executable); protection against root editing is **not** supported (review). |
| **T-11**| Privilege Delegation | **Absence Assertion** | Subagent delegation surfaces are absent in Sprint 5. |
| **T-12**| Vendor Metadata Trust| **Review Check** | Evaluator decides on trusted JSON store, not untrusted upstream YAML metadata. |

## 2. Adversarial Bypass Challenges

### Missing-Policy and Uncovered-Path Behavior:
- **Challenge:** What happens if an agent discovers a capability that was omitted from the policy JSON?
- **Analysis:** Under default-deny, the lookup failure maps directly to `DENY`. 
- **Challenge:** What if the invocation path is malformed or not mapped?
- **Analysis:** The path-covered check ensures that only explicitly listed paths are allowed. An unmapped path resolves to `DENY`.

### Future Entry-Point Bypass:
- **Challenge:** If new capability surfaces (like memory writes or system calls) are added in Sprint 8+, can they bypass this gate?
- **Analysis:** Yes, because the harness cannot force future developers to route their calls through the gate. The gate is not a magic shield.
- **Mitigation:** The threat model honestly states this limitation. **R-06 stays OPEN** after Sprint 5. End-to-end validation must recur as each new capability surface is integrated.

### Payload and Config Escalation:
- **Challenge:** Can prompt injection or malicious JSON inputs modify policy state at runtime?
- **Analysis:** No. The policy store is read-only at evaluation time and human-curated. The evaluator only accepts standard invocation context parameters, completely ignoring any request-supplied overrides.
