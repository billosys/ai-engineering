# Slice09 Claim/Card Linkage Evidence

## Census and contexts

The frozen inventory has exactly 32 parsed roots: one `claim` template and 31
`concept-card` roots. The claim template has `assertion_kind`, `card_ref`, and
`statement` present as null, and empty `source_refs` and `source_support_refs`.
It is the only parsed claim root; it is not populated standalone-claim evidence.
The three malformed rich inputs remain parser limitations rather than absent,
null, or empty selected fields.

Card contexts differ materially. The concept-card template has empty selected
collections. The minimal synthetic example has an empty `claim_refs` list;
claim-backed and rich synthetic examples have populated lists whose fictional
targets illustrate shape only. Four Arc07 pilot cards have `claim_refs` and
`source_refs`, but no `source_support_refs`; six expanded cards instead expose
only scalar `source_snapshot`. The pinned rich and teaching reruns have
populated source, claim, and support lists. This is why the registry preserves
absent, empty, populated-list, and scalar-token states rather than flattening
them into one reference model.

## Assertion and support trace

`cc-model-data-constraints` (pilot revision 1) requests the embedded heading
`claim-model-data-constraints` through `claim_refs`; its body gives the limited
methodological assertion. `support-model-data-constraints` names that claim as
`subject_ref`, selects Chapter 1 lines 37--45, and says what the span supports
and does not support. The card's `source_refs` names `ccn-book` and its
preparation record is separate upstream provenance. Thus card -> embedded
claim -> support -> subject/source reference is readable and partly structured,
but it neither proves a literal Markdown fragment anchor, a declared embedded
claim record/revision, nor support for every card sentence.

The rich and teaching rerun copies independently use absolute source paths and
heading-style claim/support paths; each requests revision 1 for embedded
claims/supports. Their bodies keep source-reference/support maps alongside
claim sections, but their paths do not by themselves declare literal anchors or
inherit target revisions. Their mapped frozen copies, rather than current
ignored workbench files, are the inspected rerun baselines.

## Reference matrix

| Context | Requested tuple | Actual target / lookup result | Limit |
| --- | --- | --- | --- |
| Pilot claim | `claim-model-data-constraints`, 1, `#claim-model-data-constraints` | matching `### Claim` heading in same card | no literal anchor, record declaration, or revision field |
| Pilot support | `support-model-data-constraints`, 1, `./support-model-data-constraints.md` | separate source-support frontmatter declares id/revision/subject | card has no `source_support_refs`; support is linked in body |
| Pilot source | `ccn-book`, `e0c697b4`, `../source-acquisition.md` | acquisition records commit identity | no source-record id/revision declaration established |
| Rerun claim/support | `*-r2`/`*-r3`, 1, `#...` | matching bodies/headings in pinned copies | heading lookup only; fragment and embedded revision unresolved |
| Synthetic examples | paths under `records/` / `sources/` | explicitly fictional examples | conventions, not missing generated targets |

Slice08 supplies the target diagnostic distinction: heading/file lookup can be
observed while literal fragments, source-record declarations, and embedded
target revisions remain unresolved. This packet attributes that prior result
and checks the rerun convention independently; it does not declare a global
reference rule.

## Historical comparison

Accent Types teaches a full readable definition, examples and relationships,
then gives chapter/section/page provenance and direct-source/confidence/
re-extraction notes. OTP Behaviour similarly gives a substantive definition,
construction, examples and source/review prose. The v3.2 guide intended both
machine-readable frontmatter and human-readable exposition, and called
provenance sacred. These bodies are useful teaching and review surfaces, but
the bounded samples do not expose machine assertion IDs, selected-span/support
records, snapshot tuples, or independently verified support. That is an
observed machine-link difference, not a claim of global inferiority, absence,
losslessness, or query equivalence.

## Consequences

Future design must decide, rather than assume, target record declarations,
literal fragment handling, reciprocal-link policy, and revision applicability.
It must preserve a claim's exact statement/qualifications separately from body
paraphrase or definition; keep card citation, scalar snapshot, claim source
and claim support distinct; and retain the actual support subject/span before
claiming warrant. No support, lifecycle, verification, schema, or extraction
decision is made here.
