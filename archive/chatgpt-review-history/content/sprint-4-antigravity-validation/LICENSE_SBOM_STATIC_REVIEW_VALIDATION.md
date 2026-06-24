# LICENSE_SBOM_STATIC_REVIEW_VALIDATION.md
# Magna Enso — Sprint 4 Clean Governed Hermes Baseline Preparation
# License / SBOM / Static Review Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-18

---

## 1. Purpose

Confirm that static review happened before import, MIT license is preserved, no runtime
dependency installation occurred, no Hermes build/run occurred, no active dependency
manifests were imported, and no dependency risk was introduced into runtime.

---

## 2. Pre-Import Gate Assessment

The LICENSE_AND_DEPENDENCY_BASELINE.md records the mandatory pre-import review. The gate
must be documented before any files are committed.

Evidence from LICENSE_AND_DEPENDENCY_BASELINE.md:
- Files inspected before import: LICENSE, pyproject.toml, package.json, package-lock.json,
  uv.lock, setup.py, hermes_cli/setup.py, ui-tui/package.json, web/package.json,
  website/package.json, website/package-lock.json, tools/registry.py,
  tools/write_approval.py, tools/approval.py, tools/memory_tool.py,
  tools/skill_manager_tool.py, cron/jobs.py

This is a thorough static review — not just the top-level license, but also candidate
retained module files. The review found that candidate runtime retained files reference
dangerous or removed surfaces, which caused ALL executable Python modules to be excluded.

ANTIGRAVITY ASSESSMENT: The pre-import static gate was correctly executed and documented.
The decision to exclude all executable modules because of dangerous surface dependencies
is the correct and conservative outcome. PASS.

---

## 3. License Verification

| Field | Expected | Found | Result |
|---|---|---|---|
| License type | MIT | MIT | PASS |
| Copyright holder | Nous Research | Copyright (c) 2025 Nous Research | PASS |
| License file preserved | vendor/hermes/UPSTREAM_LICENSE.txt | Present; full MIT text | PASS |
| pyproject.toml license declaration | MIT | license = "MIT"; license-files = ["LICENSE"] | PASS |
| UPSTREAM_LICENSE.txt SHA-256 | 821556e6...2a5ab6 | 821556e6...2a5ab6 (verified) | PASS |

The MIT license is fully preserved in vendor/hermes/UPSTREAM_LICENSE.txt with the exact
copyright notice. The SHA-256 of the license file matches both the manifest and the
original clone. PASS.

---

## 4. SBOM / Dependency Risk Assessment

| Check | Expected | Result |
|---|---|---|
| Runtime dependencies introduced by vendor baseline | Zero | PASS — no importable modules; no package manifests |
| Active pyproject.toml in vendor/hermes/ | None | PASS — renamed .source.txt |
| Active package.json in vendor/hermes/ | None | PASS — renamed .source.txt |
| Hermes dependencies installed | None | PASS — no installation occurred |
| Hermes uv.lock resolved | No | PASS — not present under vendor/hermes/ |
| New Python packages in magna-enso environment | None | PASS — no packages installed |
| New Node packages in magna-enso environment | None | PASS — no npm/yarn install |

SBOM verdict: Zero runtime dependencies introduced by the Sprint 4 vendor baseline.
The baseline is a zero-footprint provenance record. PASS.

---

## 5. Notable Candidate Module Findings (Static Review Results)

The static review inspected candidate Hermes runtime modules that were initially
considered for retention. All were excluded because they reference dangerous surfaces:

| Candidate Module | Dangerous Surface Reference | Outcome |
|---|---|---|
| tools/approval.py | Gateway/plugin approval flows; remote/container backend context | EXCLUDED |
| tools/write_approval.py | Background review; gateway sessions; terminal approval callbacks | EXCLUDED |
| tools/skill_manager_tool.py | Curator/background-review provenance; registry self-registration | EXCLUDED |
| cron/jobs.py | no_agent direct-script metadata; scheduler execution integration | EXCLUDED |
| tools/registry.py | Dynamic import/discovery mechanics | EXCLUDED |

ANTIGRAVITY ASSESSMENT: The decision to exclude all candidate runtime modules is correct
and conservative. The dangerous surface references in these modules would make it impossible
to safely import them without first:
1. Severing the dangerous surface dependencies
2. Implementing replacement Magna-owned versions
3. Running through Sprint 5+ policy engine design

This is the appropriate deferred scope. PASS.

---

## 6. No-Build / No-Install / No-Run Verification

| Check | Prohibited | Evidence of occurrence | Result |
|---|---|---|---|
| Hermes build | Not allowed | No build artifacts; no dist/; no .egg-info | PASS |
| Hermes run | Not allowed | No process started; no logs; no session state | PASS |
| pip/uv install | Not allowed | No new packages; no site-packages changes | PASS |
| npm install | Not allowed | No node_modules under vendor/hermes/ | PASS |
| Package scripts executed | Not allowed | No postinstall script ran; vendor/hermes/ has no package.json | PASS |
| Dependencies resolved | Not allowed | No lock file under vendor/hermes/ | PASS |

---

## 7. Active Manifest Import Check

| Manifest type | Active name | Present in vendor/hermes/? | Result |
|---|---|---|---|
| Python project | pyproject.toml | NO | PASS |
| Python setup | setup.py, setup.cfg | NO | PASS |
| Python init | __init__.py | NO | PASS |
| Node | package.json | NO | PASS |
| Node lock | package-lock.json | NO | PASS |
| uv lock | uv.lock | NO | PASS |
| Plugin manifest | plugin.yaml, plugin.yml, manifest.yaml | NO | PASS |

All active manifest types absent. The only manifest-related files are
`UPSTREAM_PYPROJECT.toml.source.txt` and `UPSTREAM_PACKAGE.json.source.txt` — both
renamed with `.source.txt` suffix making them inactive reference documents, not
packageable/discoverable artifacts.

---

## 8. Known Limitation

LICENSE_AND_DEPENDENCY_BASELINE.md §Risks correctly acknowledges: "This is not a full
transitive dependency license scan of all Hermes dependencies." The transitive dependency
review (uv.lock → all Python packages, sub-dependencies, CVE status) was intentionally
not performed because:
1. Transitive review requires dependency installation (prohibited)
2. No executable modules were imported, so transitive dependency risk = zero
3. Full transitive review is a Sprint 5+ requirement when executable modules are introduced

This is correctly scoped for Sprint 4. PASS.

---

## 9. License / SBOM / Static Review Verdict

```
Pre-import static gate:         PASS — documented before import; thorough; correct
MIT license preserved:          PASS — exact copy; SHA-256 verified
No runtime dependencies:        PASS — zero footprint on Magna Enso environment
No build/run/install:           PASS — confirmed absent
No active manifests imported:   PASS — .source.txt rename correctly applied
Candidate module exclusions:    PASS — all candidates excluded due to dangerous deps
Known limitation (transitive):  CORRECTLY SCOPED — deferred to Sprint 5+

LICENSE / SBOM / STATIC REVIEW VALIDATION: PASS
```
