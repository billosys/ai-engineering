# v4.0 Implementation Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice05-implementation-plan-synthesis
artifact: v40-implementation-plan
status: proposed-done
planned-source-home: knowledge/concept-card-method/
release-claim: none
```

## Purpose

This implementation plan composes the verified Arc05 planning outputs into a
future source-edit plan for the v4.0 concept-card method skill. It preserves
the accepted Arc03 conceptual model and accepted Arc04 skill architecture while
staying planning only.

This artifact is implementation planning, not source implementation. It does
not edit source, does not create generated zips, is not release evidence, does
not claim release readiness, and leaves source edits remain deferred to a
future implementation effort.

## Verified Inputs

| Input | Status | Implementation consequence |
|-------|--------|----------------------------|
| Slice01 source-surface inventory | verified by CDC | Plan against the source checkout at `/Users/oubiwann/lab/billosys/ai-engineering`, existing `knowledge/`, README, Makefile, package list, package-path, generated zip, and version-history surfaces. |
| Slice02 source layout plan | verified by CDC | Implement under `knowledge/concept-card-method/` with a thin `SKILL.md` and package-compatible `guides/` tree. |
| Slice03 schema and validation plan | verified by CDC | Use Markdown records with YAML frontmatter, lowercase snake_case vocabulary, and documentation-only validator scope for the first implementation. |
| Slice04 package and release plan | verified by CDC | Add package and discoverability support through Makefile, package list, README, generated zip verification, package-path checks, installability checks, and source version history. |

## Preserved Arc03 Decisions

The implementation must keep these accepted Arc03 conceptual model constructs
distinct:

- concept card;
- claim;
- source support;
- source span and source locator;
- relationship edge;
- competency question;
- extraction run;
- validation result;
- verification result;
- reconciliation result;
- preservation decision;
- memory admission.

The future source implementation must not collapse evidence grade, extraction
confidence, verification state, reconciliation state, validation result, or
memory admission into one confidence field.

## Preserved Arc04 Decisions

The implementation must preserve these accepted Arc04 skill architecture
decisions:

- `SKILL.md` is a thin entrypoint with reason to load, positive load, negative
  load, problem ownership, dependency direction, and guide routing.
- The skill owns concept-card method representation and routes project
  management, generic source reading, domain correctness, source edits, and
  implementation planning to adjacent guidance.
- Guides remain concern-based: load/routing, operator workflow, extraction,
  re-extraction and preservation, evidence lifecycle, graph/CQ,
  reconciliation, validation/verification, memory admission, and maintenance
  and packaging.
- Templates preserve user-authored, trace record, and result record surface
  classes.
- Examples include minimal card, claim-backed card, CQ coverage,
  relationship edge, extraction-run trace, reconciliation, memory admission,
  and five-agent default recipe unless explicitly deferred.
- The five-agent workflow remains a default recipe, not an invariant.
- Validation remains split across deterministic structural checks, semantic
  audit, human/operator review, and deferred runtime checks.

## Source Implementation Shape

Future implementation should create these source surfaces:

- `knowledge/concept-card-method/SKILL.md`;
- `knowledge/concept-card-method/guides/01-load-contract.md`;
- `knowledge/concept-card-method/guides/02-operator-workflow.md`;
- `knowledge/concept-card-method/guides/03-extraction.md`;
- `knowledge/concept-card-method/guides/04-re-extraction-preservation.md`;
- `knowledge/concept-card-method/guides/05-evidence-lifecycle.md`;
- `knowledge/concept-card-method/guides/06-graph-cq.md`;
- `knowledge/concept-card-method/guides/07-reconciliation.md`;
- `knowledge/concept-card-method/guides/08-validation-verification.md`;
- `knowledge/concept-card-method/guides/09-memory-admission.md`;
- `knowledge/concept-card-method/guides/10-maintenance-packaging.md`;
- `knowledge/concept-card-method/guides/templates/*.md`;
- `knowledge/concept-card-method/guides/examples/*.md`;
- `knowledge/concept-card-method/guides/validation/*.md`;
- `knowledge/concept-card-method/guides/reference/*.md`.

Templates, examples, validation documentation, and support documents stay
under `guides/` so the package can use the existing `SKILL.md` plus sibling
guides behavior.

## Package and Discoverability Shape

Future implementation should add the concept-card method to source package
and discoverability surfaces:

- README/library discoverability entry for `knowledge/concept-card-method/`;
- `Makefile` target `concept-card-method`;
- generated zip `concept-card-method.zip`;
- package list entry in `INSTALL_ZIPS`;
- skill check entry in `ALL_SKILL_FILES`;
- `.PHONY`, `skills`, help, install, uninstall, clean, and package-path
  behavior consistent with existing skill packages;
- package-path policy that avoids exception rows unless links are deliberately
  source-only or excluded.

## Release and Evidence Boundary

The implementation plan supports Arc05 composition rows A-6, A-7, A-8, and
A-9:

- A-6: accepted Arc04 layout, guide, template, example, schema, enum,
  validation, validator-code, implementation slice, and source edit sequence
  decisions are preserved.
- A-7: README, library discoverability, Makefile, package list, package-path,
  generated zip, tests, release gates, version history, source edit, and
  planning-only boundaries are covered.
- A-8: runtime systems, GraphRAG, graph database, ontology database, memory
  runtime, CCDP service, live extraction, release readiness, later owner, and
  deferred work are explicitly out of scope.
- A-9: the source-edit boundary remains intact until a later implementation
  plan explicitly authorizes source edits.

## Out of Scope

Out of scope for this artifact: source implementation, source edits, generated
zips, package release, release readiness, executable validator-code, runtime
services, GraphRAG, graph database, ontology database, memory runtime, CCDP
service, live extraction, CI changes, and generated release artifacts.

## Close Input

After CDC verifies Slice05, Arc05 is ready for formal arc close. Arc05 close
must still reproduce its own composition rows; this Slice05 plan supports that
close but does not close Arc05 or Project03 by itself.
