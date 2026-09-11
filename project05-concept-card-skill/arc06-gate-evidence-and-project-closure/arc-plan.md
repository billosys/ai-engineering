# Arc06 Plan: Gate Evidence And Project Closure

```yaml
project: project05-concept-card-skill
arc: arc06-gate-evidence-and-project-closure
status: open
opened: 2026-09-11
depends-on:
  - arc05-packaging-docs-and-installability
```

## Capability

Arc06 performs the final Project05 closure pass. It reruns the final
repository-local gates, inspects the current generated packages, reconciles
the project ledger, records explicit acceptable deferrals/no-ops, and prepares
Project05 for formal closure.

This arc must not defer the nondeferrable objectives: live installable
`document-extraction` and `concept-cards` skills. If a final gate finds a
scope-relevant defect, fix it narrowly and rerun the affected checks before
proposing closure.

## Dependencies

Arc06 consumes:

- closed Arc01 through Arc05 plans, ledgers, CDC verifications, and closing
  reports;
- current source tree and generated package behavior;
- Project05 project plan and ledger;
- repository package, version, Markdown-path, and install validation gates.

Arc06 may record acceptable deferrals only for adjacent systems outside the
nondeferrable Project05 objectives, such as executable validators, runtime
services, graph/ontology databases, GraphRAG integrations, CCDP services,
memory runtime automation, CI expansion, and release publishing outside
repository-local gates.

## Slice Breakdown

| Slice | Scope | Dependencies |
| --- | --- | --- |
| Slice01: Final Gates And Project Closure | Run final gates, inspect current packages/install evidence as needed, reconcile project ledger rows P-2 through P-8, document acceptable deferrals/no-ops, and produce proposed Project05 closure artifacts. | Arc05 close. |

## Arc Exit Criteria

Arc06 closes when:

- final repository gates pass or any failure is fixed and rerun;
- generated package contents for both new skills are current and inspected;
- project ledger rows P-2 through P-8 are reconciled with reproduced evidence,
  explicit deferrals, or explicit no-op decisions;
- no key Project05 objective is deferred without an explicit operator decision;
- the final project closing report records delivered capability, validation
  evidence, accepted warnings, operational incidents, and remaining future work;
- source and planning worktrees are clean after commits.

## Version History

### v1.0 - 2026-09-11

Opened Arc06 after Arc05 closure for final Project05 gate evidence, ledger
reconciliation, explicit deferral/no-op statement, and project closure.
