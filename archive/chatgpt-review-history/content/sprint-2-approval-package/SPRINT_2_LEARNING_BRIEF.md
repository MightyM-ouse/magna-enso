# SPRINT_2_LEARNING_BRIEF.md
# Magna Enso — Sprint 2 Learning Brief
# Type: Local-only approval package (educational)
# Date: 2026-06-17
# Audience: Human owner learning professional software delivery while building Magna.

---

## 1. Why this brief exists

You asked to learn professional software delivery as we build. Sprint 2 is a perfect teaching moment:
it is how mature teams evaluate **adopting someone else's code as a foundation** without taking on hidden
risk. This brief explains the concepts; the other files apply them.

## 2. Why Sprint 2 exists (the principle)

> You never build on a dependency you have not audited.

Hermes is a *candidate* base. Before betting the Magna Enso runtime on it (Sprint 4), a professional team
first answers: What is it? What does it do? What does it touch? What does it cost us legally and
operationally? Sprint 2 buys that knowledge cheaply (reading) before the expensive commitment (forking).

## 3. What a "read-only audit" means

- **Read-only** = you look but do not change. You clone into a throwaway workspace, inspect, and write
  findings. You never edit, build, run, or ship the audited code.
- **Why separate workspace?** So the thing you are studying can never accidentally contaminate the thing
  you are building. The audited clone is disposable; your product repo stays pristine.
- **Professional analogy:** due diligence before an acquisition. You inspect the books; you do not yet
  merge the companies.

## 4. Why external dependency provenance matters

**Provenance** = knowing exactly where code came from and at what version.
- Record the **source repository URL** and the exact **commit SHA** you audited.
- Without provenance you cannot reproduce findings, track upstream security fixes, or prove what you based
  your fork on. The Sprint 4 baseline's first commit must state the Hermes source + SHA.
- Lesson: *"works on my machine" is not provenance; a pinned commit hash is.*

## 5. How open-source reuse is evaluated

A professional reuse assessment weighs four things:
1. **License** — does the license permit your use, and what must you do in return (e.g. MIT requires
   preserving the copyright/permission notice)? Incompatible or copyleft terms can block reuse.
2. **Architecture fit** — does its structure map cleanly onto what you need (here: can each capability be
   placed behind a Magna policy gate)?
3. **Risk surface** — what does it touch that is dangerous (network exposure, autonomous execution,
   memory/skill writes, cloud providers)?
4. **Maintenance cost** — forking means you own upstream-sync, security patches, and divergence forever
   (Risk R-11).

The output is a **keep / rebuild / exclude** decision per module — not "clone it all".

## 6. How to avoid scope creep

**Scope creep** = a task quietly growing beyond its remit. Classic Sprint 2 creep would be: "while I'm in
here, let me fix / refactor / start wiring it in." Guards:
- A written non-goals list (`SPRINT_2_SCOPE_AND_BOUNDARIES.md` §2).
- "Reports only; stop after audit reports" in the approval block.
- A reviewer (Antigravity) who checks that nothing beyond the audit happened.
- TRACE evidence that records exactly what was done, making creep visible.

## 7. How to protect the main repo

- Audit in a **sibling/throwaway** location (`_scratch/`), never inside `magna-enso/`.
- **No Hermes source** committed to the product repo.
- **No commits/pushes** during the audit.
- `.gitignore` + scratch-outside-repo means even an accidental copy cannot be tracked.
- Lesson: *the integrity of your baseline is a feature; defend it structurally, not just by intention.*

## 8. How to document evidence like a professional team

- **One question → one report → one conclusion**, each citing exactly what was inspected (file paths +
  commit SHA), so a reviewer can reproduce it.
- Separate **facts** (what the code does) from **judgments** (whether it is suitable) — state confidence levels.
- End with a **Light Curve** (evidence package) and pause for **human sign-off** — no self-approval.
- Honest data contract: what you observed is real; anything estimated is labeled as an estimate.

## 9. The through-line

Sprint 2 teaches the discipline that makes Sprint 4 safe: **investigate before you commit, document so
others can verify, and never let the thing you're studying touch the thing you're shipping.**
