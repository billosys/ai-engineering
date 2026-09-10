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

These files are live in the source skill but are not yet a packaged surface.
The current `pack_skill` and `pack_component_skill` helpers copy `guides/`,
`templates/`, and `examples/`, not `references/`. Arc05 must wire and validate
this directory before any generated-zip or installation claim. Do not relocate
these records under `guides/` merely to evade that package work.

## Method Boundary

Use `document-extraction` for raw PDF, EPUB, HTML, or converted-source cleanup.
Prepared outputs are upstream provenance only; they are not automatic claim
support, verification, or memory admission.
