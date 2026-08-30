# Source Package And Role-Language Notes

```yaml
project: project02-collab-breakout
arc: arc03-functional-analysis
slice: slice02-current-workflow-evaluation
status: proposed-done
architecture-decisions: none
notes-status: analytical, non-final, not accepted architecture
scope: current monolith only
```

## Input Contract

These notes consume the Slice01 functional-analysis method, usage-surface
inventory, scenario matrix, Arc03 input register, Slice01 CDC verification,
and Arc02 close evidence as the input contract for current-monolith
source/package and role-language evaluation.

Project01 and `project01-harmonise-paths` remain cross-cutting constraints:
source/package language, package-local link behavior, zip root behavior,
release surface behavior, CCDP contrast, `make check-package-paths`,
component contract fields, and package/release gate implications must travel
into Arc04 and Arc05.

## Source/Package Findings

| ID | Surface | Current behavior | Finding | Evidence basis | Downstream implication |
|----|---------|------------------|---------|----------------|------------------------|
| SPR-01 | source/package orientation | README distinguishes source repo, installable skill zips, unzipped Codex install, and CCDP protocol package. | Current source/package behavior is explicit enough for the current monolith, but the explanation is distributed across README sections. | `README.md:150`, `README.md:240`, `README.md:264`, `README.md:278`, `README.md:329`, `README.md:342`. | Arc04 component contracts should repeat package mode fields; Arc05 should update README without making it a second composer. |
| SPR-02 | package-local link behavior | The collaboration-framework bundle stages `SKILL.md`, framework docs, PM split files, and templates so relative links resolve inside the package. | Package-local behavior is implemented by explicit `CF_FILES`, not a broad docs glob. This is good for package precision but creates a maintenance point for every component split. | `Makefile:75`, `Makefile:86`, `Makefile:108`, `Makefile:113`, `Makefile:123`. | Arc04 must define support assets and package files per component; Arc05 must update Makefile lists. |
| SPR-03 | zip root behavior | Skill zips wrap contents under a package name matching frontmatter; CCDP zip uses one `ccdp/` root. | Zip root behavior is clear today and should become a component contract field for future standalone packages. | `Makefile:4`, `Makefile:9`, `Makefile:80`, `Makefile:254`, `Makefile:279`; `protocols/ccdp/README.md:3`. | Arc04/Arc05 should require named zip roots and entrypoints for every accepted component. |
| SPR-04 | release surface behavior | README documents `make all`, `make skills`, `make collab-framework`, `make install`, `make check-package-paths`, and separate CCDP package commands. | Release surface behavior is usable, but source README, package README, and Make targets must stay synchronized after breakout. | `README.md:248`, `README.md:268`, `README.md:278`, `README.md:287`, `Makefile:52`, `Makefile:64`, `Makefile:216`. | Arc05 implementation plan needs README, SKILL, Makefile, and package-path verification gates. |
| SPR-05 | CCDP contrast | CCDP is documented and packaged separately from installable skills. | CCDP contrast is a current strength: it prevents protocol package behavior from being mistaken for collaboration-framework skill component behavior. | `README.md:278`, `README.md:313`, `protocols/ccdp/README.md:3`, `protocols/ccdp/README.md:22`, `protocols/ccdp/README.md:32`. | Arc04 should keep CCDP as contrast and package/release gate input, not as a framework component. |
| SPR-06 | `make check-package-paths` | The Make target builds skill zips and validates Markdown paths with exceptions. | `make check-package-paths` is the current package/release gate for installable skills. The exception file already distinguishes source-only/provenance placeholders from package-local paths. | `Makefile:216`, `scripts/check-package-paths:421`, `scripts/check-package-paths:451`, `scripts/check-package-paths:528`, `package-path-exceptions.tsv:8`. | Arc04 must require gate strategy; Arc05 must make each component's package paths checkable. |
| SPR-07 | component contract implications | No per-component source/package contract exists yet because the framework is still monolithic. | Component contract fields are a missing current structure, not a current source defect. The needed fields are source path, package path, entrypoint, support assets, dependency links, package-local behavior, zip root, release gates, and version-history owner. | Arc02 BNF-09, BNF-14, D-10, D-11; Project02 DoD. | Arc04 owns accepted contract shape; Arc05 owns implementation slices and checks. |

## Role-Language Findings

| ID | Surface | Current role-language behavior | Finding | Evidence basis | Downstream implication |
|----|---------|--------------------------------|---------|----------------|------------------------|
| RLF-01 | top-level SKILL | The top-level skill maps CDC to Codex Desktop, CC to Codex CLI, and unqualified Claude references to the active model instance. | Current role-language clarity is strong when the top-level composer is loaded. | `SKILL.md:69`, `SKILL.md:326`; `docs/AI-ENGINEERING-METHODOLOGY.md:23`, `docs/AI-ENGINEERING-METHODOLOGY.md:31`, `docs/AI-ENGINEERING-METHODOLOGY.md:37`. | Slice03 should test whether standalone components need local notes. |
| RLF-02 | PM and ledger | PM and ledger docs each include Codex notes preserving canonical filenames, CDC/CC roles, and evidence-strength discipline. | Role language is adequate for planning, review, verifier, and reviewer flows when PM and ledger are both loaded. | `docs/PROJECT-MANAGEMENT.md:19`, `templates/LEDGER-DISCIPLINE.md:48`, `docs/pm/04-closing-slices.md:8`. | Arc04 should preserve dependency direction: ledger owns evidence terms; PM owns lifecycle routing. |
| RLF-03 | source AGENTS and planning AGENTS | The implementation and planning worktrees both distinguish source checkout work from planning-branch work. | Operator and fresh-context users get clear checkout routing when AGENTS files are loaded. | Source `AGENTS.md` and planning `AGENTS.md` read during this slice; Slice02 prompt repeats the split. | Arc05 should preserve AGENTS/CLAUDE compatibility during source edits. |
| RLF-04 | audit | The audit prompt still names `CLAUDE.md` in project-context preparation and lacks a local Codex/AGENTS adapter. | Audit is the weakest current role-language clarity surface for a direct fresh-context Codex load. | `docs/CODE-AUDIT.md:25`, `SKILL.md:328`. | Slice03 should test audit standalone component notes; Arc04 should decide adapter ownership. |
| RLF-05 | coverage | The coverage guide has explicit Notes for Codex saying the title is historical and commands are Rust/Cargo-shaped examples. | Coverage direct load is better adapted than its title suggests, but the title still creates discoverability and role-language friction. | `docs/CLAUDE-CODE-COVERAGE.md:1`, `docs/CLAUDE-CODE-COVERAGE.md:7`, `docs/CLAUDE-CODE-COVERAGE.md:10`, `docs/CLAUDE-CODE-COVERAGE.md:12`. | Arc04 should choose surface-neutral naming or compatibility wrapper. |
| RLF-06 | delegation | Delegation policy includes a Codex Desktop / Codex CLI section and preserves the thinking versus lookup line. | Role-language clarity is good for delegation, though the document title and audience remain Claude-oriented. | `docs/SUBAGENT-DELEGATION-POLICY.md:9`, `docs/SUBAGENT-DELEGATION-POLICY.md:76`, `docs/SUBAGENT-DELEGATION-POLICY.md:90`. | Slice03 should test whether local notes are enough for standalone use. |
| RLF-07 | contribution | Contribution style and template are mostly role-neutral, but they still reference Claude-era source paths in places. | Contribution guidance is clear for operator and maintainer-facing work if style and template travel together. | `docs/CONTRIBUTION-STYLE.md:33`, `docs/CONTRIBUTION-STYLE.md:43`, `templates/CONTRIBUTION-TICKET.md:3`, `templates/CONTRIBUTION-TICKET.md:200`. | Arc04 should package the template as a support asset with role-neutral entry guidance. |
| RLF-08 | fresh-context use | Fresh-context actors can succeed if they start from top-level SKILL, AGENTS, PM wayfinder, or prompt. | Fresh-context role-language clarity becomes weaker when a single deep guide is loaded without its adapter chain. | Slice01 US-03, US-07, US-08; current source role adapters above. | Arc04 should decide central adapter plus short local component notes or another drift-controlled pattern. |

## Current Conclusion

The current monolith carries Project01 and `project01-harmonise-paths`
source/package constraints well enough for present use: package-local links,
zip roots, release surface distinctions, CCDP contrast, and
`make check-package-paths` are all visible and testable. The gap is future
component contract form, not present monolith usability.

Role-language clarity is also adequate in composed use: CDC, CC, Claude,
Codex, operator, verifier, reviewer, and fresh-context roles are interpretable
when the top-level composer or planning prompt is loaded. The weak point is
standalone direct loading of older or specialized documents, especially audit
and coverage. That weak point belongs to Slice03 and Arc04; this artifact
does not decide final architecture.
