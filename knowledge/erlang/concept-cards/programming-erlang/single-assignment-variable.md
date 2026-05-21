---
# === CORE IDENTIFICATION ===
concept: Single-Assignment Variable
slug: single-assignment-variable

# === CLASSIFICATION ===
category: core-idioms
subcategory: variables
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Basic Concepts"
chapter_number: 3
pdf_page: null
section: "Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - immutable variable
  - bound variable
  - unbound variable
  - variable binding

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - the-match-operator
  - pattern-matching
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why can't I change a variable's value in Erlang?"
  - "What is a single-assignment variable?"
---

# Quick Definition

A single-assignment variable can be given a value only once. After it is bound, that value can never change; attempting to rebind it to a different value raises a match error.

# Core Definition

"Erlang has *single-assignment variables*. As the name suggests, they can be given a value only once. If you try to change the value of a variable once it has been set, then you'll get an error" (Chapter 3, "Erlang Variables Do Not Vary"). "A variable that has had a value assigned to it is called a *bound* variable; otherwise, it is called an *unbound* variable." "When Erlang sees a statement such as `X = 1234` and `X` has not been bound before, then it binds the variable `X` to the value `1234`. ... once it gets a value, it keeps it forever." Variable names must start with an uppercase letter. The scope of a variable "is the lexical unit in which it is defined" — there are no global variables, and the same name in different functions is unrelated. Erlang is a functional language with *immutable state*; to express something like `X = X + 1`, you "invent a new variable ... (say `X1`) and ... write `X1 = X + 1`."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A variable may be bound to a value only once.
2. Before binding, a variable is *unbound*; after binding, it is *bound*.
3. A bound variable's value can never be changed.
4. Variable names must start with an uppercase letter (e.g., `X`, `This`, `A_long_name`).
5. A variable's scope is the lexical unit (clause/function) in which it appears.
6. The same name in different functions refers to unrelated variables.
7. Rebinding to a *different* value raises `** exception error: no match of right hand side value`.

# Construction / Recognition

## To Bind a Variable:
1. Write `Variable = Expression` where `Variable` is currently unbound.
2. Erlang evaluates `Expression` and binds the variable to that value permanently.

## To "Update" a Value:
1. Do not rebind; instead introduce a fresh variable name.
2. Write `X1 = X + 1` rather than `X = X + 1`.

## To Recognize It:
1. A capitalized name bound exactly once within its scope.

# Context & Application

- **Typical contexts**: Every Erlang program; every variable is single-assignment.
- **Common applications**: Threading evolving values through a computation by introducing `X1`, `X2`, etc.
- **Historical/stylistic notes**: Armstrong compares it to algebra: "if there's an X in several different parts in the same equation, then all the Xs mean the same thing." Immutable state is also what makes Erlang programs safe to parallelize — "there is no shared memory, and there are no locks."

# Examples

**Example 1** (Chapter 3, "Variables"): `1> X = 123456789.` binds `X`; later `4> X = 1234.` fails with `** exception error: no match of right hand side value 1234`.

**Example 2** (Chapter 3, "Why Single Assignment Improves Our Programs"): To express `X = X + 1`, the Erlang way is to "invent a new variable whose name hasn't been used before (say `X1`) and to write `X1 = X + 1`."

# Relationships

## Builds Upon
- This is a foundational concept and does not build upon another card in this source.

## Enables
- **The match operator** — `=` behaves as assignment precisely when the left side is an unbound single-assignment variable.
- **Pattern matching** — Single-assignment semantics determine when a match succeeds or fails.

## Related
- **The match operator** — The `=` that performs the one-time binding.
- **Pattern matching** — Binds variables as a side effect of a successful match.

## Contrasts With
- No directly contrasting concept *card* in scope; the source contrasts Erlang variables with mutable variables in imperative languages such as C and Java.

# Common Errors

- **Error**: Trying to reuse a bound variable for a new value (`X = X + 1`).
  **Correction**: Introduce a new name (`X1 = X + 1`); bound variables cannot be changed.

- **Error**: Writing a variable with a lowercase initial letter.
  **Correction**: Variables must start with an uppercase letter; a lowercase name is an atom.

# Common Confusions

- **Confusion**: Thinking single-assignment makes programming harder by forbidding updates.
  **Clarification**: It is "a benefit, not a problem" — programs where a variable cannot change are far easier to understand and debug, since there is only one place a value was set.

- **Confusion**: Believing `X` is a memory address whose contents you change.
  **Clarification**: In Erlang `X` is a name for a value that can never change, unlike the disguised memory address in imperative languages.

# Source Reference

"Programming Erlang, Second Edition," Chapter 3: Basic Concepts, sections "Variables," "Erlang Variables Do Not Vary," and "Why Single Assignment Improves Our Programs." EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotations from Chapter 3, "Erlang Variables Do Not Vary."
- Confidence rationale: HIGH — the term "single-assignment variables" is explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
