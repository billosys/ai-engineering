---
# === CORE IDENTIFICATION ===
concept: Pattern Matching
slug: pattern-matching

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: pattern-matching
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.4.3 Pattern matching: assignment on steroids"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - match operator
  - pattern
  - badmatch
  - "= operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - single-assignment
  - erlang-term
extends: []
related:
  - function-clause-selection
  - anonymous-variable
  - tuple
  - list
  - string
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is pattern matching in Erlang?"
  - "What does the = operator really do?"
  - "What can and cannot appear in a pattern?"
  - "How do you match a string prefix?"
---

# Quick Definition

Pattern matching tests a value against a pattern, binding any variables in the pattern to corresponding parts of the value. The `=` operator is a match operator, not plain assignment.

# Core Definition

Pattern matching "serves the following important purposes: choosing control flow branches, performing variable assignments (bindings), and decomposing data structures" (Chapter 2, section 2.4.3). The `=` operator "does *pattern matching*, rather than assignment. On the left side, you have a *pattern*; and on the right side, you have a plain old expression." The right side is evaluated to a value, which is matched against the pattern. If it does not match (`17 = 42`), the match fails and throws an exception with reason code `badmatch`. If it matches, any variables in the pattern are bound to the corresponding parts of the value. Patterns "can only contain variables, constants, and constant data structures like lists and tuples — no operators, function calls, funs" — except `++`, which may be used in a pattern if its left argument is a constant string (enabling string-prefix matching). A variable may occur several times in a pattern, requiring those fields to be equal.

# Prerequisites

- **Single assignment** — matching binds single-assignment variables.
- **Erlang term** — patterns match against term values.

# Key Properties

1. The `=` operator performs pattern matching, not plain assignment.
2. The right-side expression is evaluated, then matched against the left-side pattern.
3. A failed match throws an exception with reason code `badmatch`.
4. A successful match binds the pattern's variables to corresponding parts of the value.
5. Patterns may contain only variables, constants, and constant data structures — no operators or calls.
6. The `++` operator is the one exception, allowed in a pattern if its left argument is a constant string.
7. A variable appearing more than once in a pattern requires those fields to be equal.

# Construction / Recognition

## To Construct/Create:
1. Write a pattern on the left of `=`, an expression on the right.
2. Use variables for parts to capture, constants/`_` for parts to assert or ignore.
3. For string prefixes, use `"prefix" ++ Rest = SomeString`.

# Context & Application

- **Typical contexts**: Assignment, control-flow selection, data decomposition.
- **Common applications**: Extracting fields from tuples and lists; selecting function clauses; matching string prefixes (so regular expressions are rarely needed).
- **Historical/stylistic notes**: Seasoned Erlang programmers do as much as possible through pattern matching rather than equality operators.

# Examples

**Example 1** (section 2.4.3): `{A, B, C} = {1970, "Richard", male}` binds `A` to `1970`, `B` to `"Richard"`, `C` to `male`; `{point, X, X} = {point, 1, 2}` fails because `X` cannot be both 1 and 2.

**Example 2** (section 2.4.4): `"http://" ++ Rest = "http://www.erlang.org"` matches a string prefix, binding `Rest` to `"www.erlang.org"`.

# Relationships

## Builds Upon
- **Single assignment** — matching binds variables once.
- **Erlang term** — patterns describe the shape of terms.

## Enables
- **Function clause selection** — clauses are chosen by matching argument patterns.
- Data-structure decomposition.

## Related
- **Anonymous variable** — `_` is a don't-care placeholder in patterns.
- **Tuple**, **list**, **string** — common things matched and decomposed.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Putting an operator or function call in a pattern.
  **Correction**: Patterns allow only variables, constants, and constant data structures — plus `++` with a constant-string left argument.

- **Error**: Expecting `X = 101` to overwrite an already-bound `X`.
  **Correction**: `=` is a match; if `X` is bound, the right side must equal it or the match throws `badmatch`.

# Common Confusions

- **Confusion**: Believing `=` is ordinary assignment.
  **Clarification**: `=` is a match operator; it matches a value against a pattern and binds the pattern's variables.

# Source Reference

Chapter 2: Erlang language essentials, section 2.4.3 "Pattern matching: assignment on steroids" and section 2.4.4 "More about patterns."

# Verification Notes

- Definition source: Direct adaptation from sections 2.4.3 and 2.4.4.
- Confidence rationale: HIGH — pattern matching, the match operator, and pattern restrictions are explicitly defined.
- Uncertainties: None.
- Cross-reference status: `anonymous-variable` is a planned card in this source.
- Re-extraction notes: Fresh extraction; no prior card.
