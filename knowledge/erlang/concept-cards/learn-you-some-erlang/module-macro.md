---
concept: MODULE Macro
slug: module-macro
category: functions-pattern-matching
subcategory: code-organization
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "More on Multiprocessing"
chapter_number: 11
pdf_page: null
section: "We Love Messages, But We Keep Them Secret"
extraction_confidence: high
aliases:
  - "?MODULE"
  - "MODULE macro"
prerequisites: []
extends: []
related:
  - process-state-loop
  - hot-code-loading
contrasts_with: []
answers_questions:
  - "What is the ?MODULE macro?"
  - "Why use ?MODULE in spawn and start functions?"
---

# MODULE Macro

## Quick Definition

`?MODULE` is a compile-time macro that expands to the current module's name as an atom. It is used to avoid hard-coding the module name in `spawn/3`, `register/2`, and fully qualified calls.

## Core Definition

When introducing the fridge's `start/1` function, the chapter writes `spawn(?MODULE, fridge2, [FoodList])` and explains: "`?MODULE` is a macro that returns the current module's name." Using it instead of a literal atom keeps the code correct if the module is renamed and centralizes the dependency. The same macro appears throughout the later chapters: in `register(?MODULE, ...)` for naming a server after its module, and in fully qualified calls like `?MODULE:loop(S)` used for hot code loading (Hébert, ch. 11, "We Love Messages, But We Keep Them Secret"; reused in ch. 13).

## Prerequisites

This is a foundational language-tooling concept with no prerequisites within these chapters.

## Key Properties

1. `?MODULE` is a macro expanded at compile time
2. It expands to the current module's name as an atom
3. Used in `spawn/3` and `spawn_link/3` to name the module without hard-coding it
4. Used in `register(?MODULE, Pid)` to register a server under its own module name
5. Used in fully qualified calls (`?MODULE:loop(S)`) for hot code loading
6. Keeps code correct and centralized if the module is renamed

## Construction / Recognition

## To Use the MODULE Macro

1. Write `spawn(?MODULE, Function, Args)` instead of `spawn(literal_name, ...)`
2. Use `register(?MODULE, Pid)` to name a process after its module
3. Use `?MODULE:Function(Args)` for a fully qualified call (e.g. to pick up new code)

## Examples

> **In a start function** (ch. 11): `start(FoodList) -> spawn(?MODULE, fridge2, [FoodList]).`
>
> **In registration** (ch. 13): `register(?MODULE, Pid=spawn(?MODULE, init, []))`.
>
> **In a hot-code-loading call** (ch. 13): the `code_change` clause runs `?MODULE:loop(S)`.

## Relationships

## Related

- **Process state loop** — `?MODULE` is used in the `start`/`spawn` functions that front the loop
- **Hot code loading** — `?MODULE:Function` fully qualified calls let a process adopt new code

## Common Errors

- **Error**: Hard-coding the module name in `spawn/3` or `register/2`
  **Correction**: Use `?MODULE` so a rename does not break the code

## Common Confusions

- **Confusion**: Thinking `?MODULE` is resolved at runtime
  **Clarification**: It is a macro expanded at compile time to the module's name atom

## Source Reference

Chapter 11, "More on Multiprocessing," section "We Love Messages, But We Keep Them Secret"; reused in Chapter 13.

## Verification Notes

- Definition: directly from ch. 11
- Confidence: HIGH — explicitly described and used repeatedly
