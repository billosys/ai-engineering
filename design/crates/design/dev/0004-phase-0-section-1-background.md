# Phase 0 - Section 1 - Background

*How This Project Arose and Why Phase 0 Matters*

All of the "Phase 0" documents taken as a whole provide the complete Phase 0 package for concept card extraction across the visual design domain. It is designed to be used alongside the general extraction methodology ([0002 — Parallel Concept Card Extraction v3](crates/design/dev/concept-cards/0002-a-guide-for-parallel-concept-card-extraction-v3.md)) and the practical howto guide ([0003 — Concept Card Extraction with Claude Code](crates/design/dev/concept-cards/0003-howto-concept-card-extraction-with-claude-code.md)).

## The Problem

This knowledge engineering project exists because of a specific, recurring frustration: a senior software engineer with 40+ years of coding experience and a genuine art background finds themselves unable to bridge the gap between *perceiving* good design and *constructing* it systematically.

The symptoms are familiar to any technically sophisticated builder who has tried to ship polished web applications or execute a brand refresh without formal design training:

- Templates and starter kits feel clichéd — the good ones are generic, the bad ones aren't worth discussing
- Custom work stalls because the builder can *see* that something is wrong but can't articulate *why* or systematically *fix* it
- Conversations with designers (or with AI about design) are hampered by a missing pattern language — the trade vocabulary that trained designers use to reason about visual decisions
- Design decisions feel like artistic intuition rather than the principled, repeatable engineering decisions they actually are

This isn't a knowledge problem in the usual sense. The target user has a highly developed aesthetic sense (more so than most engineering peers), deep mathematical fluency (group theory, type theory, category theory), post-doctoral-level music theory, and decades of software architecture experience. What's missing is the *formal vocabulary*, the *systematic frameworks*, and the *decision procedures* that would let them leverage what they already know.

## Why a Knowledge Base (and Why This Methodology)

The target user has already built — in collaboration with an AI partner — a series of concept-card knowledge bases covering graduate-level mathematics, post-doctoral music theory, advanced Rust programming, and more. These knowledge bases are backed by in-memory full-text search, graph databases, and vector databases, and they power multi-RAG AI expert systems that consistently produce results peers describe as extraordinary.

The methodology behind these systems has been refined through formal critique against six decades of ontology engineering and knowledge engineering research. The concept card format — atomic knowledge units with typed relationships, confidence scoring, competency questions, and tiered classification — has proven remarkably effective at making complex domains accessible to AI systems while remaining human-readable.

Visual design deserves the same treatment. The research conducted in Phase 0 confirms what the target user suspected: **visual design possesses formal structure, empirical grounding, and mathematical depth fully comparable to graduate-level mathematics or post-doctoral music theory.** It is not a "soft" discipline — it has psychophysical laws (Stevens's Power Law, Weber-Fechner), mathematical absolutes (the 17 wallpaper groups classifying all possible 2D repeating patterns), computational formalisations of perceptual grouping (Kubovy & Wagemans's Pure Distance Law), and rigorous cross-domain isomorphisms with music theory (equal temperament ↔ perceptual colour uniformity) and software engineering (design tokens ↔ abstraction, component props ↔ API design).

The knowledge base approach is superior to alternatives (taking a course, reading books linearly, following tutorials) because:

1. **It's queryable** — the MCP server lets the AI partner traverse the concept graph, answer competency questions, and assemble decision frameworks on demand, without consuming context on material that isn't relevant to the current task
2. **It's structured** — typed relationships (prerequisites, extends, related, contrasts_with) create a navigable graph rather than a flat collection of facts
3. **It bridges domains** — the Rosetta Stone framework explicitly maps design concepts to the user's existing expertise in engineering, mathematics, and music theory, converting new vocabulary into familiar structures
4. **It scales** — new sources can be extracted and ingested incrementally without restructuring what already exists

## The Phases

The full project proceeds through five phases:

### Phase 0: Research Foundation & Domain Specification ← YOU ARE HERE

Define the domain taxonomy, competency questions, notation conventions, tier definitions, source prioritisation, and the Rosetta Stone framework. This is the architectural blueprint — every subsequent phase depends on it.

### Phase 1: Source Acquisition & Conversion

Acquire the primary sources (books, websites, design system documentation) and convert them to clean Markdown using the marker PDF tool and web capture workflows. Output: `sources-md/<source-slug>/` directories with chapter-level `.md` files ready for extraction.

### Phase 2: Concept Card Extraction

Using the parallel extraction methodology (5 Opus agents per source), extract atomic concept cards from each source in wave order. Each wave is fully extracted, validated (structural checks, consistency checks, CQ coverage), and corrected before the next wave begins. Output: `concept-cards/visual-design/` with hundreds of validated `.md` files.

### Phase 3: Knowledge Base Ingestion & Infrastructure

Ingest the validated concept cards into the graph database (typed relationships become edges), full-text search index (for keyword discovery), and vector store (for semantic similarity). Build the MCP server that exposes graph traversal, FTS, and vector search to the AI partner. Output: a running MCP server the AI can query without exhausting context.

### Phase 4: Guide Generation & Skill Creation

With the knowledge base queryable, generate the four guide types (Pattern Language, Decision Framework, Critique Protocol, Rosetta Stone) by traversing the concept graph. Create Claude skills that leverage the knowledge base for specific tasks: palette evaluation, layout critique, type system design, component API review. Output: guides in `guides/visual-design/` and skills ready for deployment.

## Why Phase 0 Is Critical

Phase 0 is the most important phase because **every error here propagates through all subsequent phases**:

- A **wrong taxonomy category** means concept cards get misclassified, graph edges connect the wrong clusters, and guides assemble incoherent groupings. Fixing this after extraction means re-classifying hundreds of cards.
- A **missing competency question** means an entire knowledge need goes unaddressed — the extraction agents don't know to look for those concepts, so they don't extract them. The gap isn't discovered until a guide fails to assemble.
- A **wrong tier assignment** means prerequisite chains are broken — foundational guides accidentally reference advanced concepts, or advanced guides laboriously re-explain fundamentals.
- A **missing Rosetta Stone mapping** means the target user's most powerful learning accelerator (connecting new vocabulary to existing expertise) is left on the table.
- A **wrong source prioritisation** means the first wave of extraction doesn't address the most pressing knowledge gaps, delaying practical value.

The research that feeds this phase examined how design education programs structure their curricula, how major design systems organise their documentation, what mathematical structures underpin visual perception, and where rigorous cross-domain bridges exist. It was conducted with the same intellectual seriousness applied to the user's mathematics and music theory knowledge bases — because the domain deserves it, and because anything less would produce a knowledge base that fails at the point of use.

## Target User Profile

The knowledge base serves a specific user archetype that should inform every extraction decision:

- **Senior software engineer / CTO** with 40+ years of coding experience
- **Studied art seriously** in secondary school; considered art school; has highly developed aesthetic perception relative to engineering peers
- **Deeply mathematical**: fluent in group theory, type theory, category theory, homotopy type theory
- **Deep music theory background**: post-doctoral level knowledge; understands intervals, temperament, harmonic relationships, counterpoint
- **Advanced programming**: Rust, Java, web technologies
- **The gap**: Can *see* when a design works or doesn't, but lacks the formal vocabulary, pattern language, systematic frameworks, and decision procedures that trained designers use. Cannot reliably *construct* solutions from first principles or articulate *why* something works.
- **The goal**: First-principles access to visual design as a rigorous discipline — not tips and tricks, but the axiomatic structure, theorems, and proof techniques of the field.

**Extraction implication**: Every concept card should, where applicable, connect to mathematical structures, software engineering parallels, or music theory analogues. The user doesn't need design dumbed down — they need it translated into frameworks they already command.
