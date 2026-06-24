AGENT_OUTPUT_REVIEW_USAGE_PROMPT.md

Use this prompt whenever attaching an agent output for review.

⸻

Prompt

Review the attached agent output using:

* AGENT_OUTPUT_REVIEW_TEMPLATE.md
* AGENT_OUTPUT_REVIEW_SOURCE_DATA.md

Please provide the response in the standard structured format.

You must include:

1. Executive verdict.
2. Requested vs implemented comparison.
3. Sprint completion percentage.
4. Module completion percentage.
5. Implementation quality rating table.
6. New / modified functions, components, scripts, APIs, or contracts.
7. Existing function memory check against the source data.
8. Validation and evidence review.
9. Risks, gaps, and drift.
10. Files changed review.
11. Commit/repository state review.
12. Final acceptance decision.
13. Source-data update block for AGENT_OUTPUT_REVIEW_SOURCE_DATA.md.
14. If corrections or next work are required:
    * short prompt summary
    * full ready-to-copy prompt for the correct worker

Rules:

* Do not hallucinate missing details.
* Mark unknowns as Not provided or Unverified.
* Clearly separate agent claims from verified evidence.
* Do not mark the sprint complete unless evidence supports it.
* Do not mark the module complete unless the source-data tracker supports it.
* Human approval remains final authority.

At the end, clearly state:

Recommended next action:
Use prompt: Yes / No
Source-data update required: Yes / No