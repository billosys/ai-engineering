---
# === CORE IDENTIFICATION ===
concept: Functional Programming
slug: functional-programming

# === CLASSIFICATION ===
category: core-idioms
subcategory: language-paradigm
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introduction"
chapter_number: null
pdf_page: null
section: "What's This Book About?"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - functional language
  - functional programming language

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - single-assignment-variable
  - concurrency-oriented-programming
  - higher-order-function
contrasts_with:
  - concurrency-vs-parallelism

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is functional programming?"
  - "Why does Erlang forbid mutable state?"
  - "What foundational concepts underpin error handling?"
---

# Quick Definition

Functional programming is a programming paradigm that forbids side effects and code that mutates shared state. Erlang belongs to the family of functional languages and uses immutable state to make concurrency safe.

# Core Definition

"Erlang belongs to the family of functional programming languages. Functional programming forbids code with side effects. Side effects and concurrency don't mix" (Introduction). In Erlang it is acceptable to mutate state within an individual process but not for one process to tinker with the state of another. Erlang has no mutexes, no synchronized methods, and none of the paraphernalia of shared-memory programming. The technical term for memory that can be modified is *mutable state*; Erlang is a functional language and has *immutable state* (Chapter 3, "Variables" sidebar "Absence of Side Effects Means We Can Parallelize Our Programs").

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Forbids code with side effects on shared data.
2. State is immutable: once a variable is bound, its value cannot change.
3. Functions can be passed as arguments and returned as values (higher-order functions).
4. Every expression has a value, including simple expressions like atoms and integers.
5. The absence of mutable shared state means programs can be parallelized without locks.

# Construction / Recognition

## To Recognize Functional Style in Erlang:

1. Variables are bound once and never reassigned.
2. There are no mutexes, locks, or synchronized blocks.
3. Computation proceeds by evaluating expressions, not executing statements that mutate memory.
4. Functions are used as data (passed to `lists:map/2`, returned by other functions).

# Context & Application

- **Typical contexts**: All Erlang code; the paradigm is enforced by the language.
- **Common applications**: Writing concurrent and distributed systems where shared mutable state would otherwise require locking.
- **Historical/stylistic notes**: The book quotes Brian Goetz ("It's the mutable state, stupid") to underline why functional programming and concurrency complement each other. Processes interact only by exchanging messages and share no data, which is why Erlang programs distribute easily over multicores or networks.

# Examples

**Example 1** (Introduction): "In Erlang it's OK to mutate state within an individual process but not for one process to tinker with the state of another process."

**Example 2** (Chapter 3, "Variables"): The Erlang way to express `X = X + 1` is to invent a new variable, e.g. `X1 = X + 1`, rather than mutate `X`.

# Relationships

## Builds Upon

- This is a foundational paradigm; it builds on no prior concept in the source.

## Enables

- **Single-assignment variable** — Immutability of variables is a direct consequence of functional programming.
- **Concurrency-oriented programming** — The absence of shared mutable state makes concurrency safe.
- **Higher-order function** — Treating functions as data is a hallmark of functional languages.

## Related

- **Message passing** — Processes share no data and interact only by messages, the functional analog of communication.

## Contrasts With

- **Imperative languages (C, Java)** — These use mutable variables and shared memory, requiring locks for concurrency.

# Common Errors

- **Error**: Trying to write `X = X + 1` to update a value.
  **Correction**: Bind a new variable, e.g. `X1 = X + 1`.

- **Error**: Expecting one process to modify another process's data directly.
  **Correction**: Send a message; processes share no memory.

# Common Confusions

- **Confusion**: Believing functional programming means no state at all.
  **Clarification**: A process may mutate its own internal state over its lifetime; what is forbidden is mutating another process's state and sharing mutable memory.

- **Confusion**: Thinking immutability is a limitation.
  **Clarification**: The book argues immutability simplifies debugging and makes programs easier to understand and to parallelize.

# Source Reference

Introduction, sections "What's This Book About?" and opening paragraphs; Chapter 3: Basic Concepts, "Variables," sidebar "Absence of Side Effects Means We Can Parallelize Our Programs."

# Verification Notes

- Definition source: Direct quotes from the Introduction and the Chapter 3 sidebar.
- Confidence rationale: HIGH — the source explicitly names and characterizes functional programming.
- Uncertainties: None.
- Cross-reference status: Verified concept names exist as planned cards.
- Re-extraction notes: Fresh extraction.
