# Occurrence-linked correction handoff — Iteration01 proposal

SOURCE remains pinned to dffa504e851b03b8e4746f1941068e4cc850b612; this is a proposed correction map, not a live edit or acceptance. The 42 clause records below join exact source spans, evidence roles, five-dimension outcomes, and literal replacement text in [claim-results.jsonl](claim-results.jsonl). The staged proof is unchanged at the prior accepted revision; expanded vectors and replay are in [numerical reconciliation](numerical-reconciliation.md).

## Exact replacement text

Each row gives the exact replacement proposed for the assessed clause. Statements marked retain preserve the mathematical claim within its stated boundary. The source spans and rationale remain in the linked claim records.

| Claim ID | Source span | Literal proposed replacement |
|---|---|---|
| `LIVE-SKILL-001` | `SKILL.md:366-366` | “A complete conversion can include decoding and nonlinear operations; only its individual linear stages are matrix multiplications.” |
| `LIVE-SKILL-001-ANALOGY` | `SKILL.md:366-366` | “As an analogy, OKLCH and equal temperament both seek useful organization of perceptual steps in domains with nonuniform responses; the mechanisms and evidence differ.” |
| `LIVE-FOUND-001-PIPELINE` | `foundations-of-design.md:239-241` | “For the prepared Oklab model, XYZ is transformed by M1, LMS components are cube-rooted, and M2 maps the rooted values to Oklab.” |
| `LIVE-FOUND-001-PERCEPTION` | `foundations-of-design.md:242-243` | “Oklab/OKLCh is designed to be more perceptually uniform for identified tasks; equal numeric L changes do not guarantee equal perceived brightness across hues or rendered outputs.” |
| `LIVE-FOUND-001-ATTRIBUTION` | `foundations-of-design.md:239-246` | “Oklab was introduced by Björn Ottosson; describe current CSS support with a dated specification citation and omit an unbounded ‘most important’ ranking.” |
| `LIVE-FOUND-002` | `foundations-of-design.md:251-252` | “Colour-space conversion pipelines may contain matrix stages and nonlinear stages; the complete operation is not necessarily a matrix multiplication.” |
| `LIVE-FOUND-003-MECHANISM` | `foundations-of-design.md:438-444` | “Equal temperament is an analogy for organising perceptual steps; the mathematical objectives, measurements, and evidence are domain-specific and are not established as identical here.” |
| `LIVE-FOUND-003-COLOUR` | `foundations-of-design.md:441-444` | “Some colour models aim for more uniform perceptual differences over bounded conditions; no universal equal-step guarantee is claimed.” |
| `LIVE-FOUND-004-STAGES` | `foundations-of-design.md:446-449` | “The linear sRGB→XYZ and XYZ→LMS stages are matrix operations.” |
| `LIVE-FOUND-004-MATRIX` | `foundations-of-design.md:446-449` | “The chain includes a componentwise cube root between linear matrix stages, so the complete conversion cannot be collapsed into a single matrix.” |
| `LIVE-FOUND-004-GRASSMANN` | `foundations-of-design.md:449-449` | “Remove the Grassmann attribution unless its specific source and applicable proposition are supplied; ordinary composition of adjacent linear matrices needs no attribution here.” |
| `LIVE-FOUND-005` | `foundations-of-design.md:451-456` | “The 12-hue/12-semitone comparison is a loose structural analogy, not evidence of a shared mechanism.” |
| `LIVE-FOUND-005-EMPIRICAL` | `foundations-of-design.md:453-455` | “Do not state the strength of empirical evidence without citing the relevant studies and defining the tested claim and population.” |
| `LIVE-FOUND-005-MATH` | `foundations-of-design.md:455-456` | “No mathematical equivalence is established by this analogy; that limit is not a proof that no equivalence could be formulated.” |
| `LIVE-DESIGN-001` | `design.md:140-142` | “Oklab/OKLCh is one model designed for improved perceptual uniformity in identified use; remove best-available and all-hue guarantees.” |
| `LIVE-DESIGN-002` | `design.md:143-146` | “Equal L increments are equal coordinate changes in Oklab; perceived differences depend on colour, observer, viewing conditions, gamut mapping, alpha, and compositing.” |
| `LIVE-COLOUR-001` | `colour.md:9-11` | “This guide concerns the named C&B sites. Oklab/OKLCh may be considered as a perceptual model; do not promise equal brightness across hues.” |
| `LIVE-COLOUR-002` | `colour.md:546-550` | “Treat paired token steps as a palette-review hypothesis. Equal temperament is an analogy; it does not establish equal perceived jumps.” |
| `CARD-001` | `matrix-transformation-colour.md:41-41` | Retain: “Matrix transformation in colour conversion is a 3×3 matrix multiplication that linearly maps colour coordinates between bases.” |
| `CARD-002` | `matrix-transformation-colour.md:45-63` | “The prepared Oklab account shows M1, componentwise cube root, and M2. These are principal stages, not the only operations.” |
| `CARD-003` | `matrix-transformation-colour.md:72-76` | Retain for individual linear stages; explicitly exclude the intervening nonlinear root from the matrix claim. |
| `CARD-004` | `matrix-transformation-colour.md:97-97` | “M1 and M2 are 3×3 matrix operations in the prepared XYZ account; the complete pipeline also includes a nonlinear componentwise cube root.” |
| `CARD-005` | `matrix-transformation-colour.md:101-103` | “For the article’s stated D65 XYZ example, M1 yields approximate LMS coordinates; preserve the source’s rounded values and identify them as that generation.” |
| `CARD-006` | `matrix-transformation-colour.md:121-121` | Retain verbatim; the staged proof and linear-white / linear-white-1/8 witnesses support this distinction. |
| `CARD-007-ERROR` | `matrix-transformation-colour.md:125-126` | “For encoded sRGB input to the article’s linear-sRGB function, decode sRGB before applying its combined matrix A.” |
| `CARD-007-NAMING` | `matrix-transformation-colour.md:128-129` | “The C++ forward code applies combined linear-sRGB matrix A directly to linear RGB. It is not the standalone XYZ→LMS matrix M1. In a consistent coefficient generation A corresponds to composing sRGB→XYZ with M1; printed rounded generations may differ, so no exact equality is asserted.” |
| `CARD-008` | `matrix-transformation-colour.md:133-134` | “The inverse pipeline uses inverse linear transforms plus inverse nonlinear operations; negating coefficients is not an inverse.” |
| `CARD-009` | `matrix-transformation-colour.md:142-142` | “The local description identifies the pinned prepared article passages; do not call them direct transcription from the original until immutable capture and lineage are verified.” |
| `CARD-009-CONFIDENCE` | `matrix-transformation-colour.md:143-143` | “Confidence is limited to comparison with the pinned prepared article; original-source confidence remains unassessed.” |
| `CARD-009-UNCERTAINTY` | `matrix-transformation-colour.md:144-144` | “Uncertainties remain: original capture/lineage is missing, and displayed coefficients are rounded.” |
| `CARD-009-CROSSREF` | `matrix-transformation-colour.md:145-145` | “The local C++ listing and four printed table rows were compared; this does not verify original-source fidelity or every referenced claim.” |
| `CARD-009-ROSETTA` | `matrix-transformation-colour.md:146-146` | “The mapping is rigorous for the identified matrix stages, not the complete pipeline including the nonlinear root.” |
| `CARD-009-OCR` | `matrix-transformation-colour.md:147-147` | “OCR/extraction history was not independently reproduced; retain only with the source conversion record and original capture.” |
| `CARD-010-ROSETTA` | `matrix-transformation-colour.md:33-35` | “The M1 and M2 stages are literal 3×3 matrix multiplications; the full conversion also includes componentwise cube roots.” |
| `CARD-011-ROSETTA-REPEAT` | `matrix-transformation-colour.md:146-146` | “The mapping is rigorous for the matrix stages; it does not describe the complete nonlinear conversion as one matrix.” |
| `CARD-012-PREREQUISITE` | `matrix-transformation-colour.md:67-68` | Retain with clarification: “The XYZ-form M1 takes XYZ input; the separate combined matrix A takes linear-sRGB input.” |
| `CARD-013-CONSTRUCT` | `matrix-transformation-colour.md:81-84` | “For a linear map, define axes and derive a matrix from basis vectors; for the complete Oklab conversion, compose the inverse linear transforms with the inverse cube and any required transfer function.” |
| `CARD-014-RECOGNIZE` | `matrix-transformation-colour.md:86-88` | “Three weighted sums identify each displayed linear matrix stage; the adjacent cbrtf operations are nonlinear and are not part of a single dot-product map.” |
| `CARD-015-CONTEXT` | `matrix-transformation-colour.md:92-92` | “Many colour conversion pipelines include matrix stages; some also include nonlinear transfer functions and other operations.” |
| `CARD-016-APPLICATIONS` | `matrix-transformation-colour.md:93-93` | “List these as examples only with application-specific sources; do not infer that the full pipeline is a matrix operation.” |
| `CARD-017-GENERATION` | `matrix-transformation-colour.md:103-103` | Retain the table description and identify its XYZ matrix generation and three-decimal rounding. |
| `CARD-018-BOUNDARY` | `matrix-transformation-colour.md:92-93` | Not a replacement assertion: these claims require separate application evidence; no GPU/ICC benchmark or relationship/CQ execution was performed. |

## Later owners and dependencies

- **R/T/C/L/G** remain the Arc02 families; this handoff provides only bounded T-family math/evidence and the overlapping DES-007/limited DES-002 correction proposals. It closes none of the other families.
- **DES-007** owns later authorized correction/review of the pipeline explanation. **DES-002** owns only the overlapping colour-uniformity/analogy clauses here; its wider perceptual population remains open.
- **Arc03–05 owners** retain later implementation and validation duties. This handoff grants no live source edit, implementation, release or next-slice authority.
- **P10-11 source readiness** and the **Operator** own original-capture readiness and any acquisition decision. For each claim, missing originals block only source-fidelity results that depend on those originals. Exact pinned mathematical operators and independently reproducible arithmetic can be assessed on their own evidence. Re-entry for a blocked fidelity clause requires an immutable original Oklab capture and manifest covering source identity/hash, capture time/version, original-to-prepared transformations, context/completeness, and exact-span mapping, plus independent P10-11 readiness.
- Any future live mutation requires a fresh explicit source assignment and independent review of the corrected revision. No blanket wait for unrelated originals and no readiness waiver are proposed.

## Practical dependencies and boundaries

Future palette/rendering work must identify input colour space and white point, target gamut, alpha and background/compositing behavior, and the actual foreground/background/state pair. These are requirements for later scoped work, not an algorithm, contrast certification, browser result, or palette result. No C&B-specific profile, semantic role, or default token steps are approved. Any example token values must be neutral and explicitly optional or supplied by the adopting project.

## Re-entry and review

- Relationships/CQs, GPU/ICC application behavior, unassigned card assertions, full 233-card/eight-live-file review, source fidelity, empirical perception and accessibility remain unassessed or open under the exact boundaries in claim records.
- Keep S02-03 and S02-05 at their CDC-accepted done status; the other seven Slice02 criteria remain open pending independent review of this iteration’s changed evidence.
- CDC should inspect exact source/evidence joins, the staged numerical replay and focused evidence controls, then decide each row independently. No Arc02 plan change or next slice is proposed by CC; CDC and Operator retain their recorded gates.
