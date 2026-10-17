# Slice17 CDC verification — initial return

2026-10-17; CDC Sofie; Two-Contributor Workflow, Expedited Mode.
**Current verdict: Iteration01 requires refinement; Slice17 remains open.**
The initial review below remains evidence at its stated revisions.

## Reviewed identities and governing scope

- Project plan1.73 and Arc02 plan1.52; slice plan1.0 and four unchanged criteria.
- Initial issue: `1855cdea5cdcda4c78c4350b5901cf2c77965e2a`;
  SOURCE baseline: `4acfec6d8fa17e1ecb869bda28a6e71d17ef771e`.
- SOURCE candidate: `485585efe99c2d2cf3b956356989664bc6ffa262`, including
  `c8b16c7e` and `26320610`.
- Planning return: `61b3c427433f324a0933f7bcdccc507e6a03accb`, including
  `cc6a8b01`, `b7e8f36a` and `609084e1`.
- Complete current thirteen primary cards, dependent terminology card, source
  changes, batch record and closing report inspected. Primary comparisons use
  the pinned prepared article and scoped Ottosson/W3C/CIE support below.

The candid incomplete return is useful evidence, not semantic acceptance.
The fixes below finish the issued delivery; no new investigation, schema,
analysis-only phase, parent scope change or successor slice is authorized.

## Row dispositions

| Row | CDC disposition | Basis |
|---|---|---|
| S17-01 | open | Several repaired cores conflict with surviving prerequisites/examples; useful positive teaching was lost; complete five-dimension outcomes remain unfinished. F01/F02/F03. |
| S17-02 | open | Dependent terminology and two guide corrections pass at their bounded scope. Header identities resolve, but directed meanings and edge/CQ warrants are unfinished. F03. |
| S17-03 | **done** | Independently reproduced roster, exact source scope, eleven permitted scalar deltas, frozen representation/citations/headings and protected populations. |
| S17-04 | open | Owning version/history and fresh native/package integration pass. The complete bounded semantic return required by this row is unfinished. Retain the passing integration evidence. |

## F01 — contradictory or inaccurate teaching remains

These are current SOURCE485585ef sections, not historical-only allegations.
Correct the entire affected sentence family, preserving useful explanations.

| Card / section | Observed problem and required interpretation |
|---|---|
| chroma-perceptual / Prerequisites | Makes chroma's value depend on uniformity. Coordinate C remains meaningful in an imperfect model; uniformity concerns interpretation of perceived differences. |
| colour-interpolation-perceptual / Prerequisites | Says interpolation is meaningful only in uniform spaces and requires Oklab then sRGB. Scope that route to the example; other selected spaces/output targets are valid. |
| lightness-perceptual / Prerequisites, Context, Confusions | Says reliable L requires uniformity, calls WCAG contrast a lightness comparison, and gives an unscoped CAM16 superiority statement. Distinguish fitted L, source lightness metric, approximate greyscale construction and actual-pair relative-luminance contrast. |
| d65-whitepoint / Construction, Recognition | Treats rounded white values as exact, says a different input white requires different Oklab matrices, and identifies D65 merely by approximate6500K. Retain rounded example, reference chromaticity/convention and adaptation to expected D65. |
| oklab / Prerequisites, Confusions | Makes explicit XYZ mandatory and invents the author's motive for the name as deliberate understatement because of superior performance. Combined linear-RGB routing is valid; keep the actual naming statement without invented motive. |
| oklab-conversion / Prerequisites, Errors, Confusions | Conflates XYZ M1 and combined RGB coefficients, omits the nonlinear stage, suggests combined coefficients could bypass decoding, and asserts exact composition across unspecified coefficient families. State domains, decoding and matched-family precision boundaries consistently. |
| matrix-transformation-colour / Properties, Construction, Errors | Treats calling a zero-offset linear map affine as an error. Linear maps are affine maps with zero translation. Inversion requires nonsingularity; the full cube-root route is nonlinear. |
| lms-cone-responses / Construction step2 | Multiplies the3×1 vector by the3×3 matrix in invalid order. Write M1(3×3) times XYZ column(3×1). |
| colour-space-comparison / Core, Properties, Construction, Confusions | Blanket CAM16 attribution loses the source distinction: generated lightness/chroma data use CAM16; perceived-hue data are the separate data used to derive IPT. Scope each table/method claim to its actual dataset. |

## F02 — restore usable positive teaching and correct attribution

The repair must remain a tool a designer can use, not only warnings.

- `oklab.md`: restore meanings of L and opponent a/b axes. The current card
  names the coordinates without explaining green–red and blue–yellow axes.
- `oklab-conversion.md` / Examples says full forward and inverse C++ listings
  are provided verbatim, but neither listing is present. Restore an executable
  mathematical recipe with the published forward coefficients, labelled
  inverse stages and a worked example; accurately describe any source excerpt.
  The matrix card also lost its numeric tables. Supply its XYZ M1/M2 rows or
  a precise local link to those labelled rows. Do not confuse combined RGB A
  with XYZ M1, independently rounded families or a specification's coefficients.
- `xyz-colour-space.md`: preserve Y's legitimate luminance role under stated
  observer/normalization; relative Y is1 at diffuse white in the referenced CSS
  convention. This differs from Oklab L. X/Z are not isolated chrominance.
- Conversion Verification Notes attributes a neural-network comparison to the
  article. The prepared article contains no `neural` occurrence. Remove that
  attribution or identify the analogy as card-author synthesis, with limits.

Prepared article lines37–51 support axes/polar coordinates;73–110 XYZ matrices;
114–161 linear-RGB forward/inverse code and update;198–232 distinct derivation
sets;234–249 scoped errors. [Ottosson's article](https://bottosson.github.io/posts/oklab/)
was inspected as current technical support, not immutable original fidelity.
[CSS Color4 dated2026-10-09](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/),
§10.9 supports XYZ Y; §§9.2/10.10 support whitepoint/adaptation distinctions.
No benchmark, physiological or browser experiment is inferred.

## F03 — finish the existing semantic review, with real joins

The79 table rows reproduce current source-card/field-index/target identities
exactly. They all use symmetric arrows, including27 prerequisites and7 extends.
Correct direction under Concept Cards guide06; add the premise, reasoning and
bounded CC outcome for each recoverable occurrence. An editorial learning route
is not a strict mathematical necessity or an author-attributed assertion.

The baseline has102 body relationships; current thirteen cards have86. Trace
baseline occurrences to retained/rephrased/merged/removed outcomes and review
all final/new ones. Do not force the final count to102 or remove useful teaching
to avoid assessing it. Compact groups with explicit membership are sufficient.
Read full bodies for questions, not just headers or question-mark searches.

All20 header CQ occurrences/five exact texts match the current headers, with
counts8/5/5/1/1. Existing group answers do not show each card's actual component.
Locate each component/premise, distinguish partial from full contribution, and
show a bounded combined answer. D65/reference background alone does not answer
uniformity; L targets alone do not warrant equal appearance or contrast.

Complete thirteen actual outcomes distinguishing prepared-source agreement,
technical correctness, scope, internal consistency and relationship/CQ support.
Missing original fidelity stays blocked where applicable. Do not call unfinished
available review an external-input block. References to CRC are erroneous here:
CDC is the independent reviewer; CC makes its own bounded assessments.

## Independently reproduced checks and retained evidence

- Exact17-path net source write set. Fourteen ordered typed headers differ only
  at the eleven authorized scalar values; raw header changes match those values.
  All fourteen literal citations and heading sequences survive. Other219 cards,
  all161 source files and unrelated guides survive. The233 exact paths match the
  accepted index; SKILL changes only its version; previous history is retained.
- All three source/four planning commits have required trailers and clean diffs.
  Aggregate planning return has exactly the three authorized paths; initial
  prompt and plan match the issued bytes. Untracked `knowledge/lfe/` untouched.
- Fresh sequential `make help`, `make check-skills`, `make check-skill-versions`,
  `make check-package-paths`, then separate fresh `make design`: all exited0.
  24 source/package skills,0 version errors;18 soft description notices;
  package scan388 Markdown,0 hard failures,596 warnings at594 locations,
  3 exceptions,684 external URLs skipped. No CDC gate failed.
- Fresh ZIP8/8 Markdown members match committed source. CDC ZIP SHA256
  `bf53ec383e7dba9fcc65e7debc021b94687aa5c6f5a41fa87b30a7523a8623a2`.
  Archive bytes differ from CC's ZIP; member comparisons establish source equality.
  CC's initial write-denied/stale-archive attempt and successful retry remain
  disclosed; they are not concealed as a first-attempt pass.
- Fresh literal-coefficient calculations: linear grey.125 gives L=.4999999967;
  decoded encoded-grey.5 gives L=.5981807266; wrongly treating.5 as linear gives
  L=.7937005208. F(.5white) differs from.5F(white); complete route is nonlinear.
  CC's neutral shortcut differs at immaterial final decimal places.
- A temporary edge-check helper initially used unavailable `YAML.unsafe_load`
  in the installed Ruby, then used available YAML parsing and passed79 exact
  identity joins,20 CQ occurrences and the current86 relationship count.
  This is structural evidence, not an edge-warrant pass.

Gate logs `/private/tmp/p10-s17-cdc-*.log`, gate exits JSON and focused results
JSON are temporary execution aids; this record is the durable result. No new
validator, numerical benchmark, browser/AT/hosted check or capture acquisition.

## Review-packet validation

The four CDC planning outputs pass24 local links/five fragments and LF/EOF
checks. All four criterion/verification/origin/significance fields remain
unchanged; only S17-03 changes status to done. Initial prompt and both CC evidence
files remain byte-identical to61b3c427. The planning diff is exactly this record,
the iteration prompt, slice plan and ledger; source HEAD remains485585ef.

## Handoff and parent boundaries

[Iteration01](cc-prompt-iteration01.md) repairs F01/F02 and completes F03 in the
same delivery. Freeze accepted metadata and all nonprimary source paths at485585ef;
retain applicable checks after verifying their inputs. S17-03 remains done.
No source changes made by CDC. Project/arc design and release gates are unchanged;
no need to bubble ordinary iteration detail into another plan. No slice close,
Slice18 opening, push or publication is authorized by this review.

## Iteration01 independent review — 2026-10-17

**Refinement required.** Source `c884b8f9ebc6c2c80385b8f1f3db9ecd63cb67fb`,
direct child of485585ef; planning return
`9214210a11443f12b70d7d9b7d83cdc7b4012694`, direct child of issuing
`de960367b73ac614619f3e7600436458eaa8c459`. The executed assignment is
[Iteration01](cc-prompt-iteration01.md); its protected scope is unchanged.
Project1.73 / Arc02 1.52 still govern; no parent amendment is needed.

Reviewed the entire source delta, complete affected teaching in conversion,
lightness, LMS and interpolation, five-outcome/CQ tables and all occurrence
identities/dispositions. Repeated endpoint Core quotations were projected to
unique card/section premises and per-occurrence meaning/outcome for inspection;
this did not substitute a count for semantic review. Recovered clipped table
projections explicitly. Retained unchanged card/guide coverage from the initial
review after checking its inputs. Prepared mathematical73–161 and derivation
198–249 passages were freshly compared; the article contains no neural/network
wording. No new inquiry or original-source acquisition was commissioned.

### Passing work and evidence retained

The restored A/B and inverse recipe is useful and its numeric example is correct.
CDC parsed the actual published rows in the current card, compared coefficients
to the prepared article, and independently calculated linearRGB(.2,.4,.8):

- A: (.338134103,.40057808296,.63433098782).
- Roots: approximately(.696674088604,.737161074847,.859221843352).
- Oklab: (.728143374354839,−.025083383345993027,−.09975633436673832).
- Reverse: (.20000002510029638,.3999999984107042,.7999998603903674).
  Maximum absolute channel error1.3960963263e-7, below1e-6.

Keep this example, axes, restored XYZ matrices, affine correction, D65/adaptation
repair and L/C-versus-hue dataset distinction. No arithmetic rerun is needed for
pure attribution or mapping changes that leave these inputs unchanged.

Independently reproduced: exactly ten allowed card-body paths; full thirteen
metadata prefixes/citations/heading sequences unchanged;233 identities; other220
cards/all161 source files unchanged; exact three-path planning return; source and
planning parent/trailer/diff checks. The three unchanged primary cards retain
applicable prior evidence. Initial prompt, Iteration01, plan and CDC record match
the issue. No source edit or push by CDC; untracked knowledge/lfe/ preserved.

The only source delta is unbundled card bodies, so all native/package inputs
are unchanged. Retain the initial CDC-fresh gates at485585ef (including warnings
and CC's disclosed earlier build recovery), rather than relabel them fresh.
The existing ZIP was also directly compared again:8/8 Markdown members match
current committed source. No native gate, browser, hosted check or original
capture verification was newly run. Focused output is temporarily recorded in
`/private/tmp/p10-s17-i1-cdc.json`; this review is the durable receipt.

### F04 — source contradictions survive the correction

These prevent S17-01 acceptance; they are substantive, not editorial polish.

| Current card / section | Failure | Required repair |
|---|---|---|
| oklab-conversion / Core and Verification Notes | Both still attribute a neural-network analogy to the article. Cross-Domain Connections correctly says it is absent; CC batch/report also claim the attribution was removed. Literal article search returns zero neural/network matches. | Identify it consistently as optional card-author analogy, absent from the prepared article, or remove it; correct the current report/evidence too. |
| oklab-conversion / Matrix prerequisite | Still says the algorithm consists of matrix multiplications, contradicting its restored nonlinear recipe. | Attribute matrix multiplication to the linear stages around the signed-root stage. |
| oklab-conversion / Common Confusions | Still asserts unconditional equality/equivalence of the printed combined and XYZ forms without a specified matched sRGB/XYZ family. | Explain conceptual composition of compatible linear stages; retain the distinction between the separately printed rounded families and their input domains. |
| lms-cone-responses / Construction step3 | Calls the values resulting after cube root lowercase l/m/s, although the source and its own code use those names before the root. | Distinguish unprimed M1 outputs from primed/rooted coordinates and final uppercase L. |
| lightness-perceptual / Common applications | Still promises greyscale conversion preserving perceived lightness, while the repaired Relationships correctly says neutral model construction with checks. | State preserving model L when setting a=b=0; appearance is approximate and requires output/context checks. |
| colour-interpolation-perceptual / Oklab prerequisite | Unqualified “The interpolation is performed in Oklab” conflicts with the broader valid selected-space explanation. | Scope this prerequisite sentence to the article's Oklab example. |

### F05 — occurrence mapping is not yet accurate

All E01–79/B001–102/F01–86/Q01–20 ID sets are complete and ordered. Header
directions are corrected. The repeated endpoint quotations are useful inputs,
but they do not make the following wrong joins true.

The baseline crosswalk calls surviving/retyped material removed. Correct these
specific joins, separating the removed overclaim from retained/revised teaching:

| Baseline | Surviving final material | Disposition required |
|---|---|---|
| B020 | F16 tradeoff analysis | Rephrased/narrowed; categorical best-balance claim retired. |
| B022 | F18 Chroma / Lightness | Chroma component retained in compound statement. |
| B042 | F36 wider gamuts | Narrowed contrast; universal supersession/HDR claim retired. |
| B045 | F39 intermediate/root | Narrowed stage relation; physiological generalization retired. |
| B046 | F40 neutral construction | Rephrased/narrowed; equal appearance not promised. |
| B066 | F60 nonlinear operations | Retained/rephrased, not absent. |
| B067 | F61 intermediate coordinates | Retained/rephrased under revised label. |
| B083 and B084 | F74 Chroma / Lightness | Two components merged into one current statement. |
| B089 | F79 Oklab | Moved/retyped from Enables to Related; approximate model. |
| B097 | F84 LMS-like intermediates | Moved/retyped from Enables to Related, with stage scope. |

Check other removal dispositions for the same label/type/merge issue, using the
existing rows and actual statements, not a fresh extraction or forced count.
B077's removal reason must not imply the prepared article lacks the IPT structural
connection: line220 explicitly says the fitted structure is the same as IPT.
Distinguish retiring a card-local dependency from denying that source statement.

Some final outcomes falsely say no reviewed cohort endpoint is named merely
because a label is compound or differs from a slug: F18/F74 include chroma and
lightness; F39 includes LMS plus conversion stages; F46 includes XYZ Y; F51/F62
name the matrix-transformation concept exactly; F33 names Oklab design and has
prepared derivation support. Resolve these actual components and state their
limited premise connections. Local general teaching need not become a new typed
edge. No new card/field/schema or out-of-cohort graph review is requested.

E69 still calls Oklab versus colour-space-comparison a contrast of named models.
One endpoint is a model, the other comparative evaluation. Describe that specific
reading distinction and the comparison card's assessment of Oklab, not imaginary
opposed models. Retain the other checked directions and sound premises.

### F06 — CQ outcomes overstate current body coverage

Q11 and Q16 claim full palette coverage, but the cited bodies only say choose
L/C/h candidates and check output; they do not specify how L targets/steps are
constructed across the intended hues. The combined answer adds that missing
step without locating it in a card. Add the small model-coordinate procedure
in lightness's existing Construction section, with appearance/gamut limits;
let Oklab/Q16 remain a partial contribution pointing to that procedure.

A useful concrete construction is L_i=L_start+i(L_end−L_start)/n for integer
n>0 and i=0…n, applying chosen L targets across intended hues with contextual
C choices and subsequent gamut/render/actual-pair checks. Equal numeric L steps
are not a universal appearance promise. This is a supported coordinate method,
not a default palette or perception experiment. It fills the assigned usage gap.

The thirteen-outcome summary also calls Oklab's uniformity contribution full
while Q15 calls it partial. Align actual component labels and source locations;
retain the other honest partial/missing contributions (including D65).

### Iteration01 row dispositions and handoff

| Row | CDC state | Evidence / remaining work |
|---|---|---|
| S17-01 | open | Restored arithmetic/axes/matrices and most initial corrections pass; F04 contradictions and F06 usable palette step remain. |
| S17-02 | open | Correct directions and explicit partial CQ records retained; F05 false joins and F06 coverage mismatch remain. Dependent/guide acceptance is unaffected. |
| S17-03 | done | Initial independent acceptance remains applicable; current preservation independently reproduced again. |
| S17-04 | open | Integration/native/package components pass by checked retention; the bounded return still overstates repairs and mapping accuracy. |

Artifact inventory is still one supporting batch record. The first-class CC
report and protected issued prompts are present. No silent deferral to global
review is accepted for these available local defects. Parent original-fidelity,
behavior, full-corpus, hosted/rendering and release gates remain open unchanged.
[Iteration02](cc-prompt-iteration02.md) narrows source mutations to the four
named bodies and repairs the affected existing records. No close or successor.

Review packet validation: four CDC paths,26 local links/seven fragments, LF/EOF
and diff whitespace pass. All criteria/verification/significance/origin/status
cells match9214210a; only Evidence/Notes change. Both issued prompts, CC batch
and CC closing report remain byte-identical. SOURCE remainsc884b8f9. This review
and Iteration02 are committed together; no receipt-only follow-up is needed.
