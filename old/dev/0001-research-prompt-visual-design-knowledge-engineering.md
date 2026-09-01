# Research Prompt: Visual Design Knowledge Engineering

*Foundations for Concept Card Extraction*

## Context for the Research Agent

You are conducting deep research to support a knowledge engineering project. The goal is to build a comprehensive, multi-source concept card knowledge base covering visual design, UI/UX, colour theory, typography, layout, and related disciplines — aimed at a very specific user profile:

**The target user** is a senior software engineer / CTO with 40+ years of coding experience who also studied art seriously in high school. They have strong visual perception and aesthetic intuition but lack the formal vocabulary, pattern language, and systematic frameworks of trained designers. They can *see* when something works or doesn't, but can't always articulate *why* or systematically *construct* solutions. They are deeply mathematical and respond well to principled, first-principles explanations.

**The methodology** uses a rigorous concept card extraction process (inspired by ontology engineering, library science, and cognitive architecture research) to create atomic knowledge units from primary sources. These cards are ingested into graph databases and vector stores, then used by AI systems via MCP servers to power expert-level guidance. The cards have typed relationships (prerequisites, extends, related, contrasts_with), confidence scoring, competency questions, and tiered classification (foundational/intermediate/advanced).

**What we need from you**: Rigorous, detailed, source-attributed research across the domains listed below. Your output will be used to write the Phase 0 document (domain taxonomy, competency questions, notation conventions, tier definitions, source prioritisation) that guides the actual concept card extraction.

---

## Research Tasks

### 1. Domain Taxonomy Validation & Refinement

We have a preliminary taxonomy for visual design knowledge. Research whether this is well-structured, what's missing, and how the field itself organises this knowledge. Look at how design education programs (university level), professional certification bodies, and major design systems documentation structure their knowledge.

**Preliminary taxonomy to validate/improve:**

- `colour-theory` (colour relationships, colour systems, palette construction, colour psychology, colour accessibility)
- `typography` (type anatomy, type classification, type systems/scales, pairing, hierarchy, responsive typography, variable fonts)
- `layout-composition` (grids, spatial relationships, responsive strategies, breakpoints vs. intrinsic design, whitespace/negative space)
- `visual-perception` (gestalt principles, visual weight, optical effects, figure-ground, perceptual grouping)
- `interaction-design` (affordances, feedback loops, mental models, motion/animation, state communication, microinteractions)
- `information-architecture` (hierarchy, progressive disclosure, navigation patterns, content strategy, wayfinding)
- `design-systems` (design tokens, component architecture, atomic design, spacing systems, naming conventions, governance)
- `accessibility` (WCAG guidelines, colour contrast, cognitive load, motor considerations, screen reader patterns, inclusive design)
- `brand-identity` (visual identity, consistency, differentiation, emotional resonance, voice & tone as design element)

**Specific questions to answer:**

- Are these categories well-supported by how the field is actually structured?
- What significant subcategories are we missing?
- How do leading design education programs (e.g., RISD, RCA, Parsons, CMU HCI, Stanford d.school) organise their curricula? What categories do they use?
- How do major design systems (Material Design 3, IBM Carbon, Shopify Polaris, GitHub Primer, Apple HIG) organise their documentation? What taxonomy emerges?
- Are there cross-cutting concerns that don't fit neatly into one category (e.g., "visual rhythm" spans typography, layout, and colour)?
- What would an ontology engineer say about the orthogonality and exhaustiveness of these categories?

### 2. Foundational Source Analysis

For each of the following sources, research their specific contributions, what unique knowledge they contain, their standing in the field, and what concepts are extractable. We need enough detail to write competency questions and prioritise extraction order.

**Colour Theory:**

- Josef Albers, *Interaction of Color* — What specific frameworks/experiments does it introduce? What are its core principles? How is it structured?
- Johannes Itten, *The Art of Color* — The seven colour contrasts, colour harmonies, the colour star. How does this differ from/complement Albers?
- The Munsell Color System — Its three dimensions, how it maps to digital colour, why it matters for designers
- OKLCH / OKLAB colour spaces — Technical details, why they're superior to HSL for perceptual uniformity, current browser/CSS support
- Any other seminal colour theory sources the field considers essential

**Typography:**

- Robert Bringhurst, *The Elements of Typographic Style* — Structure, core principles, what makes it canonical
- Ellen Lupton, *Thinking with Type* — How it differs from Bringhurst, what practical knowledge it adds
- Tim Brown's Modular Scale — The mathematical basis, common ratios, how they relate to musical intervals
- Matthew Butterick, *Practical Typography* — Key principles, web-specific guidance
- Any other seminal typography sources

**Layout & Composition:**

- Josef Müller-Brockmann, *Grid Systems in Graphic Design* — The mathematical grid construction methods, multi-column systems
- Massimo Vignelli, *The Vignelli Canon* — Core philosophy, the intangibles/tangibles framework
- Jan Tschichold, *The New Typography* — Historical significance, asymmetric layout principles
- Every Layout (every-layout.dev) — The "intrinsic design" approach, key layout primitives
- Utopia (utopia.fyi) — Fluid type and space, the mathematical interpolation approach

**UI/UX & Interaction:**

- Don Norman, *The Design of Everyday Things* — Core concepts (affordances, signifiers, mapping, feedback, mental models, conceptual models)
- Steve Krug, *Don't Make Me Think* — Core heuristics, the usability testing approach
- Refactoring UI (refactoringui.com) — Structure, key tactical patterns, how it bridges developer-to-designer gap
- Laws of UX (lawsofux.com) — Complete list of laws, their psychological foundations, practical applications
- Nielsen Norman Group — Key foundational articles and research findings that are considered canonical

**Visual Perception & Psychology:**

- Rudolf Arnheim, *Art and Visual Perception* — Gestalt principles as applied to art/design, visual thinking
- Colin Ware, *Information Visualization: Perception for Design* — Preattentive processing, visual encoding effectiveness rankings

**Design Systems:**

- Brad Frost, *Atomic Design* — The five levels, how they map to component architecture
- Nathan Curtis's design system methodology — Design tokens, spacing scales, system governance

**Web-Specific Craft:**

- Josh Comeau (joshwcomeau.com) — Key CSS mental models, interactive teaching approach
- Stephanie Eckles (moderncss.dev) — Modern CSS patterns and solutions
- Smashing Magazine's design books — Which are most valuable and why

### 3. Competency Question Research

We need to generate 40-60 competency questions organised by type (definitional, relational, procedural, prerequisite, diagnostic). These should reflect:

- What a technically sophisticated person building real web applications actually needs to know
- Questions at all three tiers (foundational, intermediate, advanced)
- Questions that bridge the gap between "I can see it" and "I can build it"
- Questions that a trained designer would consider essential vs. nice-to-know

**Research what questions design education programs use for assessment.** Look at:

- University design course learning objectives and exam questions
- Professional design certification criteria (if any exist)
- Common interview questions for senior product designers
- The questions that design system documentation implicitly answers
- What Refactoring UI and similar "design for developers" resources identify as the key knowledge gaps

**Also research: what are the most common and most consequential mistakes that developers make when designing without formal training?** These will generate diagnostic competency questions.

### 4. Mathematical & Scientific Underpinnings

Given the user's strong mathematical background, research the formal/mathematical dimensions of design that would resonate:

- **Colour science**: CIE colour spaces, colour difference formulas (ΔE), metamerism, chromatic adaptation. The mathematical structure of perceptually uniform colour spaces (CIELAB, OKLAB). How colour quantisation works.
- **Typographic mathematics**: The golden ratio in typography (and its debunking/nuancing), modular scales and their basis in musical intervals (perfect fourth = 4:3, perfect fifth = 3:2, etc.), the mathematical relationship between x-height, cap height, and line height.
- **Grid mathematics**: Müller-Brockmann's mathematical grid construction, the relationship between column count, gutter width, and margin. How modular grids create proportional systems.
- **Gestalt as perceptual computation**: Proximity as distance function, similarity as feature matching, closure as interpolation, continuity as curve fitting. Research on the computational models of gestalt perception.
- **Information theory in design**: Signal-to-noise ratio applied to visual communication, Tufte's data-ink ratio, the relationship between entropy and visual complexity.
- **Fitts's Law, Hick's Law, and other quantitative UX laws**: Their actual mathematical formulations, not just the popular simplifications. Boundary conditions and when they break down.

### 5. Cross-Domain Pattern Mapping (The "Rosetta Stone")

Research explicit connections between:

- **Art concepts → Design terminology**: How concepts from fine art training (composition, value, colour temperature, figure-ground, focal point, visual flow) map to their design/UX equivalents
- **Engineering concepts → Design terminology**: How concepts from software engineering (abstraction, modularity, separation of concerns, DRY, naming conventions, API design) map to design system concepts
- **Mathematics → Design**: Where mathematical structures (group theory, topology, category theory) have direct analogues in design (symmetry groups in pattern design, topological properties of layout, morphisms between design states/breakpoints)
- **Music theory → Design**: Given the user also has a deep music theory background — research parallels between musical concepts (harmony, rhythm, counterpoint, tension-resolution, voicing) and visual design concepts. These analogies are often made loosely; find where they hold rigorously.

### 6. Notation & Representation Conventions

Research the standard notations used in professional design practice:

- **Colour notation**: When to use hex vs. RGB vs. HSL vs. OKLCH vs. named colours. Industry conventions for documenting colour palettes and colour relationships.
- **Typography notation**: How typographic specifications are documented (font-size/line-height shorthand, tracking units, optical sizing parameters). Design token naming conventions for type scales.
- **Spacing notation**: 4-point grid, 8-point grid, the arguments for each. How spacing scales are documented. The t-shirt sizing convention vs. numerical scales.
- **Responsive notation**: How breakpoints, fluid ranges, and container queries are documented. Utopia's clamp() notation.
- **Component notation**: How components are specified in design systems (props, variants, states). The relationship between Figma's component model and code component APIs.

### 7. Current State of the Art (2024-2025)

Research the most current developments that our knowledge base should reflect:

- **CSS capabilities**: What's now possible in CSS that changes design patterns (container queries, :has(), view transitions, scroll-driven animations, subgrid, relative colour syntax)?
- **Design tooling**: Current state of Figma, design token tooling, style dictionary, design-to-code pipelines
- **AI in design**: How AI is currently being used in design workflows (not just generation — analysis, accessibility auditing, design system enforcement)
- **Variable fonts**: Current state, browser support, how they change typographic practice
- **Colour in CSS**: The oklch() function, relative colour syntax, colour-mix(), wide-gamut displays

### 8. Source Availability & Acquisition Research

For each recommended source, determine:

- Is a PDF or ebook version legally available for purchase?
- What format (PDF, EPUB, etc.)?
- Approximate page count and structural complexity (for estimating extraction effort)
- Are there companion websites or free online resources that supplement the book?
- For web-native sources (Every Layout, Utopia, Laws of UX, etc.) — what's the content structure and how might it best be captured?

---

## Output Format

Structure your research output as a single comprehensive document with clear sections matching the research tasks above. For each section:

1. **Lead with findings** — State what you found, with specifics
2. **Cite sources** — URL, author, publication, date where possible
3. **Note confidence** — Flag where information may be outdated or uncertain
4. **Include direct quotes sparingly** — Only when the exact wording matters for accuracy
5. **Recommend actions** — What should we do with this finding?

**Target length**: Be thorough. This is the research foundation for the entire project. 5,000-10,000 words is appropriate. Depth over breadth — it's better to be deeply rigorous on the most important topics than to skim everything.

**Priority order** if you must triage:

1. Domain taxonomy validation (this structures everything else)
2. Competency questions (these define what we extract)
3. Source analysis (what's in each book, specifically)
4. Mathematical underpinnings (the unique value-add for this user)
5. Rosetta Stone mappings (the bridge to existing knowledge)
6. Notation conventions
7. Current state of the art
8. Source availability

---

## What NOT to Do

- Don't generate concept cards — that's a later phase
- Don't write the Phase 0 document — we'll do that collaboratively
- Don't summarise sources you haven't actually researched — flag gaps honestly
- Don't sacrifice rigour for coverage — we need depth on the important things
- Don't assume standard design knowledge — verify and cite

---

## Final Note

The person who will use this research output has built concept-card knowledge bases for graduate-level mathematics (group theory, type theory, category theory, homotopy type theory), post-doctoral music theory, and advanced programming languages. The bar for rigour is extremely high. The design domain should be treated with the same intellectual seriousness as those domains — not as a "soft" discipline but as a field with its own formal structures, empirical foundations, and deep principles. Meet that bar.
