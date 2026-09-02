# Arc02 Readiness Packet

```yaml
project: project04-knowledge-library-reorg
arc: arc01-material-inventory
slice: slice04-arc01-synthesis
artifact: arc02-readiness-packet
artifact-status: slice synthesis evidence
created-on: 2026-09-02
source_checkout: /Users/oubiwann/lab/billosys/ai-engineering
source-files-edited: false
```

## Verdict

Arc02 is ready to open after Slice04 is CDC-verified. Arc01 now has a
source-backed evidence base for the target directory contract, but this packet
is not arc close. Formal arc close still needs CDC verification of Slice04 and
an Arc01 composition check against `arc01-material-inventory/ledger.md`.

Arc02 can now decide the target contract for `docs/`, `knowledge/`,
`templates/`, `protocols/`, README, `SKILL.md`, package roots, validation
gates, compatibility surfaces, and migration sequencing. Arc02 should treat
this packet as decision substrate, not as permission to edit the source
checkout.

## Consumed Verified Evidence

| Slice | Verified close evidence | Required artifacts consumed | What the evidence contributes |
|-------|-------------------------|-----------------------------|-------------------------------|
| Slice01 | `arc01-material-inventory/slice01-source-surface-inventory/cdc-verification.md` records `status: verified-closed` and reproduced all seven ledger rows. | `current-source-surface-map.md`, `material-role-classification.md`, `source-validation-surface-map.md`. | Current source-backed inventory for `README.md`, `SKILL.md`, `docs/`, `knowledge/`, `templates/`, `protocols/`, `Makefile`, package-path exceptions, validation scripts, compatibility files, generated zips, `site/`, `assets/`, and `workbench/`. |
| Slice02 | `arc01-material-inventory/slice02-imported-architecture-integration/cdc-verification.md` records `status: verified-closed` and reproduced all seven ledger rows. | `imported-architecture-evidence-map.md`, `prior-proposal-register.md`, `project04-integration-conflicts-and-questions.md`. | Separates Project02 accepted facts, Project02 implementation-plan hypotheses, Project03 method-skill facts, compatibility obligations, conflicts, open questions, and re-entry conditions. |
| Slice03 | `arc01-material-inventory/slice03-skill-topology-classification/cdc-verification.md` records `status: verified-closed` and reproduced all seven ledger rows. | `skill-kind-topology-decision-instrument.md`, `skill-kind-topology-classification-matrix.md`, `public-language-implications.md`. | Provides the tested skill-kind and topology instrument, classifications for current packaged skills and planned surfaces, edge cases, public-language risks, and the external ontology rubric boundary. |

The external ontology rubric is also consumed as project-level input from
`artifacts/external-ontology-rubric-research.md`. It remains tested input, not
accepted taxonomy.

## Current Source-Backed Facts

These facts come from the live source inventory, not from prior planning alone.

- `docs/` is currently mixed: framework/operational source, method material,
  extraction guidance, design/dev history, and some end-user documentation all
  live there. Arc02 must not assume `docs/` is already only user-facing.
- `knowledge/` currently holds packaged domain/tooling skill substrate:
  Rust, Go, C++, JavaScript/Deno, Erlang/OTP, Cobalt, Visual Design, Tailwind
  CSS, Deno lint, and Biome linting.
- `knowledge/biome/` is a current source-backed edge case because one source
  root has two package entrypoints and two generated package roots.
- The top-level `SKILL.md` is the current `collaboration-framework` entrypoint
  and is packaged through selected `docs/` and `templates/` files, not through a
  `knowledge/<slug>/` source-root convention.
- `templates/` contains reusable support payloads. Two current templates are
  part of the framework package payload through `CF_FILES`.
- `protocols/ccdp/` is a current protocol/package surface with separate
  package behavior and separate validation from installable skill zips.
- `README.md`, `SKILL.md`, `AGENTS.md`, `CLAUDE.md`, `Makefile`,
  `package-path-exceptions.tsv`, generated package roots, `scripts/`, and
  package-local links are compatibility and validation surfaces that must move
  together with any accepted directory contract.
- No current validator encodes explicit `atomic` or `composite` metadata.
  Existing checks validate entrypoint frontmatter, package roots, package-local
  links, package exceptions, and CCDP package shape.

## Project02 Accepted Facts

Project02 facts that Arc02 must preserve:

- `collaboration-framework` remains the daily-driver composer and accepted
  composite anchor.
- The seven specialist components are `engineering-methods`,
  `project-management`, `work-verification`, `testing`, `code-auditing`,
  `agent-coordination`, and `contribution-style`.
- `engineering-methods` owns methodology, process, operational routing,
  component-boundary analysis, ontology critique placement, and
  source/package/release gates.
- Each component versions as a whole through `SKILL.md` plus sibling
  `version-history.md`.
- Ontology critique belongs inside `engineering-methods` guidance, not as a
  new standalone Project02 component.
- Memory admission is future research, not a Project02 component.
- CCDP remains a separate protocol distribution, not a collaboration-framework
  component and not an installable skill package, unless a later protocol
  package decision explicitly reopens that policy.

## Project02 Implementation-Plan Hypotheses

These are useful prior plans, but Arc02 must test them against Project04 before
source edits:

- Top-level component roots such as `engineering-methods/` and
  `project-management/`.
- Generated specialist component zips, `COMPONENT_ZIPS`, `INSTALL_ZIPS`,
  `ALL_SKILL_FILES`, package roots, and Makefile targets.
- Package root names matching component names.
- README reader-mode language for source checkout, generated zip,
  unzipped/install, and installed skill use.
- Migration sequencing that creates compatibility before removing old paths,
  repairs package-local links before adding package-path exceptions, and keeps
  generated zips as validation outputs rather than committed planning
  artifacts.
- Compatibility handling for the current top-level `SKILL.md`, old `docs/`
  source paths, framework templates, old prompt names, and source provenance.

## Project03 Planned Surface Facts

Project03 contributes planned surface evidence, not live source evidence:

- `concept-card-method` is a planned method skill and is not live source in
  `/Users/oubiwann/lab/billosys/ai-engineering`.
- Project03 planned a future `knowledge/concept-card-method/` source root,
  thin `SKILL.md`, focused `guides/`, templates, examples, validation docs,
  memory admission guidance, and CCDP-adjacent boundaries.
- Current public language must say planned method skill until source
  implementation and package validation actually exist.
- The method should not be placed under `protocols/` merely because it is
  CCDP-adjacent, and CCDP should not be absorbed into a skill package.

## Skill Kind and Topology Facts

Arc02 should keep kind and topology independent.

- Skill kind answers what the surface is about: domain/tooling,
  framework/operational, method, protocol/package, support/template, or
  source/provenance.
- Topology answers how the surface is composed: atomic, composite,
  bridge/integration layer, or application/task bundle.
- Rust is the current candidate atomic domain/tooling anchor.
- `collaboration-framework` is the accepted composite framework/operational
  anchor.
- `concept-card-method` is a planned method skill with provisional atomic
  method classification and composite pressure.
- Biome is a source-root/package-root edge case: a composite source root with
  atomic package-entry behavior.
- CCDP is a protocol/package bridge, not a skill kind.
- Support templates should remain support surfaces unless an accepted
  `SKILL.md` entrypoint and package behavior make them loadable skills.
- The external ontology rubric remains tested input and should not be
  presented as final public taxonomy.

## Unresolved Decisions For Arc02

Arc02 should decide:

- the exact `docs/` contract: what remains public explanation, what becomes a
  wrapper, and what moves because it is source-like substrate;
- the exact `knowledge/` contract: whether it houses domain/tooling,
  framework/operational, and method skill source roots under one family;
- whether Project02 framework components live under `knowledge/`, top-level
  roots, a framework family root, or another accepted source-root model;
- whether method skills such as planned `concept-card-method` live under
  `knowledge/`;
- whether atomic and composite skill source roots share one convention;
- whether package roots equal source roots, frontmatter names, or selected-file
  package roots;
- how to represent multi-entrypoint roots such as `knowledge/biome/`;
- where cross-cutting templates live after ownership is assigned;
- how CCDP remains a separate protocol/package surface while still being linked
  from user docs and method/framework material;
- which old paths get wrapper docs, migration notes, or package-path exception
  treatment;
- which validations are mandatory for each later implementation slice.

## Source-Edit Risks

- Moving framework source out of `docs/` without repairing `CF_FILES`,
  `SKILL.md`, README routes, package-local links, and package-path exceptions
  can break the current `collaboration-framework.zip`.
- Treating Project02 top-level roots as already accepted for Project04 can
  weaken the `knowledge/` substrate direction before Arc02 decides the
  directory contract.
- Claiming `concept-card-method` as current source can mislead readers because
  the planned surface is not live source.
- Folding CCDP into installable skills can blur protocol package validation and
  skill package validation.
- Collapsing kind into topology can produce false public rules such as
  domain/tooling equals atomic or framework/operational equals composite.
- Adding package-path exceptions before repairing package-local links can hide
  avoidable breakage.
- Moving source-like docs without preserving version history and provenance can
  erase accepted Project02 and Project03 lineage.

## Validation Obligations

Arc02 and later implementation arcs should require source-checkout validation
appropriate to touched surfaces:

- `make check-skills` when `SKILL.md` or `SKILL*.md` paths, frontmatter, or
  `ALL_SKILL_FILES` change.
- `make check-package-paths` after generated skill packages and package-local
  links are updated.
- `make all` after package targets, aggregate package lists, or generated zip
  behavior changes.
- `make collab-framework` when composer files or framework component package
  behavior changes.
- `make ccdp-package` and `make check-ccdp-package` only when CCDP source,
  package contents, README links, or protocol paths change.
- Direct checks of `AGENTS.md` and `CLAUDE.md` symlink intent when compatibility
  instructions move or are rewritten.
- README/docs link checks after public wayfinding changes.
- Diff checks and source checkout status checks for every implementation slice.

## Re-Entry Conditions

Re-enter Project02 architecture only if Arc02 cannot preserve the accepted
component roles, composer behavior, component version histories, or
source/package/release gate ownership under any coherent directory contract.

Re-enter Project03 method architecture only if Arc02 cannot preserve
`concept-card-method` as planned method-skill input without claiming live
source or breaking its thin-entrypoint/focused-guides architecture.

Re-enter CCDP package policy only if keeping CCDP under `protocols/ccdp/` with
separate package validation becomes incompatible with the accepted directory
contract or an explicit later protocol-package decision changes the policy.

Re-enter kind/topology classifications if Arc02 changes source roots,
entrypoint shape, package behavior, component ownership, generated package
roots, or validation behavior in a way that changes load reason or composition
identity.

## Arc01 Composition Evidence

This section prepares Arc01 composition evidence for formal arc close. It is
not arc close.

| Arc01 capability piece | Evidence now available | Composition status |
|------------------------|------------------------|--------------------|
| Current repository material roles | Slice01 verified source surface map, material role classification, and validation surface map. | Prepared: `docs`, `knowledge`, `templates`, `protocols`, `README`, `Makefile`, package-path, and compatibility surfaces are covered. |
| Imported Project02 and Project03 inputs | Slice02 verified evidence map, prior proposal register, and conflicts/questions artifact. | Prepared: accepted facts, working hypotheses, conflicts, and re-entry conditions are separated. |
| Skill kind and topology classification | Slice03 verified decision instrument, classification matrix, and public-language implications. | Prepared: atomic, composite, bridge/integration, application/task bundle, skill kind, and external ontology rubric boundaries are covered. |
| Arc02 readiness | This Slice04 packet, `directory-contract-requirements.md`, and `arc01-synthesis-decision-register.md`. | Pending CDC verification, then ready for the formal arc close composition row. |

Formal arc close should reproduce Arc01 ledger row A-5 after Slice04 is
verified-closed and should not inherit this packet as sufficient closure by
itself.
