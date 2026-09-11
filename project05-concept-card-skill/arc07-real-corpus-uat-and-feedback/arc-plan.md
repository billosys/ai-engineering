# Arc07 Plan: Real Corpus UAT And Feedback

```yaml
project: project05-concept-card-skill
arc: arc07-real-corpus-uat-and-feedback
status: open
opened: 2026-09-11
depends-on:
  - arc06-gate-evidence-and-project-closure
source-corpus:
  url: https://github.com/CompCogNeuro/book
```

## Capability

Arc07 turns Project05's delivered skills from package-complete into
field-tested. It uses the open `CompCogNeuro/book` Markdown textbook corpus as
a real source, prepares the corpus with `document-extraction`, generates and
reviews concept cards with `concept-cards`, records real-use friction, and
feeds accepted findings back into the skills before final closure.

This is not a simple smoke test. It is an iterative field trial with explicit
measures, evidence capture, feedback disposition, and a RAG/graph handoff
boundary for the forthcoming memory-protocol work.

## Dependencies

Arc07 consumes:

- Arc02's `document-extraction` source-preparation contracts;
- Arc03 and Arc04's `concept-cards` method, records, examples, and references;
- Arc05 package/install evidence and Arc06 closure-baseline gates;
- the `CompCogNeuro/book` corpus snapshot, license, Markdown chapter files,
  figures, glossary, metadata, and references;
- operator goals for memory-protocol concept-card retrieval and future
  RAG/MCP/graph use.

Arc07 may produce source-skill refinements when real use reveals a gap. It
must not silently implement a production graph database, GraphRAG system, MCP
server, memory runtime, or external release unless the operator explicitly
expands a slice to include that work. Otherwise it produces an import-ready
handoff and a follow-on boundary for the memory-protocol project.

## Slice Breakdown

| Slice | Scope | Dependencies |
| --- | --- | --- |
| Slice01: UAT Protocol And Corpus Intake | Pin or acquire the `CompCogNeuro/book` source snapshot, inspect license and file structure, define UAT questions/measures, select pilot corpus slices, and write the RAG handoff assumptions. | Arc06 baseline. |
| Slice02: Pilot Markdown Preparation And Card Extraction | Prepare a representative subset with `document-extraction`, generate concept-card records with `concept-cards`, and record friction, ambiguity, and missing guidance. | Slice01. |
| Slice03: Feedback-Driven Skill Refinement | Convert pilot findings into accepted skill/template/example updates or explicit no-op/follow-on decisions; rerun relevant gates. | Slice02. |
| Slice04: Expanded Corpus Card Generation | Generate the agreed concept-card set for the corpus or accepted corpus subset, with validation, verification sampling, provenance, and caveat records. | Slice03. |
| Slice05: RAG Handoff And UAT Synthesis | Package the concept-card corpus for downstream RAG/graph/MCP use, document import/query assumptions, summarize UAT findings, and hand off to Arc08 closure refresh. | Slice04. |

## Arc Exit Criteria

Arc07 closes when:

- the corpus snapshot, license, source manifest, and file inventory are
  recorded;
- UAT questions, measures, pilot sample, and stop conditions are explicit
  before pilot generation;
- pilot and expanded concept-card generation produce inspectable artifacts or
  explicit stop/caveat records;
- every real-use finding is dispositioned as a source refinement, no-op, or
  follow-on work with a re-entry condition;
- generated concept-card records preserve provenance, source support, evidence
  grade, extraction confidence, validation, verification, reconciliation, and
  memory-admission distinctions;
- RAG/graph/MCP needs are captured as an import-ready handoff or a follow-on
  project boundary, not smuggled in as an unverified runtime claim;
- relevant source/package gates pass after any skill edits.

## Version History

### v1.0 - 2026-09-11

Opened Arc07 after the operator paused Project05 closure to require real-corpus
UAT and iterative feedback using the `CompCogNeuro/book` Markdown textbook
corpus, with memory-protocol/RAG use as the downstream acceptance pressure.
