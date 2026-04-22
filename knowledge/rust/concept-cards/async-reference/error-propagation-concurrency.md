---
concept: Error Propagation in Concurrency
slug: error-propagation-concurrency
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
  - "concurrent error propagation"
  - "error handling in structured concurrency"
prerequisites:
  - structured-concurrency
  - task-tree
extends:
  - task-tree
related:
  - cancellation-propagation
  - error-propagation-concurrency
  - nursery-pattern
contrasts_with: []
answers_questions:
  - "How does structured concurrency relate to error propagation?"
  - "Why does unstructured concurrency make error handling difficult?"
---

# Quick Definition

In structured concurrency, errors flow upward from child tasks to parent tasks, leveraging the language's standard error handling mechanisms. The task tree guarantees that a live parent always exists to receive errors, unlike unstructured concurrency where errors may go uncaught.

# Core Definition

"This allows results and errors to always be passed back to parent tasks." (Async Reference, Ch. 3: Structured Concurrency, introduction)

The source elaborates: "if a task is live, then all of its ancestor tasks must also be live. [...] This means that for any task (except the root task), there is always a live task to send results or errors to. Indeed, the ideal approach is that the language's error handling is extended so that errors are always propagated to the parent task. In Rust, this should apply to both returning `Result::Err` and to panicking." (Ch. 3, "Principles of structured concurrency")

The problem in unstructured concurrency is explicit: "Errors may go uncaught because languages' error handling mechanisms cannot be applied to the unconstrained control flow of unstructured concurrency." (Ch. 3, introduction)

# Prerequisites

- **Structured concurrency** -- error propagation is a key benefit of the structured concurrency discipline
- **Task tree** -- the tree structure guarantees a live parent to receive errors

# Key Properties

1. Errors flow upward from child tasks to parent tasks
2. The task tree guarantees a live parent is always available to receive errors
3. In Rust, error propagation should cover both `Result::Err` returns and panics
4. In unstructured concurrency, errors may go uncaught -- there is no guarantee a receiver exists
5. Parent tasks should handle errors from their children, even if the handling is to explicitly ignore them
6. In Trio, error handling uses Python exceptions automatically propagated to parents
7. In Rust with Tokio, join handles must be checked for errors -- dropping them silently discards the result
8. Error propagation can be adopted selectively even without full structured concurrency

# Construction / Recognition

## To Implement Error Propagation:
1. Retain join handles for all spawned child tasks
2. Await or check every join handle for errors
3. Handle errors from children in the parent: log, propagate, or explicitly ignore
4. For panics, ensure the parent catches and handles the panic result from the join handle
5. Never drop a join handle without checking its result

## To Recognize Missing Error Propagation:
1. Look for dropped join handles -- errors are silently lost
2. Check whether `.unwrap()` on join handles will propagate panics
3. Look for spawned tasks whose results are never observed

# Context & Application

Error propagation is one of the most practical benefits of structured concurrency. The source identifies it as a problem that is "fairly easy to adopt" even without full structured concurrency: "Another element of structured concurrency which is fairly easy to adopt is to always propagate errors to the parent task. Just like regular error handling, the best thing to do might be to ignore the error, but this should be explicit in the code of the parent task." (Ch. 3, "Partially structured concurrency")

In Rust async specifically, the source notes a practical limitation: "you can only assume a weaker invariant than with 'real' structured concurrency: rather than being able to assume that a parent task is always alive, you can only assume that the parent is always alive unless it has been cancelled or it has panicked." Despite this, the benefit remains: "you never have to handle the case of having no parent to handle some result *under normal execution*."

The source also connects error propagation to cancellation: when a child task errors, the parent may need to cancel sibling tasks. "If a task completes early due to an error [...] then before returning the task must wait for all its child tasks to complete. In practice, an early return must trigger cancellation of child tasks."

# Examples

**Example 1** (Ch. 3, introduction): The unstructured problem: "Errors may go uncaught because languages' error handling mechanisms cannot be applied to the unconstrained control flow of unstructured concurrency."

**Example 2** (Ch. 3, "Principles of structured concurrency"): The structured solution: "the ideal approach is that the language's error handling is extended so that errors are always propagated to the parent task. In Rust, this should apply to both returning `Result::Err` and to panicking."

**Example 3** (Ch. 3, "Implementing structured concurrency"): Trio's approach: "Error handling uses Python exceptions which are automatically propagated to parent tasks."

**Example 4** (Ch. 3, "Structured and unstructured idioms"): The practical Rust guidance: "Handles must be checked for errors to ensure errors in child tasks are properly handled."

# Relationships

## Builds Upon
- **task-tree** -- the tree structure guarantees a parent exists to receive errors
- **structured-concurrency** -- error propagation is a core benefit of the discipline

## Enables
- Reliable concurrent error handling without ad hoc mechanisms
- Confident reasoning about error states across task boundaries

## Related
- **cancellation-propagation** -- errors in children may trigger cancellation of siblings
- **nursery-pattern** -- nurseries provide the conduit for error propagation

## Contrasts With
- None explicitly named, but contrasts with unstructured error handling where errors may go unobserved

# Common Errors

- **Error**: Dropping a `JoinHandle` without checking its result, silently discarding errors.
  **Correction**: Always await or inspect join handles. In Tokio, a dropped `JoinHandle` means "the result of the child task is not handled by any other task."

- **Error**: Using `.unwrap()` on join handle results without considering that this converts a child panic into a parent panic.
  **Correction**: Match on the join result to handle errors gracefully rather than propagating panics blindly.

# Common Confusions

- **Confusion**: Thinking error propagation requires full structured concurrency.
  **Clarification**: Error propagation is "fairly easy to adopt" selectively. "Just like regular error handling, the best thing to do might be to ignore the error, but this should be explicit in the code of the parent task."

- **Confusion**: Assuming Rust's type system prevents lost errors in concurrent code.
  **Clarification**: While `Result` forces error handling in sequential code, a dropped `JoinHandle` silently discards the task's result (including errors). The type system does not enforce that join handles are awaited.

# Source Reference

Chapter 3: Structured Concurrency. Primary discussion in the introduction (problems with unstructured error handling) and "Principles of structured concurrency" (the structured solution). Practical Rust guidance in "Structured and unstructured idioms." Trio's approach in "Implementing structured concurrency." Selective adoption discussed in "Partially structured concurrency."

# Verification Notes

- Definition source: Direct quotations from Ch. 3 introduction and "Principles" section
- Key Properties: Synthesized from multiple sections covering both the theoretical principle and practical Rust concerns
- Confidence rationale: HIGH -- the source explicitly discusses error propagation as a core benefit of structured concurrency, with clear examples of both the problem (unstructured) and solution (structured)
- Uncertainties: The source does not provide concrete Rust code examples of error propagation patterns; the discussion is conceptual
- Cross-reference status: All slugs reference cards in this extraction set
