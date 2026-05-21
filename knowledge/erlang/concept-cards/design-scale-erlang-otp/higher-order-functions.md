---
# === CORE IDENTIFICATION ===
concept: Higher-Order Functions
slug: higher-order-functions

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: funs
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Fun with Anonymous Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - HOF
  - predicate

# === TYPED RELATIONSHIPS ===
prerequisites:
  - anonymous-functions
extends: []
related:
  - recursion
  - list-comprehensions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a higher-order function in Erlang?"
  - "What is a predicate?"
---

# Quick Definition

A higher-order function is a function that takes funs as arguments (and/or returns them). The classic example is `filter`, which applies a predicate fun to each list element.

# Core Definition

"Functions that take funs as arguments are called higher-order functions. An example of such a function is `filter`, where a predicate is represented by a fun that returns true or false, applied to the elements of a list. `filter` returns a list made up of those elements that have the required property; namely, those for which the fun returns true" (Cesarini & Vinoski, p. 25). The book defines a *predicate* as "a fun that, based on certain conditions defined in the function, returns the atoms true or false" (pp. 25-26).

# Prerequisites

- **Anonymous functions** — Higher-order functions consume funs; you must understand funs (and that functions are first-class) to use them.

# Key Properties

1. A higher-order function accepts one or more funs as arguments.
2. A predicate is a fun returning `true` or `false`.
3. `filter/2` keeps exactly the elements for which the predicate returns `true`.
4. The fun argument may be anonymous, a `fun Mod:F/N` reference, or a named fun.
5. Higher-order functions abstract iteration logic away from per-element decisions.

# Construction / Recognition

## To Construct:
1. Write a function whose parameter list includes a fun.
2. In the body, apply that fun to data (e.g., `P(X)`).

## To Recognize:
1. A function parameter that is later called as a function (e.g., `P(X)`).

# Context & Application

- **Typical contexts**: List processing where the per-element behavior varies by caller.
- **Common applications**: Filtering, mapping, folding collections.
- **Historical/stylistic notes**: Higher-order functions and list comprehensions are presented as two complementary approaches to list manipulation.

# Examples

**Example 1** (p. 25): `filter/2`, a higher-order function taking a predicate `P`:

```erlang
-module(ex3).
-export([filter/2, is_even/1]).
filter(P,[]) -> [];
filter(P,[X|Xs]) ->
    case P(X) of
        true ->
            [X|filter(P,Xs)];
        _ ->
            filter(P,Xs)
    end.

is_even(X) ->
    X rem 2 == 0.
```

**Example 2** (p. 26): Invoking it with an anonymous predicate: `ex3:filter(fun(X) -> X rem 2 == 0 end, [1,2,3,4])` returns `[2,4]`.

# Relationships

## Builds Upon
- **Anonymous functions** — The fun arguments a higher-order function consumes.

## Enables
- *(none specific in scope)*

## Related
- **Recursion** — `filter/2` is itself implemented recursively.
- **List comprehensions** — An alternative way to express the same filtering.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Passing a fun of the wrong arity to a higher-order function.
  **Correction**: Match the fun's arity to how the higher-order function applies it (e.g., `P(X)` needs arity 1).

# Common Confusions

- **Confusion**: Thinking a predicate may return any value.
  **Clarification**: A predicate specifically returns the atoms `true` or `false`.

# Source Reference

Chapter 1: Introducing Erlang, Section "Fun with Anonymous Functions," pages 25-26.

# Verification Notes

- Definition source: Direct quotes from pp. 25-26.
- Confidence rationale: HIGH — explicit definition with the `filter/2` example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
