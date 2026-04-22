---
concept: Partially Structured Concurrency
slug: partially-structured-concurrency
category: concurrency
subcategory: null
tier: advanced
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Structured Concurrency"
chapter_number: 3
pdf_page: null
section: "Partially structured concurrency"
extraction_confidence: high
aliases:
  - "selective structured concurrency"
  - "pragmatic structured concurrency"
prerequisites:
  - structured-concurrency
  - unstructured-concurrency
extends:
  - structured-concurrency
related:
  - task-tree
  - cancellation-propagation
  - error-propagation-concurrency
contrasts_with: []
answers_questions:
  - "How do I apply structured concurrency principles to async Rust programs?"
  - "What must I understand before applying structured concurrency?"
  - "Can I get benefits from structured concurrency without fully adopting it?"
---

# Quick Definition

Partially structured concurrency is the pragmatic approach of selectively applying structured concurrency principles in languages and runtimes (like Rust) that do not enforce them. It includes using structured concurrency as a design discipline, always propagating errors, and propagating cancellation, even without full language support.

# Core Definition

"Like many programming techniques, the full benefits of structured concurrency come from *only* using it. If all concurrency is structured, then it makes it much easier to reason about the behaviour of the whole program. However, that has requirements on a language which are not easily met; it is easy enough to do unstructured concurrency in Rust, for example. However, even applying the principles of structured concurrency selectively, or thinking in terms of structured concurrency can be useful." (Async Reference, Ch. 3: Structured Concurrency, "Partially structured concurrency")

The source also describes a practical compromise: "One useful compromise pattern is to only allow unstructured concurrency at the highest level of abstraction, and only for tasks spawned from the outer-most functions of the main task (ideally only from the `main` function). [...] Under such a pattern, a bunch of tasks are spawned from `main`, usually with distinct responsibilities and limited interaction between each other. [...] Within each of these tasks, structured concurrency is rigorously applied." (Ch. 3, "Applying structured concurrency to the design of async programs")

# Prerequisites

- **Structured concurrency** -- must understand the full philosophy before applying it selectively
- **Unstructured concurrency** -- must understand the default pattern to know what is being improved

# Key Properties

1. Full benefits of structured concurrency come from exclusive use, but selective application is still useful
2. Can be applied as a design discipline: document parent-child relationships and ensure children terminate before parents
3. Error propagation is "fairly easy to adopt" even without full structured concurrency
4. Cancellation propagation of children when a parent is cancelled is another adoptable discipline
5. The compromise pattern: unstructured concurrency only at the top level, structured concurrency within each top-level task
6. Important to document where the program is structured and where it violates the discipline
7. Since Rust cannot enforce the rules, awareness and documentation are critical

# Construction / Recognition

## To Apply Partially Structured Concurrency:
1. Design the program's task relationships as a tree (document the parent-child structure)
2. Ensure child tasks terminate before parents under normal execution
3. Always propagate errors from children to parents -- even if the parent ignores them, this should be explicit
4. Cancel all child tasks when a parent is cancelled
5. Allow unstructured concurrency only at the top level (`main` or equivalent)
6. Apply structured concurrency rigorously within each top-level task
7. Document any deviations from structured concurrency discipline

## Three Adoptable Disciplines (from source):
1. **Design discipline**: "always consider and document the parent-child relationships between tasks and ensure that a child task terminates before its parent"
2. **Error discipline**: "always propagate errors to the parent task"
3. **Cancellation discipline**: "cancel all child tasks in the event of cancelling a parent task"

# Context & Application

Partially structured concurrency is the practical reality for async Rust. The source acknowledges: "Concurrency in Rust (whether async or using threads) is inherently unstructured. Tasks can be arbitrarily spawned, errors and panics on other tasks can be ignored, and cancellation is usually instantaneous and does not propagate to other tasks."

Given this reality, the source recommends three approaches (Ch. 3, "Practical structured concurrency with async Rust"):
1. "Design your programs at a high level in accordance with structured concurrency."
2. "Stick to structured concurrency idioms where possible (and avoid unstructured idioms)."
3. "Use crates to make structured concurrency more ergonomic and reliable."

The weaker invariant that results is still valuable: "rather than being able to assume that a parent task is always alive, you can only assume that the parent is always alive unless it has been cancelled or it has panicked. While this is sub-optimal, it can still simplify programming because you never have to handle the case of having no parent to handle some result *under normal execution*."

# Examples

**Example 1** (Ch. 3, "Partially structured concurrency"): Three selectively adoptable disciplines:
- "One can use structured concurrency as a design discipline. When designing a program, always consider and document the parent-child relationships between tasks."
- "Another element of structured concurrency which is fairly easy to adopt is to always propagate errors to the parent task."
- "Another programming discipline to learn from structured concurrency is to cancel all child tasks in the event of cancelling a parent task."

**Example 2** (Ch. 3, "Applying structured concurrency"): The compromise pattern: "One useful compromise pattern is to only allow unstructured concurrency at the highest level of abstraction [...] Within each of these tasks, structured concurrency is rigorously applied."

**Example 3** (Ch. 3, "Practical structured concurrency with async Rust"): The weaker invariant: "you never have to handle the case of having no parent to handle some result *under normal execution*."

# Relationships

## Builds Upon
- **structured-concurrency** -- selective application of the full philosophy
- **unstructured-concurrency** -- understanding what is being partially replaced

## Enables
- Practical concurrent programming with many benefits of structured concurrency in languages that do not enforce it
- Incremental adoption of structured concurrency in existing codebases

## Related
- **task-tree** -- the tree structure is maintained as a design discipline rather than an enforced invariant
- **cancellation-propagation** -- one of the three adoptable disciplines
- **error-propagation-concurrency** -- one of the three adoptable disciplines

## Contrasts With
- None explicitly -- it is intermediate between full structured and full unstructured

# Common Errors

- **Error**: Applying structured concurrency within a component but spawning unstructured tasks at every level of the application.
  **Correction**: Limit unstructured concurrency to the top level only. Within each top-level task, apply structured concurrency rigorously.

- **Error**: Not documenting which parts of the program use structured vs. unstructured concurrency.
  **Correction**: "Since Rust can't enforce the rules of structured concurrency, it's important to be aware of, and to document, in which ways the program (or component) is structured and where it violates the structured concurrency discipline."

# Common Confusions

- **Confusion**: Thinking partial adoption provides the same guarantees as full structured concurrency.
  **Clarification**: The source is explicit: "the full benefits of structured concurrency come from *only* using it." Partial adoption provides a weaker invariant, but it is still valuable for reasoning about program behavior under normal execution.

- **Confusion**: Thinking that following structured concurrency idioms in Rust is all-or-nothing.
  **Clarification**: The source describes three independently adoptable disciplines (design, error propagation, cancellation propagation). Each provides incremental benefit.

# Source Reference

Chapter 3: Structured Concurrency. Primary discussion in "Partially structured concurrency." Practical Rust application in "Practical structured concurrency with async Rust" and "Applying structured concurrency to the design of async programs."

# Verification Notes

- Definition source: Direct quotation from "Partially structured concurrency" section
- Key Properties: Extracted from the "Partially structured concurrency" and "Applying structured concurrency" sections
- Confidence rationale: HIGH -- the source explicitly discusses partial adoption with clear recommendations and specific disciplines to adopt
- Uncertainties: The "Applying" section has TODO markers ("TODO why is this useful?" and "TODO would be great to have a case study here"), indicating the source authors intended to elaborate further. The core content on partial adoption is complete.
- Cross-reference status: All slugs reference cards in this extraction set
