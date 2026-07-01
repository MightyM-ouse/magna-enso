# HERMES-TECH-001 — Local Evidence Amendment

Status: AUTHORIZED_AMENDMENT  
Parent task: `HERMES-TECH-001`  
Issue: #36  
Prepared by: ChatGPT/System Architect  
Approved by: Product Owner request  

---

## Purpose

This amendment extends the Claude review scope for `HERMES-TECH-001`.

Claude must inspect both GitHub evidence and the Product Owner-approved local Magna workspace because historical Hermes capability assessment material may exist locally and may not yet have been curated into GitHub.

---

## Local workspace scope

Claude must ask the local shell for the active project location and confirm which Magna checkout is being used before drawing conclusions.

The Product Owner has indicated that the required local access is available in the Magna folder.

---

## Required local checks

Claude should run or equivalent-check:

```text
pwd
git status --short --branch
git branch --show-current
git log --oneline --decorate -10
```

Claude should then search local files for Hermes capability assessment evidence, including:

```text
Hermes
hermes-agent
capability assessment
adopt
adapt
wrap
defer
self-improvement
memory
skills
terminal
Telegram
WhatsApp
scheduler
MCP
delegation
```

---

## Evidence handling rules

Claude must separate evidence into:

```text
ACCEPTED_GITHUB_EVIDENCE
LOCAL_ONLY_UNVERIFIED_UNTIL_COMMITTED
STALE_OR_NONCANONICAL_EVIDENCE
RECOMMENDED_FOR_CURATED_IMPORT
```

Claude must not treat local-only material as accepted `main` state.

Claude must not bulk-copy raw local folders into GitHub. If local evidence is useful, Claude should recommend a curated destination such as:

```text
trace/reviews/
trace/evidence/
trace/assessments/
docs/architecture/
docs/technical-specifications/
```

---

## Required report update

Claude's review report must include a section named:

```text
Local Magna Workspace Findings
```

That section must list:

- local location checked;
- git branch and status summary;
- local-only evidence found;
- whether each item should be curated into GitHub;
- recommended destination path;
- whether the evidence changes any capability decision.

---

## Boundaries

This amendment does not authorize runtime code changes, Hermes activation, final sprint planning, story finalization, or merge. It only expands evidence discovery for the technical assessment review.
