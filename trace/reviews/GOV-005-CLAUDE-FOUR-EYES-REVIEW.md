# GOV-005 — Claude Independent Four-Eyes Review

## Provenance and scope

- Review task: `GOV-005-CLAUDE-REVIEW` (packet `trace/tasks/GOV-005-CLAUDE-REVIEW.md`)
- Instruction prepared by: ChatGPT / System Architect — approved by: Product Owner (Vinay)
- Reviewer: Claude (architecture specification / independent reviewer), separate review branch
- Review target: draft PR #13 (`codex/GOV-005-multi-agent-governance`), Issue #12
- Review branch: `claude/GOV-005-four-eyes-review`, created from PR #13 head `2885f0bc62b7f5c941a1525d26eb0a97b51a6186`
- Method: independent investigation + adversarial checks against the actual repository state; implementation/validation claims were not assumed correct.

## Synchronization verdict — `SYNC_PASS`

| Sync check (policy §"Mandatory synchronization gate") | Result |
|---|---|
| PR #13 open + draft, base `main`, head `2885f0b` | PASS |
| PR #13 head behind base `main`? | PASS — 0 commits in `main` not in head (`git rev-list --count head..origin/main = 0`) |
| Repo governance check on PR #13 | `governance` check = PASS (5s) — **but see CF-1: that check does not run the GOV-005 validator** |
| Existing Claude review branch/PR/unpushed conflict | None — no `claude/GOV-005-*` branch or PR existed |
| Canonical vs operational GitHub state | Consistent enough to proceed; content drift recorded as CF-2/CF-3 (not a sync blocker) |

`SYNC_PASS` permitted review execution. Chat memory was not used as proof of state.

## Review verdict (advisory to ChatGPT / Product Owner) — `CHANGES_REQUIRED`

The governance design is **coherent, security-conscious, and preserves Product Owner authority**. It is
**not yet safely enforceable** because its central machine validator is not run in CI, and several
machine-readable records have drifted or are unconstrained. None of the findings touch runtime, product,
Hermes, HELIX, SGN-01, or policy-engine scope. **No merge, acceptance, or approval is implied by this review.**

---

## 1. Confirmed defects (severity-ordered)

### CF-1 — HIGH (enforceability): the GOV-005 validator is not executed by CI
`.github/workflows/governance-validation.yml` (the green `governance` check on PR #13) runs: `python3 -m
json.tool` on `trace/CELESTIAL_INDEX.json`; `ruby -ryaml` on three YAML files; a **required-files check that
references GOV-001-era files** (`docs/governance/SOURCE_OF_TRUTH.md`, `docs/governance/MULTI_AGENT_OPERATING_MODEL.md`,
`trace/tasks/GOV-001.md`, `trace/evidence/GOV-001_LIGHT_CURVE.md`); and pinned Gitleaks. It does **not** run
`scripts/validate_multi_agent_governance.py`, nor check for any GOV-005 canonical file
(`MULTI_AGENT_EXECUTION_POLICY.md`, `agent_handoff.schema.json`, `ACTIVE_WORK_REGISTRY.yaml`).
Evidence: `grep -rl validate_multi_agent_governance .github/` → none; full workflow body. Impact: the Light
Curve asserts "Structural policy/adapter alignment | Pass: `scripts/validate_multi_agent_governance.py`", but
that PASS came from a manual/local run (handoff deviation: "GitHub interface was used"), not CI. AC #10 is only
partially satisfied — the validator exists but does not gate the PR, so future drift is not caught.
**Recommended fix (for ChatGPT/PO — not applied here):** add a CI step that installs a pinned PyYAML and runs
the validator on `pull_request`; extend the required-files check to the GOV-005 canonical set.

### CF-2 — MEDIUM (status drift): recorded commit pointers are stale vs the branch head
`trace/ACTIVE_WORK_REGISTRY.yaml` `GOV-005.latest_known_commit` = `e7e0e07…`, and both handoffs record
`final_commit` / "Implementation commit" = `e7e0e07…`, but the branch head is `2885f0b…` — **10 later commits**
(`git log e7e0e07..HEAD`), including substantive governance edits ("clarify branch ownership" in `AGENTS.md`,
`MULTI_AGENT_EXECUTION_POLICY.md`, `WORKFLOWS.yaml`), the finalize commits, the Claude review packet, the
namespace-exception note, and a review-launch correction. This is precisely the status drift GOV-005 is
designed to prevent. **Recommended fix:** ChatGPT updates `latest_known_commit` after final push and defines
the field as the authoritative current pointer (see NB-2). ChatGPT-owned field — recorded, not edited by Claude.

### CF-3 — MEDIUM (coherence, AC #9): task status disagrees across artifacts, with no mapping
`trace/tasks/GOV-005.md` = `IN_PROGRESS`; `ACTIVE_WORK_REGISTRY.yaml` `GOV-005.status` = `PUSHED_FOR_REVIEW`;
`GOV-005_HANDOFF.json` `task.status` = `IMPLEMENTED_AWAITING_INDEPENDENT_REVIEW`; `STAR_MAP.md` = "in progress".
The handoff value is **not** in the registry `status_vocabulary`. AC #9 ("current status agree") is weakened.
**Recommended fix:** define one status source + an explicit cross-artifact mapping; restrict handoff/registry
status to the published vocabulary.

### CF-4 — MEDIUM (schema/validator weakness): `task.status` is unconstrained
`agent_handoff.schema.json` → `task.status` is `{"type":"string"}` with no enum, and
`validate_multi_agent_governance.py` does not cross-check status against `status_vocabulary`. Therefore the
out-of-vocabulary status in CF-3 passes both the schema and the validator. **Recommended fix:** constrain
`task.status` to the active-work `status_vocabulary` (or a handoff enum) and assert it in the validator.

### CF-5 — MEDIUM (owned-path conformance): 2 changed files fall outside declared writable paths
PR #13 changes 22 files; GOV-005 declares 19 writable paths. Two changed files —
`trace/evidence/GOV-005_HANDOFF.json` and `trace/evidence/GOV-005_HANDOFF.md` — are **not** covered
(writable_paths lists only `trace/evidence/GOV-005_LIGHT_CURVE.md`, no `trace/evidence/GOV-005*` glob).
GOV-005.md's own validation step "Confirm only GOV-005-owned paths changed" would flag this; neither schema nor
validator enforces changed-files ⊆ writable_paths. **Recommended fix:** add `trace/evidence/GOV-005_HANDOFF.json`
and `trace/evidence/GOV-005_HANDOFF.md` (or `trace/evidence/GOV-005*`) to GOV-005 writable_paths; add a
changed-files-in-ownership check (see NB-3).

## 2. Corrections made by Claude
**None to implementation-owned files.** Every confirmed defect lives in (a) the CI workflow — outside GOV-005
ownership and a privileged/CI change, (b) ChatGPT-owned registry fields, or (c) the immutable GOV-005 packet.
Per the four-eyes rule ("Any correction to the implementation branch requires assigned ownership"), Claude
records precise fixes for ChatGPT to apply on the implementation branch rather than editing outside its
review ownership. Claude added only: this review, the Claude handoff (`*.md`/`*.json`), and its own entry in
the active-work registry. **Every confirmed finding above is preserved regardless of disposition.**

## 3. Nonblocking improvements
- **NB-1 (LOW):** the validator hard-fails without PyYAML, and PyYAML is neither a declared repo dependency nor
  installed in CI (because CI does not run the validator). If CF-1 is fixed, pin PyYAML; document it for local runs.
- **NB-2 (LOW):** a handoff `final_commit` can never equal the commit that contains the handoff (self-reference).
  State in the template/policy that `final_commit` is the last pre-handoff implementation commit, and that
  `ACTIVE_WORK_REGISTRY.latest_known_commit` is the authoritative current pointer reconciled by ChatGPT post-push.
- **NB-3 (LOW):** add a git-aware CI/validator step that checks (i) PR-changed files ⊆ the active task's
  writable_paths, and (ii) `latest_known_commit` equals/an-ancestor-of the branch head.

## 4. Product Owner judgment questions
- **Q1:** Accept the one-time `codex/`-namespace exception for this GOV-005 PR (disclosed in the registry with
  rationale and "must not be repeated")? 
- **Q2:** Must the GOV-005 validator be wired into CI **before** merge (CF-1), or merge now with a tracked fast-follow?
- **Q3:** Choose the single canonical source of task status and the cross-artifact mapping (CF-3/CF-4).

## 5. Controls verified correct (positive findings)
- **VC-1 — Product Owner authority preserved.** `ROLE_REGISTRY` `final_authority`/`acceptance_authority` =
  `product_owner`; `WORKFLOWS` `git.merge_authority` = `product_owner`; policy reserves scope/risk/acceptance/
  merge/release to the PO; the validator asserts both. (AC #4)
- **VC-2 — Hermes inactive; no out-of-scope content.** `governed_runtime_experiment.status: inactive` (validator
  asserts). Diff contains no runtime/product/Sprint-5/policy-engine/Hermes/HELIX/SGN-01/ARCH-001 implementation. (AC #11)
- **VC-3 — System/credential/privileged/destructive/external actions are approval-gated** (policy
  §"Actions requiring Product Owner approval"). (AC #6)
- **VC-4 — Synchronization gate is well-formed** with exactly three outcomes; chat memory is explicitly not
  proof; validator asserts the outcome set. (AC #1)
- **VC-5 — Ownership exclusivity + undeclared-overlap detection** in `validate_active_work` (unique ids/branches,
  full-SHA starting commits, writable-path overlap check). (AC #2)
- **VC-6 — No secrets / no private absolute paths** in the package (independent scan: only policy text and
  validator code match "secret/token"; CI Gitleaks pinned by SHA-256).
- **VC-7 — Immutable execution authority + separate amendments** are specified, addressing the GOV-004
  control-file race. (AC #7)
- **VC-8 — Diff confined to documentation/governance/schema/evidence.** (AC #11)

## 6. Requirement-to-evidence assessment (AC #1–#12)
| AC | Assessment | Evidence |
|---|---|---|
| 1 Sync before instruction | Met (contract) | policy gate; VC-4 |
| 2 Isolated parallel ownership | Met (contract); see CF-5 gap | registry; validator overlap check |
| 3 Bounded autonomous envelope | Met | policy §Bounded autonomous actions; ROLE_REGISTRY |
| 4 PO authority explicit | Met | VC-1 |
| 5 Outcome-oriented tasks | Met | policy §Outcome-oriented task design; GOV-005.md |
| 6 Downloads/approval-gating | Met | policy §Downloads + §Approval; schema download fields |
| 7 Immutable authority + amendments | Met | VC-7 |
| 8 Human + machine readable output | Met | handoff md + json + schema |
| 9 Status agreement | **Partially met** | CF-3 |
| 10 Automated validation | **Partially met** | CF-1 (validator not in CI) |
| 11 No runtime/out-of-scope | Met | VC-2/VC-8 |
| 12 Draft PR + evidence ready for review | Met | PR #13 draft; this review |

## 7. Validation results (exact; failures and skips visible)
| Check | Command/tool | Result | Note |
|---|---|---|---|
| PR governance check | `gh pr checks 13` | PASS (5s) | does **not** run the GOV-005 validator (CF-1) |
| GOV-005 validator (local) | `python3 scripts/validate_multi_agent_governance.py` | **SKIPPED** | PyYAML not installed in review env; no dependency install permitted (NB-1) |
| JSON parse | `python3 json.load` ×3 | PASS | schema, handoff, celestial index |
| YAML parse | `ruby -ryaml` ×4 | PASS | active-work, workflows, roles, trace_config |
| Whitespace/conflict | `git diff --check main..head` | PASS | exit 0 |
| Secret / private-path scan | `grep` over PR diff | PASS | no `/Users/`, key, or token pattern |
| Owned-path conformance | changed ⊆ writable_paths | **FAIL** | 2 files outside (CF-5) |
| Commit-pointer drift | head vs `latest_known_commit` | **FAIL** | `2885f0b` ≠ `e7e0e07` (CF-2) |
| Status agreement | packet/registry/handoff/STAR_MAP | **FAIL** | 3+ differing statuses (CF-3) |
| Claude handoff vs schema | hand-verified (no `jsonschema` lib) | PASS | structural + const checks |

## 8. Residual risks
- **RR-1:** Until CF-1 is fixed, the contract is enforced only by manual validator runs, so drift (CF-2/CF-3)
  re-enters undetected — the green badge is reassuring but not enforcing the GOV-005 contract.
- **RR-2:** A pure-file validator cannot verify git head vs recorded commit or changed-files ⊆ ownership;
  these classes need a git-aware CI step or disciplined post-push reconciliation (currently manual).
- **RR-3:** ARCH-001 (PR #9) must resynchronize after GOV-005 merges; stacked-dependency risk if integration
  order is not honored.

## 9. Boundaries honored by this review
No merge, self-approval, or acceptance. No push to `main` or the implementation branch. No change to runtime,
product, Sprint 5, policy-engine selection, Hermes, HELIX, SGN-01, ARCH-001, the GOV-005 packet, or another
task's owned paths. Issue #12 not closed. Findings preserved.
