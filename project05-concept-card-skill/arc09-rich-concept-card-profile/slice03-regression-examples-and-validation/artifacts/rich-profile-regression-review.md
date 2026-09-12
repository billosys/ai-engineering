# Rich Profile Regression Review

## Scope And Evidence

This review compares the Slice02 rich profile against three historical or
candidate shapes as evidence, not as schemas:

- `knowledge/concept-cards/templates/concept-card.md`
- `knowledge/concept-cards/examples/rich-profile-card.md`
- `/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/applied-chord.md`
- `knowledge/erlang/concept-cards/design-scale-erlang-otp/application-behaviour.md`
- Arc07 candidate `slice02-pilot-markdown-preparation-and-card-extraction/artifacts/candidate-cards/cc-memory-consolidation.md`

This is a same-context structural and comparative review. It does not verify
the warrant of a real-corpus assertion, accept any candidate card, reconcile
conflicts, admit memory, or assess retrieval/runtime behavior.

## Required-Section Coverage

The Slice02 template and synthetic rich example both contain all required
reader-facing sections. The grouped headings preserve the required meanings:

| Required affordance | Template and rich example | Result |
| --- | --- | --- |
| Concept boundary | `Concept Boundary` | present |
| Quick and core definition | `Quick Definition And Core Definition` | present |
| Prerequisites and key properties | `Prerequisites And Key Properties` | present |
| Construction / recognition | `Construction Or Recognition` | present |
| Context / application | `Context And Application` | present |
| Examples | `Examples` | present |
| Relationships and CQs | `Relationships And Competency Questions` | present |
| Common errors and confusions | `Common Errors And Common Confusions` | present |
| Source reference and support map | `Source Reference And Support Map` | present |
| Extraction notes and review boundaries | `Extraction Notes And Review Boundaries` | present |

The template requires an explicit `not applicable`, `not established in the
selected source`, or `unresolved` reason when a section cannot be populated.
The rich example demonstrates this in its error/confusion section and explains
that its source and control identities are fictional.

## Comparison With Applied Chord

The `applied-chord` card supplies the useful rich-reader pattern: quick/core
definitions, separate prerequisites and properties, construction and
recognition steps, context, two named examples, relationships, errors,
confusions, source reference, and a final verification-note section. The
Slice02 profile recovers each of those affordances, adding an explicit concept
boundary and a source/support map.

The old card's `Verification Notes` combines direct-definition provenance,
confidence rationale, and re-extraction history in one prose section. The
Slice02 `Extraction Notes And Review Boundaries` deliberately does not replace
claim/source-support, evidence grade, validation, verification,
reconciliation, preservation, operator review, or memory-admission records.
That is an improvement in control separation, not a claim that the historical
card was semantically incorrect.

## Comparison With Erlang Application Behaviour

The Erlang card has the same strong reader-facing affordances and adds a worked
code example. Its frontmatter and `Verification Notes` nevertheless present
legacy confidence and cross-reference wording in a form that does not expose
the v4 result-record boundaries. The Slice02 profile restores the useful
definitions, properties, procedure, context, examples, relationships,
confusions, and source route while requiring separate v4 control references.

The checked Erlang file ends with a trailing `</content>` response envelope.
Its fenced Erlang block is a legitimate worked-example code fence, not a
whole-card wrapper. The new rich template and example contain neither the
trailing envelope nor a whole-card Markdown fence, so the review confirms the
profile's wrapper-hygiene guidance addresses a concrete historical failure
mode.

## Comparison With Arc07 Candidate

Arc07's `cc-memory-consolidation.md` has strong v4 candidate controls: stable
identity/revision, source and prepared-source provenance, one claim with linked
support, extraction confidence, unassessed lifecycle fields, and an explicit
operator-review boundary. Its body is intentionally thin: boundary/summary,
claim/evidence, relationships/CQs, provenance, lifecycle, and handoff only.

The Slice02 profile adds the reader/reference affordances missing from that
candidate shape without changing its candidate status model. A future real
corpus card must retain Arc07-style source support and candidate/review limits;
the rich body does not convert a candidate into an accepted or admitted card.
No Arc07 card was edited or regenerated.

## Improvement, Limits, And Blockers

The current profile restores the older cards' navigable learning body while
making one-concept scope, source/support routing, explicit empty-section
reasons, and review limits visible. It preserves typed relationship/CQ and v4
lifecycle controls rather than putting those claims in a legacy verification
paragraph.

The synthetic example's source, locator, claim, support, edge, CQ, and run
paths are intentionally fictional and non-resolving. It therefore demonstrates
traceability shape, not real-source warrant or package-local reference closure.
This is not a direct Slice02 source blocker because the example labels itself
synthetic and makes no real-corpus support claim. Slice04 should retain this
limit when inspecting package contents, and future real-corpus examples need
recoverable source records before any semantic result is claimed.

No direct source correction is required by this review. Source surfaces remain
unchanged in Slice03.
