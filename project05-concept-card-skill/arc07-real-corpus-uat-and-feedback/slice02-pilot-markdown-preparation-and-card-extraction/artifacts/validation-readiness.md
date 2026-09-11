# Validation And Readiness

## Preparation Checks

| Check | Result | Evidence and limitation |
| --- | --- | --- |
| Pinned source identity | pass | Detached `HEAD`, tree, file hashes, and temporary path are in [source acquisition](./source-acquisition.md). |
| Pilot scope | pass | [Manifest](./prepared-source-manifest.md) and [structure map](./structure-map.md) name only declared Chapter 1 and Chapter 7 units. |
| Locator completeness | pass with caveat | Every candidate support span has a path, heading, source lines, and file identity; line locators require the pinned file hash. |
| Markdown readiness | pass | The source is already authored Markdown; no conversion or repair was necessary. |
| Figure dependencies | pass with bounded coverage | `fig_gears.png` and `fig_patsep_clr.png` were directly inspected; all other figures are outside the sample unless a candidate names them. |
| Citation and cross-reference dependencies | caveated | Citation keys and cross-references were identified where candidate context contains them, but cited works and destination chapters were not resolved. |

## Candidate Lifecycle Boundary

Candidate records may be structurally self-checked for required identity,
locator, support, and lifecycle fields. They are not independently verified,
reconciled, operator-accepted, or admitted to memory. Evidence grade is an
assistant assessment of the inspected source warrant; extraction confidence is
an independent assessment of this extraction act.

## Readiness Decision

The prepared sample is ready for a small candidate-card packet under the UAT
protocol. It is not ready for a whole-corpus run, bibliographic truth review,
or runtime ingestion. The unresolved citation and cross-reference dependencies
remain attached to the affected cards as caveats.
