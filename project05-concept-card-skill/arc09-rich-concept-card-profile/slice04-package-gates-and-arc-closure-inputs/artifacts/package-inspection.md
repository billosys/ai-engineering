# Arc09 Package Inspection

## Freshness And Integrity

The archives inspected here were rebuilt by the final
`make check-package-paths` run. `unzip -tqq` passed for both archives. Their
entry counts and checksums are recorded in [final gate evidence](./final-gate-evidence.md).

## Concept-Cards Archive

`target/skills/concept-cards.zip` contains all Arc09 rich-profile surfaces:

- `concept-cards/SKILL.md`, whose packaged metadata is version `1.8.0` and
  whose body defaults real-corpus extraction to the rich readable profile;
- `concept-cards/version-history.md`;
- `concept-cards/templates/concept-card.md`;
- `concept-cards/examples/rich-profile-card.md`;
- `concept-cards/guides/01-load-contract.md`;
- `concept-cards/guides/02-operator-workflow.md`;
- `concept-cards/guides/03-extraction.md`;
- `concept-cards/guides/04-re-extraction-preservation.md`;
- `concept-cards/guides/05-evidence-lifecycle.md`;
- `concept-cards/guides/06-graph-cq.md`;
- `concept-cards/guides/08-validation-verification.md`;
- `concept-cards/references/structural-validation-candidates.md`;
- `concept-cards/references/semantic-audit-boundaries.md`; and
- `concept-cards/references/operator-review-gates.md`.

The archive contains 44 entries total, including the expected sibling
directories and unmodified concept-card support files. The package inspection
therefore confirms that the rich profile is delivered through the generated
archive, not merely present in source.

## Document-Extraction Boundary

`target/skills/document-extraction.zip` contains 28 entries and its manifest
has no `concept-cards`, `rich-profile`, or `arc09` path. A source diff from the
Slice02 rich-profile baseline (`1d6bbd08`) to the current source head contains
no `knowledge/document-extraction` path. Arc09 therefore did not silently
couple document preparation to the rich-profile package change.

This boundary does not alter the documented routing: `concept-cards` may use
document-extraction outputs as upstream provenance, but the two package roots
remain independent.
