# Slice16 CDC verification

## Initial independent review — 2026-10-16

**Verdict: refinement required; Slice16 remains open.** CDC Sofie reviewed CC's
source `8f622e4426484eed56c918f69206c429129f9e32` and planning return
`e04d8846d36d194c4766190e28a1d7d2c58d0c86`, against initial issue
`f8205b360e67e4bdf30ad5d69fe2916ddf8da0f2` / [prompt](cc-prompt.md).
Source parent is the assigned65ed7a05. Planning return has exactly the three
permitted paths. Both commits have the two required trailers and pass whitespace
checks. CDC made no source correction. CC artifacts remain their initial evidence.

| Row | CDC disposition | Evidence / limit |
|---|---|---|
| S16-01 | open | Useful corrections landed, but F01 leaves incompatible teaching in the same cards. E00 resolves CDC's erroneous midpoint expectation; it is not a CC defect. |
| S16-02 | open | F01/F02/F03: body contradictions, missing worked guide procedure and insufficient occurrence-specific semantic support remain. Counts/resolution alone do not establish this criterion. |
| S16-03 | done | Independently reproduced exact source/metadata/citation/population preservation at8f622e44; see Reproduced checks. Applicability to a revised candidate must be checked. |
| S16-04 | open | Version and native package integration pass independently at8f622e44. The complete return is not yet accurate (F03), and the guide repair changes package inputs requiring fresh gates. Retain the passing integration evidence at this revision. |

## E00 — CDC assignment erratum, resolved

The plan's witness3 **was** `(0.5,0,0,1)` for opaque red/blue midpoint in sRGB.
It **is** `(0.5,0,0.5,1)`: componentwise lerp averages both the red and blue
components. CDC independently calculated this and confirms CC was right to flag
it. The slice plan/current iteration records the corrected oracle; the issued
initial prompt is preserved. This corrects an arithmetic typo in CDC-owned
instructions, with no changed method, acceptance criterion or source boundary.
No further Operator decision is needed to compute the stated interpolation.

## F01 — Repeated card assertions still contradict the repairs

Correctness-grade; S16-01/02. The observed pattern is that openings were corrected
while corresponding procedures, examples, relationship explanations or error
notes retained the earlier claim. A full-card reread must follow each correction
through these surfaces; another opening-only patch will not meet the contract.
These are concrete examples at source8f622e44, not an instruction to rewrite
unrelated content:

| Card / location | Remaining issue and required direction |
|---|---|
| css-rgba.md — Prerequisites, Key Properties, Recognition, Common Errors | The card still mandates eight alpha bits, excludes integer/percentage alpha, says the fourth value is always decimal, and suggests alpha255 may be invalid. Scope RGBA8 as an example; show aliases, optional alpha, numbers/percentages and specified clamping consistently. |
| rgb-colour-model.md — Key Properties, Relationships, Verification Notes | Key Properties and Relationships still present rgba() as an extension rather than an alias; the uncertainty note still teaches an integer-only classic form. Keep useful legacy examples explicitly scoped, with current grammar consistent throughout. |
| hex-colour-notation.md — Recognition, Example2, Relationships/Related | Recognition omits four/eight digits; Example2 silently corrects a source typo inside a purported quotation; Related still says rgba() is needed for alpha. Cover all forms and label the corrected example/paraphrase accurately. |
| colour-bit-depth.md — Prerequisites, Recognition, Common Errors | Prerequisites still imply quantizing linear-light values generally; recognition implies CSS mandates eight-bit values and equates every1-bit display with black/white; the32-bit error note still generalizes alpha allocation. Distinguish code count from the assigned palette, encoded/storage/model properties throughout. |
| hsl-css-syntax.md — Recognition and Examples2–3 | Recognition still requires a bare numeric hue; Sass/GreenSock excerpts are not labelled historical dependency-specific examples. Add usable modern syntax and keep the original excerpts with accurate limits. |
| additive-colour-mixing.md and subtractive-colour-mixing.md — Key Properties, Recognition, Common Errors | Unqualified lightening as an additive recognition test and generic on-screen red+green/pigment recipes survive. State physical summation under declared primaries versus digital interpolation/blending, and material-dependent pigment examples. |
| gradient-colour-interpolation.md — Prerequisites, Key Properties, Relationships, Common Errors | Prerequisite/relationship prose still universalizes RGB interpolation; normalized SVG offsets are conflated with CSS stops; 'green' is ambiguous as a CSS keyword in the numeric example. Name explicit colour endpoints/space, separate CSS lengths/percentages/angles from SVG offsets, and supply the corrected red/blue witness and alpha example. |
| mix-blend-mode.md — Core, Key Properties, Examples, Common Errors | Core misdescribes the prepared source's backdrop wording; Key Properties still applies per-channel processing to all modes; color-burn only says branches are required without teaching them; error heading suggests isolation disables blending altogether. Use the actual prepared attribution, distinguish separable modes, give the clipped branch formula and explain blending within an isolated group. |
| fecolormatrix.md — Cross-Domain Connections, Relationships/Related, Common Errors | Literal matrix mathematics is labelled STRUCTURAL while its preserved header says rigorous; CSS shorthand equivalence reappears after being rejected; invalid-value behavior is left as 'unexpected or null'. Make the bounded mathematical operation/rating consistent, explain default filter-space differences and avoid unsupported failure behavior. |
| gradient-colour-interpolation.md and css-colour-custom-properties.md — mapping labels, construction, currentColor example and verification notes | Mapping strength labels conflict between metadata/body/notes; custom-properties construction still mandates aliases and its copied currentColor selector loses the source's leading dot. Keep frozen metadata, qualify the bounded mathematical/structural claim consistently, make the optional theme recipe usable and fix the transcription. |
| colour-contrast.md — Construction/Recognition | A 1:1 ratio means equal relative luminance, not necessarily identical colours. Correct the recognition statement without weakening the text/non-text distinctions already added. |
| Primary-cohort Verification Notes | Separate historical extractor notes/confidence from current review; do not leave a current 'None' uncertainty, 'verified across sources', mapping strength or high/medium rationale contradicting the actual scope or preserved header. Original-capture fidelity and actual browser checks remain unassessed; no new header fields or scores. |

The applicable bases are [CSS Color4 §§4–7,13](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/),
[Compositing §§3.4,5.1,10](https://www.w3.org/TR/2024/CRD-compositing-1-20240321/),
[Filter Effects §§9.1,9.6,10](https://www.w3.org/TR/filter-effects-1/),
[Variables §§2–3](https://www.w3.org/TR/css-variables-1/) and the prepared source.
These are current technical/scope judgments, not historical capture fidelity.

## F02 — The guide lacks the assigned worked contrast procedure

Correctness-grade; S16-02. `guides/colour.md:38` adds thresholds and general
review advice but neither the promised numerical examples nor primary WCAG links
nor the actual sRGB calculation procedure. Supply a short method for an opaque
rendered sRGB pair: decode components, compute relative luminance and ratio,
apply the relevant criterion without rounding up. Use black/white21:1 and
#777/#fff≈4.4780894536:1 (fails normal-text AA), with primary glossary/criteria
links, relevant large-text definition and exceptions. Examples are illustrations,
not identity defaults. Keep the existing alpha/state/rendering caveats. No site,
widget or browser-conformance claim is requested.

## F03 — Semantic evidence is not yet attached at its claimed scope

Correctness-grade; S16-01/02/04. The per-card table's Scope column often reports
'No header change' rather than general/contextual/historical/inferred claim scope.
The ordered53-edge inventory records membership but not each asserted meaning,
support/rationale/outcome. Body edges are covered only by a blanket read assertion;
CQ components lack specific answering card/source passages. The discovered source
contradictions refute the table's present unqualified consistency claims.

Repair in the existing batch record: explicit five outcomes per card; precise
changed/unsupported claim-to-prepared/spec/premise joins; recoverable mappings for
all53 header occurrences and body relationship statements, plus all10 header CQ
occurrences and body questions. Group rows where a shared explanation explicitly
covers each member; do not create a schema, a file per edge, or a validator.
A prerequisite B listed by A reads B→A; extends reads A→B; related/contrast are
symmetric. Explain support, editorial inference or an exact remaining gap. Endpoint
resolution and shared source identity do not prove warrant. Give actual supported
answer components and locate them in the final cards; acknowledge partial coverage.

Correct concrete receipt errors alongside this substantive repair: additive has
four header edges (three related/one contrast), mix-blend has three (two
prerequisites/one related), not three/four respectively. Compositing1 is the
2024-03-21 **Candidate Recommendation Draft**, not a W3C Recommendation, at the
recorded URL. The specification's own status confirms this. Retain the original
observations as superseded history by pin/short explanation; no duplicate corpus
or receipt-only commit chain.

## Reproduced checks and retained proof

- Temporary independent Ruby comparisons passed: exact17-path source diff and
  assigned parent;233 unique indexed paths equal the tree;13 changed cards and220
  byte-identical; all13 Source References identical; recursive typed/order and raw
  header bytes identical outside the eight allowed scalar changes; all161 sources
  identical;17 before/after SHA256 pairs reproduce. Owning entrypoint differs only
  by1.0.12→1.0.13 and the history preserves the prior contents. LF/EOF and both
  commit whitespace/trailer/scope checks pass.
- Independent arithmetic reproduces the corrected red/blue and transparent-white/
  black midpoints, RGB/hex/count examples, source matrix opaque-black output,
  multiply/screen and color-burn branch outputs, black/white and both nontrivial
  contrast values. CSS grammar/substitution conclusions are specification-based
  inspection, not executed browser tests.
- Fresh native `make help`, `make check-skills`, `make check-skill-versions`,
  `make check-package-paths`, and separate fresh `make design` completed. Version
  gate:24 source skills/24 packages/0 errors. Paths:388 Markdown/0 hard failures,
  596 warnings at594 locations,3 exceptions,681 external URLs skipped. Descriptions
  pass the hard limit;18 exceed the soft300-character target, including design360.
  Eight ZIP Markdown members match committed source. CDC archive SHA256
  `ba995ae37342f832d5aa1208334f2f439d837dfc2a55e63072e14dd5bbc0575f`.
  Timestamp-dependent ZIP hashes need not equal CC's; member bytes do.
- Temporary checks/logs were kept under /private/tmp, not added as a product.
  An optional process-status read was sandbox-denied; it was unnecessary once
  the native logs/package were available. No corresponding evidence is claimed.
  The first link-helper invocation included concurrent Project08 edits and failed
  on an unrelated missing target; the corrected five-file Project10 scope passed.
  Concurrent Project08 files were left untouched.

Retain these results for unchanged inputs after checking applicability. The guide
repair changes package members: fresh package/version gates and byte comparison
are required. Header/citation preservation must be checked on the new delta;
there is no need to replay historical normalization/Unicode transformations.

## Bubble-up and current handoff

The17-path source candidate delivers useful portions of the coherent correction,
but not yet the complete internally consistent teaching/semantic result. E00 is
an author error; F01–F03 remain within the approved slice. No population, schema,
source-input, project/arc criterion or release gate changes. S16-03 is accepted
at its named revision; other rows stay open. One supporting artifact is present,
`artifacts/batch-record.md`; the closing report/ledger are first-class records.
No source or CC evidence was overwritten by CDC. Missing fidelity and actual
browser/hosted/AT/full-corpus gates keep their existing owners.

Issue [Iteration01](cc-prompt-iteration01.md). Keep detailed refinement here and in
the slice; no next slice opens. The arc's navigation pointer is changed once to
this slice's assignment history so future iterations do not require parent-plan
status repetition. No project-plan amendment is needed.
