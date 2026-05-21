---
# === CORE IDENTIFICATION ===
concept: Guard
slug: guard

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: guards
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.5.3 Guards"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - guard test
  - "when clause"
  - type test

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-clause-selection
extends:
  - function-clause-selection
related:
  - pattern-matching
  - case-expression
  - bif
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a guard in Erlang?"
  - "What can and cannot appear in a guard?"
  - "Why can't a guard call your own functions?"
---

# Quick Definition

A guard is an extra requirement on a clause, introduced by the keyword `when`, containing one or more limited tests that must all be true for the clause to be selected.

# Core Definition

"You can add extra requirements to the clauses... using *guards*" (Chapter 2, section 2.5.3). "A clause guard begins with the keyword `when` and ends at the `->` arrow. It contains one or more tests, separated by commas if there are more than one, and all of them have to be `true` for the clause to be selected." Guards commonly use *type tests* — built-in functions like `is_boolean(...)`, `is_atom(...)`, `is_integer(...)` (from the `erlang` module). "The number of things you can do within a guard is strictly limited": you may use most operators and some BIFs (like `self()`), but you cannot call your own functions or functions in another module. This is partly for efficiency, but mostly because of side effects — if a guard fails, you must be able to try the next clause "as if nothing happened," which would be impossible if a guard could, for example, send a message.

# Prerequisites

- **Function clauses and clause selection** — a guard is an extra requirement on a clause.

# Key Properties

1. A guard begins with `when` and ends at the `->` arrow.
2. It contains one or more tests; with commas, all must be true.
3. Type tests (`is_boolean`, `is_atom`, `is_integer`, ...) are common guard BIFs.
4. Guards may use most operators and some BIFs (like `self()`).
5. Guards cannot call user-defined functions or functions in other modules.
6. The restriction exists for efficiency and, mainly, to forbid side effects.
7. A failed guard lets execution proceed to the next clause as if nothing happened.

# Construction / Recognition

## To Construct/Create:
1. After the clause head, write `when` followed by one or more tests.
2. Separate multiple tests with commas (all must hold).
3. End the guard at the `->` arrow.
4. Use variables from the pattern so the guard can refer to them.

# Context & Application

- **Typical contexts**: Function clauses, `case` clauses, and `if` expressions.
- **Common applications**: Restricting clauses to specific types or value ranges; plugging holes that pattern matching alone cannot.
- **Historical/stylistic notes**: The side-effect-free nature of guards makes clauses easy to reason about, reorder, and refactor.

# Examples

**Example 1** (section 2.5.3): `either_or_both(true, B) when is_boolean(B) -> true;` — the guard `is_boolean(B)` ensures the second argument is a Boolean, rejecting calls like `either_or_both(true, 42)`.

**Example 2** (section 2.6.2): `sign(N) when is_number(N) -> if N > 0 -> positive; N < 0 -> negative; true -> zero end.` uses guards both on the function clause and within the `if` expression.

# Relationships

## Builds Upon
- **Function clauses and clause selection** — guards refine clause selection.

## Enables
- Type- and value-restricted clause selection; `if` expressions.

## Related
- **Pattern matching** — guards complement patterns in choosing clauses.
- **Case expression** — `case` clauses can also carry guards.
- **Built-in function** — type tests in guards are BIFs.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Calling your own function inside a guard.
  **Correction**: Guards may not call user-defined functions; use only operators, type tests, and permitted BIFs.

- **Error**: Relying on pattern matching alone where a type assertion is needed.
  **Correction**: Add a guard (e.g. `when is_boolean(B)`) to reject unexpected values that a pattern would otherwise accept.

# Common Confusions

- **Confusion**: Thinking a guard can contain any expression.
  **Clarification**: Guard tests are strictly limited — no user function calls, no side effects — so a failed guard can be abandoned cleanly.

# Source Reference

Chapter 2: Erlang language essentials, section 2.5.3 "Guards." See also section 2.6.2 "If expressions."

# Verification Notes

- Definition source: Direct adaptation from section 2.5.3.
- Confidence rationale: HIGH — guards, their syntax, and their restrictions are explicitly defined.
- Uncertainties: None.
- Cross-reference status: `case-expression` is a planned card in this source.
- Re-extraction notes: Fresh extraction; no prior card.
