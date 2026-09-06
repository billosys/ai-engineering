# Slice02 Plan: Extraction, Re-Extraction, And Provenance

```yaml
project: project05-concept-card-skill
arc: arc03-concept-cards-skill-core
slice: slice02-extraction-reextraction-provenance
status: open
opened: 2026-09-06
depends-on:
  - slice01-source-scaffold-and-load-contract
```

## Goal

Implement the source-faithful extraction and re-extraction/provenance core of
`concept-cards`. This slice turns the scaffold's future routes into detailed
guides for deriving cards and claims from sources, comparing new extraction
against prior cards, preserving prior value, and recording source spans,
source support, and extraction-run provenance without implementing the later
evidence lifecycle, validation/verification, relationship/CQ, reconciliation,
memory-admission, template/example, or package surfaces.

## Scope

In scope:

- add `knowledge/concept-cards/guides/03-extraction.md`;
- add `knowledge/concept-cards/guides/04-re-extraction-preservation.md`;
- update `knowledge/concept-cards/SKILL.md` so guides 03 and 04 are live;
- update `knowledge/concept-cards/version-history.md`;
- advance the source skill version from `1.0.0` to `1.1.0`;
- define source-faithful extraction workflow, including concept boundaries,
  claim identification, excerpt discipline, source locator/span capture,
  source support assertions, extraction confidence, and extraction-run
  provenance;
- define re-extraction workflow, including source-primary comparison against
  existing cards, changed/unchanged/absent source treatment, preservation
  decisions, old-card unique value, unsupported prior claims, and unresolved
  material;
- keep `document-extraction` outputs as upstream provenance when preparation
  records are present.

Out of scope:

- implementing `05-evidence-lifecycle.md` or any later guide;
- defining final templates, examples, schema files, validation/reference
  support directories, or executable validators;
- adding package, Makefile, README, docs, generated zip, or install wiring;
- performing live extraction against a real corpus;
- implementing runtime services, graph or ontology databases, GraphRAG, CCDP
  services, memory runtime automation, or cross-skill package behavior;
- recreating `knowledge/concept-card-method/` or `knowledge/source-preparation/`.

## Required Design Pressure

The guides must be useful enough for human-assisted and agent-direct operation.
They should give stepwise instructions an assistant can follow directly when
source files are accessible, while also supporting a human operator who must
provide excerpts, locators, prior-card observations, or checks.

The extraction guide must keep these concepts distinct:

- concept card versus claim;
- source locator versus source span;
- source support versus bibliography, prepared-source provenance, and
  extraction confidence;
- source statement versus assistant inference;
- extraction run provenance versus source support;
- extraction confidence versus evidence grade.

The re-extraction guide must preserve Project03's source-primary rule: new
extraction is compared against the source first, then against prior cards as
comparison inputs. Prior-card value can be preserved, superseded, rejected, or
left unresolved, but it cannot disappear silently.

## Exit Criteria

Slice02 is complete when:

- guides 03 and 04 exist and are routed as live from `SKILL.md`;
- `SKILL.md` and `version-history.md` agree on version `1.1.0`;
- guide 03 covers source snapshot/prepared-source inputs, extraction run
  identity, concept/card boundary selection, claim extraction, source locator
  and span capture, support assertions, extraction confidence, inference
  boundaries, caveats, and handoff output;
- guide 04 covers prior-card inventory, source-primary comparison,
  preservation decisions, source drift, unsupported prior material,
  unresolved material, re-extraction run provenance, and handoff output;
- guides 03/04 support both human-assisted and agent-direct use;
- later guide/support/package/runtime work remains explicit future scope;
- no old roots, templates/examples, package/docs/install changes, executable
  validators, or runtime behavior are added;
- focused validators and local Markdown link checks pass.

## Expected Artifacts

No separate durable planning artifacts are expected. Implementation output is
the source files listed above. Durable close evidence belongs in this slice's
`closing-report.md`, `ledger.md`, and later `cdc-verification.md`.
