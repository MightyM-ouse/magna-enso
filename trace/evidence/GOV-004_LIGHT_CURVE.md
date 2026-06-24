# GOV-004 Light Curve

## Identity

- Task: GOV-004 - GitHub-native project review archive
- Issue: #10
- Draft pull request: #11
- Worker: Codex
- Mode: investigation then execution
- Branch: `codex/GOV-004-chatgpt-review-archive`
- Starting task-branch HEAD: `a8ca4125326280861b02100fde5c652517e6306c`
- Verified `main` baseline: `20e69cad9edfc71e193de3411f7778a64c041273`
- Migration commit: `ab8f7bb`
- Date: 2026-06-24

## Scope result

Created a governed, noncanonical archive under `archive/chatgpt-review-history/`. No
runtime, Sprint 5, policy-engine, Hermes, HELIX, SGN-01, dependency, environment,
infrastructure, or ARCH-001 change was made. The local review source was not modified or
deleted.

## Evidence chain

1. GitHub Issue #10, draft PR #11, assigned branch, task packet, role, workflow, context
   routes, governance policies, and remote state were verified.
2. The assigned branch was confirmed to use the exact recorded `main` merge base.
3. A clean isolated worktree was created; the dirty Sprint 5 checkout was left untouched.
4. The pre-implementation report was created before source copying.
5. Gitleaks 8.30.1 scanned the source with a fully redacted report outside Git: zero
   findings.
6. A no-symlink-traversal inventory recorded 593 objects / 549 files / 9,981,769 bytes.
7. Every object received exactly one allowed disposition before controlled copy.
8. 401 safe files were copied with preserved hierarchy; 54 received exact-path redaction
   and 6 byte-identical duplicates were preserved with provenance links.
9. Before/after source snapshots matched in full, including relative paths, hashes, sizes,
   and modification timestamps.
10. Manifest, archived hashes, private-path absence, JSON, YAML, XML, held-item, size, and
    source-integrity checks passed.
11. A remote task-packet amendment was reconciled losslessly through the exact-file
    recovery authorized on Issue #10. Private mode-0700 backups, the local binary patch,
    base/remote/reconciled copies, and SHA-256 records remain outside the repository.
12. The approved `.gitignore` exception unignored only the governed nine-file directory;
    unrelated named, generic, and archive-local Hermes-audit fixture paths remain ignored.

## Disposition summary

| Disposition | Objects | Source bytes |
|---|---:|---:|
| `COMMIT_REDACTED` | 54 | 285,180 |
| `COMMIT_UNCHANGED` | 377 | 2,579,603 |
| `DUPLICATE_COMMITTED` | 6 | 46,721 |
| `EXCLUDE_MACHINE_NOISE` | 7 | 98,821 |
| `HOLD_GENERATED_TRANSPORT` | 3 | 3,856,795 |
| `HOLD_RAW_ARTIFACT` | 146 | 3,114,649 |

Committed archive payload: 401 files / 2,909,677 archived bytes.

## Validation record

| Validation | Result |
|---|---|
| Source secret scan | Pass; Gitleaks 8.30.1, zero findings |
| Source stop gates | Pass; 593 <= 5,000 and candidate 2,911,504 bytes <= 100 MiB |
| Manifest coverage | Pass; 593/593 objects, one disposition each |
| Archived hashes | Pass; 401/401 recomputed |
| JSON / YAML / XML | Pass; 6/6, 11/11, 50/50 |
| Local private-path absence | Pass for migrated archive and GOV-004 evidence; governing task retains its authorized exact local-path controls |
| Source integrity | Pass; snapshots exactly equal |
| Synchronization recovery | Pass; HEAD fast-forwarded to `d1f53d4`, all other GOV-004 artifact hashes unchanged |
| Governed ignore exception | Pass; governed path unignored, three unrelated fixture path shapes still ignored |
| Allowed diff paths | Pass; only task-packet-authorized paths staged |
| Held/symlink/special/oversize staging | Pass; none staged |
| Complete staged-tree Gitleaks | Pass; Gitleaks 8.30.1, zero findings |
| `git diff --check` | Pass under Product Owner exception: exactly 38 source-identical findings across the 28 governed paths below; all non-archive changed files pass |
| Governance Actions | Pass for migration commit `ab8f7bb`; run `28120144618`, job `83269695182` |
| Build/backend/router/browser | Not applicable; archive/documentation-only task |

## Visible failures and limitations

- The first successful Gitleaks source scan was followed by a wrapper failure because
  `status` is reserved in zsh. The scan was rerun successfully using `rc`.
- PyYAML was unavailable and was not installed. The first system-Ruby YAML command used
  unsupported modern keywords and failed; all 11 YAML files then passed the compatible
  Psych AST syntax parser.
- Historical code is noncanonical archive text and was not executed.
- No held raw/transport material was uploaded because GOV-004 does not authorize a new
  artifact mechanism.
- Initial staging exposed 41 UTF-8 files under two `raw-command-output/` directories that
  had been typed as text instead of held by purpose. The gate stopped publication; all 41
  files and both directory records were reclassified as raw artifacts, their generated
  archive copies were removed, and manifest/report totals were recomputed.
- Default staged `git diff --check` reports 24 trailing-whitespace and 14 blank-line-at-EOF
  findings across 28 historical archive files. All 38 findings were verified against the
  read-only source. Governance-only changed paths pass. Silent normalization would violate
  archive fidelity and recorded hashes. The Product Owner approved preserving this exact
  bounded set; any additional finding or path remains a stop.

## Approved historical whitespace paths

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
- The first `git merge --ff-only` attempt after the remote amendment aborted because the
  task packet had local changes. The authorized exact-file recovery then completed without
  loss; the aborted attempt changed no file.

## Review state

Implementation is complete but not accepted. Product Owner review, any independent review
the Product Owner requires, and Product Owner merge remain outstanding. Codex did not
merge, close the issue, delete the branch, modify the source, or self-accept.
