# Arc08 Plan: Post-UAT Closure Refresh

```yaml
project: project05-concept-card-skill
arc: arc08-post-uat-closure-refresh
status: open
opened: 2026-09-11
depends-on:
  - arc07-real-corpus-uat-and-feedback
```

## Capability

Arc08 performs the post-UAT Project05 closure refresh. It reruns the final
repository-local gates after Arc07, inspects current generated packages,
reconciles the project ledger with Arc07 rows P-9 through P-11, records final
deferrals/follow-on boundaries, and formally closes Project05 if the evidence
still composes.

This arc must not defer either nondeferrable objective: live installable
`document-extraction` and `concept-cards` skills. It also must not turn the
Arc07 candidate-card packet into operator-accepted knowledge, semantic
verification, reconciliation, memory admission, retrieval evidence, or runtime
implementation.

## Dependencies

Arc08 consumes:

- closed Arc01 through Arc05 implementation/package evidence;
- Arc06 closure-baseline gates and project close packet;
- closed Arc07 real-corpus UAT, feedback disposition, ten-card candidate set,
  and RAG/graph/MCP handoff boundaries;
- current source tree and generated package behavior;
- Project05 project plan and ledger.

Arc08 may record acceptable follow-on work only for adjacent systems outside
Project05's nondeferrable objectives, including executable validators,
runtime services, graph or ontology databases, GraphRAG integrations, MCP
servers, memory runtime automation, retrieval evaluation, operator card
review, semantic verification, full-book extraction, CI expansion, and release
publishing outside repository-local gates.

## Slice Breakdown

| Slice | Scope | Dependencies |
| --- | --- | --- |
| Slice01: Final Gates And Project Closure Refresh | Rerun final gates, inspect current packages/install evidence as needed, reconcile project ledger rows P-2 through P-11 after Arc07, document final deferrals/follow-ons, and produce refreshed Project05 closure artifacts. | Arc07 close. |

## Arc Exit Criteria

Arc08 closes when:

- final repository gates pass or any failure is fixed and rerun;
- generated package contents for both Project05 skills are current and
  inspected;
- project ledger rows P-2 through P-11 are reconciled with reproduced
  evidence, explicit deferrals, or explicit no-op decisions;
- Arc07 UAT findings and RAG handoff boundaries are represented in the final
  project close without runtime or memory-admission overclaim;
- no key Project05 objective is deferred without an explicit operator
  decision;
- final Project05 closure records delivered capability, validation evidence,
  accepted warnings, operational incidents, remaining future work, and the
  candidate-card/operator-review boundary;
- source and planning worktrees are clean after commits.

## Version History

### v1.0 - 2026-09-11

Opened Arc08 after Arc07 close for post-UAT final gates, project ledger
reconciliation, explicit follow-on boundaries, and formal Project05 closure.
