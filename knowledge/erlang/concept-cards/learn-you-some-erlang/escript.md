---
concept: escript
slug: escript
category: functions-pattern-matching
subcategory: tooling
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Functionally Solving Problems"
chapter_number: 8
pdf_page: null
section: "Heathrow to London"
extraction_confidence: medium
aliases:
  - "escript"
  - "Erlang scripting"
prerequisites: []
extends: []
related:
  - functional-problem-solving-approach
contrasts_with: []
answers_questions:
  - "How do I run an Erlang program outside the shell?"
  - "What is escript?"
---

# escript

## Quick Definition

`escript` is the Erlang command for running Erlang programs as scripts without starting the `erl` shell or compiling first. The script's `main/1` function is called automatically with the command-line arguments.

## Core Definition

The chapter shows two ways to run a program outside the Erlang shell. One is a `main/1` function plus `erlang:halt/0` and `io:format/2`, started via `erl -noshell -run`. The other is `escript`: "the Erlang `escript` command provides a simple way to run Erlang programs without starting the `erl` application directly. Basically, the command takes a module and allows you to interpret it without needing to compile it first." An escript file replaces the `-module` attribute with a script header (`#!/usr/bin/env escript`); its `main/1` "will automatically be called when you start the script." Adding `-mode(compile).` compiles the code instead of interpreting it (interpretation is slower) (Hébert, ch. 8, "Running the Program Without the Erlang Shell," "Using escript" sidebar).

## Prerequisites

This is a tooling concept with no conceptual prerequisites within this chapter.

## Key Properties

1. Runs an Erlang program as a script without the `erl` shell
2. Does not require compiling the module first — it interprets it
3. The script file uses a header (`#!/usr/bin/env escript`) instead of `-module`
4. `main/1` is called automatically with the command-line arguments
5. Adding `-mode(compile).` compiles rather than interprets (faster)
6. An alternative to escript is `erl -noshell -run Module Function Args`

## Construction / Recognition

## To Write an escript

1. Start the file with `#!/usr/bin/env escript` and an `%% -*- erlang -*-` line
2. Omit the `-module` attribute
3. Define `main([Args]) -> ...` to receive command-line arguments
4. Run it as `./script-name.erl` or `escript script-name.erl`
5. Add `-mode(compile).` to compile instead of interpret for speed

## Examples

> **escript header** (ch. 8): `#!/usr/bin/env escript` followed by `%% -*- erlang -*-` and `main([StringArguments]) -> ...`.
>
> **Non-escript alternative** (ch. 8): `erl -noshell -run road main road.txt` runs a compiled module's `main/1` from the command line.

## Relationships

## Related

- **Functional problem-solving approach** — The Heathrow example is the program made runnable via escript

## Common Errors

- **Error**: Keeping the `-module` attribute in an escript file
  **Correction**: An escript uses a script header instead of `-module`

## Common Confusions

- **Confusion**: Thinking escript always compiles the code
  **Clarification**: escript interprets by default (slower); add `-mode(compile).` to compile

## Source Reference

Chapter 8, "Functionally Solving Problems," section "Heathrow to London," subsection "Running the Program Without the Erlang Shell" and the "Using escript" sidebar.

## Verification Notes

- Definition and header: directly from the ch. 8 sidebar
- Confidence: MEDIUM — described in a sidebar with a partial example, no full worked script
