AGENT_OUTPUT_REVIEW_TEMPLATE.md

Magna / Enso / HELIX — Agent Output Review Response Template

1. Purpose

This file defines the standard response format ChatGPT must use when the user attaches output from Claude, Codex, Antigravity, Hermes Agent, Grok, or any other worker and asks for review.

The goal is to produce a consistent, comparable, sprint-aware review showing:

* what was requested
* what was actually implemented
* what was validated
* what is incomplete
* what functions/files were added or changed
* current sprint completion
* current module completion
* implementation rating
* required corrections
* ready-to-copy follow-up prompt

This template is for ChatGPT project-level orchestration review, not for runtime implementation.

⸻

2. Trigger Phrase

Use this template when the user says any of the following:

Use the agent output review template.
Review this agent output using the Magna review template.
Refer to AGENT_OUTPUT_REVIEW_TEMPLATE.md and review.
Review the attached output and update source data.
Compare requested vs implemented.

⸻

3. Required Inputs

Before reviewing, ChatGPT should look for:

1. User’s original request or prompt to the agent.
2. Agent output / final summary.
3. Changed files list.
4. Validation results.
5. Commit hash, if any.
6. Sprint/module name.
7. Existing source-data file, if provided:
    * AGENT_OUTPUT_REVIEW_SOURCE_DATA.md
8. Any existing roadmap, sprint plan, feature tracker, decision log, or risk register provided in the chat.

If any input is missing, ChatGPT must continue with available evidence and clearly mark unknowns as:

Not provided
Unverified
Cannot confirm from attached output

Do not invent implementation details.

⸻

STANDARD RESPONSE FORMAT

Every response must use the following structure.

⸻

1. Executive Review Verdict

Provide a short overall verdict.

Format:

Verdict: Approved / Approved with corrections / Needs revision / Blocked / Rejected
Confidence: High / Medium / Low
Overall Rating: X.X / 10
Sprint Impact: Positive / Neutral / Risky / Blocking
Module Impact: Positive / Partial / Unclear / Negative

Then provide 3–5 lines explaining the verdict.

⸻

2. Requested vs Implemented Comparison

Create a table comparing the request against the actual output.

#	Requested Item	Implemented / Reported	Evidence From Output	Status	Rating	Gap / Comment
1	What was requested	What agent says was done	File/report/validation reference	Done / Partial / Missing / Unverified / Drift	0–5	Short comment

Status meanings:

Status	Meaning
Done	Clear evidence shows it was completed
Partial	Some work done, but incomplete
Missing	Requested item not addressed
Unverified	Claimed but no evidence provided
Drift	Implementation went outside or away from request

Rating scale:

Score	Meaning
5	Fully implemented with evidence
4	Implemented with minor gaps
3	Partially implemented
2	Weak / unclear implementation
1	Mostly missing
0	Not done or harmful drift

⸻

3. Sprint Completion Status

Identify the sprint and calculate/reason about completion.

Format:

Sprint: <Sprint name / number>
Sprint Goal: <goal>
Sprint Status: Not started / In progress / Review / Accepted / Blocked
Estimated Sprint Completion: XX%
Confidence: High / Medium / Low

Then provide a table:

Sprint Deliverable	Expected	Actual	Status	Completion Weight	Notes
Deliverable 1	Expected output	Actual output	Done / Partial / Missing	XX%	Notes

Rules:

* If feature weights are not provided, assume equal weight.
* If validation is missing, do not mark sprint as 100%.
* If implementation exists but no tests are provided, cap completion at 80% unless the task was documentation-only.
* If human approval is pending, mark sprint as Review, not Accepted.

⸻

4. Module Completion Status

Track the broader module or feature area.

Format:

Module: <Module / feature area>
Module Goal: <goal>
Previous Completion: XX% / Unknown
New Estimated Completion: XX%
Delta: +X% / -X% / No change
Confidence: High / Medium / Low

Then provide:

Module Capability	Already Implemented	Newly Added	Remaining	Status
Capability 1	Yes/No/Unknown	Yes/No	What remains	Done/Partial/Missing

Rules:

* Module completion must consider all known planned capabilities.
* If source data is not provided, call it an initial estimate.
* If source data is provided, compare against it and update the module progress.

⸻

5. Implementation Quality Rating

Rate the implementation across key dimensions.

Area	Rating / 10	Assessment
Scope adherence	X	Did it do what was asked?
Architecture alignment	X	Does it fit Magna/HELIX/Enso architecture?
Governance alignment	X	Did it respect human authority, no hidden autonomy, no unsafe changes?
Code quality / structure	X	If code was changed
Test coverage	X	Are tests sufficient?
Validation quality	X	Were build/tests/smoke checks run?
Documentation / reports	X	Are reports clear and stored properly?
Risk handling	X	Were risks identified and mitigated?
Traceability	X	Are files, commits, evidence, and next steps clear?

Then calculate:

Overall Implementation Rating: X.X / 10

⸻

6. New / Modified Functions and Components

Create a function/component inventory.

#	Function / Class / Component / Script	File	Type	New / Modified	Purpose	Evidence	Status
1	functionName	path/file.ext	Function/Class/API/UI/Script/Test	New/Modified	What it does	Output reference	Verified/Unverified

If the output does not provide function-level detail, say:

Function-level inventory could not be fully confirmed from the supplied output.

Then list file-level changes instead.

⸻

7. Existing Function Memory Check

Compare new functions against the known source-data registry.

Function / Component	Already Known?	Previous Purpose	Current Change	Memory Update Needed
name	Yes/No/Unknown	Existing description	What changed	Add / Update / No change

Rules:

* If AGENT_OUTPUT_REVIEW_SOURCE_DATA.md is provided, use it as source of truth.
* If not provided, create a “proposed memory update” section.
* Never assume a function exists unless evidence is provided.

⸻

8. Validation and Evidence Review

Summarize validation.

Validation Item	Expected	Reported Result	Status	Comment
Build	npm build / equivalent	Pass/Fail/Not run	Done/Missing/Failed	Comment
Backend tests	pytest / equivalent	Pass/Fail/Not run	Done/Missing/Failed	Comment
Router smoke	command router / smoke tests	Pass/Fail/Not run	Done/Missing/Failed	Comment
Lint / diff check	git diff –check	Pass/Fail/Not run	Done/Missing/Failed	Comment
Review package	ZIP / logs / reports	Provided/Not provided	Done/Missing	Comment

Add:

Validation Verdict: Strong / Acceptable / Weak / Insufficient / Failed

⸻

9. Risks, Gaps, and Drift

Create a concise risk table.

Risk / Gap	Severity	Evidence	Required Action
Risk 1	Low/Medium/High/Critical	What shows it	What to do

Also include:

Architecture Drift: None / Minor / Moderate / High
Governance Drift: None / Minor / Moderate / High
Scope Drift: None / Minor / Moderate / High

⸻

10. Files Changed Review

If file changes are provided, create this table:

File	Change Type	Expected?	Risk	Comment
path/file	Added/Modified/Deleted	Yes/No/Unclear	Low/Medium/High	Comment

If no file list is provided:

Changed files were not provided, so file-level review is limited.

⸻

11. Commit and Repository State

Format:

Branch: <branch or Not provided>
Commit Hash: <hash or Not provided>
Working Tree Status: Clean / Dirty / Not provided
Push Status: Pushed / Not pushed / Not provided

Assessment:

* If commit hash is missing after implementation, flag it.
* If auto-commit occurred without approval, flag as governance issue.
* If push occurred without explicit instruction, flag as high severity.

⸻

12. Final Acceptance Decision

Use one of:

Accepted
Accepted with minor corrections
Needs correction before acceptance
Blocked pending evidence
Rejected due to drift

Then explain:

Reason:
- ...
Required before next sprint:
- ...

⸻

13. Source Data Update Block

At the end of every review, provide a ready-to-copy update block for AGENT_OUTPUT_REVIEW_SOURCE_DATA.md.

Use this format:

## Update — <YYYY-MM-DD> — <Sprint / Module / Task>
### Review Summary
- Agent reviewed:
- Sprint:
- Module:
- Verdict:
- Overall rating:
- Completion delta:
### New / Modified Functions
| Function / Component | File | Change | Purpose | Status |
|---|---|---|---|---|
### Sprint Progress Update
| Sprint | Previous % | New % | Basis |
|---|---:|---:|---|
### Module Progress Update
| Module | Previous % | New % | Basis |
|---|---:|---:|---|
### Decisions / Risks
| Item | Type | Status | Notes |
|---|---|---|---|
### Next Required Action
- ...

If no update is needed, say:

No source-data update required.

⸻

14. Ready-to-Copy Follow-Up Prompt

If corrections, continuation, validation, or next work is needed, provide:

14.1 Short Prompt Summary

One short paragraph:

This prompt asks the agent to correct <X>, validate <Y>, and return <Z>.

14.2 Full Ready-to-Copy Prompt

Provide a detailed prompt in a copy-ready block.

The prompt must include:

* task title
* current context
* exact corrections required
* files to inspect
* files allowed to modify
* files forbidden to modify
* validation commands
* reporting requirements
* final response format
* stop condition

The prompt must be specific enough to paste directly into Claude, Codex, Antigravity, Hermes Agent, or Grok.

⸻

15. Response Ending

Every review must end with:

Recommended next action: <action>
Use prompt: Yes / No
Source-data update required: Yes / No

⸻

Important Rules

1. Do not hallucinate details.
2. Clearly separate agent claims from verified evidence.
3. Do not mark anything complete without evidence.
4. Do not confuse design completion with implementation completion.
5. Do not confuse implementation completion with validation completion.
6. Keep human approval as final authority.
7. Always identify scope drift.
8. Always identify governance drift.
9. Always provide correction prompt if action is needed.
10. Always provide source-data update block unless no update is required.