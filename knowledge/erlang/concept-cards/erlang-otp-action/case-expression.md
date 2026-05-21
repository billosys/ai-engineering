---
# === CORE IDENTIFICATION ===
concept: Case and If Expressions
slug: case-expression

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: control-flow
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.6 Case and if expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - case expression
  - if expression
  - "case ... of ... end"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
  - function-clause-selection
extends: []
related:
  - guard
  - tuple
contrasts_with:
  - function-clause-selection

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a case expression?"
  - "How is an if expression different from a case expression?"
  - "Does Erlang have an if-then-else?"
---

# Quick Definition

A `case` expression is an in-expression branch construct with clauses matched against a switch value; an `if` expression is a stripped-down `case` whose clauses depend only on guards.

# Core Definition

"Erlang provides `case` expressions" for making control-flow branches without inventing a new function name for each choice (Chapter 2, section 2.6). A `case` expression has one or more clauses, each with one pattern (no parentheses needed), of the form `case Value of Pattern -> Body; ... end`. Clauses are separated by semicolons; the whole expression ends with the keyword `end` (no semicolon after the last clause — they are separators, not terminators). To switch on multiple items, group them in a tuple. `case` clauses may carry guards. Erlang has no Boolean if-then-else — you use a `case` instead. An `if` expression (section 2.6.2) is "a stripped-down variant of `case` expressions, without a specific value to switch on and without patterns"; its clauses depend only on guards, and a catch-all clause is written `true -> ...` because a guard that is always true always matches.

# Prerequisites

- **Pattern matching** — `case` clauses match patterns against a value.
- **Function clauses and clause selection** — `case`/`if` reuse the clause idea inside an expression.

# Key Properties

1. A `case` expression branches by matching clauses against a switch value.
2. `case` clauses have one pattern each and are separated by semicolons.
3. A `case` expression ends with the keyword `end`.
4. Multiple switch items are grouped using a tuple.
5. `case` and `if` clauses may carry guards.
6. Erlang has no Boolean if-then-else; a `case` is used instead.
7. An `if` expression has no switch value and no patterns — only guards; its catch-all is `true -> ...`.

# Construction / Recognition

## To Construct/Create:
1. Write `case Expr of`, then clauses `Pattern [when Guard] -> Body`, separated by `;`, then `end`.
2. To switch on several values, build a tuple: `case {A, B} of ...`.
3. For a pure guard switch, write `if Guard1 -> ...; ...; true -> ... end`.

# Context & Application

- **Typical contexts**: Branching within a function body.
- **Common applications**: Choosing behavior without defining extra functions; checking a Boolean result with explicit `true`/`false` clauses.
- **Historical/stylistic notes**: `if` expressions were "added to the language a long time ago, a bit on a whim" and are not used often; many programmers consider them a waste of the `if` keyword.

# Examples

**Example 1** (section 2.6): The `area/1` function rewritten as `area(Shape) -> case Shape of {circle, Radius} -> ...; {square, Side} -> ...; {rectangle, Height, Width} -> ... end.`

**Example 2** (section 2.6.2): `sign(N) when is_number(N) -> if N > 0 -> positive; N < 0 -> negative; true -> zero end.` — an `if` expression with a `true ->` catch-all.

# Relationships

## Builds Upon
- **Pattern matching** and **function clause selection** — `case`/`if` apply the clause idea inside an expression.

## Enables
- In-expression branching without extra function definitions.

## Related
- **Guard** — `case` and `if` clauses use guards; `if` clauses use only guards.
- **Tuple** — used to switch on multiple values in a `case`.

## Contrasts With
- **Function clauses and clause selection** — function clauses branch at the function level; `case`/`if` branch within an expression.

# Common Errors

- **Error**: Using an underscore catch-all in the last `case` clause of a Boolean switch.
  **Correction**: Spell out both `true` and `false` so the program fails early on unexpected input and Dialyzer can see the intent.

- **Error**: Putting a semicolon after the last `case`/`if` clause.
  **Correction**: Clause separators are semicolons; the last clause has none — the expression ends with `end`.

# Common Confusions

- **Confusion**: Expecting an Erlang Boolean if-then-else.
  **Clarification**: There is none; use a `case` expression. The `if` expression is a guard-only switch, not a Boolean if-then-else.

# Source Reference

Chapter 2: Erlang language essentials, section 2.6 "Case and if expressions," including 2.6.1 and 2.6.2.

# Verification Notes

- Definition source: Direct adaptation from section 2.6.
- Confidence rationale: HIGH — `case` and `if` expressions are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card. Merged `case` and `if` into one card since `if` is presented by the source explicitly as a stripped-down variant of `case`.
