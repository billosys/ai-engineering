# Arc09 Plan: Rich Concept-Card Profile

```yaml
project: project05-concept-card-skill
arc: arc09-rich-concept-card-profile
status: closed
opened: 2026-09-11
depends-on:
  - arc08-post-uat-closure-refresh
```

## Capability

Arc09 restores the useful v3.2 rich-card output profile inside the live
`concept-cards` skill while preserving the stronger v4 lifecycle, provenance,
evidence, validation, verification, reconciliation, and memory-admission
controls implemented in Project05.

The triggering finding is evidence-backed: Arc07 candidate cards are more
auditable than older corpora, but they lack the richer learner/reference
sections found in prior `complete-musician` cards, Erlang v3.2 cards, and the
original v3.2 prompts. Arc09 must synthesize those strengths rather than
reverting wholesale to v3.2.

## Dependencies

Arc09 consumes:

- Arc08's CDC-verified post-UAT closure baseline;
- the Project05 source-v32 prompt artifacts;
- the Project03 v3.2-to-v4.0 carry-forward analysis;
- the `complete-musician` concept-card corpus as older rich-card evidence;
- the Erlang `design-scale-erlang-otp` concept-card corpus as recent v3.2
  prompt evidence;
- the Arc07 CompCogNeuro candidate cards and UAT findings;
- current `knowledge/concept-cards` source, package, and validation contracts.

Arc09 must not expand Project05 into full-book extraction, operator acceptance
of CompCogNeuro cards, semantic verification of the corpus, memory admission,
graph/RAG/MCP runtime implementation, or retrieval evaluation.

## Slice Breakdown

| Slice | Scope | Dependencies |
| --- | --- | --- |
| Slice01: V3.2 Richness Gap And Design | Produce a durable gap analysis and implementation design that identifies which v3.2 sections, checks, and examples must carry forward into the live skill and where they belong. | Arc08; v3.2 prompts; sample corpora. |
| Slice02: Rich Profile Source Updates | Update `concept-cards` guides/templates/examples/references/version history so real-corpus extraction defaults to rich cards while preserving v4 lifecycle/provenance controls. | Slice01. |
| Slice03: Regression Examples And Validation | Add or update representative examples and validation guidance so missing rich sections, weak examples, and wrapper artifacts are caught without weakening v4 record discipline. | Slice02. |
| Slice04: Package Gates And Arc Closure Inputs | Run focused and repository gates, inspect packages, reconcile ledgers, and prepare Arc10 final-closure refresh inputs. | Slice03. |

## Arc Exit Criteria

Arc09 closes when:

- the required rich-card sections are explicitly designed and implemented in
  the owning `concept-cards` surfaces;
- templates and examples show how rich body sections coexist with v4
  lifecycle/evidence fields;
- validation or review guidance can detect missing rich sections, generic
  examples, stale wrapper artifacts, and lifecycle/evidence regressions;
- source/package version histories and discoverability surfaces are updated
  where affected;
- repository-local gates pass or failures are fixed and rerun;
- project ledger rows P-12 and P-13 are satisfied or explicitly blocked with
  operator-visible evidence;
- no runtime, RAG, graph, MCP, memory-admission, or full-book extraction claim
  is introduced.

## Version History

### v1.0 - 2026-09-11

Opened Arc09 after Arc08 CDC verification and operator acceptance of the
rich-card profile finding.

### v1.1 - 2026-09-11

Slice01 is CDC-verified and Slice02 is opened for bounded `concept-cards`
source updates. No Arc09 slice breakdown, sequencing, or scope change was
required.

### v1.2 - 2026-09-11

Slice02 is CDC-verified and Slice03 is opened for regression examples and
validation. No Arc09 scope or sequencing change was required; Slice03 uses the
regression protocol defined by Slice01.

### v1.3 - 2026-09-11

Slice03 is CDC-verified and Slice04 is opened for final package gates, package
inspection, and Arc09 closure inputs. No Arc09 scope or sequencing change was
required.

### v1.4 - 2026-09-12

Slice04 is CDC-verified and Arc09 is closed. CDC reproduced final repository
gates, package-path validation, archive integrity, archive content, caveat
retention, and Arc10 handoff readiness. Arc10 is opened for final Project05
closure refresh.
