# Design knowledge audit

Date: 2026-10-08, America/Chicago. Source baseline: `dffa504e851b03b8e4746f1941068e4cc850b612`, `main`. Skill metadata: `visual-design-system`, `1.0.0`.

## Assessment

This is a promising philosophy of visual composition embedded in a publishing-brand implementation, rather than a dependable general design skill. Its best ideas are content-led composition, semantic roles, proportional relationships, intrinsic layout, expressive coherence, and hospitable craft. However, the entrypoint turns project choices and useful heuristics into universal laws; several mathematical and accessibility claims are incorrect. The large underlying card collection does not remedy this: it is neither routed from the entrypoint nor included in the installable package, and selected cards contain their own unsupported extrapolations.

The proposed release boundary is **1.5: trustworthy foundations and coherent operation**, then **2.0: a complete, evidence-led design practice**. The accompanying [synthesis](audit-modernization-synthesis.md) develops those proposals. These are audit findings and recommendations, not implementation acceptance or approved project plans.

## Scope and evidence

Read the complete entrypoint, all six guides, and sibling history: eight files, 4,114 lines. Checked cross-file claims, CSS examples, Makefile packaging, staging behavior, documentation routes, and a freshly generated design zip. Inventoried all 233 cards and 161 source-tree files (160 Markdown files plus one conversion report); performed targeted content searches and inspected selected card/source passages. Current comparisons use official documentation and original research where retrievable.

| Surface | Coverage and boundary |
| --- | --- |
| Entrypoint and six guides | Complete substantive review; all remain unchanged. These are the entire live instructional payload. |
| Package | Fresh `make design`; eight actual files, plus two directory entries. Entrypoint is copied unchanged. |
| Concept cards | Complete inventory/search coverage; targeted semantic checks. **Not** a claim-by-claim verification of all 233 cards. |
| Source material | Collection inventory; targeted Brown/Ottosson/Butterick passages. The 160 source documents were not all reread. |
| External systems | Targeted primary-source comparison, not an exhaustive audit of each system. Material pages required search-indexed official passages where direct retrieval returned a JavaScript shell. |
| Rendered products | No real product was supplied. Numerical examples were checked; no browser/assistive-technology conformance or user study was performed. |
| Other repository work | Excluded. Pre-existing untracked `knowledge/lfe/` was left untouched. |

Scales covered: individual claims and expressions; each guide; colour/type/layout composition; the whole skill; its package and repository integration. There is no standalone application in this scope. Canonical architecture is discoverable through `SKILL.md` and `guides/design.md`, but the package has no operational architecture for design research, interaction states, or evaluation.

Severity is relative to the skill's ability to guide real work: High means a realistic correctness/accessibility failure; Medium means material quality, maintainability, or capability loss; Low means local presentation damage. **16 findings: 7 High, 8 Medium, 1 Low; no Blockers.**

## Findings

### DES-001 — High: a specific publishing brand is the default design contract

**Locations:** `knowledge/design/SKILL.md:5`, `:68–74`, `:118–177`, `:248–250`; `guides/colour.md:9–28`; `guides/type.md:9–26`; `guides/layout.md:9–11`. **Scale:** whole skill.

The description explicitly limits the skill to Cowboys & Beans while its triggers promise help with any visual-design question. Core rules prescribe brand browns, warm neutrals, three named fonts, one accent per site, three domains, and particular font axes. These are not marked optional examples. A fresh assistant therefore has positive instructions to impose C&B decisions on unrelated work.

**Fix:** separate portable principles, project configuration, and historical examples. Generic workflows must first consume the user's existing identity or establish a brief. Remove the C&B preset from default routing. Preserve its provenance in Git and, if retained as a useful case study, behind an explicit opt-in route. Do not merely rename brown to “primary”: teach how to select roles and evaluate a palette.

### DES-002 — High: heuristics become false perceptual guarantees

**Locations:** `SKILL.md:67–74`, `:362–368`; `guides/design.md:107–126`, `:140–145`, `:246–263`, `:308–334`; `guides/layout.md:387–400`. **Scale:** cross-guide theory.

The skill says all quantitative scales must be geometric; proximity precedes every other grouping cue; regularity necessarily produces pleasure; and constraints make bad compositions impossible. It mixes psychophysical models, mathematical constructions, aesthetic preferences, and empirical conclusions without their boundary conditions. Principle I demands geometric colour-lightness steps while Principle II recommends equal additive lightness increments. Neither proposition establishes accessible contrast or good composition.

The local Brown source explicitly permits optical adjustments outside the scale: `sources/md/posts/more-meaningful-typography.md:266`, `:310–314`. The card itself preserves that qualification at `concept-cards/posts/modular-scale.md:130–155`. The guide loses it.

**Fix:** classify claims as mathematical identity, scoped empirical finding, design heuristic, project convention, or analogy. Prefer coherent scales, proximity, and regularity where they serve meaning; permit documented optical correction, content density, different scripts, and deliberate expressive departures. Remove guarantees of universal beauty and automatic correctness. Keep craft and proportion as commitments, not purported neuroscience.

### DES-003 — High: the central fluid-scale invariant is mathematically false

**Locations:** `guides/layout.md:186–196`, `:362–375`, `:935–945`. **Scale:** mathematical model.

Linear interpolation between two geometric progressions with different ratios does not generally yield another geometric progression. The guide also describes clamped linear functions as asymptotic curves and says proportions are constant while simultaneously changing their ratios.

For the documented endpoints, let `s_n(t) = (1-t)16(1.2)^n + t20(4/3)^n`. At `t=0.5`, steps 0–3 are `18`, `22.933333`, `29.297778`, `37.527704`. Successive ratios are `1.274074`, `1.277519`, `1.280906`, not one constant. This is a counterexample, not an argument against fluid typography.

**Fix:** say each step interpolates independently between chosen endpoint scales. State which relationships are actually guaranteed and test intermediate widths. Utopia's [space-palette article](https://utopia.fyi/blog/painting-with-a-fluid-space-palette/) also distinguishes its space multipliers from a single geometric type ratio; a common base does not make the scales identical.

### DES-004 — High: generated numbers do not implement the stated configuration

**Locations:** `SKILL.md:153`, `:187–206`; `guides/type.md:139`, `:474`; `guides/layout.md:496–527`. **Scale:** examples and cross-file configuration.

The small-screen ratio is variously 1.25 and 1.2. The advertised base endpoints are 16px and 20px, but the published step-0 clamp yields the following at a 16px root:

| Viewport | Published clamp result | Declared intended result |
| --- | ---: | ---: |
| 360px | 16.19664px | 16px |
| 900px | 18.85560px | 18px |
| 1440px | 21.33920px | 20px |

**Fix:** select one illustrative configuration and generate every table/snippet from it. For these base endpoints, `clamp(1rem, 0.9166667rem + 0.3703704vi, 1.25rem)` matches the stated values under the stated root-size assumption. This is an arithmetic correction, **not** accessibility certification. Include negative steps, interior widths, rounding tolerance, root-size changes, and endpoint checks in the example verification.

### DES-005 — High: logical viewport units are presented as an accessibility guarantee

**Locations:** `guides/layout.md:937–940`; `guides/breaking-the-layout-monoculture.md:198–204`. **Scale:** accessibility claim.

`vi` follows the viewport's inline axis; it does not inherently preserve text enlargement. In horizontal writing it follows the same axis as `vw`. Changing the unit cannot by itself establish WCAG text-resize conformance. See the [CSS unit definition](https://www.w3.org/TR/css-values-4/#viewport-relative-lengths) and [W3C resize-text explanation](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html).

**Fix:** preserve user font preferences and test actual text enlargement, clipping, overlap, and functionality. Separately test reflow; do not substitute a narrow screenshot for text-resize testing. Retain `vi` where logical-axis behavior is intended, without the guarantee.

### DES-006 — High: decorative recommendations lack an accessible interaction floor

**Locations:** `SKILL.md:266–281`; `guides/colour.md:338–348`, `:418–465`, `:508`; `guides/breaking-the-layout-monoculture.md:452–485`; `guides/layout.md:693–695`. **Scale:** whole user experience.

The review checklist mentions contrast but omits keyboard operation, focus, semantics, reading order, reduced motion, and assistive-technology behavior. The complete live payload contains no `keyboard`, `screen reader`, `prefers-reduced-motion`, `forced-colors`, or `focus-visible` text. Hover reveals, scroll effects, Reels, and Imposter positioning are recommended without their behavioral obligations. Positioning a box is not a modal-dialog implementation.

Placeholder and disabled text share one token, though their contrast obligations differ. Reconstructing the declared neutral palette (`C=.01`, `h=55`, `L=.62` text) gives approximately **3.15:1** against `L=.95` and **3.39:1** against `L=.975`. Those values miss normal-text 4.5:1; the latter resembles the gallery-label pairing. This is a calculation from stated palette parameters, not a measurement of a supplied website: complete CSS definitions are absent. [W3C explicitly includes placeholder text in the contrast requirement](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

**Fix in 1.5:** provide focus/keyboard/semantic baselines, foreground/background/state pairing checks, visible fallback content, motion preferences, and routes to [APG patterns](https://www.w3.org/WAI/ARIA/apg/patterns/). Distinguish decoration from necessary control boundaries. State target-size requirements accurately: 24px AA has exceptions; 44px can be a chosen stronger target, not an unexplained universal standard. See [target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum). Full pattern coverage belongs in 2.0, but safe instructions cannot wait.

### DES-007 — High: the colour-conversion explanation removes required nonlinear operations

**Locations:** `SKILL.md:366`; `guides/foundations-of-design.md:239–252`, `:446–449`. **Scale:** technical correctness.

The guide correctly mentions Oklab's cube-root step, then later claims that the whole sRGB → XYZ → LMS → Oklab conversion collapses into one 3×3 matrix. It cannot: encoded sRGB needs linearization, and Oklab includes a nonlinear step. The local card states this distinction correctly at `concept-cards/posts/matrix-transformation-colour.md:75–76`, `:121–126`. The [original Oklab derivation](https://bottosson.github.io/posts/oklab/) supplies the actual pipeline and explicitly discusses approximation limits.

**Fix:** distinguish linear transforms from the complete nonlinear pipeline; describe OKLCH as approximately perceptually uniform, not an exact brightness/contrast oracle. Add gamut handling, compositing/background context, and measured contrast to practical palette guidance. Keep the temperament comparison as an analogy, not proof of an identical perceptual mechanism.

### DES-008 — Medium: named design systems and DTCG are used as authority for an invented universal architecture

**Locations:** `guides/design.md:61–84`, `:165–180`, `:371–376`; `guides/colour.md:564–567`; `guides/foundations-of-design.md:465–511`. **Scale:** intellectual provenance and system architecture.

Convergence is described as proof that the chosen architecture is a design fact. The DTCG format does not prescribe three token layers or universal semantic meanings. [Fluent explicitly documents two token layers](https://fluent2.microsoft.design/design-tokens). [Carbon's type styles](https://www.carbondesignsystem.com/building-blocks/foundations/typography/type-sets) include 14, 16, 20, 28, 32, 42, and 54px headings, rather than a single fixed-ratio progression; it also distinguishes productive and expressive typography. These are counterexamples to universality, not faults in those systems.

**Fix:** treat reference → semantic → optional component aliases as a useful local architecture with tradeoffs. Explain source-system differences. Cite DTCG as an [interchange format with typed values and references](https://www.designtokens.org/tr/2025.10/format/), and validate actual exports before saying they conform. Separate design-language version, implementation version, and documentation date. In particular, distinguish [current Polaris web components and migration](https://shopify.dev/docs/apps/build/app-home/migrate-from-polaris-react) from historical React guidance.

### DES-009 — Medium: intrinsic layout has become a ban on legitimate adaptation

**Locations:** `SKILL.md:82`, `:208–210`, `:272`; `guides/layout.md:291–293`, `:698–700`, `:970–975`; `guides/breaking-the-layout-monoculture.md:107–108`. **Scale:** layout method.

The “zero media queries” test confuses avoiding unnecessary overrides with a correctness criterion. Some decisions are discrete: navigation modes, reading order, density, pointer capabilities, print, and motion preferences. Container queries still contain thresholds; using `ch` does not make a threshold self-justifying. A finite primitive vocabulary cannot guarantee every composition is useful.

**Fix:** teach intrinsic layout first, then content-driven container/viewport adaptation and user preferences. Require a reason for a breakpoint, not its absence. Separate geometry primitives from semantic components and interaction patterns. Scope prose measure constraints to prose rather than applying a universal 60ch restriction to controls, tables, and every other element.

### DES-010 — Medium: the package ships converted presentation material with unreliable routes and examples

**Locations:** `SKILL.md:31–37`, `:258–262`; all six guide headers at `:1–3`; `guides/layout.md:508–528`, `:864–887`; `Makefile:245–263`, `:323–324`; `scripts/stage-skill-entrypoint:12–15`. **Scale:** package and reading workflow.

The entrypoint names `layout.md`, `colour.md`, etc. as though they were siblings, but they exist under `guides/`; the staged entrypoint is byte-identical. All guides retain publishing-site wrappers and a missing monogram reference. CSS examples in the layout guide are converted span markup, not directly copyable CSS. The colour guide refers to primitive custom properties without supplying complete definitions. The primitive inventory also changes from twelve in the monoculture guide to thirteen elsewhere without an explained extension.

**Fix:** use real relative Markdown routes, clean teaching prose, fenced runnable examples, explicit local/upstream primitive attribution, and complete declared dependencies. Preserve original presentation material as provenance rather than preserving its rendering debris as the live guide. Test in an isolated unpacked package; a repository-relative search can conceal these problems. The 451-character description also exceeds the 300-character editorial target, though the existing build accepts it.

### DES-011 — Medium: typography is a font selection pitch, not a transferable typesetting method

**Locations:** `guides/type.md:23–123`, `:246–450`; `SKILL.md:145–177`. **Scale:** domain capability.

The guide devotes substantial space to why three faces suit one brand but provides no operational font-loading/fallback procedure, script-coverage selection, font-file axis verification, robust numeric typography, or text-spacing override checks. Its examples use 0.55–0.7rem functional text while the rules insist all sizes come from the scale. This is a legibility risk and internal contradiction; small size alone is not a demonstrated WCAG violation.

**Fix in 1.5:** teach role selection, reading conditions, x-height/measure/leading, optical corrections, actual font-axis ranges, fallbacks and loading behavior, and a minimum readable example policy. In 2.0, expand microtypography, data typography, multilingual shaping and punctuation, and editorial composition. [Spectrum's applied typography](https://spectrum.adobe.com/foundations/typography/applying-the-type-system) and [W3C language enablement](https://www.w3.org/International/typography/) supply useful additional material; their own chosen values remain context-specific.

### DES-012 — Medium: the case against templates overstates the research

**Locations:** `guides/breaking-the-layout-monoculture.md:28–35`, `:52–73`, `:522–528`; `guides/layout.md:793–799`; `SKILL.md:218–230`. **Scale:** research interpretation.

The CHI paper's indexed original abstract reports increased similarity **since 2007** within a 2003–2019 dataset, including over 30% decline in its page-layout distance measure. The guide turns this into a general “30% over sixteen years” claim. It then uses advertising-attention research to assert that familiar page templates degrade comprehension and engagement in general. The cited [NN/g banner-blindness study](https://www.nngroup.com/articles/banner-blindness-old-and-new-findings/) does not establish that broad conclusion.

**Fix:** retain distinctiveness as an intentional expressive goal; describe the dataset and metric precisely, and separate observation from causal interpretation. Evaluate departures from conventions against task success, orientation and repeat use. Repetition may be exactly right for comparable items and learned controls. Obtain the full [CHI paper](https://doi.org/10.1145/3411764.3445156) before retaining stronger numerical or causal claims: direct PDF retrieval failed in this audit, so the inspected abstract does not certify the full study.

### DES-013 — Medium: the research substrate is much narrower than the guide's authority claims

**Locations:** `guides/foundations-of-design.md:9–15`, `:120–127`, `:213–218`, `:550–583`; `guides/breaking-the-layout-monoculture.md:537–582`; `Makefile:261–263`. **Scale:** evidence architecture.

The guides claim a broad research survey and 55 competency questions, but there is no complete traceable source-to-claim/CQ inventory in the live package. Source-name lists mix scholarly results, historical interpretation, web-platform facts and recommendations. Present source holdings are 156 Butterick pages and four posts. No local source snapshots for Material, Carbon, Polaris, Every Layout, Utopia or CUBE appeared in the designated source tree. That does not make every uncaptured citation false; it means the asserted research is difficult to reproduce and maintain.

**Fix:** create a source register with edition/version, locator, retrieval/snapshot identity, applicability and rights notes; attach consequential claims to exact support. Represent “named,” “available,” “read,” “extracted,” and “verified” separately. Resolve or remove unsupported counts. Use a concise curated package with optional depth routes; do not ship all 233 cards automatically or copy acquired books into packages.

### DES-014 — Medium: the workflow begins after the most consequential design decisions

**Locations:** `SKILL.md:256–281`; `guides/foundations-of-design.md:40–86`, `:186–204`. **Scale:** whole skill's advertised capability.

“Designing a New Page” starts by selecting layout primitives. There is no operational path from audience, task, content, context and constraints to alternative concepts, prototypes and observed outcomes. The foundations guide itself identifies missing visual elements, motion, data visualization, imagery and accessibility integration, but those diagnoses never become usable procedures. The package cannot yet be a designer's main AI-assisted tool.

**Fix:** 1.5 adds a brief/context intake and limits the promise to what is supported. 2.0 adds discovery, information architecture, content design, interaction/state design, expression and art direction, inclusive practice, critique, validation and system maintenance. These are connected design responsibilities, not a request to turn the skill into a giant component library. [Design Council's framework](https://www.designcouncil.org.uk/resources/framework-for-innovation/) and [GOV.UK publication criteria](https://design-system.service.gov.uk/community/contribution-criteria/) provide process/evidence counterweights to the current CSS-first approach.

### DES-015 — Medium: targeted card checks expose invalid cross-domain extrapolation and incomplete local provenance

**Locations:** `concept-cards/munsell-colour-system/munsell-hue-circle.md:76–90`, `:116`; `concept-cards/posts/modular-scale.md:155`; source/card collection boundary. **Scale:** knowledge substrate.

The Munsell card describes triads as coset decompositions of `Z/10Z`. Subgroup/coset sizes divide ten; there are no three-element cosets. An indexing analogy does not establish pigment mixing or perceptual harmony. The same card converts a 100-step notation into a “perceptual resolution limit” without support shown for that physiological claim. Meanwhile the 150 Arnheim/Munsell/Tschichold cards have no originals in this skill's designated source tree; their correctness cannot be certified from their confidence fields.

**Fix:** correct the demonstrated algebra, scope the indexing analogy, and recheck physiological claims against source evidence. Keep unresolved cards visibly unverified and exclude them from normative guidance. Inventory all cards for this extrapolation pattern before 1.5; conduct full claim-level reconciliation for any cards promoted into the 2.0 tool. Coordinate with existing concept-card project ownership rather than silently migrating historical schemas or records.

### DES-016 — Low: literal Unicode escapes damage the article-derived cards

**Location:** `concept-cards/posts/matrix-transformation-colour.md:41–61`, representative of all 46 posts cards. **Scale:** collection presentation.

Literal `\u00d7`, `\u2192` and similar sequences appear in normal Markdown prose. They impair reading and copying mathematical material. **Fix:** make a scoped presentation repair with a before/after diff that preserves mathematical meaning and provenance; do not blindly decode legitimate code escapes across all files.

## Clean checks and strengths

1. `metadata.version` and the sibling history agree on 1.0.0. The fresh build's source version gate checked 23 skills and reported zero errors; no competing design history file was found.
2. Complete searches found no `cnbb`/`Cowboys` strings in the source or concept-card trees. Brand contamination is concentrated in the live instructional layer, which makes isolation feasible.
3. The generated design package contains exactly the declared entrypoint, history and six guides; it does not accidentally bundle the acquired source corpus.
4. The Brown source and selected cards retain explicit room for optical judgment; this is recoverable source guidance, not a need to abandon proportional design.
5. Oklab's nonlinear step is preserved in the local conversion cards. The matrix-only mistake is not universal across the corpus.
6. The foundations guide recognizes accessibility as cross-cutting and identifies imagery, motion and data visualization as gaps. The repair can make those existing insights operational.
7. Semantic colour roles, content-driven dimensions, and composition from small spatial primitives remain useful. No finding requires adopting a corporate visual identity.

## Verification record and limits

- `make help`: inspected repository entrypoints.
- `make design`: exit 0; source version check 23 skills / 0 errors; design description 451 characters, over editorial target; eight payload files, 166,519 bytes total uncompressed.
- Python calculations reproduced the clamp endpoint mismatch, non-geometric intermediate ratios, and reconstructed neutral contrast values. Contrast uses the original Oklab inverse to linear sRGB and WCAG relative luminance; all reconstructed channels were in gamut.
- Python/package inspection confirmed the unchanged staged entrypoint, missing root-level guide routes, absent monogram, complete inventory counts, and 46 cards containing literal Unicode escapes.
- Full repository `make check-package-paths`, user-task trials, rendered specimen checks, assistive-technology tests and all-card semantic verification were **not run**. No source/package changes are proposed-done; a successful build does not establish instructional correctness.
- External lookup failures: one CHI PDF URL redirected to a lab homepage; the alternate PDF timed out. Several Material pages returned a JavaScript shell. Only the retrievable primary excerpts are relied upon for those sources.
- The audit is independent of the original design-authoring session, but these new proposals have not received independent acceptance. During the original audit, no commits, releases, source edits, or planning-tree mutations were made. Subsequent project establishment and administrative relocation are recorded in [the relocation record](artifact-relocation.md).
