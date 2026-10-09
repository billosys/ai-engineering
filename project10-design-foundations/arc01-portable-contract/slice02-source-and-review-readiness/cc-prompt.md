# CC assignment — Source and Review Readiness

Initial assignment, issued 2026-10-09. Project-relative path:
`arc01-portable-contract/slice02-source-and-review-readiness/cc-prompt.md`.

## Outcome, roles and scope

Build a complete source/locator and review-method packet from accepted Slice01.
Resolve required source gaps with actual evidence where accessible; report
unavailable inputs precisely and continue independent work. Sofie is CDC in the
planning chat; you are CC in a separate context. Return through the Operator.
Keep all nine ledger rows open for CDC; do not accept your own work, create a
CRC role, or advance Slice03. Expedited Mode is now enabled for Project10, with
independent acceptance, evidence, scope and Operator gates unchanged.

All 233 cards receive the project's five-dimension semantic review later;
this slice establishes source readiness and its procedure, not corpus acceptance.
No C&B compatibility bridge/preset, card schema migration or source repair.

## Roots, revisions and drift

Locate with `git worktree list`. SOURCE is
`/Users/oubiwann/lab/billosys/ai-engineering` on main; PLANNING is its planning
worktree; PROJECT is `PLANNING/project10-design-foundations`; SLICE is this
directory. PREVIOUS is the sibling `slice01-scope-and-portability-contract`.

- Source pin: `dffa504e851b03b8e4746f1941068e4cc850b612`.
- Accepted Slice01 CC evidence: `9cc203380aede19231b7c5119f0b43d9fe3d0e78`;
  CDC closure: `1944d1ed11d4e3d6f701dfe0f18c5afa713df9cd`.
- Shared Project09 audit pin: `795ac75b7d02536e0e95252457ac3282cd17d8d8`.
- Record the actual planning commit containing this issued open set.

Inspect both statuses. Pre-existing SOURCE `knowledge/lfe/` and PLANNING
`project12-chcd-protocol/` are unrelated; do not clean, reset or stage them.
Unrelated HEAD changes may coexist with documented per-path unchanged inputs.
Changed baseline/assignment or conflicting scope goes to CDC before dependent
output; never silently repin or replace accepted Slice01 evidence.

## Required intake

Follow standing collaboration-framework and project-management routes. Load
complete required text, recovering truncation through bounded contiguous reads.
Record actual extents and query populations separately, with exact executable
queries/results, errors and a source-cited readback in execution notes.

| Input | Required scope |
|---|---|
| PROJECT project-plan/ledger; Arc01 arc-plan/ledger; this slice plan/ledger/prompt/reconnaissance | Full, in governing order |
| PREVIOUS source-readiness and portability-contract | Full; original/prepared limits, identity populations, handoff and binding/proposed distinctions |
| PREVIOUS CDC verification | Current verdict and complete `Iteration02 independent verification and acceptance`; prior reviews only where needed |
| PREVIOUS baseline-files.tsv and card-source-index.jsonl | Required-data: exact full populations; inspect all 233 raw reference/locator projections in bounded groups |
| SOURCE knowledge/concept-cards/SKILL.md | Full |
| concept-cards guides/08-validation-verification.md | Opening through actor provenance; Perform Semantic Verification; Make Each Result Recoverable; Prevent False Upgrades |
| concept-cards guides/06-graph-cq.md and guides/07-reconciliation.md | Full; relationships/question coverage, comparison and preservation |
| SOURCE knowledge/document-extraction/SKILL.md and guides/03-output-contract.md, 09-locator-model.md, 10-validation-and-reports.md | Full; typed locators, original/prepared distinction, per-use readiness and caveats |
| SOURCE design sources/md/ | Required-data: complete holdings/identity inventory; full cited target sections and relevant structural context for all 83 locally sourced cards |
| SOURCE knowledge/design/concept-cards/posts/golden-ratio.md and knowledge/design/concept-cards/munsell-colour-system/munsell-hue-circle.md | Full |
| Original files explicitly supplied by Operator | Conditional: inspect exact named files only; load corresponding document-extraction format guide before inspecting/mapping them |

The readback must distinguish prepared navigation from original fidelity,
primary identity from additional citations, per-claim review from a card summary,
and blocked readiness from a completed report. No full-book read or all-card
semantic review is requested here. Do not claim missing originals were inspected.

## Ordered execution and exact artifacts

### 1. Source identity and evidence needs

Write `artifacts/source-register.md`. Reconcile the eight **raw** primary pairs
and counts against the accepted index. Give each an unambiguous local key with
its exact raw strings, observed title/author and bibliographic assertions,
original path/URI and edition/capture identity where checked, prepared paths and
hashes, identifying witnesses, lineage/unknowns, and caveats. For absent evidence
use explicit unknowns and reasons, not guessed editions or placeholders claiming
content. Dates/editions asserted by cards are separate from observed originals.

Inspect every raw reference for additional citations, recording their literal
passage, card population and role (e.g. further reading, attributed support,
unclear). Keep these separate from the eight primary identities; Brown's
Bringhurst reference is not proof of a Bringhurst source or automatic support
for every claim. Unknown role remains unknown.

Public read-only research may use source authors, publishers, libraries/archive
catalogs and official article pages to identify acquisition candidates. Cite
actual pages/access dates and distinguish metadata, excerpts and full sources.
Do not scan private storage, purchase or download files. Exact Operator-supplied
original files may be inspected and hashed without altering them; record direct
versus Operator-reported observations. No copying, conversion or source-tree
mutation is allowed by this initial assignment.

### 2. Every-card locator accounting

Write `artifacts/locator-map.jsonl`, UTF-8, one object per baseline card sorted
by path. This is local slice evidence, not a new concept-card schema. Keys:

- `card_path`, `card_sha256`: exact accepted index identity.
- `primary_source_raw`: mapping with `source` and `authors`, copied as the
  accepted literal lists, including quotes/escapes; no YAML normalization.
- `asserted_locators_raw`: exact lists for `chapter`, `pdf_page`, `section`,
  plus unchanged `source_reference_raw` and its heading status.
- `prepared_targets`: list of checked or proposed target objects below.
- `original_targets`: same shape for actual original resources, or `[]` with
  a named unavailable-evidence caveat. Never fill from the card itself.
- `mapping_notes`, `caveat_ids`: explain evidence, ambiguity and unmet criteria.

Target object: `path_or_uri`, `snapshot_sha256` (null only with explanation),
`locator_kind`, `locator_value`, `basis`, `mapping_assessment`, `evidence_ref`.
For local Markdown use one-based inclusive line start/end in the hashed file;
retain heading hierarchy/order or HTML IDs/URL identity when actually present.
For PDFs distinguish physical position/base from printed labels; preserve raw
asserted locators alongside checked interpretations. For web material preserve
capture identity and original anchor/resource information; invent no pages.
Use descriptive scoped assessments such as checked prepared navigation,
candidate-only, or original mapping unresolved, with reasons. No new global
status vocabulary is established. Multiple sections/targets are permitted.

For 37 Butterick cards, refine broad substring candidates through page title,
source URL, body boundary and contextual inspection. A stray cross-link in
`text-formatting.md` is not the `headings.md` article. Some pages have no Markdown
heading: use checked title/body line spans without fabricated anchors. For all
46 post cards, inspect references as well as null section fields; retain each
cited section and qualification. For the 150 book cards, represent unavailable
originals honestly; do not call an asserted `pdf_page` a checked physical page.

Re-read all 233 output objects and directly compare copied fields/hashes/path
sets with the index. Re-open every checked local target, validate digest/span,
boundary evidence and claim of uniqueness. A path/count check alone is weaker
than this mapping check. Inspect complete relevant sections; no search-snippet
substitute for their qualifications. Mapping does not establish semantic support.

### 3. Acquisition/preparation actions and readiness

Write `artifacts/source-input-actions.md`: each identity/edition/capture/locator/
fidelity gap gets its affected population, evidence/caveat ID, exact required
input or action, next owner, authorization state, and falsifiable re-entry check.
Ask for original/capture paths and edition evidence specifically; no request
that the Operator repeat settled design scope. Public metadata options are
proposals, not acquired inputs. Necessary source mutations return to CDC for a
named follow-up allowlist and format/preparation contract before mutation.

Write `artifacts/readiness-report.md`. Assess prepared reading/navigation and
original-source traceability/fidelity separately for each group and affected
cards. Account for the source-preparation categories in document-extraction's
output contract, with applicable checks/limits rather than placeholder files.
Retain conversion-report link/media caveats and sampled/unrun fidelity coverage.
Give exact declared use, snapshot, evidence and blocked re-entry conditions.

**S02-08 remains open wherever required original/edition/capture/fidelity evidence
prevents the agreed dependent review.** A request, catalog listing, unique title,
prepared file, or caveated reading status does not close it. Missing inputs do
not prevent completing independent mapping/procedure work or returning its
evidence, but prevent claiming Slice02 done and automatically advancing Slice03.
An explicit proposal to change sequencing/scope goes to CDC/Operator; no inferred
deferral, quarantine or reduction of the 233-card contract.

### 4. Executable five-dimension procedure

Write `artifacts/review-procedure.md`. Define the future ordered review:

1. Pin card/source/guide revisions; read every card's complete body, examples,
   implementation mappings, relationships, prerequisites and question coverage.
2. Inventory every substantive assertion with a local per-card claim ID and
   exact card span/text. Separate source-attribution assertions, historical
   positions, mathematical/technical correctness, contextual advice and analogy.
3. Inspect cited spans with qualifying/contradictory context; record evidence
   for source fidelity, correctness, scope/attribution, internal/cross-card/guide
   consistency, and relationship/question coverage separately.
4. Record each dimension's outcome/reason, blocked evidence and next owner.
   Source faithfulness and present-day truth can legitimately differ. A valid
   relationship endpoint or populated question list is not semantic coverage.
5. Correct/qualify/remove only under assigned mutation authority, retaining
   prior revision, reasons and affected downstream material. Revised claims and
   implicated guide/card relations require review at their new revisions.
6. Reconcile all original 233 identities to additions/splits/merges/removals,
   claim-level coverage and every repeated live-guide claim. No whole-card
   summary may conceal unfinished dimensions. Independent CDC review remains
   separate from CC checks; preserve counterevidence and outstanding gates.

Specify a compact **local claim-result shape** in prose or a worked record:
claim ID; card path/hash/span/assertion; evidence type and snapshot-bound source
spans; five separate dimension results/reasons; actor/role/date/method revision;
prior/revised subject and affected dependencies; blocked input/owner; proposed
disposition and independent-review status. This is evidence design, not a
Project08 schema migration or new runtime. Explain scope accounting for all
eight live files and DES allocations from the accepted contract; final Arc02
execution-group allocation is Slice03 work.

Use grounded analytical cases to exercise the method, with inputs, expected
handling and actual limits: Munsell page-4 assertion without original; Brown null
section with richer references/further reading; Butterick title/body without a
Markdown heading and with many substring hits; source faithfulness versus truth
of an added mathematical/CSS claim; existing relationship endpoints versus an
unproven CQ answerability claim. Describe how the protocol catches each false
upgrade. These examples do not count as all-card semantic review or certify
uninspected claims; distinguish any real limited comparison actually performed.

## Validation, allowlist and return

Use direct queries, retain exact commands/results/extents and failures in
`artifacts/execution-notes.md`. No maintained validator is requested. Check:
eight raw primary groups and all discovered secondary-citation observations;
233 unique sorted card rows with exact raw copies; all checked target bytes/spans;
every gap owner/re-entry condition; five dimensions and all contrasting cases;
source/snapshot versus prepared-navigation readiness; protected input equality;
all local file/fragment targets, final newlines, whitespace and planning
`git diff --check`. Count/set equality never proves semantic warrant.

CC may create/edit only these paths relative to SLICE:

- `artifacts/source-register.md`
- `artifacts/locator-map.jsonl`
- `artifacts/source-input-actions.md`
- `artifacts/review-procedure.md`
- `artifacts/readiness-report.md`
- `artifacts/execution-notes.md`
- `ledger.md` (evidence/notes only; no weakened criteria or self-acceptance)
- `closing-report.md` (actual execution report; may be explicitly partial).

Preserve all plans/prompts, author reconnaissance, the entire accepted Slice01,
Project09, source/cards/guides/metadata/packaging and installed skills. Full
source/package gates are untriggered by this planning-only assignment; no browser
or accessibility acceptance follows from document inspection. Do not pre-create
CDC verification or successful close records.

After actual work/checks, commit exactly the existing named outputs with an
explicit path list and `git commit --only`, preserving unrelated staging, and
both required trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Return exact assignment/output/source/audit revisions, all nine row dispositions,
artifact inventory, queries/coverage, failed/blocked/unrun attempts and a named
**Bubble-up to the arc** section: assigned piece delivered, unanticipated needs,
and specification-versus-delivery with remaining gates/owners. If S02-08 is
unresolved, return a partial/blocked report and concrete required inputs; do not
call the slice proposed-done. CDC reviews actual evidence and determines closure
and the next Expedited handoff. No publishing or source mutation is authorized.
