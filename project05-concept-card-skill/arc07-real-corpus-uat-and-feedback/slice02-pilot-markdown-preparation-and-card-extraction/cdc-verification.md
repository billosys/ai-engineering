# CDC Verification: Slice02 Pilot Markdown Preparation And Card Extraction

```yaml
project: project05-concept-card-skill
arc: arc07-real-corpus-uat-and-feedback
slice: slice02-pilot-markdown-preparation-and-card-extraction
status: verified-closed
verified-by: Codex CDC
verified-on: 2026-09-11
cc-planning-commit: 8bfa080
```

## Verdict

Slice02 is verified closed. The slice acquired the pinned corpus outside the
planning tree, prepared only the declared Chapter 1 and Chapter 7 pilot sample,
produced a bounded four-card candidate packet with source-support records, and
captured seven feedback findings for Slice03 disposition.

No source skill, package, graph/RAG/MCP surface, memory runtime, or vendored
corpus content changed in this slice.

## Reproduced Checks

| Check | Result | Evidence |
| --- | --- | --- |
| Planning commit scope | pass | `git show --name-status 8bfa080 -- .../slice02...` shows Slice02 planning artifacts, ledger, slice plan, and closing report only. |
| Pinned checkout identity | pass | `/private/tmp/project05-compcogneuro-book-e0c697b4` resolves `HEAD` to `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d` and tree `894b3e10baa38e9d9c29a2e52b64f4d0ffb1378a`; checkout status is clean. |
| Source and figure hashes | pass | SHA-256 values for `chapter-01.md`, `chapter-07.md`, `figures/fig_gears.png`, and `figures/fig_patsep_clr.png` match `source-acquisition.md` and `locator-map.md`. |
| Pilot scope | pass | Manifest, structure map, locator map, and scoped artifact search cover only declared Chapter 1 and Chapter 7 sample material; no other chapter file references were found in Slice02 artifacts. |
| Source spans | pass with caveat | Recorded line ranges resolve in the pinned checkout and support the candidate topics. Long Markdown paragraph lines make some ranges broad; this is already captured by locator/readiness caveats and finding F-1. |
| Prepared-source evidence | pass | Manifest, structure map, locator map, and readiness report preserve snapshot identity, line/heading locators, dependency observations, readiness limit, and citation/cross-reference caveats. |
| Candidate packet shape | pass | Exactly four `cc-*.md` files and four `support-*.md` files exist under `candidate-cards/`; all eight frontmatters parse as concept-card or source-support records. |
| Lifecycle boundaries | pass | Candidate records keep verification, reconciliation, preservation, operator acceptance, and memory admission unassessed or absent; review packet states no operator review occurred. |
| Dependency handling | pass | Gear and pattern-separation figure assets are hashed and directly inspected; `@Marr71`, `@MarshallHelgadottirMolleEtAl06`, and Executive Function cross-reference dependencies remain caveated. |
| Friction handoff | pass | `friction-log.md` records F-1 through F-7 with areas, severity, observations, and suggested Slice03 disposition routes. |
| Hygiene | pass | `git diff --check 8bfa080^ 8bfa080 -- .../slice02...` passed; source and planning worktrees were clean before CDC closeout edits. |

## Row Verification

| Row | CDC status | Evidence |
| --- | --- | --- |
| S2-1 | done | Pinned checkout, tree, clean status, sampled file hashes, and non-vendoring statement reproduced. |
| S2-2 | done | Declared Chapter 1 and Chapter 7 pilot scope reproduced from manifest/maps and scoped search. |
| S2-3 | done | Prepared-source records preserve locators, dependencies, readiness, and caveats for the bounded sample. |
| S2-4 | done | Four candidate cards and four support records parse, remain reviewable, and preserve lifecycle distinctions. |
| S2-5 | done | Figure inspection and citation/cross-reference caveats are explicit rather than silently promoted. |
| S2-6 | done | Review packet cleanly separates generated candidates from operator acceptance, verification, and memory admission. |
| S2-7 | done | Seven findings are captured for Slice03; none is treated as accepted defect or silently dropped. |
| S2-8 | done | Diff/status checks confirm planning-only scope and no runtime/source-skill changes. |

## Bubble-Up To Arc07

Slice02 delivers Arc07 row A7-3: the pilot generation exercised
`document-extraction` and `concept-cards` on representative real source
material and produced inspectable preparation evidence, candidate-card records,
and friction findings.

The seven findings in `friction-log.md` require Slice03 disposition. The
current Arc07 plan already assigns Slice03 to convert pilot findings into
accepted skill/template/example updates or explicit no-op/follow-on decisions,
so no arc-plan scope change is required before opening Slice03.

The silent-drop diff is clean: Slice02 did not widen into whole-corpus
generation, bibliography resolution, operator card acceptance, runtime
ingestion, graph/RAG/MCP implementation, or source-skill edits.
