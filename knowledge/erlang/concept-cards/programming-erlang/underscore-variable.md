---
# === CORE IDENTIFICATION ===
concept: Underscore Variable
slug: underscore-variable

# === CLASSIFICATION ===
category: core-idioms
subcategory: variables
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Underscore Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "_Var"
  - underscore-prefixed variable

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
extends: []
related: []
contrasts_with:
  - anonymous-variable

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an underscore variable?"
  - "How does _Var differ from the anonymous variable _?"
  - "Why use an underscore-prefixed variable?"
---

# Quick Definition

An underscore variable, `_VarName`, is a normal variable that the compiler treats specially: it suppresses the "variable used only once" warning, but unlike `_` it is still a real, bindable variable.

# Core Definition

"The special syntax `_VarName` is used for a normal variable, not an anonymous variable" ("The Rest of Sequential Erlang", *Underscore Variables*). "Normally the compiler will generate a warning if a variable is used only once in a clause since this is usually the sign of an error. If the variable is used only once but starts with an underscore, the warning message will not be generated." Because `_Var` is a normal variable, "very subtle bugs can be caused by forgetting this and using it as a 'don't care' pattern" — in a complicated pattern match, an accidentally repeated `_Int` still binds and can cause a match to fail. There are two main uses: naming a variable you do not intend to use (e.g. `open(File, _Mode)` reads better than `open(File, _)`), and debugging — renaming `Q` to `_Q` lets you comment out the only use without triggering an unused-variable warning.

# Prerequisites

- **Pattern matching** — Underscore variables matter chiefly in pattern matching contexts.

# Key Properties

1. `_VarName` is a normal, bindable variable — not the anonymous variable.
2. The compiler suppresses the "used only once" warning for underscore-prefixed variables.
3. Because it binds, a repeated `_Var` in a pattern still imposes an equality constraint.
4. Used to name a deliberately unused variable readably.
5. Used in debugging so a variable's only use can be commented out without a warning.

# Construction / Recognition

## To Construct/Create:
1. Prefix a variable name with an underscore: `_Mode`, `_Q`.

## To Identify/Recognize:
1. A name starting with `_` followed by letters is an underscore variable (a real variable); a lone `_` is the anonymous variable.

# Context & Application

- **Typical contexts**: function heads with unused parameters; debugging.
- **Common applications**: `open(File, _Mode)` documents the unused argument; renaming `Q` to `_Q` lets a debug `io:format` be commented out warning-free.
- **Historical/stylistic notes**: the leading underscore signals intent ("I know this is unused") to both reader and compiler.

# Examples

**Example 1** (*Underscore Variables*): debugging without an unused-variable warning:

```erlang
some_func(X) ->
    {P, _Q} = some_other_func(X),
    io:format("_Q = ~p~n", [_Q]),
    P.
```

The `io:format` line can be commented out and the compiler will not complain that `_Q` is unused — whereas a plain `Q` would trigger a warning.

# Relationships

## Builds Upon
- This builds on pattern matching.

## Enables
- This concept does not have downstream cards in scope.

## Related
- No directly related concept in scope.

## Contrasts With
- **Anonymous variable** — The lone `_` matches anything and never binds; `_Var` is a real variable that binds and can cause repeated-variable match failures.

# Common Errors

- **Error**: Using `_Var` as a "don't care" pattern and accidentally repeating it.
  **Correction**: A repeated `_Var` still binds and constrains the match; use the anonymous `_` for genuine don't-care positions.

# Common Confusions

- **Confusion**: Believing `_Var` behaves like the anonymous variable `_`.
  **Clarification**: `_Var` is a normal variable that binds; only the lone `_` is anonymous.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Underscore Variables".

# Verification Notes

- Definition source: Direct quotation and adaptation from *Underscore Variables*.
- Confidence rationale: HIGH — the source explicitly explains the construct, its warning behavior, and its pitfalls.
- Uncertainties: None.
- Cross-reference status: Slug `pattern-matching` assumed canonical; `anonymous-variable` exists.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
