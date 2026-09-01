# v4.0 Deferral Register

```yaml
project: project03-concept-card-method
arc: arc05-implementation-plan
slice: slice05-implementation-plan-synthesis
artifact: v40-deferral-register
status: proposed-done
```

## Purpose

This register records deferred work with owner, rationale, and re-entry
condition. It prevents the implementation plan from implying source
implementation, release readiness, runtime services, or generated release
artifacts that Project03 did not authorize.

## Deferred Work

| Deferred item | Owner | Rationale | Re-entry condition |
|---------------|-------|-----------|--------------------|
| executable validator-code | future implementation owner | Slice03 accepted documentation-only validator scope for the first implementation plan; deterministic candidates need implementation language, path handling, tests, and failure-output decisions before code exists. | A later implementation slice explicitly accepts validator-code scope, source path, language, tests, and failure-message contract. |
| validator-code tests | future implementation owner | Tests for executable validator-code cannot exist before validator-code is accepted. | Re-enter with executable validator-code implementation or with a documentation-only example parser accepted as scope. |
| runtime services | future runtime owner | Project03 plans a method skill, not a runtime system. | Re-enter only when a runtime project defines service responsibilities, interfaces, operators, evidence, and safety gates. |
| GraphRAG | future retrieval owner | GraphRAG retrieval quality is outside the documentation skill and cannot be proven by templates alone. | Re-enter when a retrieval system, corpus, query set, expected answer criteria, and evaluation gate are accepted. |
| graph database | future graph owner | Arc03 defined graph-native edge semantics but did not authorize a graph database. | Re-enter when a graph storage project owns schema, persistence, migration, import/export, and consistency checks. |
| ontology database | future ontology owner | The v4.0 method can critique ontology structure without implementing an ontology database. | Re-enter when ontology storage, query, validation, and curation workflows are accepted. |
| memory runtime | future memory owner | Memory admission is a method decision surface, not an automated memory runtime. | Re-enter when a memory runtime project defines substrate format, admission enforcement, contradiction handling, and rollback evidence. |
| CCDP service | future protocol/runtime owner | Project03 stays CCDP-compatible in evidence language but does not implement a CCDP service. | Re-enter when a CCDP service project accepts transport, requester/provider roles, evidence exchange, and validation gates. |
| live extraction | future extraction-runtime owner | Live extraction behavior requires source access, workflow safety, operator controls, and reproducible runtime evidence. | Re-enter when a live extraction project defines accepted inputs, outputs, source permissions, validation, and operator review gates. |
| package release | future release owner | Arc05 plans package mechanics and release gates but does not perform a package release. | Re-enter after implementation passes release gates and an operator explicitly authorizes package release. |
| generated release artifact | future release owner | Generated zips are local build artifacts under current ignore policy, not committed release artifacts. | Re-enter when release policy names which generated artifact is published, where it is stored, and which checksum/provenance evidence is required. |
| CI changes | future implementation or release owner | Current Arc05 plans local gates; CI changes need broader repository policy. | Re-enter when an implementation or release slice accepts CI surface, runtime cost, and failure policy. |
| package-path exception rows | future packaging owner | The package-compatible `guides/` layout should avoid exceptions by default. | Re-enter only for intentional source-only or excluded links with package, document, target, classification, disposition, reason, source, and expires. |

## Non-Deferrals

These items are not deferred from Slice05 because they are delivered as
planning artifacts:

- implementation plan;
- source edit sequence;
- verification gate matrix;
- implementation-slice recommendations;
- Project03 close input.

## Boundary

Deferred work is not a silent drop. Every deferred item above has an owner,
rationale, and re-entry condition. None of the deferred items are implemented
or released by this planning slice.
