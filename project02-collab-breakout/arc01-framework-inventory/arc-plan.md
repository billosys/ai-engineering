# Arc 01: Framework Inventory and Problem Map

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
status: planned
depends-on:
  - project01-harmonise-paths:closed-and-completely-verified
blocks:
  - arc02-conceptual-analysis
related:
  - ../../project01-harmonise-paths
  - /Users/oubiwann/lab/billosys/ai-engineering/SKILL.md
  - /Users/oubiwann/lab/billosys/ai-engineering/README.md
  - /Users/oubiwann/lab/billosys/ai-engineering/docs
  - /Users/oubiwann/lab/billosys/ai-engineering/templates
```

## Capability

Arc 01 establishes the evidence base for the collaboration-framework breakout.
It inventories the current framework from actual source artifacts, maps major
concepts and operational disciplines to their source locations, identifies the
historical and functional problems each mechanism appears to address, and
surfaces the open questions that the conceptual analysis must settle.

The arc does not decide the final breakout. Its job is to make later judgment
honest: the conceptual and functional analyses should not be guessing what is
inside the current framework or relying on the current file boundaries as if
they were already the ontology.

## Slice Breakdown

### Slice 01: Source Inventory

Directory: `slice01-source-inventory`

Scope: inspect the current framework entry points and source documents, record
the source/package path assumptions that must be inherited from Project 01,
and produce a source-backed inventory of concepts, disciplines, templates, and
usage promises.

Blocks: Slice 02.

### Slice 02: Problem-Solution Map

Directory: `slice02-problem-solution-map`

Scope: convert the inventory into a historical problem-to-solution map. For
each major failure mode, identify the current mechanism or mechanisms that
claim to address it, the evidence that the mechanism exists, and any suspected
underfit, overfit, overlap, or missing solution.

Blocks: Slice 03.

Detailed open set deferred until Slice 01 closes.

### Slice 03: Arc 01 Synthesis

Directory: `slice03-arc01-synthesis`

Scope: synthesize Arc 01 into input material for Arc 02: current component
clusters, candidate breakout components, suspected mislabels, suspected
improper splits/merges, package/path constraints inherited from Project 01,
and open questions for operator discussion.

Blocks: Arc 02.

Detailed open set deferred until Slice 02 closes.

## Dependencies

Consumes:

- Verified Project 01 path-harmonisation results, especially source-vs-package
  path contract and package validation requirements.
- Current source checkout at
  `/Users/oubiwann/lab/billosys/ai-engineering`.
- Planning artifacts under this project directory.

Leaves for later arcs:

- A source-backed evidence map for conceptual analysis.
- A problem-solution map for checking whether current mechanisms address the
  stated/historical problem space.
- A list of open questions that should be answered before target component
  boundaries are finalized.

## Version History

### v1.0 - 2026-08-29

Initial Arc 01 plan opened with Slice 01 planned and execution explicitly
blocked on verified completion of `project01-harmonise-paths`.
