# Capability Crosswalk

## Iteration 01 completeness index

`field-dispositions.json` is the machine-checkable companion: 169/169 parsed
top-level keys and 307 observed field paths are represented, with record-kind,
shape, concrete file/hash/value evidence and exact-path migration consequence.
Its inventory-only entries deliberately do not choose a schema; this readable
table supplies the evidence-based semantic groupings. Prose-defined fields from
the v3.2 prompts, current concept-cards references, and document-extraction
handoff/output contract were separately reviewed and appear in the source,
locator, support, lifecycle and body rows below.

These dispositions describe observed behavior, not a selected schema. `Preserve`
requires an explicit Arc02 answer; it does not mandate a legacy field name.

| Capability | Evidence | Disposition | Requirement / probe |
| --- | --- | --- | --- |
| Concept identity and aliases | Legacy `concept`/`slug`/`aliases`; modern `id`/`revision`/`title`/`concept_slug` | preserve, rename/relocate | Define stable source-safe identity and alias authority; test duplicate title/slug and revisions. |
| Category, subcategory, tier | Every legacy card; absent from modern template | preserve, redesign semantics | Retain values without imposing three levels on every domain; separate discovery classification from pedagogy. |
| Source title/slug/author | Every legacy card | preserve, split | Separate resource, contributors/roles, edition, capture, representation and citation. |
| Chapter/page/section | Legacy scalar/null trio; modern source/prepared refs | preserve, relocate | Typed snapshot-bound locator/span; no forced page/chapter for web/paper inputs. |
| Extraction confidence | Legacy scalar; modern mapping | preserve, scoped | Distinct from warrant, validation and verification; explicit unknown supported. |
| Claim source support | Legacy prose; modern claim/support refs | preserve, strengthen | Resolve claim-to-span support; bibliography/prepared source is not support. |
| Prerequisite traversal | Legacy slug list/body | preserve with typed projection | Directed supported edge plus practical query view; test fugue prerequisites, cycle, missing target, uncertainty. |
| Extends/related/contrast | Flat lists; prose relations in rich candidates | preserve, currently weakened | Edge semantics, direction/symmetry, ID, provenance, uncertainty and revision must be queryable. |
| CQs | Legacy text list; modern CQ records | preserve, strengthen | Separate question ID/text, coverage, answerability and evidence. |
| Rich teaching body | v3.2 required sections; richer rerun bodies | preserve and refine | Evaluate definitions, recognition/construction, examples, errors, relationship usefulness and fidelity together. |
| Lifecycle | Transitional scalars; current result refs | preserve without false promotion | Subject/revision/actor/authority required; one verified claim cannot verify/admit its card. |
| Prior value | v3.1/3.2 merge workflow; preservation records | preserve | Value inventory/disposition required; no silent overwrite. |
| Run provenance | Modern run/method/actor refs | preserve | Pin actual prompt/settings/snapshots and failed attempts. |
| YAML portability | Three preserved rich candidates fail parsing | absent / must be repaired later | Parser fixture for colon scalars, null/empty/missing and reference resolution. |

## Arc02 no-loss conclusions

1. Preserve a readable teaching surface and a directly queryable relationship/CQ
   surface; prose-only links and opaque pointers do not meet both.
2. Preserve historical values with migration dispositions; missing, empty, null,
   malformed and unknown differ.
3. Separate resource identity, preparation provenance, locator/span and support.
4. Keep evidence grade, extraction confidence, validation, verification,
   reconciliation, preservation and memory admission separately scoped.
