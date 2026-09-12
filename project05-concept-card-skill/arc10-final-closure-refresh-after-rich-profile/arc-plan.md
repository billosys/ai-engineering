# Arc10 Plan: Final Closure Refresh After Rich Profile

```yaml
project: project05-concept-card-skill
arc: arc10-final-closure-refresh-after-rich-profile
status: active
opened: 2026-09-12
depends-on:
  - arc09-rich-concept-card-profile
```

## Capability

Arc10 performs the final Project05 closure refresh after the accepted rich
concept-card profile refinement. It reruns the final repository-local gates,
inspects current generated packages, reconciles the project ledger through
Arc09, preserves all UAT and rich-profile caveats, and prepares Project05 for
formal closure if the evidence still composes.

This arc must not defer either nondeferrable objective: live installable
`document-extraction` and `concept-cards` skills. It also must not convert
planning, package, regression, or candidate-card evidence into operator card
acceptance, semantic verification, reconciliation, preservation, memory
admission, retrieval quality, graph/RAG/MCP implementation, runtime ingestion,
or full-book extraction.

## Dependencies

Arc10 consumes:

- closed Arc01 through Arc05 implementation/package evidence;
- Arc06 closure-baseline evidence;
- closed Arc07 real-corpus UAT, feedback disposition, candidate-card set, and
  RAG/graph/MCP handoff boundaries;
- Arc08 post-UAT closure baseline;
- closed Arc09 rich-profile design, source, regression, package, and caveat
  evidence;
- current source tree and generated package behavior;
- Project05 project plan and ledger.

Arc10 may record follow-on work only for adjacent systems outside Project05's
nondeferrable objectives, including executable validators, runtime services,
graph or ontology databases, GraphRAG integrations, MCP servers, memory runtime
automation, retrieval evaluation, operator card review, semantic verification,
full-book extraction, CI expansion, and release publishing outside
repository-local gates.

## Slice Breakdown

| Slice | Scope | Dependencies |
| --- | --- | --- |
| Slice01: Final Gates And Project Closure Refresh | Rerun final gates, inspect current packages, reconcile project ledger rows P-1 through P-13 after Arc09, document final follow-on boundaries, and produce refreshed Project05 closure artifacts. | Arc09 close. |

## Arc Exit Criteria

Arc10 closes when:

- final repository gates pass or any failure is fixed and rerun;
- generated package contents for both Project05 skills are current and
  inspected;
- Project05 ledger rows P-1 through P-13 are reconciled with reproduced
  evidence, explicit deferrals, or explicit no-op decisions;
- Arc07 UAT findings, Arc07 RAG handoff boundaries, and Arc09 rich-profile
  caveats are represented in the final project close without runtime,
  memory-admission, or card-acceptance overclaim;
- no key Project05 objective is deferred without an explicit operator
  decision;
- final Project05 closure records delivered capability, validation evidence,
  accepted warnings, operational incidents, remaining future work, and
  candidate-card/operator-review boundaries;
- source and planning worktrees are clean after commits.

## Version History

### v1.0 - 2026-09-12

Opened Arc10 after Arc09 CDC closure for final Project05 closure refresh.
