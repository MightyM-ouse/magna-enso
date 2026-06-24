# Magna Enso ChatGPT Project Source

## What this package is

This four-file package gives ChatGPT stable operating instructions while keeping changing
product knowledge in the canonical GitHub repository.

| File | Responsibility |
|---|---|
| `SKILL.md` | Routes Magna Enso requests to the correct bootstrap and contract. |
| `PROJECT_BOOTSTRAP.md` | Defines GitHub-first startup, roles, TRACE workflow, and boundaries. |
| `RESPONSE_CONTRACT.md` | Defines concise but meaningful responses and short analogies. |
| `README.md` | Installation, validation, and legacy-source removal guidance. |

## Installation

1. Upload all four files to the ChatGPT project source together.
2. Remove the seven legacy files listed below; do not run old and new instructions in
   parallel.
3. Start a fresh project conversation.
4. Ask ChatGPT to identify the canonical repository and current Star Map state.
5. Confirm that it checks GitHub before answering and uses the response contract.

## Legacy files to remove after upload

- `SKILL.md` containing the unrelated `frontend-design` skill (replace with this package).
- `AGENT_OUTPUT_REVIEW_USAGE_PROMPT.md`
- `AGENT_OUTPUT_REVIEW_TEMPLATE.md`
- Previous `README.md` titled `Magna ChatGPT Mentor Templates`
- `CHATGPT_PROMPT_RESPONSE_FORMAT.md`
- `CHATGPT_MENTOR_ROLE_AND_OPERATING_MODEL.md`
- `CHATGPT_REVIEW_AND_NEXT_STEP_FORMAT.md`

Their useful rules are superseded by GitHub `AGENTS.md`, `CHATGPT.md`, TRACE, and this
response contract. Historical copies may be archived outside the active project source if
desired, but must not remain active instructions.

## Validation questions

Use these in a fresh conversation:

1. `What repository is canonical, and what must you read before giving project status?`
2. `What is our next step? Use the standard response style.`
3. `Review this worker claim when no evidence is provided.`
4. `Explain squash merge using a short analogy.`

Expected behavior: GitHub-first verification, no invented status, concise context, a useful
analogy when appropriate, one clear next action, and no unnecessary manual UI checks.
