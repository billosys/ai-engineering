---
slice: slice02-book-card-metadata
status: closed
depends-on: [slice01-schema-and-field-inventory]
blocks: [arc06 composition, arc04 final release readiness]
---

# Slice02 — All-Card Metadata Normalization and Rendering

## Result and authority

Apply the accepted existing-field mapping to the remaining223 cards on main;
verify the complete233-card population (150 book +83 web), including ten already
accepted pilots, and inspect actual GitHub file rendering at the final revision.
This implements the Operator's2026-10-12 combined delivery amendment, not the
superseded150-book-only draft. The retained directory name is historical.
Two contributors: separate CC implements; CDC Sofie independently reviews via
Operator relay. Expedited Mode. All [six criteria](ledger.md), [seven arc rows](../ledger.md)
and [thirteen project rows](../../ledger.md) remain binding.

[Project plan](../../project-plan.md) and [Arc06 plan](../arc-plan.md) govern.
Slice01 is independently closed at source `4ccc6f6055743d8e8b53251d7e8852f04d1ed181` /
planning `9934079aecc5a8c9bc2888c9a1b627fb4f3c55ff`; [CDC acceptance](../slice01-schema-and-field-inventory/cdc-verification.md#iteration02-independent-acceptance-and-slice-close--2026-10-13)
freezes historical3.2 mapping and reusable helper. No renewed schema selection,
separate pilot, header census or source-acquisition assignment is needed.

## Exact input and mutation scope

Main input `4ccc6f6055743d8e8b53251d7e8852f04d1ed181`. Immutable [Slice01 inventory](../slice01-schema-and-field-inventory/artifacts/header-inventory.jsonl)
SHA-256 `c7306e8a62291fa635e154463553fd990a9b12d91d70cb4403a0259f9e49dd5c`;233 unique rows,
current card revisions `fe4e0558` remain byte-applicable to current input.
The **exact card allowlist** is `current.path` for rows whose `pilot` is false,
in this hash-pinned file:223 paths. Ten `pilot:true` paths are protected. Complete
union equals tracked design card paths; additions/deletions/renames unauthorized.
The only two extra source write paths are `knowledge/design/SKILL.md` and
`knowledge/design/version-history.md`:225 source paths total. Helper SHA-256
`8ce4f31322aaa63389283b6a5ce3b41ddc184c73a971f55771997ee343a731ba` stays exact; no helper edit.
The [prompt](cc-prompt.md#exact-allowlist-and-baseline) supplies the executable
selection. No glob/tree-level commit. Drift in any selected/protected design
input is resolved before mutation; unrelated main advances may be retained only
with an explicit byte-applicability/parent record. Preserve unrelated work.

## Frozen existing-field contract

Exactly `[[]]` in `aliases`, `prerequisites`, `extends`, `contrasts_with` becomes
`[]`; no other typed value changes. Remaining90 occurrences affect53 non-pilot
cards; original106 include16 already fixed in six pilots. Preserve populated
nested aliases/lists and all22 observed root fields/extensions, member/key order,
null/empty/absence, scalar types, decoded Unicode, slugs/paths/source references,
confidence, relationships/CQs and domain extension values. Missing stays absent;
no added IDs, dates, review states, schema_version, defaults or inferred facts.
Existing missing/non-flat fields remain recorded conformance limitations.

Use accepted helper serialization: leading UTF-8/LF YAML mapping, unindented
`---` delimiters, two-space nesting, JSON-quoted string values with direct
Unicode, explicit null/empty collections and unchanged body bytes after the
closing delimiter. Source originals and Project08 are untouched. Metadata
formatting is not semantic or source-fidelity acceptance; originals are not
required to preserve their existing edition/page strings. Arc02 owns body
escape/presentation and substantive fixes. Whole rendering gates are not waived.

## Implementation and proof

1. Before writes reconcile all233 input hashes/typed metadata/body bytes with
   the immutable inventory; select223 exact remaining paths and ten protected
   pilots. Check helper hash/current skill authority/history. Run its nonmutating
   `--check` all233; compare expected values independently of converter output.
2. Execute accepted helper `--write` only223 selected paths. Any conflict or I/O
   interruption stops the batch; inspect written/restored/held/recovery-failed
   accounting and actual bytes before considering retry. Never overwrite external
   work, rebaseline it silently or promise all-file transactional guarantees.
3. Independently decode every final header with installed Perl YAML::XS/JSON::PP,
   comparing to inventory current metadata plus only four exact sentinel rules.
   Compare recursive mapping-key order from original/final YAML ASTs as well;
   unordered decoder hashes alone do not prove it. Compare every body's bytes directly to pinned input blobs, not only converter
   hashes. Ten pilots stay whole-byte exact. Check all233 idempotent and zero
   remaining permitted sentinels. Preserve paths/slugs/references; disclose any
   pre-existing unresolved target rather than claim semantic relationship review.
4. Bump owning skill metadata1.0.4→1.0.5 and append one corresponding significant
   correction entry to sibling history. No skill version prose in other owned
   files or independent guide history. No packaging-list change is needed:
   cards/helper remain unbundled; validate them as source, eight packaged Markdown
   members as actual ZIP entries. Run applicable Make gates in the prompt.
5. Emit one233-row result bridge and one concise batch record, plus ledger
   evidence and closing report. Exercise actual preservation/parser negatives
   on representative current data; do not add a general validator framework.
6. Inspect full hosted file views for all233 at the exact final card revision;
   record per-card coverage/observations. Use available approved read access.
   Publication/push is not authorized here. If that revision is unavailable,
   deliver checked local source changes and return partial with S02-05 open,
   exact blocker/re-entry owner. Do not replace actual observation with raw
   fetch, local YAML/GFM parsing or a prior different revision's screenshot.

## Result bridge and hosted boundary

`artifacts/batch-results.jsonl` has exactly one unique record per accepted233
path. Each links the immutable inventory row/path and baseline `dffa504e`,
prechange `4ccc6f6055743d8e8b53251d7e8852f04d1ed181` and actual postchange commit/path/hash;
records normalized versus unchanged-pilot disposition, exact sentinel deltas,
complete after typed metadata, original/preserved body bytes/hash and old/new
body byte offsets/closing-delimiter lines. Offset convention equals inventory:
body begins immediately after closing `---`, including its existing following
newline. Header line changes are an explicit locator delta, not a content edit.
Recover full headers from pinned Git blobs rather than duplicate the census.

Per record include hosted status (pass/fail/unavailable/unrun), exact revision
and URL when applicable, observer/method/date, concrete metadata/Markdown checks,
evidence location/observation and failure or unavailable reason. These are review
records, not new card metadata fields. Record all233, including unchecked ones.
Inspect metadata keys/values, nested lists/mappings, nulls, quoting/Unicode and
whole-body headings/lists/tables/fences/code/links as present against actual
expected content. A parsed table alone does not establish the whole rendered view.
Existing literal body escapes or other rendering defects are reported to Arc02;
they cannot be silently repaired here or counted as passing a correctness gate.
Unavailable views or unresolved defects leave S02-05/A06-05 open. Sampling and
local previews cannot close the whole-population hosted obligation.

Arc02 consumes baseline/current/postchange path/hash/body-location bridge and
owns substantive/body/fidelity gaps. Arc04 consumes applicable source/package
revisions for final composition. Historical manifests/index/locators stay pinned;
a header change invalidates old whole-file hashes, not unchanged body content.
Record that applicability explicitly, without blanket semantic acceptance.

## Compact outputs and checks

Exactly four CC planning write paths in this slice: `artifacts/batch-record.md`,
`artifacts/batch-results.jsonl`, `ledger.md` (evidence/notes only) and
`closing-report.md`. Record intake, commands/coverage, positives/negatives,
failed/recovered/unrun attempts, package identities, hosted coverage limits,
all six proposed row outcomes and downstream owners in those existing files.
No recreated schema/census/gap/readiness reports; no new source checker product.
Checks: whole233 independent typed/body/reference/idempotence comparisons,
eight preservation/parser negatives, fresh affected package/version gates,
committed parent/path/trailer integrity, links/EOF/diff. No install/publication.

## Assignment history and author readiness

Initial [cc-prompt.md](cc-prompt.md) issued2026-10-13 by this introducing commit,
planning parent `9934079aecc5a8c9bc2888c9a1b627fb4f3c55ff`. Initial assignment returned source `b49f4589` / planning `877cd9d2`;
local work independently accepted2026-10-13, five done/one hosted row open.
This local-review handoff is historical. Current next action is Arc02/Slice09
source presentation repair after the hosted F01 finding; see the current handoff below.
CDC closes only after all binding rows are satisfied or an explicit Operator
disposition is recorded.

Initial author preparation retained at input `4ccc6f60`:
CDC inspected actual helper semantics, byte recovery/Unicode controls,
all233 check results and inventory. All223 remaining outputs differ, ten pilots
are idempotent,90 sentinel deltas/53 cards reproduce,225-path source scope is
fully determined before handoff. Guide08's structural/semantic distinction and
work-verification retention apply: mapping/body preservation uses independent
raw blobs/decoder; hosted claims require actual view evidence. Installed Ruby/
Perl interfaces are already exercised. The approved recipe reuses the safe
helper, not new conversion logic. Missing host access blocks hosted acceptance,
not these authorized local mutations; complete coverage records leave no silent
exclusions. Work is one repeated mechanical operation with refinement headroom.

## Version History

- 1.2 (2026-10-13): Activate approved combined233 normalization/rendering after
  Slice01 I2 closure. Exact223 card mutations, ten protected pilots, frozen3.2
  mapping, six complete criteria and compact outputs; retain hosted gate.
- 1.1 (2026-10-12): Operator consolidates book/web/rendering drafts; former
  unissued text superseded before any assignment.
- 1.0 (2026-10-10): Original unissued150-book-card cohort draft, retained in Git.

Open-set/close checks: exact ten planning paths, unchanged thirteen project/
seven arc/six Slice01 criteria, all six Slice01 done, A06-01 done/six open,
all six Slice02 open. Three issued Slice01 prompts and all original CC artifacts
remain byte-exact. Sixty local destinations and twenty fragments resolve;
LF/EOF/diff checks pass. Main remains `4ccc6f60` with no tracked change.

## Current review and Operator handoff — 2026-10-13

[CDC initial review](cdc-verification.md#initial-return-review--2026-10-13)
accepts S02-01/02/03/04/06; S02-05 stays open. Nine reviewed local design commits
and one remote install commit need integration before publishing exact card
revision `b49f4589`. CDC's uncommitted merge simulation preserves both; no branch
was changed. [Operator publication proposal](cdc-verification.md#hosted-blocker-and-concrete-operator-handoff)
is the next handoff. After approval/access, CDC issues a read-only hosted-check
follow-up; no duplicate normalization, census or evidence phase is needed.

- 1.3 (2026-10-13): Initial return independently accepts all local obligations;
  leave actual233 hosted rendering open and give concrete Operator publication
  handoff. Preserve original prompt and all six acceptance criteria.

Review-record checks: exact six planning paths; six criteria unchanged, five
done/one open; issued prompt, CC artifacts and parent ledgers byte-exact.
Thirty-eight local destinations/fourteen fragments resolve; EOF/diff checks pass.
Main unchanged at `b49f4589`; remote tracking refreshed to `1bbef13e` only.

## Hosted review and current handoff — 2026-10-13

Was: publication/access blocked. Now: Operator publication is complete at
`c4cc7427`; CDC independently fetched all233 exact views. Metadata passes across
233, but46 post-card bodies display1062 literal Unicode escapes. S02-05 stays
open under its existing requirement, not by a new criterion or deferred scope.
[CDC F01](cdc-verification.md#hosted-return-independent-review--2026-10-13)
supersedes CC's all233-body-pass proposal. Initial prompt remains preserved;
CC's publication/hosted follow-up returned at `eac665f5` under the Operator's
conversation approval without a new CDC-issued iteration prompt.

**Historical source-repair assignment:** [Arc02/Slice09 CC prompt](../../arc02-theory-and-evidence/slice09-post-card-unicode-presentation/cc-prompt.md).
Body repair belongs to Arc02. That assignment also permits correction of the
four existing Arc06 CC outputs while retaining local fields and historical
observations. No active Arc06 source mutation, repeated normalization or extra
readiness/evidence-only iteration. Publication of the repaired source and actual
final-revision views remain the re-entry route for this slice; no automatic close.

- 1.4 (2026-10-13): Published hosted review reproduces metadata success but finds
  literal escapes across46 bodies; retain five done/one open, authorize next
  already-owned Arc02 presentation repair and correct false rendering passes.

## Historical hosted follow-up — 2026-10-13

Was: Arc02/Slice09 source repair was active, then five prepared evidence strings
awaited Operator acceptance. Now: Slice09 is closed; source589d7c21 remains
independently accepted and the Operator accepted the five fields at b3aabcdf.
[Iteration01](cc-prompt-iteration01.md), issued at b3aabcdf, is the current CC
hosted assignment. The Operator also authorizes CC normal publication of the
reviewed main/planning range through the Slice09 closure. CC rechecks drift,
records push results, then executes the read-only all233 check once exact-source
publication/access succeeds. No force push or extra source mutation is authorized. Predecessor
is preserved initialcc-prompt.md; intervening Operator-authorized hosted return
at eac665f5 remains historical. No source mutation or metadata re-normalization.

- 1.5 (2026-10-13): Prepare exact233 corrected-revision hosted follow-up after
  independent source review. Retain evidence repair/publication gates, original
  six criteria and five done/one open; no advance by copied source-match verdict.

- 1.6 (2026-10-13): Record Operator evidence acceptance and separate CC normal-
  publication authorization after Slice09 closure. The already-issued hosted
  Iteration01 proceeds after actual source access; five done/one open retained.

## Current closure and arc handoff — 2026-10-13

Plan revision **1.7**. Was: five done/one hosted row open. Now: all six rows
done after independent review of5020db52 at exact published589d7c21; see
[final verification](cdc-verification.md#iteration01-independent-hosted-review-and-slice02-close--2026-10-13).
All233 actual metadata/body views and source/history joins pass. Initial and
Iteration01 prompts remain preserved; no active CC assignment or source repair.
Original metadata-only body proof remains historical;46 intentional Arc02
presentation changes are checked separately. No schema/semantic acceptance added.

Expedited handoff proceeds to the [Arc06 composition report](../closing-report.md)
and its Operator gate. No further rendering slice or invented readiness work.
Arc02 content/fidelity and Arc04 package/final-revision/release owners retain
all obligations. Publication of the source is complete; this review is local
planning work and does not perform a push.

- 1.7 (2026-10-13): Independently accept Iteration01 hosted result and close all
  six criteria; retain historical failures/pins and prepare formal arc composition.
