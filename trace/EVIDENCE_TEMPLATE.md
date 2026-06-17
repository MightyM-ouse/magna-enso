# Light Curve — Evidence Package Template

> A Light Curve is durable, reviewable proof of work. Every meaningful task writes one into
> `trace/evidence/`. Naming: `trace/evidence/ENSO-NNNN_LIGHT_CURVE.md`.

```md
# Light Curve — ENSO-NNNN
Task ID: ENSO-NNNN
Mode History: <e.g. investigation → execution → review>
Evidence Level: <Light | Standard | Full>
Date: YYYY-MM-DD
Worker(s): <role/worker>

Goal:

Context Route Used:           # which CELESTIAL_INDEX area(s)
Files Inspected:
Files Changed:                # "none" for non-code tasks
Commands Run:                 # "none" if not applicable
Validation Results:           # Spectrometer checklist results; real, not estimated

Findings:
Risks:                        # link R-<id> where relevant
Decisions Made:               # link EH-<id> where relevant
Final Status:                 # in_review | needs_changes | approved (human)
Next Steps:

Human Approval:               # name + date, or "pending"
```

## Honest data contract
- What changed / shipped must be **real**. Any token/cost/effort numbers are **approximate** and labeled so.
- Governance evidence (no policy bypass, no public listener, no silent memory write, etc.) must be shown,
  not asserted — include the test/observation that demonstrates it.

## Evidence by mode
- **Investigation:** symptom, hypotheses, evidence for/against, root-cause confidence, recommended fix.
- **Execution:** implementation summary, files changed, tests run, risks.
- **Review:** findings, risk level, approval recommendation.
