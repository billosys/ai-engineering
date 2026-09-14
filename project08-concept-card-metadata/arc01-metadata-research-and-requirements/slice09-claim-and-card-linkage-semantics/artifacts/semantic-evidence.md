# Slice09 Claim/Card Linkage Evidence

## Census and contexts

The frozen inventory has exactly 32 parsed roots: one `claim` template and 31
`concept-card` roots. The claim template has `assertion_kind`, `card_ref`, and
`statement` present as null, and empty `source_refs` and `source_support_refs`.
It is the only parsed claim root; it is not populated standalone-claim evidence.
The three malformed rich inputs are specifically
`cc-memory-forms.md` (SHA `d9bc411c...17593`), `cc-priming-forms.md`
(`c62584f...3ae8`), and `cc-recognition-dual-process.md`
(`e691cbfc...1e1e`) in the rich rerun. YAML::XS rejected their frontmatter;
they remain parse limitations rather than absent, null, or empty selected
fields, and their text was not reinterpreted as valid metadata.

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

The rich and teaching rerun copies independently use the tuple
`ccn-book`, revision `e0c697b4d4d134f29cb5c2bbde41b1b6b409b63d`, and
`/private/tmp/project05-compcogneuro-book-e0c697b4/chapter-01.md`; each requests
revision 1 for its embedded claim/support. The source path was readable at this
review and hashes to `6a72d202...cba48`, matching the pilot acquisition's
sampled Chapter 1 hash. Its Markdown frontmatter names only `bibfile`, so it
does not declare source-record ID `ccn-book` or a revision field. The rerun
body maps use heading-style claim/support paths; they do not themselves declare
literal anchors or inherit target revisions.

The frozen mapping is exact: rich original
`workbench/.../compcogneuro-rich-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md`
and its baseline copy both hash `65915a99...c3695`; teaching original
`workbench/.../compcogneuro-teaching-rerun-2026-09-12/candidate-cards/cc-model-data-constraints.md`
and its copy both hash `09771f4f...230fb`. `source-sha256sums.txt` identifies
the originals and `copy-sha256sums.txt` the copies. No current ignored workbench
file was needed for this comparison.

## Reference matrix

| Context | Requested tuple | Actual target / lookup result | Limit |
| --- | --- | --- | --- |
| Pilot claim | `claim-model-data-constraints`, 1, `#claim-model-data-constraints` | matching `### Claim` heading in same card | no literal anchor, record declaration, or revision field |
| Pilot support | `support-model-data-constraints`, 1, `./support-model-data-constraints.md` | separate source-support frontmatter declares id/revision/subject | card has no `source_support_refs`; support is linked in body |
| Pilot source | `ccn-book`, `e0c697b4`, `../source-acquisition.md` | registered acquisition target declares full checked-out commit and Chapter 1 hash | no source-record `ccn-book` or source revision field is declared |
| Rich rerun source | `ccn-book`, full `e0c697b4...b63d`, absolute Chapter 1 path | path currently available; bytes match acquisition Chapter 1; target declares only `bibfile` | path/hash and requested commit correspondence observed; ID/revision declaration unresolved |
| Teaching rerun source | same `ccn-book`, full commit, same absolute Chapter 1 path | same available byte target and metadata limitation | same bounded agreement/unknown components |
| Rich rerun claim/support | `claim-model-data-constraints-r2` / `support-model-data-constraints-r2`, 1, `#...` | matching named body sections in pinned rich copy | heading lookup only; fragment and embedded revision unresolved |
| Teaching rerun claim/support | `claim-model-data-constraints-r3` / `support-model-data-constraints-r3`, 1, `#...` | matching named body sections in pinned teaching copy | heading lookup only; fragment and embedded revision unresolved |
| Synthetic examples | paths under `records/` / `sources/` | explicitly fictional examples | conventions, not missing generated targets |

Slice08 supplies the target diagnostic distinction: heading/file lookup can be
observed while literal fragments, source-record declarations, and embedded
target revisions remain unresolved. This packet attributes that prior result
and checks the rerun convention independently; it does not declare a global
reference rule.

## Historical comparison

Accent Types' Core Definition says that temporal and nontemporal accents draw
attention and then spells out metric, agogic, dynamic, registral and textural
cases; its Source Reference gives Chapter 2, section and pages 43--46, while
Verification Notes say the definition was directly sourced and categorized.
That wording/scope is readable, but the card contains no machine assertion ID
or selected span record for an individual sentence. OTP Behaviour's Core
Definition says a behaviour divides a process into generic behaviour-module
and specific callback-module parts, and its Source Reference/Verification Notes
identify the OTP section and direct quote/confidence rationale. It is likewise
readable with frontmatter source fields, but no structured claim statement,
assertion-mode, source-support tuple, or snapshot applies mechanically to that
particular definition. In contrast, the current claim template separates a
null `statement` slot from a null `assertion_kind` slot; current cards make
body headings readable but do not turn them into declared embedded records.
The v3.2 guide intended both machine-readable frontmatter and human-readable
exposition, and called provenance sacred. This is an observed bounded
machine-link difference, not a global absence, losslessness, query-equivalence,
or source-truth judgment.

## Consequences

Future design must decide, rather than assume, target record declarations,
literal fragment handling, reciprocal-link policy, and revision applicability.
It must preserve a claim's exact statement/qualifications separately from body
paraphrase or definition; keep card citation, scalar snapshot, claim source
and claim support distinct; and retain the actual support subject/span before
claiming warrant. No support, lifecycle, verification, schema, or extraction
decision is made here.
