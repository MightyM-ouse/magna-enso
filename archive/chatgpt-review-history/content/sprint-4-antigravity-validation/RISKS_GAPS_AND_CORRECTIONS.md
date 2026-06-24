# RISKS_GAPS_AND_CORRECTIONS.md
# Magna Enso — Sprint 4 Clean Governed Hermes Baseline Preparation
# Risks, Gaps, and Corrections
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-18

---

## 1. Purpose

Enumerate all risks, gaps, and corrections found during Sprint 4 validation.

---

## 2. Issues Register

| ID | Severity | Type | Description | Blocking? | Required Action |
|---|---|---|---|---|---|
| VN-S4-01 | INFO | State naming | browser_snapshot_model state is read_only_if_privacy_gated rather than plain read_only. This is actually MORE precise and correctly encodes the MVP = disabled posture (privacy gate does not exist). Noted for documentation clarity only. | NO | None — the conditional name is correct and more informative |

---

## 3. Items Scrutinized and Confirmed Non-Issues

The following items were investigated and confirmed to be non-issues:

| Item | Conclusion |
|---|---|
| UPSTREAM_PYPROJECT.toml.source.txt contains active package declarations | NOT an issue — .source.txt suffix makes this file non-discoverable by pip/uv/setuptools. The file is a reference artifact, not a manifest. |
| UPSTREAM_PYPROJECT.toml.source.txt mentions 40+ Python dependencies | NOT an issue — text references only; no package is installed; no dependency is introduced into the runtime environment |
| UPSTREAM_PACKAGE.json.source.txt contains scripts and workspaces | NOT an issue — .source.txt suffix; npm/yarn ignore this file; no script is executed |
| RETAINED_SURFACE_STATES.yaml could be loaded by Python code | NOT an issue — no Python code exists in magna-enso/; no YAML loader is wired to this file |
| vendor/hermes/retained/ might be confused for runnable code | NOT an issue — README.md explicitly states "This folder does not contain active Hermes runtime code"; contents are metadata records |
| The word "import" appears in pyproject.toml.source.txt | NOT an issue — this refers to Python import paths in setuptools configuration, not code being imported into Magna Enso |
| provenance/UPSTREAM_PYPROJECT.toml.source.txt is 365 lines | NOT an issue — all text; no code executed; SHA-256 matches approved clone |
| No __init__.py under vendor/ | This is CORRECT — absence of __init__.py prevents Python package discovery |

---

## 4. Forward Risks (Sprint 4 Correctly Identifies, Does Not Claim to Close)

The following risks are correctly held OPEN in the risk register and are not claimed to
be mitigated by the Sprint 4 baseline:

| Risk | Status | Sprint 4 Contribution |
|---|---|---|
| R-01 (Hermes reuse/coupling) | OPEN | Baseline is minimal and inert; coupling reduced by non-import of executable modules |
| R-02 (License/deps) | OPEN | Top-level MIT confirmed; full transitive review deferred to Sprint 5+ executable import |
| R-06 (Policy bypass) | OPEN | Sprint 4 is structurally safe by absence only; enforcement requires Sprint 5 policy engine |
| R-11 (Fork maintenance) | WATCH | This is not a full fork; selective vendor baseline reduces maintenance burden |

These risks are correctly documented in RISK_REGISTER.md Sprint 4 note and ENSO-0004_LIGHT_CURVE.md.
The ENSO-0004 explicitly lists R-01, R-02, R-06 as OPEN in §Risks.

---

## 5. Future Sprint 5 Requirements Implied by Sprint 4

Sprint 4 correctly defers the following to Sprint 5+. These are not Sprint 4 gaps —
they are correctly scoped as future work:

| Item | Why Deferred |
|---|---|
| Runtime policy engine | Sprint 5 — requires separate approval, design, and implementation |
| Capability gate implementation | Sprint 5 — requires policy engine first |
| Executable retained module import | Sprint 5+ — requires policy engine + dependency review + approval |
| Transitive dependency SBOM scan | Sprint 5+ — requires dependency installation to scan transitives |
| Approval-request flow implementation | Sprint 5 (ENSO-F-0502) |
| tools/approval.py Magna-owned replacement | Sprint 5+ — dangerous deps in Hermes version must be severed |
| tools/write_approval.py Magna-owned replacement | Sprint 5+ — same reason |
| tools/skill_manager_tool.py Magna-owned replacement | Sprint 5+ — curator/background-review deps must be severed |

---

## 6. Severity Summary

| Severity | Count | Items |
|---|---|---|
| CRITICAL | 0 | None |
| HIGH | 0 | None |
| MEDIUM | 0 | None |
| LOW | 0 | None |
| INFO | 1 | VN-S4-01 (browser_snapshot_model state name — informational only; no action required) |

Zero blocking issues. Zero required corrections. Zero recommended corrections.
Sprint 4 is clean. This is the best possible validation outcome for a bounded provenance
baseline task.

---

## 7. What Is Confirmed Absent (All Required-Absent Items)

- Critical issues: CONFIRMED NONE
- High issues: CONFIRMED NONE
- Runtime code: CONFIRMED ABSENT
- Policy engine code: CONFIRMED ABSENT
- Dangerous surfaces: ALL 15 CONFIRMED ABSENT
- False enforcement claims: CONFIRMED ABSENT
- Sprint 5 work: CONFIRMED NOT STARTED
- New commits: CONFIRMED — 0 new commits on branch
- Push: CONFIRMED — no remote branch
- EH-0005B promotion: CONFIRMED — remains PROPOSED
- Hermes run/build/activate: CONFIRMED DID NOT OCCUR
- Dependency installation: CONFIRMED DID NOT OCCUR
