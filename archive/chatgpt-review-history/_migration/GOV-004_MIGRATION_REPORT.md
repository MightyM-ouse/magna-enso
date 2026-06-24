# GOV-004 Migration Report

## Result

`EXECUTED_AWAITING_PRODUCT_OWNER_REVIEW`

The controlled archive copy completed in the isolated GOV-004 worktree. All 593 source
filesystem objects received one manifest disposition. The archive contains 401 safe files
with 2,909,677 archived bytes. The source before/after snapshots are identical.

## Inventory and disposition

| Disposition | Objects | Source bytes |
|---|---:|---:|
| `COMMIT_REDACTED` | 54 | 285,180 |
| `COMMIT_UNCHANGED` | 377 | 2,579,603 |
| `DUPLICATE_COMMITTED` | 6 | 46,721 |
| `EXCLUDE_MACHINE_NOISE` | 7 | 98,821 |
| `HOLD_GENERATED_TRANSPORT` | 3 | 3,856,795 |
| `HOLD_RAW_ARTIFACT` | 146 | 3,114,649 |
| **Total** | **593** | **9,981,769** |

`COMMIT_UNCHANGED` includes 36 safe directories. Git records the 401 committed files;
directory entries remain in the manifest for complete source-object accounting. No object
was classified as secret/credential, unsafe personal data, oversize, symlink, special, or
unreadable. Gitleaks found zero source leaks.

## Copy and provenance

- Relative hierarchy and filenames were preserved under `content/`.
- 54 text files received deterministic exact-path redaction.
- 6 byte-identical safe source files were preserved and linked with `duplicate_of`.
- Source SHA-256 is present for every readable regular source file.
- Archived SHA-256 is present and verified for every copied file.
- No binary metadata sanitization was needed: all committed candidates were valid UTF-8
  text; PNG screenshots were held as raw artifacts; generated ZIPs were held as transport.
- Candidate committed source bytes were 2,911,504, below the 100 MiB stop gate.
- No file exceeded 25 MiB and no GitHub hard limit was approached.

## Deterministic text redaction

Exact strings were replaced longest-first:

1. Exact local review-source path -> `<CHATGPT_REVIEW_SOURCE>`
2. Exact local Magna workspace path -> `<MAGNA_LOCAL_ROOT>`
3. Exact local user-home path -> `<LOCAL_USER_HOME>`

No broad name replacement was performed. The source was never rewritten.

## Source-integrity proof

Safe JSON snapshots were stored outside the repository before inventory and after copy.
They contain relative paths, object type, regular-file size and SHA-256, and modification
timestamp in nanoseconds.

| Comparison | Before | After | Result |
|---|---:|---:|---|
| Files | 549 | 549 | Equal |
| All entries | 593 | 593 | Equal |
| Regular-file bytes | 9,981,769 | 9,981,769 | Equal |
| Relative path + SHA-256 set | - | - | Equal |
| Modification timestamps | - | - | Equal |
| Complete safe snapshot | - | - | Equal |

The local source remained present and unchanged.

## Validation

| Check | Result |
|---|---|
| Manifest JSON parse | Pass |
| Every source object has one allowed disposition | Pass: 593/593 |
| Archived file count | Pass: 401 manifest / 401 filesystem |
| Archived SHA-256 recomputation | Pass: 401/401 |
| Archived JSON parse | Pass: 6/6 |
| Archived YAML syntax parse | Pass: 11/11 using Ruby Psych AST parser |
| Archived SVG/draw.io XML parse | Pass: 50/50 |
| Exact private-path scan in archive | Pass |
| Source Gitleaks 8.30.1 | Pass: zero findings |
| Source integrity | Pass: complete snapshots equal |
| Governed Hermes-audit path | Pass: no longer ignored after approved exception |
| Unrelated Hermes-audit paths | Pass: three fixture path shapes remain ignored by `.gitignore` line 37 |
| Application/backend/browser tests | Not applicable: archive/documentation-only task |
| Complete staged-tree Gitleaks | Pass: Gitleaks 8.30.1, zero findings |
| Allowed staged paths | Pass: only GOV-004 task-packet paths |
| Held/symlink/special/oversize staging | Pass: none staged |
| `git diff --check` | Pass under Product Owner exception: exactly 38 source-identical findings across the 28 governed paths below; all non-archive changed files pass |
| Governance Actions check | Pending push |

Historical Python and JavaScript files were archived as noncanonical text and were not
executed. The first source-scan wrapper used zsh's reserved `status` variable after the
successful scan and failed at the wrapper step; the identical scan was rerun successfully
with a nonreserved variable. A Python YAML parser was unavailable. An initial Ruby command
used unsupported modern keyword arguments with the system Ruby 2.6 and failed; YAML syntax
was then verified successfully with `YAML.parse_file`. These failures did not alter source
or archive content.

The first staged review found that 41 text files under two `raw-command-output/`
directories had been classified by UTF-8 type rather than by their raw-log purpose. The
commit gate stopped publication. Those 41 files and two directory records were reclassified
as `HOLD_RAW_ARTIFACT`, their generated archive copies were removed, manifest and report
totals were recomputed, and staging was refreshed. No source file was changed or deleted.

The refreshed default `git diff --cached --check` then reported 24 trailing-whitespace
findings and 14 extra-blank-line-at-EOF findings across 28 historical archive files. A
provenance-aware comparison verified all 38 findings already exist in the corresponding
read-only source files. All non-archive changed paths pass `git diff --check`. Removing the
historical whitespace would change archived hashes and conflict with the manifest's
`COMMIT_UNCHANGED` or exact-path-only `COMMIT_REDACTED` dispositions. The Product Owner
approved preserving this exact bounded set; any additional path or finding remains a stop.

### Approved historical whitespace paths

| Findings | Archive path |
|---:|---|
| 7 | `archive/chatgpt-review-history/content/AGENT_OUTPUT_REVIEW_SOURCE_DATA.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-antigravity-independent-validation/02_PACKAGE_INTEGRITY_VALIDATION.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-antigravity-independent-validation/04_VALIDATION_REPRODUCIBILITY.md` |
| 3 | `archive/chatgpt-review-history/content/magna-program-antigravity-independent-validation/adversarial-analysis/mcc_regex_bypass.py` |
| 1 | `archive/chatgpt-review-history/content/magna-program-discovery-reconstruction/02_PRODUCT_LINEAGE_AND_TERMINOLOGY.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-discovery-reconstruction/16_DECISIONS_REQUIRED_FROM_VINAY.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-discovery-reconstruction/17_RECOMMENDED_FOUNDATION_SEQUENCE.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/00_EVIDENCE_COMPLETION_MASTER_REPORT.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/01_PREFLIGHT_AND_REPOSITORY_STATE.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/02_CANONICAL_MAGNA_DIRECT_READ.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/03_CURRENT_SOURCE_ARCHITECTURE_VERIFICATION.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/04_PRESGN_STATUS_VERIFICATION.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/05_POLICY_ENGINE_COMPARATIVE_AUDIT.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/06_TRACE_COMPLETE_ASSESSMENT.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/07_RUNTIME_TRACEABILITY_CONTRACT_MAP.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/08_UX_ENVIRONMENT_AND_BACKLOG_VERIFICATION.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/09_VALIDATION_RESULTS.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/10_CORRECTED_STATUS_AND_PERCENTAGES.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/11_REUSE_EVIDENCE_UPDATE.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/12_REMAINING_CONTRADICTIONS_AND_QUESTIONS.md` |
| 1 | `archive/chatgpt-review-history/content/magna-program-evidence-completion/13_RECOMMENDED_FOUNDATION_GATE.md` |
| 1 | `archive/chatgpt-review-history/content/sprint-5-antigravity-approval-validation/CODEX_PROMPT_READINESS_VALIDATION.md` |
| 1 | `archive/chatgpt-review-history/content/sprint-5-antigravity-approval-validation/ENFORCEMENT_ARCHITECTURE_VALIDATION.md` |
| 1 | `archive/chatgpt-review-history/content/sprint-5-antigravity-approval-validation/HUMAN_AUTHORITY_BOUNDARY_VALIDATION.md` |
| 3 | `archive/chatgpt-review-history/content/sprint-5-antigravity-approval-validation/TEST_AND_COVERAGE_PLAN_VALIDATION.md` |
| 1 | `archive/chatgpt-review-history/content/sprint-5-antigravity-approval-validation/THREAT_AND_BYPASS_MODEL_VALIDATION.md` |
| 1 | `archive/chatgpt-review-history/content/sprint-5-antigravity-security-revalidation/PROVIDER_ISOLATION_REVALIDATION.md` |
| 1 | `archive/chatgpt-review-history/content/sprint-5-approval-package/FAILURE_MODES_AND_FAIL_CLOSED_BEHAVIOR.md` |

Total: 38 findings across 28 paths. The archived bytes remain unchanged.

## Synchronization recovery

Remote commit `d1f53d4` amended only `trace/tasks/GOV-004.md` to authorize the narrow
ignore-rule exception. Because that file also contained local execution-state edits, the
initial `--ff-only` attempt correctly aborted without changing the worktree. Following the
Issue #10 recovery instruction, Codex stored the complete local file, binary patch, base
version, remote version, reconciled version, and SHA-256 records in a mode-0700 directory
outside the repository. The remote task packet remained governing, while substantive
execution facts were placed in its labelled pre-amendment checkpoint section.

After external reconciliation validation, only the task file was restored to `HEAD`, the
branch fast-forwarded to `d1f53d4`, and the reconciled task was replaced byte-for-byte.
Hashes confirmed every other tracked and untracked GOV-004 artifact remained unchanged.
No reset, clean, stash, force checkout, untracked deletion, ARCH-001 change, or source
mutation occurred.

## Commands and versions

- Git `2.54.0`
- Gitleaks `8.30.1`
- `python3 /private/tmp/gov004_archive.py inventory`
- `python3 /private/tmp/gov004_archive.py copy`
- `python3 /private/tmp/gov004_archive.py snapshot-after`
- `gitleaks dir <source> --redact=100 --report-format json --report-path <outside-repository> --no-banner`
- `python3 -m json.tool <manifest>`
- Ruby Psych `YAML.parse_file` over archived YAML files
- Python `xml.etree.ElementTree` over archived SVG and draw.io files

The one-off migration program and redacted raw scanner report remain outside the
repository. Final staged-tree, diff, path, manifest, size, symlink, ignore, branch/PR, and
Governance CI results are recorded in the GOV-004 Light Curve.
