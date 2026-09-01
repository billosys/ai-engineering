# Skill Kind and Topology Classification Matrix

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice03-skill-topology-classification
artifact: skill-kind-topology-classification-matrix
artifact-status: slice classification evidence
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-head-observed: 5b796c3
created-on: 2026-09-01
source-files-edited: false
```

## Classification Boundary

This matrix classifies current and planned surfaces for Arc01 evidence. It is
not Arc02's directory contract and not Arc05's final public wording.

Current packaged rows are source-backed by the live source checkout, Slice01
inventory, README routes, `knowledge/*/SKILL*.md`, and `Makefile` package
targets. Planned rows are explicitly marked as planned Project02 or planned
Project03 and are not live source.

## Current Packaged Source-Backed Surfaces

| Surface | Current/planned status | Kind classification | Topology classification | Evidence | Confidence | Caveats or re-entry conditions | Arc02 source-root or package-root implication |
|---------|------------------------|---------------------|-------------------------|----------|------------|-------------------------------|----------------------------------------------|
| `knowledge/rust/` | current packaged, source-backed | domain/tooling | candidate atomic | `knowledge/rust/SKILL.md`, `rust-guidelines.zip`, README says Rust has 661 patterns, and Slice01 names Rust as the candidate atomic anchor. | high | Reopen if Rust becomes a router over independently loadable Rust subskills. | Strong anchor for `knowledge/` as skill substrate; package root can remain frontmatter name even if source root stays `knowledge/rust/`. |
| `knowledge/go/` | current packaged, source-backed | domain/tooling | atomic | `knowledge/go/SKILL.md`, `go-guidelines.zip`, README describes one Go practice/toolchain skill. | high | Reopen if Go splits into language, server, tooling, or style-guide subskills with independent packages. | Supports one source root, one skill entrypoint, one package root pattern. |
| `knowledge/cpp/` | current packaged, source-backed | domain/tooling | atomic | `knowledge/cpp/SKILL.md`, `cpp-guidelines.zip`, guides plus source/provenance and tools; README describes C++ Core Guidelines coverage. | high | Source import/provenance and tools are secondary roles, not composition by themselves. Reopen if tooling becomes separately loadable. | Keep provenance and tools visible as source-only or package-excluded surfaces if root moves. |
| `knowledge/js/` | current packaged, source-backed | domain/tooling | atomic with bridge/integration pressure | `knowledge/js/SKILL.md`, `javascript-deno-guidelines.zip`, README describes JavaScript/Deno, Deno-first, Biome-adjacent guidance. | medium | JS/Deno/Biome is an edge case because language, runtime, and linter surfaces are adjacent. Reopen if JS, Deno runtime, and Biome become separate required load units. | Arc02 should avoid making adjacency imply one composite package unless package evidence changes. |
| `knowledge/erlang/` | current packaged, source-backed | domain/tooling | atomic | `knowledge/erlang/SKILL.md`, `erlang-guidelines.zip`, guides, concept-cards, sources, tools, and workbench for Erlang/OTP. | high | Workbench and tools are provenance/support roles; they do not make the skill composite unless exposed as independent load units. | Preserve source-only workbench distinction if `knowledge/` anatomy changes. |
| `knowledge/cobalt/` | current packaged, source-backed | domain/tooling | atomic | `knowledge/cobalt/SKILL.md`, `cobalt-guidelines.zip`, README describes one Cobalt static-site-generation toolchain. | high | Liquid/Rust context is supporting knowledge, not necessarily a second loadable component. | Fits current `pack_skill` package behavior. |
| `knowledge/design/` | current packaged, source-backed | domain/tooling | atomic with cross-domain caveat | `knowledge/design/SKILL.md`, `visual-design-system.zip`, README describes a visual design system grounded in perceptual science, color, type, layout, and CSS practice. | medium/high | Broad interdisciplinary sources do not make it composite unless the skill routes across independent design/science/CSS components. | Supports `knowledge/` as source substrate for broad domains, not only programming languages. |
| `knowledge/tailwindcss/` | current packaged, source-backed | domain/tooling | atomic | `knowledge/tailwindcss/SKILL.md`, `tailwindcss.zip`, README describes Tailwind CSS v4 configuration and migration guidance. | high | Reopen if Tailwind becomes part of a larger CSS framework router. | Straightforward one source root, one entrypoint, one package. |
| `knowledge/deno/` | current packaged, source-backed | domain/tooling | atomic | `knowledge/deno/SKILL-js-linter.md`, `deno-js-linter.zip`, README describes Deno lint's 70 language-level rules. | high | Complements Biome but does not require Biome to satisfy its lint-rule load reason. | Package root differs from source root and follows skill frontmatter name. |
| `knowledge/biome/` | current packaged, source-backed | domain/tooling | composite source root; atomic package entries | `knowledge/biome/` has `SKILL-js-linter.md` and `SKILL-web-linter.md`; `make biome` emits `biome-js-linter.zip` and `biome-linter.zip`. | high for root composite; medium for each package atomicity | Biome is the main edge case: one source root contains two installable entrypoints and guide subtrees. Reopen if Arc02 decides source roots must equal package roots. | Arc02 must decide whether multiple entrypoints under one `knowledge/` root remain valid or require package-root/source-root separation rules. |
| top-level `SKILL.md` / current `collaboration-framework` | current packaged, source-backed | framework/operational | accepted composite | Source `SKILL.md` frontmatter name is `collaboration-framework`; `CF_FILES` packages top-level `SKILL.md`, framework docs, PM docs, and templates; README calls it the daily-driver composer over component disciplines. | high | Current source is monolithic selected-file bundle. Reopen after Project02 component source roots land. | Arc02 must preserve composer behavior while deciding whether framework source moves under `knowledge/`, top-level component roots, or another contract. |

## Planned Project02 Framework Components

These are planned Project02 surfaces from accepted architecture and
implementation-planning artifacts. They are not live source and not yet current
packaged source-backed surfaces.

| Surface | Current/planned status | Kind classification | Topology classification | Evidence | Confidence | Caveats or re-entry conditions | Arc02 source-root or package-root implication |
|---------|------------------------|---------------------|-------------------------|----------|------------|-------------------------------|----------------------------------------------|
| `collaboration-framework` | planned Project02; partially current as top-level composer | framework/operational | composite | Operator-accepted architecture keeps it as daily-driver composer over seven specialist components. | high | Reopen only if implementation removes specialist routing, which would conflict with accepted Project02 facts. | Preserve `collaboration-framework.zip` and installed route while deciding source-root home. |
| `engineering-methods` | planned Project02, not live source | framework/operational with method/gate role | bridge/integration layer | Accepted owner of methodology, process, operational routing, component-boundary analysis, ontology critique, and source/package/release gates. | medium/high | May classify atomic if implementation presents one coherent engineering-methods load reason; may classify composite if it becomes a router over methods. | Strong Arc02 stress case for whether framework/method source belongs under `knowledge/` or top-level component roots. |
| `project-management` | planned Project02, not live source | framework/operational | atomic operational method | Owns project -> arc -> slice lifecycle, planning layout, top-down planning, close/bubble-up, confirmation, anti-patterns, and examples. | medium/high | Depends on `work-verification`, but dependency does not make it composite unless routing becomes identity-defining. | Source root should preserve PM guide sequence and example ownership. |
| `work-verification` | planned Project02, not live source | framework/operational; support/template secondary | atomic operational method | Owns ledger discipline, evidence strength, row closure, silent-drop checks, independent verification, and `LEDGER-DISCIPLINE.md`. | medium/high | Template support is secondary. Reopen if it becomes a broader evidence framework over multiple independent packages. | Needs package-local template handling and version-history preservation. |
| `testing` | planned Project02, not live source | framework/operational | atomic with expansion caveat | Accepted as broader testing component containing coverage hardening and future TDD guidance. | medium | Reopen if testing becomes a composite router across coverage, TDD, CI, and domain-specific validators. | Arc02 should allow future guide growth without overfitting to old coverage prompt name. |
| `code-auditing` | planned Project02, not live source | framework/operational; method | atomic operational method | Accepted diagnosis-only audit component with stage/scale guidance and audit-to-hardening handoff. | high | Handoff to `testing` is adjacent routing, not enough for composite classification. | Preserve diagnosis-only identity and avoid merging into testing. |
| `agent-coordination` | planned Project02, not live source | framework/operational | bridge/integration layer | Accepted owner of CC/CDC/operator terminology, delegation decisions, context packets, result integration, and multi-assistant failure modes. | medium/high | May remain bridge rather than composite if it connects actors and surfaces without packaging subcomponents. | Arc02 should provide a source root that can name roles without absorbing PM or verification. |
| `contribution-style` | planned Project02, not live source | framework/operational; support/template secondary | atomic operational method | Accepted owner of contribution voice, upstream ticket workflow, and `CONTRIBUTION-TICKET.md`. | high | Template support remains secondary unless ticket templates become an independent package. | Needs package-local template placement if separated from top-level `templates/`. |

## Planned Project03 Method Skill

| Surface | Current/planned status | Kind classification | Topology classification | Evidence | Confidence | Caveats or re-entry conditions | Arc02 source-root or package-root implication |
|---------|------------------------|---------------------|-------------------------|----------|------------|-------------------------------|----------------------------------------------|
| `concept-card-method` | planned Project03, not yet implemented, not live source | method | provisional atomic method with composite pressure | Project03 plans `knowledge/concept-card-method/`, thin `SKILL.md`, focused `guides/`, templates, examples, validation documentation, memory admission guidance, and CCDP-adjacent boundaries. | medium | Borderline edge case. Reopen if implementation makes ontology engineering, source extraction, validation/audit, memory admission, and CCDP routing independent required components rather than internal method concerns. | Arc02 should decide whether planned method skills live under `knowledge/` and whether package-compatible `guides/` subdirectories remain the method-skill convention. |

## Protocol and Templates/Support Surfaces

| Surface | Current/planned status | Kind classification | Topology classification | Evidence | Confidence | Caveats or re-entry conditions | Arc02 source-root or package-root implication |
|---------|------------------------|---------------------|-------------------------|----------|------------|-------------------------------|----------------------------------------------|
| CCDP / `protocols/ccdp/` | current protocol/package, source-backed | protocol/package | bridge/integration layer | README says CCDP is packaged separately, not an installable skill zip; Makefile has `ccdp-package` and `check-ccdp-package`; Slice02 preserves CCDP separation. | high | Do not classify as skill package unless a future protocol decision accepts that change. | Keep under `protocols/` or provide docs wrappers; do not let skill package roots absorb CCDP accidentally. |
| `templates/GUIDE.md` | current templates/support, source-backed | support/template | atomic support template | Source `templates/` contains `GUIDE.md`; README routes new-guide contributors to it. | high | Reopen if Project04 moves it under an owning method/component or turns it into generated docs. | Arc02 must decide whether cross-cutting templates remain top-level or move under owning knowledge roots. |
| `templates/LEDGER-DISCIPLINE.md` | current templates/support, source-backed | framework/operational plus support/template | atomic operational method/support surface | Bundled by `CF_FILES`; Slice01 classifies it as work-verification and template/support; Project02 plans it under `work-verification/templates/`. | high | Reopen after Project02 source implementation decides whether the full protocol remains template payload or guide content. | Likely owned by `work-verification`; preserve package-local links and version history. |
| `templates/CONTRIBUTION-TICKET.md` | current templates/support, source-backed | support/template plus framework/operational | atomic support template | Bundled by `CF_FILES`; paired with contribution style; Project02 plans it under `contribution-style/templates/`. | high | Reopen if contribution templates become multiple independently loadable ticket-writing surfaces. | Likely owned by `contribution-style`; preserve source provenance if moved. |

## Edge Case Conclusions

- Rust is the candidate atomic anchor because it is a current source-backed
  domain/tooling skill with one coherent load reason, one source entrypoint,
  and one package root.
- `collaboration-framework` is the accepted composite anchor because its
  source and Project02 architecture make daily-driver composition its identity.
- `concept-card-method` is a method skill edge case: current evidence supports
  provisional atomic method classification, but the classification is
  borderline because validation, memory admission, graph/CQ, ontology, and
  CCDP-adjacent concerns could become independent components in a future
  implementation.
- Biome is a package/source-root edge case: the source root is composite
  because it contains two packaged skills, while each package can still behave
  atomically for its own linter load reason.
- JS/Deno/Biome is a category adjacency edge case: JavaScript/Deno guidance,
  Deno lint, and Biome linting are adjacent and sometimes cross-referenced,
  but current packages remain separately loadable.
- CCDP is not a skill kind here. It is a protocol/package bridge with separate
  package validation.
- templates/support surfaces should be described as support unless an accepted
  skill entrypoint and package behavior make them loadable skills.

## Arc02 Inputs

Arc02 must decide:

- whether current and planned skill source roots live under `knowledge/` even
  for framework/operational and method kinds;
- whether atomic and composite skill source roots share one source-root
  convention;
- whether generated package roots should match source roots, frontmatter
  names, or selected-file package roots;
- how to handle multi-entrypoint source roots such as `knowledge/biome/`;
- which top-level templates remain cross-cutting versus move under owning
  component or method roots;
- how README, `docs/`, and `SKILL.md` routes describe current versus planned
  surfaces without overclaiming implementation state;
- how CCDP stays a separate protocol/package surface while remaining linked
  from relevant docs and methods.
