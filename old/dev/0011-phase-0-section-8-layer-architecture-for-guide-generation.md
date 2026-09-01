# Phase 0 - Section 8 - Layer Architecture for Guide Generation

## 8. Layer Architecture for Guide Generation

After concept cards are extracted and ingested into the graph DB, guides will be synthesised by traversing the concept graph. This section defines the guide types and their relationship to the taxonomy.

### 8.1 Guide Type A: Pattern Language Guides

**Purpose**: Give the user the vocabulary and mental models of trained designers.

**Generation method**: For each cluster of related terms in the concept graph, generate a narrative that introduces the terms in dependency order, explains their relationships, and provides recognition examples.

**Examples**:

- "The Language of Visual Hierarchy" — traverses `visual-hierarchy`, `typographic-hierarchy`, `colour-hierarchy`, `spatial-hierarchy`, `visual-weight`, `emphasis`, `de-emphasis`
- "Talking About Colour" — traverses `hue`, `saturation`, `chroma`, `lightness`, `value`, `colour-temperature`, `colour-harmony`, `simultaneous-contrast`
- "The Vocabulary of Space" — traverses `whitespace`, `negative-space`, `padding`, `margin`, `gap`, `measure`, `leading`, `tracking`

### 8.2 Guide Type B: Decision Framework Guides

**Purpose**: Give the user systematic procedures for common design decisions.

**Generation method**: Follow `prerequisites` chains and `related` edges across categories to assemble all concepts relevant to a specific design task. Structure as decision trees or evaluation checklists.

**Examples**:

- "Choosing a Colour Palette for a SaaS Application" — pulls from `colour-theory`, `accessibility`, `design-systems`, `visual-identity`
- "Designing a Type System from Scratch" — pulls from `typography`, `design-systems`, `layout-composition`
- "Evaluating Navigation Structure" — pulls from `information-architecture`, `interaction-design`, `accessibility`

### 8.3 Guide Type C: Critique Protocol Guides

**Purpose**: Give the user structured analytical lenses for evaluating designs.

**Generation method**: Assemble diagnostic competency questions by category and tier into systematic evaluation rubrics.

**Examples**:

- "The 6-Point Developer Design Audit" — based on the six most common developer design mistakes (CQs 18, 19, 20, 30, 31, 46)
- "Evaluating a Landing Page" — systematic hierarchy, colour, typography, spacing, interaction, and accessibility review
- "Reviewing a Component Library" — design system architecture, token consistency, API design, state coverage

### 8.4 Guide Type D: Rosetta Stone Guides

**Purpose**: Map the user's existing mental models to design terminology.

**Generation method**: Collect all concept cards with cross-domain connections, group by source domain (engineering, music, mathematics, art), and generate narrative bridges.

**Examples**:

- "Design for Engineers: The Concepts You Already Know" — all RIGOROUS software engineering mappings
- "What Your Music Theory Teaches You About Design" — all music theory mappings, distinguishing RIGOROUS from STRUCTURAL from LOOSE
- "The Mathematics of Visual Design" — all mathematical formalisations, from group theory to information theory
