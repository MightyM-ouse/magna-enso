# License And Dependency Review

## Purpose

Provide an engineering review of Hermes Agent licensing and dependency posture for Sprint 2. This is not legal advice.

## Files Inspected

- `LICENSE`
- `pyproject.toml`
- `uv.lock`
- `setup.py`
- `package.json`
- `package-lock.json`
- `apps/bootstrap-installer/package.json`
- `apps/desktop/package.json`
- `apps/shared/package.json`
- `scripts/whatsapp-bridge/package.json`
- `scripts/whatsapp-bridge/package-lock.json`
- `ui-tui/package.json`
- `web/package.json`
- `website/package.json`
- `website/package-lock.json`
- `plugins/hermes-achievements/LICENSE`
- `plugins/security-guidance/LICENSE`

## Findings

- Top-level license type verified from local `LICENSE`: MIT.
- Copyright notice in top-level `LICENSE`: `(c) 2025 Nous Research`.
- `pyproject.toml` also declares `license = {text = "MIT"}`.
- The prior MIT assumption is verified for the top-level repository snapshot audited.
- Python packaging evidence: `pyproject.toml`, `uv.lock`, `setup.py`.
- Frontend/package-manager evidence: root `package.json` and `package-lock.json`, plus package files in `apps/`, `web/`, `website/`, `ui-tui/`, and `scripts/whatsapp-bridge/`.
- Hermes uses exact-pinned core Python dependencies in `pyproject.toml`.
- The repository contains many optional integration dependencies and plugin packages. Those increase supply-chain and configuration risk even when not active.

## Major Runtime Dependencies Observed

Core Python runtime dependencies include:

- Model/API/runtime: `openai`, `httpx[socks]`, `requests`, `websockets`, `fastapi`, `uvicorn[standard]`
- Agent/config/UI: `rich`, `prompt_toolkit`, `pydantic`, `pyyaml`, `ruamel.yaml`, `jinja2`
- Scheduling and persistence helpers: `croniter`, `psutil`, `filelock`
- Security/network helpers: `certifi`, `PyJWT[crypto]`, `urllib3`
- Terminal/browser/media helpers: `ptyprocess`, `pywinpty`, `Pillow`

Optional dependency groups include:

- Cloud/model providers: `anthropic`, `mistral`, `boto3`/Bedrock, Azure identity, Google/Gemini-related packages, provider plugins under `plugins/model-providers/`
- Web/search/browser: `exa`, `firecrawl`, `parallel-web`, browser plugins under `plugins/browser/`
- Messaging: Telegram, Discord, Slack, Matrix, SMS, Teams, Home Assistant, DingTalk, Feishu, WeCom, and others
- Remote execution: `modal`, `daytona`
- Voice/media: `edge-tts`, transcription/TTS and YouTube/media integrations

## Evidence Paths

- `LICENSE`
- `pyproject.toml`
- `uv.lock`
- `package.json`
- `apps/desktop/package.json`
- `web/package.json`
- `website/package.json`
- `scripts/whatsapp-bridge/package.json`
- `plugins/model-providers/*/plugin.yaml`
- `plugins/platforms/*/plugin.yaml`

## Confidence Level

Medium-high. Top-level license and direct manifest evidence are clear. Full transitive dependency license analysis was not performed.

## Risks

- Optional integrations cover many external services; each may introduce separate terms, credentials, and supply-chain exposure.
- Node subprojects and plugin subtrees need separate dependency/license scans before any fork baseline is accepted.
- Optional provider and messaging dependencies could be dormant in a governed fork, but must still be removed or pinned if packaged.
- Plugin license files exist and should not be assumed identical without legal review.

## Open Questions

- Which Hermes subprojects would be retained in a Sprint 4 fork package?
- Should the governed fork vendor no optional integrations until explicitly approved?
- Should dependency review be repeated with an SBOM tool during Antigravity validation?

## Recommendation

Treat the MIT assumption as verified for the top-level audited snapshot, but require a separate dependency and plugin license review before any Sprint 4 fork ships or bundles Hermes code.
