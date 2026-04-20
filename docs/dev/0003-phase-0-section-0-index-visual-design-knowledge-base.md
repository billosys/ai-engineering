# Phase 0 Index: Visual Design Knowledge Base

This Phase 0 specification is split across multiple files for manageable context consumption by Claude Code during extraction. Files are ordered by section number and should be read in sequence for full context, though each is self-contained enough to be referenced independently during extraction.

---

| Section | Title | Description | Filename |
|---------|-------|-------------|----------|
| 0 | Document Index | This file. Master index of all Phase 0 specification documents with descriptions and reading order. | `crates/design/dev/0003-phase-0-section-0-index-visual-design-knowledge-base.md` |
| 1 | Background & Target User Profile | How this project arose, what problem it solves, the five-phase roadmap, why Phase 0 is critical, and the target user profile that should inform every extraction decision. | `crates/design/dev/0004-phase-0-section-1-background.md` |
| 2 | Domain Taxonomy | The 13-category taxonomy organised into four layers (perception → principles → domain knowledge → systems & implementation), with category definitions, scope descriptions, orthogonality notes, and cross-cutting concept card specifications. | `crates/design/dev/0005-phase-0-section-2-domain-taxonomy.md` |
| 3 | Tier Definitions | Criteria for foundational/intermediate/advanced classification, with a per-category tier assignment table showing which concepts belong at which level. | `crates/design/dev/0006-phase-0-section-3-tier-definitions.md` |
| 4 | Competency Questions | All 55 competency questions across five types (definitional, relational, procedural, prerequisite, diagnostic) and three tiers, plus the high-priority CQ list that drives extraction focus. The largest section — these define what the knowledge base must answer. | `crates/design/dev/0007-phase-0-section-4-competency-questions.md` |
| 5 | Notation Conventions | Standard representations for colour (hex, OKLCH, tokens), typography (scales, fluid type, DTCG composites), spacing (4pt/8pt grid, t-shirt sizing, semantic aliases), responsive design (breakpoints, clamp(), container queries), and mathematical formulations (Fitts's, Hick's, Stevens's, Weber-Fechner, gestalt, colour transforms). | `crates/design/dev/0008-phase-0-section-5-notation-conventions.md` |
| 6 | Source Prioritisation & Extraction Order | Four extraction waves ordered by strategic value, estimated card counts per source, acquisition details, and source-specific extraction notes (how to handle each source's unique structure and challenges). | `crates/design/dev/0009-phase-0-section-6-source-prioritisation-and-extraction-order.md` |
| 7 | Rosetta Stone Framework | The cross-domain mapping system: rigour classification (RIGOROUS/STRUCTURAL/LOOSE), complete mapping tables for software engineering → design, music theory → design, and mathematics → design, plus the implementation pattern for embedding mappings in concept cards. | `crates/design/dev/0010-phase-0-section-7-the-rosetta-stone-framework.md` |
| 8 | Guide Generation Architecture | The four guide types (Pattern Language, Decision Framework, Critique Protocol, Rosetta Stone) that will be synthesised from concept cards after ingestion, with examples and generation methods for each. | `crates/design/dev/0011-phase-0-section-8-layer-architecture-for-guide-generation.md` |
| 9 | Extraction-Specific Instructions | Concept card template extensions for visual design (layer field, rosetta_stone field, css_implementation field), plus domain-specific agent guidance for parallel extraction. | `crates/design/dev/0012-phase-0-section-9-extraction-specific-instructions.md` |
| 10 | Validation Criteria | Post-extraction validation checklists covering taxonomy coverage, competency question coverage, Rosetta Stone coverage, and layer integrity. | `crates/design/dev/0013-phase-0-section-10-validation-criteria.md` |
| A | Appendices | The Six Developer Design Mistakes (the diagnostic foundation), source acquisition checklist with status tracking, and the project directory structure. | `crates/design/dev/0014-phase-0-section-11-appendices.md` |

---

## Reading Order by Role

**For the extraction coordinator (Claude Code, Phase 1-2):**

- Essential: 00, 01, 02, 03, 04, 05, 09, 10
- Reference: 06, 07, 11

**For guide generation (Claude Code, Phase 4):**

- Essential: 00, 01, 02, 04, 07, 08
- Reference: 03, 05, 06

**For the human project lead (all phases):**

- All documents, in order.
