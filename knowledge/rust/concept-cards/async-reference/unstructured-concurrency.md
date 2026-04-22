---
concept: Unstructured Concurrency
slug: unstructured-concurrency
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
  - "unstructured concurrent programming"
prerequisites:
  - async-task
extends: []
related:
  - structured-concurrency
  - cancellation-propagation
contrasts_with:
  - structured-concurrency
answers_questions:
  - "What is the difference between structured and unstructured concurrency?"
  - "What are the downsides of unstructured concurrency?"
---

# Quick Definition

Unstructured concurrency is the default pattern where tasks are spawned independently with no enforced parent-child relationships, forming a "bag of tasks" that may terminate in any order. It is the concurrent programming analog of `goto`-based control flow.

# Core Definition

"A typical pattern is that a task is started using some kind of spawning statement. That task then runs to completion concurrently with other tasks in the system (including the task which spawned it). There is no constraint on which task finishes first. The program is essentially just a bag of tasks which live independently and might terminate at any time. Any communication or synchronization of the tasks is ad hoc, and the programmer cannot assume that any other task will still be running." (Async Reference, Ch. 3: Structured Concurrency, introduction)

# Prerequisites

- **Async task** -- understanding what concurrent tasks are is necessary to understand the lack of structure between them

# Key Properties

1. Tasks are spawned independently with no enforced lifetime relationships
2. There is no constraint on which task finishes first
3. Communication and synchronization between tasks is ad hoc
4. The programmer cannot assume any other task is still running
5. Returning results from a task requires extra-linguistic mechanisms
6. Errors may go uncaught because language error handling cannot span unstructured control flow
7. Any task may be running, terminated (successfully or with error), or cancelled, independently of all others
8. Join handles mitigate some downsides but are an ad hoc mechanism with no reliable guarantees

# Construction / Recognition

## To Recognize Unstructured Concurrency:
1. Look for tasks spawned without retained or awaited join handles
2. Check whether any task might outlive the function or scope that spawned it
3. Look for dropped join handles or fire-and-forget spawns
4. Check whether errors from child tasks could go unobserved
5. Look for `select` or race patterns that abruptly cancel futures without propagation

# Context & Application

Unstructured concurrency is the default in most languages and runtimes, including Rust. The source explicitly states: "Concurrency in Rust (whether async or using threads) is inherently unstructured. Tasks can be arbitrarily spawned, errors and panics on other tasks can be ignored, and cancellation is usually instantaneous and does not propagate to other tasks."

The source frames unstructured concurrency as analogous to `goto`-based control flow: just as structured programming replaced `goto` with functions and loops (trading flexibility for predictability), structured concurrency replaces ad hoc task spawning with tree-structured task management.

The practical consequences are severe: "This lack of structure is one reason why concurrent programming is considered categorically more difficult than sequential programming."

# Examples

**Example 1** (Ch. 3, introduction): The source describes the typical unstructured pattern: a task is spawned, runs to completion concurrently, and the program becomes "essentially just a bag of tasks which live independently and might terminate at any time."

**Example 2** (Ch. 3, "Structured and unstructured idioms"): Idioms that lead to unstructured concurrency include:
- "Spawning tasks without awaiting their completion via a join handle, or dropping those join handles."
- "Select or race macros/functions. These are not inherently structured, but since they abruptly cancel futures, it's a common source of unstructured cancellation."
- "Worker tasks or pools."

**Example 3** (Ch. 3, footnote on join handles): "Using join handles mitigates these downsides somewhat, but is an ad hoc mechanism with no reliable guarantees. To get the full benefits of structured concurrency you have to be meticulous about always using them, as well as handling cancellation and errors properly."

# Relationships

## Builds Upon
- **async-task** -- unstructured concurrency is a pattern of task usage

## Enables
- Nothing directly -- unstructured concurrency is the pattern to be improved upon

## Related
- **cancellation-propagation** -- absent in unstructured concurrency, which is part of the problem

## Contrasts With
- **structured-concurrency** -- the disciplined alternative that organizes tasks into a tree

# Common Errors

- **Error**: Dropping join handles and assuming the spawned task will "just work."
  **Correction**: Dropped join handles mean the result (including errors) of the child task goes unobserved. Either await the handle or use a structured concurrency pattern.

- **Error**: Assuming another task is still running when sending it a message or signal.
  **Correction**: In unstructured concurrency, any task may have already terminated. Always handle the case where a peer task is gone.

# Common Confusions

- **Confusion**: Believing that using join handles makes concurrency structured.
  **Clarification**: Join handles are "an ad hoc mechanism with no reliable guarantees." Structured concurrency requires meticulous use of handles plus proper cancellation and error propagation -- difficult without language or library support.

- **Confusion**: Thinking unstructured concurrency is always wrong.
  **Clarification**: Unstructured concurrency is sometimes appropriate, particularly at the highest level of abstraction. The source describes a compromise pattern where top-level tasks are unstructured but structured concurrency is applied rigorously within each.

# Source Reference

Chapter 3: Structured Concurrency, introduction section. The concept is defined as the contrast/default against which structured concurrency is motivated. Additional discussion in "Structured and unstructured idioms" section and footnotes.

# Verification Notes

- Definition source: Direct quotation from Ch. 3 introduction, paragraph 3 and surrounding context
- Key Properties: All extracted from explicit statements in the source text
- Confidence rationale: HIGH -- the source explicitly characterizes unstructured concurrency with clear description of its properties and downsides
- Uncertainties: None for the definition; the source is thorough in its characterization
- Cross-reference status: All slugs reference cards in this extraction set
