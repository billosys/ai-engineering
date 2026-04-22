---
concept: Nursery Pattern
slug: nursery-pattern
category: concurrency
subcategory: null
tier: advanced
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Structured Concurrency"
chapter_number: 3
pdf_page: null
section: "Implementing structured concurrency"
extraction_confidence: high
aliases:
  - "nursery"
  - "scope object"
  - "task scope"
prerequisites:
  - structured-concurrency
  - task-tree
  - temporal-scope
extends:
  - temporal-scope
related:
  - scoped-threads
  - cancellation-propagation
  - error-propagation-concurrency
contrasts_with: []
answers_questions:
  - "What is the nursery pattern in structured concurrency?"
  - "How does the nursery pattern relate to Rust's scoped threads?"
---

# Quick Definition

The nursery pattern is an implementation mechanism for structured concurrency where a scope object manages the lifetime of child tasks, ensuring they all complete before the scope exits. The pattern was pioneered by Python's Trio library and has analogs in Rust's `std::thread::Scope` and crates like moro and async-nursery.

# Core Definition

"The exemplar implementation of structured concurrency is the Python Trio library. Trio is a general purpose library for async programming and IO designed around the concepts of structured concurrency. Trio programs use the `async with` construct to define a lexical scope for spawning tasks. Spawned tasks are associated with a nursery object (which is somewhat like a Scope in Rust). The lifetime of a task is tied to the dynamic temporal scope of its nursery, and in the common case, the lexical scope of an `async with` block. This enforces the parent/child relationship between tasks and thus the tree-invariant of structured concurrency." (Async Reference, Ch. 3: Structured Concurrency, "Implementing structured concurrency")

The source also describes nurseries more generally in the "Principles" section: "the temporal scope of tasks can extend beyond a lexical scope by using an object in the program (often called a 'scope' or 'nursery'). Such an object can be passed or stored, and thus have an arbitrary lifetime. We still have an important reasoning tool: the tasks tied to that object cannot outlive it."

# Prerequisites

- **Structured concurrency** -- the nursery pattern is the implementation mechanism for the philosophy
- **Task tree** -- nurseries enforce the tree structure by managing parent-child task relationships
- **Temporal scope** -- nurseries are the concrete representation of temporal scope as an object

# Key Properties

1. A nursery (or scope) object defines the temporal scope for a group of child tasks
2. Tasks spawned into a nursery are tied to its lifetime
3. The nursery ensures all child tasks complete before the scope exits
4. In the common case, the nursery's lifetime is tied to a lexical scope (e.g., a block or function)
5. The nursery object can be passed or stored, allowing temporal scope to extend beyond lexical scope
6. Tasks tied to a nursery cannot outlive it
7. In Rust, this integrates with the lifetime system
8. Error handling is automatic: errors propagate from child tasks through the nursery to the parent

# Construction / Recognition

## To Use the Nursery Pattern:
1. Create a scope/nursery object, typically tied to a lexical scope (e.g., `async with` in Trio, `std::thread::scope` in Rust)
2. Spawn child tasks into the nursery rather than into the global runtime
3. The nursery tracks all spawned tasks
4. When the scope exits, the nursery ensures all tasks have completed
5. Errors from any child task propagate to the parent via the nursery

## To Recognize the Nursery Pattern:
1. Look for a scope object that manages task spawning
2. Check that all task spawns go through the scope rather than a global spawn function
3. Verify that the scope waits for all tasks before returning

# Context & Application

The nursery pattern originates from Python's Trio library, which the source calls "the exemplar implementation of structured concurrency." In Trio, the `async with trio.open_nursery() as nursery:` construct creates a lexical scope; tasks spawned with `nursery.start_soon()` must complete before the `async with` block exits.

In Rust, `std::thread::Scope` serves a similar role for synchronous threads: "You can even pass around the `Scope` object like a Trio nursery."

For async Rust, the source mentions several crates that provide nursery-like patterns: moro (by Niko Matsakis), async-nursery, and futures-concurrency. However, the "Crates for structured concurrency" section is incomplete (marked TODO), so detailed comparison of these crates is not available in the source.

# Examples

**Example 1** (Ch. 3, "Implementing structured concurrency"): The Trio nursery pattern: "Trio programs use the `async with` construct to define a lexical scope for spawning tasks. Spawned tasks are associated with a nursery object. The lifetime of a task is tied to the dynamic temporal scope of its nursery."

**Example 2** (Ch. 3, "Scoped threads"): The Rust analog for synchronous concurrency: "Using scoped threads limits child lifetimes and automatically propagates panics back to the parent thread. [...] You can even pass around the `Scope` object like a Trio nursery."

**Example 3** (Ch. 3, "Crates for structured concurrency"): The source lists Rust async crates that implement nursery-like patterns: moro, async-nursery, and futures-concurrency (section is TODO but crate names are provided).

# Relationships

## Builds Upon
- **temporal-scope** -- nurseries are the concrete reification of temporal scope
- **task-tree** -- nurseries enforce the tree structure

## Enables
- **cancellation-propagation** -- nurseries can propagate cancellation to all managed tasks
- **error-propagation-concurrency** -- nurseries provide the conduit for errors to flow to parents

## Related
- **scoped-threads** -- `std::thread::Scope` is the synchronous Rust analog of a nursery

## Contrasts With
- None explicitly -- but contrasts with global task spawning (e.g., `tokio::spawn`) which does not enforce temporal scope

# Common Errors

- **Error**: Spawning some tasks through the nursery and others through global spawn, mixing structured and unstructured patterns.
  **Correction**: All tasks within a structured concurrency scope should be spawned through the nursery/scope object to maintain the tree invariant.

- **Error**: Dropping the nursery object without awaiting all child tasks.
  **Correction**: The nursery must wait for all tasks to complete before it is dropped. This is usually enforced by the nursery's API (e.g., the `async with` block in Trio, or the closure in `std::thread::scope`).

# Common Confusions

- **Confusion**: Thinking nurseries are Python-specific.
  **Clarification**: The nursery pattern originated in Trio but is language-independent. Rust has `std::thread::Scope` for threads and crates like moro and async-nursery for async tasks. The concept (a scope object managing child task lifetimes) applies broadly.

- **Confusion**: Conflating a nursery with a thread pool or task pool.
  **Clarification**: A nursery manages task lifetimes and enforces structured concurrency. A pool manages task reuse for performance. The source explicitly lists worker pools as an idiom that "does not play well with structured concurrency."

# Source Reference

Chapter 3: Structured Concurrency, "Implementing structured concurrency" section for the Trio example. "Principles of structured concurrency" for the general concept of scope objects. "Scoped threads" section for the Rust synchronous analog. "Crates for structured concurrency" for async Rust implementations (section is incomplete/TODO).

# Verification Notes

- Definition source: Direct quotation from "Implementing structured concurrency" section; supplementary material from "Principles" section
- Key Properties: Synthesized from multiple sections covering the Trio example, general principles, and Rust analogs
- Confidence rationale: HIGH -- the source provides a clear, detailed description of the Trio nursery and its properties, with explicit comparison to Rust's Scope
- Uncertainties: The "Crates for structured concurrency" section is marked TODO, so details on moro, async-nursery, and futures-concurrency are not available from this source
- Cross-reference status: All slugs reference cards in this extraction set
