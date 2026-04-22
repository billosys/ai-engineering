---
concept: Temporal Scope
slug: temporal-scope
category: concurrency
subcategory: null
tier: advanced
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Structured Concurrency"
chapter_number: 3
pdf_page: null
section: "Principles of structured concurrency"
extraction_confidence: high
aliases:
  - "task lifetime"
  - "temporal task scope"
prerequisites:
  - structured-concurrency
  - task-tree
extends:
  - task-tree
related:
  - nursery-pattern
  - scoped-threads
  - async-drop
contrasts_with: []
answers_questions:
  - "What is temporal scope in structured concurrency?"
  - "How does temporal scope relate to lexical scope?"
---

# Quick Definition

Temporal scope is the principle that the lifetime of a concurrent task should follow the lexical scope in which it is created -- a task should not outlive the function or block where it is started. When a task's lifetime must extend beyond a lexical scope, it is reified using a scope or nursery object.

# Core Definition

"Primarily, temporal scope follows lexical scope, which means that a task should not outlive the function or block where it is created. However, this is not a requirement of structured concurrency as long as longer-lived tasks are reified in the program in some way (typically by using an object to represent the temporal scope of a child task within its parent task)." (Async Reference, Ch. 3: Structured Concurrency, introduction)

The source elaborates in the "Principles" section: "the lifetime of child tasks can be represented in the parent task. In the common case, the lifetime of a task (its temporal scope) is tied to the lexical scope in which it is started. For example, all tasks started within a function should complete before the function returns. This is an extremely powerful reasoning tool." (Ch. 3, "Principles of structured concurrency")

# Prerequisites

- **Structured concurrency** -- temporal scope is a core principle of the structured concurrency philosophy
- **Task tree** -- temporal scope derives from and reinforces the tree structure of tasks

# Key Properties

1. In the common case, temporal scope follows lexical scope: tasks complete before the enclosing function or block returns
2. Temporal scope can extend beyond lexical scope by using a scope or nursery object
3. The scope object can be passed or stored, giving it an arbitrary lifetime
4. Tasks tied to a scope object cannot outlive that object
5. In Rust, the scope-object approach integrates with the lifetime system
6. All tasks started within a function should complete before the function returns (including early returns and panics)
7. If a function returns early (including via panic), it must wait for child tasks to complete -- in practice this means triggering cancellation

# Construction / Recognition

## To Apply Temporal Scope:
1. For each concurrent task, identify the lexical scope where it is spawned
2. Ensure the task completes before that scope exits
3. If the task must live beyond the spawning scope, create an explicit scope object (nursery) to represent its lifetime
4. Handle early returns: if the enclosing function returns early or panics, cancel child tasks and wait for their completion before continuing the return

## To Recognize Temporal Scope Violations:
1. Look for tasks that outlive the function that spawned them
2. Check for spawned tasks with no associated scope or join handle
3. Look for tasks that survive early returns or panics of their parent

# Context & Application

Temporal scope is described as "an extremely powerful reasoning tool." It enables programmers to reason about concurrent task lifetimes the same way they reason about variable lifetimes in sequential code -- by looking at lexical scope boundaries.

The practical design implication is stated explicitly: "Temporal scope should follow lexical scope where possible, or in concrete terms a function shouldn't return (including early returns and panics) until any tasks launched in the function are complete." (Ch. 3, "Applying structured concurrency to the design of async programs")

For library authors, this means temporal encapsulation: "it is important that encapsulation of the library component includes temporal encapsulation. I.e., it doesn't start tasks which keep running beyond the API functions returning."

In Rust, the concept maps naturally to ownership and lifetimes. The source notes that Rust's scoped threads demonstrate this: "scoped threads allow child threads to borrow data from the parent thread, something not possible with concurrent-unstructured threads. This can be very useful and shows how well structured concurrency and Rust-ownership-style resource management can work together."

# Examples

**Example 1** (Ch. 3, "Principles of structured concurrency"): "In the common case, the lifetime of a task (its temporal scope) is tied to the lexical scope in which it is started. For example, all tasks started within a function should complete before the function returns."

**Example 2** (Ch. 3, "Principles of structured concurrency"): When temporal scope extends beyond lexical scope: "the temporal scope of tasks can extend beyond a lexical scope by using an object in the program (often called a 'scope' or 'nursery'). Such an object can be passed or stored, and thus have an arbitrary lifetime. We still have an important reasoning tool: the tasks tied to that object cannot outlive it (in Rust this property lets us integrate tasks with the lifetime system)."

**Example 3** (Ch. 3, "Principles of structured concurrency"): The error/panic case: "If a task completes early due to an error (in Rust, this might mean a panic, as well as an early return), then before returning the task must wait for all its child tasks to complete. In practice, an early return must trigger cancellation of child tasks."

# Relationships

## Builds Upon
- **task-tree** -- temporal scope is the lifetime dimension of the tree structure
- **structured-concurrency** -- temporal scope is one of its core principles

## Enables
- **nursery-pattern** -- nurseries are the mechanism for reifying temporal scope as an object
- Resource reasoning across concurrent tasks (objects owned by parents remain valid for child task duration)

## Related
- **scoped-threads** -- Rust's `std::thread::scope` demonstrates temporal scope for synchronous concurrency
- **async-drop** -- async destructors would enable temporal scope enforcement in async contexts

## Contrasts With
- None explicitly named, but contrasts with the unstructured pattern where tasks have unbounded lifetimes

# Common Errors

- **Error**: Allowing a library function to spawn background tasks that outlive the function call.
  **Correction**: Ensure temporal encapsulation -- all tasks spawned by a function complete before it returns. If background work is needed, use an explicit scope object owned by the caller.

- **Error**: Not handling early returns or panics -- the function exits but child tasks keep running.
  **Correction**: Early returns and panics must trigger cancellation of child tasks. Wait for their completion before the function actually returns.

# Common Confusions

- **Confusion**: Thinking temporal scope MUST equal lexical scope.
  **Clarification**: Temporal scope follows lexical scope "in the common case," but can extend beyond it using a scope/nursery object. The key constraint is that temporal scope must be explicitly represented in the program.

- **Confusion**: Conflating temporal scope with Rust's ownership lifetimes.
  **Clarification**: They are related but distinct. Temporal scope is about task lifetime in structured concurrency. Rust lifetimes are about reference validity. The source notes they integrate well ("in Rust this property lets us integrate tasks with the lifetime system"), but temporal scope is a language-independent concept.

# Source Reference

Chapter 3: Structured Concurrency. Defined in the introduction and elaborated in "Principles of structured concurrency." Practical application discussed in "Applying structured concurrency to the design of async programs."

# Verification Notes

- Definition source: Direct quotation from Ch. 3 introduction and "Principles" section
- Key Properties: Extracted from multiple paragraphs across the introduction and principles sections
- Confidence rationale: HIGH -- the source explicitly defines temporal scope, explains its relationship to lexical scope, and describes the escape hatch (scope objects)
- Uncertainties: None for the definition; the concept is thoroughly explained
- Cross-reference status: All slugs reference cards in this extraction set or from Ch. 1/Ch. 2 extractions
