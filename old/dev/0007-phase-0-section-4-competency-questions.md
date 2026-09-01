# Phase 0 - Section 4 - Competency Questions

## 4. Competency Questions

56 questions across five types and three tiers. These define what the knowledge base must be able to answer and drive extraction priorities.

### 4.1 Foundational Tier — Core Vocabulary and First Principles

#### Definitional (11 questions)

1. What is visual hierarchy, and what visual properties (size, colour, contrast, weight, spacing) establish it?
2. What are the gestalt principles of perceptual grouping, and how does each one work?
3. What is the difference between hue, saturation/chroma, and lightness/value?
4. What are the three components of HSL, and why is HSL more useful than hex notation for palette construction?
5. What are the basic anatomical parts of a letterform (baseline, x-height, cap height, ascender, descender, counter)?
6. What distinguishes a serif typeface from a sans-serif, and what are the historical/functional reasons for each?
56. What typographic conventions and details — such as proper quotation marks, correct dash usage, appropriate sentence spacing, and considered hyphenation — distinguish professionally typeset text from default or amateur formatting, and why do they matter for perceived quality?
7. What is a grid system, and what problem does it solve in visual composition?
8. What is an affordance (in Norman's corrected sense), and how does it differ from a signifier?
9. What is a design token, and how does it differ from a hard-coded value?
10. What does WCAG stand for, and what are its four principles (POUR)?
11. What distinguishes a spacing system from arbitrary padding values — what problem does constraint solve?

#### Relational (6 questions)

1. How do font weight, colour, and spacing work *together* with font size to create typographic hierarchy — why is size alone insufficient?
2. How does the relationship between inter-group and intra-group spacing communicate which elements belong together (gestalt proximity)?
3. How does the visual-elements concept of "value" (light-dark range) connect to colour theory's "lightness" and to contrast as a design principle?
4. How do CSS custom properties relate to design tokens — what is the mapping between the design concept and its implementation?
5. What is the relationship between Fitts's Law and minimum touch target sizes in mobile design?
6. How does the Weber-Fechner Law explain why spacing and type scales must be geometric (multiplicative) rather than arithmetic (additive)?

#### Diagnostic (4 questions)

1. A card layout uses 16px padding inside cards, 16px between cards, and 16px between card title and body text. Everything feels "flat." What principle was violated, and what's the fix?
2. A page uses five different font sizes (13px, 15px, 17px, 22px, 31px) with no apparent pattern. What's wrong, and what system would fix it?
3. A developer says "I tried making it look good by adding more colours." The result looks chaotic. What foundational principle are they missing?
4. A button and a text link are styled identically (same colour, no border or background difference). A user hesitates before clicking. What's missing?

### 4.2 Intermediate Tier — Applied Knowledge and Pattern Recognition

#### Procedural (8 questions)

1. Given a data-rich card (title, status badge, three metrics, timestamp, action button), how do you assign visual hierarchy: what gets the most weight, what gets de-emphasized, and why?
2. How do you construct a colour palette starting from a single brand colour using OKLCH? What systematic steps ensure adequate contrast and accessible combinations?
3. How do you choose a modular scale ratio for a type system? What factors determine whether a 1.2 (minor third) or 1.333 (perfect fourth) ratio is appropriate?
4. How do you design the states of an interactive component (default, hover, active, focus, disabled, loading, error)? What visual properties change for each state, and why?
5. How do you ensure a coloured status badge communicates its meaning without relying solely on colour? What redundant encoding strategies exist?
6. How do you evaluate and select a typeface pairing for a web application? What properties should contrast, and what should harmonise?
7. How do you create a spacing scale for a design system? What base unit, what progression, and what naming convention?
8. How do you structure navigation for an application with 30+ distinct views? What IA principles govern the decision?

#### Diagnostic (8 questions)

1. A dashboard uses teal header, red error badges, green success indicators, blue links, yellow warning banners, and purple notification badges. It looks like a "clown car." What principle was violated, and how do you fix it?
2. A form uses identical 8px spacing between every element (label-to-input, input-to-input, section-to-section). Why does it look wrong? What spacing variation communicates structure?
3. A sidebar navigation has 24 equally-styled links. Users can't find anything. What's the diagnosis, and what visual/structural techniques address it?
4. A landing page hero section uses a 14px body font, a 16px heading, and a 14px subheading. Why does it feel like nothing stands out?
5. A dark-mode implementation simply inverts all colours. Text on some backgrounds becomes unreadable. What went wrong?
6. An icon set mixes outlined and filled styles, some at 16px and some at 24px, some with rounded corners and some with sharp corners. It feels "off." What principle was violated?
7. A mobile app puts the primary action button at the top-right corner of the screen. Users on large phones struggle to reach it. What law was violated?
8. A registration form asks for 12 fields on a single page. Completion rates are low. What principle applies, and what design pattern addresses it?

### 4.3 Advanced Tier — Systematic Thinking and Cross-Domain Integration

#### Relational (8 questions)

1. How does a well-structured design token system map onto CSS custom properties? What is the isomorphism between design decisions and code architecture?
2. How does cognitive load theory (intrinsic, extraneous, germane) relate to progressive disclosure and visual hierarchy? When is simplification harmful?
3. How does the temperament problem in music theory (uniformising a perceptually non-uniform space) map precisely to the perceptual uniformity problem in colour science (CIELAB → OKLAB)?
4. How do the 17 wallpaper groups from group theory classify all possible repeating 2D patterns, and what does this mean for CSS `background-repeat` and pattern design?
5. How does the software engineering principle of "composition over inheritance" manifest in CSS layout (Every Layout's approach) and in design system component architecture?
6. How does Stevens's Power Law (ψ = k × Iⁿ) with its compressive exponent for visual area (n ≈ 0.7) explain why perceived size doesn't scale linearly — and what does this imply for icon sizing, spacing scales, and data visualisation?
7. How does the three-tier token architecture (primitive → semantic → component) map onto the concept of abstraction layers in software engineering?
8. What is the relationship between Hick's Law (RT = a + b × log₂(n+1)) and the design of navigation, search interfaces, and progressive disclosure — and when does it break down (Leonard's finding on high stimulus-response compatibility)?

#### Diagnostic (6 questions)

1. An admin panel organises its UI by database tables — Users page, Orders page, Products page, each showing all columns in a table. Users complain they can't get their work done efficiently. Diagnose the fundamental mistake and propose the restructuring principle.
2. A design system defines 47 colour tokens but has no semantic layer — components reference `blue-500` directly rather than `color-primary`. What breaks when the brand colour changes? What architectural principle was violated?
3. A component library has a `<Card>` component with 23 boolean props (hasShadow, hasHeader, hasFooter, isCompact, isHighlighted...). Developers constantly misconfigure it. What's the design system architecture problem, and what pattern fixes it?
4. A responsive design uses 6 breakpoints with completely different layouts at each. The CSS is 4,000 lines and breaks constantly between breakpoints. What's the systematic alternative?
5. A team's design system uses a 4px spacing scale but components don't align with each other on the page. Investigating reveals some components use padding from the scale but margin values are ad hoc. What governance principle is missing?
6. A dark theme was implemented by swapping background and foreground colours, but the interface feels "heavy" and fatiguing. The light theme feels balanced. What perceptual principle explains this, and what's the correct approach to dark theme design?

#### Procedural (4 questions)

1. How do you design a complete design token architecture from scratch — from primitive values through semantic aliases to component-level tokens? What decisions must be made at each layer?
2. How do you implement a fluid type and spacing system using CSS `clamp()` and modular scale ratios? What are the mathematical inputs and how do you derive the output declarations?
3. How do you systematically audit an existing interface for visual design quality? What checklist of principles and patterns do you evaluate, in what order?
4. How do you construct a Rosetta Stone mapping between an engineering team's existing mental models (software architecture, API design, type systems) and the design concepts they need to learn? What mappings are rigorous vs. merely metaphorical?

### 4.4 Competency Question Coverage Requirements

Every concept card MUST list at least one competency question in its `answers_questions` field. The following CQs are **high priority** — the concepts that answer them should be extracted with particular care and completeness:

- **CQ 1** (visual hierarchy) — This is the single most important concept for the target user
- **CQ 2** (gestalt principles) — The perceptual foundation for everything
- **CQ 11** (spacing systems) — Addresses the #2 developer mistake
- **CQ 17** (Weber-Fechner and geometric scales) — The mathematical "why" behind spacing
- **CQ 18** (flat spacing diagnostic) — The most common spacing mistake
- **CQ 22** (hierarchy assignment procedure) — The "how do I actually do this" question
- **CQ 23** (OKLCH palette construction) — Procedural colour knowledge
- **CQ 30** (clown car diagnostic) — Addresses the #3 developer mistake
- **CQ 38** (token-to-CSS isomorphism) — The engineering bridge
- **CQ 40** (temperament ↔ perceptual uniformity) — The deepest Rosetta Stone mapping
- **CQ 46** (data-model-driven IA) — Addresses the #5 developer mistake
