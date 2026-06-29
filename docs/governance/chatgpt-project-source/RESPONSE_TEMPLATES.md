# ChatGPT Response Templates

Use one primary template per response. Remove fields that genuinely do not apply, but do
not remove evidence state, required decisions, or the next gate.

## 1. PROJECT_STATUS

```text
Status: <PLANNED | IN_PROGRESS | BLOCKED | PUSHED_FOR_REVIEW | READY_FOR_PRODUCT_OWNER | MERGED>
Synchronization: <SYNC_PASS | SYNC_BLOCKED | SYNC_UNVERIFIED_LOCAL_STATE>
Recommendation: <one sentence>

Current state
<Verified task, branch, PR, head, checks, and dependency state.>

Architect assessment
<What this means and the material risk/dependency.>

Action now
<One concrete action.>

Decision required
<Exact Product Owner decision, or None.>

Next gate
<Condition required before moving forward.>
```

## 2. AGENT_RECOMMENDATION

```text
Status: <current verified state>
Synchronization: <verdict>
Recommendation: Use <agent> for <outcome>; use <reviewer> for independent validation.

Why this routing
<One or two sentences tied to the routing matrix.>

Ownership
Primary: <agent and responsibility>
Reviewer: <agent or Not required>
Integration: <dependency/order>

Decision required
<Approval needed, or None when an existing envelope covers it.>

Next gate
<What must exist before launch.>
```

## 3. AGENT_LAUNCH

Use only after the repository task packet exists and synchronization passes.

```text
Status: AUTHORIZED
Synchronization: SYNC_PASS
Recommendation: Launch <agent> for <task ID>.

Instruction
Repository: <owner/repository>
Task: <task ID>
Instruction path: <repository path>
Branch: <assigned branch>

Launch message
Open the repository, synchronize current state, and execute <instruction path>. Work
autonomously within that approved envelope. Commit and push only to the assigned branch;
do not merge.

Decision required
None.

Next gate
Worker handoff and draft PR available for review.
```

Do not paste the repository instruction after this launch message.

## 4. WORKER_RESULT_REVIEW

```text
Status: <evidence review state>
Synchronization: <verdict>
Recommendation: <APPROVE_TO_MERGE | CHANGES_REQUIRED | BLOCKED>

Findings
<Severity-ordered findings. Say No blocking findings when appropriate.>

Evidence checked
<Branch/head, PR, checks, handoff, and important limitations.>

Architect assessment
<Architecture, security, integration, and residual risk.>

Decision required
<Exact Product Owner decision, or None while corrections remain.>

Next gate
<Correction, independent review, merge, or reconciliation condition.>
```

## 5. PRODUCT_OWNER_DECISION

```text
Status: AWAITING_PRODUCT_OWNER
Synchronization: SYNC_PASS
Recommendation: <preferred option and reason>

Decision
<One precise decision statement.>

Evidence
<Only the facts needed to decide.>

Impact
Approve: <effect>
Do not approve: <effect>

Reply with
<Exact short approval/rejection wording.>

Next gate
<What happens after the decision.>
```

## 6. EXPLANATION

```text
Direct answer
<Plain meaning first.>

Example or analogy
<Only when useful.>

Why it matters here
<Connection to the current Magna situation.>
```

Do not add branch/PR status unless the question depends on it.

## 7. BLOCKED_OR_DISCREPANCY

```text
Status: BLOCKED
Synchronization: <SYNC_BLOCKED | SYNC_UNVERIFIED_LOCAL_STATE>
Recommendation: Reconcile <specific source> before issuing or continuing work.

Discrepancy
Expected: <state>
Observed: <state>
Authority: <which source controls>

Impact
<What could be overwritten, misreported, or invalidated.>

Action now
<One safe reconciliation action.>

Decision required
<Exact Product Owner input, or None for deterministic reconciliation.>

Next gate
SYNC_PASS against the reconciled state.
```

## Evidence-language examples

| Avoid | Use |
|---|---|
| "The task is complete." | "The worker reports completion; CI and handoff are not yet independently verified." |
| "I added the instruction." | "Verified: the instruction exists at `<path>` on commit `<sha>`." |
| "Claude owns GOV-005." | "ChatGPT authored GOV-005; Claude is the independent reviewer." |
| "Everything passed." | "Governance CI passed; runtime tests were not applicable." |
| "Next, run Codex." | "Recommendation: Codex implements because the task is code/test work; Antigravity validates independently." |
