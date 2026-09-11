# Concept Card References

These source-local references describe the record vocabulary and review
boundaries used by sibling templates and examples. They are guidance for
human-operated Markdown/YAML records, not a finalized executable schema,
validator, or evidence that a review occurred.

| Need | Reference |
| --- | --- |
| Group fields by record purpose | [Record Field Groups](./record-field-groups.md) |
| Use descriptive vocabulary consistently | [Vocabulary](./vocabulary.md) |
| Identify machine-checkable candidates and limits | [Structural Validation Candidates](./structural-validation-candidates.md) |
| Keep interpretive assessment out of structural checks | [Semantic Audit Boundaries](./semantic-audit-boundaries.md) |
| Escalate accountable decisions to a person or operator | [Operator Review Gates](./operator-review-gates.md) |

## Package Boundary

These files are live source support and are copied by the `concept-cards`
Makefile package target. They have not yet been independently installed into an
isolated destination. Arc05 retains docs/discoverability and install-smoke work.
The helpers copy only intended local support directories; they do not copy
`sources/`, workbench output, or planning artifacts.

## Method Boundary

Use `document-extraction` for raw PDF, EPUB, HTML, or converted-source cleanup.
Prepared outputs are upstream provenance only; they are not automatic claim
support, verification, or memory admission.
