# Source Migration Register

| Source | Current classification | Action |
|---|---|---|
| `AGENTS.md` | Canonical entry, stale rules | Replace through GOV-001 |
| Model bridge files | Useful, stale roles | Keep thin and revise |
| `trace/` operating instance | Canonical framework, stale state/paths | Retain and revise |
| `../planning/*` references | Missing from repository | Replace with repository-native sources |
| `../../ChatGPTReview/*` | Historical local staging | Stop using as operational source |
| Corrected architecture/spec package | Accepted migration input | Integrate in a dedicated architecture PR |
| Corrected diagram package | Accepted editable/visual input | Integrate curated Draw.io/SVG/HTML in a dedicated PR |
| Draft/correction ZIPs | Generated transport artifacts | Do not commit |
| Raw render logs/scripts | Reproducible but noisy | Store as Actions artifacts when needed |
| Current ChatGPT project sources | Duplicated operating guidance | Replace later with a thin GitHub bootstrap |
| Sprint 1-4 Light Curves | Historical accepted evidence | Retain unchanged |
| Untracked Sprint 5 files | Unreviewed implementation | Keep outside GOV-001; review separately |

Nothing is deleted solely because it is redundant. Canonical replacement and traceable
supersession must exist first.

