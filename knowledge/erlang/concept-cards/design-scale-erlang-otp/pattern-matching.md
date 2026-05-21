---
# === CORE IDENTIFICATION ===
concept: Pattern Matching
slug: pattern-matching

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: pattern-matching
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Recursion and Pattern Matching"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - clause selection
  - matching

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - recursion
  - single-assignment-variables
  - selective-receive
  - records
  - maps
contrasts_with:
  - binary-pattern-matching

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Erlang select which function clause to run?"
  - "How does pattern matching work with already-bound variables?"
  - "What foundational Erlang concepts underpin the OTP behaviors?"
---

# Quick Definition

Pattern matching binds variables and selects function clauses by structurally comparing a pattern against a value. When a function is applied to an argument, the first clause whose pattern matches is used.

# Core Definition

A function is "presented in two clauses, where each clause has a head and a body, separated by the arrow (->). In the head we see the function applied to a pattern, and when a function is applied to an argument, the first clause whose pattern matches the argument is used" (Cesarini & Vinoski, p. 22). Patterns also decompose data: "the `[X|Xs]` syntax assigns the first element of the list, or head, to `X` and the remainder of the list, or tail, to `Xs`" (p. 22). Crucially, Erlang patterns may contain *already-bound* variables: "variables occurring in patterns can be already bound" (p. 31), in which case the match succeeds only if the value equals the existing binding.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A pattern can bind an unbound variable or constrain an already-bound one.
2. Clauses are tried in order; the first matching clause is selected.
3. `[]` matches the empty list; `[X|Xs]` matches a nonempty list, binding head and tail.
4. Matching an already-bound variable acts as an equality test.
5. Matching also works in `case` expressions, `receive` clauses, and `=` assignments.
6. A failed match raises a runtime error (or, in `receive`, leaves the message in the mailbox).

# Construction / Recognition

## To Construct:
1. Write a pattern in a function head, `case` clause, `receive` clause, or left of `=`.
2. Use literals to require exact values, variables to capture, and `_` to ignore.
3. Use structural patterns like `[H|T]`, `{A,B}`, or record/map patterns to decompose data.

## To Recognize:
1. Look for the clause head or left-hand side of `=`.
2. Determine which identifiers are unbound (capturing) versus already bound (constraining).

# Context & Application

- **Typical contexts**: Function-clause dispatch, list decomposition, message reception.
- **Common applications**: Replacing conditionals; selecting `receive` messages; extracting record/map fields.
- **Historical/stylistic notes**: The book prefers pattern matching in function heads over `case` expressions for clarity (p. 22, footnote 1).

# Examples

**Example 1** (p. 22): `print_all/1` uses `[]` and `[X|Xs]` patterns to select base and recursive clauses.

**Example 2** (p. 31): In the echo example, the variable `Pid` is already bound when the `receive` runs, so the `receive` "will accept only those messages in which the first component is that particular pid."

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- **Recursion** — Base and recursive clauses are chosen by matching.
- **Selective receive** — Each `receive` clause matches messages in the mailbox.
- **Records** and **Maps** — Both support pattern-based field extraction.

## Related
- **Single-assignment variables** — Re-matching a bound variable is an equality check.

## Contrasts With
- **Binary pattern matching** — A bit-level extension of pattern matching for binary data.

# Common Errors

- **Error**: Reusing a variable name in a pattern and expecting capture, when it is already bound.
  **Correction**: Use a fresh name to capture, or accept the equality constraint deliberately.

# Common Confusions

- **Confusion**: Assuming pattern variables always bind fresh, as in some other languages.
  **Clarification**: In Erlang an already-bound variable in a pattern constrains the match to its current value.

# Source Reference

Chapter 1: Introducing Erlang, Section "Recursion and Pattern Matching," pages 21-31. See also the "Bound Variables in Patterns" sidebar on p. 31.

# Verification Notes

- Definition source: Direct quotes from pp. 22 and 31.
- Confidence rationale: HIGH — explicitly defined with examples and a dedicated sidebar.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
