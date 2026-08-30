# Arc03 Conceptual Model Inputs

```yaml
project: project03-concept-card-method
arc: arc02-method-inventory
slice: slice03-inventory-synthesis
status: proposed-done
handoff-to: ../../arc03-conceptual-model
mode: input packet
not-final: true
```

## Scope Fence

This packet names Arc03 inputs, not final conceptual model decisions. Arc03
must decide the model. Slice03 only carries forward source-backed constructs,
required distinctions, and open question prompts from the verified Arc02
inventory and gap analysis.

Out of scope for Slice03: final packaging, skill layout, implementation
mechanics, source edits, package behavior, Makefile changes, README
integration, examples, deterministic validator scripts, live corpus extraction,
GraphRAG runtime, memory runtime, ontology database, and CCDP service design.

## Candidate Constructs

### concept card

Input: v3.2 treats the concept card as the atomic knowledge unit with YAML
frontmatter and Markdown body sections.

Required distinction: Arc03 should decide whether a concept card remains the
primary durable unit or becomes a container for more granular claim, source
span, evidence grade, verification, relationship, and memory admission records.

Open question: What invariant makes one card one card when claims,
relationships, and evidence may vary independently?

### claim

Input: v3.2 cards contain synthesized assertions, but the method does not name
claim as a separate construct.

Required distinction: Arc03 should decide whether each extracted assertion is a
claim with its own provenance, evidence grade, confidence, verification status,
and admission state.

Open question: Is a card itself a claim, a bundle of claims, or a curated
summary over claims?

### source span

Input: v3.2 records source title, slug, authors, chapter, PDF page, section,
source reference, and verification notes.

Required distinction: Arc03 should decide whether source span is a first-class
anchor separate from bibliographic provenance and card-level source reference.

Open question: What granularity is required: section, paragraph, quote, page
range, line range, or source-specific locator?

### evidence grade

Input: v3.2 has `extraction_confidence`, but Slice02 identifies evidence grade
as distinct from extraction confidence and verification state.

Required distinction: Arc03 should decide whether evidence grade describes the
claim's warrant, the source-span support, the verification result, human
attestation, or a separate synthesis over all of them.

Open question: Which grade vocabulary should v4.0 use, and how does it map to
CCDP-compatible claim/provenance/audit semantics?

### relationship or edge

Input: v3.2 has four relationship fields: `prerequisites`, `extends`,
`related`, and `contrasts_with`, with explanatory body sections.

Required distinction: Arc03 should decide whether relationship stays a
card-local field or becomes an edge with type, endpoints, evidence, status,
inverse policy, reconciliation result, and graph closure expectations.

Open question: Which graph-native relationship semantics are needed without
discarding the useful v3.2 relationship fields prematurely?

### competency question

Input: v3.2 uses competency questions for requirement elicitation, mapping,
card-level `answers_questions`, and validation coverage.

Required distinction: Arc03 should decide whether a competency question is a
requirement, a test, a retrieval query, a coverage target, or all of those
under different statuses.

Open question: What explicit status should track whether a competency question
is covered, answerable, verified, obsolete, or deferred?

### extraction run

Input: v3.2 and 0010 describe coordinated extraction phases, agent
assignments, prompts, source material, output cards, and validation, but do not
model the run itself.

Required distinction: Arc03 should decide whether extraction run is a trace
object that records source snapshot, prompt version, agent scope, generated
card set, old-card inputs, preservation decisions, validation result, and
reconciliation result.

Open question: What minimum run metadata is required before downstream memory
can rely on produced cards?

### verifier

Input: v3.2 validates cards through checklists, grep commands, CQ coverage, and
sampled semantic quality, but does not name verifier as a role or construct.

Required distinction: Arc03 should decide whether verifier is a person, model,
process, evidence record, role label, or verification-result authority.

Open question: What separates extractor confidence from verifier judgment and
independent reproduction?

### reconciliation

Input: v3.2 parallel extraction has coordination and validation, but Slice02
identifies missing reconciliation for duplicate concepts, competing
definitions, slug drift, taxonomy drift, relationship asymmetry, and parallel
agent conflicts.

Required distinction: Arc03 should decide whether reconciliation is a workflow
phase, a role, a result object, or a status attached to cards, claims, and
edges.

Open question: What conflicts must reconciliation detect before a card or
relationship can advance?

### memory admission

Input: v3.2 has validation and preservation checks, but memory admission is
implicit. Project03 targets provenance-bearing memory consolidation.

Required distinction: Arc03 should decide whether memory admission is a
lifecycle state, a gate result, a policy decision, or a durable evidence record
that says future cognition may rely on the card.

Open question: What evidence is necessary before extracted content is admitted
to durable semantic memory?

## Cross-Construct Questions

- How should extraction confidence, evidence grade, verification status,
  reconciliation status, and memory admission differ?
- Which constructs are method concepts and which belong to Arc04 packaging or
  Arc05 implementation?
- Which statuses can be machine-validated, which require semantic QA, and
  which require operator acceptance?
- Which source-backed v3.2 fields stay card-local, and which become separate
  entities in v4.0?
- What must be preserved from old cards when claims or source spans become more
  granular than the v3.2 card?

## Boundary Reminders

Arc03 owns the conceptual model. This packet is not final and does not design
the model. Arc04 owns skill layout and package decisions. Arc05 owns
implementation planning. No source edits are authorized by this handoff.
