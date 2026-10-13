# Arc06 Slice01 — CC proposed closing report

## Disposition

CC proposes completion of the six Slice01 outcomes below. All six ledger
statuses remain `open`; CDC Sofie must independently review this report, the
source candidate and the linked evidence before accepting any row. No schema,
semantic, source-fidelity, hosted-final or Project10 release acceptance is
claimed.

| Criterion | CC proposal | Evidence and limit |
|---|---|---|
| S01-01 — authority and populations | Proposed done | The intake record pins the issued planning parent, main source parent, accepted baseline index and historical 3.2 definition. Project08 P-15 remains open; no draft 4.0 or skill-version inference was used. The 233 identities and input hashes reconcile. |
| S01-02 — raw/typed census | Proposed done | The [233-row inventory](artifacts/header-inventory.jsonl) includes complete baseline/current raw headers, typed metadata, nested extensions, hashes and source-index records. AST guards ran before loading; Perl YAML::XS/JSON::PP independently compared all 233 virtual and actual card values/body bytes with zero mismatches. This is structural preservation evidence, not semantic warrant. |
| S01-03 — existing-field crosswalk | Proposed done | The [batch record](artifacts/batch-record.md#contract-readback-and-drift-check-before-source-mutation) maps all 19 historical fields plus the three extensions, distinguishes definitions from checklist recommendations and preserves missing/null/empty distinctions. No field or fact was invented. |
| S01-04 — preservation/rendering contract and controls | Proposed done with hosted-view limit | All eight serialized corruption controls were detected; a write-mode validation failure left its first valid input unchanged. The assigned pinned GitHub matrix observation and structurally different reference could not be opened in this environment. The batch record labels the rendering symptom as prior CDC evidence, records the failed fetch/browser attempts, and makes no general failure or sentinel-cause claim. Changed-revision all-233 hosted checks remain pending for Slice02. |
| S01-05 — pilot and full allocation | Proposed done | Main commit `fe4e055885983be6d0b4bbbff1ef201485499aac` contains exactly ten assigned cards, the helper and paired design skill version/history update. Independent validation found the 10 pilot and 223 remaining paths disjoint with exact 233 union; all body bytes are preserved. Bulk change awaits CDC acceptance. |
| S01-06 — scoped return and owner accounting | Proposed done | Source and planning commits use separate exact allowlists and the required trailers. Make/version/package gates, negative routes, one initial sandbox failure and successful rerun, unavailable hosted checks, review owners and downstream applicability are recorded here and in the [batch record](artifacts/batch-record.md#execution-and-validation-receipts). |

## Source candidate and evidence

- Source parent: `1489e76730b759f01fb1e839a18b363d8296b610`.
- Source candidate: `fe4e055885983be6d0b4bbbff1ef201485499aac` (13 paths; both
  required co-author trailers). The helper is
  [`normalize-design-card-metadata.rb`](../../../../../../ai-engineering/scripts/normalize-design-card-metadata.rb)
  in the main checkout; the inventory maps each output to its source-index
  record and body locator.
- Planning parent for this CC: `e87186057c4795dfc342f15e06dc8e5a031c9ad2`,
  whose predecessor is `a900b68a10a0110c453867b827f865a4d8008bb6`.
- Inventory: 233 rows, 10 pilot / 223 remaining, SHA-256
  `c7306e8a62291fa635e154463553fd990a9b12d91d70cb4403a0259f9e49dd5c`.
- Input distribution remains 150 book-backed / 83 web-backed. The ten pilots
  sample all eight source-author identity cohorts, extension states, nulls,
  nested values, non-ASCII text and all four sentinel fields.
- `make help`, `make check-skills`, `make check-skill-versions`,
  `make check-package-paths`, and fresh `make design` completed. The package
  path check scanned 24 zips and 388 Markdown files, with 0 hard failures and
  596 warnings. All eight Markdown members in the design ZIP matched their
  source bytes. `git diff --check` and the exact source allowlist passed.
- No push, install or publication occurred. Body hashes did not change. The
  pinned matrix card's literal body escape report is retained as prior CDC
  evidence; CC did not get a live browser view. Source fidelity and body fixes
  remain Arc02 work; all-233 changed-revision GitHub checks remain unrun.

## Review, handoff and next-slice readiness

- **CDC Sofie**, through the Operator relay, owns independent review and all
  six acceptance decisions. The source candidate and this report are ready for
  that review; no row is closed by CC.
- **Slice02 is not opened or ready for prompt issuance yet.** It depends on
  independent acceptance of this contract/pilot. The existing Slice02 plan is
  an explicitly superseded 150-book-card draft; CDC must revise the active
  plan/ledger to the current all-233 normalization/rendering scope, recheck the
  accepted contract's applicability, and pin the then-current main revision
  before issuing its prompt.
- **Operator and CDC** own the availability and attribution of exact-revision
  hosted checks for the changed population. No push or publication was
  authorized in Slice01; unavailable host evidence leaves that gate open.
- **Arc02** owns substantive claims, source fidelity and body/presentation
  escape repair. **Arc04** owns downstream release and package composition
  after later source revisions. The inventory's immutable baseline index rows,
  current commit/path mapping and preserved body hashes are the locator bridge
  for both.

## Iteration01 return

CC proposes this correction for independent review by CDC Sofie via Operator
relay. The assignment and its exact behavior are recorded in the linked
[Iteration01 batch evidence](artifacts/batch-record.md#iteration01-execution-and-current-dispositions).
It corrects F01's helper write path and F02's two historical sentinel-table
entries. It does not re-open accepted intake, census, or mapping conclusions.

| Criterion | Current CC disposition | Evidence and limit |
|---|---|---|
| S01-01 — authority and populations | Remains done at accepted evidence | Prior independent disposition retained; no authority or population change. |
| S01-02 — raw/typed census | Remains done at accepted inventory bytes | All 233 actual candidate `--check` records matched current input hashes, typed input metadata, body hashes/lengths and the expected exact transformations. Inventory bytes are unchanged. |
| S01-03 — existing-field crosswalk | Remains done at accepted mapping | F02 table is corrected: additive prerequisites/extends; gamut prerequisites/extends/contrasts_with. Both populated nested alias arrays remain preserved. This does not accept a 4.0 profile or claim full string-list conformance. |
| S01-04 — preservation/rendering contract and controls | Open, return for CDC review | CDC's supplied two-case fixture plus actual CLI witnesses cover prewrite conflict, interrupted replacement, external edit held during recovery, late conflict, recovery failure, missing/symlink targets, invalid input and duplicate path. All interrupted cases exited nonzero with zero JSONL and path/failure accounting. Hosted observations remain attributed to prior CDC; changed-revision hosting remains open. |
| S01-05 — pilot and allocation | Open, return for CDC review | Main helper candidate is `d2188c45a451be8b5e82f534f9a9ac067c137b64`, parent `fe4e055885983be6d0b4bbbff1ef201485499aac`, exact one-file scope. All ten pilot outputs remain byte-idempotent, and no card or 233-row inventory bytes changed. Bulk conversion still awaits CDC review and authorization. |
| S01-06 — scoped return and owner accounting | Open, return for CDC review | Main candidate has both required trailers; planning update is limited to this batch record, ledger evidence/notes and closing report. Package inputs plus `Makefile` compare byte-identically to the accepted source parent. Failed harness setup assertions were corrected and disclosed in the batch record. |

The exact CDC-supplied fixture ran against candidate `d2188c4` from committed
source bytes and original `1489e767` card blobs. Ordinary two-file conversion
and follow-up check each returned two rows with exact seven-field public
records, no private original-byte field, exact typed transformation/body
preservation, and byte-idempotent output. The full 233-path `--check` returned
0; no private buffers were serialized, 90 remaining sentinels were the only
prospective typed changes, and all ten pilots were idempotent. Ruby syntax
validation returned `Syntax OK`. The last input-hash check occurs inside the
atomic replacement helper after temporary-file staging and immediately before
`rename`; the write hook witnesses were rerun against this final candidate.

CDC-accepted `make help`, `make check-skills`, `make check-package-paths`, and
fresh `make design` at the parent revision remain applicable because the
helper is unbundled and all eight packaged Markdown sources, design version
history, and Makefile are byte-identical to that parent. No new ZIP build was
needed. These checks were not rerun for this helper-only change. No live card
was used by any witness; no hosted, semantic, source-fidelity or release result
is claimed.

All six ledger status values remain CDC-owned and unchanged: S01-01/02/03 are
done; S01-04/05/06 are open. Slice01 remains open, Slice02 remains unissued,
and no parent composition or release approval is implied.

## Iteration02 return

CC proposes this two-site recovery correction for independent CDC review. The
source candidate is `4ccc6f6055743d8e8b53251d7e8852f04d1ed181`, parent
`d2188c45a451be8b5e82f534f9a9ac067c137b64`; its only changed path is
`scripts/normalize-design-card-metadata.rb`. The two recovery comparisons now
compare file bytes against `record.fetch('output').b`; UTF-8 serialization,
cards, inventory, parser, transformation, serializer and all other helper
lines remain unchanged. The planning return is limited to this batch record,
ledger evidence/notes and this closing report. These records are proposed-done
for CDC review; this report does not close the slice.

The official two-case CLI fixture ran against the committed helper and pinned
original blobs in additive-first and matrix-first order. Both prewrite edit
cases exited nonzero with zero JSONL, retained exact external first bytes and
untouched exact second originals, and reported conflict/held paths. Both
second-rename failures exited nonzero with zero JSONL, restored exact originals
for both paths, and reported written/restored without held or recovery-failed
paths while preserving the injected error. Matrix-first ordinary conversion
and check each returned two public rows; typed values followed only the four
exact sentinel rules, body bytes/hashes matched the inventory, private state
was absent, and the second check was byte-idempotent. Additional real-CLI
cases retained a literal edit made during failure and reported held; injected
rollback failure retained the completed output and reported recovery-failed;
a disposable helper with only the second `.b` reverted failed exact-original
restoration as expected.

The candidate's nonmutating `--check` returned233 records. All233 current input
hashes, typed inputs, body byte/hash observations, exact transformations and
public seven-field records matched the immutable inventory; ten pilot rows
were idempotent and90 exact non-pilot sentinels remain. `ruby -c` and
`git diff --check` passed. Each of the eight packaged design Markdown inputs
and `Makefile` compares byte-identically with accepted source parent `fe4e0558`,
so the accepted package gates remain applicable; they were not rerun and no ZIP
was rebuilt. Prior parser/serialization/path/symlink/duplicate controls remain
applicable because those methods and bytes are unchanged. No live `--write`,
card mutation, inventory change, hosted check, semantic acceptance, source
fidelity claim or release check occurred. The batch record preserves the
corrected one-off harness attempts and their successful reruns.

Planning candidate: parent `ce393b8cdcac47818538518a21c526ceda59482a`; exact
three-path scope is `artifacts/batch-record.md`, `ledger.md`, and
`closing-report.md`. Both source and planning commits carry the required
co-author trailers. The six row statuses remain CDC-owned and unchanged:
S01-01/02/03 done; S01-04/05/06 open. Slice01 remains open; no Slice02 prompt,
bulk conversion, changed-revision hosted acceptance, semantic acceptance,
parent composition or release approval is claimed.
