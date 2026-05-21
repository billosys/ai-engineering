---
# === CORE IDENTIFICATION ===
concept: List Comprehensions
slug: list-comprehensions

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: comprehensions
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "List Comprehensions: Generate and Test"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - generate and test
  - comprehension

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related:
  - recursion
  - higher-order-functions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a list comprehension in Erlang?"
  - "How do generators and tests work in a list comprehension?"
---

# Quick Definition

A list comprehension is an expression that generates list elements from one or more generators and applies optional Boolean tests, producing a list of results for every combination that passes all tests.

# Core Definition

List comprehensions are "expressions that generate elements and apply tests (or filters) to them" (Cesarini & Vinoski, p. 27). The format is `[Expression || Generators, Tests, Generators, Tests]`. A generator has the form `X <- [2,3,5,7,11]`, successively binding `X` to each list value — "the symbol `<-` is meant to suggest the 'element of' symbol for sets, ∈" (p. 28). "The Tests are Boolean expressions, which are evaluated for each combination of values of the bound variables. If all the Tests in a group return true, then the Expression is generated" (p. 28). Tests are optional; the construct as a whole "generates a list of results, one for each combination of values of the bound variables that passes all the tests."

# Prerequisites

- **Pattern matching** — A generator `Pattern <- List` matches each element against a pattern; understanding matching is required.

# Key Properties

1. Syntax: `[Expression || Generators, Tests]`.
2. A generator `X <- List` binds `X` to each element in turn.
3. Tests are Boolean expressions; using them is optional.
4. The expression is emitted once per combination of generator values passing all tests.
5. Multiple generators produce all combinations; later generators may depend on earlier bound variables.
6. The expression may have side effects, in which case the result list holds the side-effecting calls' return values.

# Construction / Recognition

## To Construct:
1. Write the result expression, then `||`.
2. List one or more generators (`Var <- List`).
3. Interleave Boolean tests to filter combinations.

## To Recognize:
1. Look for `[ ... || ... ]` with a `||` separating expression from generators/tests.

# Context & Application

- **Typical contexts**: Transforming and filtering lists concisely.
- **Common applications**: Rewriting `filter/2`; generating combinations; producing side effects over a list.
- **Historical/stylistic notes**: Modeled on set-theory comprehensions; the authors showcase the four-line N-queens solver.

# Examples

**Example 1** (p. 28): `filter/2` rewritten as a comprehension — `X` is the expression, `X<-Xs` the generator, `P(X)` the test:

```erlang
filter(P,Xs) -> [ X || X<-Xs, P(X) ].
```

**Example 2** (p. 29): Multiple generators, with the second depending on the first:

```erlang
6> [ {X,Y} || X <- [1,2], Y <- [X+3,X+4,X+5] ].
[{1,4},{1,5},{1,6},{2,5},{2,6},{2,7}]
```

**Example 3** (p. 29): The N-queens solver uses a comprehension with a generator and a `safe/3` test, and the `--` list-difference operator.

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- *(none specific in scope)*

## Related
- **Recursion** and **Higher-order functions** — Alternative approaches to the same list-manipulation tasks.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Expecting generator order not to matter when one generator depends on another.
  **Correction**: Generators evaluate left to right, so `X` must precede a generator that references `X`.

# Common Confusions

- **Confusion**: Thinking a comprehension with side effects returns nothing.
  **Clarification**: It still returns a list — of the return values of the side-effecting expressions (e.g., `[ok,ok,ok]`).

# Source Reference

Chapter 1: Introducing Erlang, Section "List Comprehensions: Generate and Test," pages 27-29.

# Verification Notes

- Definition source: Direct quotes from pp. 27-28.
- Confidence rationale: HIGH — explicit definition, syntax, and several examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
