# Slice01 CC batch record

## Intake and pins

- Assignment: initial `cc-prompt.md`, issued by planning commit
  `e87186057c4795dfc342f15e06dc8e5a031c9ad2` (parent
  `a900b68a10a0110c453867b827f865a4d8008bb6`). The superseded unissued draft
  was not used as authority.
- Main/source input: `1489e76730b759f01fb1e839a18b363d8296b610`, tree
  `6058b581fb4d4c9c25599e07fca72e635bb4b392`. Planning HEAD at intake:
  `e87186057c4795dfc342f15e06dc8e5a031c9ad2`. Main was clean except the
  pre-existing untracked `knowledge/lfe/`; it is preserved.
- Required contract: Project08 P-15 is still open. Use the Operator-approved
  historical 3.2 fallback, not draft 4.0 or a skill-version inference.
  `project05-concept-card-skill/artifacts/source-v32/source-0009-howto-concept-card-extraction-with-llms-v3.2.md`,
  SHA-256 `b1cfa8b4114a299f621ada9898b63a4a8b2e4a3dfd961b939b8eea745f3872d9`;
  field definitions lines 90–224, empty-array checklist lines 632–650, and
  null chapter/page rules lines 813–835 were read in full.
- Intake files read: this issued prompt (SHA-256
  `5fe9c6b33b5624ffd6fbc664e36a858a1fd3cd80846e7177ae77da4d4b5126f8`),
  slice plan (`27e08e9e687bc193d9b9ae4b960a695fec28741f4ef0ddf7632c93fb4bad97ba`),
  ledger (`c27201874eca2cf6dd5b01f94b526a11aaa51022862b433c681164cbf987acc9`),
  Project10 Scope/DoD, Immediate Sequence, metadata addition, Workflow and
  Current Status; Arc06 scope, mapping, slice, verification and workflow
  sections and its seven rows; Project08 P-15 and its ledger restriction; the
  concept-cards skill and its structural validation section; current design
  skill/history; collaboration-framework, project-management, work-verification
  entrypoints and the prompt intake route. Their governing instructions were
  applied: structural evidence is not semantic acceptance; scope, histories,
  source/report parents and six open ledger rows are preserved.
- Runtime at intake: Ruby 2.6.10, Psych 3.1.0, Perl YAML::XS 0.82 and JSON::PP
  4.06 are installed. No dependency was installed. `make help` passed from the
  pinned source checkout before work.

## Contract readback and drift check (before source mutation)

The 3.2 contract names nineteen existing root fields. `concept` is the
human-readable name; `slug` is the lower-case hyphenated filename identity;
`category` is the primary taxonomy; `subcategory` is optional finer taxonomy;
`tier` describes prerequisite depth. Provenance is carried by `source`,
`source_slug`, scalar `authors`, exact `chapter`, integer-or-null
`chapter_number`, page-or-null `pdf_page`, and section-or-null `section`.
`extraction_confidence` is retained with its rationale in the body. `aliases`
are authority-control variants; `prerequisites` encode required prior
understanding; `extends` means builds upon/elaborates; `related` is
non-hierarchical; `contrasts_with` means commonly confused; and
`answers_questions` links competency questions. The definitions and examples
are distinguished from checklist recommendations. In particular, “empty array
if none” is a recommendation for the four string-list fields, not authority to
fill missing keys or turn null into empty. The chapter/page passage explicitly
allows null for unnumbered chapters and sources without PDFs.

| Existing field(s) | 3.2 reading and observed state in all 233 | Mapping/preservation rule |
|---|---|---|
| `concept` | Required identity string; 233 strings | Preserve decoded value and key position. |
| `slug` | Filename slug; 233 strings matched the filename stem | Preserve; do not derive or rewrite identity. |
| `category` | Primary taxonomy; 233 strings | Preserve current taxonomy values. |
| `subcategory` | Optional finer category; 209 strings, 24 null | Preserve null versus string; no default. |
| `tier` | Prerequisite depth; 233 strings | Preserve exact value; no recalculation. |
| `source` | Full source title; 233 strings | Preserve exactly. |
| `source_slug` | Source directory identity; 233 strings | Preserve even where a directory recommendation is unmet; never infer a replacement. |
| `authors` | Credited author(s), scalar string; 233 strings | Preserve scalar type and spelling, including multi-author spelling. |
| `chapter` | Exact chapter title; 233 strings | Preserve, including textual appendix/unnumbered labels. |
| `chapter_number` | Integer; null permitted by unnumbered/appendix rule; 150 integers, 83 null | Preserve integer/null state. |
| `pdf_page` | Page or null where no PDF; 150 integers, 83 null | Preserve integer/null state. |
| `section` | Section heading or null; 158 strings, 75 null | Preserve string/null state. |
| `extraction_confidence` | Confidence plus body rationale; 233 strings | Preserve; no confidence upgrade or semantic re-evaluation. |
| `aliases` | String-list variants; 233 root arrays, 13 exact `[[]]` sentinels | Only exact `[[]]` becomes `[]`; all populated/nested members and ordering remain. |
| `prerequisites` | Exact prerequisite slugs; 233 arrays, 14 exact sentinels | Only exact `[[]]` becomes `[]`; preserve all other members/order. |
| `extends` | Builds upon/elaborates; 233 arrays, 42 exact sentinels | Only exact `[[]]` becomes `[]`; preserve all other members/order. |
| `related` | Non-hierarchical associations; 233 arrays, no authorized conversion | Preserve exactly. |
| `contrasts_with` | Commonly confused concepts; 233 arrays, 37 exact sentinels | Only exact `[[]]` becomes `[]`; preserve all other members/order. |
| `answers_questions` | Competency-question references; 233 arrays | Preserve every question and order. |
| `layer` | Extension, present as string in all 233; not defined in selected 3.2 field set | Preserve as opaque existing value; do not infer semantics. |
| `rosetta_stone` | Extension, present in 232; root array with nested mappings in observed populated cases | Preserve absence separately from `[]`, all nested key/value types, and order. |
| `css_implementation` | Extension, present in 222; root array with nested mappings in observed populated cases | Preserve absence separately from `[]`, all nested key/value types, and order. |

This is an existing-field mapping, not a new schema adoption or full
conformance verdict. The 22 observed root keys above are the complete union;
there are no proposed IDs, review/lifecycle fields, placeholders or invented
facts. All observed extension internals remain opaque data. All body bytes,
including literal backslashes and blank-line separators, remain unchanged.

## Complete population and baseline reconciliation

The accepted Arc01 `card-source-index.jsonl` SHA-256 is
`ce5207eb89ddcfd4cb301dd49fc9cc6286561c6428c82b46bdaf7dc8aa6463cb`.
The raw/typed projection read all 233 current frontmatter blocks, retaining
the complete raw header, ordered typed metadata, exact path, whole-input hash,
body byte count and body SHA-256. It reconciled 233 unique paths to 233 unique
index identities with exact path-set equality. Main HEAD is the pinned commit;
all 233 card files equal their indexed bytes (the index represents the stated
baseline `dffa504e851b03b8e4746f1941068e4cc850b612`). There are no silent
parser exclusions. Observed distribution: Arnheim 112, Cleland 19, Tschichold
19, Butterick 37, Drasner 12, Brown 10, Oklab 13, Okhsv 11; 150 book-source
and 83 web-source cards. The full per-card raw/typed record and baseline/current
bridge is delivered in `header-inventory.jsonl`.

At intake the census found exactly 19 core keys on every card; `layer` on 233,
`rosetta_stone` on 232 and `css_implementation` on 222. Null counts are
`subcategory` 24, `section` 75, `chapter_number` 83 and `pdf_page` 83. Exact
wrong-shape sentinel counts are `aliases` 13, `prerequisites` 14, `extends`
42 and `contrasts_with` 37, 106 occurrences across 59 cards. The ten assigned
paths and SHA-256 values were checked against the plan before mutation; the
remaining set is 223 paths. These counts describe the input, not a diagnosis
that all metadata fails to render or that sentinels caused a hosted failure.

Input/header contract checked: UTF-8, one leading `---` block with a closing
`---`, mapping root; AST inspection rejects duplicate keys, aliases/anchors,
merge keys and custom tags before safe loading. Root and nested values are
recursively typed; the complete original typed object is the preservation
oracle apart from the four exact sentinel transformations. Proposed output is
LF UTF-8 with a leading/closing frontmatter delimiter, two-space nested
containers, JSON-compatible double-quoted string values, decoded Unicode,
explicit `null`, `[]`, `{}`, and stable mapping order. The body starts
immediately after the closing delimiter and is byte-preserved including its
separator. Every path is prevalidated before any write; replacement is atomic
per file only, so no batch-transaction guarantee is made.

## Rendering observation and limits

The assigned pinned reference is matrix-transformation-colour at revision
`4e82e7a6f25fd7fec57fe074c1a6d204a751191f`. Network page fetch returned
“Cache miss”; browser inventory was empty and Chrome was unavailable. A second
structurally different pinned reference was also attempted and unavailable.
Therefore this CC could not observe a live hosted rendering. The supplied plan's
prior CDC observation is that the matrix card's metadata appeared as a table,
including decoded Björn and nested 3×3 values, while its body displayed literal
Unicode escape text. That is prior CDC evidence, not a new CC observation.
Expected normalized metadata display is prospective. No claim is made that all
metadata fails, that `[[]]` explains the hosted symptom, or that a changed
revision has been checked. Changed-revision hosting for all 233 is Slice02.

## Ten pilot input headers and body boundaries

All ten complete raw headers, typed values, whole-input hashes, body byte
counts and body hashes were inspected from the census before source edits.
This bounded roster makes the exact sentinel-only changes reviewable; the full
records are in the inventory.

| Path | Before: exact sentinel fields | Other preservation-relevant facts | Body bytes / SHA-256 |
|---|---|---|---|
| `knowledge/design/concept-cards/art-and-visual-perception/depth-why-we-see-it.md` | `extends`, `contrasts_with` | Nested extension mappings; populated prerequisites/related/CQs | 8000 / `33fb17be740aa6c8058cef9beda45ff908c613f8da5a63775e08437d172582ed` |
| `knowledge/design/concept-cards/munsell-colour-system/analogous-harmony.md` | none | `section: null`; nested CSS string with newline | 4330 / `368366c90fcfbd7fbb1a3e2334abb717df9d36b1befb4bb9a7df0072b23f87a2` |
| `knowledge/design/concept-cards/posts/additive-colour-mixing.md` | `aliases`, `prerequisites`, `extends` | chapter/page/section null; no `css_implementation`; populated nested extension | 4533 / `afb287818f82160c3075d25bd9ed8ec7b0884e9ce059566aa3c6fcfe17bf4d48` |
| `knowledge/design/concept-cards/posts/colour-space.md` | `aliases`, `prerequisites`, `extends`, `contrasts_with` | no visual extensions; section null; aliases sentinel is distinct from later literal-backslash identity concern | 5019 / `c59a6bd6a167460d192cf205f4f69b63d41795a0fc1d6c14c24af3afe4e70d88` |
| `knowledge/design/concept-cards/posts/colour-gamut.md` | `aliases`, `prerequisites`, `extends`, `contrasts_with` | null chapter/page/section; Unicode author decodes to Björn | 4726 / `298b7c90f000f892a0f19446991238ecd62f777076be1e6e49b02e7a2c52cae5` |
| `knowledge/design/concept-cards/posts/golden-ratio.md` | `prerequisites`, `extends`, `contrasts_with` | populated nested aliases, Rosetta Stone and CSS mappings; Greek/math Unicode and literal source escapes | 7718 / `c90d97499fa66cdf0116a9bcfe8709bddf2e92994167c0d4f7c141a427fe2280` |
| `knowledge/design/concept-cards/practical-typography/all-caps.md` | none | null chapter/page; nested CSS implementation | 3795 / `017f561bc7e8067db6b3019dc26d16168fc6f35cc266cbb4dfb39d62b8f05e74` |
| `knowledge/design/concept-cards/the-new-typography/active-white-space.md` | none | explicit empty arrays; null section; nested CSS implementation | 4815 / `911888837818cdae885682ea6f3b180d393585dec4caee70c745c65d01ede250` |
| `knowledge/design/concept-cards/posts/matrix-transformation-colour.md` | `aliases`, `contrasts_with` | nested Rosetta mapping; decoded Björn; hosted reference above | 6291 / `5aeddf6cc349a3ee84be031ebb36dc3859232c79eb9e62de57b510d820c93f57` |
| `knowledge/design/concept-cards/art-and-visual-perception/adaptation-level-and-visual-norms.md` | none | null subcategory; populated Rosetta Stone; null/empty distinctions retained | 7375 / `a10904d6d5ba0a0f0f2870a83c28d5c2fc7ba9d104dd5a50664ceba50c147fc0` |

## Work and review boundaries

Authorized main paths total thirteen: these ten cards, new
`scripts/normalize-design-card-metadata.rb`, design SKILL metadata only
(1.0.3→1.0.4), and one corresponding design version-history entry. Authorized
planning paths total four: this record, `header-inventory.jsonl`, ledger
evidence/notes only, and `closing-report.md`. No card outside the ten, skill
teaching text, other project, Project08, package membership, source original,
install, publish or push is authorized. CC may propose all six ledger outcomes;
all six statuses stay `open` until independent CDC review. All-233 changed
revision hosted checks and bulk conversion remain downstream.

Intake command recovery: an initial Ruby census one-liner had a syntax error
and executed no work; a subsequent complete projection was created only under
`/private/tmp`, then its size, 233 line count, unique path reconciliation,
core-field presence, source pin and body-boundary hashes were checked here.
No source or planning file had been changed when this readback was written.

## Execution and validation receipts

- Source candidate commit: `fe4e055885983be6d0b4bbbff1ef201485499aac`, parent
  `1489e76730b759f01fb1e839a18b363d8296b610`; exactly the thirteen authorized
  source paths. Commit trailers are separate lines. The source worktree is clean
  apart from preserved untracked `knowledge/lfe/`. Design skill source metadata
  and history both report 1.0.4; the teaching body is unchanged.
- The helper at `scripts/normalize-design-card-metadata.rb` uses Ruby 2.6.10 /
  Psych 3.1.0. It parses an AST before `safe_load`, rejects duplicate keys,
  aliases/anchors, merge keys, custom tags, invalid UTF-8/BOM/fenced/multiple or
  non-mapping headers, and unsupported recursive value/key shapes. `--check`
  is nonmutating; `--write` accepts explicit tracked card paths only. It
  prevalidates every path/output before sequential same-directory atomic
  replacements. It does not promise multi-file transactionality. No arguments
  exited 0 without writing. JSONL includes input/output whole-file hashes,
  complete typed input and transformed metadata, and body byte/hash values.
- Before the pilot write, the helper checked 233/233 tracked card paths. All
  paths reconciled with the accepted index and original input hashes; the
  complete typed metadata agreed with the raw/typed census. The independent
  Perl YAML::XS 0.82 / JSON::PP 4.06 decoder compared all 233 virtual outputs
  with the only four permitted sentinel rules: typed mismatches 0, body-byte
  mismatches 0. These checks ran before source mutation.
- The write accepted exactly the ten named inputs after all ten exact intake
  hashes matched the plan. Ten files received deterministic frontmatter
  serialization; 16 exact sentinel occurrences across six cards became empty
  arrays. The other four pilot cards had no sentinel value delta. All other
  metadata values, extension/nested shapes and order remain unchanged.
- Post-write helper `--check` returned 233/233. Its prospective output hash
  equals the current input hash for all ten pilots (10/10 idempotent). The other
  223 remain unchanged at baseline; `--check` reports their prospective
  formatting output without writing it. Independent Perl comparison against
  the original census found 233 rows, 10 pilots, 223 untouched, typed
  mismatches 0, body mismatches 0, and path/hash allocation mismatches 0.
- Negative controls used serialized pilot-derived YAML candidates and the
  complete-object/body preservation comparisons. All eight were detected:
  dropped `rosetta_stone` extension; dropped nested aliases member; null
  `section` changed to `[]`; invented `schema_version`; duplicate root key;
  BOM; fenced frontmatter; and changed body byte. A write request containing a
  valid first pilot plus an out-of-repository second path exited 1 during
  prevalidation; the first pilot's SHA-256 remained
  `8cd71ebf7b63945a3957b4caeb8f6a911dce7b372f40f425cfeacfedf21041a9` before
  and after. No card changed during that failure witness.
- Complete inventory:
  `artifacts/header-inventory.jsonl`, 233 JSONL rows, 1,789,888 bytes,
  SHA-256 `c7306e8a62291fa635e154463553fd990a9b12d91d70cb4403a0259f9e49dd5c`.
  Every row carries the accepted source-index record, baseline raw header and
  typed metadata, current raw header and typed metadata, baseline/current path,
  whole-file hash and revision, exact body bytes/hash, pilot membership, and
  any sentinel delta. Independent inventory checks confirmed 10/223 disjoint
  populations with union 233 and source revision
  `fe4e055885983be6d0b4bbbff1ef201485499aac`.
- Make gates: `make help` passed; `make check-skills` passed (24 skills; all
  descriptions within the hard validator limit, 18 over the 300-character
  editorial target); `make check-skill-versions` passed (24 source skills,
  24 packages, 0 errors); `make check-package-paths` passed (24 zips, 388
  Markdown files, 0 hard failures, 596 warnings, 3 explicit exceptions, 681
  skipped external URLs); fresh `make design` succeeded. Package-path warnings
  are retained as findings, not promoted to failures. Eight Markdown members
  in `visual-design-system.zip` were individually byte-identical to source:

  | Member | Bytes | SHA-256 |
  |---|---:|---|
  | `visual-design-system/SKILL.md` | 8950 | `b0b91010ac762616dd420cbfe37c00256e97dec043ecd7b5ddf29c199ecf2ea8` |
  | `visual-design-system/version-history.md` | 1396 | `f62d7909b93fbe3e0cc0f9c8868a001526ba95cbee0b1b6094f25e3f40f20c7c` |
  | `visual-design-system/guides/colour.md` | 3840 | `cff6170bbeb08c62a26580a9b0d768b42e50d042bac40f4d7b829f01690ab97a` |
  | `visual-design-system/guides/foundations-of-design.md` | 29583 | `347378644c54e53bf4a3ab8025b8449e74b6cdd50bbd1050661297dc7696c60a` |
  | `visual-design-system/guides/breaking-the-layout-monoculture.md` | 21764 | `8dfc00d23b870087b83d0c322c6fd95406e8ae7c001515a4bd7dae7ecb450d6f` |
  | `visual-design-system/guides/design.md` | 10977 | `9347a9277528f008f2428627dced9531e8d7bcd7a2ebe135120a2a9811d74d2a` |
  | `visual-design-system/guides/type.md` | 3396 | `ec74e3cf8ef1b32dd340d27c0fcae6e923c52b59778e7cbe8d226aa92fe672b2` |
  | `visual-design-system/guides/layout.md` | 35706 | `af50575508c1f44cd870b480f729ff64897943293576f047ac9737875941822` |

- `git diff --check`, staged diff check and exact thirteen-path staged allowlist
  passed. No source, card, guide, package-definition or Project08 path outside
  the issued list was committed. Package builds remained generated/ignored.
- Hosted-view limit: direct web fetches for the assigned matrix card and a
  structurally different pinned reference returned “Cache miss”; browser
  inventory was empty and Chrome was unavailable. The supplied plan records
  CDC's earlier observation of a metadata table with decoded Björn/nested
  values and literal Unicode escape text in the body. CC did not reproduce that
  live view, so it remains prior CDC evidence. Expected candidate display is
  prospective only. Do not infer a general metadata rendering failure or a
  sentinel cause. Exact changed-revision hosted checks for all 233 stay with
  Slice02; no push/publication occurred.

### Failure and recovery log

- A preflight projection initially reported some body spans one byte short on
  Unicode-bearing cards because its temporary delimiter offsets mixed text and
  byte indexing. It was discarded and regenerated from raw byte delimiters;
  the corrected 233 body hashes/lengths match the helper and independent Perl
  decoder. The durable inventory uses the corrected split.
- The first helper check exposed a missing Ruby process-status import; after
  correcting it, the next check exposed the same Unicode delimiter-offset
  risk in the helper. The implementation now validates UTF-8 then performs
  byte-based delimiter matching. Focused Unicode check, all-233 virtual check,
  independent decoder and actual pilot output passed afterward.
- The first package-gate invocation was denied while Make created its standard
  `build/` directory; no validation was counted from that attempt. The exact
  gates were rerun with build write access and completed successfully.
- A source-history append guard and two inventory-construction assertions
  rejected their assumptions before card changes or durable inventory output;
  each was corrected using the observed history terminator, committed source
  hash and distinction between current input versus prospective converter
  output. No path outside the issued scope was changed.
- Because a one-blank-line cleanup followed the first successful package build,
  all requested Make gates and the fresh design ZIP were rerun against the
  committed source. The eight-member byte-identity check above uses this final
  rebuilt ZIP; the rerun exited 0.

### Downstream ownership

- CDC Sofie, via Operator relay, owns independent Slice01 review and any
  acceptance. All six criteria remain open until that review.
- No Slice02 prompt is opened by this return. CDC owns its applicability and
  exact all-233 plan/ledger revision after accepting this pilot; Operator/CDC
  own availability and attribution of exact-revision hosted checks. No bulk
  write or publication is authorized here.
- Arc02 owns substantive body/escape and source-fidelity questions; this
  metadata-only commit did not change body bytes. Arc04 owns release/package
  composition after downstream source revisions. The inventory's baseline
  source-index records and body hashes provide the Arc02/Arc04 locator bridge.
