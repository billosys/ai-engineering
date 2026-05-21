---
# === CORE IDENTIFICATION ===
concept: Function Clause
slug: function-clause

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: function-definition
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Modules and Functions"
chapter_number: 4
pdf_page: null
section: "Modules Are Where We Store Code"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - clause
  - clause head
  - clause body

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - pattern-matching
extends: []
related:
  - guard
  - case-expression
  - recursion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a function clause?"
  - "Does the order of function clauses matter?"
---

# Quick Definition

A function clause is one branch of a function definition: a head (name plus argument patterns, with an optional guard) and a body, joined by `->`. Clauses are tried in order; the first whose pattern matches is the one that runs.

# Core Definition

"The function `area` consists of two *clauses*. The clauses are separated by a semicolon, and the final clause is terminated by dot whitespace. Each clause has a *head* and a *body* separated by an arrow (`->`). The head consists of a function name followed by zero or more patterns, and the body consists of a sequence of *expressions* ... which are evaluated if the pattern in the head is successfully matched against the calling arguments. The clauses are tried in the order they appear in the function definition" (Chapter 4, "Modules Are Where We Store Code"). "Each pattern corresponds to exactly one clause." "When a function is entered, the clauses are pattern matched against the calling arguments in the order they are presented in the file" (Chapter 4, "Extending the Program"). Clause order matters in general, although it does not matter when the patterns are mutually exclusive. Semicolons separate clauses "in function definitions and in `case`, `if`, `try`..`catch`, and `receive` expressions" (Chapter 4, "Where to Put the Semicolons").

# Prerequisites

- **Function** — A clause is a constituent of a function definition.
- **Pattern matching** — A clause is selected by matching its head pattern against the call arguments.

# Key Properties

1. A clause has a head and a body joined by `->`.
2. The head is the function name plus zero or more argument patterns (and an optional `when` guard).
3. The body is a sequence of expressions.
4. Clauses of one function are separated by `;`; the final clause ends with dot-whitespace.
5. Clauses are tried top to bottom; the first whose pattern (and guard) matches runs.
6. Clause order matters in general, but not when the patterns are mutually exclusive.
7. If no clause matches, a runtime error (`no function clause matching`) is raised.

# Construction / Recognition

## To Write Clauses:
1. Write each branch as `name(Pattern) -> Body`.
2. Separate clauses with `;`.
3. End the last clause with `.` followed by whitespace.
4. Order clauses so the intended one is reached, especially when patterns overlap.

## To Recognize It:
1. Repeated `name(...)` definitions separated by semicolons within one function.

# Context & Application

- **Typical contexts**: Defining a function that behaves differently for different argument shapes.
- **Common applications**: One clause per geometric shape in `area/1`; a recursive list function with one clause for `[H|T]` and one for `[]`.
- **Historical/stylistic notes**: Replacing pattern matching with explicit `if`/`switch` is what Erlang clauses avoid — "the Erlang compiler generates optimal pattern matching code."

# Examples

**Example 1** (Chapter 4, "Modules Are Where We Store Code"): `area/1` has two clauses — `area({rectangle, Width, Height}) -> Width * Height;` and `area({square, Side}) -> Side * Side.` — each handling one shape.

**Example 2** (Chapter 4, "Back to Shopping"): `total([{What, N}|T]) -> shop:cost(What) * N + total(T); total([]) -> 0.` — a nonempty-list clause and an empty-list clause.

# Relationships

## Builds Upon
- **Function** — Clauses are the pieces a function is made of.
- **Pattern matching** — Each clause is chosen by matching its head.

## Enables
- **Recursion** — A recursive function uses a recursive clause and a base-case clause.

## Related
- **Guard** — A clause head may carry a `when` guard to refine matching.
- **Case expression** — `case` clauses follow the same pattern/body structure.
- **Recursion** — Base and recursive cases are written as separate clauses.

## Contrasts With
- No directly contrasting concept in these chapters.

# Common Errors

- **Error**: Ordering a general clause before a specific one so the specific clause is unreachable.
  **Correction**: Place more specific patterns first; remember clauses are tried top to bottom.

- **Error**: Separating clauses with `.` instead of `;`.
  **Correction**: Clauses are separated by `;`; only the final clause ends with `.`.

# Common Confusions

- **Confusion**: Believing clause order never matters.
  **Clarification**: Order is irrelevant only when patterns are mutually exclusive; otherwise it determines which clause runs.

- **Confusion**: Thinking a non-matching call falls through silently.
  **Clarification**: If no clause matches, the program fails with a runtime error — this is deliberate in Erlang.

# Source Reference

"Programming Erlang, Second Edition," Chapter 4: Modules and Functions, sections "Modules Are Where We Store Code," "Extending the Program," and "Where to Put the Semicolons." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 4, "Modules Are Where We Store Code" and "Extending the Program."
- Confidence rationale: HIGH — clauses (head, body, ordering) are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
