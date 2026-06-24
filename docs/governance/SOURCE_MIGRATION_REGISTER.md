# Source Migration Register

| Source | Current classification | Action |
|---|---|---|
| `AGENTS.md` | Canonical worker entry | Retain |
| Root model adapter files | Canonical thin role adapters | Retain |
| `trace/` operating instance | Canonical applied TRACE instance | Retain and maintain through tasks |
| `../planning/*` references | Missing legacy references | Do not restore; use repository-native sources |
| `../../ChatGPTReview/*` | Historical local staging | Do not use as operational source |
| Corrected architecture/spec package | Accepted migration input | Integrate in a dedicated architecture PR |
| Corrected diagram package | Accepted editable/visual input | Integrate curated sources in a dedicated PR |
| Draft/correction ZIPs | Generated transport artifacts | Do not commit |
| Raw render logs/scripts | Reproducible but noisy | Store as Actions artifacts when needed |
| ChatGPT four-file project source | Canonical stable bootstrap exported from GitHub | Retain in GitHub and upload to ChatGPT project source |
| Legacy seven-file ChatGPT source bundle | Redundant and partly stale; old `SKILL.md` is unrelated | Remove from active source after GOV-002 validation |
| Sprint 1-4 Light Curves | Historical accepted evidence | Retain unchanged |
| Untracked Sprint 5 files | Unreviewed implementation | Review separately |

## GOV-002 supersession map

| Legacy active file | Canonical replacement |
|---|---|
| Frontend-design `SKILL.md` | `docs/governance/chatgpt-project-source/SKILL.md` |
| `AGENT_OUTPUT_REVIEW_USAGE_PROMPT.md` | `AGENTS.md`, TRACE task/evidence, and response contract review rules |
| `AGENT_OUTPUT_REVIEW_TEMPLATE.md` | TRACE review workflow and response contract review rules |
| Mentor-template `README.md` | `docs/governance/chatgpt-project-source/README.md` |
| `CHATGPT_PROMPT_RESPONSE_FORMAT.md` | GitHub issue/task packet plus response contract worker-instruction rules |
| `CHATGPT_MENTOR_ROLE_AND_OPERATING_MODEL.md` | `CHATGPT.md` and `PROJECT_BOOTSTRAP.md` |
| `CHATGPT_REVIEW_AND_NEXT_STEP_FORMAT.md` | TRACE evidence workflow and `RESPONSE_CONTRACT.md` |

Nothing is deleted solely because it is redundant. The Product Owner removes legacy active
project-source files only after the replacement package is uploaded and validated in a
fresh conversation.
