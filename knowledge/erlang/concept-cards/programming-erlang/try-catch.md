---
# === CORE IDENTIFICATION ===
concept: try...catch Expression
slug: try-catch

# === CLASSIFICATION ===
category: error-handling
subcategory: exceptions
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Error Handling in Sequential Programs"
chapter_number: 6
pdf_page: null
section: "Trapping an Exception with try...catch"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "try ... catch"
  - "try ... of ... catch ... after ... end"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - exception
  - error-class
  - pattern-matching
extends: []
related:
  - catch-expression
  - case-expression
  - throw-exit-error
contrasts_with:
  - catch-expression

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I trap an exception with try...catch?"
  - "What does the after section of try...catch do?"
  - "How is try...catch like a case expression?"
---

# Quick Definition

`try...catch` is an expression that evaluates a body, dispatches a normal result via `of` patterns and any exception via `catch` patterns, and optionally runs cleanup code in an `after` section.

# Core Definition

The Erlang `try...catch` expression has the form `try FuncOrExpressionSeq of Pattern -> Expressions; ... catch ExceptionType:ExPattern -> ExExpressions; ... after AfterExpressions end`. It works as follows ("Error Handling in Sequential Programs", *Trapping an Exception with try...catch*): first `FuncOrExpressionSeq` is evaluated. If it finishes without an exception, its return value is pattern matched against the `of` patterns. If an exception is raised, the `catch` patterns are matched to decide which expressions to run. `ExceptionType` is an atom — one of `throw`, `exit`, or `error` — telling how the exception was generated; if omitted it defaults to `throw`. "Everything in Erlang is an expression, and all expressions have values" — so `try...end` itself has a value. The book describes it as "a `case` expression on steroids."

# Prerequisites

- **Exception** — `try...catch` exists to trap exceptions.
- **Error class** — The `catch` patterns are tagged with an exception class (`throw`/`exit`/`error`).
- **Pattern matching** — Both the `of` and `catch` clauses select expressions via pattern matching.

# Key Properties

1. The whole `try...end` form is an expression with a value.
2. The `of` section pattern matches a successful return value.
3. The `catch` section pattern matches a raised exception, tagged `Class:Pattern`.
4. If the class tag is omitted in a `catch` clause, it defaults to `throw`.
5. The `after` section runs cleanup code that is guaranteed to execute whether or not an exception was raised; its return value is lost.
6. The `of` section and the `after` section can both be omitted.
7. Internal runtime errors always carry the class `error`.

# Construction / Recognition

## To Construct/Create:
1. Write `try Expr of Pattern -> ... catch Class:ExPattern -> ... after Cleanup end`.
2. Omit `of` for the shortcut form: `try F catch ... end` behaves like `try F of Val -> Val catch ... end`.
3. Omit `after` when no cleanup is needed.

## To Identify/Recognize:
1. A `catch` clause written `_:_ -> ...` catches every possible exception (any class, any value).
2. A `catch` clause written `_ -> ...` (no class tag) only catches `throw` exceptions, since the tag defaults to `throw`.

# Context & Application

- **Typical contexts**: code where errors are possible but rare, where the caller wants to handle specific `throw` exceptions.
- **Common applications**: wrapping a call that may raise any of the three exception classes and distinguishing them.
- **Historical/stylistic notes**: similar to Java `try/catch/finally` and Ruby `begin/rescue/ensure`.

# Examples

**Example 1** (*Programming Idioms with try...catch*): a wrapper distinguishing all exception classes:

```erlang
catcher(N) ->
    try generate_exception(N) of
        Val -> {N, normal, Val}
    catch
        throw:X -> {N, caught, thrown, X};
        exit:X  -> {N, caught, exited, X};
        error:X -> {N, caught, error, X}
    end.
```

Running `demo1()` over `[1,2,3,4,5]` yields `[{1,normal,a},{2,caught,thrown,a},{3,caught,exited,a},{4,normal,{'EXIT',a}},{5,caught,error,a}]`.

**Example 2** (*Catching Every Possible Exception*): the catch-all idiom:

```erlang
try Expr
catch
    _:_ -> %% Code to handle all exceptions
end
```

# Relationships

## Builds Upon
- This builds on exceptions and pattern matching rather than on a single parent card.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **case expression** — `try...catch` is described as a `case` expression with `catch` and `after` blocks added.
- **throw/exit/error** — The BIFs whose exceptions `try...catch` traps.

## Contrasts With
- **catch expression** — The older `catch` primitive converts an exception into an `{'EXIT', ...}` tuple and gives a detailed stack trace, but cannot dispatch on class or run an `after` block.

# Common Errors

- **Error**: Writing a `catch _ -> ...` clause expecting it to catch all exceptions.
  **Correction**: Omitting the class tag defaults it to `throw`; use `_:_ -> ...` to catch every class.

- **Error**: Relying on the `after` section's return value.
  **Correction**: The return value of the `after` expressions is discarded; use it only for side-effecting cleanup.

# Common Confusions

- **Confusion**: Believing `try...catch` and the bare `catch` primitive are the same construct.
  **Clarification**: They are different — `catch` predates `try...catch`; `try...catch` adds class dispatch, `of`, and `after`.

- **Confusion**: Thinking the `after` block only runs on success or only on failure.
  **Clarification**: The `after` block is guaranteed to run in both cases.

# Source Reference

Chapter 6: "Error Handling in Sequential Programs", sections "Trapping an Exception with try...catch", "try...catch Has a Value", "Shortcuts", "Programming Idioms with try...catch", "Catching Every Possible Exception".

# Verification Notes

- Definition source: Direct adaptation of *Trapping an Exception with try...catch* and the surrounding idiom sections.
- Confidence rationale: HIGH — the source fully specifies the syntax, semantics, and shortcuts with worked examples.
- Uncertainties: None.
- Cross-reference status: Slugs `exception`, `error-class`, `catch-expression`, `throw-exit-error` extracted in this chapter; `pattern-matching` assumed canonical; `case-expression` exists.
- Re-extraction notes: Fresh extraction; overwrote prior card of the same slug.
