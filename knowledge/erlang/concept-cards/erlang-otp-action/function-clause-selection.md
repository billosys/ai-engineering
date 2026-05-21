---
# === CORE IDENTIFICATION ===
concept: Function Clauses and Clause Selection
slug: function-clause-selection

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: function-definition
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.5.2 Multiple clauses and pattern matching for choice"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - function clause
  - multiple clauses
  - clause selection
  - function_clause

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-function
  - pattern-matching
extends:
  - erlang-function
related:
  - guard
  - case-expression
  - let-it-crash
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a function clause?"
  - "How does Erlang choose which clause to run?"
  - "What happens when no clause matches?"
---

# Quick Definition

A function may consist of multiple clauses; Erlang selects which to run by trying them in top-down order, matching the call's arguments against each clause's patterns.

# Core Definition

"In Erlang, a function can consist of more than one *clause*" (Chapter 2, section 2.5.2). When the function is called, "Erlang tries the clauses in top-down order using pattern matching: first, it matches the incoming arguments against the patterns in the first clause; if they don't match, the next clause is tried, and so on." If no clause matches, you get a runtime exception of type `function_clause`. The clauses are separated by semicolons (`;`) and only the last is terminated by a period (`.`); all clauses must share the same name and arity and be defined together. Clauses make knowledge explicit: if execution reaches a later clause, the patterns of earlier clauses are known not to have matched. Spelling out the exact expected cases — rather than using a catch-all `(_, _)` — makes a function *fail early* on unexpected input, so bad data does not propagate.

# Prerequisites

- **Erlang function** — clauses make up a function.
- **Pattern matching** — clause selection works by matching argument patterns.

# Key Properties

1. A function may have multiple clauses.
2. Clauses are tried in top-down order.
3. The incoming arguments are matched against each clause's patterns.
4. The first matching clause is selected.
5. If no clause matches, a `function_clause` runtime exception is thrown.
6. Clauses are separated by semicolons; only the last ends with a period.
7. All clauses must share the same name and arity and be defined together.

# Construction / Recognition

## To Construct/Create:
1. Write each clause as a head (with patterns) `->` body.
2. Separate clauses with `;`; terminate the last with `.`.
3. Order clauses so more specific patterns come first if order matters.
4. Spell out the expected cases rather than using a catch-all.

# Context & Application

- **Typical contexts**: Defining functions whose behavior depends on argument shape or value.
- **Common applications**: Dispatching on tagged tuples; Boolean functions; recursion base/step cases.
- **Historical/stylistic notes**: When clause patterns are mutually exclusive (e.g. matching distinct tuple tags), clause order does not matter.

# Examples

**Example 1** (section 2.5.2): `either_or_both/2` has three clauses — `either_or_both(true, _) -> true; either_or_both(_, true) -> true; either_or_both(false, false) -> false.` — tried top-down; an unexpected value yields a `function_clause` exception.

**Example 2** (section 2.5.4): The `area/1` function has clauses for `{circle, Radius}`, `{square, Side}`, and `{rectangle, Height, Width}`; because the patterns are mutually exclusive, clause order does not matter.

# Relationships

## Builds Upon
- **Erlang function** — a function is made of clauses.
- **Pattern matching** — clause selection matches argument patterns.

## Enables
- **Guard** — clauses may carry guards for finer selection.
- Recursion via base and step clauses.

## Related
- **Case expression** — `case` offers clause-style branching within an expression.
- **Let it crash** — a `function_clause` exception makes a function fail early on bad input.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Using a catch-all `(_, _)` last clause "to be nice."
  **Correction**: This hides bad input; spell out expected cases so the function fails early on unexpected values.

- **Error**: Terminating every clause with a period.
  **Correction**: Clauses are separated by semicolons; only the last clause ends with a period.

# Common Confusions

- **Confusion**: Thinking clause order always matters.
  **Clarification**: Order matters only when clauses can both match; mutually exclusive clauses can be in any order.

# Source Reference

Chapter 2: Erlang language essentials, section 2.5.2 "Multiple clauses and pattern matching for choice" and section 2.5.4 "Patterns, clauses, and variable scope."

# Verification Notes

- Definition source: Direct adaptation from sections 2.5.2 and 2.5.4.
- Confidence rationale: HIGH — function clauses and clause selection are explicitly defined.
- Uncertainties: None.
- Cross-reference status: `case-expression` is a planned card in this source.
- Re-extraction notes: Fresh extraction; no prior card.
