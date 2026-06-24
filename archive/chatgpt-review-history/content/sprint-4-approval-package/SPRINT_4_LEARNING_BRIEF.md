# SPRINT_4_LEARNING_BRIEF.md
# Magna Enso — Sprint 4 Learning Brief
# Type: Local-only approval package (educational)
# Date: 2026-06-17
# Audience: Human owner learning professional software delivery while building Magna.

---

## 1. What a "clean governed fork baseline" means

A **baseline** is the first known-good starting point of your codebase. A **fork** is taking someone else's
project as your starting point. **Clean** = you do not blindly copy everything; you take only what you need,
record where it came from, and strip what is dangerous. **Governed** = before anything can *run*, it is
bounded by your safety rules (default-deny, capability states). So a *clean governed fork baseline* is:
"a minimal, provenance-tracked, danger-stripped starting point that is safe by construction and not yet live."

## 2. Fork vs. copy vs. vendor import vs. reference-only

| Approach | What it is | Best when |
|---|---|---|
| **Full fork** | Take the whole upstream repo as yours and diverge | You will heavily reuse and maintain most of it |
| **Shallow copy** | Copy files in, lose upstream git history | Quick, but weak provenance — avoid for a base |
| **Selective vendor import** | Copy *only chosen* modules into a `vendor/` area, with provenance recorded | You want a *minimal* surface and clear traceability |
| **Reference-only** | Don't import; just read it where it sits | You only need to learn from it |
| **Submodule** | Link upstream repo as a nested git pointer | You want to track upstream exactly, accept coupling |
| **Patch-based fork** | Keep upstream pristine + apply your changes as patches | You want auditable, reversible divergence |

For a *minimal, danger-stripped, highly-reviewable* base, **selective vendor import** usually wins:
you bring in only retained modules, record provenance, and never carry the dangerous ones.

## 3. Why removing dangerous modules can be safer than disabling them

"Disabled" code is still *present* — it can be re-enabled by a flag, reached by a forgotten path, or
imported by mistake (Sprint 2 found Hermes reaches capabilities by many paths). **Removed** code is *gone* —
there is nothing to re-enable or bypass. For the worst surfaces (remote execution, messaging, dynamic
plugins, autonomous self-improvement), removal eliminates the risk entirely; disabling only *reduces* it.
Rule of thumb: remove what you will never want in MVP; disable what you might want later but not now.

## 4. Why provenance matters

**Provenance** = a precise record of what you took, from where, at exactly which version (commit SHA). It
lets you: reproduce the baseline, track upstream security fixes, prove what your fork is based on, and audit
license obligations. Without it, you cannot answer "where did this code come from?" — which is unacceptable
for anything you ship. The first baseline commit must name the Hermes source repo + SHA `33b1d144`.

## 5. Why SBOM / license review matters

An **SBOM** (Software Bill of Materials) lists every component and dependency you ship and its license. You
need it because: (a) licenses carry obligations (MIT needs attribution; copyleft may force you to open-source
more than you intend); (b) dependencies can have vulnerabilities; (c) Terms of Service on bundled providers
can restrict use. Reviewing licenses/SBOM **before** committing source prevents legal and security debt that
is painful to unwind later. (Sprint 2 verified top-level MIT, but the *transitive* review is still open — R-02.)

## 6. Why governance must precede runtime execution

If you make code *run* first and add safety later, every gap between "runs" and "governed" is a live
vulnerability. Magna's sequence is deliberate: **design governance (Sprint 3) → build a danger-stripped,
non-running baseline (Sprint 4) → implement enforcement (Sprint 5) → only then allow gated execution.** You
never give a system the ability to act before you can bound and prove what it may do.

## 7. The through-line

Sprint 4 is "bring in the minimum, prove where it came from, strip the dangerous parts, and keep it switched
off." It turns an audited *candidate* into a governed *baseline* — without ever letting it act.
