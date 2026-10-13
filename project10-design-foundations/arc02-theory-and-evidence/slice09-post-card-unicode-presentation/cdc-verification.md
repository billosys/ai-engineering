# Arc02 Slice09 independent CDC verification

## Initial return review and prepared evidence correction — 2026-10-13

**Current verdict: S09-01/02/03 done; S09-04 open solely for Operator acceptance
of the five-field CDC-authored evidence repair below. Slice09 remains open.**
Separate CDC Sofie reviewed CC source `589d7c21bd6c9a415b921b80479822561861fa79`
(parent `c4cc74279ac845003b0c80f55907981241c58a99`) and planning
`e1e59efe5519a5c615e606d2c04b69d31c287097` (parent issue
`58d7502116ce00c26dbeb03796dd24cca01de872`) against the preserved [initial prompt](cc-prompt.md).
Two contributors, Expedited Mode. No source repair or publication by CDC.

## Independently reproduced checks

- Exact48 source and seven CC planning paths, parents, both required trailers
  and committed whitespace checks reproduce. Issued plans/prompts, parent
  ledgers, frozen inputs and CDC records are byte-preserved by CC. No source
  file beyond the46 posts and owning entrypoint/history changes.
- All233 pinned inputs resolve; every final card equals the committed original
  prefix plus precisely the prompt's literal body-token replacements. All46
  headers and all187 other cards are byte-equal; no other body number, assertion,
  newline, fence, reference or actual Unicode is changed. Complete46-row
  correction table hashes/sizes/header offsets/closing lines/counts reproduce.
  Exactly1062 occurrences/23 token types and−3337 body bytes; UTF-8, line counts
  and second-pass body idempotence pass. Actual candidate is the positive witness;
  an undecoded Matrix escape, changed header and unrelated changed body number
  each fail the same expected-byte oracle.
- Entrypoint changes only the version scalar1.0.5→1.0.6; sibling history appends
  the matching entry and preserves previous bytes. Fresh `make help`,
  `make check-skills check-skill-versions check-package-paths design` pass on
  the current integrated source/Makefile.24 sources/24 packages, zero version
  errors and hard path failures;18 editorial notices,596 warnings at594 locations,
  three exceptions and681 skipped external URLs remain. The package gates rebuild
  packages; final design target reports up to date. All eight actual packaged
  Markdown members equal committed source. CDC ZIP SHA-256
  `c10fe0875f98bbc51bd23b6961c46734b4b7c283869af791a73477d1efa5fc93`;
  CC's differing archive timestamp/hash does not change member identity.
- All233 Arc06 non-hosted bridge objects remain equal to the pinned input.
  The187 unaffected records remain line-byte exact. Each affected hosted record
  retains its original complete observation, response identity/URL, structural
  checks and metadata pass, while marking the published body fail;46 counts,
  source-candidate pointers and ownership join exact source data. No corrected
  local body is called hosted-pass. Arc06 stays five done/one open.

CDC's temporary checker initially demanded equal separately cropped display
snippets, then exposed the actual five partially decoded expected snippets below.
Its idempotence check also initially decoded the entire file, including protected
YAML string escapes; corrected it to the specified body boundary. Neither helper
failure altered repository source. The corrected full233 checker and three
negative controls pass; the five snippet findings remain disclosed rather than
being reclassified as a harness failure.

## F01 and the prepared CDC repair

Five `hosted.correction_review.expected_vs_visible.expected` values decoded only
the first token in their visible snippet. The second literal escape made the
claimed expected display absent from the correct source. Source transformation,
46-row byte bridge, hosted failure classifications and retained metadata evidence
are correct; only these five expected-display strings need repair.

| Record | CC expected text at e1e59efe | Prepared correct expected text |
|---|---|---|
| `colour-interpolation-perceptual.md` | `colour(t) = (1-t) × colour_A + t \u00d7 colour_B, f…` | `colour(t) = (1-t) × colour_A + t × colour_B, f…` |
| `golden-ratio.md` | `The golden ratio (φ \u2248 1.618) is a proportion f…` | `The golden ratio (φ ≈ 1.618) is a proportion f…` |
| `hex-colour-notation.md` | `…rs encodes one colour channel (0–255 as 00\u2013FF).` | `…rs encodes one colour channel (0–255 as 00–FF).` |
| `hsl.md` | `…bes colours by three parameters — Hue (0\u2013360 degrees), Satur…` | `…bes colours by three parameters — Hue (0–360 degrees), Satur…` |
| `munsell-colour-system.md` | `…by three independent dimensions — Hue, Chroma, and Value \u2014 e…` | `…by three independent dimensions — Hue, Chroma, and Value — e…` |

CDC prepared exactly these five string replacements in the existing Arc06
`artifacts/batch-results.jsonl`. Each complete prior expected string, input
revision, observer/date and reason is retained under
`hosted.correction_review.expected_snippet_correction`; every other field and228
other record lines remain exact. The new expected strings decode all whitelisted
tokens in their unchanged visible spans and occur literally in the independently
accepted source bodies. The recipe has no remaining ambiguity and no source edit.
This is **CDC doer-attested repair**, not independent acceptance of CDC's own edit.
The Operator can accept it; no extra CC implementation cycle is necessary.

## Four-row walk

| ID | CDC disposition | Basis / remaining gate |
|---|---|---|
| S09-01 | done | Fresh complete233 input/scope reconciliation and exact48/seven path integrity. |
| S09-02 | done | Complete expected bytes/metadata preservation,46 token/body table and three credible negatives. |
| S09-03 | done | Current owning version/history, fresh Make gates and eight actual package-member comparisons. |
| S09-04 | open | All correction lineage/owners and hosted failure history independently checked; five authored expected-snippet fixes await Operator acceptance. |

CDC restored issued criterion wording after CC's spacing-only editorial changes
while updating reviewer statuses; no criterion, denominator or scope changed.
The sole new supporting artifact is CC's `artifacts/batch-record.md`; revised
Arc06 artifacts stay in their original slice. Close-set report/prompt/ledger
remain first-class documents, with all issued prompts preserved.

## Concrete Operator publication handoff

Fresh remote read on2026-10-13 still gives main `c4cc74279ac845003b0c80f55907981241c58a99`
and planning `eac665f569d269b6a913e2f9349ef3e73656781e`. Local main
`589d7c21bd6c9a415b921b80479822561861fa79` is its direct child: exactly one reviewed
source correction,48 paths. No merge/rebase/force operation is needed at these
refs. CC owns the next normal main/planning push after Operator approval; CDC
does not duplicate it. Recheck drift and preserve unrelated work before pushing.

The concrete approval comprises (1) this five-string evidence repair and
(2) normal publication of the reviewed source commit and planning return/review.
[The preserved source prompt](cc-prompt.md#correct-the-existing-hosted-evidence-in-this-same-return)
reserves new publication to the Operator. [Work-verification](/Users/oubiwann/lab/billosys/ai-engineering/knowledge/work-verification/SKILL.md)
states “self-review is never independent”; its independent-verification guide
requires another verifier or the Operator for reviewer-authored repairs. Thus
these two gates remain pending; publication of the previous range is not inferred
as approval of this newly reviewed correction. No release/install approval sought.

Ready [Arc06 read-only hosted follow-up](../../arc06-card-metadata-and-rendering/slice02-book-card-metadata/cc-prompt-iteration01.md)
checks all233 actual exact-revision pages after corrected source is accessible.
It does not change source or replace observation with local parsing. The earlier
`c4cc742` body-preservation results remain historical; new body hashes/locators
use the accepted Slice09 correction table. Full fidelity/semantic and Arc04
composition/release gates remain open.

## Bubble-up

Source presentation capability is delivered locally at the reviewed revision;
metadata and useful teaching are preserved. Evidence expectations have a complete,
reviewable five-string fix and named Operator gate. No hidden source gap, new
investigation or semantic acceptance. Slice09 can close immediately after that
acceptance; Arc06 rendering can resume after publication. Parent plans record this
current state rather than pretending source delivery proves hosted correctness.
