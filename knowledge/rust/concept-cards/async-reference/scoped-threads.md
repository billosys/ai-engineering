---
concept: Scoped Threads
slug: scoped-threads
category: language-features
subcategory: null
tier: intermediate
source: "Async Reference"
source_slug: async-reference
authors: "Rust Async Working Group"
chapter: "Structured Concurrency"
chapter_number: 3
pdf_page: null
section: "Scoped threads"
extraction_confidence: high
aliases:
  - "std::thread::scope"
  - "thread scope"
  - "scoped threading"
prerequisites:
  - structured-concurrency
extends: []
related:
  - nursery-pattern
  - temporal-scope
  - task-tree
contrasts_with:
  - unstructured-concurrency
answers_questions:
  - "How do scoped threads relate to structured concurrency?"
  - "What is the difference between scoped threads and unscoped threads?"
---

# Quick Definition

Scoped threads are Rust's `std::thread::scope` mechanism for spawning threads whose lifetimes are bounded by a lexical scope, providing structured concurrency for synchronous code. They limit child lifetimes, automatically propagate panics, and -- uniquely in Rust -- allow child threads to borrow data from the parent thread.

# Core Definition

"Structured concurrency with Rust threads works pretty well. Although you can't prevent spawning threads with unscoped lifetime, this is easy to avoid. Instead, restrict yourself to using scoped threads, see the `scope` function docs for how. Using scoped threads limits child lifetimes and automatically propagates panics back to the parent thread. The parent thread must check the results of child threads to handle errors though. You can even pass around the `Scope` object like a Trio nursery." (Async Reference, Ch. 3: Structured Concurrency, "Scoped threads")

# Prerequisites

- **Structured concurrency** -- scoped threads are understood as the synchronous Rust implementation of structured concurrency principles

# Key Properties

1. Scoped threads limit child thread lifetimes to the enclosing scope
2. Panics in child threads are automatically propagated to the parent thread
3. The parent thread must check results of child threads to handle errors
4. The `Scope` object can be passed around like a Trio nursery
5. Child threads can borrow data from the parent thread (not possible with unscoped `std::thread::spawn`)
6. Cancellation is not usually an issue for Rust threads, but if used, it must be manually integrated with scoped threads
7. Demonstrates how well structured concurrency and Rust's ownership-based resource management work together

# Construction / Recognition

## To Use Scoped Threads:
1. Call `std::thread::scope(|s| { ... })` to create a scope
2. Within the closure, spawn threads using `s.spawn(|| { ... })`
3. Child threads can borrow data from the parent (the scope enforces lifetime bounds)
4. When the scope closure exits, all child threads are joined automatically
5. Check thread results for errors (panics propagate, but `Result` errors must be explicitly handled)

## To Recognize Scoped vs. Unscoped Threads:
1. Scoped: threads spawned via `scope.spawn()` within a `std::thread::scope` block
2. Unscoped: threads spawned via `std::thread::spawn()` with `'static` bounds on the closure
3. Key indicator: if the spawned closure borrows non-`'static` data, it must be scoped

# Context & Application

Scoped threads are the synchronous analog of the nursery pattern and the most accessible form of structured concurrency in Rust. The source presents them as a "related topic" that provides useful context, noting they are "not necessary to know to use structured concurrency with async Rust, but is useful context included for the curious."

The key advantage unique to Rust is the borrowing capability: "scoped threads allow child threads to borrow data from the parent thread, something not possible with concurrent-unstructured threads. This can be very useful and shows how well structured concurrency and Rust-ownership-style resource management can work together."

The source draws an explicit parallel to the Trio nursery: you can "pass around the `Scope` object like a Trio nursery," making the `Scope` a reified representation of temporal scope.

The absence of an equivalent "scoped tasks" construct for async Rust is noted as an open question: "another good question is why there is no similar construct for async programming ('scoped tasks')?" The answer is marked TODO in the source.

# Examples

**Example 1** (Ch. 3, "Scoped threads"): The source describes the full set of structured concurrency benefits: "Using scoped threads limits child lifetimes and automatically propagates panics back to the parent thread."

**Example 2** (Ch. 3, "Scoped threads"): The borrowing advantage: "scoped threads allow child threads to borrow data from the parent thread, something not possible with concurrent-unstructured threads."

**Example 3** (Ch. 3, "Scoped threads"): The nursery parallel: "You can even pass around the `Scope` object like a Trio nursery."

# Relationships

## Builds Upon
- **structured-concurrency** -- scoped threads are the synchronous Rust implementation

## Enables
- Borrowing across thread boundaries (unique to scoped threads in Rust)
- Structured resource management across concurrent threads

## Related
- **nursery-pattern** -- the `Scope` object functions like a nursery
- **temporal-scope** -- scoped threads enforce temporal scope tied to lexical scope
- **task-tree** -- scoped threads enforce the parent-child tree structure for threads

## Contrasts With
- **unstructured-concurrency** -- unscoped `std::thread::spawn` is unstructured (no lifetime bounds, `'static` requirement, no automatic panic propagation)

# Common Errors

- **Error**: Using `std::thread::spawn` instead of scoped threads and then needing `Arc`/`clone` to share data.
  **Correction**: Use `std::thread::scope` when child threads need to borrow parent data. Scoped threads allow borrowing without `Arc`.

- **Error**: Forgetting to check thread results for errors (as opposed to panics).
  **Correction**: Panics propagate automatically, but `Result::Err` values must be explicitly checked. "The parent thread must check the results of child threads to handle errors."

# Common Confusions

- **Confusion**: Thinking scoped threads and async scoped tasks are the same thing.
  **Clarification**: Scoped threads exist in stable Rust (`std::thread::scope`). There is no equivalent "scoped tasks" for async Rust -- the source notes this as an open question, partly blocked by the lack of async drop.

- **Confusion**: Thinking cancellation is automatically handled by scoped threads.
  **Clarification**: "Cancellation is not usually an issue for Rust threads, but if you do make use of thread cancellation, you'll have to integrate that with scoped threads manually." Threads do not have the same cancellation semantics as async futures.

# Source Reference

Chapter 3: Structured Concurrency, "Scoped threads" section under "Related topics." References `std::thread::scope` function docs and `std::thread::Scope` struct docs from the Rust standard library.

# Verification Notes

- Definition source: Direct quotation from the "Scoped threads" section
- Key Properties: All from explicit statements in the same section
- Confidence rationale: HIGH -- the source explicitly describes scoped threads with clear properties and comparisons, and links to the standard library documentation
- Uncertainties: The source marks as TODO the question of why there is no equivalent for async ("scoped tasks")
- Cross-reference status: All slugs reference cards in this extraction set
