# v4.0 Maintenance Ownership Model

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice04-validation-packaging-discoverability
status: proposed-done
mode: maintenance ownership model
```

## Purpose

This artifact defines maintenance ownership for the v4.0 concept-card method
skill architecture. It assigns owner and change path expectations for the
conceptual model, guide, template, example, package list, package behavior,
README, skill library, validation candidate, validator-code, and version
history alignment.

## Ownership Matrix

| Area | Owner | Change path |
|------|-------|-------------|
| conceptual model | Arc03 owns accepted conceptual semantics; Slice05 owns Arc04 synthesis alignment; future method maintainers own post-release changes. | Change through an explicit model-change proposal, then update affected guides, templates, examples, validation candidates, README text, and version history. |
| guide architecture | Arc04 Slice03 owns the initial guide architecture; Slice05 composes it; Arc05 implements source guide files. | Change by identifying affected guide concerns and preserving the thin SKILL.md route. |
| template architecture | Arc04 Slice03 owns the initial template architecture; Slice05 composes it; Arc05 implements source template files. | Change by preserving user-authored, trace record, and result record surface classes. |
| example architecture | Arc04 Slice03 owns release-critical example architecture; Slice05 confirms first-release set; Arc05 implements exact example files. | Change by naming affected release-critical or optional examples and updating validation expectations. |
| package behavior | Arc04 Slice04 owns architecture-level package behavior; Slice05 composes it; Arc05 performs implementation planning. | Change by updating packaged surface categories and routing exact file layout to Arc05. |
| package list | Arc05 owns source package list edits and release mechanics. | Change through implementation planning, Makefile/package updates, generated zips, tests, and release gates. |
| README | Arc04 Slice04 owns discoverability promise boundaries; Arc05 owns source README edits. | Change by preserving the promise boundary and updating version history for touched source docs. |
| skill library | Arc04 Slice04 owns architecture-level skill library discoverability; Arc05 owns source/package publication mechanics. | Change by keeping reason-to-load text consistent with SKILL.md and README. |
| validation candidate | Arc04 Slice04 owns candidate classification; Slice05 owns synthesis; Arc05 owns executable planning. | Change by marking whether the candidate is deterministic structural, semantic audit, human/operator review, or deferred runtime. |
| validator-code | Arc05 owns validator-code implementation planning, tests, and CLI/API behavior. | Change only after the architecture synthesis accepts the candidate and exact schema syntax. |
| version history | Arc05 owns source version history updates for every changed source document. | Change by updating each touched source file's local version history, or the enclosing versioned file when needed. |

## Maintenance Rules

- Maintenance ownership follows the accepted conceptual model: concept card,
  claim, source support, source span, evidence grade, extraction confidence,
  verification state/result, validation result, reconciliation state/result,
  preservation decision, and memory admission remain distinct.
- Guide changes must preserve the load contract and thin SKILL.md route.
- Template changes must preserve user-authored, trace record, and result
  record surfaces.
- Example changes must identify whether the example is release-critical or
  optional/later.
- Package behavior changes must preserve library discoverability without
  implying runtime services.
- README and skill library changes must not overpromise GraphRAG, graph
  database, ontology database, memory runtime, CCDP service, live extraction,
  executable validator-code, generated zips, or package release behavior.
- Validation candidate changes must not silently become validator-code.
- Source changes must include version history alignment when Arc05 edits
  source files.

## Preservation of Prior Decisions

This model preserves the Slice02 load contract, thin SKILL.md posture, and
dependency direction. It also preserves Slice03 guide architecture, template
architecture, and example architecture, including user-authored surfaces,
trace record surfaces, result record surfaces, release-critical examples, the
five-agent default recipe, not an invariant, and parallel-worker provenance.

## Later Owner Routing

| Later owner | Routed question |
|-------------|-----------------|
| Slice05 | architecture synthesis, final decision register, owner summary, and Arc05 handoff. |
| Arc05 | implementation planning for source edit work, exact file layout, schema syntax, enum spelling, validator-code, Makefile, README edits, generated zips, tests, release mechanics, package updates, source package list edits, and version history updates. |

## Out of Scope

Out of scope for this artifact: source SKILL.md edits, source checkout edits,
source edit mechanics, validator-code implementation, deterministic validation
scripts, exact CLI/API behavior, graph database design, GraphRAG runtime,
memory runtime, CCDP service behavior, live extraction, package release, and
generated zips.
