# Current Workflow Evaluation

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice02-current-workflow-evaluation
status: proposed-done
architecture-decisions: none
evaluation-status: analytical, non-final, not accepted architecture
scope: current monolith only
```

## Input Contract

This evaluation consumes the verified Slice01 input contract:

- Slice01 CDC verification:
  `../slice01-usage-surface-instrument/cdc-verification.md`
- Slice01 functional-analysis method:
  `../slice01-usage-surface-instrument/artifacts/functional-analysis-method.md`
- Slice01 usage-surface inventory:
  `../slice01-usage-surface-instrument/artifacts/usage-surface-inventory.md`
- Slice01 scenario matrix:
  `../slice01-usage-surface-instrument/artifacts/scenario-matrix.md`
- Slice01 Arc03 input register:
  `../slice01-usage-surface-instrument/artifacts/arc03-input-register.md`
- Arc02 close evidence:
  `../../arc02-conceptual-analysis/closing-report.md`

It also consumes Arc02's conceptual model, boundary and naming findings, and
Arc04 operator decision register as background. Those inputs are analytical and
non-final. This Slice02 evaluation records how the current monolith behaves; it
does not decide final breakout architecture. Architecture deferred to Arc04
after Arc03 closes and operator acceptance occurs.

Source evidence was read from the implementation checkout at
`/Users/oubiwann/lab/billosys/ai-engineering` on source commit `b5e55c5`.
No source files were edited.

## Scenario Evaluation Rows

| Scenario ID | Actor | Entrypoint | Trigger | Inputs | Expected outcome | Load set | Dependencies | Friction signals | Evidence collected | Downstream owner |
|-------------|-------|------------|---------|--------|------------------|----------|--------------|------------------|--------------------|------------------|
| S-01 current monolith source/package | Human source reader | `README.md` | direct source-clone reading after clone | README, source tree, Makefile target list | Reader can tell source clone, packaged skill, unzipped install, and CCDP package modes apart. | README collaboration-framework overview, build/install section, repository layout, CCDP section, Makefile targets, package-path exceptions. | Project01 and `project01-harmonise-paths` path gates before package claims. | Medium context cost; source/package ambiguity is mostly controlled but spread across README, Makefile, CCDP README, and exceptions; package-local link behavior is visible only after reading validation material. | `README.md:150`, `README.md:240`, `README.md:278`, `README.md:329`, `README.md:342`; `Makefile:52`, `Makefile:216`, `Makefile:254`; `package-path-exceptions.tsv:8`; `protocols/ccdp/README.md:3`. | Slice02 records current behavior; Slice04 and Arc05 should consume package/release gate evidence. |
| S-02 current monolith LLM skill loading | Active LLM | top-level `SKILL.md` or `/collaboration-framework` | session start | SKILL routing table and required load guidance | LLM gets posture/process floor and routes to PM, ledger, audit, coverage, delegation, or contribution as needed. | Top-level SKILL frontmatter, inline posture/practice summary, Notes for Codex, framework-file routing table, relevant operational guide. | Posture before methodology; PM wayfinder before planning; ledger before ledgered close. | High context cost because the composer carries substantial inline posture and practice; routing is strong, but the top-level load path is over-rich for narrow operational triggers and can hide dependency order unless the routed file is loaded. | `SKILL.md:69`, `SKILL.md:90`, `SKILL.md:106`, `SKILL.md:326`, `SKILL.md:327`, `SKILL.md:328`; `docs/AI-ENGINEERING-METHODOLOGY.md:17`. | Slice03 should compare standalone and composed load sets; Arc04 should decide top-level composer contract. |
| S-03 planning workflow | CC, CDC, or operator | `docs/PROJECT-MANAGEMENT.md` | planning a project, arc, or slice | PM wayfinder, PM split files, ledger discipline | Actor can open planning work with canonical files and artifact home. | PM wayfinder, canonical planning worktree guide, top-down planning guide, slice close guide, arc close plan-change section, ledger discipline. | PM layout before open set; ledger before acceptance criteria; slice close before arc bubble-up. | Medium to high context cost and dependency-order friction; the wayfinder controls discoverability, but a fresh actor still must load multiple split files to perform a close safely. | `docs/PROJECT-MANAGEMENT.md:35`, `docs/PROJECT-MANAGEMENT.md:47`, `docs/pm/02-canonical-planning-worktree.md:54`, `docs/pm/03-planning-top-down.md:80`, `docs/pm/04-closing-slices.md:14`, `templates/LEDGER-DISCIPLINE.md:174`. | Slice02 records current monolith load behavior; Slice03 tests PM family granularity. |
| S-04 execution workflow | CC | slice `cc-prompt.md` | execution requested by operator | slice plan, ledger, source checkout | CC can execute slice without source/planning confusion and reports CC-attested close. | Slice `cc-prompt.md`, `slice-plan.md`, `ledger.md`, planning AGENTS, source AGENTS, source files as read-only or writable according to prompt. | Source checkout scope from prompt and AGENTS; ledger rows before implementation; artifact home before writing durable outputs. | Role-language clarity is adequate when AGENTS and methodology adapters are loaded; source/package mode ambiguity remains a risk when prompts mention both planning and source checkouts. | This Slice02 prompt names planning worktree, read-only source checkout, no source edits, Project02-only planning scope, and artifact home. Source `AGENTS.md` and planning `AGENTS.md` both distinguish planning from main. `docs/AI-ENGINEERING-METHODOLOGY.md:23`, `docs/AI-ENGINEERING-METHODOLOGY.md:31`, `docs/AI-ENGINEERING-METHODOLOGY.md:77`. | Slice02 records; Slice04 should carry role-language and source/package requirements into architecture inputs. |
| S-05 review workflow | CDC or fresh verifier | `closing-report.md` and `ledger.md` | proposed-done slice | artifacts, ledger, diff, close report | Reviewer reproduces rows and writes CDC verification. | Ledger discipline, PM slice close guide, close report, artifact inventory, staged or committed diff. | Ledger evidence semantics before close review; PM bubble-up check after row reproduction. | Review load is intentionally high; friction comes from attested/reproduced vocabulary, row-count checks, and the need to inspect both artifacts and diff. The current monolith controls inherited claim acceptance through ledger discipline. | `templates/LEDGER-DISCIPLINE.md:150`, `templates/LEDGER-DISCIPLINE.md:198`, `templates/LEDGER-DISCIPLINE.md:214`; `docs/pm/04-closing-slices.md:36`; Slice01 CDC verification demonstrates this path. | Slice02 records; Slice04 should preserve CDC verification requirements in functional synthesis. |
| S-06 slice close and arc close composition | CDC and operator | PM close files and arc ledger | slice or final arc slice closes | child close reports, arc ledger, artifacts | Slice close bubbles up to arc; arc close reproduces composition. | PM slice close guide, PM arc close guide, ledger discipline, child close reports, arc `ledger.md`. | Ledger owns evidence semantics; PM owns lifecycle routing and plan-change discipline. | Unclear handoff risk is real but documented: PM tells where close and bubble-up live, while ledger owns verification mechanics. Inherited-composition risk is explicitly named and controlled at arc/project scale. | `docs/pm/04-closing-slices.md:8`, `docs/pm/04-closing-slices.md:63`, `docs/pm/05-closing-arcs.md:13`, `templates/LEDGER-DISCIPLINE.md:142`, `templates/LEDGER-DISCIPLINE.md:302`. | Slice02 records; Slice03 tests ledger/PM composition; Slice04 carries composition risk forward. |
| S-07 audit standalone component | User and active LLM | `docs/CODE-AUDIT.md` | audit requested | README, project context, domain skills | Audit remains diagnosis-only and writes scoped workbench outputs unless a ledgered slice overrides to artifacts. | Code-audit prompt, repo README, local instruction file, architecture/design docs when discoverable, detected domain skills, audit map. | Domain skill loading after audit map; evidence access before severity; diagnosis before follow-up fixes. | Strong audit contract, but current load path is over-rich for a quick audit and under-adapted for Codex/AGENTS because the source prompt still names `CLAUDE.md`; output-location conflict exists between audit `workbench/` defaults and slice-local `artifacts/` unless the slice prompt overrides it. | `docs/CODE-AUDIT.md:8`, `docs/CODE-AUDIT.md:25`, `docs/CODE-AUDIT.md:71`, `docs/CODE-AUDIT.md:134`, `docs/CODE-AUDIT.md:354`; `SKILL.md:328`. | Slice02 records; Slice03 should compare audit as a standalone operational component; Arc04/Arc05 must resolve output and adapter behavior. |

## Required Usage Surface Coverage

- README/source-clone: covered by S-01. Current README gives human
  orientation, package build/install commands, repository layout, and CCDP
  contrast. It is useful but dense.
- packaged skill: covered by S-01 and S-02. The package path is visible through
  `make collab-framework`, `make install`, `CF_FILES`, and package-path
  validation.
- LLM skill loading: covered by S-02. The current top-level skill is usable as
  a monolithic composer but costly for narrow triggers.
- session start: covered by S-02. The posture and methodology floor is strong,
  but the current monolith loads more than some sessions need.
- planning: covered by S-03. The PM wayfinder plus split files are coherent
  when loaded in order.
- execution: covered by S-04. Slice prompts plus AGENTS rules preserve planning
  versus source checkout boundaries.
- review: covered by S-05. CDC verification is well specified by ledger and PM
  close mechanics.
- slice close: covered by S-05 and S-06. Close reports require row walks,
  artifact inventories, silent-drop diffs, and bubble-up.
- arc close: covered by S-06. Composition must be reproduced at arc scale.
- audit: covered by S-07. The audit prompt is diagnosis-only and multi-scale,
  with a default `workbench/` output location.
- coverage: current behavior is source-grounded as a related surface. The
  guide has Codex notes and says the historical Claude Code/Cargo examples
  must be adapted to repo tooling; detailed standalone testing belongs to
  Slice03.
- delegation: current behavior is source-grounded as a related surface. The
  policy cleanly distinguishes thinking work from lookup work, and Codex notes
  are present.
- contribution: current behavior is source-grounded as a related surface.
  Style and template are mutually dependent; template-only use is under-served.
- source/package: covered by S-01 and the package notes artifact. The current
  source distinguishes source clone, generated skill zip, unzipped installed
  skill, and CCDP package, but the distinction is distributed.
- role-language: covered by S-04 and the package notes artifact. Current
  role-language clarity is strongest when top-level SKILL, methodology, PM,
  ledger, and AGENTS adapters are available together.

## Current Monolith Finding Summary

The current monolith works as a composed framework entrypoint. It gives humans
and LLMs a single visible `/collaboration-framework` route, preserves the
posture/process floor, and routes to PM, ledger, audit, coverage, delegation,
and contribution surfaces.

Its functional pressure is load shape. Narrow workflows often need one
discipline but must first pass through a rich composer or know the exact source
document. The strongest current friction categories are high context cost at
session start, dependency-order friction in PM/ledger close, source/package
mode distributed across README/Makefile/package checks, role-language adapter
scatter, and audit output-location conflict.

This evaluation is analytical and non-final. It evaluates the current monolith
only, does not decide component boundaries, and leaves final architecture
deferred to Arc04 after Arc03 functional analysis and operator acceptance.
