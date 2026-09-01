# v4.0 Load Contract

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice02-load-contract-ownership
status: proposed-done
mode: load contract
```

## Purpose

This artifact defines when a session should load the v4.0 concept-card method
skill and how a thin `SKILL.md` entrypoint should route work. It decides the
load contract only. It does not choose final guide architecture, final template
architecture, final example set, package inclusion, README integration,
Makefile changes, validator-code, deterministic validation scripts, generated
zips, released packages, graph database design, memory runtime design, CCDP
service design, live extraction behavior, or source checkout edits.

## Reason to Load

Load the concept-card method skill when the user is doing method-specific
concept-card work, especially when the session must create, revise, audit, or
plan cards as a provenance-bearing knowledge substrate.

Positive load triggers:

- The user asks to extract concept cards from source material.
- The user asks to re-extract, reconcile, compare, or preserve prior concept
  cards against newer source material.
- The user asks for a v4.0 concept-card method, concept-card ontology, or
  concept-card skill architecture task.
- The user asks to attach or evaluate claim-level source support, evidence
  grade, extraction confidence, verification state, validation result,
  reconciliation state, or memory admission for concept-card material.
- The user asks to design or assess competency question coverage for cards,
  claims, source support, or relationship edges.
- The user asks to prepare concept-card material for durable semantic memory
  admission, while preserving source support and verification/reconciliation
  state.
- A project plan or slice prompt explicitly names the concept-card method,
  v3.2/v4.0 concept-card extraction, or a concept-card skill surface.

## Negative Load Triggers

Do not load this skill by default for related work whose primary problem is
owned elsewhere.

Use these as negative trigger rules: in each case, do not load this skill
unless the operator also asks for concept-card method output.

- General research summarization that does not ask for concept cards, claims,
  CQs, extraction runs, or memory admission.
- General project-management work such as opening a project, closing a slice,
  updating ledgers, or writing plans when the concept-card method is not the
  subject. Route that to collaboration-framework and project management
  guidance.
- Source reading or citation lookup whose output is ordinary notes, not a
  concept-card substrate. Use source-reading practices first, then load this
  skill only if the user asks to convert the evidence into cards or claims.
- Implementation planning, source edits, validator-code, Makefile changes,
  README changes, package updates, generated zips, release mechanics, or test
  gates. Route those to Arc05 implementation planning or the relevant language
  and repository guidance.
- Domain-knowledge work where the main question is correctness in Rust, Go,
  Erlang, C++, JavaScript/Deno, visual design, or another domain. Load the
  domain-knowledge skill first; load this skill only when that knowledge is to
  be represented as concept cards.
- Memory work that is only recall, lookup, or memory-file maintenance. Load
  this skill when the session needs provenance-bearing concept-card extraction
  or memory admission gates, not for every memory interaction.

## Thin Entrypoint Contract

The future `SKILL.md` should be a thin entrypoint. It should answer:

- when to load the skill;
- what problem ownership the skill accepts;
- what it does not own;
- how to route to focused guide surfaces;
- which unresolved choices remain owned by later planning or implementation.

The entrypoint should not embed the full method, final guide text, final
template definitions, examples, validation candidate details, package behavior,
README integration, or source-edit instructions. It should route to guides by
method concern without freezing final guide filenames as accepted
architecture in this slice.

Candidate routing concerns for later guide architecture:

- extraction from source material;
- re-extraction and prior-card preservation;
- evidence lifecycle, including claim, source support, evidence grade,
  extraction confidence, verification state, validation result,
  reconciliation state, and memory admission;
- graph and competency question use;
- reconciliation and conflict result records;
- validation and verification workflow;
- memory admission policy and operator acceptance.

Slice03 owns final guide, template, and example architecture. Slice04 owns
validation determinism, package behavior, README integration, discoverability,
and maintenance ownership. Slice05 owns architecture synthesis. Arc05 owns
implementation planning for source edit work, Makefile changes, validator-code,
generated zips, package updates, and release gates.

## Five-Agent Workflow Position

The v3.2 five-agent workflow is a default recipe, not an invariant.

Rationale:

- Arc03 accepted extraction-run and parallel-worker provenance as conceptual
  commitments, but it did not require exactly five workers.
- Treating five agents as invariant would overfit the skill to one execution
  shape and could block smaller source sets, larger source sets, or tool-driven
  extraction.
- Treating the workflow as merely deferred would leave Slice03 without enough
  operator workflow guidance for guide and template planning.

The load contract should present the pattern as parameterized around roles:
source-primary extraction, parallel re-extraction where useful, reconciliation,
validation, and verification. The default recipe may name five agents as a
known working pattern, but extraction runs must record actual agent scope,
parallel-worker provenance, source snapshot, output set, preservation
decisions, validation result, reconciliation result, and memory-admission
implications whether the run uses one worker or many.

## Out of Scope

Out of scope for this slice: final guide architecture, final template
architecture, final example set, package inclusion, README integration,
Makefile changes, validator-code, deterministic validation scripts, generated
zips, released packages, graph database design, memory runtime design, CCDP
service design, live extraction behavior, source checkout edits, exact schema
syntax, and exact enum spelling.
