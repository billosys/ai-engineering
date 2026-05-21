---
# === CORE IDENTIFICATION ===
concept: Binary Comprehension
slug: binary-comprehension

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: comprehensions
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Comprehensions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "bit string comprehension"
  - "binary comprehension expression"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bit-syntax-expressions
  - list-comprehension
extends:
  - list-comprehension
related:
  - map-comprehension
  - binary
  - bit-string
contrasts_with:
  - list-comprehension

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use binary comprehensions in Erlang?"
  - "How do I construct a binary from a list using a comprehension?"
  - "How do I iterate over bytes in a binary with a comprehension?"
---

# Quick Definition

A binary comprehension `<< BitStringExpr || Qualifier1, ..., QualifierN >>` constructs a bit string by concatenating the results of evaluating `BitStringExpr` for each combination of generator elements for which all filters are true.

# Core Definition

Binary comprehensions (bit string comprehensions) have the syntax `<< BitStringExpr || Qualifier1, ..., QualifierN >>` where `BitStringExpr` is an expression that evaluates to a bit string and each `Qualifier` is a generator or filter. If `BitStringExpr` is a function call, it must be enclosed in parentheses. The comprehension returns a bit string created by concatenating the results. All generator types (list, bit string, map, zip) and filter types work the same as in list comprehensions. When there are no generators, the result is the bit string from `BitStringExpr` if all filters are true, or `<<>>` otherwise (Erlang Reference Manual, "Comprehensions" section).

# Prerequisites

- **bit-syntax-expressions** — The output expression and bit string generators use bit syntax.
- **list-comprehension** — Binary comprehensions share the same qualifier syntax (generators, filters).

# Key Properties

1. Syntax: `<< BitStringExpr || Qualifier1, ..., QualifierN >>`.
2. `BitStringExpr` must evaluate to a bit string.
3. Function calls in `BitStringExpr` must be parenthesized.
4. Bit string generators use `<=` (relaxed) or `<:=` (strict).
5. Can mix generator types (list generators, bit string generators, map generators).
6. Result is a bit string formed by concatenating all results.

# Construction / Recognition

## To Construct:
```erlang
<< <<(X*2)>> || <<X>> <:= <<1,2,3>> >>
<< <<(X*2)>> || X <:- [1,2,3] >>
```

## To Recognize:
1. Look for `<< ... || ... >>` syntax.
2. The expression before `||` evaluates to a bit string.

# Context & Application

Binary comprehensions are used for transforming binaries byte-by-byte or bit-by-bit, converting between lists and binaries, and constructing binaries from computed values. They provide a declarative alternative to recursive binary processing functions.

# Examples

**Example 1** (Comprehensions section): Doubling bytes in a binary using a bit string generator:

```erlang
1> << <<(X*2)>> || <<X>> <:= <<1,2,3>> >>.
<<2,4,6>>
```

**Example 2** (Comprehensions section): Constructing a binary from a list generator:

```erlang
1> << <<(X*2)>> || X <:- [1,2,3] >>.
<<2,4,6>>
```

**Example 3** (Comprehensions section): Extracting bytes from a binary into a list:

```erlang
1> [X*2 || <<X>> <:= <<1,2,3>>].
[2,4,6]
```

# Relationships

## Builds Upon
- **bit-syntax-expressions** — Output and bit string generators use bit syntax.
- **list-comprehension** — Shares generator and filter syntax.

## Related
- **map-comprehension** — Another comprehension variant that constructs maps.
- **binary** — Binary comprehensions produce binaries/bit strings.

## Contrasts With
- **list-comprehension** — Uses `<< ... || ... >>` vs `[ ... || ... ]` and produces bit strings vs lists.

# Common Errors

- **Error**: Forgetting to parenthesize a function call in the bit string expression.
  **Correction**: Write `<< (f(X)) || ... >>` not `<< f(X) || ... >>`.

- **Error**: The bit string expression not evaluating to a bit string.
  **Correction**: Ensure the expression produces a bit string, typically by wrapping in `<< >>` like `<<(X*2)>>`.

# Common Confusions

- **Confusion**: Mixing up list generators and bit string generators in binary comprehensions.
  **Clarification**: Both are valid. A list generator (`<:-`) iterates a list; a bit string generator (`<:=`) iterates segments of a bit string. Either can be used as a source for a binary comprehension.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Comprehensions" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — clear syntax and examples from source
- Uncertainties: None
- Cross-reference status: Verified shared qualifier syntax with list-comprehension
