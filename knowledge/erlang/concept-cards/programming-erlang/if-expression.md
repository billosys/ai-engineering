---
# === CORE IDENTIFICATION ===
concept: If Expression
slug: if-expression

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
  - if ... end
  - if statement

# === TYPED RELATIONSHIPS ===
prerequisites:
  - guard
extends: []
related:
  - case-expression
  - function-clause
contrasts_with:
  - case-expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an if expression in Erlang?"
  - "Why does an if expression need a true guard?"
---

# Quick Definition

An `if` expression evaluates a series of guards in order and runs the body of the first guard that succeeds. Unlike many languages, every Erlang `if` must have at least one succeeding guard or it raises an exception.

# Core Definition

"A second conditional primitive, `if`, is also provided" (Chapter 4, "if Expressions"). Its syntax is:

```erlang
if
    Guard1 -> Expr_seq1;
    Guard2 -> Expr_seq2;
    ...
end
```

"This is evaluated as follows: First `Guard1` is evaluated. If this evaluates to `true`, then the value of `if` is the value obtained by evaluating the expression sequence `Expr_seq1`. If `Guard1` does not succeed, `Guard2` is evaluated, and so on, until a guard succeeds. At least one of the guards in the `if` expression must evaluate to `true`; otherwise, an exception will be raised." Because `if` is an expression and "all expressions are supposed to have values," an `if` with no succeeding guard "would be an error in Erlang and cause the program to crash." For this reason "the Erlang programmer will often add a `true` guard at the end of an `if` expression" as a catchall — the atom `true` always succeeds.

# Prerequisites

- **Guard** — Each branch of an `if` is a guard; understanding guards is essential.

# Key Properties

1. `if ... end` evaluates a sequence of guards top to bottom.
2. The body of the first succeeding guard runs; its value is the `if`'s value.
3. Each branch is `Guard -> ExprSequence`.
4. At least one guard must succeed, or an exception is raised.
5. A final `true` guard is the conventional catchall, since the atom `true` always succeeds.
6. `if` is an expression: it must always produce a value.

# Construction / Recognition

## To Write an If Expression:
1. Write `if`.
2. List `Guard -> Body` branches separated by `;`.
3. Optionally add a final `true -> Body` catchall.
4. Close with `end`.

## To Recognize It:
1. The keywords `if ... end` with guards before each `->`.

# Context & Application

- **Typical contexts**: Choosing between actions purely on guard conditions, inside a function body.
- **Common applications**: Simple conditional logic where there is no value to pattern-match.
- **Historical/stylistic notes**: Programmers coming from C write `if` without an `else`; in Erlang that risks a crash, so a `true` catchall is added unless an exception is actually wanted.

# Examples

**Example 1** (Chapter 4, "Use of the true Guard"): The skeleton `if Guard -> Expressions; Guard -> Expressions; ...; true -> Expressions end` shows the atom `true` used as a catchall final guard.

**Example 2** (Chapter 4, "if Expressions"): `if A > 0 -> do_this() end` — modeled on a C `if` with no `else` — crashes when `A =< 0` because the `if` then has no value; adding `true -> ...` avoids the exception.

# Relationships

## Builds Upon
- **Guard** — Every `if` branch is a guard.

## Enables
- Compact guard-based branching without patterns.

## Related
- **Case expression** — The other conditional primitive.
- **Function clause** — `if` is an in-body alternative to guard-bearing clauses.

## Contrasts With
- **Case expression** — `case` matches a computed value against patterns (with optional guards); `if` has no value and selects purely on guards.

# Common Errors

- **Error**: Writing an `if` with no guard that can succeed (a C-style `if` without an `else`).
  **Correction**: Add a final `true ->` branch, or expect an exception when no guard holds.

- **Error**: Expecting an `if` with no matching branch to simply do nothing.
  **Correction**: `if` is an expression and must yield a value; no succeeding guard raises an exception.

# Common Confusions

- **Confusion**: Thinking an Erlang `if` works like a C `if` statement.
  **Clarification**: Erlang `if` is an *expression* that must produce a value; it requires a succeeding guard or it crashes.

- **Confusion**: Confusing `if` with `case`.
  **Clarification**: `case` matches a value against patterns; `if` only evaluates guards and has no value to match.

# Source Reference

"Programming Erlang, Second Edition," Chapter 4: Modules and Functions, section "case and if Expressions" (subsection "if Expressions") and "Use of the true Guard." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations and syntax skeleton from Chapter 4, "if Expressions."
- Confidence rationale: HIGH — syntax, evaluation, and the must-succeed rule are explicitly stated.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
