# 09 — UX & Surface Assessment

> **UI presence does not prove a complete user workflow.** Marks below separate
> *surface exists* from *real backend connectivity* from *validated workflow*.

## 1. magna-command-center — the only product with a real UI today

**Approved shell (HAB-01, ✅ landed, "frozen 10-tab"):** Command (`/`), Identity,
Agents, Memory, Explorer, Cognition, Cosmos, Help, Settings, System (Blueprint §4).

| Surface | Exists | Real backend | Validation evidence |
|---|---|---|---|
| Command (router + System Tool) | ✅ | ✅ (router, Ollama, System Tool) | "manual UI verification passed" (status doc); `verify_command_router.mjs` |
| Identity (CSF-01 self-model) | ✅ | ✅ | `test_csf_01_command_integration` |
| Agents & roles | ✅ | ✅ | `test_agent_permission_profiles` |
| Memory / traceability | 🟡 partial | 🟡 read-only recall | Blueprint §5 "🟡 partial" |
| Explorer (Cognitive Architecture Explorer) | ✅ | ✅ read-only viz | `test_cognitive_explorer`; status doc §1 |
| Cognition / Observatory (Implementation Index) | ✅ | ✅ | Blueprint §5 "clickable deep-links" |
| Cosmos chronicle | ✅ | ✅ | Blueprint §5 |
| Help / Settings / System | ✅ | ✅ | `test_system_routes`, `test_provider_settings` |
| **Magna Presence** (3D avatar) | ✅ | 🟡 (presence signals, event-fed) | `layer-20/21-*` branches + docs; "presence RC freeze" tag/branch |
| Permission Center | 🟡 foundation | 🟡 | `v0.10.5-permission-center-foundation-stable`; Blueprint calls it "planned control surface" |
| Voice (push-to-talk) | ✅ but ⏸ deferred | 🟡 | `v0.10-voice-push-to-talk-stable`; no wake-word |
| Web search UI | 🟡 mock | ⬜ live (mock only) | README; `test_web_search_agent` |
| Mobile / LAN remote | ⏸ deferred | ⬜ | Blueprint §5 |

**Design system:** Tailwind 4 + Framer Motion + Three.js; `MAGNA_VISUAL_LANGUAGE.md`;
the `magna-aesthetic` skill governs visual quality. Heavy investment in cinematic
presence (many `layer-21-*` screenshot/cinematic tuning branches).

**States (empty/loading/error/approval/recovery):** approval + authorization-UX states
are evidenced (`test_authorization_ux`, `test_approval_visibility`); other states not
individually verified. **Accessibility:** no a11y evidence found — *Not confirmed.*
**Responsive:** mobile/LAN deferred; responsive behavior *Not confirmed.*

**UX debt / missing specs:** mobile/voice deferred; Permission Center only foundational;
web search visual-only; no a11y evidence; two product names historically ("Magna
Command Center" being retired to "Magna").

## 2. magna-enso — no UI yet

The **Capability Control UI (Observatory)** is **Sprint 13, PLANNED**. Today Enso has
**no user-facing surface** — only governance documents and (uncommitted) backend policy
code. Target UX (sprint plan §S13): capability list + policy state, pending-approval
queue, schedule proposals, memory/skill review, evidence/Light Curve browser, prominent
"human approves here" controls; a11y pass required at S13. **Status: NOT STARTED.**

## 3. TRACE — developer-facing dashboard

React + Vite + Tailwind dashboard (`src/ui/`): live tool timeline, durations,
context-rot gauge, evidence browser, approximate-ROI panel. Real backend (FastAPI SSE).
Target users = developers running AI sessions. Status: CURRENT (v1 alpha); not re-run.

## 4. Target users & journeys

- **Magna / Enso:** a single owner (Vinay) — plan/validate/evolve work via bounded
  workers with explicit approvals. Single-user, local-first.
- **TRACE:** developers + AI agents wanting context-rot prevention + ROI observability.

## 5. Real-vs-mock summary

| Behaviour | Reality |
|---|---|
| Local model chat (Ollama) | Real |
| Saved runs → tasks, review/scoring | Real (gated) |
| Web search | **Mock/stub by default** |
| Cloud review/OpenAI | Real but **opt-in only** |
| Voice | Real but **deferred/push-to-talk only** |
| Enso Capability Control UI | **Does not exist** |
| Presence avatar | Real rendering; "presence signals" partially event-fed |

**Bottom line:** the only validated end-user workflows are in magna-command-center, and
even there validation is **manual/self-reported**, not reproduced here.
