# CC Iteration02 — finish the remaining Slice16 rule and evidence corrections

Execute this refinement and return evidence to CDC Sofie through the Operator.
Project10 / Arc02 / Slice16; Two-Contributor Workflow; Expedited Mode. No push,
self-acceptance, next-slice opening, acquisition or new inquiry.

SOURCE=/Users/oubiwann/lab/billosys/ai-engineering, main pin
`19c7a08a459d19aa0a51e76cd7f6156fe18111b3`.
PLANNING=SOURCE/.worktrees/planning, predecessor
`40c801963d2910d67503fde2f7ed5d3396097bc1`; issue is the commit adding this file.
S=project10-design-foundations/arc02-theory-and-evidence/slice16-css-colour-mechanics.
Current assignment: S/cc-prompt-iteration02.md. Preceding
S/cc-prompt-iteration01.md and initial prompt remain preserved. Confirm
[assignment history](slice-plan.md#assignment-history) and both worktrees; do not
reset/rebase or overwrite drift/unrelated work, including Project08 and knowledge/lfe/.

## Remaining work and concrete recipe

S16-03 is independently done. S16-01/02/04 remain open for
[CDC F04–F06](cdc-verification.md#iteration01-independent-review). The guide,
preservation and native integration pass at19c7a08a; retain those results when
their inputs remain applicable. Do not redo the earlier whole-card correction,
53-edge inventory or arithmetic investigation.

1. **F04, two current-syntax distinctions.** In css-rgba Key Properties3 replace
   the numeric-only legacy alpha restriction with number-or-percentage in either
   syntax. A suitable shape is: “Both legacy and modern forms accept number or
   percentage alpha; `rgba(255, 0, 0, 50%)` and `rgba(255, 0, 0, 0.5)` have the
   same alpha.” Keep alias/optional/clamping teaching. Make the Common Errors
   heading target assuming a0–255 alpha scale; expecting clamped255 to render
   opaque is not itself wrong. In hsl-css-syntax Recognition2 and affected
   explanatory repeats, distinguish modern number/percentage S/L from legacy
   percentage-only S/L. Numbers use a0–100 reference scale, not0–1.
   `hsl(180 100 50 / 50%)` and `hsl(180 100% 50% / 50%)` agree; legacy
   `hsl(180, 100, 50)` is not valid. Preserve working historical excerpts and
   the modern angle example. No browser-support claim follows from the draft.
2. **F05, review scope inside existing Verification Notes.** Inspect the notes
   in all twelve cards. Clearly separate unchanged extraction-confidence metadata
   and retained predecessor remarks from current technical support/results.
   Add a short scope sentence or explicitly label the affected remarks; do not
   invent a new extraction run, confidence score, independent verification or
   original-source provenance. For example, identify retained remarks as assertions
   present in the predecessor card at19c7a08a, then state that this correction
   uses prepared text/linked current rules and does not assess original-capture
   fidelity or browser behavior. Do not claim every retained remark was written
   by the original extractor if that provenance is unknown. Resolve the unqualified
   “None” uncertainty notes (additive/subtractive/bit-depth), RGB's stale
   integer-only classic-syntax note, HSL's “verified across both sources”, and
   the subject of blend's Medium body rationale versus frozen High metadata.
   Current technical links/qualified support must remain usable and distinct.
   An already accurate note needs no cosmetic rewrite. Read each resulting
   complete card for contradictions introduced or left by these exact changes.
3. **F06, small corrections in the existing batch.** Keep all exact field/index
   identities, endpoints and membership. Distinguish table list-locator arrows
   from semantic orientation: A listing prerequisite B means B→A; extends A→B;
   related/contrast symmetric. Rename the locator column or explain its role
   explicitly and supply one shared field rule covering its explicit rows; no
   second table or edge files. Correct RGB answers_questions[1]'s copied mixing
   answer: locate RGB's actual partial range/precision/storage contribution and
   name the bit-depth/hex passages supplying counts versus gamut. Preserve the
   existing shared-answer synthesis, qualifying completeness per occurrence.
   Update only dependent five-outcome/support/proposal cells and delta receipts.
4. Return an accurate four-row report and the three existing evidence files.
   Keep prior observations identifiable by pin/short supersession; append the
   new delta, not another copied corpus or receipt-only chain. Retained evidence
   stays at its original revision/date; report what you actually reran.

Wording of these body qualifications is local discretion within the specified
meaning. All substantive decisions above are binding within the already approved
scope. Do not use this assignment to restyle cards or begin new historical work.

## Required reading and intake

Follow current SOURCE AGENTS/current collaboration-framework and project-management
routes. Before dependent edits, read the following complete extents, recover
truncation, and record a concise actual coverage/readback in the existing batch:

- Project plan: Release target, Scope and definition of done including full-corpus
  contract, Evidence and workload economy, Operator deferral and Workflow and
  acceptance. Then Arc02 plan: Accepted inputs and preservation, Complete coverage
  and source re-entry, Workflow and current assignment. Historical chronicles are
  reference-only. These retain1.1.0 target and full233/eight-file obligations.
- Current slice plan/ledger and this prompt in full; CDC review's complete
  Iteration01 independent review section; previous prompt's Corrected oracle and
  retained result. Earlier recipes are reference-only where this narrower exact
  assignment carries the relevant constraint. E00 stays resolved.
- Current concept-cards and visual-design entrypoints; concept-cards guide05
  Record Extraction Confidence Separately, Record Evidence Gaps Without Upgrading
  Them and Keep Rich Prose Attached To Its Warrant; guide06 Identify Endpoints
  And Meaning and Assess Coverage And Answerability. Engineering-methods guide07
  Required reading and CC intake; work-verification guide05 Evidence During
  Correction Review. Apply these to the actual subjects, not just a read receipt.
- All twelve complete primary cards at the paths below. Batch: complete Per-card
  evidence outcomes, Iteration01 occurrence-level reconciliation and Final
  Iteration01 return and preservation checks; current closing report. No need
  to replay historical extraction/metadata/Unicode evidence. Prepared article's
  RGB Values/HSL Values and necessary antecedents are required for the narrowed
  source-attribution distinctions; the161 inputs remain read-only.
- Primary CSS Color4 CRD2026-10-09 §§4.1–4.3,5.1,7 grammar/reference ranges:
  https://www.w3.org/TR/2026/CRD-css-color-4-20261009/ . Read full selected rules,
  not a title/snippet; distinguish modern and legacy grammar. Do not claim runtime
  support. Other unchanged spec/equation reads are prior evidence, not fresh reads.
- Data: parse all233 accepted Arc01/Slice01 index rows at9cc20338 and compare exact
  paths to current source, then select these twelve exact paths. Parse their
  existing header values/order/types and10 CQ/53 relationship occurrences; check
  only the affected direction/answer joins substantively against the already
  complete cohort. No new dataset, schema, validator or broad corruption suite.

## Exact write and commit scope

Only these SOURCE card bodies may change. In the first two named grammar files,
the F04 statement family and F05 Verification Notes are authorized; in all other
cards, only needed F05 Verification Notes qualifications are authorized:

```text
knowledge/design/concept-cards/posts/css-rgba.md
knowledge/design/concept-cards/posts/hsl-css-syntax.md
knowledge/design/concept-cards/posts/additive-colour-mixing.md
knowledge/design/concept-cards/posts/subtractive-colour-mixing.md
knowledge/design/concept-cards/posts/colour-bit-depth.md
knowledge/design/concept-cards/posts/rgb-colour-model.md
knowledge/design/concept-cards/posts/hex-colour-notation.md
knowledge/design/concept-cards/posts/css-colour-custom-properties.md
knowledge/design/concept-cards/posts/gradient-colour-interpolation.md
knowledge/design/concept-cards/posts/mix-blend-mode.md
knowledge/design/concept-cards/posts/fecolormatrix.md
knowledge/design/concept-cards/posts/colour-contrast.md
```

These are a maximum allowlist, not a requirement to edit an already accurate note.
Freeze every header byte/value/type/order, literal Source Reference and existing
section heading at19c7a08a. Other221 cards, all161 sources, every guide (including
the accepted colour guide), HSL endpoint, owning SKILL/history, helpers, Makefile
and package lists remain unchanged. Keep1.0.13 for this unfinished grouped repair.
No new fields, IDs, files, source-input capture or scope reduction. If drift or
an unlisted required correction appears, report the exact dependency and continue
independent authorized work; do not silently broaden scope.

Only these PLANNING return files may change:

```text
project10-design-foundations/arc02-theory-and-evidence/slice16-css-colour-mechanics/artifacts/batch-record.md
project10-design-foundations/arc02-theory-and-evidence/slice16-css-colour-mechanics/ledger.md
project10-design-foundations/arc02-theory-and-evidence/slice16-css-colour-mechanics/closing-report.md
```

Ledger Evidence/Notes only: criteria/statuses remain open/open/done/open.
Plans, prompts, CDC review and unrelated records are protected inputs. One
supporting artifact remains the batch; report and ledger are first-class records.

## Focused checks, retained evidence and return

Inspect the two grammar pairs above and their contrary legacy-HSL example
against the actual grammar. Also retain the invalid mixed-unit legacy RGB
contrast: `rgb(50%, 0, 0)` is invalid while `rgba(255, 0, 0, 50%)` is valid;
the all-number/all-percentage restriction applies to RGB components, not alpha.
Check references/annotations directly; a text pattern's presence alone is not
semantic proof. Temporary arithmetic/inspection is sufficient, no browser or
general parser implementation required.

Compare the actual delta against19c7a08a: authorized statements/sections only,
233 exact identities, frozen raw and typed/ordered headers, Source References,
all other cards/sources/guides/packaging inputs. Check LF/EOF/local links,
`git diff --check`, exact commit paths and both trailers. Reconcile53 field/index
occurrences and10 CQ entries without changing metadata; inspect the changed
direction/answer meanings rather than requiring a new negative-control suite.

CDC's fresh sequential native gates and8/8 ZIP comparison at19c7a08a are accepted
in cdc-verification.md. These cards are not bundled. This narrower assignment
permits retaining those results, plus prior unchanged arithmetic, after checking
that their source/build/checker/dependency inputs are byte-identical and no
finding invalidates them. Do not label retention as a fresh run. No mandatory
Make rebuild for this unbundled-card-only delta; if affected inputs differ,
identify the impact before dependent acceptance and rerun relevant native gates
sequentially from `make help` as needed. Never run shared packaging gates concurrently.

Commit only actual authorized changes in each worktree separately with explicit
named paths (`git commit --only`); preserve others' staging. Each commit requires:

```text
Co-authored-by: Codex <noreply@openai.com>

Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Return final source/planning hashes, paths, actual fresh/retained checks,
F04–F06 dispositions, all four row proposals and limits. No receipt-only child
commit required. CDC independently accepts/closes; historical fidelity, actual
browser/AT/hosted, global233/eight-file and release/parent gates remain with their
existing owners. Nothing is pushed or published.
