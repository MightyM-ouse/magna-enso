# GOV-006 Light Curve

## Status

`IMPLEMENTED_AWAITING_PRODUCT_OWNER_TEMPLATE_REVIEW`

## Result

Created a canonical agent-routing guide, machine-readable routing matrix, strengthened
ChatGPT response contract, and seven response templates. The package directly addresses
misleading branch ownership, duplicated chat prompts, ambiguous evidence state, inconsistent
status reporting, unclear agent selection, and missing next-gate visibility.

## Parallel execution evidence

| Check | Result |
|---|---|
| GOV-005 review baseline | Fixed at `2885f0bc62b7f5c941a1525d26eb0a97b51a6186` |
| Claude published branch/PR at GOV-006 start | None found |
| Claude state | `SYNC_UNVERIFIED_LOCAL_STATE` - known active locally |
| Writable overlap | None; GOV-006 uses response/routing files only |
| GOV-005 PR mutation | None |
| GOV-006 branch namespace | Correct: `chatgpt/` |

## Controls delivered

- Agent responsibility and prohibition matrix.
- Task-to-agent default routing.
- Architecture-to-code, defect, governance, and Hermes-experiment patterns.
- Proactive ChatGPT agent recommendation rule.
- Repository-native dispatch with short launch messages.
- Mandatory workflow response header.
- Verified/worker-claim/inference/unknown/decision evidence states.
- Seven standard response templates.
- Integrity rules separating changed, proposed, verified, and claimed state.
- Machine-readable routing validation.

## Validation

| Check | Result |
|---|---|
| Routing YAML parse | Pass |
| Agent/route completeness | Pass: 5 agents, 12 default routes |
| Hermes inactive boundary | Pass |
| Response template completeness | Pass: 7/7 required templates |
| Response contract cross-links | Pass |
| Private path/secret-pattern scan | Pass |
| `git diff --check` | Pass |
| Runtime/application tests | Not applicable; governance documentation only |

## Decision required

Product Owner reviews whether the templates are clear, concise, and sufficient for routine
Magna collaboration. No merge or acceptance is implied by publication.
