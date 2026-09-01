# Arc04 Architecture Input Inventory

```yaml
project: project03-concept-card-method
arc: arc04-skill-architecture
slice: slice01-architecture-input-inventory
status: proposed-done
mode: architecture input inventory
```

## Purpose

This inventory captures the accepted Arc03 commitments and candidate
skill-architecture surfaces that Arc04 must preserve while planning the v4.0
concept-card method skill. It is an input map only. It does not choose final
skill architecture, final file layout, exact schema syntax, exact enum
spelling, validator-code, README edits, Makefile edits, generated zips,
runtime services, live extraction, graph database, memory runtime, CCDP service
behavior, or source SKILL.md edits.

## Consumed Planning Inputs

| Source | Input used for this inventory |
|--------|-------------------------------|
| `../../../project-plan.md` | Project03 roadmap and Arc04 placement after the accepted Arc03 conceptual model. |
| `../../../ledger.md` | Project-level boundary that source edits remain out of scope until accepted implementation planning. |
| `../../arc-plan.md` | Arc04 capability: plan skill architecture surfaces without editing packaged skill source. |
| `../../ledger.md` | Arc-level criteria for load contract, problem ownership, dependency direction, package behavior, maintenance ownership, and source-edit fences. |
| `slice-plan.md` | Slice01 mandate to inventory inputs and questions, not decide architecture. |
| `ledger.md` | Slice-local falsifiable checks for produced artifacts, required terms, scope fences, and source cleanliness. |
| `../../../arc03-conceptual-model/closing-report.md` | Accepted close input that Arc03 delivered the conceptual model and handoff for Arc04. |
| `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-conceptual-model.md` | Accepted construct model, lifecycle flow, attachment points, preservation rules, and Arc04 boundary. |
| `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/v40-model-decision-register.md` | Accepted, provisional, deferred, out-of-scope, and open decisions that Arc04 must route. |
| `../../../arc03-conceptual-model/slice04-model-synthesis/artifacts/arc04-skill-architecture-handoff.md` | Direct list of commitments, candidate skill surfaces, Arc04 questions, dependencies, risks, and explicit non-decisions. |

## Accepted Arc03 Commitments to Preserve

| Commitment | Architecture implication |
|------------|--------------------------|
| concept card remains the visible atomic method unit | The loadable skill should preserve one concept per card as the authoring surface even if claims and result records become separate template or guide concerns. |
| claim is first-class when finer granularity is needed | Guides and templates must allow a claim to carry source support, evidence grade, verification, reconciliation, and memory admission without forcing all evidence into card prose. |
| source support and source span are distinct from provenance | Skill language must separate bibliographic/run provenance from the source support attachment that states which source span supports a claim or edge. |
| evidence grade is distinct from extraction confidence | The skill must not collapse warrant, extractor certainty, verification state, reconciliation state, validation result, or memory admission into one confidence field. |
| verification result and validation result are separate records | Architecture must leave room for structural validation and semantic verification to produce different evidence artifacts. |
| reconciliation is an auditable process with result records | Architecture must preserve conflict classes, decision rationale, lifecycle effect, and admission implication instead of treating conflicts as cleanup prose. |
| memory admission is a distinct lifecycle gate | A validated card, claim, edge, or CQ must not become durable semantic memory merely because it exists; admission policy needs an explicit surface. |
| relationship vocabulary carries forward from v3.2 | `prerequisites`, `extends`, `related`, and `contrasts_with` remain method vocabulary, with graph-native edge identity required when evidence or lifecycle state attaches. |
| competency questions remain first-class constructs | The skill must preserve CQ roles for requirement, answerability, coverage, verification, retrieval, obsolete, and deferred states. |
| extraction run is a first-class trace entity | Architecture must provide a place for source snapshot, method or prompt version, agent scope, output set, preservation decisions, validation result, reconciliation result, and parallel-worker provenance. |

## Candidate Skill Surfaces

| Surface | Candidate content | Status for Arc04 |
|---------|-------------------|------------------|
| `SKILL.md` | Thin entrypoint, reason to load, non-ownership boundaries, and routing to focused guides. | Candidate surface; exact wording deferred to Slice02 and synthesis. |
| guide set | Extraction, re-extraction, evidence/lifecycle, graph/CQ semantics, reconciliation, memory admission, and verification/validation. | Candidate surface; split and naming deferred to Slice03. |
| template set | Concept card, claim/source support, CQ, extraction run trace, validation result, verification result, reconciliation result, and memory admission. | Candidate surface; user-authored versus trace-record distinction deferred to Slice03. |
| validation candidate set | Required fields, provenance, source support, relationship references, CQ coverage, graph closure, preservation decisions, memory admission gates, path/slug hygiene, and consistency checks. | Candidate surface; deterministic subset deferred to Slice04 and Arc05 implementation planning. |
| example set | Minimal card, claim-backed card, CQ coverage example, relationship/edge example, extraction-run trace example, reconciliation example, and memory-admission example. | Candidate surface; release-critical examples deferred to Slice03. |
| README integration | Discoverability, supported method status, packaged surfaces, and experimental boundaries. | Candidate surface; integration plan deferred to Slice04 and Arc05. |
| package behavior | Whether guides, templates, examples, scripts, generated artifacts, and validation candidates are included in a packaged skill. | Candidate surface; package inclusion deferred to Slice04 and implementation planning. |
| maintenance ownership | Version history, conceptual model preservation, package ownership, validation updates, and README ownership. | Candidate surface; owner model deferred to Slice04 and Slice05. |

## Input Status Map

### Accepted

- The conceptual model commitments listed above are accepted Arc03 inputs.
- The skill must preserve distinct lifecycle concepts: extraction confidence,
  source support, evidence grade, verification, validation, reconciliation, and
  memory admission.
- Arc04 owns skill architecture planning; Arc05 owns implementation planning
  and source-edit planning.

### Provisional

- Source span identity and locator granularity remain provisional.
- Evidence grade vocabulary remains provisional.
- Verification state, reconciliation state, CQ status, and memory admission
  vocabulary remain provisional.
- Relationship storage as card-local fields versus graph-native edges remains
  provisional except when evidence, provenance, lifecycle state, reconciliation,
  or CQ coverage requires edge identity.
- Human/operator acceptance thresholds remain provisional.

### Deferred

- Final guide split, template shape, and example set.
- Exact schema syntax and enum spelling.
- Deterministic validator-code implementation.
- Exact package behavior, README integration, Makefile integration, generated
  zips, and release mechanics.
- CQ retrieval implementation and any runtime memory or graph services.

## Out of Scope

Out of scope for this slice: final skill architecture, final file layout,
source SKILL.md edits, README edits, Makefile edits, validator-code,
generated zips, runtime services, live extraction, graph database, memory
runtime, CCDP service design, schema implementation, package release, and
operator workflow enforcement.

## Downstream Routing

| Later owner | Inventory item routed forward |
|-------------|-------------------------------|
| Slice02 | `SKILL.md` load contract, reason to load, problem ownership, dependency direction, and operator-facing ownership boundary. |
| Slice03 | Guide split, template set, example set, and distinction between user-authored surfaces and trace/result records. |
| Slice04 | Validation determinism, package behavior, README integration, discoverability, and maintenance ownership. |
| Slice05 | Architecture synthesis, accepted architecture packet, unresolved decision register, and Arc05 handoff. |
| Arc05 | Source edits, exact file layout, validator-code, schema syntax, enum spelling, generated zips, Makefile changes, README changes, and implementation planning. |
