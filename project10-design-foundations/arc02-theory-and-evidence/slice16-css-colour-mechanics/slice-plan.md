---
slice: slice16-css-colour-mechanics
status: closed
depends-on: [accepted Arc01 corpus and prepared-source records, current design source]
---

# Slice16 — CSS Colour Mechanics

Revision **1.3**, opened2026-10-16 after the Operator lifted the reassessment hold.
Two contributors, Expedited Mode: CDC Sofie authors/reviews; separate CC implements
through Operator relay. [Project](../../project-plan.md), [arc](../arc-plan.md),
[ledger](ledger.md) and [initial assignment](cc-prompt.md) govern. Planning predecessor
`c64c5835fed0ac5d2377ff3dc12fe854e35438ce`; SOURCE/main baseline
`65ed7a05d602e775bfa5cec16bfb4ccf206c8c63`. The issuing commit is the commit adding
this open set. Initial CC return: source8f622e44/planninge04d8846.
CDC accepted all four criteria on2026-10-17 at source4acfec6d / CC planning0dced6bb;
see [independent closure](cdc-verification.md#iteration02-independent-review-and-slice16-closure).
No active CC assignment. The initial prompt and both iterations remain historical
issued records; their exact mutation/check constraints still delimit acceptance.

## Deliverable and exact scope

Make the twelve Drasner cards a useful, internally consistent explanation of CSS
colour mechanics: read, assess, repair, check and return them together. Complete
their five available-evidence outcomes and affected local relationship/CQ work
in this batch. Historical original-capture fidelity stays explicitly blocked.
No separate analysis-only packet or future fix handoff is the deliverable.

The following twelve files under SOURCE `knowledge/design/concept-cards/posts/`
are the complete primary cohort (1,464 lines / 68,387 bytes at the pin):

| Card basename | Required correction / retained teaching |
|---|---|
| additive-colour-mixing.md | Distinguish physical light summation under fixed primaries from encoded-sRGB arithmetic, averaging/interpolation and compositing. A display has a bounded gamut; RGB cannot produce every visible colour. Preserve the light/pigment distinction and contextual historical attribution. |
| subtractive-colour-mixing.md | Explain absorption as the simplified model, CMY versus traditional RYB, and contextual pigment outcomes. Mixing any extra pigment does not universally darken every mixture or guarantee brown/black. Keep the source example attributed, not a universal test for additive/subtractive processes. |
| colour-bit-depth.md | Separate bits per channel, bits per pixel and alpha allocation. A full n-bit encoding has 2^n bit patterns; three independent eight-bit colour channels have 2^24 combinations. RGBA8 is an example of 32-bit storage, not all 32-bit formats. Code count is not gamut, accurate reproduction, or a fixed human discrimination threshold. |
| rgb-colour-model.md | Explain encoded sRGB, modern and comma notation, numbers/percentages and fractional precision. Correct the integer-only error; 0.5 is a small channel value, not 50 percent. CSS notation does not mandate an eight-bit framebuffer. |
| hex-colour-notation.md | Cover 3/4/6/8 digits and alpha ordering, shorthand constraints and exact byte conversion. Keep base16 teaching; qualify unsupported popularity/universal-interchange and manipulation prohibitions. Numeric rgb() may express precision unavailable in an eight-bit hex channel. |
| css-rgba.md | rgb()/rgba() are aliases in current CSS; alpha accepts numbers/percentages, including integer1. Explain clamping and colour alpha versus group opacity; no fixed eight-bit storage requirement. Preserve working legacy examples alongside modern syntax. |
| hsl-css-syntax.md | Distinguish CSS HSL coordinates from perceptual uniformity and attributed Munsell history. Include modern syntax, hue angles/wrapping, hsl()/hsla() aliases; do not teach bare-number hue or commas as the only valid form. Old Sass/GreenSock examples remain explicitly historical excerpts, not current dependency recipes. |
| css-colour-custom-properties.md | Retain a usable scoped-theme example, optional semantic aliases and currentColor. Correct mandatory naming/tier policy and the dependency-injection equivalence. Explain where substitution resolves: changing a primitive does not re-evaluate an inherited alias already computed on an ancestor. Preserve existing project tokens. |
| gradient-colour-interpolation.md | Distinguish CSS gradient geometry from its interpolation space and SVG rules. Name the space in numerical examples, use premultiplied alpha, distinguish interpolation from physical addition, and avoid claiming a universal sRGB default. CSS Images owns gradient syntax; CSS Color supplies interpolation algorithms. Do not promise an Oklab rainbow or perceptual perfection. |
| mix-blend-mode.md | Separate backdrop, blended result and alpha compositing. Restrict per-channel formulas to separable modes; contrast non-separable hue/saturation/color/luminosity. Correct color-burn clipping/branches, the supposed CSS 'linear' mode, fixed exhaustive mode-count claims and overflow/isolation confusion. Preserve multiply/screen examples. |
| fecolormatrix.md | Explain twenty coefficients as four output rows by five input columns for [R,G,B,A,1], or the augmented five-by-five form. Upstream also calls the value list '5x4'; state rows/columns explicitly rather than treating that label alone as an error. Bias makes the RGBA mapping affine. Explain non-premultiplied operation, filter colour space and clipping; preserve the source matrix and expose its alpha term. SVG hueRotate is a matrix operation, not guaranteed HSL hue-wheel rotation; SVG filter defaults differ from CSS filter functions. A matrix alone does not validate colour-vision simulation. |
| colour-contrast.md | Add primary WCAG support, correct text-size/level/exception scope and non-text/use-of-colour distinctions. Remove the false yellow/blue counterexample; distinguish HSL lightness from relative luminance. Give a reproducible sRGB pair procedure without promising whole-page accessibility. |

Additional authorized source paths, with narrow responsibilities:

- `knowledge/design/concept-cards/posts/hsl.md`: dependent repair only of the
  Drasner/Munsell lineage assertion in Core Definition and Relationships/Related;
  identify it as Drasner's comparison, not proof of mathematical equivalence or
  inspected history. Read the whole endpoint, but claim no complete Ottosson-card
  acceptance. All other body material and its complete metadata remain unchanged.
- `knowledge/design/guides/colour.md`: add a short usable pair-check procedure
  under Choose candidate values, using the contrast witnesses below and primary
  WCAG links. Retain supplied-identity, role/state and actual-rendering obligations.
- `knowledge/design/guides/foundations-of-design.md`: repair only the OKLCH
  paragraph in Colour Theory, the Temperament → perceptual-uniformity paragraph
  in Music Theory → Visual Design, and the opening/closing notation assertions
  in Colour Notation. Replace exact equal-appearance/identical-mathematics and
  universal hex assertions with qualified methods/analogy. Preserve adjacent
  Brown arithmetic, nonlinear conversion stages and optional token policy.
- `knowledge/design/SKILL.md`: only metadata.version **1.0.12 → 1.0.13**.
- `knowledge/design/version-history.md`: matching correction entry; retain history.

Exactly17 source paths are authorized; use the explicit enumeration in the prompt.
For the twelve primary headers, changes may affect only existing
`rosetta_stone[0].note` on additive, bit-depth, custom-properties, gradient, blend
and filter cards; additionally custom-properties `rating` becomes `structural`
and filter `concept` becomes `Affine transformation in homogeneous coordinates`.
Qualify those mapping notes consistently with the table; all other header bytes,
values/types/order, nested aliases, confidence, source identity, questions and
relationship lists stay unchanged. No fields/IDs/schema additions. Keep every
existing body section and the complete literal Source Reference section in all
thirteen cards. Add current technical links/explanations in Verification Notes
or other body prose, without overwriting the historical source citation.

All other220 cards, all161 source-tree files, other guides, helpers and packaging
lists are protected. Do not acquire/reconvert sources, redesign schema or create
a new verifier product. The accepted233 path identities remain; no split/merge.

## Implementation and proof

Read the complete cohort and the complete445-line prepared
`knowledge/design/sources/md/posts/working-with-colours.md`
(SHA256 `f4cf46139cd45b5e8d78865666520520493dbafe4fe39a89b9c0e32227c0e4af`).
Compare each substantive claim to its actual prepared passage; preserve quotations
accurately or identify an explicit paraphrase/correction. Prepared text itself
contains historical simplifications/typos. Separate its assertions from current
technical teaching and author-added mathematics. Current specs supplement technical
correctness; they do not establish fidelity of a missing historical capture.

Use the primary sections in the prompt. Resolve supported defects in the same
body; keep examples/explanation useful. Local wording is CC discretion within
these binding technical boundaries. If a new defect needs an unlisted file or
consequential decision, finish independent allowed repairs and return the exact
extension needed; do not silently broaden mutation scope or start a new inquiry.

Focused expected witnesses (temporary calculations/inspection suffice; do not
build a reusable validator or a broad mutation suite):

1. RGB precision: 50 percent of255 is127.5, while numeric0.5 is not50 percent.
   `rgb(0.5, 0.5, 0.5)` is not intrinsically invalid. Distinguish valid modern
   `rgb(50% 0 0 / 50%)` from invalid mixed-unit comma `rgb(50%, 0, 0)`.
   `#0f08` expands to `#00ff0088`, whose alpha is136/255, not exactly0.5.
2. Count: 2^8=256; 256^3=16,777,216 colour triples. Adding eight alpha bits
   changes RGBA combinations, not the RGB gamut or a universal vision threshold.
3. Gradient: explicitly in sRGB, opaque red/blue midpoint is(0.5,0,0.5,1).
   Transparent white(1,1,1,0) → opaque black(0,0,0,1) at t=0.5 gives
   non-premultiplied output(0,0,0,0.5), not independent-grey(0.5,0.5,0.5,0.5).
   Keep gradient colour space/default claims scoped to the named spec/environment.
4. Matrix: the retained source matrix maps opaque black(0,0,0,1) to
   (0,1,0,1); the alpha term alone forces green1. Identity maps an arbitrary
   RGBA input unchanged; a nonzero bias is affine. These distinguish a mistaken
   ordinary4-vector product and a false generally image-dependent green effect.
5. Separable blend example with opaque backdrop: Cb=0.2,Cs=0.4 → multiply0.08,
   screen0.52. Color-burn uses its clipped branches, including Cb=1,Cs=0 →1
   and Cb=0.2,Cs=0 →0. Do not describe these blend functions as the entire
   alpha-compositing algorithm or as formulas for non-separable modes.
6. Contrast: black/white21:1; #777/#fff≈4.4780894536:1 fails normal-text AA
   (no rounding up); #ffff00/#0000ff≈8.0016366612:1 despite equal HSL L.
   Use WCAG's sRGB decoding/weights and contrast formula. State text AA/AAA,
   large-scale definition/exceptions and non-text requirements separately.
7. Scoped substitution: root `--ink:black; --alias:var(--ink)`; child
   `--ink:red` with consumers `color:var(--ink)`, `color:var(--alias)` and
   `color:blue` means red, black, blue respectively. Redeclaring the alias on
   the child makes its consumer red. Label normative reasoning separately from
   any actual browser observation; do not fabricate runtime evidence.

Re-read revised complete cards. Record per-card five outcomes, detailed evidence
for changed/unsupported/blocked claims and sound-claim span groups with explicit
coverage. For all53 header relation occurrences plus every body relationship,
state endpoints/revisions, direction/meaning, support and outcome. All header
endpoints are within the primary cohort or `hsl.md`; compare the relevant endpoint
constructs directly. Preserve the lists but clarify reading-aid/analogy limits in
body explanations; do not promote these into formally verified dependencies.

Review all10 header question occurrences (five distinct texts), plus any body
questions. Retain exact question text; map required answer components, give the
supported answer and limits, and repair available missing explanation now. E.g.
the bit-depth question needs count versus gamut; theming needs scope/substitution
conditions; blending needs separability/compositing. No automatic deferral of
accessible endpoints or already available evidence. Unavailable historical,
external or actual-behavior evidence has an exact remaining input/check and owner.
This is local semantic review, not whole233/global closure.

## Evidence, checks and return

One supporting artifact: `artifacts/batch-record.md`. It holds concise actual
intake/readback, the12-card five-outcome table, claim exceptions/source spans,
local edges/CQ components, before/after hashes/deltas, focused witness methods and
results, guide reconciliation and remaining owners. Use tables or compact records
inside it; no new schema or copied corpus. Closing report summarizes all four
rows and cites this evidence. Preserve original mistakes as historical observations
where a prior record is superseded; do not require a receipt-only commit chain.

Reuse the accepted233 index and current source tree for identity/preservation,
not a replay of every old header/Unicode transformation. Establish exact changed
path/field/body scope, typed YAML preservation, Source Reference equality, unchanged
other cards/sources/guides and LF/EOF/local links. Native mandatory gates from
SOURCE: `make help`, `make check-skills`, `make check-skill-versions`,
`make check-package-paths`, then separate fresh `make design`. Compare all eight
packaged Markdown members with committed source and record archive hash/counts.
Cards are not bundled: the ZIP does not validate card bodies or hosted rendering.
Record warnings and failures/recovery honestly; new nonzero gates block dependent
acceptance. No publication, push, installed-task, browser/AT or hosted acceptance
is promised here. Final changed-revision hosted work remains P10-13/Arc04; actual
behavior and complete review remain Arc02; historical fidelity remains P10-11.

**Initial return contract (historical; Iteration01 now governs):** CC could change
exactly three planning paths: `artifacts/batch-record.md`,
`ledger.md` Evidence/Notes only (criteria/statuses remain open), and
`closing-report.md`. Preserve this plan/prompt and all predecessor records.
Commit scoped source and planning work separately with both required trailers;
return final hashes, changed paths, actual checks, limits and four-row proposals.
No push. CDC independently accepts and closes; parents stay open at their scope.

## Author readiness

CDC read the updated project548lines and Arc02353lines at planningc64c5835
(including recovery of truncated output); the full twelve-card cohort, complete
hsl endpoint, complete445-line prepared source, full colour guide and the named
foundations paragraphs at source65ed7a05. The literal53-edge/10-question header
projection and twelve raw-source-index memberships were inspected. The author
applied concept-cards evidence and graph/CQ guidance to separate prepared-source
agreement, current correctness, endpoint warrant and question answer components;
visual-design's actual-pair/optional-token guidance governs guide reconciliation.
Primary CSS Color, Filter Effects, Compositing, Variables and WCAG sections were
inspected for the concrete corrections; Images4 retrieval failed at W3C and its
official editor draft was used. Current online retrieval is not immutable capture
fidelity. Independent arithmetic reproduced the two nontrivial contrast witnesses.

Readiness: source-grounded defects and positive teaching are identified; technical
policies, mutation exceptions and failure boundaries are resolved; domain rules
are applied above; exact source/evidence homes are executable; seven focused
witnesses discriminate known mistakes; prompt/ledger/plan agree. Approximately
1,600 card lines plus445 prepared lines, short guide contexts and bounded method/
spec sections leave implementation/review headroom in a normal CC context. This
is a ready source-fix batch under the approved project, not a new research trial.

## Assignment history

- Initial: `cc-prompt.md`, issued2026-10-16 atf8205b36 after predecessorc64c5835;
  returned at source8f622e44/planninge04d8846. Independently reviewed: S16-03 done,
  remaining rows open. Preserved unchanged.
- Returned / reviewed: `cc-prompt-iteration01.md`, issued2026-10-16 atcf61f017,
  predecessore04d8846; returned at source19c7a08a/planning40c80196. Guide/native
  integration and preservation pass; F04–F06 remain. S16-03 done, three rows open.
- Accepted / final: `cc-prompt-iteration02.md`, issued2026-10-16 in the commit
  adding it, predecessor40c801963d2910d67503fde2f7ed5d3396097bc1. SOURCE pin19c7a08a.
  Correct F04–F06 within twelve card bodies and the same three return files;
  freeze the guide and retain applicable independent evidence. Returned at source4acfec6d /
  planning0dced6bb; CDC accepts all four rows on2026-10-17. No active assignment.

## Iteration01 author readiness and erratum

Was: witness3 gave `(0.5,0,0,1)` for opaque red/blue. Now:
`(0.5,0,0.5,1)`, independently computed by CDC and correctly raised by CC.
This repairs the author arithmetic, not the acceptance texts or source boundary.
The initial prompt and initial CC observation remain preserved.

CDC read all twelve revised primary cards, the HSL/guide/source delta and the
complete263-line batch/49-line closing report at8f622e44/e04d8846. The observed
failure is incomplete propagation through repeated body assertions; the refinement
therefore follows each claim family through the existing full-card sections,
checks concrete contrary examples and repairs the joined semantic evidence in
place. No new investigation or verifier is commissioned. The scoped primary
specifications and concept-card evidence/graph rules support the prescribed
repairs; source/citation preservation and fresh package integration already
reproduce. Iteration mutation is narrowed to twelve card bodies and the colour
guide; all headers, HSL endpoint, foundations, entrypoint/history are now frozen
at8f622e44. Keep version1.0.13 for this unfinished correction. One existing batch
record and three CC return paths suffice; corrected guide inputs need fresh gates.
Readiness is source-grounded, design-complete within the approved semantics,
guideline-applied, executable in named paths, falsifiable by contrary examples,
and coherent with the four-row contract. No required original-source evidence
is manufactured and no recipe depends on the false midpoint.

## Iteration02 author readiness and active delta

CDC independently read the complete revised cohort/guide and changed support
records at19c7a08a/40c80196; grammar inspection reproduces valid legacy percentage
alpha and modern numeric HSL components excluded by the cards. The remaining
verification-note scope and exact RGB CQ/direction mismatches are located in
[F04–F06](cdc-verification.md#f04-current-css-grammar-still-excludes-valid-values).
Their cause and repair are known; no diagnostic inquiry is assigned. Contrasting
grammar examples distinguish the correction without a browser or new validator.
Concept-card confidence/edge/CQ rules determine the preserved distinctions.

Current mutation scope: only the two grammar families in css-rgba/hsl-css-syntax,
and needed Verification Notes qualifications in the twelve primary card bodies.
All headers, Source References, section headings and other source bytes are
frozen19c7a08a, including the colour guide, HSL endpoint, entrypoint/history,
all161 source files and other221 cards. Same three CC return files. Keep1.0.13.
Retain accepted guide/arithmetic/native evidence after checking dependencies;
fresh native builds are not required for unbundled-card-only prose if their
inputs remain unchanged. Exact delta/preservation/meaning checks remain required.
The prompt carries the complete executable delta, focused reading/query scope,
positive/contrary examples and return contract. Readiness is source-grounded,
guideline-applied, design-complete, executable, falsifiable and within the current
four-row contract; accepted work is protected and context remains for execution.

## Version History

- 1.3 (2026-10-17): Independently accept Iteration02 and close all four criteria;
  preserve source-fidelity, actual-behavior, global and release boundaries.

- 1.2 (2026-10-16): Review Iteration01; retain passing guide, preservation and
  package integration, and issue a narrower syntax/provenance/evidence refinement.
  No parent-plan change or new slice.

- 1.1 (2026-10-16): Initial CDC review accepts preservation, resolves its own
  midpoint typo and issues one consolidated source/guide/evidence refinement.
  Preserve the initial prompt and parent criteria; Slice16 remains active.

- 1.0 (2026-10-16): Open the connected twelve-card CSS colour repair with local
  edge/CQ work, dependent HSL/guide reconciliation and proportionate evidence under
  the reassessed plans. All four criteria start open; no source acceptance.
