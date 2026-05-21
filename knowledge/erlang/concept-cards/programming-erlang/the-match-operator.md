---
# === CORE IDENTIFICATION ===
concept: The Match Operator
slug: the-match-operator

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: operators
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Basic Concepts"
chapter_number: 3
pdf_page: null
section: "Variable Bindings and Pattern Matching"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "= operator"
  - pattern matching operator
  - equals operator

# === TYPED RELATIONSHIPS ===
prerequisites:
  - single-assignment-variable
extends: []
related:
  - pattern-matching
  - tuple
  - list
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Is = an assignment operator in Erlang?"
  - "What does the = operator do?"
---

# Quick Definition

In Erlang `=` is the match operator, not an assignment operator. `Lhs = Rhs` evaluates the right side and matches the result against the pattern on the left, binding any unbound variables and failing if the pattern does not fit.

# Core Definition

"`=` is not an assignment operator; it's actually a *pattern matching operator*" (Chapter 3, "Variables"). "In Erlang, however, `=` is a *pattern matching* operation. `Lhs = Rhs` really means this: evaluate the right side (`Rhs`), and then match the result against the pattern on the left side (`Lhs`)" (Chapter 3, "Variable Bindings and Pattern Matching"). A bare variable is "a simple form of pattern": the first time `X = SomeExpression` runs, Erlang binds `X` to make the statement true. "If at a later stage we say `X = AnotherExpression`, the match will succeed only if `SomeExpression` and `AnotherExpression` are identical." The value of the whole expression `Lhs = Rhs` "is defined to be `Rhs`." It behaves "like assignment when `X` is an unbound variable" — but with already-bound variables and compound patterns it instead tests for a match and may fail.

# Prerequisites

- **Single-assignment variable** — The match operator binds single-assignment variables; understanding bound vs. unbound is essential to predicting whether `=` succeeds.

# Key Properties

1. `=` matches, it does not assign.
2. `Lhs = Rhs` evaluates `Rhs`, then matches it against the pattern `Lhs`.
3. An unbound variable on the left is bound to make the match succeed.
4. An already-bound variable on the left succeeds only if its value equals `Rhs`.
5. The value of `Lhs = Rhs` is `Rhs`.
6. A failed match raises `** exception error: no match of right hand side value ...`.
7. Patterns on the left may be arbitrarily complex (tuples, lists), not just variables.

# Construction / Recognition

## To Use the Match Operator:
1. Write `Pattern = Expression`.
2. Erlang evaluates `Expression`.
3. It matches the result against `Pattern`, binding unbound variables.
4. If the structures cannot be made equal, a match error is raised.

## To Recognize a Match That Acts as Assignment:
1. The left side is a single, currently-unbound, uppercase variable.

## To Recognize a Match That Acts as a Test:
1. The left side contains bound variables or a compound pattern.

# Context & Application

- **Typical contexts**: Binding variables, extracting fields from tuples and lists, and writing inline tests.
- **Common applications**: `{point, X, Y} = Point` unpacks a tuple; `12 = area(...)` doubles as an assertion in test code.
- **Historical/stylistic notes**: Armstrong notes our brains read `X = ...` as assignment and are "almost right" — `X` is *almost* a variable and `=` is *almost* an assignment operator.

# Examples

**Example 1** (Chapter 3, "Variable Bindings and Pattern Matching"): `1> X = (2+4).` evaluates the right side to `6` and binds `X`; later `X = 6.` succeeds (prints `6`) because `X` already equals `6`, but `X = Y.` fails with a match error when `X` is `6` and `Y` is `10`.

**Example 2** (Chapter 4, "Adding Tests to Your Code"): `12 = area({rectangle, 3, 4})` works as a test — if `area(...)` did not return `12`, the match would fail and raise an error.

# Relationships

## Builds Upon
- **Single-assignment variable** — The match operator is how a variable receives its one and only binding.

## Enables
- **Pattern matching** — `=` is the explicit, operator form of the pattern-matching mechanism that pervades the language.

## Related
- **Pattern matching** — `=` is one place pattern matching occurs (also in function heads, `case`, `receive`).
- **Tuple** and **list** — Common compound patterns used on the left of `=`.

## Contrasts With
- No directly contrasting concept *card* in scope; the source contrasts `=` with the assignment operator of imperative languages.

# Common Errors

- **Error**: Writing `x = 123` with a lowercase `x`, expecting assignment.
  **Correction**: `x` is an atom; matching the atom `x` against `123` fails. Use an uppercase variable.

- **Error**: Reusing a bound variable on the left of `=` and expecting it to take the new value.
  **Correction**: With a bound variable, `=` is a test; it fails unless both sides are equal.

# Common Confusions

- **Confusion**: Believing `=` assigns, like in C or Java.
  **Clarification**: `=` matches. It only *resembles* assignment when the left side is a single unbound variable.

- **Confusion**: Thinking `=` always produces a usable result.
  **Clarification**: If the pattern does not match the value, `=` raises an exception rather than returning anything.

# Source Reference

"Programming Erlang, Second Edition," Chapter 3: Basic Concepts, sections "Variables," "Variable Bindings and Pattern Matching," and "Extracting Values from Tuples." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 3, "Variable Bindings and Pattern Matching."
- Confidence rationale: HIGH — the source repeatedly and explicitly states `=` is a pattern matching operator.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
