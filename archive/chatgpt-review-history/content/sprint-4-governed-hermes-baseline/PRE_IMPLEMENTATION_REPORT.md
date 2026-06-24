# Pre-Implementation Report

## Purpose

Record the Sprint 4 plan of record before any source import or file creation inside `magna-enso/`.

## 1. Current Branch And HEAD

- Repository: `<MAGNA_LOCAL_ROOT>/magna-enso`
- Branch before isolation: `main`
- Isolated branch used: `audit/sprint-4-governed-hermes-baseline`
- HEAD before Sprint 4 work: `966629a`
- Current accepted commit: `966629a`

## 2. Git Status

- Mandatory initial status on `main`: clean (`## main`)
- Mandatory initial HEAD confirmation: `966629a`
- Isolation branch created before repo edits: `audit/sprint-4-governed-hermes-baseline`

## 3. Confirmed Sprint 4 Scope

Sprint 4 is approved for bounded baseline preparation only:

- Selective vendor import only.
- Imported source must be inert and quarantined.
- No runtime activation.
- No Hermes run, build, activation, or runtime use.
- No policy engine implementation.
- No runtime enforcement claim.
- No Sprint 5 work.
- No push, merge, or commit without separate human approval.

## 4. Approved Hermes SHA

- Source repo: `https://github.com/nousresearch/hermes-agent`
- Approved SHA: `33b1d144590a211100f42aa911fd7f91ba031507`
- Source must not use moving `main` or a newer SHA.
- If the source at that SHA is unavailable or mismatched, Sprint 4 must stop.

## 5. Proposed Target Path

- Proposed repo target: `vendor/hermes/`
- Target posture: inert/quarantined.
- No app code may import it.
- No CLI/UI entry point may invoke it.
- No tool registration or package discovery may activate it.

## 6. Proposed Retained Modules

Retained content is limited to inert models, metadata, and documentation that can be mapped to Sprint 3 capability states:

- Local safe status/read models: `active_safe`
- Sensitive local read models: `read_only`
- Project metadata/status model: `active_safe`
- Memory write model documentation/design only: `draft_only`
- Skill write model documentation/design only: `draft_only`
- Scheduler metadata documentation/design only: `report_only`
- Browser snapshot model documentation/design only: `read_only` if privacy-gated, not activated
- Terminal/code model documentation/design only: `approval_required`, disabled until a future policy engine exists

The first source import will be restricted to minimal, non-executable provenance/license and static schema/model references only. Any retained source with a dependency on a removed dangerous surface is a stop condition.

## 7. Proposed Excluded/Removed Surfaces

The following surfaces are excluded from import:

- Background review and self-improvement loops
- Curator/self-review execution
- Direct script cron
- Executable scheduler
- Messaging gateways
- Outbound delivery
- Cloud provider activation
- External memory sync
- Plugin/MCP dynamic loading
- Remote execution backends
- Subagent delegation
- Browser actions
- Terminal/code execution activation
- API listeners
- File transfer activation

## 8. License/SBOM/Static Review Approach

Before any imported source is committed:

- Read source manifests and license files statically.
- Verify source SHA and provenance.
- Preserve MIT license text and copyright notice.
- Inventory every imported file.
- Record hashes for imported files.
- Identify whether retained files introduce runtime dependencies.
- Stop if license or dependency status is incompatible or unclear.

No Hermes runtime, build, package script, or dependency install is permitted for review.

## 9. No-Network / No-Run / No-Build Confirmation

- Hermes will not be run.
- Hermes will not be built.
- No Hermes dependencies will be installed.
- No package scripts will execute.
- No cloud, messaging, plugin/MCP, browser action, terminal execution, or API listener surface will be activated.
- Validation is static/structural only.

## 10. Stop Conditions

Stop and report if:

- Current repo is dirty outside approved Sprint 4 work.
- Current source SHA differs from `33b1d144590a211100f42aa911fd7f91ba031507`.
- Source at the approved SHA is unavailable.
- Any retained file depends on a removed dangerous surface.
- License or dependency status is unclear or incompatible.
- Completing the task would require running/building Hermes or installing dependencies.
- Completing the task would require runtime/policy-engine implementation.
- Completing the task would start Sprint 5 or promote EH-0005B.

## Confidence Level

High for scope and boundaries. Import feasibility remains subject to the mandatory static license/provenance review gate.

## Recommendation

Proceed to static source/provenance/license review only. If clean, import the smallest inert quarantined baseline needed to preserve provenance and retained-surface design references.
