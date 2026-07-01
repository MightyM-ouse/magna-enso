# HERMES-TECH-001 — Claude Review and Correction Instruction

Status: READY_FOR_CLAUDE_REVIEW  
Parent task: `HERMES-TECH-001`  
Issue: #36  
Prepared by: ChatGPT/System Architect  
Review target branch: `chatgpt/HERMES-TECH-001-assessment`  
Expected Claude branch: `claude/HERMES-TECH-001-review`  

---

## 1. Role

Claude acts as independent architecture and technical-assessment reviewer.

Claude must verify whether the assessment seed correctly captures prior Hermes capability assessment evidence, current Magna Enso governance constraints, and Epic 1 readiness for `Magna version enso`.

---

## 2. Required startup

Before providing conclusions, Claude must read:

- `AGENTS.md`
- `CLAUDE.md`
- `trace/STAR_MAP.md`
- `trace/ACTIVE_WORK_REGISTRY.yaml`
- `trace/CELESTIAL_INDEX.json`
- `trace/tasks/HERMES-TECH-001.md`
- `trace/assessments/MAGNA_VERSION_ENSO_TECHNICAL_ASSESSMENT_SEED.md`
- `trace/planning/MAGNA_HERMES_RUNTIME_ADOPTION_BRIEF.md`
- `trace/planning/MAGNA_VERSION_ENSO_TECHNICAL_ASSESSMENT_SCOPE.md`

Claude must then search routed repository evidence for prior Hermes capability assessment, including but not limited to:

- `vendor/hermes/`
- `trace/evidence/`
- `trace/reviews/`
- `trace/tasks/`
- `docs/architecture/`
- `docs/technical-specifications/`
- governed archive material when routed by `CELESTIAL_INDEX`

Claude must not rely on chat memory as evidence.

---

## 3. Review objectives

Claude must check and correct the following:

1. Whether a prior detailed Hermes capability assessment exists in the repository.
2. Whether the seed assessment correctly identifies which details are already available.
3. Whether current capability classifications are too aggressive, too conservative, or missing.
4. Whether the assessment preserves Magna identity, TRACE, Product Owner authority, and local-first control.
5. Whether the proposed Epic 1 readiness scope is realistic.
6. Whether any Hermes capability should be deferred to protect first-version delivery.
7. Whether PR #33 Magna identity/logo dependency is correctly considered.
8. Whether the next workflow after product user stories is correct: story correctness review, final approved/design-ready stories, then detailed sprint planning.

---

## 4. Required corrections format

Claude must create a review report at:

```text
trace/reviews/HERMES-TECH-001-CLAUDE-REVIEW.md
```

The report must contain:

- `SYNC` verdict.
- Evidence files reviewed.
- Findings table.
- Corrections to capability classification.
- Features that must be adopted for Epic 1.
- Features that can be deferred.
- Risks and unresolved decisions.
- Recommended edits to the seed assessment.
- Final verdict: `ACCEPT`, `ACCEPT_WITH_CORRECTIONS`, `CHANGES_REQUIRED`, or `BLOCKED`.

Claude may also propose a handoff file:

```text
trace/evidence/HERMES-TECH-001-CLAUDE-HANDOFF.md
trace/evidence/HERMES-TECH-001-CLAUDE-HANDOFF.json
```

---

## 5. Boundaries

Claude must not:

- Activate Hermes.
- Modify runtime code.
- Modify product user stories unless explicitly assigned later.
- Create final sprint plan.
- Mark any story final/design-ready.
- Merge, close, or self-approve.
- Assume Hermes profiles are security sandboxes.
- Treat archived/noncanonical evidence as current without route and rationale.

---

## 6. Expected outcome

After Claude review, ChatGPT/System Architect and Product Owner should know:

- What prior Hermes assessment evidence exists.
- What corrections are required.
- Which features must be adopted for Magna version enso Epic 1.
- Which features should be deferred.
- What technical findings must be included before final approved/design-ready user stories and sprint planning.
