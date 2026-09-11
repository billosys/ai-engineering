# Arc04 Closing Report

```yaml
status: closed
closed-by: CDC
closed-on: 2026-09-10
```

## Capability

Arc04 was planned to implement the `concept-cards` support surfaces that make
the Arc03 core guides directly usable: sibling templates, representative
examples, schema/reference material, and validation review surfaces, all in the
current `knowledge/concept-cards/` layout.

Arc04 delivered that capability at source level. It did not attempt package,
docs, install, generated-zip, executable validator, runtime graph, memory
runtime, CCDP service, live-corpus extraction, or old-root revival work; those
remain outside Arc04 and, where applicable, are assigned to Arc05.

## Slice Walk

| Slice | Outcome | Evidence |
| --- | --- | --- |
| Slice01: Record Template Foundation | delivered | CDC verified twelve sibling templates under `knowledge/concept-cards/templates/`, entrypoint routes, version/history update, and focused validation against source commit `979ead0d74bed09106c5a4bb62adb1c9978a1bbd`. |
| Slice02: Representative Examples | delivered | CDC verified eight sibling examples under `knowledge/concept-cards/examples/`, entrypoint routes, bounded handoff wording, version/history update, and focused validation against source commit `c890990525cfda965f04b291c487d897c0e365d6`. |
| Slice03: Schema Reference And Review Surfaces | delivered | CDC verified six sibling reference files under `knowledge/concept-cards/references/`, entrypoint routes, bounded guide handoffs, version/history update, Arc05 package-support handoff, and focused validation against source commit `6f3e6b0ec02d03adc41be6abc559511e4d87d0e2`. |

## Composition Check

The slices recompose into the Arc04 capability:

- `templates/` supplies the twelve fillable record shapes for cards, claims,
  support, locators, relationship edges, CQs, extraction runs, validation,
  verification, reconciliation, preservation, and memory admission.
- `examples/` supplies the eight planned synthetic examples: minimal card,
  claim-backed card, CQ coverage, relationship edge, extraction-run trace,
  reconciliation, memory admission, and parallel-worker default recipe.
- `references/` supplies the source-local field groups, vocabulary,
  deterministic structural candidates, semantic audit boundaries, and operator
  review gates needed to use and review the templates/examples without turning
  them into executable schemas or runtime claims.
- The source surfaces preserve Arc03 construct distinctions: endpoint support
  remains separate from edge support; CQ coverage remains separate from
  answerability/retrieval; validation remains structural; verification remains
  semantic; reconciliation, preservation, and memory admission remain separate
  lifecycle decisions.
- Document cleanup remains routed to `document-extraction`; prepared source
  outputs are upstream provenance, not automatic source support or claim
  warrant.
- Arc04 source wording records that package targets, generated zips,
  docs/discoverability, install behavior, and package validation remain Arc05.

No arc-scale silent drop was found.

## Arc Ledger Walk

| Row | Final status | Evidence |
| --- | --- | --- |
| A4-1 | done | Slice01 CDC verification reproduced all seven Slice01 rows and direct inspection confirmed the twelve live sibling templates. |
| A4-2 | done | Slice02 CDC verification reproduced all eight Slice02 rows and direct inspection confirmed the eight live sibling examples. |
| A4-3 | done | Slice03 CDC verification reproduced all nine Slice03 rows and direct inspection confirmed the six live sibling reference/review files. |
| A4-4 | done | Arc-scale inspection across templates, examples, and references confirmed preservation of the Arc03 construct and lifecycle distinctions. |
| A4-5 | done | Arc-scale inspection confirmed raw document cleanup routes to `document-extraction` and prepared outputs are upstream provenance only. |
| A4-6 | done | Arc-scale source-scope review confirmed no package/docs/install/runtime work, generated zips, executable validators, old roots, runtime graph, memory runtime, CCDP service, or live-corpus extraction was claimed as complete. |
| A4-7 | done | Slice02 and Slice03 CDC verification confirmed availability/handoff wording stayed current as templates, examples, and references landed, while Arc05 boundaries remain explicit. |

Rows: 7. Done: 7. Deferred: 0. No-op: 0.

## Accumulated Plan Changes

- Arc04 v1.1 recorded that Slice01 surfaced stale guide availability wording
  for newly live templates and assigned bounded cleanup to Slice02.
- Arc04 v1.2 recorded that Slice02 closure and package-behavior inspection
  clarified the `references/` placement and the Arc05 package-support
  requirement.

Both changes expanded or clarified planned Arc04 work without reducing scope or
re-sequencing the project roadmap.

## Bubble-Up To Project

Arc04 delivered the capability assigned by `project-plan.md`: concept-card
templates, examples, schema/reference material, and validation review surfaces
using Project03 v4.0 semantics in the current post-Project04 sibling layout.

Arc04 confirms, rather than changes, the Project05 roadmap: Arc05 must wire
both `document-extraction` and `concept-cards` into package targets, docs,
generated zips, install behavior, and package validation. The specific
`references/` support-directory requirement should be included in Arc05 source
scope because current packaging helpers do not copy that directory.

No project roadmap re-sequencing, scope reduction, or new arc is required.
