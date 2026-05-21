---
# === CORE IDENTIFICATION ===
concept: Try After Clause
slug: try-after-clause

# === CLASSIFICATION ===
category: error-handling
subcategory: exception-handling
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Expressions"
chapter_number: null
pdf_page: null
section: "Try"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "after clause"
  - "try-after"
  - "finally clause"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - try-expression
extends:
  - try-expression
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I ensure cleanup code runs regardless of exceptions?"
  - "What is the after clause in a try expression?"
---

# Quick Definition

The `after` clause in a `try` expression guarantees that cleanup code executes regardless of whether the protected expression succeeds or raises an exception. Its return value is discarded.

# Core Definition

The `after` section of a `try` expression is intended for cleanup with side effects. `AfterBody` is evaluated after either `Body` or `ExceptionBody`, no matter which one. The evaluated value of `AfterBody` is lost; the return value of the `try` expression is the same with an `after` section as without. Even if an exception occurs during evaluation of `Body` or `ExceptionBody`, `AfterBody` is evaluated, and the original exception is then re-raised. If an exception occurs during evaluation of `AfterBody` itself, it masks any prior exception. The `after` section can be used with or without a `catch` section (Erlang Reference Manual, "Try" section).

# Prerequisites

- **try-expression** — The `after` clause is a component of the `try` expression.

# Key Properties

1. `AfterBody` always executes after `Body` or `ExceptionBody`.
2. The return value of `AfterBody` is discarded.
3. If `Body` or `ExceptionBody` raises an exception, `AfterBody` still executes, and the exception propagates after.
4. An exception in `AfterBody` masks any prior exception.
5. `try Exprs after AfterBody end` is valid (no `of` or `catch` needed).
6. Variables bound in the `after` section are unsafe after the whole `try` construct.

# Construction / Recognition

## To Construct:
1. Add `after` before `end` in a `try` expression.
2. Place cleanup expressions in the `after` body.

## To Recognize:
1. Look for the `after` keyword within a `try...end` block.

# Context & Application

The `after` clause is used for resource cleanup — closing files, releasing locks, cleaning up ETS tables, etc. It is analogous to `finally` in Java or Python. The most common pattern is `try Exprs after cleanup() end` where cleanup must happen regardless of success or failure.

# Examples

**Example 1** (Try section): File cleanup:

```erlang
termize_file(Name) ->
    {ok,F} = file:open(Name, [read,binary]),
    try
        {ok,Bin} = file:read(F, 1024*1024),
        binary_to_term(Bin)
    after
        file:close(F)
    end.
```

# Relationships

## Builds Upon
- **try-expression** — The `after` clause is part of the `try` expression.

## Enables
- No directly dependent concepts.

## Related
- No additional related concepts.

## Contrasts With
- No direct contrasts within this source.

# Common Errors

- **Error**: Relying on the return value of the `after` body.
  **Correction**: The `after` body's return value is always discarded. Return values must come from `Body` or `ExceptionBody`.

- **Error**: Raising an exception in `AfterBody` that masks the original exception.
  **Correction**: Keep `AfterBody` as simple as possible to avoid masking exceptions. Handle errors in cleanup code defensively.

# Common Confusions

- **Confusion**: Thinking `after` catches exceptions.
  **Clarification**: `after` does not catch exceptions; it merely guarantees execution. Exceptions still propagate after `AfterBody` completes.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Try" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — explicit semantics and examples provided
- Uncertainties: None
- Cross-reference status: Prerequisites verified
