# Slice21 independent review — initial candidate, 2026-10-18

**Verdict: refinement required.** S21-02, S21-03 and S21-04 are independently
accepted at the bounded scope below; S21-01 remains open for F01. Four opening
criteria and four return rows are accounted for. This record does not close
the slice or change its ledger, plans, source or CC evidence.

## Reviewer, authority and candidate

Actual reviewer: Codex context `/root/s21_review`, assigned independent reviewer
under the Two-Contributor arrangement in Operator-authorized Autonomous Mode.
External CC implemented this candidate; CDC Sofie `/root` coordinates integration.
This is neither CC self-review nor a permanent CRC appointment. Governing mode
and attribution are committed in planning `f8c39d15`; assignment is the preserved
`cdc-review-prompt.md`, supplementing the unchanged `cc-prompt.md`.

SOURCE is `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/design-arc02-autonomous`,
branch `codex/project10-arc02-autonomous`, HEAD
`d19de06d1e79e22dac0b67b5bf2e527c048a1f73`. It remained tracked-clean throughout
review. PLANNING is the canonical `.worktrees/planning`, branch `planning`.

The reported implementation is `dba03b611572eadb15525e814282dde67d65a9bd`, parent
`52bfa46332592106f9301226571d6f441df8ce2d`; CC return is
`8f326bcb0b2e39e05884942a3955d22b7004562f`, parent
`e9876d8a08740694d40f66db6f0a79faf31340ee`. Direct Git object checks reproduce:

| Objects compared | Exact `knowledge/design` tree identity |
|---|---|
| Reported candidate `dba03b61` and current `d19de06d` | `799227297de46d563b47c909a5597f3b611ec84a` |
| Issued predecessor `52bfa463` and rewritten predecessor `64e23846` | `4f28bdf0d0ca6d2f9e20a62959e620f1940a6686` |

Thus the entire design subtree, not merely selected cards, supplies a valid
reported-to-current bridge. Framework/native gate inputs outside design changed;
their historical gate output was not promoted to fresh evidence. Gates below
ran against actual current SOURCE. This record is the sole reviewer-authored
durable file; no source repair, commit, push or publication was performed.

## Inputs inspected and method

Read Project10's active plan first, then Arc02's active plan, both parent ledgers'
complete criteria, and the complete Slice21 plan, ledger, issued prompt, review
prompt, 375-line CC batch and 88-line closing report. Read current AGENTS,
collaboration-framework, PM wayfinder, methodology's workflow/Autonomous sections,
closing-slice guidance, work-verification's ledger/evidence/row/independence guides,
testing's native validation guidance, visual-design-system and Concept Cards
entrypoints and evidence/graph/CQ guidance. Truncated guidance outputs were
recovered in bounded reads before conclusions; receipts alone were not evidence.

Read all six final cards, their complete before/after diffs, all six complete
prepared Butterick pages (682 lines), the complete type guide and owning history.
Read Core Definition, Prerequisites and Relationships in `font`, `small-caps`,
`all-caps`, `body-text` and `typographic-color`. These endpoint sections warrant
local premises, not whole-endpoint acceptance. Read Slice20's current conceptual
CQ1/CQ12 answers and checked relevant current typography/heading/guide support.

Primary definition prose/tables checked live: [CSS Fonts4 Working Draft,
2026-10-16](https://www.w3.org/TR/2026/WD-css-fonts-4-20261016/), §§6.3,6.4,6.7,6.12,7;
[CSS Text3 §7.2 including cursive scripts](https://www.w3.org/TR/css-text-3/#letter-spacing-property);
[Adobe kerning/tracking](https://helpx.adobe.com/indesign/desktop/format-and-style-text/tabs-indents-and-spacing/about-kerning-and-tracking.html),
Types of kerning through measurement. Linked test listings were not run.

Independent direct queries parsed the complete accepted 233-row index at
`9cc203380aede19231b7c5119f0b43d9fe3d0e78`, all current card paths, six raw and
typed headers, every relation/CQ occurrence, frozen sections and protected
populations. No maintained validator or fixture subsystem was added.

## F01 — P2: restore the requested round/flat teaching

Location: SOURCE `knowledge/design/concept-cards/practical-typography/optical-vs-metric-spacing.md:79`
(also the generic pair inventory at lines45/58). The final Example1 says Butterick
“also discusses” `un`/`no` and `nt`/`it`, but never explains the round/flat
comparison. Merely retaining pair names loses what the example teaches.

The complete prepared `sources/md/practical-typography/metrics-vs-optical-spacing.md:32–36`
reports that metrics balances `un`/`no`, while optical brings round `o` closer
to flat `n`. The predecessor Example1 retained that concrete contrast. Binding
recipe6 explicitly requires retaining the round/flat comparison, and the slice
plan requires useful examples rather than generic inspection stubs. This is a
source-supported teaching omission, not a demand for a new rendered specimen.

Required repair: restore the concrete round/flat explanation with Butterick's
illustration attribution and existing no-new-rendering limitation. Preserve the
qualified Adobe comparison and all protected representations. Correct the batch's
optical-card fidelity/teaching assessment to reflect the repaired wording and
return that exact revision. No new research, font test or other-card rewrite is
needed. Owner: next assigned CC; acceptance: independent reviewer after repair.

## Six-card five-dimension findings

All judgments concern available prepared material and actual candidate bytes.
Original immutable capture/conversion fidelity remains P10-11-blocked for every
card; historical extraction confidence is preserved and is not certification.

| Card | Available-source fidelity | Technical correctness | Scope | Internal/cross-card consistency | Local edges/CQs |
|---|---|---|---|---|---|
| OpenType features | Font/application distinction and source-era support preserved. | Reviewed feature availability/default distinction passes. | Required shaping is separated from optional Latin refinements; no current support survey. | Compatible with the five cohort cards and guide. | T01,T09–12/B01–05 pass; CQ1 contribution is partial. |
| Kerning | Visible-gap example and attributed advice retained. | Metric controls, no-data case and tracking distinction pass. | No universal default or equal-gap guarantee. | Repeated error/example claims agree with tracking and optical cards. | T02,T13–15,T26/B06–09 pass; CQ5 absent, CQ12 spacing contribution. |
| Letterspacing | Source range, size exceptions and disputed Goudy account retained. | Tracking/shaping and illustrative percentage mapping pass. | No mandatory caps range, lowercase ban or comfort claim. | Caps/small-caps endpoints and guide agree; no blanket script rule. | T03,T16–18,T27/B10–13 pass; CQ11 absent, CQ12 partial. |
| Ligatures | Collision, nonconnecting `gy`, manual-text warning and preference retained; missing names stay unknown. | Required/optional and shaping/text distinctions pass. | No search/AT outcome or Latin rule generalized to every script. | Feature and kerning explanations agree. | T04,T19–20/B14–16 pass; CQ5 absent. |
| Alternate figures | Four combinations, TOP40, columns, zero/one clue and height exception retained. | Form/advance choices and alignment limitations pass. | No default/oldstyle superiority or all-font availability promise. | OpenType, caps/body endpoints and packaged numeric request agree. | T05–06,T21–22/B17–20 pass; CQ5 anatomy absent. |
| Optical/metrics | Nu/un and accumulation argument retained; round/flat teaching is missing: F01. | Qualified definitions and distinction from optical sizing pass. | Source judgment/patent are attributed; no price, legal or empirical guarantee. | Kerning/tracking/texture premises agree. | T07–08,T23–25/B21–25 pass; CQ5 absent, CQ12 texture/spacing contribution. |

## Local semantics and discriminating checks

Directly recovered 27 header tuples: 8 prerequisites,17 related,2 contrasts,
0 extends. Every card/field/index/target matches the CC table T01–T27. Checked
each actual premise separately: T01–08 are understanding dependencies in the
target→card direction; T09–25 are symmetric, qualified feature/context
associations; T26–27 are the kerning/tracking contrast, not two independent
warrants. In particular, T20 is editorial substitution-versus-spacing association,
T24 is texture rather than literal colour, and T25 retains Butterick attribution.
No reciprocal-field requirement or acceptance of whole endpoints is invented.

Independently inspected all25 predecessor body statements against final sections:
B01–05 feature/resource scope; B06–09 pair/tracking/control scope; B10–13 caps
tracking advice; B14–16 optional forms and substitution; B17–20 independent numeral
choices/context; B21–25 InDesign/data/texture/accumulation scope. All25 have
recoverable revised premises in their original subsection/order; no new body
relationship occurrence or header deletion substitutes for a missing review.
F01 concerns the separate teaching example, not these edge warrants.

Analytic checks, not browser observations:

- Fonts4 controls do not create absent features. `font-kerning` distinguishes
  `auto/normal/none`, is metric and proportional-glyph scoped; missing data need
  not change output. Common ligatures normally default on; `font-variant-ligatures:none`
  does not disable required ligatures. High-level requests can be overridden by
  explicit low-level settings. Numeric form and width are independent groups.
  These comparisons support the candidate's qualified controls, not glyph results.
- Text3's nonzero-effective-spacing case says optional ligatures **should not**
  apply; explicit low-level features take precedence. Required shaping is
  separate. Cursive runs may use appropriate elongation/compression; otherwise
  joining must not be broken by added inter-letter gaps. The candidate's
  “can suppress” summary is not read as an unconditional ligature-off law.
- Direct arithmetic:5%/12% of12pt =0.6pt/1.44pt; source1.4pt is rounded.
  At20px the values are1px/2.4px. Those calculations do not make the range required.
- Equal digit advances alone cannot align decimal positions in unequal-length
  strings. A matching zero/one run is not proof about all ten digits. Adobe's
  conditional optical-use cases do not prove a particular font's performance;
  its optical guidance is Roman-glyph oriented, not an all-script guarantee.

### Actual CQ components

All9 memberships and all four exact texts are unchanged. No membership is removed
to inflate coverage. The CC table correctly limits this cohort's contribution;
its references to Slice20 do not reopen that accepted conceptual answer.

| Exact question | Occurrences / independent answer attempt and real gaps |
|---|---|
| What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it? | CQ1: OpenType[0]. Hierarchy communicates relative importance and content relationships through coordinated visual distinction. Current typography/headings and the guide's role method supply size, weight, spacing, colour and contrast; this cohort adds conditional feature/spacing choices. Cohort-only coverage is partial, but no new specimen is needed for this conceptual answer. |
| What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)? | CQ5: kerning[0],ligatures[0],alternate-figures[0],optical[0]. These members do not define the requested anatomy set. Alternate figures supplies limited baseline/cap-height/ascender/descender context, not a supported complete answer. The missing definitions remain a real local coverage gap, owned by global composition. |
| What distinguishes a spacing system from arbitrary padding values — what problem does constraint solve? | CQ11: letterspacing[0]. Contextual tracking and a percentage example do not explain a spacing system, arbitrary padding or the role of constraint. No adequate answer can be derived from this membership; retain the gap. |
| How do font weight, colour, and spacing work together with font size to create typographic hierarchy — why is size alone insufficient? | CQ12: kerning[1],letterspacing[1],optical[1]. The cohort supplies spacing/texture distinctions. Current headings' optical weight/size example and the role guide support why size alone omits other distinguishing cues; colour-pair and texture meanings stay separate. No missing conceptual component is inferred solely from absent rendered specimens; the cohort itself remains a partial contribution. |

## Preservation, scope and package reproduction

All direct checks below exited0. The raw-header comparison applied only the
seven exact issued scalar substitutions, then compared every remaining byte;
typed YAML and mapping order agreed. Complete nonassigned card/source objects
were compared against the issued predecessor, not sampled.

- Accepted index233 rows/233 unique paths exactly equals the current roster.
- Exactly nine design source paths changed;227 other complete cards and161
  source files, including `_conversion-report.txt`, are byte-identical.
- All six heading sequences and literal Source Reference sections are frozen;
  all nine changed files pass LF/terminal-newline and whitespace checks.
- Only `type.md` changed among guides, wholly inside “Check candidates and
  fallbacks”; its other sections and other five guides are preserved.
- Entry metadata changes only1.0.17→1.0.18. History addition is additive;
  existing ordering survives. Whole owned-tree inspection found one entrypoint,
  one sibling history and no duplicate current-version labels elsewhere;
  the fresh source/package version gate also passes.
- Two local guide links, including the layout fragment, resolve from the
  guide's directory. The six cards have no local Markdown links.
- Reported source commit contains exactly nine allowed paths and both required
  coauthor trailers. CC return contains only batch/report/ledger; ledger diff
  changes Evidence/Notes only. Both reported parent pins and trailers reproduce.

Native gates ran **sequentially in current SOURCE**, starting with `make help`.
After the first dependency failure, all subsequent Make invocations used
`SKILL_PYTHON=/Users/oubiwann/lab/billosys/ai-engineering/.venv/bin/python`, the
existing repository environment (resolves to the shared ai-maths environment;
PyYAML6.0.3). No dependency installation or source edit was needed.

| Order | Command / attempt | Exit and actual result |
|---|---|---|
|1|`make help`|0; target surface inspected.|
|2a|`make check-skills`, default worktree interpreter|2; PyYAML unavailable. This attempt supplies no passing gate evidence.|
|2b|`make check-skills`, explicit existing environment|0;25 skills within hard limit;19 descriptions above300-character editorial target. Design remains360.|
|3|`make check-skill-versions`, same environment|0;25 source skills,25 packages,0 errors.|
|4|`make check-package-paths`, same environment|0;25 zips,402 Markdown files,0 hard failures,606 warnings/605 unique locations,3 explicit exceptions,798 external URLs skipped.|
|5|Delete only generated design ZIP, then separate `make design`, same environment|0;fresh8-Markdown-member design package.|
|6|Read fresh ZIP and compare each Markdown member with `git show HEAD:<source path>`|0;8/8 byte-identical;129072 total uncompressed Markdown bytes.|

Current warning categories:170 repo-only/provenance,154 parser false positive,
124 bundled-reference,107 sibling-skill-reference,28 example-project,
23 source-clone-reference. CC's historical596 warnings/594 unique locations and
97 sibling references remain its historical result. Current framework/native
inputs differ outside the design-byte bridge; no claim is made that the old
counts reproduce. Warnings are not promoted to hard failures. Detailed warning
expansion was unrun; the gate reported zero hard failures.

Fresh ZIP SHA-256:
`a84faa792bddef0f920d4623b6fca604f81b328513c12b2f0693e4375a83f068`.
Its eight members are SKILL,history and six guides; each matches committed
current source. This is a new timestamp-bearing ZIP, not CC's historical hash.
Temporary gate transcripts are `/private/tmp/s21-review-versions.log` and
`/private/tmp/s21-review-paths.log`; this record preserves the durable results.

## Per-row dispositions and bubble-up

| Criterion | Independent disposition | Strength / reason |
|---|---|---|
|S21-01|**Open**|Prepared-source/domain review reproduced; F01 prevents complete teaching acceptance. Original-capture limitation is separate.|
|S21-02|**Done at bounded local scope**|Reproduced27 typed warrants,25 body dispositions,9 memberships/four component assessments, named endpoint sections and guide integration. Known CQ gaps are explicitly preserved as required.|
|S21-03|**Done**|Reconciled exact index/header/byte/frozen-section/guide-boundary checks at current candidate.|
|S21-04|**Done at local integration scope**|Reconciled current fresh native/version/package gates,8/8 committed-byte comparison, scope/trailers and bounded return. Environment failure/retry and current warnings retained.|

The connected feature/spacing method is delivered, but its assigned source
teaching is incomplete until F01 is repaired. The sole supporting artifact is
the batch record; report, ledger and issued prompts remain first-class records.
No new dependency, architecture or acceptance change is needed. CDC should
retain the current arc and issue one bounded refinement before slice close;
ordinary status/retrospective/advancement duties remain with CDC after acceptance.

No original-capture fidelity, full endpoint/corpus/live/global composition,
browser/font/InDesign/search/AT behavior, hosted rendering, release or publication
is established. Those checks were unrun here and retain their existing owners.
Accepted structural/package evidence must not be presented as those outcomes.

## Iteration01 independent acceptance — 2026-10-18

**Current verdict: all four bounded Slice21 criteria accepted. F01 is resolved.**
This section supersedes the initial candidate's current verdict while preserving
its finding, failure/retry history and original evidence above. Actual reviewer
remains `/root/s21_review`, independent of repair implementer `/root/s21_cc`;
CDC `/root` retains slice closure, retrospective and coordination duties.

Assignment: preserved `cc-prompt-iteration01.md`, issued in planning
`ad8ebdd7a38beb83bdf245c9c2d71411df2eee0d`. Reviewed actual source
`bca347f580132b0313a9bbb29d77c980a995b8f9`, parent
`d19de06d1e79e22dac0b67b5bf2e527c048a1f73`, on
`codex/project10-arc02-autonomous` in the dedicated source worktree. Reviewed
actual planning return `64c5cb3c03894c7d98aaba8d7bca56fdcebbe4d0`, parent equal
to the issuing commit. Both worktrees were clean before this append. No source
repair or commit was made by the reviewer.

### Repair meaning and current evidence

Read the issued correction, actual source delta and revised card context,
prepared comparison lines32–38, complete Iteration01 batch addition, current
report and ledger. The replacement at optical card Example1, line79, now
explains the leftward `u` movement, rounded `o` versus flat `n` proximity in
`un`/`no`, and darker `nt`/`it` gaps versus `ti`. It agrees with the source's
reported comparison and the exact issued paragraph. Butterick attribution and
the no-independent-rendering limit prevent promotion into a new observed or
universal result. Adobe's conditional comparison remains intact. F01 passes.

The batch explicitly supersedes its initial incomplete optical teaching
assessment with five current outcomes. Available prepared-source fidelity and
useful teaching now pass; technical wording, scope, cross-card consistency and
unchanged local edge/CQ coverage remain consistent. P10-11 capture fidelity
and all previously named global/actual-behavior gaps remain unresolved.

Fresh independent direct checks all exited0:

- The source commit changes exactly the one allowed file and one paragraph.
  Reversing only that paragraph restores every predecessor byte and exact blob
  `9be7f3a329045a23c6b57c8f2537e6f44f3da498`; current blob is
  `26d01b1bea0b953bc85aa78e08143eee3b7b0a3d`. Thus metadata, headings,
  citations, relationships and all other card text are untouched.
- Complete tracked-path/object comparison:7080 paths preserved,7079 other
  source objects identical, including Make, checker, package lists and helpers.
  All233 identities match the accepted index; all233 raw headers and232 other
  whole cards match `d19de06d`. All161 sources,6 guides and owner/history match.
  The earlier seven-scalar/baseline preservation result therefore remains valid.
- LF/EOF and `git diff --check` pass; revised card has0 local Markdown links.
  Planning return changes exactly batch,report,ledger. Batch/report append
  rather than erase history; ledger changes Evidence/Notes only, retaining
  criteria and open/done/done/done statuses. Both commit messages have both
  coauthor trailers recognized by Git's trailer parser.
- Existing design ZIP is unchanged at SHA-256
  `a84faa792bddef0f920d4623b6fca604f81b328513c12b2f0693e4375a83f068`.
  Fresh inspection compares all8 Markdown members against both `d19de06d` and
  `bca347f5` committed source;8/8 match.

Native checks were **retained, not rerun**. The exact source/input comparison
establishes that the unbundled paragraph cannot affect their checked properties;
all package/checker inputs and criteria are identical and no new finding
undermines the methods. The initial independent record identifies actor,
revision, method, results and accessible evidence. The issued iteration
explicitly permits retention, and no fresh native gate applies to this delta.
Retain the initial25-skill/package version result,606 warnings/605 locations,
zero hard failures and8/8 package result, with its default-interpreter failure
and successful retry still visible. This is not a fresh build or behavior claim.

### Current row walk and handoff

| Criterion | Current independent disposition | Evidence applicability |
|---|---|---|
| S21-01 | **Done at available-evidence scope** | F01 repair reproduced against prepared source; unaffected five-dimension results retained after exact delta review. |
| S21-02 | **Done at bounded local scope** |27 typed/25 body/9 CQ results retained; all relevant representations unchanged and repaired illustration agrees with the same texture/spacing premise. |
| S21-03 | **Done** | Fresh exact reversal, entire object/input comparison,233 roster/raw headers and retained original-baseline bridge reconcile preservation. |
| S21-04 | **Done at local integration scope** | Retained independent native evidence plus fresh unchanged-ZIP8/8 inspection; current scopes, trailers and bounded return reproduced. |

All four opening rows are accounted for; no new finding remains in this slice.
The repair completes its assigned concrete teaching without a new dependency,
scope change or extra artifact. CDC may close the slice with required
retrospective/status/bubble-up updates. Original editions/captures remain
unavailable; this acceptance does not close dependent fidelity, full corpus/
live/global composition, browser/font/InDesign/search/AT/hosted behavior,
arc/project acceptance, release or publication gates.
