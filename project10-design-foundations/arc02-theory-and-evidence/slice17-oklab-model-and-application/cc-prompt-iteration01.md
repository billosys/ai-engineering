# CC implementation — Slice17 Iteration01

Execute this refinement and return to **CDC Sofie through the Operator**.
Two contributors, Expedited Mode. This is the current assignment, not another
request to prepare a plan. No CRC role, successor slice, push or publication.

## Identity, input pins and required intake

Project10 / Arc02 / Slice17. This prompt:
`arc02-theory-and-evidence/slice17-oklab-model-and-application/cc-prompt-iteration01.md`.
Prior assignment [cc-prompt.md](cc-prompt.md) remains preserved.
Read the active [project plan](../../project-plan.md)1.73 and project ledger,
then [arc plan](../arc-plan.md)1.52 and arc ledger, then complete
[slice plan](slice-plan.md), [ledger](ledger.md), [CDC review](cdc-verification.md),
[batch record](artifacts/batch-record.md), [closing report](closing-report.md)
and this prompt before dependent edits. Read initial prompt's preservation and
source/technical contract; this prompt narrows its write set explicitly below.

- SOURCE/main: `485585efe99c2d2cf3b956356989664bc6ffa262`.
- Planning predecessor/CC return: `61b3c427433f324a0933f7bcdccc507e6a03accb`.
- Initial body-relationship baseline: `4acfec6d8fa17e1ecb869bda28a6e71d17ef771e`.
- The issuing commit is the one adding this prompt. Record its actual identity.

Use current SOURCE `AGENTS.md`, collaboration-framework and its PM wayfinder /
iteration routes, engineering-methods guide07 intake/retained evidence,
work-verification ledger discipline, and relevant visual-design guidance.
Load Concept Cards entrypoint and guides05-evidence-lifecycle/06-graph-cq.
Read all thirteen current cards completely and the actual prepared/spec passages
used below; record actual intake coverage and limits, not invented receipt counts.
Reuse earlier reading only with an explicit input/scope applicability check.

## Binding scope and result

Make the cohort usable and internally consistent; finish available-evidence
review alongside source repairs. No new inquiry, schema, helper, corpus copy,
standalone analysis packet, validator or receipt-only commit chain.

Only bodies of these thirteen SOURCE paths may change, all under
`knowledge/design/concept-cards/posts/`:

- `chroma-perceptual.md`
- `colour-interpolation-perceptual.md`
- `colour-space-comparison.md`
- `colour-space.md`
- `d65-whitepoint.md`
- `gamut-srgb.md`
- `lightness-perceptual.md`
- `lms-cone-responses.md`
- `matrix-transformation-colour.md`
- `oklab-conversion.md`
- `oklab.md`
- `perceptual-uniformity.md`
- `xyz-colour-space.md`

Freeze full metadata prefixes, literal Source References and existing heading
sequences at485585ef, including the eleven already accepted scalar corrections.
Freeze dependent chroma-vs-saturation, guides, SKILL/history1.0.14, other220 cards,
all161 sources, helpers and packaging inputs. No metadata change or new version.
S17-03 is CDC-done; S17-01/02/04 remain open. Retain their passing components.

## F01 — reconcile the contradictory sections

Apply the concrete card/section corrections in [F01](cdc-verification.md#f01--contradictory-or-inaccurate-teaching-remains).
Binding interpretations, carried through prerequisites, construction, examples,
relationships, errors, confusions and verification notes:

1. Approximate uniformity informs interpretation; it is not a prerequisite for
   valid chroma coordinates or interpolation. Scope Oklab/sRGB routing to the
   chosen example. XYZ is an optional explicit intermediate in this route.
2. Model L, XYZ Y and WCAG relative luminance are distinct. Scope comparison
   claims to the source's lightness data/metric; greyscale/palette appearance
   remains approximate and contrast uses actual rendered pairs.
3. D65 is a reference convention/chromaticity, not any source near6500K.
   The printed XYZ white is rounded. Adapt differing input whites to the expected
   reference rather than telling readers to rederive Oklab matrices.
4. XYZ M1 accepts XYZ; combined A accepts **linear** sRGB and never decodes
   encoded input. Include the real cube-root stage. Compatible linear stages
   compose conceptually; independent rounded coefficient families need not be
   literally identical. Use one published family consistently in each example.
5. A zero-offset linear map is also affine. Do not add an unstated translation;
   inversion requires nonsingularity. Matrix order is M1(3×3) × XYZ column(3×1).
6. Preserve actual source naming without inventing the author's motivation.
   In comparison prose, distinguish generated CAM16 lightness/chroma data from
   the separate perceived-hue data used to derive IPT (prepared198–232).

This is a whole-card reconciliation, not just a replacement of each Core section.
Do not propagate the old errors into newly restored examples.

## F02 — restore useful positive definitions and conversion teaching

Prepared `knowledge/design/sources/md/posts/a-perceptual-colour-space.md`
remains504 lines, SHA256
`ffe5494da6f0d040fb341d8e1f03d3e396600f6787088b6d57e32613798375f4`.
Use37–51 for axes/polar,73–110 for XYZ matrices,114–161 for combined RGB code,
198–249 for dataset/metric attribution. Inspect needed primary support linked
in the review; current web support is not immutable original-source fidelity.

Recommended concrete presentation; wording and compact layout are local discretion:

- Restore L as fitted lightness, a green–red and b blue–yellow axes in oklab.
- Put the article's combined forward A/B coefficient rows in conversion, with
  decode → A × linearRGB → signed real cube root → B × rooted values.
  A rows are (.4122214708,.5363325363,.0514459929),
  (.2119034982,.6806995451,.1073969566),
  (.0883024619,.2817188376,.6299787005).
  B rows are (.2104542553,.7936177850,-.0040720468),
  (1.9779984951,-2.4285922050,.4505937099),
  (.0259040371,.7827717662,-.8086757660).
  Reverse using the article's inverse coefficient rows, cube each intermediate,
  then inverse linear transform; encode only for encoded-sRGB output.
  Label published rounded inverse coefficients; do not promise exact inversion.
- Restore XYZ M1/M2 numeric teaching in the matrix card, or link precisely to
  locally supplied labelled rows. Do not label combined A as XYZ M1.
  Keep at least one complete worked forward/reverse example. No compiler,
  new conversion library or perception benchmark is needed for mathematical prose.
- Correct “full C++ listing provided verbatim” if showing equations/excerpts.
  Restore XYZ Y's luminance role under observer/normalization conventions;
  CSS Color4 §10.9 uses relative Y=1 at diffuse white. Keep its difference from L.
- The article has no neural-network comparison. Remove that attribution or
  explicitly identify optional card-author structural analogy with its limits.

## F03 — finish the semantic work in the existing batch record

Use the same single artifact. Compact groups are welcome when all occurrence
members and their evidence/contribution joins are explicit. No new schema.

**Edges:** Assess all79 current header occurrences by card + field/index, actual
endpoint revision/passage, relation sentence, direction, supporting premise,
reasoning and CC outcome/limit. `A.prerequisites=B` means B→A supports
understanding A; `A.extends=B` means A→B elaborates B; related/contrast are
symmetric with a specific basis. “Target resolves” does not complete review.

Worked method: chroma-perceptual.prerequisites[0] is oklab→chroma-perceptual.
Article37–51 and the repaired oklab axes define a/b; chroma's C=hypot(a,b)
consumes them. This supports an editorial learning route to its coordinate
operands, not perfect uniformity or strict necessity in every colour model.
Use the same endpoint-premise reasoning for actual other members. The contrast
with colour-space-comparison is a model/comparison reading route; give its
specific comparative basis rather than claiming the constructs are opposites.
Do not invent or edit metadata to manufacture support; expose any residual gap.

**Body relationships:** Trace all102 baseline statements to final retained,
rephrased, merged or removed-with-reason dispositions, then assess every final
and introduced relationship. Current485585ef has86; final count is derived, not
forced. Use card/heading/label/ordinal to make joins recoverable. Preserve useful
teaching when merging; deletion alone is not reconciliation.

**Questions:** Keep all20 header occurrences/five exact texts. Locate each
card's actual answer component/premise; distinguish full, partial and missing
contributions. Show a bounded combined answer for each text. Palette teaching
must connect chosen L targets/steps across hues with chroma/gamut/render checks
and actual-pair contrast, without guaranteeing equal appearance. D65 alone is
background, not a complete uniformity answer. Read whole bodies for further
question statements; if none, name that read scope rather than inventing CQs.

**Outcomes:** Finish thirteen actual five-dimension rows: prepared-source
agreement/fidelity limit, technical correctness, scope, internal consistency,
edge/CQ support. Name the claim/passage evidence and final defects or limits;
retain source-fidelity blocks where originals/captures are missing. Replace
blanket unfinished/CRC labels with actual CC assessments; CDC accepts later.
Preserve prior observations by pin and short supersession notes, not duplicate
reports. Complete available work before proposing done; a real blocker must
identify exact affected members/input/owner, not the need for further review.

## Checks, retained evidence and return

Freshly check the repaired recipe against literal source coefficients. For
encoded grey.5, decode to.21404114048223255 before A; expected L≈.5981807266.
Wrongly treating.5 as linear gives L≈.7937005208; linear grey.125 gives
L≈.4999999967. Use a declared tolerance (e.g.1e-6 for these printed L values).
Show forward stages and inverse round trip under an appropriate declared
coefficient-precision tolerance. Retain applicable signed-root, hue-wrap,
nonlinearity and out-of-gamut witnesses after checking their exact inputs/claims;
rerun only affected/new arithmetic. No precision-only expansion or browser claim.

Re-read complete final cards for contradictions and useful teaching. Compare
all233 identities,13 changed-body scopes, frozen metadata/citations/headings,
other220 cards and161 sources; check local links, LF/EOF and diff whitespace.
CDC's fresh native/version/package gates and8/8 ZIP proof are in the review.
These thirteen cards are unbundled: retain that evidence after byte-checking
all its inputs; no automatic rebuild of unchanged packages. If inputs drift,
stop affected work for reconciliation rather than silently expanding scope.

Only three planning outputs may change: `artifacts/batch-record.md`,
`ledger.md` Evidence/Notes cells, and first-class `closing-report.md`.
Do not change criteria/statuses, prompts, plans, CDC review or other projects.
Report this iteration/issue, exact source/planning commits, F01–F03 outcomes,
all four row dispositions, actual checks/failures/retention and remaining gates.
No independent acceptance, full-corpus fidelity, hosted or release inference.

Commit separately on SOURCE/main and planning with exact named changed paths
(use `git commit --only` to protect concurrent work); include both separate
trailers in each commit: Codex <noreply@openai.com> and Billo AI
<ai-engineering@billo.systems>. Preserve unrelated/untracked work and do not
push. Return to Operator for CDC review; no slice close or next slice by CC.
