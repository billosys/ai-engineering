# Arc01 Synthesis Decision Register

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice04-arc01-synthesis
artifact: arc01-synthesis-decision-register
artifact-status: slice synthesis evidence
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Purpose

This register gives Arc02 decision rows that can become Arc02 ledger rows,
directory contract sections, or migration plan checkpoints. Each row names an
Arc02 decision, options to test, evidence source, what to preserve, risk,
validation obligation, operator decision need, and re-entry condition.

## Decision Register

| ID | Arc02 decision | Options to test | Evidence source | Preserve | Risk | Validation obligation | Operator decision |
|----|----------------|-----------------|-----------------|----------|------|-----------------------|-------------------|
| D-1 | Arc02 decision: define the `docs/` versus `knowledge/` directory contract. | `docs/` as public explanation plus `knowledge/` as substrate; wrapper docs over moved source; limited exceptions for source-like docs. | Slice01 `material-role-classification.md`; Project04 plan; external ontology rubric tested input. | Preserve the operator distinction: `docs/` documents repository materials, while `knowledge/` holds raw and derived substrate where accepted. | Source-like framework or method material may stay hidden in `docs/`, or user docs may absorb source material. | Validate final paths with README/docs link checks, `make check-package-paths`, and source path scans after moves. | Operator decision required for final directory contract and any intentional exceptions. |
| D-2 | Arc02 decision: choose source root placement for Project02 framework/operational components. | `knowledge/<component>/`; top-level component roots; `knowledge/framework/<component>/`; wrapper docs over component roots. | Project02 `operator-accepted-architecture.md`; Slice02 imported architecture map; Slice03 matrix. | Preserve accepted component names, roles, composer behavior, source/package/release gate ownership, and sibling version history. | Prior top-level root hypothesis could override Project04's `knowledge/` substrate direction without review. | Validate source root changes against `SKILL.md`, `ALL_SKILL_FILES`, package roots, and `make check-skills`. | Operator decision required if Arc02 selects a root convention that differs from Project02 implementation hypotheses. |
| D-3 | Arc02 decision: preserve `collaboration-framework` as daily-driver composer while adding specialist components. | Composer package remains installed default; composer-local source root; transitional top-level shim; source checkout route through README/docs. | Project02 accepted architecture; Slice01 current top-level `SKILL.md`; Project02 skill-entrypoint plan. | Preserve `collaboration-framework` as accepted composite and avoid language that it is deprecated. | Moving the current top-level entrypoint can break source readers or package payloads. | `make collab-framework`, `make check-skills`, `make check-package-paths`, and installed route wording review. | Operator decision needed for top-level `SKILL.md` compatibility shim or removal policy. |
| D-4 | Arc02 decision: decide method skill source root policy for planned `concept-card-method`. | `knowledge/concept-card-method/`; method family under `knowledge/`; separate top-level method root; defer until implementation. | Slice02 Project03 method evidence; Slice03 classification matrix; Project03 planning artifacts summarized by Slice02. | Preserve planned surface status: method skill, not live source; thin `SKILL.md`; focused `guides/`; validation distinctions; memory admission as lifecycle gate; CCDP-adjacent boundary. | README or docs may claim `concept-card-method` is available before implementation. | Future package validation with `make check-skills`, `make check-package-paths`, and method-specific structural/semantic/human review gates. | Operator decision needed before public docs describe the method as implemented. |
| D-5 | Arc02 decision: keep skill kind and topology independent in the directory contract. | Directory metadata fields; contract prose; separate source-root and package-root rules; defer final public vocabulary to Arc05. | Slice03 decision instrument; Slice03 public-language implications; external ontology rubric. | Preserve skill kind, topology, atomic, composite, bridge/integration, and application/task bundle as separate concepts. | False rules such as domain/tooling equals atomic or framework/operational equals composite can drive wrong moves. | Verify with targeted wording searches in Arc02 artifacts and later README/docs. | Operator decision needed if Arc02 wants these terms in public-facing docs before Arc05. |
| D-6 | Arc02 decision: define source root versus package root relationship. | Package root equals frontmatter `name:`; package root equals source root; package root equals component name; selected-file package root. | Slice01 Makefile/validator map; Project02 package target plan; Slice03 Biome and composer classifications. | Preserve generated package roots, package-local links, installed skill routes, and current multi-entrypoint realities. | Forcing package root equals source root could break Biome-style roots or selected-file composer packaging. | `make check-package-paths`, generated zip inspection, `ALL_SKILL_FILES`, and `INSTALL_ZIPS` review. | Operator decision required for any intentional source/package name divergence. |
| D-7 | Arc02 decision: decide multi-entrypoint source-root policy for `knowledge/biome/`. | Allow multiple `SKILL*.md` entrypoints in one source root; split package roots into separate source roots; keep common source root with package-local guide subtrees. | Slice01 source map; Slice03 classification matrix. | Preserve current `biome-js-linter` and `biome-linter` behavior or migrate both deliberately. | A one-root-one-package rule would silently misclassify existing source. | Run both Biome package checks through `make check-skills` and `make check-package-paths`. | Operator decision needed if source-root split creates larger migration cost than clarity benefit. |
| D-8 | Arc02 decision: define template ownership and movement. | Keep top-level `templates/`; move templates under owning components; keep top-level wrapper docs; split cross-cutting from owner-local templates. | Slice01 template roles; Project02 file layout; Slice03 support/template rows. | Preserve template provenance and package-local payloads for work-verification and contribution-style. | Top-level templates may stay ambiguous, or owner-local packages may lose template payloads. | Validate `CF_FILES`, component package contents, package-local links, and package-path exceptions. | Operator decision required for any template left top-level as a cross-cutting exception. |
| D-9 | Arc02 decision: preserve CCDP as protocol/package surface. | Keep `protocols/ccdp/`; add user docs wrapper; cross-link from method/framework docs; reopen package policy only explicitly. | Slice01 protocol and validation maps; Slice02 accepted facts; Slice03 public language. | Preserve `protocols/ccdp`, `ccdp.zip`, `make ccdp-package`, `make check-ccdp-package`, source-only exclusions, and protocol status. | CCDP could be accidentally described or packaged as a skill. | Run CCDP package checks only when touched; always keep skill-package checks separate from CCDP checks. | Operator decision required to reopen protocol package policy. |
| D-10 | Arc02 decision: define README, `docs/`, and `SKILL.md` wayfinding responsibility. | README as short orientation; focused `docs/` pages by topic; `SKILL.md` route tables for load behavior; installed skill route wording across packages. | Project04 plan; Project02 README wayfinding plan; Slice03 public-language implications. | Preserve source checkout, generated zip, unzipped/install, installed skill, and CCDP reader modes. | README, docs, and skill entrypoints may duplicate or contradict one another. | README/docs link checks, `make check-package-paths`, and package-local route review. | Operator decision needed for final public wording in Arc05 after source/package evidence exists. |
| D-11 | Arc02 decision: define migration plan sequencing and compatibility gates. | Mechanical moves first; compatibility shims; wrapper docs; Makefile/package updates after payloads exist; exceptions after link repair. | Project02 implementation sequence roadmap; Slice01 validation surface map; Slice02 conflicts/questions. | Preserve provenance, version history, old source path recognition, and explicit source-edit authorization boundaries. | Entangling prose rewrites with moves can hide loss of history or broken links. | Every source implementation slice should run relevant make targets, diff checks, source status checks, and package-path checks. | Operator decision required before source edits begin and for any compatibility shim policy. |
| D-12 | Arc02 decision: choose package-path exception policy. | Zero exceptions after repair; narrow expiring exceptions; accepted warnings with rationale; source-only/provenance classifications. | Project02 package-path link exception plan; Slice01 validation map. | Preserve package-local links as the default and make exceptions visible debt. | Exceptions can hide broken generated package behavior if added too early or too broadly. | `make check-package-paths`, exception-only checks if supported, and generated zip inspection. | Operator decision required for accepted warnings that remain at migration close. |

## Cross-Register Re-Entry Conditions

- Re-enter Project02 if no directory contract can preserve the accepted
  `collaboration-framework` composer, seven specialist components,
  source/package/release gate ownership, component version histories, and CCDP
  separation.
- Re-enter Project03 if Arc02 cannot preserve `concept-card-method` as planned
  method skill input without claiming it is live source.
- Re-enter protocol policy if CCDP can no longer remain a separate
  protocol/package with its own validation under `protocols/ccdp/`.
- Re-enter classification if source root, package root, entrypoint shape,
  generated package behavior, component ownership, or validation behavior
  changes a surface's load reason or composition identity.
- Re-enter migration plan if package-local links cannot be repaired before
  package-path exception rows are needed.

## Source-Edit Risks

- Source-edit risks are highest where a path participates in both user
  wayfinding and generated package behavior: `README`, `SKILL.md`, framework
  docs, `templates/`, `Makefile`, and `package-path-exceptions.tsv`.
- Planned surface rows must remain planned until implementation lands. This is
  especially important for `concept-card-method`, Project02 specialist
  components, and any new package roots.
- Current source-backed facts should not be overwritten by imported hypotheses.
  The directory contract should say when a prior Project02 implementation plan
  is accepted, adjusted, or rejected for Project04.
- The external ontology rubric should stay an evidence source and tested input,
  not accepted taxonomy or final public language.

## Arc01 Composition Notes For Close

Arc01 composition can now be tested by reading Slice01 current source evidence,
Slice02 Project02/Project03 integration evidence, Slice03 skill kind/topology
evidence, and these Slice04 synthesis artifacts together.

This register is not arc close. The formal arc close should verify that
current `docs`, `knowledge`, `templates`, `protocols`, `README`, `Makefile`,
package-path, atomic, composite, Project02, Project03, and Arc02 readiness
claims compose without unresolved silent drops.
