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
