---
# === CORE IDENTIFICATION ===
concept: Conditional Compilation
slug: conditional-compilation

# === CLASSIFICATION ===
category: tooling
subcategory: compilation
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "The Rest of Sequential Erlang"
chapter_number: 8
pdf_page: null
section: "Control Flow in Macros"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "-ifdef"
  - "-ifndef"
  - "-undef"
  - macro control flow

# === TYPED RELATIONSHIPS ===
prerequisites:
  - macro
extends:
  - macro
related:
  - erlang-preprocessor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I conditionally compile Erlang code?"
  - "What directives control macro expansion?"
  - "How do I define a debug macro that compiles away in production?"
---

# Quick Definition

Conditional compilation uses the preprocessor directives `-undef`, `-ifdef`, `-ifndef`, `-else`, and `-endif` to control which macro definitions and code take effect based on whether a macro is defined.

# Core Definition

Inside a module, directives control macro expansion ("The Rest of Sequential Erlang", *Control Flow in Macros*): `-undef(Macro).` undefines a macro so it can no longer be called; `-ifdef(Macro).` evaluates the following lines only if `Macro` has been defined; `-ifndef(Macro).` evaluates them only if `Macro` is undefined; `-else.` is allowed after an `ifdef`/`ifndef` and applies when the condition was false; `-endif.` marks the end of an `ifdef`/`ifndef`. "Conditional macros must be properly nested." A macro can be set at compile time via an extra argument to `c/2` — e.g. `c(m1, {d, debug_flag})` defines `debug_flag`.

# Prerequisites

- **Macro** — Conditional compilation controls which macro definitions and code blocks are used.

# Key Properties

1. `-undef(Macro)` undefines a macro.
2. `-ifdef(Macro)` includes the following lines only if `Macro` is defined.
3. `-ifndef(Macro)` includes them only if `Macro` is undefined.
4. `-else` provides the alternative branch after `ifdef`/`ifndef`.
5. `-endif` closes an `ifdef`/`ifndef` block.
6. Conditional directives must be properly nested.
7. A macro flag can be set at compile time with `c(Mod, {d, FlagName})`.

# Construction / Recognition

## To Construct/Create:
1. Bracket alternative `-define`s: `-ifdef(debug_flag). -define(...). -else. -define(...). -endif.`
2. Compile with the flag set: `c(m1, {d, debug_flag})`.

## To Identify/Recognize:
1. The `-ifdef`/`-ifndef`/`-else`/`-endif` directives mark conditionally compiled regions.

# Context & Application

- **Typical contexts**: enabling debug instrumentation only in debug builds.
- **Common applications**: a `DEBUG` macro that prints when `debug_flag` is set and expands to the atom `void` otherwise.
- **Historical/stylistic notes**: `void` as the no-op replacement is just a reminder that nobody is interested in the macro's value.

# Examples

**Example 1** (*Control Flow in Macros*): a flag-controlled debug macro:

```erlang
-ifdef(debug_flag).
-define(DEBUG(X), io:format("DEBUG ~p:~p ~p~n",[?MODULE, ?LINE, X])).
-else.
-define(DEBUG(X), void).
-endif.

loop(0) -> done;
loop(N) ->
    ?DEBUG(N),
    loop(N-1).
```

Compiled with `c(m1, {d, debug_flag})`, `?DEBUG(N)` prints; otherwise it expands to `void`.

# Relationships

## Builds Upon
- **Macro** — Conditional compilation elaborates the macro system.

## Enables
- This concept does not have downstream cards in scope.

## Related
- **Erlang preprocessor** — These directives are processed by the preprocessor.

## Contrasts With
- No directly contrasting concept in scope.

# Common Errors

- **Error**: Forgetting an `-endif` to close an `-ifdef` block.
  **Correction**: Conditional directives must be properly nested; every `-ifdef`/`-ifndef` needs a matching `-endif`.

- **Error**: Expecting a macro to be defined without setting its flag at compile time.
  **Correction**: Pass `{d, FlagName}` to `c/2` (or the compiler) to define the flag.

# Common Confusions

- **Confusion**: Thinking `-else` can stand alone.
  **Clarification**: `-else` is only valid after an `-ifdef` or `-ifndef` and before the matching `-endif`.

# Source Reference

Chapter 8: "The Rest of Sequential Erlang", section "Macros" (subsection "Control Flow in Macros").

# Verification Notes

- Definition source: Direct adaptation of the *Control Flow in Macros* subsection.
- Confidence rationale: HIGH — the source explicitly defines each directive and gives a worked debug-macro example.
- Uncertainties: None.
- Cross-reference status: Slug `macro` extracted in this chapter; `erlang-preprocessor` extracted in this chapter.
- Re-extraction notes: Fresh extraction; no prior card existed for this slug.
