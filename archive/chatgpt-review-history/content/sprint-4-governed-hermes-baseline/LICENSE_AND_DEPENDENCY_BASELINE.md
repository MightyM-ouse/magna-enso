# License And Dependency Baseline

## Purpose

Record the mandatory Sprint 4 static license/dependency/SBOM review before any imported source is committed.

## Honesty Statement

This baseline is structurally safe / not runtime-enforced. Retained risky capabilities remain disabled until Sprint 5. No Hermes runtime, build, package script, or dependency install was performed.

## Source Reviewed

- Source repository: `https://github.com/nousresearch/hermes-agent`
- Approved SHA: `33b1d144590a211100f42aa911fd7f91ba031507`
- Local source path: `<MAGNA_LOCAL_ROOT>/_scratch/hermes-readonly-audit/hermes-clone/`

## Files Inspected

- `LICENSE`
- `pyproject.toml`
- `package.json`
- `package-lock.json`
- `uv.lock`
- `setup.py`
- `hermes_cli/setup.py`
- `ui-tui/package.json`
- `web/package.json`
- `website/package.json`
- `website/package-lock.json`
- `tools/registry.py`
- `tools/write_approval.py`
- `tools/approval.py`
- `tools/memory_tool.py`
- `tools/skill_manager_tool.py`
- `cron/jobs.py`

## Findings

- Top-level license is MIT.
- Copyright notice: `Copyright (c) 2025 Nous Research`.
- `pyproject.toml` declares `license = "MIT"` and `license-files = ["LICENSE"]`.
- Python package metadata exists in `pyproject.toml`, `uv.lock`, and setup files.
- Node package metadata exists in root/package and UI/web/website package files.
- Full Hermes manifests contain many runtime and optional dependencies tied to removed or disabled surfaces.
- Static review of candidate runtime retained files found references to removed/disabled surfaces:
  - `tools/approval.py` references gateway/plugin approval flows and remote/container backend context.
  - `tools/write_approval.py` references background review, gateway sessions, and terminal approval callback paths.
  - `tools/skill_manager_tool.py` references curator/background-review provenance and registry self-registration.
  - `cron/jobs.py` contains `no_agent` direct-script metadata and scheduler integration references.
  - `tools/registry.py` contains dynamic import/discovery mechanics.
- Because retained module candidates reference dangerous or removed surfaces, no executable Hermes Python module source is imported in this Sprint 4 baseline.

## Dependency/SBOM Result

No runtime dependencies are introduced by the baseline because no importable Hermes modules, Python packages, Node packages, package manifests under active names, or package-discovery files are imported.

Imported upstream artifacts are limited to inert provenance/license/manifest references:

| Component | Version / SHA | License | Runtime dependency impact |
|---|---|---|---|
| Hermes top-level license | `33b1d144590a211100f42aa911fd7f91ba031507` | MIT | None |
| Hermes `pyproject.toml` as `.source.txt` | `33b1d144590a211100f42aa911fd7f91ba031507` | MIT project metadata | None; non-active text artifact |
| Hermes root `package.json` as `.source.txt` | `33b1d144590a211100f42aa911fd7f91ba031507` | MIT project context | None; non-active text artifact |

## Stop-Condition Assessment

- Incompatible top-level license: not found.
- Unclear retained runtime dependency: avoided by not importing executable runtime modules.
- Retained module depends on removed dangerous surface: found in candidate runtime modules, so those modules were excluded from import.
- Need to run/build/install dependencies: not required and not performed.

## Risks

- This is not a full transitive dependency license scan of all Hermes dependencies.
- Future Sprint 5+ runtime imports must repeat dependency review for any executable module before activation.
- The baseline preserves only inert reference artifacts, not runnable retained source.

## Open Questions

- Which executable modules, if any, should be refactored into Magna-owned governed code after Sprint 5 policy design?
- Whether a future legal/SBOM tool review should be run before importing executable code.

## Recommendation

Proceed only with an inert, non-importable provenance baseline. Do not import executable Hermes modules until a future task can sever dangerous dependencies and repeat license/dependency review.

## Confidence Level

High for top-level MIT and zero-runtime-dependency impact of the selected inert artifacts. Medium for full Hermes dependency posture, because transitive review was intentionally not performed without dependency installation.
