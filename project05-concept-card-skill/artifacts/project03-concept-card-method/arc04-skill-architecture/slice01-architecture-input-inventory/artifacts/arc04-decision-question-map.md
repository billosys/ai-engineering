# Arc04 Decision Question Map

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice01-architecture-input-inventory
status: proposed-done
mode: decision question map
```

## Purpose

This map preserves open architecture questions for later Arc04 slices and
Arc05. It assigns a decision owner without choosing final skill architecture,
final file layout, exact schema syntax, exact enum spelling, validator-code,
README edits, Makefile edits, generated zips, runtime services, live
extraction, graph database, memory runtime, CCDP service behavior, or source
SKILL.md edits.

## Decision Axes

| Axis | Meaning for later decisions |
|------|-----------------------------|
| reason to load | What user problem, artifact state, or operator intent should trigger the concept-card method skill. |
| problem ownership | Which problems the skill owns directly versus routes to collaboration-framework, project management, source reading, or later implementation planning. |
| dependency direction | Whether this skill depends on adjacent framework guidance, adjacent guidance depends on it, or both remain peers with explicit routing. |
| package behavior | Which guides, templates, examples, scripts, generated artifacts, and validation candidates belong in the packaged skill. |
| maintenance ownership | Which file or process owns conceptual model updates, version history, package updates, README integration, and validator updates. |
| validation determinism | Which checks are stable enough for deterministic validation versus semantic audit or human/operator review. |
| operator workflow | How extraction, re-extraction, verification, reconciliation, and memory admission should be presented to the operator. |
| decision owner | The later slice or arc responsible for deciding the question. |

## Question Map

| Question | Axes | decision owner | Preserve until decision |
|----------|------|----------------|-------------------------|
| When should the concept-card method skill load? | reason to load; operator workflow | Slice02 | Do not make every research or memory task load the skill by default. |
| What problem does the skill own directly? | problem ownership; dependency direction | Slice02 | Preserve the boundary between concept-card method work and general collaboration-framework ledger work. |
| What does the skill explicitly leave to adjacent guidance? | problem ownership; dependency direction | Slice02 | Source reading, project close discipline, and broad evidence practice may remain owned by existing skills unless Slice02 decides otherwise. |
| How should `SKILL.md` route to guides? | reason to load; dependency direction; operator workflow | Slice02 | Keep the entrypoint thin until the load contract is accepted. |
| Is the v3.2 five-agent workflow invariant, default recipe, or parameterized pattern? | operator workflow; validation determinism | Slice02 | Preserve extraction-run traceability and parallel-worker provenance without enforcing policy early. |
| Which guide split best preserves extraction, evidence lifecycle, graph/CQ semantics, reconciliation, memory admission, and verification/validation? | problem ownership; operator workflow; maintenance ownership | Slice03 | Do not merge distinct lifecycle concerns into one confidence or validation guide. |
| Which template surfaces are user-authored, and which are internal trace/result records? | operator workflow; validation determinism; maintenance ownership | Slice03 | Preserve concept card authoring while keeping claim/source support and result records available where granularity matters. |
| Which examples are release-critical? | reason to load; operator workflow; package behavior | Slice03 | Preserve example coverage for minimal card, claim-backed card, CQ coverage, relationship/edge, extraction run, reconciliation, and memory admission. |
| Which validation candidate checks are deterministic enough for later automation? | validation determinism; package behavior | Slice04 | Preserve candidates for required fields, provenance, source support, relationship references, CQ coverage, graph closure, preservation decisions, and memory admission gates. |
| Which checks remain semantic audit or human/operator review? | validation determinism; operator workflow | Slice04 | Do not promise validator-code for evidence grade, verification outcome, reconciliation judgment, or admission policy before Arc05. |
| What package behavior should the architecture recommend? | package behavior; maintenance ownership | Slice04 | Decide whether guides, templates, examples, scripts, generated artifacts, and validation candidates are packaged surfaces or planning-only inputs. |
| How should README integration and discoverability work? | package behavior; maintenance ownership | Slice04 | Keep README promises aligned with packaged behavior and avoid implying runtime GraphRAG, memory runtime, ontology database, or CCDP service support. |
| What maintenance ownership model keeps the skill aligned with the conceptual model? | maintenance ownership; dependency direction | Slice04 | Preserve version-history obligations and route future conceptual-model changes through an explicit owner. |
| What final architecture packet should Arc04 accept? | decision owner; maintenance ownership; package behavior | Slice05 | Architecture synthesis must show how Slice02, Slice03, and Slice04 decisions compose. |
| What unresolved questions must move to implementation planning? | decision owner; validation determinism; package behavior | Slice05 | Arc05 should receive exact file layout, source edits, schema syntax, enum spelling, validator-code, Makefile, README, generated zips, and package implementation questions. |
| Which source changes are authorized only after architecture acceptance? | problem ownership; package behavior; decision owner | Arc05 | Source SKILL.md edits, guide/template creation, README edits, Makefile edits, validator-code, generated zips, and release mechanics remain later implementation planning. |

## Owner Summary

| Owner | Decision area |
|-------|---------------|
| Slice02 | load contract, reason to load, problem ownership, dependency direction, and operator workflow boundary. |
| Slice03 | guide architecture, template architecture, example architecture, and user-authored versus trace/result-record surfaces. |
| Slice04 | validation determinism, package behavior, README integration, discoverability, and maintenance ownership. |
| Slice05 | architecture synthesis, acceptance packet, unresolved decision register, and Arc05 handoff. |
| Arc05 | implementation planning for source edits, exact file layout, schema syntax, enum spelling, validator-code, Makefile changes, README changes, generated zips, package changes, and release gates. |

## Out of Scope

Out of scope for this slice: final skill architecture, final file layout,
source SKILL.md edits, README edits, Makefile edits, validator-code,
generated zips, runtime services, live extraction, graph database, memory
runtime, CCDP service design, exact schema syntax, exact enum spelling, package
release, and implementation changes.
