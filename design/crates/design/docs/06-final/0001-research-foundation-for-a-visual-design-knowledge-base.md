---
number: 1
title: "Research foundation for a visual design knowledge base"
author: "database tables"
component: All
tags: [change-me]
created: 2026-02-28
updated: 2026-02-28
state: Final
supersedes: null
superseded-by: null
version: 1.0
---

# Research foundation for a visual design knowledge base

**The field of visual design possesses formal structure, empirical grounding, and mathematical depth fully comparable to graduate-level mathematics or post-doctoral music theory.** This research validates and refines a nine-category domain taxonomy, identifies critical gaps, maps 55 competency questions across three tiers, analyzes 30+ foundational sources, and documents the mathematical underpinnings that will give a technically sophisticated reader first-principles access to the discipline. The most important finding: the proposed taxonomy is well-structured for its purpose but requires a foundational layer (visual elements), promotion of motion design to standalone status, and explicit treatment of cross-cutting principles (hierarchy, contrast, rhythm, proportion) that span every category. Design systems documentation from Google, Apple, IBM, Shopify, and GitHub converges on a six-layer architecture — principles, visual styles, tokens, components, patterns, platform — that should inform the knowledge base's tier definitions.

---

## The taxonomy is strong but needs a foundational layer and three additions

The preliminary nine-category taxonomy maps well to how foundational design education is structured at RISD, Parsons, and CMU. **Colour theory, typography, and layout-composition receive universal standalone treatment** across every program and textbook examined. Visual perception, interaction design, and accessibility have strong support. Information architecture, design systems, and brand identity have moderate support but sit at different abstraction levels.

**Critical gap: visual elements.** Every design foundations textbook — Lupton & Phillips's *Graphic Design: The New Basics*, Lauer & Pentak's *Design Basics* — opens with point, line, plane, shape, texture, and value. RISD teaches "form" as a foundational principle co-equal with colour and typography. These atomic building blocks are more fundamental than any of the nine categories and must be added as a layer-zero category.

**Three categories to add:**

- **Motion design** — RISD and Parsons both offer dedicated tracks; Material Design 3, Carbon, Polaris, and Apple HIG all document motion as a standalone visual style. Animation principles (easing, timing, choreography) are distinct from interaction design.
- **Data visualization** — Carnegie Mellon offers it as a standalone course; Carbon and Polaris document it as a top-level section. It doesn't fit colour, typography, or layout alone.
- **Imagery** — RISD lists "image" as co-equal with colour and type. Photography direction, iconography, and illustration selection are fundamental design decisions with no current home in the taxonomy.

**Orthogonality issues to address.** An ontology engineer would flag three concerns. First, visual-perception and layout-composition overlap significantly — gestalt principles *are* the perceptual laws governing layout. Keep them separate but cross-reference heavily. Second, accessibility operates as a cross-cutting quality attribute touching every other category, not a peer domain. Model it as a facet dimension or ensure each category has accessibility subconcepts. Third, brand-identity sits at a higher abstraction level — it's an application context drawing on colour, typography, and design systems rather than a knowledge domain of equal granularity. Consider renaming it "visual-identity-systems" to focus on the extractable knowledge (logo construction, identity systems, visual language) rather than strategy.

**Cross-cutting principles that span categories.** Hierarchy, contrast, rhythm/repetition, scale/proportion, and balance appear in every textbook and design system but belong to no single category. The knowledge base should model these as cross-cutting concept cards that reference multiple domains, similar to how mathematical theorems reference multiple branches.

### How design systems organize their documentation

Analysis of five major systems reveals a convergent six-layer architecture:

| Layer | Material Design 3 | Carbon | Polaris | Primer | Apple HIG |
|-------|-------------------|--------|---------|--------|-----------|
| Principles | Foundations | Guidelines | Foundations | Foundations | Foundations |
| Visual styles | Styles | Elements | Design | Primitives | Foundations |
| Tokens | Design tokens | Tokens (embedded) | Tokens (top-level) | Primitives | Implicit |
| Components | Components | Components | Components | Components | Components |
| Patterns | — | Patterns | Patterns | Guides | Patterns |
| Platform | Develop | Developing | — | — | Platforms/Technologies |

**Universal visual style categories** across all five systems: colour, typography, spacing/layout, motion, icons, and elevation/depth. The W3C Design Tokens Community Group published its **first stable specification (October 2025)** defining seven primitive types (colour, dimension, fontFamily, fontWeight, duration, cubicBezier, number) and six composite types (shadow, typography, border, gradient, transition, strokeStyle). This taxonomy should inform the design-systems category structure.

---

## Fifty-five competency questions bridge perception and implementation

Research into design education assessment, professional certification criteria, senior designer interview processes, and developer knowledge gaps produced 55 competency questions across five types and three tiers. The questions specifically bridge "I can see it" and "I can build it" — connecting visual perception to systematic implementation.

### Foundational tier: core vocabulary and first principles

**Definitional.** What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it? What distinguishes a spacing system from arbitrary padding values — what problem does constraint solve? What are the three components of HSL, and why is it more useful than hex for palette construction?

**Relational.** How do font weight and colour work *together* with font size to create typographic hierarchy — why is size alone insufficient? How does the relationship between inter-group and intra-group spacing communicate which elements belong together?

**Diagnostic.** A card layout uses 16px padding inside cards, 16px between cards, and 16px between card title and body. Why does everything feel flat? *(Answer: identical spacing erases the distinction between containment and separation; intra-card spacing should be tighter than inter-card spacing.)*

### Intermediate tier: applied knowledge and pattern recognition

**Procedural.** Given a data-rich card (title, status, three metrics, timestamp, action button), how do you assign visual hierarchy: what gets the most weight, what gets de-emphasized, and why? How do you ensure a coloured status badge is accessible without relying solely on colour?

**Diagnostic.** A dashboard uses teal header, red errors, green success, blue links, yellow warnings, purple badges. It looks like a "clown car." What principle was violated? *(Answer: no constrained palette. Define one primary, neutrals, and semantic colours with consistent shades. Reduce total unique hues.)* A form uses identical 8px spacing everywhere. Why does it look "off"? *(Answer: spacing should vary to communicate structure — 4px label-to-input, 16px field-to-field, 32px section-to-section.)*

### Advanced tier: systematic thinking and cross-domain integration

**Relational.** How does a well-structured design token system map onto CSS custom properties? What is the isomorphism between design decisions and code architecture? How does cognitive load theory (intrinsic, extraneous, germane) relate to progressive disclosure and visual hierarchy?

**Diagnostic.** An admin panel organizes UI by database tables — Users page, Orders page, Products page, each showing all columns. Diagnose the fundamental mistake. *(Answer: UI mirrors the data model instead of user tasks. Reorganize around goals: "Process orders," "Handle returns." Show relevant data from multiple tables on task-focused views.)*

The **most common and most consequential developer design mistakes** (validated across multiple sources including Refactoring UI) that diagnostic questions must target: (1) no visual hierarchy — everything has equal weight; (2) inconsistent spacing — no system; (3) unconstrained colour — too many unrelated hues; (4) no type scale — random font sizes; (5) data-model-driven information architecture instead of task-driven; (6) equal-weight buttons — no primary/secondary distinction. These six account for the majority of the perceived quality gap between developer-built and designer-built interfaces.

---

## Source analysis reveals a clear intellectual lineage from perception science to CSS implementation

The sources form a pipeline: **perception science** (Arnheim, Ware, gestalt research) → **design principles** (Norman, Nielsen, Laws of UX) → **practical patterns** (Krug, Refactoring UI) → **system architecture** (Frost, Curtis) → **CSS implementation** (Comeau, Eckles, Every Layout, Utopia). Each source below is assessed for extractable concepts, standing, and unique contribution.

### Colour theory: from Albers's relativity to OKLCH's perceptual uniformity

**Josef Albers, *Interaction of Color* (1963).** The canonical colour education text. Central thesis: "In visual perception a colour is almost never seen as it really is." Organized as sequential exercises progressing from simple to complex. Key extractable concepts: colour relativity, simultaneous contrast, one colour appearing as two (and vice versa), vibrating boundaries, transparency illusion. **272 pages, paperback widely available, no ebook.** Standing: universally canonical.

**Johannes Itten, *The Art of Color* (1961).** Complements Albers with a classification-based approach. The **seven colour contrasts** (hue, light-dark, cold-warm, complementary, simultaneous, saturation, extension/proportion) are individually card-worthy concepts. The contrast of extension is particularly mathematical: Goethe's balance ratios (yellow:violet = 1:3, orange:blue = 1:2, red:green = 1:1). Itten and Albers represent complementary pedagogies — Itten classifies, Albers observes. **Condensed version *Elements of Color* (~96 pages, Wiley) is more accessible.**

**OKLCH/OKLAB (Björn Ottosson, 2020).** The most important modern colour space for web design. Mathematical structure: XYZ → LMS via matrix M₁ → cube-root nonlinearity → opponent-colour transform via M₂. Superior to HSL because **equal L changes produce equal perceived brightness across all hues** — critical for accessible palette generation. CSS support is now baseline: `oklch(L C H)` works in Chrome 111+, Safari 15.4+, Firefox 113+. The relative colour syntax `oklch(from var(--base) calc(l + 0.15) c h)` enables dynamic palette manipulation from a single token. Tailwind CSS 4.0 and Photoshop have adopted OKLCH as default.

**CIE colour science** provides the mathematical foundation. The colour difference formulas progress from simple Euclidean distance in CIELAB (ΔE*₇₆) through the sophisticated CIEDE2000 with its five correction terms (hue rotation for blues, neutral compensation, improved weighting). For the target user: **colour space conversions are 3×3 matrix multiplications** — this is literally linear algebra, not metaphor.

### Typography: from Bringhurst's proportions to Utopia's fluid interpolation

**Robert Bringhurst, *The Elements of Typographic Style* (v4.0, 2012, 398 pages).** The "typographers' bible." Organized around principles (rhythm, proportion, harmony) rather than tutorials. Its mathematical content on proportional systems directly inspired Tim Brown's modular scale work. Standing: canonical but print-focused — no web-specific content.

**Tim Brown's modular scale** is the critical bridge between typographic tradition and web implementation. A modular scale generates font sizes through repeated multiplication by a ratio — **the ratios are explicitly musical intervals**: minor second (15:16 ≈ 1.067), major third (4:5 = 1.250), perfect fourth (3:4 ≈ 1.333), perfect fifth (2:3 = 1.500). The modularscale.com calculator exports to Sass and JavaScript. Brown explicitly quotes Bringhurst: "A modular scale, like a musical scale, is a prearranged set of harmonious proportions."

**Every Layout (Heydon Pickering & Andy Bell)** defines **13 layout primitives** — Stack, Box, Center, Cluster, Sidebar, Switcher, Cover, Grid, Frame, Reel, Imposter, Icon, Container — that are intrinsically responsive without media queries. Philosophy: "composition over inheritance" applied to CSS. This directly maps the GoF software engineering principle to front-end architecture.

**Utopia (James Gilyead & Trys Mudford)** provides the mathematical framework for fluid responsive design. Core math: CSS `clamp()` performs linear interpolation between viewport widths. Define a modular scale ratio at minimum and maximum viewports (e.g., 1.2 at 360px, 1.25 at 1240px); each scale step gets its own clamp() declaration, causing **headings to grow faster than body text** as the viewport widens. The space system applies the same principle to spacing tokens.

### UI/UX: Norman's affordances through Laws of UX to Refactoring UI

**Don Norman, *The Design of Everyday Things* (revised 2013, 368 pages).** The foundational text of interaction design. Six concepts for discoverability: affordances, signifiers, mapping, feedback, constraints, conceptual models. The 2013 revision introduced "signifiers" to resolve the widespread misuse of "affordance" — affordances are possible actions, signifiers communicate those possibilities. Key frameworks: Gulf of Execution, Gulf of Evaluation, Seven Stages of Action.

**Laws of UX (Jon Yablonski, lawsofux.com)** compiles **30 laws** organized into heuristics (Fitts's Law, Hick's Law, Jakob's Law, Miller's Law, Doherty Threshold), gestalt principles (proximity, similarity, common region, Prägnanz, uniform connectedness), cognitive biases (Peak-End Rule, Von Restorff Effect, Serial Position Effect), and principles (Tesler's Law, Zeigarnik Effect). The site is freely accessible and each law includes psychological foundations and practical applications — ideal for concept card extraction.

**Refactoring UI (Adam Wathan & Steve Schoger, ~218 pages, PDF).** The definitive developer-to-designer bridge. Core insight: **design is a set of systematic, repeatable decisions, not artistic intuition.** Eight chapters covering hierarchy, spacing, typography, colour, depth, images, finishing touches. Key tactical patterns: constrained spacing scales (4/8/12/16/24/32/48px), HSL-based palette construction (8-10 shades per hue), "start with too much whitespace," design in greyscale first to force hierarchy through spacing and contrast rather than colour. Standing: beloved by developers; zero theory filler.

**Brad Frost, *Atomic Design* (free at atomicdesign.bradfrost.com).** Five levels: atoms → molecules → organisms → templates → pages. Maps directly to React/Vue component architecture. Criticism: the chemistry metaphor creates categorization debates, but the underlying hierarchy principle is sound.

---

## Design has rigorous mathematical structure — not soft-discipline hand-waving

### Quantitative UX laws have precise formulations

**Fitts's Law (ISO 9241 standard, Shannon formulation):**

> MT = a + b × log₂(1 + D/W)

where MT is movement time, D is distance to target, W is target width, and the Index of Difficulty ID = log₂(1 + D/W) is measured in bits. Fitts drew directly from Shannon's channel capacity theorem: movement amplitude is analogous to signal power, target width to noise power. **Throughput TP = ID/MT** ≈ 10 bits/s for mouse pointing. Breaks down for very small targets, touch input (fat finger minimum ~7-10mm), and saccadic eye movements. The **Steering Law** for path-following (menus, scrollbars) is derived from Fitts's Law by integral calculus: T = a + b × (A/W), where the logarithmic term vanishes into a linear relationship.

**Hick's Law:** RT = a + b × log₂(n + 1), where the +1 represents the null event (temporal uncertainty of stimulus onset). General form uses Shannon entropy: RT = a + b × H where H = -Σ pᵢ log₂(pᵢ). Breaks down critically when stimulus-response compatibility is high (Leonard, 1959: NO set-size effect with highly compatible mappings) and for expert users with practiced spatial memory.

**Stevens's Power Law** (ψ = k × Iⁿ) explains why design systems use geometric spacing scales: visual area has exponent n ≈ 0.7 (compressive), meaning doubling physical area does NOT double perceived size — you need ~2.7× the area. Brightness has n ≈ 0.33, explaining why gamma correction and perceptually uniform colour spaces are necessary.

**Weber-Fechner Law** (ΔI/I = k) establishes that just-noticeable differences are proportional to stimulus intensity. For line length, k ≈ 0.03 (3%). This is why spacing scales must be geometric (multiplicative) rather than arithmetic (additive) to create perceptually equal steps.

### Group theory classifies all possible repeating patterns

The **17 wallpaper groups** (proven by Fedorov, 1891) constitute a complete mathematical classification of every possible two-dimensional repeating pattern. The **7 frieze groups** do the same for border/strip patterns. The **crystallographic restriction theorem** proves that only 2-, 3-, 4-, and 6-fold rotational symmetries are compatible with periodic lattices — which is why 5-fold symmetry (Penrose tilings) requires aperiodic structures. This is not a heuristic but a mathematical absolute: any CSS `background-repeat` pattern, textile, or tile design must conform to one of these groups.

### Gestalt principles have computational formalisations

Kubovy & Wagemans (1995, 1998) established the **Pure Distance Law**: grouping by proximity follows an exponential decay function of relative inter-element distance — log[p(b)/p(a)] = -α × (|b|/|a| - 1), where α ≈ 3 is the attraction constant. Crucially, only *relative* distances matter, not absolute ones. Recent work using **persistent homology** (Chen et al., 2024) provides a unified computational framework where proximity appears as 0-dimensional persistence and closure as 1-dimensional persistence in Vietoris-Rips filtrations.

---

## The Rosetta Stone: where cross-domain analogies are rigorous versus merely metaphorical

### Software engineering → design systems: these are implementations, not analogies

Every major software engineering principle has a direct, non-metaphorical implementation in design systems. **Abstraction** → design tokens abstract visual decisions from implementation, identically to software abstraction. **DRY** → a centralized token repository (JSON/YAML) is the single source of truth; Style Dictionary transforms it to platform outputs. **API design** → a React component's props interface `<Button variant="primary" size="lg" disabled>` IS an API with types, defaults, and contracts. **Composition over inheritance** → Every Layout explicitly advocates this for CSS, composing layout primitives instead of inheriting from parent classes. **Dependency injection** → CSS custom properties are injected at root scope and consumed by children — this is inversion of control. These mappings are all rated **RIGOROUS**: they use the same concepts, not analogies to them.

### Music theory → visual design: three rigorous connections, several structural parallels

**Musical intervals → type scale ratios (RIGOROUS).** Tim Brown explicitly adopted musical interval ratios for modular type scales. The mathematics is *identical*: perfect fourth (4:3 = 1.333), perfect fifth (3:2 = 1.500), golden ratio (1:φ = 1.618). A music theorist immediately understands that a perfect-fourth type scale means each step is 4:3 of the previous — and why this produces perceived proportional harmony.

**Temperament → perceptual uniformity in colour spaces (RIGOROUS).** This is the deepest and most intellectually satisfying bridge. Equal temperament compromises interval purity so all keys are equally usable — every semitone is exactly 2^(1/12). Perceptually uniform colour spaces (CIELAB, Oklab) compromise physical accuracy so all regions of colour space have equal perceptual step sizes. Both solve **the identical mathematical problem**: uniformizing a perceptual space that is inherently non-uniform. Just as equal temperament makes no interval perfectly pure (except the octave), CIELAB makes no colour region perfectly calibrated (blues are notably worse). Oklab improves on CIELAB the way well-temperaments improve on equal temperament for specific key regions.

**Linear algebra → colour space transformations (RIGOROUS).** Colour space conversions are 3×3 matrix multiplications. sRGB → XYZ, XYZ → LMS, LMS → Oklab opponent channels — each step is a matrix multiply, and the chain can be collapsed into a single matrix per Grassmann's additivity law.

**Colour harmony ↔ musical harmony (LOOSE to STRUCTURAL).** The 12-hue wheel / 12-semitone parallel is structurally suggestive, but colour perception is trichromatic (three cone types) while auditory perception is frequency-analytic (cochlear resonance). Empirical evidence for colour harmony based on frequency ratios is weak — a BYU study found harmonies constructed from musical frequency ratios "extremely uninteresting." The *structural* parallel (complementary relationships, triadic relationships) has practical value, but mathematical equivalence is unsupported.

**Rhythm, tension-resolution, dynamics, key/tonality** are all rated **STRUCTURAL**: meaningful parallels with practical design value, but operating through different perceptual mechanisms (temporal vs. spatial).

---

## Notation conventions converge on three-tier token architecture

### Colour notation is shifting from hex to OKLCH

Hex remains the universal interchange format, but the industry is moving toward OKLCH for manipulation and token definition. The dominant pattern is a **three-tier token architecture**: primitive tokens (`color.blue.500`) → semantic tokens (`color.primary`, `color.surface.default`) → component tokens (`color.button.primary.background.hover`). Material Design 3 uses a 0-100 tonal scale for lightness; Adobe Spectrum uses 50-900 numeric scales. With CSS relative colour syntax now baseline, teams can define `--brand-l`, `--brand-c`, `--brand-h` as separate properties and generate tonal scales via `calc()`, dramatically reducing the number of pre-computed variables.

### Spacing notation: 4-point base with 8-point primary rhythm

The **4-point vs. 8-point grid debate** has converged: modern teams use a **4pt base** with 8pt as the primary structural rhythm. Component padding at 4-16px, section margins at 24-64px. For token naming, the dominant patterns are T-shirt sizing (`space-xs` through `space-3xl`), numeric scales (`space.1` through `space.8`), and semantic aliases (`spacing.inset.md`, `spacing.section.lg`). Nathan Curtis's **inset variants** (squish, stretch) provide additional precision for component padding.

### Typography tokens use composite structures

The DTCG specification defines typography as a composite token type combining fontFamily, fontSize, fontWeight, lineHeight, and letterSpacing. Material Design 3's typescale uses a two-axis naming convention: category (display, headline, title, body, label) × size (large, medium, small) → `typescale-display-large`. Utopia's fluid type approach names scale steps numerically (`--step--2` through `--step-5`) with each step getting its own `clamp()` declaration.

### Responsive notation is shifting from breakpoints to fluid ranges

Breakpoint naming universally uses T-shirt sizing (`sm`, `md`, `lg`, `xl`), but Utopia's approach replaces discrete breakpoints with continuous `clamp()` interpolation. Container queries (`@container`) enable component-level responsiveness independent of viewport, with container units (`cqw`, `cqi`) for sizing relative to the container. **Cascade layers** (`@layer`) solve specificity wars by defining explicit cascade order independent of selector specificity.

---

## The 2024-2025 CSS landscape represents a generational capability shift

Modern CSS has undergone a transformation comparable to the introduction of Flexbox. **Container queries** (96%+ global support) let components respond to their own available space, not the viewport — revolutionary for design systems where the same component appears in different contexts. **`:has()`** enables parent selection based on children, previously requiring JavaScript. **Subgrid** (97% support) solves nested alignment problems. **CSS Nesting** eliminates the need for preprocessors for organization. **Scroll-driven animations** replace GSAP ScrollTrigger for parallax and reveal effects.

For colour: `oklch()`, `color-mix()`, relative colour syntax, and `color(display-p3)` are all baseline. Wide-gamut displays (Display P3 covers ~50% more colours than sRGB) are standard on Apple devices and OLED screens. Variable fonts provide continuous weight, width, and optical size adjustment from a single file — Inter Variable at 405KB replaces four static files totaling 680KB.

**Figma** has matured its variables system with multi-mode support (light/dark, brand variants), native DTCG JSON import/export, and Code Connect for mapping Figma components to production code. Style Dictionary v4 provides first-class DTCG format support for transforming tokens to any platform.

---

## Source availability and acquisition summary

| Source | Format | Pages | Free? | Priority |
|--------|--------|-------|-------|----------|
| Albers, *Interaction of Color* | Paperback (no ebook) | 272 | No | Essential |
| Itten, *Elements of Color* | Paperback | 96 | No | High |
| Bringhurst, *Elements of Typographic Style* | Print only, v4.0 | 398 | No | Essential |
| Lupton, *Thinking with Type* (3rd ed, 2024) | Print, companion site | 256 | No (site free) | Essential |
| Müller-Brockmann, *Grid Systems* | Print, bilingual | 176 | No | High |
| Vignelli, *The Vignelli Canon* | **Free PDF** from RIT | 96 | **Yes** | Essential |
| Norman, *Design of Everyday Things* | Ebook available | 368 | No | Essential |
| Krug, *Don't Make Me Think* | Print/ebook | 200 | No | High |
| Frost, *Atomic Design* | **Free online** | ~200 | **Yes** | High |
| Refactoring UI | PDF only | ~218 | No ($79-149) | **Critical** for target user |
| Laws of UX | **Free website** + book | — | **Yes** (site) | Essential |
| Butterick, *Practical Typography* | **Free web book** | — | **Yes** | High |
| Every Layout | Paid website (some free) | — | Partially | High |
| Utopia | **Free calculators** + blog | — | **Yes** | Essential |
| Comeau, CSS for JS Developers | Paid course (blog free) | — | Partially | High |
| Eckles, ModernCSS.dev | **Free website** | — | **Yes** | High |
| Gurney, *Color and Light* | Print | 224 | No | Supplementary |
| Arnheim, *Art and Visual Perception* | Print | 508 | No | Supplementary |
| Ware, *Information Visualization* | Print (4th ed) | 560 | No | Supplementary |

**Recommended acquisition priority for the target user:** Start with the free resources (Vignelli Canon, Atomic Design, Laws of UX, Butterick, Utopia, ModernCSS.dev), then acquire Refactoring UI (the single most valuable resource for a developer), followed by Lupton and Bringhurst for typography, Albers for colour, and Norman for interaction design principles.

---

## Conclusion: the knowledge base should mirror the field's layered architecture

This research reveals that visual design is not a flat collection of tips but a **layered discipline** with formal mathematical structure at its foundation. The knowledge base should reflect this architecture:

**Layer 0 (perception science):** Gestalt grouping laws, preattentive processing, Stevens's Power Law, Weber-Fechner — the psychophysical ground truth that explains *why* design principles work. This is where the target user's mathematical fluency becomes a superpower.

**Layer 1 (design principles):** The cross-cutting concerns — hierarchy, contrast, rhythm, proportion, balance — that operate across all visual domains. These are the "theorems" of the discipline.

**Layer 2 (domain knowledge):** The ten-category taxonomy (visual elements, colour theory, typography, layout-composition, visual perception, interaction design, information architecture, design systems, motion design, accessibility) with their specific concepts, vocabulary, and techniques.

**Layer 3 (implementation):** CSS capabilities, design tokens, component architecture, fluid systems — the executable knowledge that turns understanding into working interfaces.

The **cross-domain Rosetta Stone** should be woven throughout rather than isolated in a separate section. When a concept card explains modular type scales, it should note the identical mathematical structure to musical intervals. When it explains OKLCH's perceptual uniformity, it should reference the temperament analogy. When it explains design tokens, it should map directly to software engineering abstraction. The target user's existing expertise in mathematics, music theory, and software engineering isn't a gap to be bridged — it's the foundation on which the entire knowledge base should be built.
