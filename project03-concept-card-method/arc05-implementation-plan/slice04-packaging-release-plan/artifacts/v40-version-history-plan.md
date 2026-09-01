# v4.0 Version History Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice04-packaging-release-plan
artifact: v40-version-history-plan
status: proposed-done
```

## Purpose

This artifact plans source version-history obligations for the future
implementation of the v4.0 concept-card method skill. It names which source
files need local version history or enclosing source version-history updates.

This plan does not edit source, does not write source version-history text,
does not build generated zips, does not perform package release, does not
claim release readiness, does not implement executable validator-code, and
does not create runtime services, GraphRAG, graph database, ontology database,
memory runtime, CCDP service, or live extraction behavior.

## Version History Obligations

| Source surface | Version history obligation | Owner |
|----------------|----------------------------|-------|
| `knowledge/concept-card-method/SKILL.md` | Add local version history for v4.0 skill creation, load contract, guide routing, package promise boundary, and documentation-only validator scope. | Future implementation |
| guide files | Each guide should either include local version history or be covered by the SKILL.md version history entry if the repository chooses thin per-guide docs. | Future implementation |
| template files | Template creation and schema/enum commitments should be recorded in local template version history or an enclosing SKILL.md/source version-history entry. | Future implementation |
| example files | Release-critical example creation should be recorded in local example version history or an enclosing source version-history entry. | Future implementation |
| validation documentation | Structural candidates, semantic boundary, human/operator boundary, and deferred runtime checks need version history coverage because they define validator and review promises. | Future implementation |
| support document files | Field glossary, source locator notes, review checklist, and change-log notes need local or enclosing version history coverage if added. | Future implementation |
| `README.md` | README version history or an appropriate repository-level history entry should record skill library and package target discoverability changes. | Future implementation |
| `Makefile` | If the Makefile has no local version history section, record package target and package list changes in the enclosing source version-history surface selected by the implementation owner. | Future implementation |
| `package-path-exceptions.tsv` | Any package-path exception row must carry source and expires fields; if the file has no local history, record the package-path exception rationale in the enclosing version history. | Future implementation |

## Source Version-History Policy

Source version-history updates should record:

- what changed;
- which Arc05 slice or implementation slice required it;
- why the change was needed;
- whether the change affects package behavior, discoverability, validation,
  release gates, or promise boundaries;
- whether executable validator-code remains deferred.

If a source file has no local version history section, the implementation plan
should name the enclosing source version-history location before source edits
begin.

## Surface-Specific Notes

SKILL.md:

- record the initial v4.0 concept-card-method skill version;
- mention the thin SKILL.md route and adjacent-skill boundary;
- mention the documentation-only validator scope if executable validator-code
  remains deferred.

Guide files:

- record initial guide creation by concern area;
- preserve the Slice02 guide split;
- record later changes that alter operator workflow, evidence lifecycle,
  graph/CQ treatment, validation, reconciliation, or memory admission.

Template and example files:

- record schema and enum commitments from Slice03;
- record example coverage for minimal card, claim-backed card, CQ coverage,
  relationship edge, extraction-run trace, reconciliation, memory admission,
  and five-agent default recipe.

Validation documentation:

- record deterministic structural validation candidates;
- record semantic audit and human/operator review boundaries;
- record deferred runtime checks explicitly.

README, Makefile, and package-path exception surfaces:

- record README/library discoverability changes;
- record Makefile package target and package list changes;
- record package-path exceptions only when unavoidable and justified.

## Later-Slice Routing

Slice05 owns implementation-plan synthesis, implementation slice
recommendations, deferral register, source edit sequence, and Project03 close
input.

Slice04 found no version-history fact that requires Arc05 re-sequencing, a new
slice, or a scope correction.
