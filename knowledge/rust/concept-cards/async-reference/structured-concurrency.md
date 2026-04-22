---
concept: Structured Concurrency
slug: structured-concurrency
category: concurrency
subcategory: null
tier: intermediate
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Structured Concurrency"
chapter_number: 3
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "structured concurrent programming"
prerequisites:
  - async-task
extends: []
related:
  - task-tree
  - temporal-scope
  - nursery-pattern
  - cancellation-propagation
  - error-propagation-concurrency
  - partially-structured-concurrency
  - scoped-threads
contrasts_with:
  - unstructured-concurrency
answers_questions:
  - "What is structured concurrency?"
  - "What must I understand before applying structured concurrency?"
  - "How do I apply structured concurrency principles to async Rust programs?"
---

# Quick Definition

Structured concurrency is a philosophy for designing concurrent programs in which tasks are organized into a tree, child tasks always finish before their parents, and temporal scope follows lexical scope. It is named by analogy to structured programming, which replaced arbitrary `goto` jumps with functions and loops.

# Core Definition

"Structured concurrency is a philosophy for designing concurrent programs. For programs to fully adhere to the principals of structured concurrency requires certain language features and libraries, but many of the benefits are available by following the philosophy without such features. Structured concurrency is independent of language and concurrency primitives (threads vs async, etc.)." The source further states: "The essential idea of structured concurrency is that tasks are organised into a tree. Child tasks start after their parents and always finish before them. This allows results and errors to always be passed back to parent tasks, and requires that cancellation of parents is always propagated to child tasks." (Async Reference, Ch. 3: Structured Concurrency, introduction)

# Prerequisites

- **Async task** -- understanding what concurrent tasks are (threads, async tasks, or similar primitives) is necessary before reasoning about how to structure their relationships

# Key Properties

1. Tasks are organized as a tree with a single root (the main task)
2. Each task (except the root) has a single parent; there are no cycles
3. Child tasks always finish executing before their parent
4. Results and errors are always passed back to parent tasks
5. Cancellation of parents propagates to all child tasks
6. Temporal scope follows lexical scope in the common case
7. Named by analogy to structured programming (functions/loops replacing `goto`)
8. Independent of language and concurrency primitives (threads, async, etc.)
9. Imposes restrictions that trade flexibility for predictability

# Construction / Recognition

## To Apply Structured Concurrency to a Program Design:
1. Organize all concurrency as a tree: identify which task is the parent of each child task
2. Ensure temporal scope follows lexical scope where possible -- a function should not return until any tasks launched within it are complete
3. Design data flow primarily from child tasks to parent tasks (including errors)
4. Ensure cancellation of a parent cancels all its children (and their children, transitively)
5. If temporal scope must extend beyond a lexical scope, use an explicit scope object (nursery) to reify the lifetime
6. Document where the design is structured and where it deviates from the discipline

## To Recognize Structured Concurrency in Code:
1. Check whether tasks form a tree (no orphaned or free-floating tasks)
2. Verify child tasks complete before parent functions return
3. Verify errors from children are handled by parents
4. Verify cancellation propagates downward through the tree

# Context & Application

Structured concurrency addresses a fundamental problem in concurrent programming: unstructured task spawning creates a "bag of tasks" that run independently, making programs difficult to understand and maintain. The source emphasizes that "this lack of structure is one reason why concurrent programming is considered categorically more difficult than sequential programming."

In Rust, concurrency is inherently unstructured -- tasks can be arbitrarily spawned, errors ignored, and cancellation does not propagate. However, structured concurrency can be applied as a design discipline, and several crates (moro, async-nursery, futures-concurrency) provide supporting abstractions.

A useful compromise pattern is to allow unstructured concurrency only at the highest level (ideally from `main`), where a few top-level tasks with distinct responsibilities are spawned, and then apply structured concurrency rigorously within each of those tasks.

**Library design implication**: If writing a library, temporal encapsulation is important -- the library should not start tasks that keep running beyond API functions returning.

# Examples

**Example 1** (Ch. 3, introduction): The source draws an analogy to structured programming: "Structured concurrency is named by analogy to structured programming, which is the idea that control flow should be structured using functions, loops, etc., rather than arbitrary jumps (`goto`)." Just as `goto` was replaced by structured control flow, unstructured task spawning should be replaced by tree-structured task management.

**Example 2** (Ch. 3, "Practical structured concurrency with async Rust"): The source describes a practical compromise pattern: "One useful compromise pattern is to only allow unstructured concurrency at the highest level of abstraction, and only for tasks spawned from the outer-most functions of the main task (ideally only from the `main` function). [...] Within each of these tasks, structured concurrency is rigorously applied."

**Example 3** (Ch. 3, "Structured and unstructured idioms"): "The easiest way to follow structured concurrency is to use futures and concurrent composition rather than tasks and spawning."

# Relationships

## Builds Upon
- **async-task** -- structured concurrency organizes tasks into a tree; understanding tasks is a prerequisite

## Enables
- **task-tree** -- the tree structure is the central organizing principle
- **temporal-scope** -- follows from the parent-child task discipline
- **cancellation-propagation** -- required by the tree invariant
- **error-propagation-concurrency** -- enabled by always having a live parent

## Related
- **nursery-pattern** -- the implementation mechanism for structured concurrency
- **scoped-threads** -- the synchronous analog in Rust
- **partially-structured-concurrency** -- selective application of the principles

## Contrasts With
- **unstructured-concurrency** -- the default "bag of tasks" approach that structured concurrency replaces

# Common Errors

- **Error**: Spawning tasks without retaining or awaiting their join handles.
  **Correction**: Always retain join handles and await child task completion before the parent returns. Use `JoinHandle`s or `JoinSet`s and check them for errors.

- **Error**: Using `select` or race macros without considering the structural implications.
  **Correction**: `select` abruptly cancels futures, which is a common source of unstructured cancellation. Consider using cancellation tokens instead so that tasks can cancel their children before terminating.

# Common Confusions

- **Confusion**: Thinking structured concurrency requires special language features or library support.
  **Clarification**: Structured concurrency is primarily a design discipline. While full enforcement requires language/library support, "many of the benefits are available by following the philosophy without such features."

- **Confusion**: Thinking structured concurrency means no concurrency at all.
  **Clarification**: Structured concurrency does not eliminate concurrency -- it organizes it into a tree. Tasks still run concurrently; they simply have well-defined parent-child relationships and lifetime constraints.

- **Confusion**: Confusing structured concurrency with sequential execution.
  **Clarification**: "There are no constraints between siblings." Sibling tasks run concurrently; the constraints are only on the parent-child relationship (children finish before parents).

# Source Reference

Chapter 3: Structured Concurrency, all sections. The concept is introduced and defined in the chapter introduction, with principles elaborated in "Principles of structured concurrency," practical guidance in "Practical structured concurrency with async Rust," and idioms in "Structured and unstructured idioms." See also references to blog posts by Martin Sustrik ("Structured Concurrency") and Yoshua Wuyts ("Tree-structured concurrency").

# Verification Notes

- Definition source: Direct quotation from Ch. 3 introduction, paragraphs 1-2
- Key Properties: All extracted from explicit statements in the source
- Confidence rationale: HIGH -- the source explicitly defines structured concurrency with clear terminology and extensive discussion across multiple sections
- Uncertainties: Some sections have TODO markers indicating incomplete content (e.g., "TODO why is this useful?" and "TODO would be great to have a case study here"), but the core definition and principles are thoroughly developed
- Cross-reference status: All slugs reference cards in this extraction set or from Ch. 1/Ch. 2 extractions
