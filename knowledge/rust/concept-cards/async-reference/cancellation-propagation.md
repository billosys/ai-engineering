---
concept: Cancellation Propagation
slug: cancellation-propagation
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
  - "structured cancellation"
  - "transitive cancellation"
prerequisites:
  - structured-concurrency
  - task-tree
extends:
  - task-tree
related:
  - async-cancellation
  - cancellation-safety
  - error-propagation-concurrency
  - temporal-scope
contrasts_with: []
answers_questions:
  - "How does cancellation propagation work in structured concurrency?"
  - "Why must parent cancellation propagate to children?"
---

# Quick Definition

Cancellation propagation is the principle that when a parent task is cancelled, all of its child tasks must also be cancelled, and their cancellation must complete before the parent's cancellation completes. This downward propagation through the task tree is a required consequence of the structured concurrency invariant that children always finish before parents.

# Core Definition

"The principle of a parent task outliving it's children has an important implication for cancellation: if a task is cancelled, then all its child tasks must be cancelled, and their cancellation must complete before the parent's cancellation completes. That in turn has implications for how cancellation can be implemented in a structurally concurrent system." (Async Reference, Ch. 3: Structured Concurrency, "Principles of structured concurrency")

The source adds the error/panic case: "If a task completes early due to an error (in Rust, this might mean a panic, as well as an early return), then before returning the task must wait for all its child tasks to complete. In practice, an early return must trigger cancellation of child tasks. This is analogous to panicking in Rust: panicking triggers destructors in the current scope before walking up the stack, calling destructors in each scope until the program terminates or the panic is caught. Under structural concurrency, an early return must trigger cancellation of child tasks (and thus cleanup of objects in those tasks) and walks down the tree of tasks cancelling all (transitive) children." (Ch. 3, "Principles of structured concurrency")

# Prerequisites

- **Structured concurrency** -- cancellation propagation is a consequence of the structured concurrency discipline
- **Task tree** -- propagation follows the tree structure downward from parent to children

# Key Properties

1. Cancellation flows downward: parent cancellation triggers child cancellation
2. Cancellation is transitive: cancelling a task cancels all its descendants
3. Child cancellation must complete before parent cancellation completes
4. Early returns (including panics) trigger cancellation of child tasks
5. Analogous to Rust's panic unwinding: destructors run in the current scope before walking up the stack
6. In Rust async, dropping a future drops owned child futures (cancelling them), but spawned tasks are not automatically cancelled
7. One workaround for lack of propagation is to use cancellation tokens instead of abrupt dropping

# Construction / Recognition

## To Implement Cancellation Propagation:
1. When a parent task is cancelled, send a cancellation signal to all child tasks
2. Wait for all child tasks to acknowledge cancellation and complete their cleanup
3. Only then allow the parent's cancellation to complete
4. For composed futures: dropping the parent future drops child futures (automatic but abrupt)
5. For spawned tasks: use cancellation tokens or explicit shutdown signals since dropping the parent does not cancel spawned children

## To Recognize Missing Cancellation Propagation:
1. Check whether spawned tasks continue running after their parent is cancelled or dropped
2. Look for dropped `JoinHandle`s -- in Tokio, dropping a JoinHandle "releases" the task rather than cancelling it
3. Check whether `select` or race patterns cancel children of the losing branch

# Context & Application

In Rust async, cancellation propagation is one of the trickiest aspects of structured concurrency. The source identifies the core problem: "One of the trickiest issues with using structured concurrency with Rust is propagating cancellation to child futures/tasks. If you're using futures and composing them concurrently, then this happens naturally if abruptly (dropping a future drops any futures it owns, cancelling them). However, when a task is dropped, there is no opportunity to send a signal to tasks it has spawned." (Ch. 3, "Practical structured concurrency with async Rust")

This leads to a weaker invariant than ideal: "you can only assume that the parent is always alive unless it has been cancelled or it has panicked."

The source recommends: "One way to work around the lack of cancellation propagation is to avoid abruptly cancelling (dropping) any task which may have children. Instead use a signal (e.g., a cancellation token) so that the task can cancel its children before terminating. Unfortunately this is incompatible with `select`."

The Tokio footnote highlights a specific pitfall: "The semantics of Tokio's `JoinHandle` is that if the handle is dropped, then the underlying task is 'released' (c.f., dropped), i.e., the result of the child task is not handled by any other task."

# Examples

**Example 1** (Ch. 3, "Principles of structured concurrency"): The panic analogy: "Under structural concurrency, an early return must trigger cancellation of child tasks (and thus cleanup of objects in those tasks) and walks down the tree of tasks cancelling all (transitive) children."

**Example 2** (Ch. 3, "Practical structured concurrency with async Rust"): Composed futures get automatic (if abrupt) cancellation: "dropping a future drops any futures it owns, cancelling them." But spawned tasks do not: "when a task is dropped, there is no opportunity to send a signal to tasks it has spawned."

**Example 3** (Ch. 3, "Structured and unstructured idioms"): The cancellation token workaround: "One way to work around the lack of cancellation propagation is to avoid abruptly cancelling (dropping) any task which may have children. Instead use a signal (e.g., a cancellation token) so that the task can cancel its children before terminating."

# Relationships

## Builds Upon
- **task-tree** -- cancellation propagates downward through the tree
- **structured-concurrency** -- cancellation propagation is a required property

## Enables
- Clean shutdown of concurrent task hierarchies
- Reliable resource cleanup across task boundaries

## Related
- **async-cancellation** -- the mechanism by which async tasks are cancelled in Rust (Ch. 1)
- **cancellation-safety** -- the property that makes cancellation safe to perform (Ch. 1)
- **error-propagation-concurrency** -- errors and cancellation both follow the tree structure
- **temporal-scope** -- cancellation propagation enforces temporal scope constraints

## Contrasts With
- None explicitly, but contrasts with the unstructured pattern where cancellation of one task has no effect on others

# Common Errors

- **Error**: Using `select` in a parent task without considering that the losing branch's futures are abruptly dropped, potentially leaving spawned grandchild tasks orphaned.
  **Correction**: Either avoid `select` for tasks with children, or use cancellation tokens to give children time to clean up.

- **Error**: Dropping a Tokio `JoinHandle` and assuming the child task is cancelled.
  **Correction**: Dropping a Tokio `JoinHandle` releases the task (it keeps running), it does not cancel it. Use `JoinHandle::abort()` for explicit cancellation, or use cancellation tokens.

# Common Confusions

- **Confusion**: Thinking Rust's future-dropping provides full cancellation propagation.
  **Clarification**: Dropping a future drops owned child futures (composing concurrently), but does not affect spawned tasks. The two mechanisms (composition vs. spawning) have fundamentally different cancellation behavior.

- **Confusion**: Thinking cancellation propagation means immediate termination.
  **Clarification**: Under structured concurrency, cancellation propagation means signaling children to cancel AND waiting for them to complete their cleanup. The parent's cancellation does not complete until all children have finished.

# Source Reference

Chapter 3: Structured Concurrency. Primary definition in "Principles of structured concurrency." Practical Rust-specific discussion in "Practical structured concurrency with async Rust" and "Structured and unstructured idioms." Tokio-specific behavior documented in footnotes.

# Verification Notes

- Definition source: Direct quotation from "Principles of structured concurrency" section
- Key Properties: Synthesized from the principles section and the Rust-specific practical section
- Confidence rationale: HIGH -- the source explicitly defines cancellation propagation and provides detailed discussion of its implications, including Rust-specific challenges
- Uncertainties: The source notes that workarounds (cancellation tokens) are "incompatible with `select`" but does not elaborate on alternatives
- Cross-reference status: async-cancellation and cancellation-safety reference Ch. 1 cards; other slugs are in this extraction set
