# Arc 01: Framework Inventory and Problem Map

```yaml
project: project02-collab-breakout
arc: arc01-framework-inventory
status: closed
depends-on:
  - project01-harmonise-paths:closed-and-completely-verified
blocks:
  - arc02-conceptual-analysis:unblocked-after-project03-review-pause
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

Status: verified/closed by CDC on 2026-08-29.

Scope: inspect the current framework entry points and source documents, record
the source/package path assumptions that must be inherited from Project 01,
and produce a source-backed inventory of concepts, disciplines, templates, and
usage promises.

Outcome: delivered. The slice produced source inventory, source-to-concept
map, Project01 path-contract notes, and gate evidence under `artifacts/`.

Blocks: no longer blocking Slice 02; Slice 02 may be opened next.

### Slice 02: Problem-Solution Map

Directory: `slice02-problem-solution-map`

Status: verified/closed by CDC on 2026-08-29.

Scope: convert the inventory into a historical problem-to-solution map. For
each major failure mode, identify the current mechanism or mechanisms that
claim to address it, the evidence that the mechanism exists, and any suspected
underfit, overfit, overlap, or missing solution.

Outcome: delivered. The slice produced a problem-solution map, mechanism
coverage matrix, and critical findings under `artifacts/`.

Blocks: no longer blocking Slice 03; Slice 03 may be opened next.

### Slice 03: Arc 01 Synthesis

Directory: `slice03-arc01-synthesis`

Status: verified/closed by CDC on 2026-08-30.

Scope: synthesize Arc 01 into input material for Arc 02: current component
clusters, candidate breakout components, suspected mislabels, suspected
improper splits/merges, package/path constraints inherited from Project 01,
and open questions for operator discussion.

Outcome: delivered. The slice produced the Arc 01 synthesis,
candidate-component inputs, and Arc 02 question register under `artifacts/`.
CDC verified that the outputs remain non-final analysis inputs and that no
remediation slice is required before Arc 02 planning.

Blocks: no longer blocking Arc 01 close; Arc 02 remains blocked until Arc 01
formally closes.

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

### v1.1 - 2026-08-29

Slice 01 marked verified/closed by CDC. The slice delivered the source-backed
inventory, concept map, Project01 path-contract notes, and open questions
needed for Slice 02. No Arc 01 scope or sequencing change was required.

### v1.2 - 2026-08-29

Slice 02 opened from the verified Slice 01 inventory and Project01 path/package
constraints. The slice remains analysis-only and does not decide final breakout
boundaries.

### v1.3 - 2026-08-29

Slice 02 marked verified/closed by CDC. The slice delivered the
problem-solution map, mechanism coverage matrix, and critical findings needed
for Slice 03. No Arc 01 scope or sequencing change was required.

### v1.4 - 2026-08-30

Slice 03 opened to synthesize Arc 01's verified inventory and problem map into
non-final Arc 02 conceptual-analysis inputs.

### v1.5 - 2026-08-30

Slice 03 marked verified/closed by CDC. The slice delivered the Arc 01
synthesis, candidate-component inputs, and Arc 02 question register needed for
formal Arc 01 close. No remediation slice is required before Arc 02 planning.

### v1.6 - 2026-08-30

Arc 01 formally closed after arc-scale composition verification. The three
verified slices compose into the promised inventory/problem-map evidence base;
Arc 02 remains paused until the operator-requested Project03 concept-card
boundary aid is reviewed.
