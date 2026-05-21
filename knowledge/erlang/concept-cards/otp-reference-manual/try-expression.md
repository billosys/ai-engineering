---
# === CORE IDENTIFICATION ===
concept: Try Expression
slug: try-expression

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
  - "try-catch"
  - "try-of-catch"
  - "try-catch-after"
  - "try expression"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - catch-expression
  - exception-classes
extends:
  - catch-expression
related:
  - try-after-clause
  - try-stacktrace
  - guard-sequences
contrasts_with:
  - catch-expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use the try-catch expression for error handling?"
  - "How do I distinguish between exception classes in Erlang?"
  - "What is the difference between try-catch and try-of-catch?"
---

# Quick Definition

The `try` expression evaluates expressions and catches exceptions with the ability to distinguish between exception classes (`error`, `exit`, `throw`). It optionally includes `of` clauses for pattern matching the success value and `after` clauses for cleanup.

# Core Definition

The `try` expression is an enhancement of `catch` that can distinguish between different exception classes, choose to handle only desired ones, and pass others on to an enclosing handler. The basic form `try Exprs catch Class:ExceptionPattern[:Stacktrace] [when Guard] -> Body end` returns the value of `Exprs` unless an exception occurs, in which case matching `ExceptionPattern` with the right `Class` is attempted sequentially. If no matching clause is found, the exception propagates. The `of` section matches the success value like a `case` expression (but raises `try_clause` instead of `case_clause` on failure). An omitted `Class` defaults to `throw`. The `of`, `catch`, and `after` sections are all optional, as long as at least `catch` or `after` is present (Erlang Reference Manual, "Try" section).

# Prerequisites

- **catch-expression** — Understanding the simpler `catch` mechanism helps motivate why `try` exists.
- **exception-classes** — Must understand `error`, `exit`, and `throw` classes to use `try` effectively.

# Key Properties

1. Can distinguish between `error`, `exit`, and `throw` exception classes.
2. `Class:ExceptionPattern[:Stacktrace]` — matches class, pattern, and optionally binds stacktrace.
3. Omitting `Class` defaults to `throw`.
4. The `of` section matches the success value (like `case`, but raises `try_clause` on failure).
5. Only exceptions from `Exprs` are caught; exceptions in `Body` or `of` bodies are not caught.
6. The `after` section always executes (cleanup), but its return value is discarded.
7. `of`, `catch`, and `after` are all optional (need at least `catch` or `after`).
8. Variables bound after `try` are unsafe in `catch`, `after`, and after the whole construct.

# Construction / Recognition

## To Construct:
1. Basic: `try Exprs catch Class:Pattern -> Body end`.
2. With of: `try Exprs of Pattern -> Body catch Class:Pattern -> ExcBody end`.
3. With after: `try Exprs after CleanupBody end`.
4. Full form: `try Exprs of ... catch ... after ... end`.

## To Recognize:
1. Look for the `try ... end` block structure.
2. May contain `of`, `catch`, and/or `after` sections.

# Context & Application

`try` is the standard mechanism for error handling in Erlang. It enables structured exception handling where different exception classes can be handled separately. The `of` section is useful when you want to match the success result and protect only the evaluation phase. The `after` section provides resource cleanup guarantees similar to `finally` in other languages.

# Examples

**Example 1** (Try section): Emulating `catch Expr` with `try`:

```erlang
try Expr
catch
    throw:Term -> Term;
    exit:Reason -> {'EXIT',Reason};
    error:Reason:Stk -> {'EXIT',{Reason,Stk}}
end
```

**Example 2** (Try section): Resource cleanup with `after`:

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

**Example 3** (Try section): Valid forms with minimal sections:

```erlang
try Exprs after AfterBody end

try Exprs
catch
    ExceptionPattern ->
        ExceptionBody
after
    AfterBody
end
```

# Relationships

## Builds Upon
- **catch-expression** — `try` is an enhancement of the simpler `catch` expression.
- **exception-classes** — `try` explicitly matches exception classes.

## Enables
- **try-after-clause** — The `after` clause provides cleanup semantics.
- **try-stacktrace** — Stacktrace binding is a feature of `try`.

## Related
- **guard-sequences** — Guards can be used in both `of` and `catch` clauses.

## Contrasts With
- **catch-expression** — `catch` cannot distinguish exception classes; `try` can.

# Common Errors

- **Error**: Expecting exceptions in the `of` body to be caught by the `catch` section.
  **Correction**: Only exceptions from the `Exprs` (between `try` and `of`/`catch`) are caught. Exceptions in `Body` propagate.

- **Error**: Using variables bound in `Exprs` inside the `catch` or `after` sections.
  **Correction**: Variables bound in `Exprs` are unsafe in `catch` and `after` sections.

# Common Confusions

- **Confusion**: Thinking omitting `Class` in catch clause means "catch all classes."
  **Clarification**: Omitting `Class` defaults to `throw`, not to all classes. To catch all classes, use explicit `error:`, `exit:`, and `throw:` patterns.

- **Confusion**: Believing the `after` section's return value is the return value of the `try`.
  **Clarification**: The `after` section's value is discarded. The `try` returns the value from `Body` or `ExceptionBody`.

# Source Reference

Erlang Reference Manual, "Expressions" chapter, "Try" section.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: High — comprehensive syntax forms, scoping rules, and examples
- Uncertainties: None
- Cross-reference status: Contrasts with catch-expression verified
