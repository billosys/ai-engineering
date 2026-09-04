# Knowledge Substrate

This guide carries the knowledge-substrate pillar split from the former AI Engineering Methodology monolith. Load it when the work is about preserving distilled judgment across sessions, sources, concept cards, skill files, or reusable knowledge structure.

This guide is one part of the engineering-methods guide set:

- [01-engineering-methodology.md](./01-engineering-methodology.md) - methodology overview, role adapter, three-pillar frame, and open questions.
- [02-knowledge-substrate.md](./02-knowledge-substrate.md) - distilled knowledge substrate, forms, examples, properties, and anti-patterns.
- [03-process-rigour.md](./03-process-rigour.md) - scales of work, 9-point SDLC, ledgers, audits, anti-degradation, and subagent discipline.
- [04-operational-routing.md](./04-operational-routing.md) - practitioner disciplines and component routing for live work.
- [05-component-boundary-analysis.md](./05-component-boundary-analysis.md) - applied-position reasoning and component-boundary analysis.
- [06-source-package-release-gates.md](./06-source-package-release-gates.md) - source, package, release, validation, and provenance gates.

## Part II — The Knowledge Substrate

### The premise

Tacit practice does not travel. Distilled practice travels.

An expert in a domain carries thousands of small judgments — which pattern to reach for, which idiom to avoid, which corner to worry about. If that expertise is not explicitly captured, it dies with the context: the session ends, the contributor leaves, the codebase ages, and the next person has to rederive everything from first principles.

The substrate is the practice of explicitly capturing distilled judgment in forms that survive.

### Forms the substrate takes

**Concept cards.** Atomic units. One pattern, one rule, or one idiom per card. Each card has an ID (for example `API-12`, `EH-07`, `CLI-33`), a strength indicator (`MUST`, `SHOULD`, `CONSIDER`, `AVOID`), a rationale, a positive example, a negative example, and a link to the upstream source that justifies it.

**Ontological structure.** How the domain is carved up. What counts as a separate concept versus a variant. Which relationships matter — composes-with, conflicts-with, prerequisite-to, supersedes. The ontology is the skeleton the cards hang from.

**Graph relationships.** Cards do not live in isolation; they point at each other. A well-built substrate can answer questions like "which patterns does CA-12 depend on?" or "what conflicts with US-04?" — not just "what does US-04 say?"

**Skill files.** The harvest. The root skill file ([SKILL.md](../SKILL.md)) is what a future reader — Claude, human, both — consults when they need to do a particular thing. It points at the underlying cards, names the selection criteria, and makes the substrate usable.

### Worked example: the Rust regeneration

Between December 2025 and April 2026, we wrote, used extensively, iterated on and then finally fully regenerated the Rust knowledge base from scratch: 21 upstream sources reconciled (the Rust Reference, Rustonomicon, API Guidelines, Performance Book, Async Book, tokio docs, Rustdoc Book, Edition Guide, Cargo Book, Pragmatic Rust, Rust Design Patterns, The Rust Programming Language, The Little Book of Rust Macros, Clippy lints, the Style Guide, the CLI Book, clap's docs, and the Compiler Development Guide, among others), 661 patterns across 17 chapters, 384 concept cards, and a Go-style top-level skill file that makes the whole substrate navigable in a single read.

The work was not "write Rust docs." The work was build a substrate that any future instance of Claude or any future human collaborator can use to write correct, idiomatic, maintainable Rust without rederiving it. A year from now, when the edition moves again or a new async primitive lands, the substrate gets updated — it does not get rebuilt.

### Properties of a good substrate

A good substrate is cumulative: each pass adds or refines; it does not silently overwrite, and historical rationale is preserved. It is portable: no hidden dependencies on tribal knowledge, and a contributor who has never met you can read it and do the work. It is auditable: every claim traces to a source, and "because clippy says so" is a fine rationale if the clippy lint is cited. It is indexed: knowledge exists and can be found when it is needed, because an un-indexed substrate is not a substrate. And it is maintained: updated as the domain moves, because a substrate that rots is worse than no substrate — it misleads with the authority of formalization.

### Anti-patterns

Substrate as deliverable rather than infrastructure. If it is written once and never consulted, it was produced for the wrong audience.

Substrate without rationale. "Do this" without "because this" and without counter-examples produces compliance without judgment.

Substrate without strength indicators. Treating `MUST` and `CONSIDER` as equivalent flattens the thing that made the substrate useful in the first place.

Substrate that the authors do not use themselves. If the cards and skill files are not the first reference the authors reach for, they have become archaeology.

---
