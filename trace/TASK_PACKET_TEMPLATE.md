# Constellation — Task Packet Template

> A Constellation is a scoped, single-purpose work package. Copy this template per task.
> Naming: `trace/tasks/ENSO-NNNN.md` (create `trace/tasks/` when the first real task is opened).

```md
# Constellation — ENSO-NNNN
Task ID: ENSO-NNNN
Sprint: <n>
Mode: <discovery | investigation | execution | review | mixed>
Goal: <one clear sentence>

Worker (role): <e.g. Codex / builder>   # see trace/ROLE_REGISTRY.yaml
Reviewer: <e.g. Antigravity + Human owner>

Context Route: <area id from trace/CELESTIAL_INDEX.json>
Allowed Scope: <explicit files/globs the task may touch>
Forbidden Scope: <anything explicitly off-limits>

Required Checks: <Spectrometer items from trace/VALIDATION_CHECKLIST.md>
Evidence Expectation: Light Curve (<Light | Standard | Full>) + review-package if code changes

Linked Feature: ENSO-F-<id>          # trace/FEATURE_TRACKER.md
Linked Risks: R-<id>, ...            # trace/RISK_REGISTER.md
Linked Decisions: EH-<id>, ...       # trace/DECISION_LOG.md

Human Approval Required: <yes/no — yes for any commit, push, or material/irreversible action>

Mode History:
  - mode: <...>
    status: <pending | in_progress | completed>
    output: <...>
```

## Rules
- One purpose per Constellation. Reference a context route — do not request full-repo scans.
- Name the worker, mode, and evidence level up front.
- Material/irreversible actions always set `Human Approval Required: yes`.
- A task that switches modes keeps the **same Task ID** and appends to `Mode History`.
