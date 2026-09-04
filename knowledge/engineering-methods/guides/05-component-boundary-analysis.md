# Component Boundary Analysis

This guide carries the applied-position reasoning split from the former AI Engineering Methodology monolith and extends it with the accepted component-boundary analysis role for engineering-methods. Load it when deciding whether a topic belongs in engineering-methods or in a specialized collaboration-framework component.

This guide is one part of the engineering-methods guide set:

- [01-engineering-methodology.md](./01-engineering-methodology.md) - methodology overview, role adapter, three-pillar frame, and open questions.
- [02-knowledge-substrate.md](./02-knowledge-substrate.md) - distilled knowledge substrate, forms, examples, properties, and anti-patterns.
- [03-process-rigour.md](./03-process-rigour.md) - scales of work, 9-point SDLC, ledgers, audits, anti-degradation, and subagent discipline.
- [04-operational-routing.md](./04-operational-routing.md) - practitioner disciplines and component routing for live work.
- [05-component-boundary-analysis.md](./05-component-boundary-analysis.md) - applied-position reasoning and component-boundary analysis.
- [06-source-package-release-gates.md](./06-source-package-release-gates.md) - source, package, release, validation, and provenance gates.

## Part V — Applied Positions

A methodology should produce positions on live questions in the field. A methodology that produces no positions is not a methodology — it is a vocabulary.

### The LFE OSS question

Lisp Flavoured Erlang, like many open source communities, is currently debating whether LLM-assisted contributions should be permitted, flagged, or rejected. The same question is being asked in Debian, in Curl, in the NetBSD project, in dozens of others — and the debate tends to reduce to a single axis: was this written by a person or by an AI?

Applying the methodology to this question produces a different answer.

**The question "LLM or not?" is the wrong axis.** Provenance of the diff is not a reliable proxy for any of the things the community actually cares about — code quality, maintainability, contributor understanding, review burden, license hygiene.

**The right axes, the ones the methodology surfaces:** Does the contribution meet the quality bar (substrate)? Does the contributor understand what they submitted, well enough to respond to review and maintain it over time (posture — peer frame, honest engagement)? Was the contribution produced with process rigour adequate to its scale (process)?

These questions have always applied to contributions from any source. LLMs simply make the gap between _a person wrote this_ and _a person understands this_ easier to hide. The gap was always there — a copy-pasted Stack Overflow answer, a contribution ghost-written by a more senior colleague, code generated from a template without comprehension — and communities with robust review practices caught it regardless of provenance.

**The methodology's recommendation: better tools and better process, not provenance gates.** Require contributors to sign that they understand what they are submitting, regardless of how it was produced. Maintain a ledger of what was reviewed and by whom, so understanding is traceable. Treat contributions the same regardless of origin — LLM-assisted or not — and hold them to the same quality floor. Invest in review capacity and automated quality checks, which cut the review burden LLMs create without gating contributors out.

This is the author's position, developed through this methodology and submitted to relevant communities. Future readers of this document may arrive at different positions on similar questions, and that is the methodology working as intended — positions fall out of the three pillars; they are not the pillars themselves.

---

## Component-Boundary Analysis

A component boundary should be drawn by the work's primary load reason, not by the nearest familiar noun. Engineering-methods owns the methodology layer: the LLM-centric SDLC, substrate/process/posture interaction, operational routing, boundary analysis, and source/package/release gate concepts. It does not absorb the specialized components that implement those disciplines.

Use these tests before moving material into this component:

- **Method test:** Does the material explain how LLM-assisted engineering work should be structured, evaluated, improved, or routed?
- **Owner test:** Is the material a general method/gate, or is it the detailed operating procedure of project-management, work-verification, testing, code-auditing, agent-coordination, or contribution-style?
- **Selective-load test:** Would a reader load this file without needing a specialized component's full procedure?
- **Package-boundary test:** Can the material survive inside `collaboration-framework.zip` without source-only paths, old monolith routes, or unverified package assumptions?

The accepted Project02/Project04 architecture places ontology critique and boundary analysis here because those questions decide how the framework is carved up. The result should route specialized work outward instead of making engineering-methods a catch-all.
