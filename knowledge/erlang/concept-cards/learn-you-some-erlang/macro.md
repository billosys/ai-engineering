---
concept: Macro
slug: macro
category: tooling
subcategory: code-organization
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Modules"
chapter_number: 2
pdf_page: null
section: "Defining Macros"
extraction_confidence: high
aliases:
  - "-define"
  - "preprocessor macro"
prerequisites:
  - module-attribute
extends: []
related:
  - compiler-options
contrasts_with: []
answers_questions:
  - "What is a module?"
---

# Macro

## Quick Definition

An Erlang macro is a text expression, defined with `-define`, that is substituted into code before compilation. Macros are used for short functions and named constants.

## Core Definition

Erlang macros are similar to C's `#define` statements and are mainly used to define short functions and constants. They are simple expressions represented by text that is replaced before the code is compiled for the VM. A macro is declared as a module attribute, `-define(MACRO, some_value).`, and used as `?MACRO` inside any function in the module; "function" macros take arguments, e.g., `-define(sub(X,Y), X-Y).`. Predefined macros include `?MODULE`, `?FILE`, and `?LINE`. Conditional definition uses `-ifdef(MACRO).`, `-else.`, and `-endif.` (Hébert, ch. 2, "Defining Macros").

## Prerequisites

- **Module attribute** — Macros are declared via the `-define` attribute

## Key Properties

1. Declared with `-define(Name, Value).` and used as `?Name`.
2. Substituted textually before compilation.
3. Avoid "magic values" — `?HOUR` is clearer than `3600`.
4. "Function" macros accept arguments: `-define(sub(X,Y), X-Y).`.
5. Predefined macros: `?MODULE` (module name atom), `?FILE` (filename string), `?LINE` (line number).
6. `-ifdef`, `-else`, `-endif` allow conditional macro definitions.

## Construction / Recognition

To define and use a macro:

1. Add `-define(NAME, value).` as a module attribute.
2. Reference it as `?NAME` inside any function.
3. The compiler replaces `?NAME` with the value before compiling.

## Context & Application

Macros avoid magic numbers and make code self-documenting; changing one definition updates every use. Conditional macros (`-ifdef`) are commonly combined with the `{d,Macro}` compiler flag to enable debug output or test functions only when wanted.

## Examples

**Example** (ch. 2): `-define(HOUR, 3600). % in seconds` names a constant; `?sub(23,47)` expands to `23-47`.

**Example** (ch. 2): The `-ifdef(DEBUGMODE)` block defines `?DEBUG(S)` to output text only when compiled with `DEBUGMODE` defined.

## Relationships

### Prerequisites

- **Module attribute** — `-define` is a module attribute

### Related

- **Compiler options** — The `{d,Macro}` flag defines macros for conditional compilation

## Common Errors

- **Error**: Forgetting the `?` prefix when using a macro
  **Correction**: Macros are invoked as `?NAME`, not `NAME`

## Common Confusions

- **Confusion**: Thinking macros are runtime functions
  **Clarification**: Macros are textually substituted before compilation, not called at runtime

## Source Reference

Chapter 2: "Modules," section "Defining Macros."

## Verification Notes

- Definition: Adapted from the "Defining Macros" section
- Confidence: HIGH — explicit section with examples
- Uncertainties: None
