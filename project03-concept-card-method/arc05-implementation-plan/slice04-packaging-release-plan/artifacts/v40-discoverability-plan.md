# v4.0 Discoverability Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice04-packaging-release-plan
artifact: v40-discoverability-plan
status: proposed-done
planned-source-home: knowledge/concept-card-method/
```

## Purpose

This artifact plans README and skill library discoverability requirements for
the v4.0 concept-card method skill. It preserves the verified Slice02
package-compatible `guides/` layout and the verified Slice03
documentation-only validator-code scope.

This plan does not edit source, does not write README/library prose, does not
build generated zips, does not perform package release, does not claim release
readiness, does not implement executable validator-code, and does not create
runtime services, GraphRAG, graph database, ontology database, memory runtime,
CCDP service, or live extraction behavior.

## README Requirements

Future README updates should add the concept-card method skill to the skill
library section and package target documentation.

README discoverability requirements:

- add a skill library entry for `knowledge/concept-card-method/`;
- update the count of knowledge skills if the README states a count;
- describe the skill as the v4.0 concept-card method for extraction,
  re-extraction, source support, evidence lifecycle, graph/CQ semantics,
  reconciliation, validation/review boundaries, and memory admission;
- mention `concept-card-method.zip` as the package artifact once package
  implementation exists;
- list `make concept-card-method` in package target examples once accepted;
- include `make check-skills` and `make check-package-paths` as expected
  verification surfaces;
- preserve the promise boundary: documentation-only validator guidance does
  not imply executable validator-code, generated zips, package release,
  release readiness, runtime services, GraphRAG, graph database, ontology
  database, memory runtime, CCDP service, or live extraction behavior.

## Skill Library Text

Skill library text should make the reason to load explicit:

> Use concept-card-method when creating, revising, auditing, reconciling,
> validating, verifying, or planning concept-card material as a
> provenance-bearing knowledge substrate.

The future README entry should be short enough to fit beside existing skill
library descriptions while naming the method boundary and adjacent routing.

## SKILL.md Metadata Requirements

Future `knowledge/concept-card-method/SKILL.md` frontmatter should include:

- `name: concept-card-method`;
- a description that names the reason to load, concept-card method ownership,
  and primary output surfaces;
- metadata tags such as `concept-cards`, `knowledge-substrate`, `provenance`,
  `evidence`, `validation`, `reconciliation`, `competency-questions`, and
  `memory-admission`;
- category metadata consistent with the repository's skill library;
- version metadata consistent with the source version-history plan.

The description should not promise executable validator-code, generated zip
availability, package release, release readiness, runtime services, GraphRAG,
graph database, ontology database, memory runtime, CCDP service, or live
extraction behavior before implementation evidence exists.

## Adjacent-Skill Routing

Discoverability text should route adjacent responsibilities clearly:

- collaboration-framework owns posture, project management, ledger
  discipline, closing mechanics, audits, and contribution style;
- domain skills own language or domain correctness;
- source-reading practice owns faithful evidence capture from primary
  material;
- Arc05 implementation planning owns source edit sequence, package mechanics,
  generated archive checks, release gates, and source version history;
- concept-card-method owns concept-card representation, source support,
  evidence lifecycle, graph/CQ method surfaces, reconciliation, validation
  guidance, review boundaries, and memory admission method guidance.

## Operator Package Expectations

Operator-facing package expectation text should say:

- the source skill home is `knowledge/concept-card-method/`;
- the package artifact is planned as `concept-card-method.zip`;
- packaged surfaces are the thin SKILL.md plus `guides/`, including templates,
  examples, validation documentation, and support documents under `guides/`;
- `make check-skills` validates SKILL.md description length;
- `make check-package-paths` validates package-context Markdown links inside
  generated archives;
- documentation-only validator scope means validation guidance is packaged as
  documentation, not executable validator-code.

## Later-Slice Routing

Slice05 owns implementation-plan synthesis, implementation slice
recommendations, deferral register, source edit sequence, and Project03 close
input.

Slice04 found no discoverability fact that requires Arc05 re-sequencing, a new
slice, or a scope correction.
