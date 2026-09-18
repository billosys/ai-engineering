---
name: engineering-methods
description: |
  Component framework/operational skill for the AI Engineering Methodology:
  knowledge substrate, collaborative posture, process rigour, and the 9-point
  SDLC. Use when designing how a body of LLM-assisted engineering work should be
  structured, evaluated, or improved; and when converting an approved slice or
  review finding into a detailed, domain-guided CC implementation prompt.
license: MIT
metadata:
  version: "1.15.0"
  hermes:
    tags: [ai-engineering, methodology, sdlc, knowledge-substrate]
    category: meta-skills
---

# Engineering Methods

Use this component when the work needs the methodology itself: the three
pillars, the 9-point SDLC, anti-degradation disciplines, or the conceptual
frame behind project, arc, slice, and ledgered work.

For contributor roles, workflow selection, or handoffs, read the methodology's
[shared invariants and workflow sections](./guides/01-engineering-methodology.md#roles-and-shared-invariants).
The Two-Contributor Workflow is the default. The Operator may explicitly select
the Three-Contributor Workflow for sustained design/review separation or the
One-Contributor Workflow for proportionate single-assistant work. All preserve
scope and evidence honesty; self-checks are not independent acceptance.

Before writing or reviewing a CC implementation assignment, read
[From Slice to Implementation Prompt](./guides/07-implementation-prompt-authoring.md) and use its
[authoring template](./templates/cc-implementation-prompt.md). The prompt author must inspect
source, apply relevant domain guides, resolve consequential choices and supply
an implementation recipe with concrete test oracles before issuing the work.
For investigation/evidence work, supply a concrete method while leaving
unsupported semantic conclusions unresolved. Check interacting rules, viable
test sequences and whether the old behavior would pass the proposed oracles.
A ledger, skill-reading list or collection of plan links is not that recipe.

For CC execution, follow the [required-reading and intake contract](./guides/07-implementation-prompt-authoring.md#required-reading-and-cc-intake):
load required text completely, execute author-scoped structured-data queries,
recover truncated output and record each kind of coverage separately. Produce
a source-cited contract readback before dependent edits. Reading
attestation does not prove comprehension or replace independent review.

Read the guides:

- [Engineering Methodology](./guides/01-engineering-methodology.md)
- [Knowledge Substrate](./guides/02-knowledge-substrate.md)
- [Process Rigour](./guides/03-process-rigour.md)
- [Operational Routing](./guides/04-operational-routing.md)
- [Component Boundary Analysis](./guides/05-component-boundary-analysis.md)
- [Source Package Release Gates](./guides/06-source-package-release-gates.md)
- [From Slice to Implementation Prompt](./guides/07-implementation-prompt-authoring.md)

The component history lives at `knowledge/engineering-methods/version-history.md`.

For active planning and closure mechanics, also load the project-management
component.

This is a component entrypoint for the collaboration framework. It is included
inside `collaboration-framework.zip` as routed dependency material and also
ships as the standalone `engineering-methods.zip` package.
