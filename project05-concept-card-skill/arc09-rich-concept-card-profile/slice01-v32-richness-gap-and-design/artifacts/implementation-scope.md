# Slice02 Implementation Scope

| Owning surface | Expected change |
| --- | --- |
| `SKILL.md` | Make the rich real-corpus profile discoverable. |
| `guides/01-load-contract.md`, `guides/03-extraction.md` | Define rich-section default, applicability, one-concept boundary, source-specific examples, and preparation routing. |
| `guides/02-operator-workflow.md`, `guides/04-re-extraction-preservation.md` | Add rich-section review/re-extraction handling without weakening lifecycle or preservation boundaries. |
| `guides/05-evidence-lifecycle.md`, `guides/06-graph-cq.md`, `guides/08-validation-verification.md` | State that rich prose never replaces support, typed edges/CQs, evidence, validation, verification, or review. |
| `templates/concept-card.md` | Add rich sections and v4-aware placeholders; replace overloaded verification-note wording. |
| `examples/` | Add or revise a rich source-backed synthetic example with linked v4 records and no completed-review claim. |
| `references/structural-validation-candidates.md`, `references/semantic-audit-boundaries.md`, `references/operator-review-gates.md` | Add checks for rich sections, source-specific examples, wrappers, and lifecycle/evidence separation. |
| `version-history.md` | Record the matching compatible capability change. |

## Version And Package Implications

Slice02 should assess a minor `concept-cards` version increment and update `metadata.version` with sibling history. Existing packaging already includes guides, templates, examples, and references; no Makefile change is expected unless a new support-directory class is added. Changed metadata requires `make check-skills` and `make check-skill-versions`; changed paths require `make check-package-paths`; fresh package inspection belongs to the assigned gate slice.

## Optional `document-extraction` Touchpoint

No change is planned. A direct blocker must be evidenced before touching it, such as an inability to retain a recoverable locator for a source-specific example. Preparation/locator/citation caveat contracts otherwise remain sufficient upstream provenance.

## Outside Slice02

Do not regenerate Arc07 cards, process the full book, accept or independently verify cards, reconcile/admit memory, or build graph/RAG/MCP/retrieval/runtime infrastructure. Slice03 owns regression proof; Slice04 owns package gates and Arc10 inputs.
