# Relationship Semantics Evidence

Historical v3.2 card-local `prerequisites`, `extends`, `related`, and
`contrasts_with` are typed relationship assertions encoded as slug lists. The
current graph guide says prerequisite lists reverse traversal (B -> A),
extension is A -> B, and related/contrast are symmetric. The old prompt gives
`contrasts_with` the specific common-confusion reading; the guide's qualified
comparison is broader and is not silently substituted for that legacy meaning.
Slugs are not stable endpoint identity, revision, or edge warrant.

The current edge template separates relation identity, endpoint roles,
direction/inverse/symmetry, edge support and closure. Its populated `precedes`
example is synthetic: endpoint validity or support cannot warrant an edge.
`relationship_type` and `relation_type` are observed distinct names, not
established equivalents. Relationship prose helps readers but cannot invent an edge.

## Census and Bounded Comparisons

The frozen inventory supplies the type/shape census: the eight legacy members
are untyped list roots/items; 21 are relationship-edge root or nested mapping
components; and six are concept-card edge-reference components. It records
absence separately from the null/unassessed template fields and from the empty
reference collections in generated-card contexts. The minimal-card example
uses `relationship_edge_refs`, while the current card template/rich profile
uses `relationship_refs`; that naming difference is preserved as observed
usage, not normalized as equivalence.

Both complete v3.2 prompts were read as historical evidence. They establish
the older readable-list convention, but do not override the current template,
guide, or frozen transition assignment. The synthetic edge body explicitly
labels itself as an example. Accordingly, comparing its declared endpoint and
support references with available targets establishes only that the declaration
is shaped as a reference: it does not establish target existence, anchor
resolution, revision inheritance, relation truth, or source-span adequacy.

Concrete consequences are: a reader can render documented orientation and
symmetric lookup without creating reciprocal records; a query layer must keep
edge support separate from endpoint resolution; an extractor/migration must
retain absent/null/empty/malformed distinctions and the two reference names;
and a future resolver needs an explicit policy for literal path anchors and
requested revisions.

## Retained Iteration 02 Witnesses

The populated synthetic edge's `from_ref` exactly matches minimal-card's
`cc-prepared-source-provenance`, revision 1; its `to_ref` exactly matches
claim-backed-card's `cc-claim-support-is-assertion-specific`, revision 1.
Both are inspected declarations, not validation of relation truth. The edge's
support ID has no native path, and a bounded `knowledge/concept-cards/examples`
search finds no record declaration for it. Rich-profile's different edge request
and its own `support-evidence-map-definition-001` card-support declaration are
therefore not substituted for the edge example's support.

`accented-incomplete-neighbor` is the populated extension witness: it extends
`incomplete-neighbor`, whose local filename exists; the documented traversal is
AIN -> incomplete-neighbor and the inverse is a reader statement, not another
record. It and `appoggiatura` reciprocally list each other in native `related`
arrays, exercising a symmetric lookup without creating a new assertion. Their
contrast fields retain the historical commonly-confused semantics; the current
guide's qualified comparison remains a separate broader convention.

The frozen inventory retains three malformed rich-card records as excluded
limits: they are neither parsed absence witnesses nor negative semantic data.

## Repaired Census And Named Reads

The frozen inventory has 2,054 eligible parsed legacy mappings (390 Complete
Musician and 1,664 Erlang), 31 concept-card mappings, and two relationship-edge
mappings. Legacy mappings have `values` objects but no literal `record_kind`;
this census normalizes them to `untyped` only after that parsed-mapping test.
For Music all four selected fields are present arrays: prerequisite 5 empty/385
nonempty; extends 180/210; related 16/374; contrasts 262/128. For Erlang,
prerequisites and related are present in 1,664 records (one null each);
contrasts is present in 1,664 (three null); extends is absent in 66 and present
as arrays in 1,598. This preserves null and absence rather than treating either
as an empty list.

`accent-types.md` declares prerequisite `meter`, related `tonal-hierarchy` and
`syncopation`, and empty extension/contrast lists; its body says metric accent
derives from the metric framework. `behaviour.md` declares prerequisite
`supervision-tree`, three related slugs and empty extension/contrast lists;
its body calls behaviours formalizations of common process patterns. Both named
slug targets exist at the registered paths, so these are successful bounded
filename lookups, not claims of globally stable identity, revision, or support.

Among the 31 current cards, `relationship_edge_refs` is present once as an
empty array (minimal-card) and absent 30 times; `relationship_refs` is present
seven times (six empty, rich-profile with one mapping) and absent 24 times.
The two edge records are a null/unassessed template and a populated synthetic
`precedes` record. Rich profile requests `edge-evidence-map-related-to-claim`,
revision 1, path `records/edge-evidence-map-related-to-claim.md`; that target is
not found at the declared source-root path. Its separate card support request
is `support-evidence-map-definition-001`; it is not the populated edge's
pathless `support-synthetic-edge-001`. The missing edge target is a bounded
lookup outcome, not a claim that all record roots or anchors are invalid.

## Historical Policy Versus Frozen Observation (Slice12 R5)

The registered historical authorities establish two related but distinct rule
scopes. `v32Parallel` documents an explicit prerequisite rule at its extraction
guidelines (`0010-a-guide-for-parallel-concept-card-re-extraction-v3.2.md:585-610`):
every non-foundational concept needs prerequisites, while its required-frontmatter
reference (`:877-893`) marks `prerequisites` required and permits an empty list
for foundational concepts. The same quality section says all frontmatter fields
must be populated, using `null` or an empty array where not applicable. The
earlier `v32Howto` audit (`0009-howto-concept-card-extraction-with-claude-code-v3.2.md:573-592`)
lists `prerequisites`, `extends`, `related` and `contrasts_with` among the
missing fields and requires conformance to the v3 template. The first rule is
therefore narrower and explicit; the latter instructions are broader
all-field/template-conformance guidance, not four separately stated
relationship-specific requiredness rules.

| Legacy root and item list | Documented historical rule and scope | Frozen observed states and item lists | Lineage/conformance limit | Future-policy question |
| --- | --- | --- | --- | --- |
| `prerequisites`, `prerequisites[]` | Non-foundational concepts need prerequisites; foundational concepts may use an empty list. The broader all-frontmatter rule permits `null`/empty where not applicable. | Music: present 390; null 0; empty 5; populated 385; 620 string items / 183 distinct. Erlang: present 1,664; absent 0; null 1; empty 306; populated 1,357; 2,282 string items / 586 distinct. | The census cannot recover whether each card was generated under the rule or whether a concept was foundational. The null witness is not evidence that no conceptual dependency exists. | Decide after P-15 whether and how a future contract expresses applicability, foundational status, missing/null/empty states and migration without silently adopting v3.2. |
| `extends`, `extends[]` | Named by the broader all-frontmatter/template-conformance guidance; no separate relation-specific requiredness rule is stated in the registered passages. | Music: present 390; absent/null 0; empty 180; populated 210; 210 string items / 88 distinct. Erlang: present 1,598; absent 66; null 0; empty 1,289; populated 309; 314 string items / 162 distinct. | Absent Erlang keys may reflect lineage, applicability or nonconformance; the frozen records do not distinguish those causes. Items remain legacy slugs without edge support or revision. | Decide whether a future profile requires, omits, nulls or empties this relation by source/card applicability, and what migration preserves the distinction. |
| `related`, `related[]` | Named by the broader all-frontmatter/template-conformance guidance; its relationship meaning is symmetric association without dependency implication. | Music: present 390; null 0; empty 16; populated 374; 752 string items / 331 distinct. Erlang: present 1,664; absent 0; null 1; empty 21; populated 1,642; 4,065 string items / 1,239 distinct. | Presence and item counts do not establish universal conformance, reciprocal storage requirements or edge truth. The null witness remains distinct from an empty list. | Decide future requiredness and reciprocal representation separately from the preserved symmetric reader behavior. |
| `contrasts_with`, `contrasts_with[]` | Named by the broader all-frontmatter/template-conformance guidance; the historical relationship meaning is commonly confused concepts, not the current guide's broader qualified comparison. | Music: present 390; null 0; empty 262; populated 128; 148 string items / 107 distinct. Erlang: present 1,664; absent 0; null 3; empty 1,133; populated 528; 643 string items / 385 distinct. | Observed null/empty states do not prove absence of contrast or universal conformance. Legacy item slugs do not supply edge-scoped support. | Decide whether the future profile retains the common-confusion distinction, how it represents qualified comparisons, and which applicability/requiredness policy is accepted. |

The matrix is an interpretation of registered rules and the frozen census, not
a future schema proposal. It preserves absent, null, empty and populated
states, does not claim universal historical conformance or individual lineage,
and leaves requiredness, applicability, migration and specification format to
the operator's P-15 discussion.

## Literal Selected-Field Census (Iteration 04)

The following is the selected-field census, not a membership count. It is
computed from the frozen inventory's parsed `values` objects. That inventory is
the preserved copy; each record's `path` and SHA-256 map it back to the original
input. The additional witnesses below were read directly from their originals;
no new copy, corpus edit, or extraction was made. `absent` means an absent key,
not a lookup returning null. `empty` is an existing zero-length array.

| Selected legacy pairs | Complete Musician (390 mappings) | Erlang (1,664 mappings) | Value/component distinction |
| --- | --- | --- | --- |
| `prerequisites`, `prerequisites[]` | present array 390; null 0; empty 5; populated 385 | present 1,664; array 1,663; null 1; empty 306; populated 1,357; absent 0 | all populated items are strings: 620 occurrences/183 distinct Music targets; 2,282/586 Erlang. The null witness is `data-type-sizes.md`. |
| `extends`, `extends[]` | present array 390; null/absent 0; empty 180; populated 210 | present array 1,598; absent 66; null 0; empty 1,289; populated 309 | all populated items are strings: 210 occurrences/88 distinct Music targets; 314/162 Erlang. `allocation-strategy.md` is the inspected absent-key witness. |
| `related`, `related[]` | present array 390; null/absent 0; empty 16; populated 374 | present 1,664; array 1,663; null 1; empty 21; populated 1,642; absent 0 | all populated items are strings: 752 occurrences/331 distinct Music targets; 4,065/1,239 Erlang. `sc-hbase-protocol.md` is the inspected null witness. |
| `contrasts_with`, `contrasts_with[]` | present array 390; null/absent 0; empty 262; populated 128 | present 1,664; array 1,661; null 3; empty 1,133; populated 528; absent 0 | all populated items are strings: 148 occurrences/107 distinct Music targets; 643/385 Erlang. `error-handling-philosophy.md` is the inspected null witness. |

Thus the eight legacy pairs have the same container/item shape only in their
non-null populated state. The frozen records show the documented historical
rule alongside variable observed conformance: `prerequisites` has explicit
non-foundational/foundational guidance, while the broader v3.2 instructions
name all four legacy keys. An Erlang `extends` key can still be absent while
`prerequisites`, `related`, and `contrasts_with` have observed nulls. A
migration/extractor must retain those states instead of manufacturing empty
arrays, without claiming that every card followed the historical instructions
or that the future profile will require the same fields. The census establishes
neither global identity nor edge warrant for any string item.

| Selected concept-card pairs | Literal state in the 31-card population |
| --- | --- |
| `relationship_edge_refs` | absent 30; present array 1; null 0; the one array is empty (`minimal-card.md`). |
| `relationship_refs` | absent 24; present array 7; null 0; six empty arrays and one populated array (`rich-profile-card.md`). |
| `relationship_refs[]` | the sole item is a mapping; it is absent when its root is absent and has no item when the root is empty. |
| `relationship_refs[].id` | sole item component is string `edge-evidence-map-related-to-claim`. |
| `relationship_refs[].path` | sole item component is string `records/edge-evidence-map-related-to-claim.md`. |
| `relationship_refs[].revision` | sole item component is number `1`. |

The last three components are components of the one observed mapping, not
defaults for an empty or absent collection. The requested path remains
unresolved in its declared source-root lookup; that is distinct from a missing
ID/revision component and from relationship truth.

| Selected relationship-edge pairs | Null/unassessed template | Populated synthetic example |
| --- | --- | --- |
| `directed` | absent | boolean `true` |
| `direction` | present null | absent |
| `endpoint_roles`, `.from_role`, `.to_role` | present mapping; both child values null | root and children absent |
| `from_ref`, `.id`, `.revision` | root present null; child components unavailable | mapping; string `cc-prepared-source-provenance`, number `1` |
| `to_ref`, `.id`, `.revision` | root present null; child components unavailable | mapping; string `cc-claim-support-is-assertion-specific`, number `1` |
| `relationship_type` | present null | absent |
| `relation_type` | absent | string `precedes` |
| `meaning` | present null | absent |
| `inverse_reading` | present null | absent |
| `symmetry` | present null | absent |
| `graph_closure_state` | string `unassessed` | absent |
| `source_support_refs` | present empty array | present one-item array |
| `source_support_refs[]` | no item | one mapping |
| `source_support_refs[].id` | no component | string `support-synthetic-edge-001` |
| `source_support_refs[].revision` | no component | number `1` |

This accounts for all 21 selected edge pairs: the template demonstrates
declared-but-unassessed slots and the example demonstrates only the listed
synthetic values. It does not make `directed` equivalent to `direction`,
`relation_type` equivalent to `relationship_type`, or the support request a
resolved support record.

### Selected-Card Context-Family Census

The 31 parsed concept-card mappings decompose into six requested context
families, including the two Arc07 output phases. This is a census of parsed records,
not a membership count and not a quality or acceptance result.

| Context family | Parsed cards | `relationship_edge_refs` | `relationship_refs` |
| --- | ---: | --- | --- |
| Template | 1 | absent 1 | empty 1 |
| Synthetic examples | 3 | empty 1; absent 2 | absent 2; populated 1 |
| Arc07 pilot outputs | 4 | absent 4 | empty 4 |
| Arc07 expanded outputs | 6 | absent 6 | absent 6 |
| Rich rerun | 7 | absent 7 | empty 1; absent 6 |
| Teaching rerun | 10 | absent 10 | absent 10 |
| **Total** | **31** | **empty 1; absent 30** | **empty 6; populated 1; absent 24** |

The rich rerun has three malformed card exclusions (`cc-memory-forms.md`,
`cc-priming-forms.md` and `cc-recognition-dual-process.md`) with YAML parse
errors. The same rich directory also contains README/INDEX/comparison
documents without card frontmatter; those are non-card records, not additional
malformed-card evidence. The malformed cards are excluded from the 31 parsed
denominator and are not absence examples.

The selected teaching witness is registered as both the original
`workbench/compcogneuro-teaching-rerun-2026-09-12/candidate-cards/cc-memory-forms.md`
and its preserved Arc01 baseline copy. Both hashes are
`451a52574cce00df9a80bbc908e12ff7c0eb246b2c634cc93d7ad3cdae3d1ac9`; the
source and copy manifests agree at line 21. Its `record_type` is
`concept-card`, id `cc-memory-forms`, revision 3, and its status is
`candidate-requires-operator-review`, with agent-direct Codex extraction and
the `run-compcogneuro-teaching-rerun-20260912` run reference. Both structured
relationship-reference keys are absent. The body nevertheless says
“Contains or routes to: episodic memory, semantic memory, recognition,
priming” and “Related: complementary learning systems.” Those are actual
candidate-card teaching prose, not stored edge records, source support, or
semantic verification.

The operational loss boundary is therefore explicit: a frontmatter-only
relationship index can preserve the two absent states but cannot recover these
body-level relationship candidates. An extractor or migration must retain the
prose and its candidate/unassessed provenance separately, while refusing to
invent slugs, endpoint identities or edge support from the prose. This witness
is real extraction output, but it is not operator-accepted or independently
verified.

### Null-Field Body/Metadata Contrast

The registered Erlang `data-type-sizes.md` witness has a present
`prerequisites` key whose value is YAML null. Its body still contains a
`Prerequisites` section with the prose “Erlang data types — The card quantifies
the memory cost of the language's primitive types.” This is a concrete
body/metadata mismatch: null does not mean that the concept has no conceptual
dependency, and it does not prove that the body sentence should be converted
into the slug `erlang-data-types`. The corresponding target is not declared by
that body section. The safe disposition is to preserve null metadata, retain
the readable prose and mark any machine relationship unresolved until a
source-grounded structured assertion exists. The other registered null-field
witnesses (`sc-hbase-protocol.md` and `error-handling-philosophy.md`) remain
useful state contrasts but are not needed to claim an additional body repair.

The direct witnesses are registered with path, SHA-256, section, and role in
`semantic-membership.json`: `erlangAbsentExtends`, `erlangNullPrerequisite`,
`erlangNullRelated`, and `erlangNullContrast`. The teaching witness is linked
through its original/copy mapping and four hash-manifest checks. The earlier
nineteen inputs are retained; these four legacy witnesses and one existing
teaching card are the only contextual additions. The exact census recipe and
all registered hash checks are in `validation-evidence.md`.

## Iteration 03 Contextual Reading And Body/Metadata Comparison

Both 862-line/907-line v3.2 prompts were presented to this context in visible
220- and 230-line sections, respectively. The howto's Typed Relationships
section calls the four lists typed relationships, requires exact slugs, and
defines prerequisite/extension/non-hierarchical/common-confusion meanings. The
parallel prompt repeats the same four field roles, requires cross-reference and
orphan checks, and labels prerequisite incoming, extension outgoing and
related/contrast symmetric. Those historical assertions enable bounded lookup;
they differ from current edge records in independently identified
representation, requested revision/resolution and relation-scoped warrant.

The current template has an empty `relationship_refs` list, minimal-card has
an empty `relationship_edge_refs` list, and rich-profile has one populated
`relationship_refs` mapping whose declared target is unresolved. Two generated
candidate cards add a useful body/metadata contrast. Arc07's
`cc-emergent-explanation` carries an empty `relationship_refs` list, explicitly
asserts no relationship edge, and proposes a future CQ about reductionism and
reconstructionism. The rich-rerun `cc-model-data-constraints` also carries an
empty list but names a prerequisite candidate and a related candidate in its
body. Both are real-corpus extraction outputs still awaiting review: neither is
synthetic merely because it is a candidate, and neither is semantically
verified or admitted. The first is a future-CQ/no-edge case; the second is a
body-level relationship-candidate case. Thus prose can teach, defer, or propose
a relation without producing a stored edge assertion. The template's
null/unassessed edge fields and the three malformed inventory records remain
distinct limitations.

The native legacy reads connect body and metadata without inventing new edges:
accent-types lists `meter` as a prerequisite and explains in its body that
metric accent depends on the metric framework; behaviour lists
`supervision-tree` and says behaviours formalize common process patterns.
`accented-incomplete-neighbor` and `appoggiatura` each list the other as
related, while their contrast lists give concrete commonly-confused comparisons.
These are scoped assertions encoded by the old cards; no source span, edge
support record, global identity, or revision is thereby supplied.
