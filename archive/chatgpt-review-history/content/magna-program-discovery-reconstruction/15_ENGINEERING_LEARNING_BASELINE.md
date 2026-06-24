# 15 — Engineering Learning Baseline

> For a strong coder who is newer to professional Scrum/architecture/Git/environments/
> delivery/governance. For each major artifact: what it is (plain language),
> professional term, why companies need it, how it applies to Magna, who owns it, when
> it's created/updated, and how Vinay should review/approve it.

## 1. Project Charter
- **Plain:** the "what are we building and what are the rules" document.
- **Term:** Project Charter / Vision & Scope.
- **Why companies need it:** stops scope creep and arguments later by fixing identity,
  scope, and authority up front.
- **Magna:** `planning/MAGNA_ENSO_PROJECT_CHARTER.md` freezes Enso identity + governance.
- **Owner:** product owner (Vinay). **When:** at project start; amended only via a logged
  decision. **Review:** confirm the scope and non-scope still match your intent.

## 2. Decision Log (ADR / "Event Horizon")
- **Plain:** a permanent list of important choices and *why*, so nobody re-litigates them.
- **Term:** Architecture Decision Record (ADR) / Decision Log.
- **Why:** future-you (and other workers) need the reasoning, not just the outcome.
- **Magna:** `trace/DECISION_LOG.md` (EH-0001…0015). Rule: **never delete; supersede.**
- **Owner:** you accept; workers propose. **When:** whenever a material/irreversible
  choice is made. **Review:** check each PROPOSED entry; mark ACCEPTED yourself.

## 3. Risk Register
- **Plain:** a list of things that could go wrong + how likely/bad + what we'll do.
- **Term:** Risk Register. **Why:** makes risk visible and owned instead of forgotten.
- **Magna:** `trace/RISK_REGISTER.md` (R-01…R-15; R-06 "no runtime enforcement" is OPEN).
- **Owner:** PO + tech lead. **When:** continuously. **Review:** confirm OPEN risks are
  acceptable before accepting a sprint.

## 4. Backlog & Feature Tracker
- **Plain:** the master to-do list of features, ordered, with "done means…" criteria.
- **Term:** Product Backlog; items have Acceptance Criteria + Definition of Done.
- **Why:** turns a vision into small, checkable pieces.
- **Magna:** `trace/FEATURE_TRACKER.md` (ENSO-F-…); honest-status rule = DoD.
- **Owner:** PO orders it; team estimates. **When:** living. **Review:** ensure "DONE"
  always has evidence (a Light Curve) — never accept "DONE" on a promise.

## 5. Sprint
- **Plain:** a short, fixed chunk of work with one goal, ending in something reviewable.
- **Term:** Sprint (Scrum). **Why:** small batches = less risk, faster feedback.
- **Magna:** `MAGNA_ENSO_SPRINT_PLAN.md` (Sprints 0–15). **Owner:** team delivers; PO
  accepts. **When:** sequential. **Review:** use the per-sprint Acceptance Criteria as
  your checklist; accept only when evidence matches.

## 6. Definition of Ready / Definition of Done
- **Plain:** DoR = "is this clear enough to start?"; DoD = "is this truly finished?"
- **Why:** prevents starting vague work and calling half-work "done."
- **Magna:** Sprint-4 readiness gates (DoR); honest-status + human-approved Light Curve
  (DoD). **Owner:** team + PO agree. **Review:** refuse to start/accept if these aren't met.

## 7. Evidence Package ("Light Curve") & Review Package
- **Plain:** the proof a change does what it claims — diffs, test logs, validation notes.
- **Term:** Evidence/Review Package; "verifiable handoff."
- **Why:** lets a human approve work *offline* without trusting a chat transcript.
- **Magna:** `trace/evidence/*_LIGHT_CURVE.md` + `ChatGPTReview/sprint-N-*`. **Owner:**
  the worker who did the work. **When:** at task close. **Review:** read it before you
  approve; if it lacks real test logs for code, it's not done.

## 8. Git: branches, commits, tags, remotes
- **Plain:** Git is a time machine + parallel-universe tool for code.
  - **Branch** = a parallel line of work (e.g. `sprint/05-policy-engine`).
  - **Commit** = a saved checkpoint with a message.
  - **Tag** = a named milestone (e.g. `v1.0-enso`).
  - **Remote** = the cloud copy (GitHub). **Untracked** = files Git isn't saving yet.
- **Why:** safe experimentation, history, collaboration, releases.
- **Magna gotcha now:** Enso's policy code is **untracked** — it exists on disk but Git
  isn't saving it, and the status docs say it doesn't exist (C-6). Lesson: *uncommitted
  work is invisible to governance.* **Review:** before accepting a sprint, run
  `git status` yourself and confirm code is committed and matches the evidence.

## 9. Environments (local/dev/test/staging/prod)
- **Plain:** separate copies of the app for building, testing, and real users.
- **Why:** you don't test on real users; you promote through stages.
- **Magna:** only **local** exists everywhere. That's fine for now (single-user,
  local-first by design) but means "production-confirmed" is impossible to claim yet.

## 10. Policy / Permission / Approval Gate
- **Plain:** a checkpoint that says "this action is allowed / denied / needs your OK."
- **Term:** authorization/policy engine; default-deny; fail-closed.
- **Why:** the safety core — nothing risky runs without a rule + (often) a human yes.
- **Magna:** Enso `policy/gate.py` (default-deny, fail-closed, audit-logged) and
  command-center ATM-01 + risk engine. **Review:** the key property to verify is
  "**no path bypasses the gate**" — ask for the negative test that proves it.

## 11. Traceability (engineering vs runtime)
- **Plain:** being able to answer "why was this built?" and "what did it do at run time?"
- **Why:** audits, debugging, trust.
- **Magna:** TRACE engineering plane (Light Curves/decisions) vs runtime plane (audit
  log/replay). Keep them separate (a built record ≠ a behaviour record).

## 12. How Vinay should review *anything* a worker hands back
1. Read the **acceptance criteria** first. 2. Open the **evidence** and check it's *real*
(git diff + test output), not a summary. 3. Run **`git status`/`git log`** to confirm the
work is committed where it claims. 4. Check the **Decision Log + Risk Register** updated.
5. Only then mark it **ACCEPTED** — you are the final authority; workers never self-accept.
