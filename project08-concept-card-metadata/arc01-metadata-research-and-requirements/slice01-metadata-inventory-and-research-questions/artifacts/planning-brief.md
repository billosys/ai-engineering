# Project08 Planning Brief

Planner-authored input, 2026-09-12. This preserves the operator's accepted
direction and research questions; it is not a completed inventory, standards
review or approved field schema.

## Operator Direction

Early concept cards carried rich teaching bodies and structured relationship
metadata that enabled immediate graph ingestion and useful prerequisite queries,
such as what a musician must master before writing a Baroque fugue. Later method
work improved evidence controls but may have weakened that usefulness. Preserve
both, and apply the inquiry to the whole metadata profile.

Classification should generalize beyond `category`, `subcategory`, `tier` without
losing their historical information. Consider tags, taxonomies, concept schemes
and established knowledge-organization methods through research.

Generalize `source`, `source_slug`, `authors`, `chapter`, `chapter_number`,
`pdf_page`, `section` across source types and formats while retaining each
meaningful data point. Distinguish the authored resource, version/edition,
retrieved snapshot, prepared representation and the cited span. Consider multiple
sources, contributors/roles, identifiers, language, rights and mutable web content
as research questions, not already-required field names.

Recover directly queryable meanings for `prerequisites`, `extends`, `related`,
`contrasts_with` and any other discovered relationships. Preserve provenance and
uncertainty per edge, direction and identity. Investigate convenient frontmatter
alongside richer edge records, including a clear authority rule to prevent drift.

Revisit `answers_questions` and `cq_refs`: question text, competency-question
identity, coverage and answerability are different information. Choose readable
names and preserve useful historical questions without asserting unsupported
answerability.

Review `evidence_grade`, `extraction_confidence`, `validation_state`,
`verification_state`, `reconciliation_state`, `preservation_state`,
`memory_admission` and their references together. Determine actual scope and
information retention rather than mandating a misleading card-wide scalar.
Make state versus reference understandable, with actor, subject, revision,
evidence and unknown/conflicting/stale-state behavior traceable.

Also inventory identity, aliases, timestamps, run/method provenance, all nested
fields and any unanticipated metadata. Exact field compatibility and preserved
meaning/query behavior are separate questions, both needing evidence.

Bodies remain open to revision: concrete examples, common errors, construction
and recognition, rich relationships, source fidelity and concise teaching prose
are part of the quality target. The historical corpora are useful comparisons,
not unquestioned truth or templates whose defects should be copied.

## Starting Architecture Hypothesis

A card could expose practical concept/discovery/relationship metadata and a
readable teaching body, while retaining scoped claim, source-support, provenance
and lifecycle records. Research whether embedded structures, references, or a
combination make the card portable and directly queryable. Specify authorities,
synchronization, missing-target behavior and migration before adopting redundant
fields. Do not interpret this hypothesis as permission to hide useful data behind
opaque pointers or to remove evidence detail for readability.

Candidate research families include W3C SKOS, Dublin Core metadata/application
profiles, Library of Congress BIBFRAME, W3C PROV-O, locator models and ontology
requirements methods such as NeON. Slice02 must consult primary sources and record
citations, applicable ideas, limitations and alternatives. No standards-compliance
claim or vocabulary adoption has been made by this brief.

## Evidence Starting Points

Paths prefixed `knowledge/` or `workbench/` are relative to the source checkout;
`old/` and `project05-.../` are relative to the planning checkout.

- `knowledge/concept-cards/`: live entrypoint, ten guides, templates, examples,
  reference/review material and version history; baseline 4.8.1.
- `knowledge/document-extraction/`: source/preparation handoff definitions.
- `old/dev/concept-cards/0009-howto-concept-card-extraction-with-claude-code-v3.2.md`.
- `old/dev/concept-cards/0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md`.
- Other `old/dev/concept-cards/` definitions and predecessor prompts, discovered
  by content rather than assuming a filename is the complete metadata contract.
- `/Users/oubiwann/lab/music-comp/ai-music-theory/concept-cards/complete-musician/`;
  initial body comparisons included `appoggiatura.md`, `structural-analysis.md`,
  `invertible-counterpoint.md`, and `pivot-area.md`.
- `knowledge/erlang/concept-cards/design-scale-erlang-otp/`: reported v3.2-derived
  corpus. Inspect actual source/provenance before assigning exact method history.
- `project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/`: pilot,
  expanded subset and handoff evidence; follow its slice paths to actual cards.
- `project05-concept-card-skill/arc09-rich-concept-card-profile/`: earlier profile
  research, implementation and regression evidence.
- `workbench/compcogneuro-rich-rerun-2026-09-12/` and
  `workbench/compcogneuro-teaching-rerun-2026-09-12/`: ignored local card sets,
  indexes and comparisons. Preserve baseline copies before relying on durability.

The prior CompCogNeuro input was `CompCogNeuro/book` snapshot
`e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d`, `chapter-01.md` lines 31-60 and
`chapter-07.md` lines 5-166. Verify the snapshot and content when preparing actual
trials. The temporary checkout may not persist. Ten historical candidates are a
comparison set, not proof that the subset has exactly ten concepts.

## Decisions To Preserve

- Name: `project08-concept-card-metadata`; five arcs are a starting hypothesis.
- Released version continuity: current 4.8.1, intended metadata work in 4.9.x.
- Arc04 may be long and gain arbitrarily many bounded slices, including source
  changes to body and metadata, informed by multiple separate CC extraction runs.
- Evaluate real outputs and useful queries, not just field/heading presence.
- Once subset quality is accepted, carry out the entire-book goal; if quality
  still misses, continue skill refinement and reruns within this project.
- Formal closure must account for observed shortcomings and operator acceptance;
  historical package success cannot substitute for these outcomes.
