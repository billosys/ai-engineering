# v4.0 Source Layout Plan

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice02-source-layout-content-plan
artifact: v40-source-layout-plan
status: proposed-done
source-checkout: /Users/oubiwann/lab/billosys/ai-engineering
planned-source-home: knowledge/concept-card-method/
```

## Purpose

This artifact decides the planned source home and exact planned paths for the
v4.0 concept-card method skill surfaces. It preserves the accepted Arc04
architecture and the Slice01 package behavior constraint. It is a planning
artifact only: it does not edit source, does not perform source
implementation, and does not choose schema syntax, enum spelling,
validator-code language, deterministic validation implementation, tests,
package target names, package list edits, package-path exception rows,
generated zip policy, release gates, release readiness, runtime services,
GraphRAG, graph database, ontology database, memory runtime, CCDP service, or
live extraction behavior.

## Source Home Decision

Accepted Slice02 decision: the planned source home is:

`/Users/oubiwann/lab/billosys/ai-engineering/knowledge/concept-card-method/`

Rationale:

- `knowledge/` is the existing source home for loadable skill knowledge.
- Slice01 found no existing top-level `knowledge/*concept*` skill directory,
  so a new `knowledge/concept-card-method/` source home avoids overloading the
  root collaboration-framework `SKILL.md`.
- The name matches the method, not a programming language or runtime, and
  keeps problem ownership explicit.
- The layout can fit the current package behavior without changing the generic
  package helper: one selected `SKILL.md` plus sibling `guides/`.

## Package Behavior Constraint

Slice01 established that current generic skill package behavior copies the
selected `SKILL.md` plus sibling guides. In shorthand: SKILL.md plus sibling
guides.

Slice02 therefore plans templates, examples, validation documentation, and
support documents under `guides/` subdirectories so they are
package-compatible with the current package contract.

No package behavior change is required by this layout for those assets.
Slice04 still owns package target names, package list edits, package-path
checks, generated zip policy, generated archives, release gates, and final
package behavior acceptance.

## Planned Paths

### Entrypoint

| Surface | Planned path | Purpose |
|---------|--------------|---------|
| thin SKILL.md | `knowledge/concept-card-method/SKILL.md` | Load contract, reason to load, positive/negative load triggers, problem ownership, dependency direction, and guide routing. |

### Guide Files

| Guide file | Planned path | Purpose |
|------------|--------------|---------|
| load contract | `knowledge/concept-card-method/guides/01-load-contract.md` | Reason to load, positive load, negative load, problem ownership, dependency direction, adjacent-skill routing. |
| operator workflow | `knowledge/concept-card-method/guides/02-operator-workflow.md` | Operator workflow from source snapshot through extraction, review, reconciliation, validation, and memory-admission decisions. |
| extraction | `knowledge/concept-card-method/guides/03-extraction.md` | Source-faithful card and claim extraction, source support, source span capture, evidence grade, and extraction confidence. |
| re-extraction and preservation | `knowledge/concept-card-method/guides/04-re-extraction-preservation.md` | Old-card inventory comparison, preservation decisions, overwrite rules, and parallel-worker provenance. |
| evidence lifecycle | `knowledge/concept-card-method/guides/05-evidence-lifecycle.md` | Evidence grade, extraction confidence, validation result, verification state/result, reconciliation state/result, and memory admission. |
| graph and CQ | `knowledge/concept-card-method/guides/06-graph-cq.md` | Relationship vocabulary, graph-native edge identity, competency question/CQ coverage, answerability, retrieval, obsolete, and deferred roles. |
| reconciliation | `knowledge/concept-card-method/guides/07-reconciliation.md` | Conflict classes, reconciliation result records, rationale, and traceability. |
| validation and verification | `knowledge/concept-card-method/guides/08-validation-verification.md` | Deterministic validation candidates, semantic audit boundary, human/operator review boundary, and deferred runtime checks. |
| memory admission | `knowledge/concept-card-method/guides/09-memory-admission.md` | Admission gate, required lifecycle inputs, operator acceptance, and memory substrate implications. |
| maintenance and packaging | `knowledge/concept-card-method/guides/10-maintenance-packaging.md` | Maintenance ownership, version history touchpoints, package surface summary, and package promise boundary. |

### Template Files

Template files are planned as package-compatible support documents under
`guides/templates/`.

| Template file | Planned path | Purpose |
|---------------|--------------|---------|
| concept card | `knowledge/concept-card-method/guides/templates/concept-card.md` | User-authored concept-card surface. |
| claim and source support | `knowledge/concept-card-method/guides/templates/claim-source-support.md` | Claim record, source support, and source span attachment points. |
| competency question | `knowledge/concept-card-method/guides/templates/competency-question.md` | CQ requirement, answerability, coverage, retrieval, obsolete, and deferred roles. |
| relationship edge | `knowledge/concept-card-method/guides/templates/relationship-edge.md` | Relationship/edge record with graph-native identity. |
| extraction run | `knowledge/concept-card-method/guides/templates/extraction-run.md` | Trace record for source snapshot, method/prompt version, agent scope, output set, old-card inputs, and parallel-worker provenance. |
| validation result | `knowledge/concept-card-method/guides/templates/validation-result.md` | Result record for deterministic and documentary validation outcomes. |
| verification result | `knowledge/concept-card-method/guides/templates/verification-result.md` | Result record for semantic or human verification outcomes. |
| reconciliation result | `knowledge/concept-card-method/guides/templates/reconciliation-result.md` | Result record for conflict resolution and rationale. |
| preservation decision | `knowledge/concept-card-method/guides/templates/preservation-decision.md` | Result record for keep, revise, retire, merge, split, or defer decisions. |
| memory admission | `knowledge/concept-card-method/guides/templates/memory-admission.md` | Result record for memory admission decisions and operator acceptance. |

Slice03 owns exact schema syntax and enum spelling inside these templates.

### Example Files

Example files are planned as package-compatible support documents under
`guides/examples/`.

| Example file | Planned path | Purpose |
|--------------|--------------|---------|
| minimal card | `knowledge/concept-card-method/guides/examples/minimal-card.md` | Smallest valid first-release concept card example. |
| claim-backed card | `knowledge/concept-card-method/guides/examples/claim-backed-card.md` | Concept card with claim/source-support attachment. |
| CQ coverage | `knowledge/concept-card-method/guides/examples/cq-coverage.md` | CQ record and coverage example. |
| relationship edge | `knowledge/concept-card-method/guides/examples/relationship-edge.md` | Relationship/edge with graph-native identity. |
| extraction run trace | `knowledge/concept-card-method/guides/examples/extraction-run-trace.md` | Extraction-run provenance and output-set trace. |
| reconciliation | `knowledge/concept-card-method/guides/examples/reconciliation.md` | Conflict handling and reconciliation result example. |
| memory admission | `knowledge/concept-card-method/guides/examples/memory-admission.md` | Admission gate example with lifecycle inputs. |
| five-agent default recipe | `knowledge/concept-card-method/guides/examples/five-agent-default-recipe.md` | Parallel-worker default recipe; five agents are a recipe, not an invariant. |

Slice04 owns whether every example is release-gated and how examples are
validated inside generated archives.

### Validation Documentation

Validation documentation is planned under `guides/validation/` so the first
implementation can package validation guidance without changing the generic
package contract.

| Validation documentation | Planned path | Purpose |
|--------------------------|--------------|---------|
| structural candidates | `knowledge/concept-card-method/guides/validation/structural-candidates.md` | Deterministic validation candidates and non-goals. |
| semantic review boundary | `knowledge/concept-card-method/guides/validation/semantic-review-boundary.md` | What requires source-aware semantic audit. |
| human review boundary | `knowledge/concept-card-method/guides/validation/human-review-boundary.md` | What requires operator or human review. |
| deferred runtime checks | `knowledge/concept-card-method/guides/validation/deferred-runtime-checks.md` | Runtime, GraphRAG, graph database, ontology database, memory runtime, CCDP service, and live extraction non-goals. |

Slice03 owns deterministic validation scope, tests, failure-message format,
and validator-code scope. Slice04 owns package checks and release gates.

### Support Documents

Support document paths are planned under `guides/reference/` so they remain
package-compatible.

| Support document | Planned path | Purpose |
|------------------|--------------|---------|
| field glossary | `knowledge/concept-card-method/guides/reference/field-glossary.md` | Human-readable field and construct glossary, pending Slice03 schema details. |
| source locator notes | `knowledge/concept-card-method/guides/reference/source-locator-notes.md` | Source span and source support identity notes, pending Slice03 decisions. |
| review checklist | `knowledge/concept-card-method/guides/reference/review-checklist.md` | Operator review checklist for examples and produced cards. |
| change log notes | `knowledge/concept-card-method/guides/reference/change-log-notes.md` | Notes for source version history obligations, pending Slice04 final wording. |

## Cross-Links

Planned cross-link structure:

- `knowledge/concept-card-method/SKILL.md` links to
  `guides/01-load-contract.md`, `guides/02-operator-workflow.md`, and the
  focused guides for the operator's task.
- `guides/02-operator-workflow.md` links to the extraction, re-extraction,
  evidence lifecycle, graph/CQ, reconciliation, validation, and memory
  admission guides.
- Each guide links to the relevant `guides/templates/` and `guides/examples/`
  files.
- `guides/08-validation-verification.md` links to `guides/validation/`.
- `guides/10-maintenance-packaging.md` links to package and discoverability
  decisions planned by Slice04.
- README/library discoverability links are deferred to Slice04.

## First Source Edit Order

The first implementation should edit source in this order:

1. Create `knowledge/concept-card-method/` with `SKILL.md` and empty
   package-compatible `guides/` subdirectories only when the implementation
   slice authorizes source edits.
2. Add the thin SKILL.md load contract and guide map.
3. Add load-contract and operator-workflow guides.
4. Add extraction, re-extraction, evidence lifecycle, graph/CQ,
   reconciliation, validation/verification, memory-admission, and
   maintenance/packaging guides.
5. Add template files under `guides/templates/`.
6. Add example files under `guides/examples/`.
7. Add validation documentation and support documents under
   `guides/validation/` and `guides/reference/`.
8. Run source-local checks planned by later slices before any package,
   README, Makefile, or release claim is made.

## Later-Slice Routing

- Slice03 owns schema syntax, enum spelling, validator-code scope,
  deterministic validation, tests, and failure-message format.
- Slice04 owns package target names, package list edits, package-path
  exceptions, package-path checks, generated zip policy, generated archives,
  release gates, README/library discoverability, and source version history.
- Slice05 owns implementation-plan synthesis, source edit sequence
  composition, implementation slice recommendations, deferral register, and
  Project03 close input.

Slice02 found no layout or content-sequencing fact that requires Arc05
re-sequencing, a new slice, or a scope correction.
