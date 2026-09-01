# Phase 0 - Section 2 - Domain Taxonomy

## 2. Domain Taxonomy

### 2.1 Category Definitions

Thirteen categories organised into four layers. Each concept card receives exactly one primary `category` value. Cross-cutting concepts receive the category of their strongest home and use `related` relationships to link across categories.

#### Layer 0 — Perceptual Foundations

| Category | Slug | Description | Scope |
|----------|------|-------------|-------|
| Visual Elements | `visual-elements` | The atomic building blocks of all visual composition | Point, line, plane, shape, form, texture, value, figure-ground. The "axioms" from which everything else is constructed. |
| Visual Perception | `visual-perception` | How the human visual system processes and organises visual information | Gestalt principles (proximity, similarity, closure, continuity, common fate, common region, Prägnanz, uniform connectedness), preattentive processing, visual weight, optical illusions, figure-ground perception, visual search, change blindness, inattentional blindness. |

#### Layer 1 — Design Principles (Cross-Cutting)

| Category | Slug | Description | Scope |
|----------|------|-------------|-------|
| Design Principles | `design-principles` | The cross-cutting "theorems" that govern all visual domains | Hierarchy, contrast, rhythm/repetition, scale/proportion, balance (symmetrical, asymmetrical, radial), unity/variety, emphasis, movement/flow, pattern, economy/parsimony. These span every other category. |

#### Layer 2 — Domain Knowledge

| Category | Slug | Description | Scope |
|----------|------|-------------|-------|
| Colour Theory | `colour-theory` | Colour as a relative, perceptual, and systematic medium | Colour models/spaces (RGB, HSL, OKLCH, CIELAB, Munsell), colour relationships (complementary, analogous, triadic, split-complementary), colour properties (hue, saturation/chroma, lightness/value), colour contrast (Itten's seven), colour temperature, colour psychology, palette construction, colour accessibility (WCAG contrast ratios), perceptual uniformity, colour harmony. |
| Typography | `typography` | The art and system of arranging type | Type anatomy (baseline, x-height, cap height, ascender, descender, counter, serif, terminal), type classification (serif, sans-serif, monospace, display, variable), type systems/scales (modular scales, fluid type), typographic hierarchy, pairing principles, measure/line-length, leading/line-height, tracking/letter-spacing, kerning, optical sizing, paragraph composition, responsive typography, web font loading, variable font axes. |
| Layout & Composition | `layout-composition` | The organisation of elements within a defined space | Grid systems (column grids, modular grids, baseline grids), spatial relationships, whitespace/negative space as structural element, alignment (optical vs. mathematical), responsive strategies (breakpoints, fluid/intrinsic design, container queries), CSS layout models (flexbox, grid, flow), aspect ratios, viewports, z-axis/layering, the fold, content choreography. |
| Interaction Design | `interaction-design` | How interfaces communicate state, possibility, and response | Affordances, signifiers, mapping, feedback, constraints, conceptual models, mental models, discoverability, progressive disclosure, state communication (hover, active, focus, disabled, loading, error, empty), microinteractions, transition design, input methods, direct manipulation, recognition vs. recall. |
| Motion Design | `motion-design` | Movement as communication and spatial reinforcement | Animation principles (easing curves, timing, duration), choreography, enter/exit transitions, state transitions, loading patterns, scroll-driven effects, physics-based motion (spring, decay), meaningful motion vs. decorative motion, motion and accessibility (prefers-reduced-motion), CSS animations vs. JavaScript animation, cubic-bezier functions. |
| Information Architecture | `information-architecture` | The structural organisation of content for findability and comprehension | Content hierarchy, navigation patterns (global, local, contextual, breadcrumb), progressive disclosure, card sorting, mental models of structure, task-driven vs. data-model-driven organisation, search vs. browse, information scent, labelling systems, taxonomy design, wayfinding. |
| Data Visualisation | `data-visualisation` | The visual encoding of quantitative and categorical information | Visual encoding channels (position, length, angle, area, colour, shape), chart type selection, Tufte's principles (data-ink ratio, chartjunk, lie factor), perceptual effectiveness rankings (Cleveland & McGill), annotation, responsive data vis, accessibility in data vis. |
| Imagery | `imagery` | Photography, iconography, and illustration as design elements | Photography direction (framing, lighting, colour grading, subject), iconography systems (outlined, filled, duotone, size grids), illustration style, image treatment (aspect ratios, cropping, masking, filters), hero images, decorative vs. informational images, alt text, image formats and performance. |

#### Layer 3 — Systems & Implementation

| Category | Slug | Description | Scope |
|----------|------|-------------|-------|
| Design Systems | `design-systems` | The architecture of scalable, consistent design | Design tokens (primitive, semantic, component), token architecture (JSON/YAML, Style Dictionary, DTCG spec), atomic design (atoms → molecules → organisms → templates → pages), component API design (props, variants, states, slots), spacing systems, naming conventions, design system governance, Figma↔code pipelines, theming, multi-brand systems. |
| Accessibility | `accessibility` | Inclusive design as a systematic quality dimension | WCAG 2.2 principles (perceivable, operable, understandable, robust), colour contrast requirements (AA, AAA), focus management, keyboard navigation, screen reader patterns (ARIA roles, landmarks, live regions), cognitive accessibility, motor accessibility (target sizes, Fitts's Law applied), reduced motion, high contrast mode, responsive text sizing, semantic HTML. |
| Visual Identity | `visual-identity` | The extractable knowledge of brand expression through visual means | Logo construction (grids, clear space, minimum size), identity systems (primary/secondary marks, lockups), visual language (how a brand uses colour, type, imagery, and motion consistently), tone through visual design, brand guidelines as design system extension. Renamed from "brand identity" to focus on the visual-design-extractable knowledge rather than brand strategy. |

### 2.2 Orthogonality Notes

These notes address structural tensions an ontology engineer would flag:

1. **Visual Perception ↔ Layout & Composition**: Gestalt principles *are* the perceptual laws governing layout. Resolution: Keep separate. Visual Perception cards explain the perceptual mechanisms (the "science"); Layout & Composition cards explain how to *exploit* those mechanisms (the "engineering"). Cross-reference heavily using `related` relationships.

2. **Accessibility as cross-cutting concern**: Accessibility touches every category (colour contrast in `colour-theory`, target sizes in `interaction-design`, motion sensitivity in `motion-design`). Resolution: Model accessibility as both a standalone category (for WCAG-specific, accessibility-first concepts) AND as a facet within other categories. Each domain category should include accessibility-relevant concepts with `related` links to the corresponding accessibility card. Use the `accessibility` category for concepts whose *primary* identity is accessibility.

3. **Design Principles as cross-cutting**: Hierarchy, contrast, rhythm, proportion, and balance appear in every domain. Resolution: Create standalone concept cards in `design-principles` that explain the general principle, with `related` links to domain-specific manifestations. For example: a `visual-hierarchy` card in `design-principles` links to `typographic-hierarchy` in `typography`, `colour-hierarchy` in `colour-theory`, and `spatial-hierarchy` in `layout-composition`.

4. **Visual Identity abstraction level**: Brand identity sits at a higher abstraction level than colour theory or typography — it's an application context drawing on multiple lower-level domains. Resolution: Renamed to `visual-identity` and scoped to extractable visual-design knowledge (logo construction, identity systems, visual language) rather than brand strategy. Cards in this category will have many `prerequisites` from lower-level categories.

5. **Data Visualisation breadth**: Data vis is an entire field; we cannot be exhaustive. Resolution: Focus extraction on the perceptual foundations (encoding effectiveness, preattentive processing applied to charts) and the design-system integration aspects (charting as component, colour in data vis). Defer specialised statistical graphics to a future extension.

6. **Generic vs. source-specific concepts.** Universal concepts (hue, chroma, value, complementary colours) exist independently of any particular colour system or theorist. Source-specific concepts (Munsell's notation system, Itten's seven contrasts, Albers's transparency exercises) are contributions of a particular source. During extraction, use generic slugs for universal concepts and source-prefixed slugs for source-specific constructs. The test: "Would this concept exist with the same definition outside this particular system?" If yes → generic slug. If no → source-prefixed slug. Multiple sources defining the same generic concept is expected and will be reconciled during harmonisation.

### 2.3 Cross-Cutting Concept Cards

The following concepts should be extracted as standalone cards in `design-principles` with `related` links across multiple categories. These are the "theorems" of visual design — they derive from Layer 0 perception science and govern all Layer 2 domain knowledge:

- `visual-hierarchy` — How visual properties establish reading order and importance
- `contrast` — The principle of differentiation across all visual dimensions
- `rhythm-and-repetition` — Predictable recurrence creating pattern and expectation
- `scale-and-proportion` — Relative sizing and the ratios that govern it
- `balance` — Visual equilibrium (symmetrical, asymmetrical, radial)
- `unity-and-variety` — Coherence vs. interest; the fundamental design tension
- `emphasis` — Directing attention to focal points
- `visual-flow` — Guiding the eye through a composition
- `economy` — Minimum sufficient means; parsimony as design principle
- `consistency` — Same meaning, same treatment; the design equivalent of referential transparency
