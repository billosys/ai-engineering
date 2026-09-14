# CDC Verification: Slice08

## Iteration 01: Closed

Independently reviewed `3436020a` on 2026-09-13 against the same seven
criteria and exact 27 pairs. **Slice08 is closed.** S8-R1/R2/R3 are resolved
as evidence/reporting corrections, not repairs to the historical pilot.
Source remains clean at `e763c661`. CC's four semantic artifacts and
closing-report.md are unchanged by this review. Earlier findings below remain
as history, not the current status or execution route.

### Findings Reconciled

- R1: Read the reference contract and targets, including all four claim
  headings, acquisition and preparation records and all six locator rows
  (four text, two figure). Heading/row lookup is demonstrated in this sample.
  The files do not declare explicit fragment anchors, separate embedded-claim
  or locator revisions, or the requested source-record ID/revision tuple.
  The revised matrix retains those unknowns and distinguishes the declared
  prepared-manifest ID/revision from a general source-snapshot contract.
  Unknown target components are valid inventory findings, not failed science
  or a requirement to invent/repair the input.
- R2: All 27 meanings now have contextual dispositions, with 27 distinct
  texts and no repeated evidence IDs within meaning lists. Inspected the
  meanings as well as counting them: source versus snapshot roles, selection
  versus context, reference components, and quote/checksum notes retain
  different consequences. Accent Types and OTP Behaviour carry readable
  source/review notes but do not supply these machine assertion/span tuples
  in the inspected samples. No global historical-absence or query-equivalence
  claim follows. Both samples and the live reference rules join the register.
- R3: Ran the entire CC validation block literally before CDC planning
  edits: exit 0. Exact-set, accepted-67 disjointness, evidence layers, all
  21 hashes, five-root census, target/context output, fixed historical
  preservation, current-state preservation and whitespace passed. The full
  target-file inspection above supplements the positive lookup queries:
  search matches alone do not establish absent declarations. The report
  and handoff now account for all seven criteria and the four artifacts.

Direct/caveated and text/figure distinctions from the initial review still
hold. This is independent semantic-inventory review, not a new inspection of
the textbook or images, independent claim warrant, operator acceptance or
memory admission. Unassessed lifecycle states remain unassessed.

### Durable Replay

Run from /Users/oubiwann/lab/billosys/ai-engineering. CDC authored this
wrapper, not CC. It reads CC's committed validation block and pins only its
open-ended prior-packet comparison to the reviewed delivery `3436020a`.
The original block was already run literally while that delivery was current.
Pinning avoids treating subsequent authorized CDC Slice04 plan maintenance as
a CC preservation failure; it does not conceal or modify the fixed historical
comparison, census, evidence or hash checks.

~~~bash
set -euo pipefail
a=project08-concept-card-metadata/arc01-metadata-research-and-requirements
s="$a/slice08-source-support-subjects-and-spans"
git -C .worktrees/planning show "3436020a:$s/artifacts/validation-evidence.md" |
  awk '/^~~~bash$/ {active=1;next} /^~~~$/ {active=0;next} active {print}' |
  sed 's/diff --exit-code d977cb31 --/diff --exit-code d977cb31 3436020a --/' |
  bash -e
jq -e '(.meanings|length)==27 and (.evidence|length)==21 and
  ([.meanings[].disposition]|unique|length)==27 and
  all(.meanings[];(.evidence_ids|length)==(.evidence_ids|unique|length))' \
  ".worktrees/planning/$s/artifacts/semantic-membership.json"
p=.worktrees/planning/project05-concept-card-skill/arc07-real-corpus-uat-and-feedback/slice02-pilot-markdown-preparation-and-card-extraction/artifacts
cat "$p/source-acquisition.md" "$p/prepared-source-manifest.md" "$p/locator-map.md"
for name in emergent-explanation memory-consolidation model-data-constraints pattern-separation
do
  cat "$p/candidate-cards/cc-$name.md"
done
git -C .worktrees/planning show --check 3436020a
~~~

Results: exit 0; all checks above pass. Direct reading confirms the four
requested claim IDs and six locator IDs can be found, without promoting
text/table lookup to universal URL-fragment or target-revision agreement.
The committed repair touches exactly six authorized files. Subsequent CDC
edits are only closure/roadmap/open-set documents; no CC semantic artifact,
source file, corpus, parser, baseline or prior accepted evidence changes.

### Seven-Row Closure

| Row | CDC disposition | Independently checked evidence |
| --- | --- | --- |
| S8-1 | done, reproduced | 21 registered hashes, named sections, reference and historical roles |
| S8-2 | done, reproduced | Exact 27 unique frozen pairs; no overlap with accepted 67 |
| S8-3 | done, reproduced | Five-root values/shapes, four claim targets, acquisition/manifest and six locator rows; explicit unresolved components |
| S8-4 | done, reproduced | Direct/caveated and text/figure contrasts; selection, status, quote, context and checksum-note limits |
| S8-5 | done, reproduced | Field-specific meanings/dispositions, live reference contract and bounded music/OTP body comparison |
| S8-6 | done, reproduced | Literal CC block, pinned CDC replay, complete four-artifact/seven-row handoff and unchanged remainder obligations |
| S8-7 | done, reproduced | Six-file CC scope, historical/current pre-review preservation, clean source and whitespace |

### Bubble-Up And What Worked

Delivered the assigned bounded comparison without reducing any criterion.
All four CC artifacts are in artifacts/; the earlier CDC correction prompt
remains there as review history. No deferral or no-op closes a row.
The useful repair was to turn unresolved target components into explicit
findings and field consequences instead of treating file availability as
reference validity. That pattern carries into the next comparison.

Arc01 is updated before opening Slice09. Accepted coverage is now 94/555;
this is a mechanical contextual-pair count, not a measure of global semantic
equivalence. Slice09 receives 21 claim/card linkage pairs; 440 others remain
(188 original Slice04, 252 original Slice05). Those original allocation
labels are accounting only. Slice04 complete-artifact integration, Slice05
remaining semantics/final replay, Slice01 closure, research Slice02/03,
P-14 and all project output-quality gates remain open and intact.

## Initial Review: Historical

Reviewed `2dfe5577` on 2026-09-13 against all seven unchanged criteria.
**Changes required.** Exact coverage, selection/status contrasts and scoped
preservation pass. Reference consistency, contextual consequences and complete
replay remain open. No new slice or parent closure follows this review.

## S8-R1: Target Agreement Is Not Established (Serious)

`semantic-evidence.md:11-17` claims all four anchors resolve and describes a
three-part reference check. The literal target loop in
`validation-evidence.md` only tests four files with `test -f`.
The input hash checks establish bytes, not the declared ID/type/revision
or fragment relationships.

Concrete target limitations from inspected registered inputs:
- The model candidate has a Claim heading containing `claim-model-data-constraints`
  and card-level revision 1, plus a claim reference requesting revision 1.
  An ID in a heading can locate an embedded assertion by text; it is not by
  itself a demonstrated resolver for `#claim-model-data-constraints` or an
  independently declared claim revision. Separate these observations.
- Locator IDs appear in table cells in locator-map.md, not explicit named
  anchors, and the map does not declare revision 1 for each locator. A row
  lookup by ID and the literal URL fragment are different checks.
- source-acquisition.md records the full upstream commit, but does not declare
  a source-record ID `ccn-book`. Recognizing the commit prefix does not establish
  every aspect of the reference tuple.
- prepared-source-manifest.md does declare prepared-source ID and revision 1.
  That is stronger identity evidence for this target, but does not settle the
  intended source-snapshot role or independently verify upstream bytes.

These are method/data limitations, not authority to repair the pilot.
Supply a bounded reference matrix for all subject/source/snapshot/locator
targets: requested values, target declarations, actual resolution convention,
agreement/mismatch/unknown and lookup consequences. Do not label all anchors
broken under every possible consumer; identify what is demonstrated and what
remains unresolved. Register the actual SKILL.md reference contract used to
interpret them, not just broad lifecycle guidance.

## S8-R2: Dispositions And Historical Comparison Are Incomplete (Serious)

All 27 meanings and memberships use exactly one disposition sentence:
preserve the field and do not promote it to verification/admission. This
useful shared caution is not the required field-specific lookup/preservation/
body consequence. The distinct definitions are progress; retain them where
supported rather than starting over.

Some definitions also elevate pilot usage into the general field meaning:
`source_spans[].source_snapshot_ref` is defined as a prepared snapshot,
its `.id` as the particular `ps-ccn-book-pilot-20260911` identifier,
and its `.path` as a prepared manifest. Separate the general snapshot
reference role from this observed target/representation and its limits.
The accepted Slice07 source-versus-snapshot distinction is not restricted
to a preparation pipeline.

The historical section (`semantic-evidence.md:48-59`) compares a guide and
synthetic conventions only. The explicitly required bounded music/OTP card
body/reference comparison is absent from both prose and the 18-input register.
Inspect/register the named historical contexts already available in Slice07;
explain actual carried information and limits without claiming equivalent
machine traversal or global absence of historical assertion support.

Make each membership's operational consequence traceable to evidence, including
reference ambiguity from S8-R1. Shared rules may be factored, but not used to
replace their contextual applications. Remove repeated target evidence IDs
in five subject meanings/memberships as incidental cleanup; duplicate IDs are
not separate corroborating observations.

## S8-R3: Replay Overstates Target And Preservation Checks (Correctness-Grade)

The existing block executes successfully but does not reproduce the asserted
anchor/type/revision comparison. Extend it with actual reference/target checks
and recorded interpretation. These can report unsupported/unresolved targets
as data; passing a diagnostic does not require every input reference to be valid.

`git rev-parse 1bacd954 d977cb31` resolves commit names; it performs no
preservation comparison between them. The report's "historical endpoints ...
are pinned" is therefore misleading as preservation evidence. The only diff
is an open-ended current-state check against d977cb31. For this delivery,
the relevant fixed comparison is d977cb31 to 2dfe5577; later repairs should
also pin their own entry/delivery comparison or clearly separate pre-commit
current-state checks. Do not use 1bacd954-to-d977cb31 as an expected empty
diff: authorized earlier CDC planning updates exist in that interval.

Include literal historical/context inspection routes and all added input
hashes. Reconcile closing-report.md's delivered-scope assertion with the
remaining requirements; keep the useful seven-row walk and artifact inventory.

## Independently Reproduced

From /Users/oubiwann/lab/billosys/ai-engineering:

~~~bash
set -eu
s=.worktrees/planning/project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice08-source-support-subjects-and-spans
awk '/^~~~bash$/ {active=1;next} /^~~~$/ {active=0;next} active {print}' "$s/artifacts/validation-evidence.md" | bash -e
jq '{meanings:(.meanings|length),
  distinct_dispositions:([.meanings[].disposition]|unique|length),
  evidence:(.evidence|length),
  repeated_evidence_lists:([.meanings[]|select((.evidence_ids|length)!=(.evidence_ids|unique|length))]|length)}' \
  "$s/artifacts/semantic-membership.json"
git -C .worktrees/planning diff --exit-code d977cb31 2dfe5577 -- \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice01-metadata-inventory-and-research-questions \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice04-semantic-identity-source-and-graph-families \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice06-record-identity-and-classification \
  project08-concept-card-metadata/arc01-metadata-research-and-requirements/slice07-source-identity-and-locator-semantics
git -C .worktrees/planning show --check 2dfe5577
~~~

Results: exact 27 unique frozen pairs, no accepted-67 overlap, both evidence
layers resolve, all 18 hashes match, census yields the five expected roots,
four files exist, preserved prior-packet diff empty and whitespace clean.
27 meanings share one disposition; five meaning evidence lists repeat targets.
Source checkout remains clean at e763c661. Commit scope is exactly the six
authorized planning files.

CDC separately inspected the registered target files and four support bodies.
The direct/caveated and text/figure comparisons, paraphrase/quote-policy limits,
checksum-note distinction and non-exhaustive support-status vocabulary hold
within this sample. Original claims of figure/source inspection remain pilot
attestation, not a new CDC source-support verdict.

## Seven-Row Walk

| Row | CDC disposition | Evidence |
| --- | --- | --- |
| S8-1 | open | 18 hashes pass; missing reference-rule and historical sample contexts under R1/R2 |
| S8-2 | done, reproduced | Exact set, uniqueness, inventory inclusion and accepted-67 disjointness |
| S8-3 | open | R1: target reference consistency/limits not established |
| S8-4 | done, reproduced | Bounded selection, support-status and caveat distinctions inspected |
| S8-5 | open | R2: generic dispositions, pilot-specific definitions and absent historical bodies |
| S8-6 | open | R3: complete target/preservation/context replay and honest scope reconciliation |
| S8-7 | done, reproduced | Six authorized files, source/prior-input preservation and whitespace |

## Bubble-Up

The four CC artifacts exist in artifacts/; completion of their substantive
comparison is partial. Preserve the demonstrated strengths. Correct R1/R2/R3
within Slice08 Iteration 01, using `artifacts/iteration-01-cc-prompt.md`.
Do not repair the pilot references or reopen accepted Slice07. This review
does not claim that those earlier locator semantics proved literal target
resolution in every support record.

No scope reduction, reassignment or parent closure: 67 pairs remain accepted,
27 assigned here and 461 outside accepted/assigned work. Slice04/01 composition,
later research and P-14 remain intact.
