---
# === CORE IDENTIFICATION ===
concept: String Prefix in Patterns
slug: string-prefix-in-patterns

# === CLASSIFICATION ===
category: functions-pattern-matching
subcategory: patterns
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "String Prefix in Patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "string prefix matching"
  - "++ in patterns"
  - "literal string prefix pattern"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - pattern-matching
  - string
extends: []
related:
  - list-operations
  - compound-pattern-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I match a string with a known prefix in a pattern?"
  - "What does \"prefix\" ++ Str mean as a pattern?"
  - "Why is ++ allowed on the left-hand side of a clause?"
---

# Quick Definition

A string literal followed by `++` and a variable is a valid pattern that matches any list (string) starting with that literal prefix, binding the remainder to the variable. It is syntactic sugar for an explicit cons pattern over character codes.

# Core Definition

When matching strings, `f("prefix" ++ Str) -> ...` is a valid pattern (Reference Manual, "Expressions" > "String Prefix in Patterns"). It is syntactic sugar for the equivalent but harder-to-read form `f([$p,$r,$e,$f,$i,$x | Str]) -> ...`. The literal prefix is expanded by the compiler into a sequence of character-code cons cells, with the trailing variable bound to whatever remains of the list.

# Prerequisites

- **pattern-matching** — the matching mechanism this builds on
- **string** — Erlang strings are lists of character codes, which is what makes the desugaring work

# Key Properties

1. Only a *literal* string may appear on the left of `++` in this pattern form.
2. The trailing operand must be a variable (or further pattern) bound to the suffix.
3. It desugars to a cons pattern over the prefix's character codes.
4. It works because Erlang strings are lists of integer code points.
5. It improves readability versus writing the explicit `[$p, $r, ... | Rest]` form.

# Construction / Recognition

## To Apply:
1. Write the known prefix as a string literal.
2. Append `++ Var` to capture the remainder.
3. Use it directly in a function head or `case` clause.

## To Recognize:
1. A double-quoted literal immediately followed by `++` on the pattern side.
2. A function head like `f("GET " ++ Rest) -> ...`.

# Context & Application

- **Typical contexts**: parsing textual protocols and command strings where a fixed keyword prefix selects a clause.
- **Common applications**: dispatching on `"prefix" ++ Str`; routing request lines.
- **Note**: for large-scale text processing, binaries and the bit syntax are usually preferred over character-list strings for performance.

# Examples

**Example 1** (Reference Manual, "String Prefix in Patterns"):

```erlang
f("prefix" ++ Str) -> ...
```

is syntactic sugar for the equivalent, harder-to-read:

```erlang
f([$p,$r,$e,$f,$i,$x | Str]) -> ...
```

# Relationships

## Builds Upon
- **pattern-matching** — the underlying mechanism
- **string** — list-of-codes representation enabling the sugar

## Related
- **list-operations** — `++` is the list-append operator this form reuses syntactically
- **compound-pattern-operator** — another pattern-side construct

## Contrasts With
(none)

# Common Errors

- **Error**: Using a variable or non-literal on the left of `++` in a pattern (e.g. `Prefix ++ Str` where `Prefix` is a variable).
  **Correction**: Only a literal string prefix is allowed on the pattern side; a variable prefix is not a valid pattern.

- **Error**: Expecting this to work efficiently on binaries.
  **Correction**: This sugar applies to list strings; for binaries use bit-syntax matching (`<<"prefix", Rest/binary>>`).

# Common Confusions

- **Confusion**: Believing `++` in a pattern performs list append at match time.
  **Clarification**: It is purely syntactic sugar expanded at compile time into a cons pattern; no append happens.

- **Confusion**: Thinking the prefix can be a computed value.
  **Clarification**: It must be a literal string.

# Source Reference

Chapter "Expressions", section "Patterns" > subsection "String Prefix in Patterns" (Erlang Reference Manual), including the `"prefix" ++ Str` desugaring example.

# Verification Notes

- Definition source: Direct adaptation of the section and its desugaring example.
- Confidence rationale: HIGH — short, explicit rule with a worked desugaring.
- Uncertainties: None.
- Cross-reference status: All referenced slugs verified (`pattern-matching`, `string`, `list-operations`, `compound-pattern-operator`).
- Re-extraction notes: New card filling a documented gap (was referenced by `patterns-in-expressions`).
