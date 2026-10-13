---
slice: slice01-schema-and-field-inventory
status: closed
depends-on: [arc01-portable-contract]
blocks: [slice02-book-card-metadata]
---

# Arc06 Slice01 — Metadata Contract and Source Pilot

## Result, authority and assignment

Deliver a reproducible existing-field crosswalk and **ten actual normalized
cards on main**, alongside the complete 233-header census. This activates the
Operator's approved combined contract/pilot in [Arc06](../arc-plan.md), under
the [project plan](../../project-plan.md). CDC Sofie reviews separate CC via
Operator relay; Two-Contributor Workflow, Expedited Mode. No bulk mutation
until independent acceptance. The six [ledger criteria](ledger.md) remain binding.

**Current state:** Iteration02 independently accepted2026-10-13; Slice01 closed,
all six rows done at source `4ccc6f60` / planning `9934079a`. Last assignment
`cc-prompt-iteration02.md` was issued `ce393b8c`; its prompt remains unchanged.
Next active assignment belongs to Slice02, not this closed slice.
The initial assignment at `e8718605` remains preserved; its thirteen-source
write scope is historical and does not authorize I2 card changes.
The superseded unissued read-only draft is replaced; its complete census,
crosswalk, preservation, GitHub diagnosis, allocation and return obligations
are retained in this exercised pilot. Historical preparation notes are unchanged.

## Schema authority and scope

Project08's P-15/schema decision remains open at `a900b68a10a0110c453867b827f865a4d8008bb6`. Therefore use the
Operator-authorized **3.2 fallback**, not a skill release or draft 4.0 hypothesis.
Exact definition: `project05-concept-card-skill/artifacts/source-v32/source-0009-howto-concept-card-extraction-with-llms-v3.2.md`, SHA-256 `b1cfa8b4114a299f621ada9898b63a4a8b2e4a3dfd961b939b8eea745f3872d9`;
required field rules lines 90–224 and checklist 632–650, plus the
unnumbered-chapter/no-PDF rules at lines 813–835. It defines nineteen core fields: concept, slug, category, subcategory, tier, source, source_slug, authors, chapter, chapter_number, pdf_page, section, extraction_confidence, aliases, prerequisites, extends, related, contrasts_with, answers_questions.
Distinguish defined rules from examples and completeness recommendations.
No new IDs, lifecycle/review states or `schema_version`; no inferred missing
values, new placeholders or confidence upgrades. This slice does not change
Project08 or the concept-cards skill.

All 233 baseline headers are structurally in scope. At the original pre-pilot input,
all 233 card paths and complete file bytes equalled `dffa504e851b03b8e4746f1941068e4cc850b612`.
The accepted index `project10-design-foundations/arc01-portable-contract/slice01-scope-and-portability-contract/artifacts/card-source-index.jsonl` (SHA-256 `ce5207eb89ddcfd4cb301dd49fc9cc6286561c6428c82b46bdaf7dc8aa6463cb`) supplies the historical
identity bridge; use parsed current identities independently, not displayed
aliases. Emit all233 rows with raw header identity, full typed metadata, body
hash and preserved baseline/current path/revision mapping. Walk every nested
path/type/state; no sampled headers or silent parser exclusions.

Current observations: nineteen core fields in every card, `layer`233,
`rosetta_stone`232 and `css_implementation`222. Nulls: subcategory24,
section75, chapter_number83 and pdf_page83. Preserve these states and all
extensions; absence remains absence. Wrong-shape `[[]]` occurs106 times in59
cards: aliases13, prerequisites14, extends42 and contrasts_with37.
These are reproducible observations, not acceptance or rendering-cause claims.
Cohorts remain Arnheim112/Cleland19/Tschichold19/Butterick37/Drasner12/
Brown10/Oklab13/Okhsv11: eight raw source-author identities, 150 book/83 web.

## Exact main write scope

| Pilot card | Input SHA-256 |
|---|---|
| `knowledge/design/concept-cards/art-and-visual-perception/depth-why-we-see-it.md` | `d67a42ed26257796db07dac5e07de2d7f4bf307138e9b6c59c5f661661453f3a` |
| `knowledge/design/concept-cards/munsell-colour-system/analogous-harmony.md` | `d067a4a3ea3c9beb90cb495fb790d268bf1484490a2fda48557afe0ab49e861a` |
| `knowledge/design/concept-cards/posts/additive-colour-mixing.md` | `8060e9c09110e09bb993cdca063d7843dc1a10d945063f6447c60c22c302bbfe` |
| `knowledge/design/concept-cards/posts/colour-space.md` | `83e2dc966f3835c072023830b3ced58c5ee14089794bde70bd10eb2e3fd4cebf` |
| `knowledge/design/concept-cards/posts/colour-gamut.md` | `a3d63d990c14cb9a2dc852c5b87c18f4475acb3061a1c11a0c16d3d8278d81ae` |
| `knowledge/design/concept-cards/posts/golden-ratio.md` | `09d132c5c18d83712cbdd389895f671c9eb6795935ef71a0102e6239e396655c` |
| `knowledge/design/concept-cards/practical-typography/all-caps.md` | `20b693adeb6828f877bf6f77f2360856d31e457f03afdd2a0bd4250e6788a58c` |
| `knowledge/design/concept-cards/the-new-typography/active-white-space.md` | `6e8c8a9ca10d36e52e37d0dae05bb3489b14a56acc076f00694f6f6b22083ba8` |
| `knowledge/design/concept-cards/posts/matrix-transformation-colour.md` | `872e8c6c5e360401d1f5332ae755a5c21542d09536221e28652e305f136fc680` |
| `knowledge/design/concept-cards/art-and-visual-perception/adaptation-level-and-visual-norms.md` | `17eca2340b7ec89bf15770461011748175c0904687447c3dc088aa0f4a604211` |

Additional source writes: new `scripts/normalize-design-card-metadata.rb`,
`knowledge/design/SKILL.md` (metadata version only, 1.0.3 to 1.0.4), and
`knowledge/design/version-history.md` (one matching micro correction entry,
all prior entries preserved). Thus thirteen main paths total. No other card,
guide, source original, Makefile/README/package list, skill or installed copy
changes. The helper is repository tooling, not a newly bundled skill asset;
its invocation is documented in the batch record. No new dependency installation,
publication or push. Current archived guides/entrypoint remain useful unchanged
apart from the version metadata. Check drift on exact inputs before mutation.

## Binding mapping and implementation recipe

1. Read authority and typed inputs; capture full intake/readback in the existing
   batch record. Reconcile the complete population to the original index.
   Use a strict leading UTF-8 YAML mapping with no BOM, duplicate keys, custom
   tags, merges or aliases. Inspect the AST **before** loading values so keys
   cannot silently overwrite. Reject malformed/fenced/non-mapping/multiple
   headers and unsupported types before any write. A parser failure remains
   in the233 denominator and blocks dependent conversion.
2. Keep every existing key, decoded scalar/type, list order and nested object.
   Authors remain scalar strings; preserve Unicode as the same decoded value.
   Keep root/nested mapping order. Preserve directory/source_slug identities
   even where the historical directory recommendation is unmet; record that
   gap instead of guessing a new attribution. Do not reinterpret confidence,
   relationships/CQs, extension ratings or null chapter numbers.
3. The sole data-shape exception: exactly `[[]]` in aliases/prerequisites/extends/
   contrasts_with becomes `[]`, consistent with the historical string-list/
   empty-array rules. Record each old/new occurrence and rule; no flattening
   elsewhere, removal of populated list items, null-to-empty or invented key.
4. Emit one leading `---` YAML mapping and unindented closing `---`, LF UTF-8,
   two-space container indentation. Quote all string values with JSON-compatible
   double quoting, emit decoded non-ASCII directly, `null` explicitly and empty
   arrays/maps as `[]`/`{}`. Existing plain safe keys may stay plain; quote other
   keys. Render nonempty lists/mappings as indented YAML blocks. Preserve decoded
   strings exactly, including literal backslashes; do not decode body escapes.
   Append the original body bytes from immediately after the closing delimiter,
   including their existing separator. Do not add/remove a body blank line.
5. Implement `ruby scripts/normalize-design-card-metadata.rb --check PATH...`
   as nonmutating inspection returning JSONL input/output hashes and typed
   metadata observations; `--write PATH...` applies that same transformation
   only to explicitly supplied tracked card paths under knowledge/design/
   concept-cards. Default/no arguments must not write. Prevalidate every supplied
   file and proposed output before mutation; a validation failure leaves every
   input unchanged. Reject symlinks, repeated/out-of-scope paths and conflicting
   simultaneous edits. Stage each valid output beside its input and replace it
   atomically per file; disclose an I/O interruption/partial batch if it occurs,
   stop and restore only this command's known outputs before retry. Never report
   all-file transactional guarantees for sequential replacements.
6. First virtual-check all233, then write **only the ten listed pilots**. Do not
   expand the pilot on an unexpected shape; report the held issue. Reparse with
   an independent installed decoder (Perl YAML::XS/JSON::PP is available) and
   compare the whole original typed object against only the four declared
   sentinel transformations, plus exact body bytes. Keep original input hashes
   outside the converter's derived observations; the converter cannot supply
   its own sole preservation oracle. A second check is byte-idempotent.
7. Produce the complete233-row inventory and a compact field-by-field crosswalk,
   pilot outcomes and the223 remaining paths (233 minus10 is223). The pilot
   and remaining set must be disjoint and union exactly233. Preserve all22
   observed root fields and nested extensions. Report missing/ambiguous rules
   without claiming full schema conformance or semantic/source acceptance.

The recommended implementation uses installed Ruby2.6.10/Psych3.1.0 AST and
safe loading, recursive emitter and JSON quoting; no general schema framework.
Local names/implementation organization are discretionary. Any alternative must
preserve this behavior; a consequential mapping change returns to CDC.

## Rendering diagnosis, meaningful checks and downstream boundaries

CDC observed the exact hosted matrix card at GitHub revision
`4e82e7a6f25fd7fec57fe074c1a6d204a751191f`; its bytes equal the current card.
[Native file view](https://github.com/billosys/ai-engineering/blob/4e82e7a6f25fd7fec57fe074c1a6d204a751191f/knowledge/design/concept-cards/posts/matrix-transformation-colour.md)
renders metadata as a table, including decoded Björn and nested 3×3 values.
Its body instead visibly contains literal Unicode escape text. Do not claim
that all existing metadata fails or that `[[]]` causes GitHub failure. Inspect
one structurally different pinned hosted reference where available; distinguish
actual observations from expected pilot output and record unavailable views.
Do not expand this into new rendering research beyond the approved metadata
question. Source fidelity is unnecessary for a lossless representation change.

Pilot checks: original/current field and body equality, correct four sentinel
rules, useful populated extension/list retention, null/absent distinctions,
Unicode/colon/backslash string equality, deterministic output and idempotence.
Require discriminating controls for dropped extension/list item, null-to-empty,
invented key, duplicate key, BOM/fenced header and changed body. Exercise parser
and preservation predicates on the corrupted actual candidates; mere fixture
labels are not evidence. Include one input-validation failure with no mutation.

Start with `make help`; run `make check-skills`, `make check-package-paths`
(including whole version/history and fresh-package contract), fresh `make design`,
source/planning `git diff --check`, exact committed scopes/trailers and individual
identity of all eight packaged Markdown members. Cards/helper are not presently
bundled: validate their source directly, do not pretend they are ZIP members.
Check owning version/history/entire tree and fresh output for duplicates.

Actual changed-revision hosted checks for **all233** remain Arc06/Slice02's
A06-05 gate. Do not push to create them under this assignment. Local parse/
prospective display checks cannot satisfy that gate. Keep baseline/current/
pilot revision and header/body locator bridges for Arc02 and final Arc04.
Body escapes/presentation and substantive card corrections stay at Arc02;
P10-11 original/capture/fidelity and all parent release gates remain open.

## Compact outputs, reading and return

Exactly four planning write paths: `artifacts/batch-record.md`,
`artifacts/header-inventory.jsonl`, `ledger.md` (evidence/notes only; statuses
CDC-owned), and `closing-report.md`. The machine233-row original/typed inventory
is justified as the preservation bridge for bulk use; the single prose batch
contains crosswalk, gaps, parser/mapping, pilot receipts, checks, failures and
owners. Do not recreate seven former draft reports or semantic validators.
All historical preparation notes, issued prompts, Arc01/02/Project08 evidence,
plans and parent ledgers are protected. Commit exact named paths separately on
main/planning with both required trailers. Report candidate parents, hashes,
checks/negative routes, covered denominators, failures/recoveries/unrun work,
six proposed row outcomes and next-slice applicability. CC proposes, never closes.

Required-full: this plan, ledger and initial prompt; concept-cards SKILL;
current design SKILL/history and applicable framework/management/work-verification
entrypoints. Required-section: concept-cards guide08 introduction and Perform Structural Validation; Project10 Scope/DoD/ImmediateSequence/metadata
addition/Workflow/CurrentStatus; Arc06 all capability/mapping/slice/verification/
workflow sections and all13 project/seven arc ledger rows; Project08 P-15 plan/
ledger adoption restriction; historical3.2 ranges above. Required-data: all233
full headers/nested typed paths, accepted index identities and ten full pilot
headers/body boundaries/hashes (not a new full teaching-body review). Conditional:
actual syntax/rendering counterpart needed to interpret a discrepancy. Reference:
historical preparation notes and other source/semantic evidence, not duplicated.
Recover truncated required reads; record actual ranges/hashes, checks and a
source-cited contract readback before edits. Intake passing already authorizes
execution; no further routine approval. Limit diagnosis to available assigned
headers/hosted examples, stop dependent work on a mapping disagreement, and
retain unavailable hosted checks as pending; no edition-acquisition detour.

## Author readiness and history

CDC inspected the actual source and enumerated all233 raw/typed headers by
complete structured projection (not233 narrative reading receipts), with exact
current-to-baseline file equality. A temporary Ruby AST/emitter trial normalized all233
virtually, preserved typed values except the four specified sentinels and body
bytes, and passed byte-idempotence. Its preservation check rejected eight actual
mutations: duplicate/BOM/fenced/extension-loss/null-empty/new-field/list-item-loss/
body-change. The ten paths cover all eight identities, all four sentinel fields,
null subcategory/page/section/chapter, absent extensions, nested objects and
non-ASCII decoded values. This is author preparation, not CC delivery or CDC
acceptance. No live source was edited. Psych safe_load/AST behavior was exercised
locally; independent Perl decoder (YAML::XS0.82/JSON::PP4.06) agrees on all233
complete original typed objects.
The fallback no-PDF/chapter rules explain existing nulls; empty-array evidence
is the lines643–644 checklist combined with the typed-list definitions.
An initial prototype hit a mixed binary/UTF-8 BOM check; comparing binary bytes
fixed it and the full trial passed. A guessed concept guide path was corrected
to `08-validation-verification.md`; the GitHub web fetch/IAB attempts failed,
then the native Chrome repository view supplied the actual bounded observation.

Apply concept-cards' separation of structural validity from semantic warrant:
normalization retains confidence/relationships, does not add lifecycle states,
and uses absence/null/preservation oracles. Apply the framework's no-silent-drop
rule to all233 and the design system's portable identity to existing local values.
This source pilot enables actual fixes now and a single all-card follow-up after
independent review; no read-only evidence phase is being reinstated.

- 1.2 (2026-10-12): Open combined contract/pilot after Slice08 independent closure;
  select authorized3.2 fallback, ten exact source cards and repeatable helper,
  reduce supporting outputs while preserving all six criteria/233-card obligations.
- 1.1 (2026-10-12): Operator consolidated the former unissued draft with pilot;
  obsolete separate output contract superseded before issuance.
- 1.0 (2026-10-10): Original planned metadata census/rendering contract.

Open-set checks: nine planning writes only, protected inputs/parent ledgers
unchanged, all13/10/7 parent criteria retained, four Slice08 done/six Slice01 open,
233 exact identities, ten hashes/eight source identities, 44 local destinations
and six fragments resolved, LF/EOF and diff checks passed. Main unchanged.

## Assignment history and I1 author readiness

- Initial `cc-prompt.md`, issued `e87186057c4795dfc342f15e06dc8e5a031c9ad2`, returned source `fe4e055885983be6d0b4bbbff1ef201485499aac` / planning `be623972b71f7be1002ed3932743c16a23dadb95`:
  S01-01/02/03 independently done; S01-04/05/06 open for F01 write-time drift/
  interrupted-batch handling and F02 sentinel-table accuracy.
- **Returned:** `cc-prompt-iteration01.md`, issued2026-10-12 by this introducing
  commit, predecessor initial prompt; returned source `d2188c45` / planning `1e7dc84c`;
  reviewed2026-10-13, F02 resolved but Unicode recovery F03 remains.
  Only main helper plus existing batch/ledger evidence/closing report change.
  All ten cards,233 inventory rows, version/history1.0.4 and schema mapping stay
  exact. I1's delta scope/check applicability supersedes initial source mutation
  and repeated-build instructions, not the six criteria or any parent obligation.

CDC inspected the actual helper and full raw/typed committed inventory, read
all233 headers through independent structured projections (not teaching bodies),
ran actual helper233/ten and positive/eight corruption controls, and reproduced
write-time losses in disposable tracked repositories containing actual input
card bytes. The algorithmic decisions for I1 are settled in its concrete recipe.
A temporary candidate buffer/guard/write-ledger/recovery shape passes conflict,
second-rename recovery and external-during-recovery witnesses without modifying
main. Ruby2.6.10/Psych3.1.0 APIs used are installed and exercised. No new schema
investigation or maintained checker framework. Runtime-private snapshots never
become card fields or public JSONL data; untouched ownership/path guards remain.

The crosswalk treats structural preservation separately from semantic warrant;
existing populated nested lists remain preserved and a conformance limitation
in F02, not an invitation to flatten them. Failure paths account for all own
writes, condition recovery on current output identity and preserve external work.
Optimistic checks do not promise a global filesystem transaction. The current
method leaves failed batches nonzero even when all own outputs recover.

- 1.3 (2026-10-12): Initial return independently accepts three criteria; issue
  one-helper I1 for reproduced write-time conflict/recovery failure and two
  inaccurate sentinel-table entries. Preserve six rows, source pilot and parent gates.

I1 open-set checks: six planning paths only; initial prompt/CC reports/inventory
and all13/seven parent criteria unchanged; six slice criteria preserved with
three done/three open. Thirty local destinations and six fragments resolve;
LF/EOF and diff checks pass. Main remains `fe4e0558` with no tracked changes.

## Iteration02 assignment and author readiness

**Accepted:** [cc-prompt-iteration02.md](cc-prompt-iteration02.md), issued
2026-10-13 by this introducing commit, predecessor I1. Input main `d2188c45` / planning `1e7dc84c`; returned `4ccc6f60` /
`9934079a`, accepted2026-10-13. Its former three-open state is historical.
Only two recovery byte comparisons and the same three CC return files change.

CDC inspected both output-identity guards and exercised the actual CLI with
original and reversed source fixtures. Ruby2.6.10 UTF-8 versus ASCII-8BIT string
equality falsely rejects identical Unicode bytes. A temporary first-site-only
repair still fails at the final guard; both `.b` comparisons restore the exact
original. This is source-grounded preparation, not an integrated self-repair.
Mapping, ten cards, immutable233 inventory and package inputs reproduce unchanged.
Guide08 keeps byte-preservation validation separate from semantic verification;
work-verification retains accepted claims by explicit unchanged-input comparison.
The ordered recipe, real failure oracle, two-site negative and compact reading/
return contract are in I2. No new decision or investigation is left to CC.

- 1.4 (2026-10-13): I1 review reproduces233/ten and resolves F02; hold bulk for
  F03 Unicode recovery. Issue two-comparison I2, preserve all six criteria and
  parent gates. Expedited Mode opens Slice02 after actual independent acceptance.

I2 open-set checks: exact six planning paths; six criteria/statuses unchanged
(three done/three open); issued prompts, CC outputs, inventory and parent ledgers
byte-equal to `1e7dc84c`. Thirty-five local destinations and nine fragments resolve;
LF/EOF and diff checks pass. Main remains `d2188c45` with no tracked change.

## Final acceptance and next assignment

[CDC final acceptance](cdc-verification.md#iteration02-independent-acceptance-and-slice-close--2026-10-13)
closes all six rows. Frozen helper, mapping and immutable inventory enable the
already authorized [Slice02 all-card assignment](../slice02-book-card-metadata/cc-prompt.md).
No card body/semantic, hosted-final or parent release gate is accepted here.

- 1.5 (2026-10-13): Independently accept I2's two-site byte correction; close
  six rows, preserve all earlier issued prompts/receipts and activate Slice02.
