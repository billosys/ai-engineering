---
# === CORE IDENTIFICATION ===
concept: Functional Programming
slug: functional-programming

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: programming-paradigm
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.5 Functional programming: Erlang's face to the world"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - functional language

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - single-assignment
  - fun
  - referential-transparency
  - message-passing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is functional programming?"
  - "How does functional programming apply to Erlang?"
  - "Is Erlang a pure functional language?"
---

# Quick Definition

Functional programming is a paradigm in which functions are data, algorithms are expressed through function calls rather than loops, and variables are never updated in place. Erlang is functional but not pure.

# Core Definition

"To summarize what functional programming is, the main ideas are that functions are data, just like integers and strings; that algorithms are expressed in terms of function calls, not using loop constructs like `while` and `for`; and that variables and values are never updated in place" (Chapter 1, section 1.5). Functional programming is "by no means the defining feature of Erlang — concurrency has that honor — but it's an important aspect." Erlang is not a "pure" functional language: it relies on side effects, but limits them to a single operation — message passing by copying. Each message is an effect on the outside world. Within itself, each process runs an almost purely functional program, which makes programs much easier to reason about than in traditional languages, without forcing the use of monads as in Haskell.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Functions are data — they can be passed, returned, and stored like any value.
2. Algorithms are expressed through function calls, not `while`/`for` loops.
3. Variables and values are never updated in place.
4. Erlang is functional but not pure — it permits side effects.
5. Erlang limits side effects to a single operation: message passing by copying.
6. Within a process, the program is almost purely functional.

# Construction / Recognition

## To Identify/Recognize:
1. Look for functions used as values (funs) and passed to other functions.
2. Look for recursion in place of explicit loops.
3. Note the absence of in-place variable updates.

# Context & Application

- **Typical contexts**: All Erlang code.
- **Common applications**: The functional mindset is a natural match for concurrent and distributed programming (the book cites Google MapReduce).
- **Historical/stylistic notes**: Erlang's syntax borrows mainly from the Prolog tradition rather than from C.

# Examples

**Example 1** (section 1.5): The book points to "Google MapReduce" as evidence that functional programming is a natural match for concurrent and distributed problems.

**Example 2** (section 1.5): Erlang limits side effects to message passing by copying — "each message is an effect on the world outside," yet each process runs an almost purely functional program.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- **Fun** — functions as data are a feature of functional programming.
- **Recursion** — recursion replaces loop constructs.
- **Single assignment** — values are never updated in place.

## Related
- **Referential transparency** — discussed alongside functional programming.
- **Message passing** — Erlang's single permitted side effect.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Trying to write loops with mutable counters as in C or Java.
  **Correction**: Express iteration through recursion and function calls; do not update variables in place.

# Common Confusions

- **Confusion**: Believing Erlang is a pure functional language.
  **Clarification**: Erlang is not pure; it allows side effects, but limits them to message passing by copying.

- **Confusion**: Thinking functional programming is Erlang's defining feature.
  **Clarification**: Concurrency is the defining feature; functional programming is an important but secondary aspect.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.5 "Functional programming: Erlang's face to the world."

# Verification Notes

- Definition source: Direct adaptation from section 1.5.
- Confidence rationale: HIGH — functional programming is explicitly summarized and Erlang's impurity stated.
- Uncertainties: None.
- Cross-reference status: `referential-transparency` and `recursion` are planned cards in this source.
- Re-extraction notes: Fresh extraction; no prior card.
