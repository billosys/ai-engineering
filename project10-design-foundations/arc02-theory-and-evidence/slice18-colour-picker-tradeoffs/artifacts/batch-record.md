# Slice18 batch record

## Intake and pinned state

- Assignment: `arc02-theory-and-evidence/slice18-colour-picker-tradeoffs/cc-prompt.md`.
- Issuing planning commit: `fe91602e2b732da71f29d2e790d25c7f85477da6`.
- Planning predecessor recorded by the prompt: `a888e85710b18f031186b2bafde97d57bd8d0c02`.
- Source baseline: `4e635bb39b2c6151014b316f45f279d3682416d4` (`Correct Oklab teaching and palette procedure`).
- Prepared picker article SHA-256: `227d62385a8ca4dfa77e9f5a10d55c9bd8d1c2f29d8964f59a1059bfb67d5d19` (1136 lines).
- Prepared Drasner article SHA-256: `f4cf46139cd45b5e8d78865666520520493dbafe4fe39a89b9c0e32227c0e4af`.
- Intake worktree observations: planning `fe91602e2b732da71f29d2e790d25c7f85477da6`; source `4e635bb39b2c6151014b316f45f279d3682416d4`. The source worktree has pre-existing untracked `knowledge/lfe/`; planning has pre-existing untracked `project14-fennel/`. Both are preserved and outside this assignment.

## Contract readback before implementation

This is a bounded source-correction assignment. The maximum source write set is exactly the eleven named card bodies/frontmatter plus `knowledge/design/SKILL.md` and its append-only `version-history.md`. Only six specified Rosetta Stone scalar values and one invalid CSS association may change in metadata; every other identity, metadata value/order/type/list distinction, citation/Source Reference section, and existing body heading is frozen. The owning design skill is to move from 1.0.14 to 1.0.15. The accepted scope is correction of supported claims from all available evidence, not a claim of source-capture fidelity, full-corpus semantic conformity, accessibility conformance, browser behavior, or release readiness.

The semantic review must cover every card across source agreement and fidelity limits, correctness, scope, internal consistency, and relationship/CQ support. It retains the source article's eight subjective and conflicting picker goals and model profiles; separates numeric independence, vector geometry, perception, smoothness and evenness; distinguishes encoded sRGB HSL/HSV arithmetic from CSS syntax; and limits gamut and conversion statements to specified conditions. It must explain the nonlinear Okhsl/Okhsv pipeline, singular/neutral conventions, three-reference rational Okhsl saturation construction, source-code/helper limits, and attributed Munsell/NCS context. The illustrative native input stays in prose but is not treated as Drasner's literal markup or as evidence of its internal picker model.

The supporting record must account for 66 header edges with direction/meaning and premises, all 65 predecessor body relationship statements with a disposition and final join, and all 15 header CQ occurrences across their three exact texts with actual answer components and bounded attempted answers. The listed RGB, grey, toe, rational interpolation, hue and degenerate-boundary witnesses are arithmetic or direct source/algebra checks; missing helper code is not represented as executed. Figures and inaccessible full Munsell-owner material remain explicit limitations.

Required local gates are sequential in the source checkout: `make help`, `make check-skills`, `make check-skill-versions`, `make check-package-paths`, fresh `make design`, then byte comparison of all eight packaged Markdown members with the committed source. Required planning deliverables are this `artifacts/batch-record.md`, a proposed-done `closing-report.md`, and Evidence/Notes updates only in the existing slice ledger. Plans, prompt, criteria, statuses, other 222 cards, 161 sources, guides, helpers, package/schema files, and the two unrelated untracked directories are preserved. Source and planning commits are separate, path-scoped, with both required co-author trailers. No push, publication, CDC acceptance, closure, or successor slice is authorized.

## Read coverage

Read in full before implementation:

- Slice18 prompt, slice plan and ledger; active Project10 plan/ledger and Arc02 plan/ledger; current planning and source instructions.
- All eleven current target cards; the complete prepared picker article; Drasner's HSL and native-input passages; the `hsl-css-syntax` endpoint; accepted Oklab, conversion, perceptual lightness/chroma and colour-method guidance.
- Collaboration-framework, project-management wayfinder and relevant planning/close routes, engineering-methods guide07, work-verification ledger/row closure/independent verification, Concept Cards entrypoint/guides05–06, visual-design colour guidance.
- CSS Color Module Level 4 Candidate Recommendation Draft dated 2026-10-09, §§7–7.2 and 14; HTML Living Standard Color state; official NCS System explanation.

The named prepared-text hashes were checked at intake. No browser picker, accessibility/AT behavior, figure image, unavailable full Munsell page, or original source-capture fidelity was tested or inferred. Technical statements derived from current standards are version-scoped to the inspected documents.

### Outcome dimensions (proposed CC assessment)

The judgments below are scoped to the complete available text, named primary support and accepted endpoints read for this task. “Full review” means the full body was inspected; it does not mean every claim has original-source capture fidelity or independent acceptance. Extraction confidence is predecessor metadata and was not recalculated.

| Card | Source agreement / fidelity limits | Correctness | Scope | Internal consistency | Relationship / CQ support |
|---|---|---|---|---|---|
| `colour-gamut` | Ottosson explicitly targets sRGB in this article; figure descriptions are prepared-text attribution only, with no visual reinspection or original-capture proof. | Corrected gamut to representable set/volume and separated conversion, destination mapping and component clipping; the named CSS Color 4 sections describe a scoped SDR display process. | Article’s sRGB coordinate/gamut case only; not a universal CSS, display, HDR or print gamut. | Removed inverted Error/Correction and unqualified cylinder/nearest-clamp teaching; HSL/HSV remain bounded RGB reparameterizations, not perceptual spaces. | Header routes to RGB/HSL/HSV and picker models are retained as scoped editorial links; supports one partial CQ contribution about design tradeoffs. |
| `hsv` | The complete prepared article names HSV and its author-rated profile; the deep-blue shift remains an attributed, uninspected example. | Added encoded-sRGB M,m,Δ,V,S and hue definitions; corrected V, achromatic hue and S<1 mixture explanations. | Classic normalized encoded-sRGB formulas only; not a general CSS or perceptual appearance definition. | HSL/HSV contrasts remain distinct by formulas; bounded versus perceived behavior is explicit. | Prerequisite RGB relation and HSL/Okhsv/NCS contrasts now state model-specific premises and limits; contributes a partial Okhsl/Okhsv CQ answer. |
| `colour-picker` | Ottosson’s space-versus-widget scope and Drasner’s native-control sentence are checked in prepared text; original native markup was not recovered. | Separated colour model, widget, output, host and accessibility concerns; HTML Living Standard supports color-well/value framing, not the asserted internal model. | No market-adoption claim or widget prescription; illustrative HTML and host-dependent UI are scoped. | Removed unsupported ubiquitous/dominant/current picker statements and false inference from native input to HSV/Okhsl. | Edges to models, principles, NCS and numeric input are editorial task/interaction routes; CQ is partial because no actual widget or accessibility evidence is in scope. |
| `chroma-vs-saturation` | Full card compared with the article and accepted Slice17 terms; unavailable original capture and full Munsell-page limits are retained. | Separated CIE terms, model C and HSL/HSV formula parameters; removed universal C/L and maximum claims. | HSLuv/Okhsl descriptions are source/model-specific; no broad perceptual law is asserted. | Relationships to orthogonality and model families now distinguish numeric coordinates from perception; outdated bounded-only note replaced with actual wider review scope. | Its two header CQs map to defined model distinctions and picker tradeoffs; chroma/saturation CQ is answerable in bounded terminology, broad picker CQ only partial. |
| `colour-picker-design-principles` | All eight goals and conflict were read in complete prepared text; model table and figures remain attributed/source-limited. | Restated eight named criteria; separated perceptual control, geometry, smoothness and evenness. Ratings are explicitly subjective. | The author’s sRGB comparison only; not a standard, universal user result or widget/accessibility score. | Both Okhsl/Okhsv Varies Evenly=no; Okhsv Orthogonal Lightness=no; HSV hue only partial. Analogy is loose. | Gamut and orthogonality edges point to actual defined criteria; CQ answer is partial to the article’s proposed frame, not all real picker quality. |
| `okhsl` | Complete article’s formulas/code and accepted Slice17 Oklab/conversion premises checked; omitted gamut helpers and unavailable figure inspection are disclosed. | Corrected toe and base-L order, get_Cs input, C0-as-slope, piecewise rational map/inverse, hue turns and neutral boundaries. Synthetic arithmetic example is not measured. | sRGB/article construction only; no exact perception, accessibility, drop-in compatibility or complete converter claim. | Removed false matrix-transform/drop-in/uniform-contrast wording and added distinct Okhsl/Okhsv profiles; metadata analogy corrected exactly as authorized. | Editorial edges to HSL, Oklab and Okhsv state distinct constructions; two CQ occurrences support a partial, task-conditional comparison. |
| `munsell-colour-system` | Retained only article-supported HVC, notation and attributed description; full Munsell-owner page unavailable, and image not inspected. | Removed universal chroma~20, exact uniformity and direct HSL/modern descent; retained irregular solid and bounded notation. | Historical overview is not extended beyond prepared source; no new historical inquiry. | NCS and HVC descriptions remain distinct; Drasner’s “based on” claim is attribution, not proof of derivation. | Edges to NCS/HSL/Oklab are qualified structural or attributed comparisons; contributes partial context to picker CQ. |
| `hsl` | Prepared source and full accepted hsl-css-syntax endpoint read; CSS syntax checked against CSS Color 4 CRD 2026-10-09 §§7–7.2. Capture fidelity and browser behavior are not inferred. | Added encoded-sRGB formula, hue, powerless/gray and degeneracy branches; modern numeric/percent and legacy syntax distinctions preserved. | Formula is classic normalized sRGB; CSS extended syntax and gamut are scoped separately; Sass remains source-era Sass. | Gray at every L, HSL L distinct from WCAG luminance, hue wrapping and compatibility are consistent throughout. | HSL→Okhsl is a learning route, not necessity or numeric interchangeability; one CQ occurrence supports a partial comparison. |
| `natural-colour-system` | Ottosson account and official NCS System notation/elementary-colour explanations checked; source app image not inspected. | Corrected NCS 1050-Y90R breakdown and separated NCS notation/system, physical sample and display RGB. | Notation does not supply a screen match; measurement/conversion conditions are required for defensible matching, without claiming one mandatory table. | Removed equivalence to RGB primaries and blanket mapping-table requirement; HWB/Munsell relations remain structural comparisons. | Picker criteria and NCS edges are source-attributed; its CQ occurrence supplies partial context, not UI evidence. |
| `orthogonal-colour-properties` | Four goals and comparison table checked in complete prepared article; figure descriptions are not new empirical observations. | Separated model-parameter independence, Euclidean basis geometry and perceptual independence; corrected model ratings and loose analogy. | Subjective sRGB table only; no guarantee across users, viewing, output or display conditions. | Chroma/saturation distinctions and both new model profiles match the principles card; exactly two metadata scalars changed. | Edges to principles and chroma/saturation are editorial conceptual routes; one CQ contribution is partial to the source frame. |
| `okhsv` | Complete construction/code and accepted Slice17 Oklab/conversion premises checked; figures not inspected; helper omissions retained. | Corrected Lr and C·Lr/L axes, cusp remap, curved-top compensation, no orthogonal lightness/evenness, hue turns and Okhwb black singularity. | Source/article sRGB profile only; constant-v is not brightness; no current adoption or universal drop-in claim. | Model profile, neutral conventions and Okhwb boundaries are consistent; metadata analogy corrected exactly as authorized. | Edges to Oklab/HSV/Okhsl are limited to constructions and tradeoffs; two CQ occurrences support partial use-case guidance. |

## Source and premise anchors used for the judgments

- **P1 — picker criteria and scope:** prepared Ottosson article “What makes a good color picker?”, “Color picking before computers,” and comparison table (prompted ranges 15–43, 85–110, 745–770). Eight proposed goals conflict; tables are subjective and article-specific to sRGB.
- **P2 — classic RGB transforms:** prepared Ottosson HSL/HSV passages (106–198, 234–297); encoded-sRGB formulas and focused arithmetic below. CSS HSL syntax is separately checked against [CSS Color 4 CRD 2026-10-09 §§7–7.2](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/#the-hsl-notation) and the read-only accepted `hsl-css-syntax` endpoint.
- **P3 — gamut:** prepared article’s sRGB/gamut discussion (89, 240–276); [CSS Color 4 §14](https://www.w3.org/TR/2026/CRD-css-color-4-20261009/#gamut-mapping), inspected as the 2026-10-09 CRD. The CRD scopes its algorithms; it does not establish one universal clamp rule.
- **P4 — Okhsv/Okhwb:** prepared article construction/code (278–307, 461–511, 840–940), plus accepted Slice17 Oklab/conversion endpoints. Prepared source lines 345–425 were also read for the L_r vertical axis, C·L_r/L horizontal axis, triangular approximation and curved-top compensation. Source figures were not inspected; omitted gamut helpers were not run.
- **P5 — Okhsl:** prepared article toe and construction/code (309–323, 513–531, 659–758, 802–1117), plus accepted Slice17 Oklab/conversion endpoints. `get_Cs` receives base Oklab L. Rational fixtures are synthetic arithmetic, not measured colours.
- **P6 — HVC/NCS:** prepared article overview (53–83, 120–125, 278–297); official [NCS System explanation](https://ncscolour.com/en-eu/pages/the-system), inspected 2026-10-17. NCS notation is not screen RGB. The full Munsell owner page was unavailable; no history claims are extended.
- **P7 — HTML native input:** Drasner prepared text lines 427–429 and [HTML Living Standard Color state](https://html.spec.whatwg.org/multipage/input.html#color-state-(type=color)). It defines color-well value serialization and says `colorspace` hints at UI; it does not select widget geometry. No browser behavior test was run.
- **P8 — CIE/model chroma:** accepted Slice17 chroma-perceptual, lightness-perceptual and Oklab endpoints; CIE S 017:2020 saturation 17-22-073 and chroma 17-22-074 definitions/notes, inspected at their official entries. Saturation relates colourfulness to the area’s own brightness; chroma relates it to the brightness of a similarly illuminated achromatic reference. The notes condition interpretation on viewing/luminance and related-colour conditions; neither defines a universal model-coordinate conversion.

## Header relationship edges (pinned baseline population)

Direction follows the accepted Concept Cards guide: for `prerequisites`, **target → card** means the target supports understanding the card; for `extends`, **card → target** means the card elaborates the target; `related` and `contrasts_with` are symmetric. Each edge is assessed as a local editorial relationship; a body-list item is not presumed to state its warrant. The W groups below name the actual connecting premise, endpoint content and source anchors. Edge rows preserve raw source/field/target and do not invent a new identity.

| # | Source card | Field → target | Direction | Connecting premise / warrant |
|---:|---|---|---|---|
| 1 | `colour-gamut` | `related` → `hsl` | symmetric | warrant group W01; see exact membership and connecting reason below. |
| 2 | `colour-gamut` | `related` → `hsv` | symmetric | warrant group W01; see exact membership and connecting reason below. |
| 3 | `colour-gamut` | `related` → `okhsl` | symmetric | warrant group W02; see exact membership and connecting reason below. |
| 4 | `colour-gamut` | `related` → `okhsv` | symmetric | warrant group W02; see exact membership and connecting reason below. |
| 5 | `hsv` | `related` → `hsl` | symmetric | warrant group W03; see exact membership and connecting reason below. |
| 6 | `hsv` | `related` → `okhsv` | symmetric | warrant group W04; see exact membership and connecting reason below. |
| 7 | `hsv` | `related` → `colour-gamut` | symmetric | warrant group W01; see exact membership and connecting reason below. |
| 8 | `hsv` | `contrasts_with` → `hsl` | symmetric | warrant group W03; see exact membership and connecting reason below. |
| 9 | `hsv` | `contrasts_with` → `okhsv` | symmetric | warrant group W04; see exact membership and connecting reason below. |
| 10 | `colour-picker` | `prerequisites` → `hsl` | `hsl` → `colour-picker` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 11 | `colour-picker` | `prerequisites` → `hsv` | `hsv` → `colour-picker` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 12 | `colour-picker` | `prerequisites` → `colour-gamut` | `colour-gamut` → `colour-picker` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 13 | `colour-picker` | `related` → `okhsl` | symmetric | warrant group W06; see exact membership and connecting reason below. |
| 14 | `colour-picker` | `related` → `okhsv` | symmetric | warrant group W06; see exact membership and connecting reason below. |
| 15 | `colour-picker` | `related` → `colour-picker-design-principles` | symmetric | warrant group W07; see exact membership and connecting reason below. |
| 16 | `chroma-vs-saturation` | `prerequisites` → `hsl` | `hsl` → `chroma-vs-saturation` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 17 | `chroma-vs-saturation` | `prerequisites` → `hsv` | `hsv` → `chroma-vs-saturation` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 18 | `chroma-vs-saturation` | `related` → `orthogonal-colour-properties` | symmetric | warrant group W08; see exact membership and connecting reason below. |
| 19 | `chroma-vs-saturation` | `related` → `okhsl` | symmetric | warrant group W06; see exact membership and connecting reason below. |
| 20 | `chroma-vs-saturation` | `related` → `okhsv` | symmetric | warrant group W06; see exact membership and connecting reason below. |
| 21 | `colour-picker-design-principles` | `prerequisites` → `colour-picker` | `colour-picker` → `colour-picker-design-principles` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 22 | `colour-picker-design-principles` | `prerequisites` → `colour-gamut` | `colour-gamut` → `colour-picker-design-principles` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 23 | `colour-picker-design-principles` | `prerequisites` → `hsl` | `hsl` → `colour-picker-design-principles` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 24 | `colour-picker-design-principles` | `prerequisites` → `hsv` | `hsv` → `colour-picker-design-principles` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 25 | `colour-picker-design-principles` | `extends` → `colour-picker` | `colour-picker-design-principles` → `colour-picker` (elaboration) | warrant group W07; see exact membership and connecting reason below. |
| 26 | `colour-picker-design-principles` | `related` → `okhsl` | symmetric | warrant group W06; see exact membership and connecting reason below. |
| 27 | `colour-picker-design-principles` | `related` → `okhsv` | symmetric | warrant group W06; see exact membership and connecting reason below. |
| 28 | `colour-picker-design-principles` | `related` → `orthogonal-colour-properties` | symmetric | warrant group W07; see exact membership and connecting reason below. |
| 29 | `okhsl` | `prerequisites` → `hsl` | `hsl` → `okhsl` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 30 | `okhsl` | `prerequisites` → `colour-gamut` | `colour-gamut` → `okhsl` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 31 | `okhsl` | `prerequisites` → `orthogonal-colour-properties` | `orthogonal-colour-properties` → `okhsl` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 32 | `okhsl` | `extends` → `hsl` | `okhsl` → `hsl` (elaboration) | warrant group W14; see exact membership and connecting reason below. |
| 33 | `okhsl` | `related` → `okhsv` | symmetric | warrant group W06; see exact membership and connecting reason below. |
| 34 | `okhsl` | `related` → `colour-picker-design-principles` | symmetric | warrant group W06; see exact membership and connecting reason below. |
| 35 | `okhsl` | `contrasts_with` → `hsl` | symmetric | warrant group W09; see exact membership and connecting reason below. |
| 36 | `okhsl` | `contrasts_with` → `okhsv` | symmetric | warrant group W21; see exact membership and connecting reason below. |
| 37 | `munsell-colour-system` | `related` → `natural-colour-system` | symmetric | warrant group W10; see exact membership and connecting reason below. |
| 38 | `munsell-colour-system` | `related` → `hsl` | symmetric | warrant group W11; see exact membership and connecting reason below. |
| 39 | `munsell-colour-system` | `related` → `okhsl` | symmetric | warrant group W12; see exact membership and connecting reason below. |
| 40 | `munsell-colour-system` | `contrasts_with` → `natural-colour-system` | symmetric | warrant group W10; see exact membership and connecting reason below. |
| 41 | `hsl` | `related` → `hsv` | symmetric | warrant group W03; see exact membership and connecting reason below. |
| 42 | `hsl` | `related` → `hsl-css-syntax` | symmetric | warrant group W13; see exact membership and connecting reason below. |
| 43 | `hsl` | `related` → `okhsl` | symmetric | warrant group W14; see exact membership and connecting reason below. |
| 44 | `hsl` | `contrasts_with` → `hsv` | symmetric | warrant group W03; see exact membership and connecting reason below. |
| 45 | `hsl` | `contrasts_with` → `okhsl` | symmetric | warrant group W14; see exact membership and connecting reason below. |
| 46 | `natural-colour-system` | `related` → `munsell-colour-system` | symmetric | warrant group W10; see exact membership and connecting reason below. |
| 47 | `natural-colour-system` | `related` → `colour-picker-design-principles` | symmetric | warrant group W16; see exact membership and connecting reason below. |
| 48 | `natural-colour-system` | `related` → `hsv` | symmetric | warrant group W17; see exact membership and connecting reason below. |
| 49 | `natural-colour-system` | `contrasts_with` → `munsell-colour-system` | symmetric | warrant group W10; see exact membership and connecting reason below. |
| 50 | `natural-colour-system` | `contrasts_with` → `hsl` | symmetric | warrant group W17; see exact membership and connecting reason below. |
| 51 | `natural-colour-system` | `contrasts_with` → `hsv` | symmetric | warrant group W17; see exact membership and connecting reason below. |
| 52 | `orthogonal-colour-properties` | `prerequisites` → `colour-gamut` | `colour-gamut` → `orthogonal-colour-properties` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 53 | `orthogonal-colour-properties` | `prerequisites` → `hsl` | `hsl` → `orthogonal-colour-properties` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 54 | `orthogonal-colour-properties` | `prerequisites` → `hsv` | `hsv` → `orthogonal-colour-properties` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 55 | `orthogonal-colour-properties` | `extends` → `colour-picker-design-principles` | `orthogonal-colour-properties` → `colour-picker-design-principles` (elaboration) | warrant group W19; see exact membership and connecting reason below. |
| 56 | `orthogonal-colour-properties` | `related` → `okhsl` | symmetric | warrant group W06; see exact membership and connecting reason below. |
| 57 | `orthogonal-colour-properties` | `related` → `okhsv` | symmetric | warrant group W06; see exact membership and connecting reason below. |
| 58 | `orthogonal-colour-properties` | `related` → `chroma-vs-saturation` | symmetric | warrant group W08; see exact membership and connecting reason below. |
| 59 | `okhsv` | `prerequisites` → `hsv` | `hsv` → `okhsv` (understanding route) | warrant group W04; see exact membership and connecting reason below. |
| 60 | `okhsv` | `prerequisites` → `colour-gamut` | `colour-gamut` → `okhsv` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 61 | `okhsv` | `prerequisites` → `orthogonal-colour-properties` | `orthogonal-colour-properties` → `okhsv` (understanding route) | warrant group W05; see exact membership and connecting reason below. |
| 62 | `okhsv` | `extends` → `hsv` | `okhsv` → `hsv` (elaboration) | warrant group W04; see exact membership and connecting reason below. |
| 63 | `okhsv` | `related` → `okhsl` | symmetric | warrant group W06; see exact membership and connecting reason below. |
| 64 | `okhsv` | `related` → `colour-picker-design-principles` | symmetric | warrant group W20; see exact membership and connecting reason below. |
| 65 | `okhsv` | `contrasts_with` → `hsv` | symmetric | warrant group W04; see exact membership and connecting reason below. |
| 66 | `okhsv` | `contrasts_with` → `okhsl` | symmetric | warrant group W21; see exact membership and connecting reason below. |

**Recount:** 66 header edges: 18 `prerequisites`, 4 `extends`, 32 `related`, 12 `contrasts_with`. The sole header endpoint outside the cohort is `hsl-css-syntax`, read in full as the accepted endpoint; its normalization, notation and legacy/current syntax passages ground only the HSL↔CSS notation relationship, not HSL↔Okhsl numeric equivalence.

### Grouped connecting warrants

Each table row points to exactly one group below. Membership lists are derived from the row references and enumerate every tuple exactly once. These are local editorial graph judgments grounded in inspected endpoint statements, not metadata quotations or claims that every source literally asserts a graph edge.

- **W01 — rows 1, 2, 7:** Rows 1, 2 and 7 connect the `colour-gamut` card to the HSL/HSV cards because its RGB gamut is the representable set for a specified RGB definition and HSL/HSV formulas reparameterize specified encoded RGB (prepared picker article 106–178). This is an editorial model/gamut association, not a literal HSL/HSV Related bullet and not a claim that all RGB definitions share one gamut.
- **W02 — rows 3, 4:** Rows 3 and 4 connect the gamut card with Okhsl/Okhsv because the prepared article compares those constructions for an sRGB picker (284–307, 745–770) and the gamut card defines representable sets. This is scoped to that named target; it does not generalize the recipes to every gamut.
- **W03 — rows 5, 8, 41, 44:** Rows 5, 8, 41 and 44 connect HSL and HSV as related/contrasting RGB transformations. Their hue calculation is shared in the classic formulas, but their S and third-coordinate definitions differ; for encoded RGB(.8,.2,.2), HSV S=.75,V=.8 and HSL S=.6,L=.5. The link is a formula-level comparison, not interchangeable coordinates.
- **W04 — rows 6, 9, 59, 62, 65:** Rows 6, 9, 59, 62 and 65 link HSV and Okhsv as a learning/contrast pair; row59 is an understanding route from HSV to the Okhsv explanation. HSV reparameterizes encoded RGB; Okhsv derives hue/chroma through Oklab-based coordinates and remaps an sRGB cross-section (prepared article 345–425, 461–511). Familiar value-like controls and attributed tradeoffs do not establish numerical compatibility or guaranteed perceived behavior.
- **W05 — rows 10, 11, 12, 16, 17, 21, 22, 23, 24, 29, 30, 31, 52, 53, 54, 60, 61:** Rows 10–12, 16–17, 21–24, 29–31, 52–54, 60 and 61 are learning routes: their targets use classic HSL/HSV definitions, a specified gamut, or the article’s four orthogonality criteria as background. These are helpful explanatory dependencies, not strict prerequisites or mathematical requirements. For Okhsv geometry, prepared lines 345–425 apply; for HSL/HSV formulas, lines 106–178 apply.
- **W06 — rows 13, 14, 19, 20, 26, 27, 33, 34, 56, 57, 63:** Rows 13–14, 19–20, 26–27, 33–34, 56–57 and 63 connect the picker comparison to model-specific Okhsl/Okhsv constructions. The article’s later table compares their profiles (745–770), while the chroma/orthogonality cards discuss their controls. The shared model family supports navigation; it does not assert equal values or identical tradeoffs.
- **W07 — rows 15, 25, 28:** Rows 15, 25 and 28 connect the colour-picker concept, its principles elaboration and orthogonality subset. The article supplies eight proposed picker criteria; the principles card names them; orthogonal-colour-properties treats four as a subset. This is an editorial teaching structure, not a universal quality standard or widget/accessibility claim.
- **W08 — rows 18, 58:** Rows 18 and 58 connect chroma/saturation definitions with the orthogonality criteria. The former distinguishes CIE appearance terms from model parameters; the latter lists orthogonal chroma and orthogonal saturation separately. This explains the conceptual link without claiming either criterion is empirically achieved.
- **W09 — rows 35:** Row 35 compares Okhsl with HSLuv only as the prepared article’s attributed mapping tradeoff. It is not an independently measured claim about uniformity, smoothness or user experience.
- **W10 — rows 37, 40, 46, 49:** Rows 37, 40, 46 and 49 connect Munsell and NCS as colour-ordering systems described through different constructions: HVC notation versus resemblance to elementary colours. Prepared text and the official NCS system explanation support this bounded comparison; the unavailable full Munsell-owner material prevents extending detailed historical or standardization claims.
- **W11 — rows 38:** Row 38 preserves Drasner’s attributed conceptual comparison between HSL and Munsell. It supports an association only; it does not establish direct historical or mathematical derivation.
- **W12 — rows 39:** Row 39 is an indirect construction-context link: the prepared article says Oklab has a construction similar to Munsell, and Okhsl derives/remaps Oklab coordinates. This does not establish that Okhsl derives from Munsell; the relation is editorial and mediated by Oklab.
- **W13 — rows 42:** Row 42 connects the HSL coordinate card to the accepted `hsl-css-syntax` endpoint: the endpoint defines CSS HSL notation, normalization and current/legacy syntax, while the card gives classic coordinates and scopes CSS syntax separately. This is a notation/use relationship, not historical Munsell/NCS support or numeric equivalence with Okhsl.
- **W14 — rows 32, 43, 45:** Rows 32, 43 and 45 connect HSL and Okhsl through familiar hue/saturation/lightness-like labels and picker use, while their constructions differ: classic encoded-RGB formulas versus an Oklab-derived, remapped model (prepared article 106–178, 345–425). This supports learning/comparison only, not matching values.
- **W16 — rows 47:** Row 47 connects NCS with the article’s picker-design criteria because its first comparison table includes an NCS profile. It records the source-specific evaluation frame, not an NCS widget or accessibility assessment.
- **W17 — rows 48, 50, 51:** Rows 48, 50 and 51 contrast NCS with HSV/HSL. The article attributes structural similarity for HSV/NCS, but NCS is perceptual notation while HSV/HSL are RGB transformations; HSL/HSV do not thereby share NCS construction or appearance semantics.
- **W19 — rows 55:** Row 55 is an explicit elaboration: the four orthogonality goals are a subset of the article’s eight proposed picker criteria. It is an editorial decomposition of the same framework and does not establish perceptual independence.
- **W20 — rows 64:** Row 64 links Okhsv with the principles card because the later picker comparison table rates Okhsv against those criteria (prepared article 745–770). This is a source-attributed profile, not an independent rating or deployed-picker result.
- **W21 — rows 36, 66:** Rows 36 and 66 are distinct sibling comparisons: row36 compares Okhsl and Okhsv under the article’s second table; row66 does the reciprocal comparison. Their mappings and source-reported profiles differ, but this does not imply numeric equivalence or a universal perceptual ranking.

## Body relationship statement joins

The predecessor denominator is **65** body-list occurrences (excluding headings and confusion entries). Every occurrence is joined below by card, subsection and label. “Retained” means unchanged text; “rephrased” means the endpoint remains with bounded meaning; “removed” means an unsupported/overbroad assertion no longer appears. These are local editorial relationships, not claims that Ottosson or Drasner asserted each graph edge.

| # | Predecessor statement (label — claim) | Final disposition and join |
|---:|---|---|
| 1 | `colour-gamut` / Builds Upon: **RGB colour model** — sRGB is the reference standard that defines the gamut | | warrant group W01; see exact membership and connecting reason below. |
| 2 | `colour-gamut` / Enables: **Colour picker design** — The gamut shape determines the complexity of picker design | | warrant group W01; see exact membership and connecting reason below. |
| 3 | `colour-gamut` / Enables: **Okhsl / Okhsv** — Both spaces are designed to map the sRGB gamut to a cylinder | | warrant group W02; see exact membership and connecting reason below. |
| 4 | `colour-gamut` / Related: **Colour spaces** — Each colour space represents the gamut differently | | warrant group W02; see exact membership and connecting reason below. |
| 5 | `hsv` / Builds Upon: **sRGB colour model** — HSV is a coordinate transformation of sRGB | | warrant group W03; see exact membership and connecting reason below. |
| 6 | `hsv` / Enables: **Okhsv** — Okhsv was designed as a perceptually-improved replacement for HSV while preserving its cylindrical structure | | warrant group W04; see exact membership and connecting reason below. |
| 7 | `hsv` / Enables: **HWB colour model** — HSV can be transformed to HWB (hue, whiteness, blackness) form, which is structurally similar to NCS | | warrant group W01; see exact membership and connecting reason below. |
| 8 | `hsv` / Related: **HSL** — Sibling model from the same 1978 paper; shares the hue calculation | | warrant group W03; see exact membership and connecting reason below. |
| 9 | `hsv` / Related: **Natural Colour System (NCS)** — Ottosson notes "HSV is quite similar to the Natural Color System in its structure" | | warrant group W04; see exact membership and connecting reason below. |
| 10 | `hsv` / Contrasts With: **Okhsv** — Okhsv corrects HSV's perceptual distortions using Oklab while maintaining cylindrical geometry | | warrant group W05; see exact membership and connecting reason below. |
| 11 | `hsv` / Contrasts With: **HSL** — Different lightness axis: HSL places grey at L=50%, S=0; HSV has grey at V=any, S=0 | | warrant group W05; see exact membership and connecting reason below. |
| 12 | `colour-picker` / Builds Upon: **HSL / HSV** — Foundational colour spaces that nearly all common pickers use | | warrant group W05; see exact membership and connecting reason below. |
| 13 | `colour-picker` / Enables: **Okhsl / Okhsv** — Purpose-built to be drop-in improvements for HSL/HSV pickers | | warrant group W06; see exact membership and connecting reason below. |
| 14 | `colour-picker` / Related: **Colour picker design principles** — The 8-property framework Ottosson articulates for evaluating picker quality | | warrant group W06; see exact membership and connecting reason below. |
| 15 | `colour-picker` / Related: **NCS colour system** — An alternative pre-digital colour ordering system also used in picker UIs | | warrant group W07; see exact membership and connecting reason below. |
| 16 | `colour-picker` / Contrasts With: **Numeric colour input** — Raw numeric entry (hex, rgb()) lacks the affordance of spatial navigation | | warrant group W05; see exact membership and connecting reason below. |
| 17 | `chroma-vs-saturation` / Builds Upon: **Perceptual colour science** — The distinction is defined by how the visual system processes colour signals | | warrant group W05; see exact membership and connecting reason below. |
| 18 | `chroma-vs-saturation` / Enables: **Orthogonal colour properties** — Recognising the distinction enables understanding why Orthogonal Chroma and Orthogonal Saturation are separate goals | | warrant group W08; see exact membership and connecting reason below. |
| 19 | `chroma-vs-saturation` / Enables: **Okhsl design** — Okhsl's saturation parameter is designed to be smoothly varying in a way that HSL's is not | | warrant group W06; see exact membership and connecting reason below. |
| 20 | `chroma-vs-saturation` / Related: **Munsell colour system** — Uses Chroma (not Saturation) as an independent dimension | | warrant group W06; see exact membership and connecting reason below. |
| 21 | `chroma-vs-saturation` / Related: **Okhsl / Okhsv** — Both provide saturation parameters that are defined carefully to avoid confusion | | warrant group W05; see exact membership and connecting reason below. |
| 22 | `colour-picker-design-principles` / Builds Upon: **Colour gamut** — The geometrical shape criterion is gamut-relative | | warrant group W05; see exact membership and connecting reason below. |
| 23 | `colour-picker-design-principles` / Builds Upon: **Perceptual colour science** — The orthogonality criteria depend on perceptual measurement | | warrant group W05; see exact membership and connecting reason below. |
| 24 | `colour-picker-design-principles` / Enables: **Okhsl / Okhsv design** — These new spaces were designed explicitly against this framework | | warrant group W05; see exact membership and connecting reason below. |
| 25 | `colour-picker-design-principles` / Enables: **Comparative colour space evaluation** — Provides vocabulary and criteria for systematic comparison | | warrant group W07; see exact membership and connecting reason below. |
| 26 | `colour-picker-design-principles` / Related: **Orthogonal colour properties** — The four orthogonality properties form a subset of this framework | | warrant group W06; see exact membership and connecting reason below. |
| 27 | `colour-picker-design-principles` / Contrasts With: **Naive simplicity** — HSL and HSV were designed for computational simplicity, not against this principled framework | | warrant group W06; see exact membership and connecting reason below. |
| 28 | `okhsl` / Builds Upon: **Oklab** — Okhsl derives its hue and lightness from Oklab coordinates | | warrant group W07; see exact membership and connecting reason below. |
| 29 | `okhsl` / Builds Upon: **HSL** — Okhsl was designed as a structural successor to HSL for picker use | | warrant group W05; see exact membership and connecting reason below. |
| 30 | `okhsl` / Enables: **Perceptually uniform colour pickers** — Okhsl enables pickers where lightness feels consistent across hues | | warrant group W05; see exact membership and connecting reason below. |
| 31 | `okhsl` / Enables: **Accessible colour palette generation** — Uniform lightness enables all-hue palettes with consistent perceived contrast | | warrant group W05; see exact membership and connecting reason below. |
| 32 | `okhsl` / Related: **Okhsv** — Sibling space optimised for a different set of tradeoffs (Value-based rather than Lightness-based) | | warrant group W14; see exact membership and connecting reason below. |
| 33 | `okhsl` / Contrasts With: **HSL** — HSL has non-orthogonal lightness and hue; Okhsl corrects both | | warrant group W06; see exact membership and connecting reason below. |
| 34 | `okhsl` / Contrasts With: **Okhsv** — Okhsv preserves maximum chroma at the edge (good for finding vivid colours); Okhsl prioritises orthogonal lightness (good for uniform brightness) | | warrant group W06; see exact membership and connecting reason below. |
| 35 | `okhsl` / Contrasts With: **HSLuv** — HSLuv also attempts uniform lightness but fails on smooth saturation variation; Okhsl is smoother | | warrant group W09; see exact membership and connecting reason below. |
| 36 | `munsell-colour-system` / Builds Upon: **Perceptual colour research** — Munsell derived dimensions from perceptual experiments | | warrant group W21; see exact membership and connecting reason below. |
| 37 | `munsell-colour-system` / Enables: **CIELab, Oklab** — Modern perceptual spaces directly continue Munsell's approach with more rigorous mathematical grounding | | warrant group W10; see exact membership and connecting reason below. |
| 38 | `munsell-colour-system` / Enables: **HSL** — Drasner notes HSL's three-channel structure traces to Munsell's conceptual framework | | warrant group W11; see exact membership and connecting reason below. |
| 39 | `munsell-colour-system` / Related: **Natural Colour System (NCS)** — A contemporary perceptual system using different principles | | warrant group W12; see exact membership and connecting reason below. |
| 40 | `munsell-colour-system` / Related: **Oklab** — Ottosson's own colour space, which follows "very similar construction" to Munsell | | warrant group W10; see exact membership and connecting reason below. |
| 41 | `munsell-colour-system` / Contrasts With: **NCS** — Munsell uses independent dimensions; NCS uses resemblance to elementary colours | | warrant group W03; see exact membership and connecting reason below. |
| 42 | `munsell-colour-system` / Contrasts With: **HSL/HSV** — These are simple RGB transformations, not perceptually uniform in the way Munsell is | | warrant group W13; see exact membership and connecting reason below. |
| 43 | `hsl` / Builds Upon: **sRGB colour model** — HSL is a transformation of sRGB coordinates | | warrant group W14; see exact membership and connecting reason below. |
| 44 | `hsl` / Enables: **Okhsl** — Okhsl was built to improve upon HSL's perceptual shortcomings while retaining its cylindrical structure | | warrant group W03; see exact membership and connecting reason below. |
| 45 | `hsl` / Enables: **Generative colour** — Predictable 0–360 hue cycle enables looping colour sequences | | warrant group W14; see exact membership and connecting reason below. |
| 46 | `hsl` / Related: **HSV** — Sibling model from the same 1978 paper; shares the same hue calculation | | warrant group W10; see exact membership and connecting reason below. |
| 47 | `hsl` / Related: **Munsell colour system** — Drasner compares HSL with Munsell; the prepared passage does not establish a direct historical derivation or mathematical equivalence | | warrant group W16; see exact membership and connecting reason below. |
| 48 | `hsl` / Contrasts With: **Okhsl** — Okhsl corrects HSL's lightness and hue distortions using Oklab | | warrant group W17; see exact membership and connecting reason below. |
| 49 | `hsl` / Contrasts With: **HSV** — Different arrangement of axes; HSL places white/black at L extremes whereas HSV places white at V=1, S=0 | | warrant group W10; see exact membership and connecting reason below. |
| 50 | `natural-colour-system` / Builds Upon: **Perceptual colour research** — NCS was derived from experiments on human colour appearance | | warrant group W17; see exact membership and connecting reason below. |
| 51 | `natural-colour-system` / Related: **Munsell colour system** — Both are perceptual colour ordering systems; NCS uses similarity to elementaries while Munsell uses independent dimensions (Hue, Chroma, Value) | | warrant group W17; see exact membership and connecting reason below. |
| 52 | `natural-colour-system` / Related: **HWB colour model** — HWB (hue, whiteness, blackness) is structurally similar to NCS but based on RGB rather than perception | | warrant group W05; see exact membership and connecting reason below. |
| 53 | `natural-colour-system` / Contrasts With: **Munsell colour system** — "The Munsell Color System... colors are described with three parameters, designed to match the perceived appearance of colors: Hue, Chroma and Value. The parameters are designed to be independent and each have a uniform scale." NCS uses similarity/resemblance framing rather than independent orthogonal parameters. | | warrant group W05; see exact membership and connecting reason below. |
| 54 | `natural-colour-system` / Contrasts With: **HSV / HWB** — NCS is derived from perceptual research; HSV/HWB from a simple RGB transformation | | warrant group W05; see exact membership and connecting reason below. |
| 55 | `orthogonal-colour-properties` / Builds Upon: **Perceptual colour science** — Orthogonality is defined in perceptual, not numeric, terms | | warrant group W19; see exact membership and connecting reason below. |
| 56 | `orthogonal-colour-properties` / Enables: **Okhsl / Okhsv design** — Both spaces prioritise Orthogonal Hue, with Okhsl additionally achieving Orthogonal Lightness | | warrant group W06; see exact membership and connecting reason below. |
| 57 | `orthogonal-colour-properties` / Related: **Colour picker design principles** — Orthogonality is a subset of the full eight-property framework | | warrant group W06; see exact membership and connecting reason below. |
| 58 | `orthogonal-colour-properties` / Related: **Chroma vs saturation** — The distinction matters because Orthogonal Chroma and Orthogonal Saturation are different properties | | warrant group W08; see exact membership and connecting reason below. |
| 59 | `okhsv` / Builds Upon: **Oklab** — Okhsv derives hue from Oklab's perceptually uniform hue angle | | warrant group W04; see exact membership and connecting reason below. |
| 60 | `okhsv` / Builds Upon: **HSV** — Okhsv is a structural drop-in for HSV, retaining its shape and conventions | | warrant group W05; see exact membership and connecting reason below. |
| 61 | `okhsv` / Enables: **Perceptual HSV-style pickers** — Enables pickers that feel like HSV but with correct hue representation | | warrant group W05; see exact membership and connecting reason below. |
| 62 | `okhsv` / Related: **Okhsl** — Sibling space prioritising orthogonal lightness instead of max-chroma-at-edge | | warrant group W04; see exact membership and connecting reason below. |
| 63 | `okhsv` / Related: **Okhwb** — A whiteness/blackness reparameterisation of Okhsv, analogous to HWB for HSV | | warrant group W06; see exact membership and connecting reason below. |
| 64 | `okhsv` / Contrasts With: **HSV** — HSV has severe hue distortions (purple shift in deep blues); Okhsv corrects these | | warrant group W20; see exact membership and connecting reason below. |
| 65 | `okhsv` / Contrasts With: **Okhsl** — Okhsl achieves orthogonal lightness (uniform brightness across hues at constant L); Okhsv does not | | warrant group W04; see exact membership and connecting reason below. |

### New final body statements with no predecessor label join

- `hsv` / Builds Upon: **RGB colour model** — The classic equations re-parameterize a specified RGB representation; the formulas in this card are for encoded sRGB.
- `colour-picker-design-principles` / Enables: **Comparative colour-space evaluation** — The criteria offer a source-specific vocabulary; they are not a published universal standard.
- `colour-picker-design-principles` / Contrasts With: **Unqualified simplicity claims** — The article describes tradeoffs among geometry and perceptual goals; no general historical claim about why HSL/HSV were designed is made here.
- `okhsl` / Enables: **Picker candidates** — Its stated coordinate tradeoffs can inform a candidate control; output and interaction still need task-specific review.
- `okhsl` / Enables: **Palette candidates** — It can generate coordinates for evaluation, but equal lightness values do not certify contrast or accessibility.
- `okhsv` / Enables: **Picker candidates** — Can inform an Oklab-derived sRGB picker candidate; host controls, output checks and accessibility require separate assessment.

## Competency-question occurrences and bounded answers

### “What makes a colour picker perceptually well-designed?” — 9 occurrences

Header occurrences: `colour-gamut`, `colour-picker`, `chroma-vs-saturation`, `colour-picker-design-principles`, `okhsl`, `munsell-colour-system`, `natural-colour-system`, `orthogonal-colour-properties`, `okhsv`.

**Required answer components and body coverage:** task/gamut and widget distinction (`colour-picker`); eight proposed criteria, conflict and subjective scope (`colour-picker-design-principles`); representable set/sRGB limits (`colour-gamut`); model formulas and differing saturation/lightness/value (`hsl`, `hsv`, `chroma-vs-saturation`); Okhsl/Okhsv profiles (`okhsl`, `okhsv`, `orthogonal-colour-properties`); attributed HVC/NCS context (`munsell-colour-system`, `natural-colour-system`). **Bounded attempt:** within Ottosson’s sRGB comparison, a picker choice weighs the eight named, sometimes conflicting goals and the selected task/gamut; ratings are subjective. Widget/accessibility, actual rendered output and user evidence remain necessary for a deployed interface. **Coverage:** partial for general perceptual quality; adequate only as the article-scoped comparison.

### “What distinguishes Okhsl from Okhsv, and when would you use each?” — 4 occurrences

Header occurrences: `hsv`, `okhsl`, `hsl`, `okhsv`.

**Required answer components and body coverage:** distinct coordinate pipelines, lightness/value interpretation, neutral boundaries, gamut construction, source table profiles and task-dependent tradeoff (`hsl`, `hsv`, `okhsl`, `okhsv`). **Bounded attempt:** Okhsl uses toe-mapped Oklab L and a three-reference rational saturation mapping; Okhsv remaps an Oklab-derived hue cross-section to a value-like control and retains the article’s cusp-at-edge aim. The source rates Okhsv no for Orthogonal Lightness and both new spaces no for Varies Evenly. Choosing depends on task/destination; numbers are not interchangeable, and no accessibility or universal preference follows. **Coverage:** partial for actual selection/use because ratings are subjective and no deployed task/host was tested.

### “What distinguishes chroma from saturation in a colour space?” — 2 occurrences

Header occurrences: `chroma-vs-saturation`, `orthogonal-colour-properties`.

**Required answer components and body coverage:** exact CIE appearance distinction and viewing/reference conditions, model coordinate versus appearance term, HSL/HSV formulas, and separate orthogonal chroma/saturation goals (`chroma-vs-saturation`, `orthogonal-colour-properties`). **Bounded attempt:** CIE saturation relates colourfulness to an area’s own brightness; CIE chroma uses the brightness of a similarly illuminated area appearing grey, white or highly transmitting. The entries’ notes qualify viewing/luminance and related-colour conditions. Oklab C=hypot(a,b) is an Oklab coordinate. Classic encoded-sRGB formulas give HSL S=Δ/(1−|2L−1|) off gray and HSV S=Δ/M for M>0; neither is a universal C/L law or direct CIE appearance measure. **Coverage:** answerable within these named definitions and formulas; no universal cross-model conversion or appearance prediction is supported.

The full eleven bodies were read for embedded questions and question-bearing confusion/procedure text, not just `?` characters. No additional independently phrased body CQ was found; headings/quoted source titles and the three frontmatter texts account for observed question marks.


## Focused arithmetic and boundary witnesses

Arithmetic used IEEE-754 double precision and tolerance `1e-9`. These checks validate the stated equations and examples only; they do not run omitted picker helper code or establish perceptual behavior.

- **Encoded sRGB HSL/HSV:** `(.8,.2,.2)` gives M=.8, m=.2, Δ=.6. HSV (h=0°, S=.75, V=.8); HSL (h=0°, S=.6, L=.5). For gray `(.5,.5,.5)`, both S=0 and hue is powerless. A second gray `(.2,.2,.2)` gives S=0, HSV V=.2 and HSL L=.2.
- **Hue units:** `.25` turns is 90°; one turn is 360° modulo a full turn. Hue normalization applies only for non-neutral C>0 in Okhsl/Okhsv; neutral h=0 is a storage convention.
- **Toe/inverse:** k1=.206, k2=.03, k3=(1+k1)/(1+k2)=1.170873786407767; `toe(L)=(k3L−k1+sqrt((k3L−k1)^2+4k2k3L))/2`, `toe_inv(l)=l(l+k1)/(k3(l+k2))`. `toe(0)=0`, `toe(1)=1`, `toe(.5)=.421140562608970` (3.03e-14 from rounded prompt value); `toe_inv(.5)=.568838198942395`. Round-trips: 0→0→0, .125→.042843442132679→.125, .5→.421140562608970→.5, 1→1→1; maximum absolute error 1.11e-16.
- **Three-reference rational map (synthetic, not measured):** C0=.1, Cmid=.12, Cmax=.2; source break at s=.8. Source map/inverse reproduce (s,C): 0→0, .4→.048, .8→.12, .9→.1488, 1→.2. Inverse recovers each s. Linear s·Cmax gives .16 at .8, not .12. C0 is initial slope while C(0)=0.
- **Neutral/black/white:** Δ=0 gives S=0 and no hue measurement. Exact Okhsl/Okhsv neutral recipes use s=0 and l/v=toe(L) without a/C normalization or cusp calls; canonical black (h=0,s=0,l/v=0), white (0,0,1) are explicit serialization conventions, not unique inverse coordinates. Near-neutral classification needs a stated tolerance. HSL denominator at L=0/1 is bypassed by Δ=0 branch.
- **Okhwb:** w=(1−s)v,b=1−v. Example s=.4,v=.5 gives w=.3,b=.5 and inverse returns s=.4,v=.5. At black s=0,v=0 gives w=0,b=1; inverse denominator 1−b=0, so inverse is undefined. Direct algebra only; helper not run.

## Exact metadata exceptions and preservation

- `okhsl`, `okhsv`, `orthogonal-colour-properties`: exactly six scalars changed: each `rosetta_stone[0].rating` `rigorous`→`loose`; each existing note replaced with: “Numeric colour-model parameters and equal frequency ratios/Euclidean basis vectors do not establish equal visual or auditory differences or perceptual independence.” Domain/concept remain unchanged.
- `colour-picker`: sole `css_implementation[0]` with property `input[type=color]`, HTML example and baseline support removed; field remains `css_implementation: []`. Illustrative HTML remains in body.
- Every other frontmatter value, order, nested list/type/null distinction, identity, extraction-confidence value and source citation is preserved. Literal Source Reference sections and body headings are preserved.
- Population replay against source pin: 233 card paths/identities; 11 target bodies/frontmatter in the authorized card set; 222 other card bodies byte-identical; all 161 prepared source files byte-identical. No guide, helper, schema, package-list or other source path changes. Pre-existing untracked `knowledge/lfe/` and `knowledge/fennel/` work is preserved.
- Owning skill metadata changed only 1.0.14→1.0.15; history entry appended using existing format. Validation/package evidence follows the source commit.

## Validation and commit evidence

- `make help`: passed; required target names confirmed before execution.
- `make check-skills`: passed; 24 source skills, 0 hard violations. It reported 18 descriptions above the 300-character editorial target; the visual-design-system description is 360 characters. This is a warning, not a gate failure.
- `make check-skill-versions`: first attempt under the default sandbox failed during package staging because writes beneath ignored `target/skills` were denied; the source scan itself reported 24 skills and 0 errors. Re-run with approved escalation passed: 24 source skills, 24 packages, 0 errors.
- `make check-package-paths`: passed, exit 0. 24 ZIPs and 388 Markdown files scanned; 0 hard failures, 596 warnings, 3 explicit exceptions, 684 skipped external URLs. Warnings are repository-wide categories (repo-only/provenance 170, parser false positive 154, bundled-reference 124, sibling-skill-reference 97, example-project path 28, source-clone-reference 23); the gate does not establish which warnings are newly introduced.
- Source commit: `7b20ccc3a701` (`Clarify colour picker tradeoffs in design cards`), exactly the 13 authorized paths, with both required co-author trailers. `git diff --check` passed before commit.
- Fresh committed-tree `make design`: passed; visual-design-system bundle contains 8 Markdown members.
- Independent ZIP replay compared each of those 8 Markdown members byte-for-byte with the corresponding file at source commit `7b20ccc3a701`; 8/8 passed. Archive directories are not counted as Markdown members.
- Unrelated untracked source work under `knowledge/lfe/` and `knowledge/fennel/` remains untouched.

## Iteration01 intake, correction and verification

### Assignment readback and current pins

- Current assignment: `cc-prompt-iteration01.md`, issued by planning commit `c5670897d904c4d5dcb44902dd4928d6882cfe23`; predecessor `5d8f3a9ffed74dbf69255956e450b855a10a3ed6`. Initial `cc-prompt.md` and CDC review remain preserved.
- Assigned source pin: `c9d98a3ec3d0a24c30a18431d7aeaa13f6451872`; reviewed design candidate `7b20ccc3a7019cfad6f238522314ce8ab70e0a35`. The source checkout is currently at `c5e743abb40db2f14b9332cea635a30f8b8a8d5b`; its only committed delta from c9 is an unrelated `README.md` deletion. The entire design tree remains byte-identical to c9 before this five-body working diff. It was preserved in place; no reset/rebase. Pre-existing untracked source `knowledge/lfe/` is untouched. Planning worktree is at the issuing commit and clean before these authorized record edits; no untracked project14 path was present at this intake.
- Required reading completed in prompt order: current planning AGENTS and source AGENTS; full collaboration-framework entrypoint (553 lines); project-management entrypoint and full guides README (184 lines); required project-management guide02/03 sections, engineering-methods guide07 intake, work-verification guide05 correction-review section; Project10/Arc02 active bodies and criterion/status rows; full Slice18 plan/ledger/prompt/CDC review/closing report; full Concept Cards entrypoint and guides05/06, Visual Design entrypoint and colour guide; all eleven cohort cards, accepted HSL CSS syntax endpoint, existing batch record; prepared Okhsv/Okhsl article sections 106–178, 284–307, 345–425, 745–770; official CIE saturation/chroma definitions and notes; CSS Color Module Level 4 Candidate Recommendation Draft title/status dated 2026-10-09. Earlier output truncations were recovered in bounded reads. Prepared article SHA256 remains `227d62385a8ca4dfa77e9f5a10d55c9bd8d1c2f29d8964f59a1059bfb67d5d19`. The first comparison table's columns are HSV, HSL, HSLuv, Lab-like and NCS; the later table is Okhsv/Okhsl. The CIE terms and Oklab/HSL/HSV coordinates are separate kinds of definition. Figures themselves were not inspected.

**Contract readback:** this is a five-card body correction to F01–F03. It repairs repeated HSL/HSV teaching and preserves the source-attributed blue-shift example without assigning hue to a neutral; restores the actual CIE chroma/saturation reference distinction; reports the correct comparison-table families and Okhsv scaled axes/curved-top compensation; and supplies endpoint-specific reasons for every preserved graph tuple. No metadata, identity, order, heading, literal Source Reference, relationship header, body relationship count or CQ membership may change. The CIE definitions do not yield a universal equation for Oklab C or RGB-model saturation. The article's table remains a subjective, sRGB-scoped comparison, and numeric controls do not guarantee appearance. S18-03/04 remain CDC accepted subject to this correction's preservation/applicability replay; S18-01/02 are still proposals for CDC. No closure, successor, push or publication.

### F01–F03 delivery and changed body joins

- **F01:** `hsv` now retains the attributed deep-blue saturation-shift example, states hue is powerless at Δ=0, replaces the neutral comparison with encoded RGB(.8,.2,.2), and aligns Common Applications and Common Confusions with Δ/M and HSL's Δ/(1−|2L−1|). `okhsv` preserves fixed numeric h/s controls as a candidate-exploration task while disclaiming perceived-hue/saturation or specified-brightness guarantees. The arithmetic outputs are listed below.
- **F02:** `colour-gamut` describes vertical L_r, horizontal C·L_r/L, triangular approximation and curved-top compensation as source-described construction, with figures uninspected; its note now identifies the CSS Color Module Level 4 Candidate Recommendation Draft (2026-10-09). Principles names the first table's five profiles and later Okhsv/Okhsl table; Munsell remains context only. Chroma/saturation defines CIE saturation/chroma in Quick Definition, Core and Key Properties, preserves conditions, and separates those terms from Oklab C and HSL/HSV S.
- **F03:** all 66 table rows now resolve to exact warrant groups W01–W23. Every group lists its exact row members, endpoint-level connecting premise and whether the link is a learning/editorial association, source-attributed comparison or scoped contrast. Row42 is specifically grounded in the accepted CSS syntax endpoint. No member is treated as supported solely because its endpoint names resemble another.
- **Body join #11:** changed from a neutral-axis assertion to the final chromatic witness and its gray equality. Other predecessor joins retain their prior dispositions. No relationship-list statement was added or removed; the final statement count remains 65. The six previously recorded unjoined final statements are retained and remain six.
- **CQ 2/2 (“chroma from saturation”):** answer components now explicitly include both CIE reference relations and their viewing conditions, Oklab C=hypot(a,b), HSL/HSV equations, and the distinction between the two orthogonality goals. The bounded answer remains model/source-specific and explicitly denies a universal C/L or cross-model conversion. The other two CQ texts and 9/4/2 occurrence memberships are unchanged.

### Updated outcome dispositions

| Card | Iteration01 proposed result | Remaining boundary |
|---|---|---|
| `hsv` | F01 examples, applications, formula and confusion text now agree with the encoded-sRGB definitions and neutral rule. | The deep-blue effect remains source-attributed; figure not inspected, no perceptual test. |
| `okhsv` | Numeric controls are distinguished from perceived hue/saturation/brightness; maximum-chroma language is scoped to its article sRGB model. | Subjective source ratings and real picker behavior remain untested. |
| `colour-gamut` | Axes, triangular approximation and curved-top compensation are aligned with prepared Okhsv text; CSS document status corrected. | Geometry is text-attributed; figure and live gamut rendering not inspected. |
| `colour-picker-design-principles` | Table columns and Munsell's historical-only role are accurately separated. | Ratings remain source judgments, not a universal standard or user evaluation. |
| `chroma-vs-saturation` | CIE definitions and notes plus model-coordinate distinctions are restored consistently across sections and CQ. | Terms do not provide a universal model conversion or actual rendered-perception test. |

These are CC proposed assessments of five revised bodies, not CDC acceptance of S18-01/02. The other six bodies remain as previously inspected for this iteration's bounded reconciliation; this is not a renewed claim of fresh source fidelity or full-corpus review.

### Current arithmetic and retained evidence

Using Python `colorsys` as a separate implementation plus direct equation assertions: encoded RGB(.8,.2,.2) -> HSV (h=0°, S=.75, V=.8), HSL (h=0°, S=.6, L=.5). RGB(.2,.2,.2) -> both S=0, V=L=.2; RGB(.5,.5,.5) -> both S=0, V=L=.5. Hue's stored zero is conventional and powerless when Δ=0. The two gray fixtures disprove the prior neutral contrast; the chromatic fixture discriminates the formulas.

Toe/inverse, synthetic three-reference rational map and Okhwb results remain applicable via the independent review at `cdc-verification.md#initial-independent-review--2026-10-17`: they were reproduced from the pinned c9/candidate source and the current changes alter none of those formulas, constants, examples or dependencies. This is carried-forward CDC evidence, not rerun or relabelled as an Iteration01 check.

### Preservation and gate applicability

- Source worktree delta is exactly the five authorized card bodies; unrelated committed README deletion and untracked `knowledge/lfe/` remain outside the staged source write set. Planning write set is this batch record, `closing-report.md`, and only ledger Evidence/Notes cells.
- All 233 card identities and raw metadata prefixes are unchanged from c9; all five target heading sequences and literal Source Reference sections are unchanged. The other 228 bodies, all 161 prepared source files, all guides and helpers remain byte-identical. All edited files have LF line endings and final newlines; local Markdown-link/fragments and `git diff --check` are recorded after final edits below.
- Owning SKILL/history, the eight packaged Markdown source inputs, Makefile and package dependencies compare byte-identically with c9. CDC's sequential native/package checks at c9 remain applicable to these unbundled card-body changes. They are retained with their original results and are not presented as fresh CC runs; no gate input or execution condition changed.
- The previous attempt's gates and archive build remain historical evidence at their recorded revisions. Current checks are only the explicit structural/body/witness/path checks enumerated below. No test suite, full corpus, browser picker, accessibility/AT, hosted rendering or release gate was run.

### Current check results

- **Source preservation replay:** passed. The assigned source population is 233 card identities; all233 raw metadata prefixes match c9; all five target heading sequences and literal Source Reference sections match; the other228 card files and all161 prepared source files are byte-identical. All six design guides, helpers, schema, SKILL/history, Makefile/package dependencies and the eight packaged Markdown inputs (SKILL, history and six guides) match c9. The only source commit paths are the five assigned bodies. All five use LF and final newlines.
- **Planning references/bytes:** 16 relative Markdown links and fragments across the three planning outputs resolve; batch record, closing report and ledger have LF and final newlines.
- **Whitespace:** `git diff --check` passed in both worktrees before commit; source commit `7068045aacd6cb75b856786a1de070791f21c2a8` also passes `git diff --check HEAD^ HEAD`.
- **Source commit:** `7068045aacd6cb75b856786a1de070791f21c2a8`, parent `c5e743abb40db2f14b9332cea635a30f8b8a8d5b`, exact five assigned paths, with both required trailers. Planning commit is the exact three-file CC return containing this record; its final hash is returned to the Operator.
