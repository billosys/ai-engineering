# classification evidence synthesis

## Purpose

This synthesis connects current public wording to prior Project04 evidence.
It preserves evidence status boundaries: external ontology rubric research is
tested input, not accepted taxonomy; Arc01 classification is planning evidence;
Arc02 and Arc03 establish source/package layout facts; Arc04 establishes the
current README/docs documentation base.

## External Ontology Rubric

The external ontology rubric says Project04 should classify by discourse
boundary, vocabulary, activities, relations, constraints, bodies of knowledge,
method/practice separation, and integration behavior. It supports a two-axis
model:

- skill kind: what the surface is about
- topology: how the surface composes

Evidence status: not accepted taxonomy. It is an independent rubric used to
avoid circular classification from repository folders alone.

## Arc01 Evidence

Arc01 Slice03 produced the accepted planning evidence for Arc05 to inspect:

- kind axis: domain/tooling, framework/operational, method, protocol/package,
  support/template, source/provenance
- topology axis: atomic, composite, bridge/integration layer,
  application/task bundle
- classification rule: do not collapse kind into topology
- Rust: candidate atomic domain/tooling anchor
- collaboration-framework: accepted composite framework/operational anchor
- concept-card-method: planned Project03 method skill, provisional atomic with
  composite pressure, not live source
- Biome: composite source root with atomic package entries
- CCDP: protocol/package bridge, not a skill package
- templates/support: support unless accepted entrypoint and package behavior
  make them loadable skills

Evidence status: verified-closed Arc01 Slice03 planning evidence, not final
public wording.

## Arc02 Evidence

Arc02 closed with a target directory contract and migration plan. Its closure
records accepted layout, path contract, compatibility, exception, source root,
package root, atomic, composite, docs, knowledge, protocols, templates, and
Arc03 handoff evidence.

Arc02 matters for Arc05 because public vocabulary cannot contradict these
source/package facts:

- docs/ is the human-facing explanation layer
- knowledge/ is the source and derived knowledge-library substrate
- protocols/ccdp remains a separate protocol/package surface
- package roots do not always equal source roots
- persistent package exceptions and warnings remain explicit gates

Evidence status: closed directory-contract evidence.

## Arc03 Evidence

Arc03 closed after landing the accepted directory reorganization source edits.
Its composition evidence records:

- collaboration-framework supporting material moved under knowledge/
  component roots while preserving the top-level composer entrypoint
- component/method/template ownership moves landed
- templates/GUIDE.md remains a cross-cutting support exception
- Biome dual package behavior is preserved
- CCDP package separation is preserved
- package-path validation is green at the hard-failure level

Evidence status: closed source-layout and package-behavior evidence.

## Arc04 Evidence

Arc04 closed with README orientation and focused docs under docs/. Current
docs explicitly keep vocabulary provisional in places such as
docs/skill-library.md and docs/collaboration-framework.md. Arc04 also records
that final skill kind and atomic/composite vocabulary is deliberately owned by
Arc05.

Evidence status: closed current public-docs baseline.

## Classification Pressure for Arc05

Arc05 should decide public wording using the current source and package
evidence, not by promoting every planning term. The highest-confidence public
positions appear to be:

- use skill package language for generated assistant skills
- use protocol distribution/package language for CCDP
- preserve docs/ versus knowledge/ boundary language
- preserve collaboration-framework as active top-level composer
- keep concept-card-method planned until source and package behavior exist
- separate skill kind from topology

Open vocabulary pressure remains around:

- whether public docs should say "programming and tooling" or
  "domain/tooling"
- how prominently public docs should use "atomic skill" and "composite skill"
- whether bridge/integration layer and application/task bundle are public user
  vocabulary or maintainer/planning vocabulary
- whether metadata categories should be adjusted later to match accepted
  public kind names

## Evidence Status Boundary

not accepted taxonomy: external ontology rubric, Arc01 provisional edge-case
labels, and current frontmatter category values.

accepted/current facts: current package names, current entrypoints, closed
docs/ versus knowledge/ layout, CCDP separation, top-level
collaboration-framework entrypoint, and Arc04 docs baseline.
