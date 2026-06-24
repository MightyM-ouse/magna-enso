# 13 — Reuse & Clean-Rebuild Assessment

> Classification per asset: **Reuse unchanged · Extract into shared versioned component ·
> Reuse after refactoring · Reimplement from specification · Retain as historical
> evidence only · Reject.** Nothing was copied or moved.

> Context: the question is what the *clean, professionally-designed Magna project* (not
> yet created) should do with existing assets. This assumes decision #3 (program
> identity) resolves toward a clean build — confirm first.

## A. magna-command-center assets

| Asset | Quality / test evidence | Coupling | Provenance/license | Classification | Note |
|---|---|---|---|---|---|
| Governance canon (`project-knowledge/` constitution, REG, COSMOS, PROTO, evolutionary map) | High (mature doctrine) | Low (docs) | Owner-authored | **Reuse after refactoring** → fold into HELIX genome for the clean build | The intellectual core; reconcile with Enso charter |
| Runtime primitives (event bus, workflow/approval engine, orchestration, observability) | Medium-High (tests exist, not re-run) | Medium (FastAPI-coupled) | Owner-authored | **Extract into shared versioned component** (candidate) OR **Reimplement from spec** | Strong design; decide vs Hermes base |
| Risk policy engine + ATM-01 boundary | Medium (tests exist) | Medium | Owner | **Reimplement from specification** | Overlaps Enso `policy/`; pick one canonical engine |
| Provider-neutral adapters (Ollama/OpenAI/web-search) | Medium | Medium | Owner | **Reuse after refactoring** | Useful pattern for Enso model integration |
| CSF-01 self-model | Medium-High (frozen) | Medium | Owner | **Reuse after refactoring** | Identity truth model is reusable doctrine |
| 10-tab shell + Presence avatar (Three.js) | Medium-High (heavy polish) | High (React/Three) | Owner | **Reuse after refactoring** or **Retain as historical evidence** | Big sunk cost; reuse if clean build keeps the shell |
| SQLite persistence + migration phases | Medium | Medium | Owner | **Reimplement from specification** | Schema design reusable; code likely rebuilt |
| Internal task traceability (`prepare/close_task`) | Medium | Medium | Owner | **Reimplement** under TRACE runtime plane | Aligns with TRACE runtime traceability goal |
| `magna_self_heal.sh` hygiene | Low-risk utility | Low | Owner | **Reuse unchanged** | Portable |
| 55+ feature branches, agent-logs | n/a | n/a | Owner | **Retain as historical evidence only** | Don't migrate; archive |

## B. magna-enso assets

| Asset | Quality | Classification | Note |
|---|---|---|---|
| TRACE engineering instance (`trace/`) | High | **Reuse unchanged** | This *is* the governance spine for any clean build |
| Planning package (`planning/`) | High | **Reuse unchanged** | Charter/roadmap/sprint plan/worker model |
| Policy engine (`policy/`, 883 LOC) | Promising design; **unverified, untracked** | **Reuse after refactoring** (after committing + fixing tests C-7 + verifying) | The most valuable new code; do not adopt as-is until green |
| Policy tests | Present but non-runnable | **Reuse after refactoring** | Fix package collision first |
| Inert Hermes baseline | Inert provenance | **Retain as historical evidence only** until a real fork decision | Not runnable |

## C. TRACE assets

| Asset | Classification | Note |
|---|---|---|
| TRACE methodology + blueprint | **Reuse unchanged** | Operating model |
| TRACE dashboard (server+UI) | **Extract into shared versioned component** | Could become the runtime observability surface for Magna if wired in |
| `proposed-governed-loop/` | **Reject or Reimplement** | Untracked/unmerged; evaluate before relying on |

## D. Hermes (external)

| Aspect | Finding | Classification |
|---|---|---|
| Source | NousResearch/Hermes-Agent @ `33b1d14…`, MIT | — |
| Suitability | "Conditionally suitable only" (EH-0013); high-risk surfaces (browser, terminal) | **Reimplement from specification behind the policy gate** (preferred) over wholesale reuse |
| Migration risk | High (network/terminal/browser/autonomy) | Keep inert until policy engine verified |

## E. Cross-cutting recommendation

There are **two policy engines, three traceability systems, and two evolution models**
across the codebases. A clean build should pick **one** of each:
- **One policy engine** — the Enso `policy/` design is the cleaner, safer-by-default
  starting point *once verified*; the command-center risk engine is the more battle-used.
- **One traceability spine** — TRACE (engineering) + a single runtime audit/replay
  surface (merge command-center's replay/lineage strengths into the Enso runtime plane).
- **One evolution narrative** — reconcile Pre-SGN belt ↔ Enso stages (decision #3 + §17).

**Do not copy/move anything until program identity (decision #3) is set.**
