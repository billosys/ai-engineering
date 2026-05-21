---
# === CORE IDENTIFICATION ===
concept: Guard
slug: guard

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: clause-selection
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Modules and Functions"
chapter_number: 4
pdf_page: null
section: "Guards"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "when clause"
  - guard sequence
  - guard expression

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function-clause
  - pattern-matching
extends: []
related:
  - case-expression
  - if-expression
  - bif
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a guard in Erlang?"
  - "How do I add conditions to a function clause?"
---

# Quick Definition

A guard is a side-effect-free test, introduced by `when`, that further restricts when a clause matches. It lets a clause perform simple comparisons on its variables beyond plain pattern matching.

# Core Definition

"Guards are constructs that we can use to increase the power of pattern matching. Using guards, we can perform simple tests and comparisons on the variables in a pattern" (Chapter 4, "Guards"). Guards appear "in the heads of function definitions where they are introduced by the `when` keyword," or anywhere an expression is allowed, where they "evaluate to one of the atoms `true` or `false`." If a guard evaluates to `true` it *succeeds*; otherwise it *fails*. A *guard sequence* `G1; G2; ...; Gn` is true if at least one guard is true (the `;` means "or"); a single *guard* `GuardExpr1, GuardExpr2, ...` is true only if all guard expressions are true (the `,` means "and"). The set of valid guard expressions is a restricted subset of Erlang — atoms, constants, term comparisons, arithmetic and boolean expressions, the guard predicates (`is_integer`, `is_atom`, ...) and guard BIFs (`abs`, `length`, `element`, ...) — chosen to guarantee that guards "are side effect free and terminate." Guards "cannot call user-defined functions."

# Prerequisites

- **Function clause** — Guards most often refine which function clause applies.
- **Pattern matching** — A guard is "an extension of pattern matching"; the pattern must match before the guard is tested.

# Key Properties

1. A guard is introduced by the `when` keyword in a clause head.
2. It extends pattern matching with simple tests and comparisons.
3. It evaluates to `true` (succeeds) or `false` (fails).
4. In a guard, `,` means "and"; in a guard sequence, `;` means "or".
5. Guard expressions are a restricted subset of Erlang — chosen to be side-effect-free and terminating.
6. Guards may call guard predicates (`is_integer/1`, etc.) and guard BIFs (`abs/1`, `length/1`, ...).
7. Guards cannot call user-defined functions.
8. `andalso`/`orelse` are short-circuit guard operators; `and`/`or` evaluate both arguments.

# Construction / Recognition

## To Add a Guard:
1. After the clause head's pattern, write `when GuardExpression`.
2. Combine tests with `,` (and) within a guard, or `;` (or) across a guard sequence.
3. Use only guard-legal expressions — predicates, comparisons, arithmetic, guard BIFs.

## To Recognize It:
1. A `when` keyword between a clause head and its `->`.

# Context & Application

- **Typical contexts**: Function clause heads, `case` clauses, `if` expressions.
- **Common applications**: `max(X, Y) when X > Y -> X;` selects the clause only when `X` is the larger; `is_integer(X), X > Y` tests type and order together.
- **Historical/stylistic notes**: "In practice, few programs use complex guards, and simple (`,`) guards suffice for most programs." Old guard names like `integer(X)` are obsolete; use `is_integer(X)`.

# Examples

**Example 1** (Chapter 4, "Guards"): `max(X, Y) when X > Y -> X; max(X, Y) -> Y.` — the first clause is taken only when the guard `X > Y` succeeds.

**Example 2** (Chapter 4, "Guard Examples"): `f(X,Y) when is_integer(X), X > Y, Y < 6 -> ...` — the comma-separated guard means "X is an integer, and X is greater than Y, and Y is less than 6."

# Relationships

## Builds Upon
- **Function clause** — Guards refine clause selection.
- **Pattern matching** — Guards extend matching; the pattern must succeed first.

## Enables
- **If expression** — `if` is built entirely from guards.

## Related
- **Case expression** — `case` clauses may carry optional guards (`Pattern when Guard ->`).
- **If expression** — Each `if` branch is a guard.
- **BIF** — Guard BIFs are the built-in functions usable inside guards.

## Contrasts With
- No directly contrasting concept in these chapters.

# Common Errors

- **Error**: Calling a user-defined function inside a guard.
  **Correction**: Guards may only use guard-legal expressions, predicates, and guard BIFs — never user functions.

- **Error**: Using `and`/`or` and expecting short-circuit evaluation.
  **Correction**: `and`/`or` evaluate both arguments; use `andalso`/`orelse` for short-circuit behavior (e.g., to guard against division by zero).

# Common Confusions

- **Confusion**: Thinking a guard runs before the pattern is matched.
  **Clarification**: Pattern matching happens first; the guard is an additional test on the already-matched variables.

- **Confusion**: Mixing up `,` and `;` in guards.
  **Clarification**: Within one guard, `,` means "and"; across a guard sequence, `;` means "or".

# Source Reference

"Programming Erlang, Second Edition," Chapter 4: Modules and Functions, section "Guards" (including "Guard Sequences," "Guard Examples," "Use of the true Guard," and Tables 1-2 of guard predicates and BIFs). EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 4, "Guards."
- Confidence rationale: HIGH — guards, guard sequences, and the side-effect-free restriction are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
