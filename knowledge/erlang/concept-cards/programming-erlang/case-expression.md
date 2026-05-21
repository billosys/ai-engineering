---
# === CORE IDENTIFICATION ===
concept: Case Expression
slug: case-expression

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: control-flow
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Modules and Functions"
chapter_number: 4
pdf_page: null
section: "case and if Expressions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - case ... of
  - case statement

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
  - function-clause
extends: []
related:
  - if-expression
  - guard
contrasts_with:
  - if-expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a case expression?"
  - "When should I use case instead of separate function clauses?"
---

# Quick Definition

A `case` expression evaluates an expression and matches its value against a series of patterns (each with an optional guard), running the body of the first that matches. It is a control structure used when defining separate function clauses is inconvenient.

# Core Definition

"`case` has the following syntax" (Chapter 4, "case Expressions"):

```erlang
case Expression of
    Pattern1 [when Guard1] -> Expr_seq1;
    Pattern2 [when Guard2] -> Expr_seq2;
    ...
end
```

"`case` is evaluated as follows: First, `Expression` is evaluated; assume this evaluates to `Value`. Thereafter, `Value` is matched in turn against `Pattern1` (with the optional guard `Guard1`), `Pattern2`, and so on, until a match is found. As soon as a match is found, then the corresponding expression sequence is evaluated — the result of evaluating the expression sequence is the value of the `case` expression. If no pattern matches, then an exception is raised." `case` and `if` are used "sometimes [when] defining lots of separate function clauses is inconvenient." Armstrong notes "strictly speaking, `case` is unnecessary" — anything written with `case` could be written with extra function clauses — but doing so "is rather ugly" because it forces inventing extra helper functions.

# Prerequisites

- **Pattern matching** — `case` selects a branch by matching the value against patterns.
- **Function clause** — `case` is an alternative to writing extra function clauses.

# Key Properties

1. `case Expression of ... end` evaluates `Expression`, then matches its value against patterns.
2. Each branch is `Pattern [when Guard] -> ExprSequence`.
3. The first matching branch's expression sequence runs; its value is the `case`'s value.
4. Branches are tried in order, top to bottom.
5. Branches may carry optional `when` guards.
6. If no pattern matches, an exception is raised.
7. It is logically unnecessary (clauses could replace it) but avoids ugly helper functions.

# Construction / Recognition

## To Write a Case Expression:
1. Write `case Expression of`.
2. List `Pattern [when Guard] -> Body` branches separated by `;`.
3. Close with `end` (the last branch has no trailing semicolon).

## To Recognize It:
1. The keywords `case ... of ... end`.

# Context & Application

- **Typical contexts**: Branching on the value of an expression inside a function body.
- **Common applications**: `filter/2` branches on `P(H)` being `true` or `false`; `odds_and_evens_acc` branches on `H rem 2`.
- **Historical/stylistic notes**: `case` keeps related branching logic together instead of splitting it across helper functions like `filter1`.

# Examples

**Example 1** (Chapter 4, "case Expressions"): `filter` defined with `case P(H) of true -> [H|filter(P, T)]; false -> filter(P, T) end` — branching on whether the predicate holds.

**Example 2** (Chapter 4, "Accumulators"): `odds_and_evens_acc` uses `case (H rem 2) of 1 -> ...; 0 -> ... end` to route each element to the odds or evens accumulator.

# Relationships

## Builds Upon
- **Pattern matching** — `case` branches are selected by matching.
- **Function clause** — `case` is an in-body alternative to separate clauses.

## Enables
- Compact in-function branching without inventing helper functions.

## Related
- **Guard** — `case` branches may carry optional guards.
- **If expression** — The other conditional primitive.

## Contrasts With
- **If expression** — `case` matches a value against *patterns* (with optional guards); `if` has no value to match and chooses purely on *guards*.

# Common Errors

- **Error**: Writing a `case` whose patterns do not cover the actual value.
  **Correction**: Ensure a pattern matches every possible value, or `case` raises an exception when none matches.

- **Error**: Putting a semicolon after the last branch.
  **Correction**: Branches are separated by `;`; the final branch before `end` has none.

# Common Confusions

- **Confusion**: Thinking `case` is essential.
  **Clarification**: It is "strictly speaking unnecessary" — equivalent code can use extra function clauses — but `case` avoids the ugliness of helper functions.

- **Confusion**: Confusing `case` with `if`.
  **Clarification**: `case` matches a computed value against patterns; `if` evaluates only guards and matches no value.

# Source Reference

"Programming Erlang, Second Edition," Chapter 4: Modules and Functions, section "case and if Expressions" (subsection "case Expressions"). EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations and syntax skeleton from Chapter 4, "case Expressions."
- Confidence rationale: HIGH — syntax and evaluation rules are explicitly stated.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
