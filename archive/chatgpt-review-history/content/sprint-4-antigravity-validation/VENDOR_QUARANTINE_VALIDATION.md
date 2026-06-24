# VENDOR_QUARANTINE_VALIDATION.md
# Magna Enso — Sprint 4 Clean Governed Hermes Baseline Preparation
# Vendor Quarantine Validation
# Reviewer: Antigravity (Spectrometer)
# Date: 2026-06-18

---

## 1. Purpose

Confirm that vendor/hermes/ is inert/quarantined: no executable Hermes modules, no .py
files, no active manifests, no setup files, no plugin manifests, no runtime directories,
no executable entrypoints, and no wiring into the Magna Enso runtime.

---

## 2. File Inventory Check

Complete file list under vendor/hermes/ (independently verified via find):

```
<MAGNA_LOCAL_ROOT>/magna-enso/vendor/hermes/README.md
<MAGNA_LOCAL_ROOT>/magna-enso/vendor/hermes/UPSTREAM_LICENSE.txt
<MAGNA_LOCAL_ROOT>/magna-enso/vendor/hermes/provenance/UPSTREAM_PACKAGE.json.source.txt
<MAGNA_LOCAL_ROOT>/magna-enso/vendor/hermes/provenance/UPSTREAM_PYPROJECT.toml.source.txt
<MAGNA_LOCAL_ROOT>/magna-enso/vendor/hermes/retained/README.md
<MAGNA_LOCAL_ROOT>/magna-enso/vendor/hermes/retained/RETAINED_SURFACE_STATES.yaml
```

Total files: 6
Total directories under vendor/hermes/ (excluding root): provenance/, retained/

---

## 3. Prohibited File Type Checks

| Check | Prohibited Pattern | Found | Result |
|---|---|---|---|
| Python source files | *.py | 0 | PASS |
| Active package manifests | package.json (non .source.txt) | 0 | PASS |
| Active Python manifests | pyproject.toml (non .source.txt) | 0 | PASS |
| Setup files | setup.py, setup.cfg | 0 | PASS |
| Python init files | __init__.py | 0 | PASS |
| Plugin manifests | plugin.yaml, plugin.yml, manifest.yaml | 0 | PASS |
| Executable entrypoints | __main__.py, run_agent.py, cli.py, manage.py | 0 | PASS |
| Lock files (active) | uv.lock, package-lock.json | 0 | PASS |
| JavaScript source | *.js, *.ts | 0 | PASS |

All prohibited file types: ABSENT. PASS.

---

## 4. Prohibited Runtime Directory Checks

| Required absent directory | Found under vendor/hermes/? | Result |
|---|---|---|
| agent/ | NO | PASS |
| tools/ | NO | PASS |
| cron/ | NO | PASS |
| gateway/ | NO | PASS |
| plugins/ | NO | PASS |
| providers/ | NO | PASS |
| hermes_cli/ | NO | PASS |
| acp_adapter/ | NO | PASS |
| tui_gateway/ | NO | PASS |
| web/ | NO | PASS |
| ui-tui/ | NO | PASS |
| apps/ | NO | PASS |
| optional-mcps/ | NO | PASS |
| optional-skills/ | NO | PASS |
| src/ | NO | PASS |

All prohibited runtime directories: ABSENT. PASS.

---

## 5. Manifest Renaming Check

| File | Active name | Renamed as .source.txt | Result |
|---|---|---|---|
| pyproject.toml | Not present as pyproject.toml | UPSTREAM_PYPROJECT.toml.source.txt | PASS |
| package.json | Not present as package.json | UPSTREAM_PACKAGE.json.source.txt | PASS |

The `.source.txt` suffix is the critical quarantine mechanism for manifests. Python's
package discovery (setuptools, uv, pip) and Node's package resolution (npm, yarn)
will not recognize files with `.source.txt` extensions as active manifests. These files
cannot trigger package installation or tool registration. PASS.

---

## 6. Runtime Wiring Check

| Check | Evidence | Result |
|---|---|---|
| vendor/hermes/ imported by any Magna Enso code | No app code exists yet in magna-enso/; vendor/hermes/ is not referenced by any Python import | PASS |
| vendor/hermes/ exposed via CLI or UI | No CLI/UI code exists in magna-enso/; vendor/hermes/ has no entrypoint | PASS |
| vendor/hermes/ wired into tool registry | No tool registry code in magna-enso/; no tool registration files under vendor/hermes/ | PASS |
| vendor/hermes/ package-discovered | No active __init__.py, pyproject.toml, or package.json — package discovery impossible | PASS |
| RETAINED_SURFACE_STATES.yaml loaded by runtime | No runtime code in magna-enso/ that could load it; YAML is static documentation only | PASS |

vendor/hermes/README.md explicitly states:
  "not imported by Magna Enso application code, not wired into runtime, not exposed through
  CLI or UI, not executable, not registered as tools, not package-discovered as active code,
  not evidence that runtime policy enforcement exists."

---

## 7. Quarantine Declaration Assessment

The quarantine block in RETAINED_SURFACE_STATES.yaml:

```yaml
quarantine:
  active_runtime: false
  imported_by_app_code: false
  exposed_by_cli_or_ui: false
  executable: false
  tool_registered: false
  package_discovered: false
  network_enabled: false
```

All 7 quarantine flags set to false. Antigravity independently verified all 7:
- active_runtime: false ✅ — no runtime code exists in magna-enso/
- imported_by_app_code: false ✅ — no app code exists; no import statements
- exposed_by_cli_or_ui: false ✅ — no CLI/UI exists; no entrypoint
- executable: false ✅ — 0 .py, 0 executable files
- tool_registered: false ✅ — no tool registry code; no tool registration files
- package_discovered: false ✅ — no active manifests; .source.txt names not discoverable
- network_enabled: false ✅ — no network source; no active listeners; no gateway

All quarantine flags verified accurate. PASS.

---

## 8. Vendor Quarantine Verdict

```
Total files in vendor/hermes/: 6 (expected 6) — PASS
.py files:                      0 — PASS
Active manifests:               0 — PASS (manifests renamed .source.txt)
Runtime directories:            0 — PASS
Executable entrypoints:         0 — PASS
Plugin manifests:               0 — PASS
Runtime wiring:                 None — PASS
Quarantine YAML block:          All 7 flags false; independently verified — PASS
README quarantine statement:    Complete; accurate — PASS

VENDOR QUARANTINE VALIDATION: PASS — FULLY INERT
```
