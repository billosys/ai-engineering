# Arc 02: Conceptual Analysis

```yaml
project: project02-collab-breakout
arc: arc02-conceptual-analysis
status: active
depends-on:
  - arc01-framework-inventory
  - project03-concept-card-method:arc01-method-positioning:slice01-project02-boundary-aid
  - project03-concept-card-method:arc01-method-positioning:slice02-project02-acceptance-handoff
blocks:
  - arc03-functional-analysis
related:
  - ../arc01-framework-inventory/closing-report.md
  - ../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc01-synthesis.md
  - ../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/candidate-component-inputs.md
  - ../arc01-framework-inventory/slice03-arc01-synthesis/artifacts/arc02-question-register.md
  - ../../project03-concept-card-method/arc01-method-positioning/slice01-project02-boundary-aid/artifacts/project02-conceptual-boundary-aid.md
  - ../../project03-concept-card-method/arc01-method-positioning/slice02-project02-acceptance-handoff/artifacts/project02-arc02-acceptance-handoff.md
  - /Users/oubiwann/lab/billosys/ai-engineering/workbench/0009-howto-concept-card-extraction-with-llms-v3.2.md
  - /Users/oubiwann/lab/billosys/ai-engineering/workbench/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md
```

## Capability

Arc 02 performs the conceptual analysis of the current collaboration framework.
It examines taxonomy, ontology, naming, concept boundaries, historical problem
fit, and possible missing or overclaimed concepts.

The central question is not "which current files should become skills?" but
"which concepts and disciplines have independent reason-to-load, independent
contracts, and sensible composition behavior?"

Arc 02 does not select the final breakout architecture. Its job is to produce
an evidence-backed conceptual model, candidate-boundary evaluation, and
operator decision set that Arc 04 can later turn into an accepted architecture
after Arc 03 functional analysis.

Project03 is input, not control surface: Arc 02 may use the Project03 boundary
aid and handoff as operator-accepted conceptual inputs, but it does not wait on
Project03's full v4.0 skill, future arcs, or internal control closure.
The v3.2 workbench docs behind Project03 are also available as read-only
provenance for the concept-card lens; Arc02 should cite them when it needs the
older method's original wording for one-concept-one-card, source faithfulness,
typed relationships, competency questions, confidence, provenance, or
preservation checks.

## Slice Breakdown

### Slice 01: Boundary Analysis Instrument

Directory: `slice01-boundary-analysis-instrument`

Status: verified/closed on 2026-08-30.

Scope: consume Arc01's closed evidence base and the Project03 boundary aid /
handoff, define the conceptual-analysis method for this arc, and seed a
component-boundary ledger with every Arc01 candidate label. The slice should
define the fields and evidence vocabulary that later slices use, but should
not decide final component boundaries.

Delivered: Slice 01 produced the Arc02 conceptual-analysis method, input
evidence register, and seeded component-boundary ledger. CDC verified the close
in `slice01-boundary-analysis-instrument/cdc-verification.md`.

Durable synthesis outputs live under the slice-local `artifacts/` directory.

### Slice 02: Candidate Boundary Evaluation

Directory: `slice02-candidate-boundary-evaluation`

Status: open as of 2026-08-30.

Scope: apply the Slice01 method to every seeded candidate label and
classify each as candidate component, component family member, support asset,
adapter, dependency edge, constraint, template, package/release gate, or
non-component concept. The slice should record evidence, problem ownership,
competency questions, relationships, risks, and provisional disposition.

Blocks: Slice 03.

Open set exists. Durable evaluation outputs belong under the slice-local
`artifacts/` directory.

### Slice 03: Ontology And Decision Synthesis

Directory: `slice03-ontology-decision-synthesis`

Status: placeholder.

Expected scope: synthesize the candidate evaluation into an Arc02 conceptual
model, naming critique, merge/split findings, missing/overclaimed concept
findings, and operator decision register for Arc04 architecture work.

Detailed planning is deferred until Slice02 closes.

## Dependencies

Consumes:

- Closed Project02 Arc01 evidence, especially the Arc01 close report, Slice03
  synthesis, candidate-component inputs, and Arc02 question register.
- Project03 boundary aid and acceptance handoff as operator-accepted inputs.
- The two top-level v3.2 concept-card workbench docs as read-only provenance
  for the Project03 boundary lens, not as Project02 control gates.
- Project01 path/package constraints carried through Arc01.

Leaves for later arcs:

- A conceptual model and boundary evaluation that Arc03 can test against real
  usage patterns.
- A non-final set of candidate component classifications and open operator
  decisions for Arc04 breakout architecture.
- A record of conceptual risks: mislabels, improper merges, improper splits,
  missing concepts, overclaimed mechanisms, and file-boundary traps.

## Version History

### v1.0 - 2026-08-29

Placeholder opened with dependency on Arc 01.

### v1.1 - 2026-08-30

Recorded soft dependency on Project03 Arc01 Slice01 before detailed Arc02
planning. The dependency exists to sharpen ontology and component-boundary
analysis using the concept-card method, not to import Project03's full future
skill architecture.

### v1.2 - 2026-08-30

Recorded operator clarification that the future Project03 concept-card method
targets v4.0. Arc02 still waits only for the small boundary aid and operator
acceptance, not for the full v4.0 skill.

### v1.3 - 2026-08-30

Updated the soft dependency to include Project03 Arc01 Slice02, the acceptance
handoff packet. Arc02 still waits only for the focused handoff and operator
acceptance, not for Project03's full v4.0 skill architecture.

### v1.4 - 2026-08-30

Recorded CDC verification of Project03 Arc01 Slice02. Arc02 now waits on
operator acceptance of the boundary aid plus handoff and Project03 Arc01
formal close, not on production of the handoff or the full v4.0 skill.

### v1.5 - 2026-08-30

Opened Arc02 as active after operator acceptance that Project03 outputs are
useful inputs and that Project03 control closure does not gate Project02.
Added the two top-level v3.2 concept-card workbench docs as read-only
provenance behind the Project03 boundary lens. Planned three slices:
boundary-analysis instrument, candidate-boundary evaluation, and
ontology/decision synthesis.

### v1.6 - 2026-08-30

Recorded Slice 01 as verified/closed and opened Slice 02. Slice 02 now owns
candidate-boundary evaluation across the 26 seeded labels, while preserving
the non-final architecture posture and leaving synthesis to Slice 03.
