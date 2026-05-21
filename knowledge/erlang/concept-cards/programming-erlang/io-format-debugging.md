---
# === CORE IDENTIFICATION ===
concept: io:format Debugging
slug: io-format-debugging

# === CLASSIFICATION ===
category: production-ops
subcategory: debugging
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Profiling, Debugging, and Tracing"
chapter_number: 21
pdf_page: null
section: "Debugging Techniques"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "print-statement debugging"
  - "io:format/2 debugging"
  - "trace printing"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - runtime-stack-trace
  - erlang-debugger
  - process-tracing
contrasts_with:
  - erlang-debugger

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I debug an Erlang program with print statements?"
  - "How do I debug a concurrent Erlang program?"
  - "What is the simplest Erlang debugging technique?"
---

# Quick Definition

io:format debugging is the practice of adding `io:format(...)` print statements to a program to display the values of variables at critical points. It is the most common Erlang debugging technique.

# Core Definition

"By far the most common technique is to just add print statements to the incorrect programs" ("Debugging Techniques"). You "simply add `io:format(...)` statements to print the values of variables you are interested in at critical points in your program" ("io:format Debugging"). Debugging Erlang is relatively easy because single-assignment variables and the absence of pointers and mutable state mean that once a variable is observed to have a wrong value, it is easy to find when and where that happened. When debugging parallel programs, it is good practice to print messages immediately *before* sending a message and immediately *after* receiving one. The technique fails when the data structures of interest become very large — in that case they can be dumped to a file instead.

# Prerequisites

This is a foundational debugging technique within this chapter — it has no prerequisites among the concepts of these chapters.

# Key Properties

1. Implemented by inserting `io:format(...)` calls at points of interest.
2. The most common Erlang debugging technique.
3. Effective because single-assignment variables make tracking a wrong value easy.
4. For concurrent code, print before sending and after receiving messages.
5. Fails for very large data structures — dump to a file instead.
6. Commonly paired with a catch-all `receive` clause that warns on unexpected messages.
7. A `NYI` (not yet implemented) macro can print module/line and `exit(nyi)` for stub functions.

# Construction / Recognition

## To Debug with io:format:
1. Identify the variables and program points of interest.
2. Insert `io:format(Fmt, Args)` calls there.
3. For concurrent code, print before each send and after each receive.
4. Use `spawn_link` rather than `spawn` so abnormal exits are reported.
5. Add a catch-all `receive` clause that prints unexpected messages.
6. Remove the print statements once the bug is found.

## To Recognize:
1. Temporary `io:format` calls scattered through application code.
2. A `?NYI(...)` macro use marking an unimplemented function.

# Context & Application

io:format debugging is the everyday, no-setup debugging tool.

- **Typical contexts**: Quick investigation of any sequential or concurrent bug.
- **Common applications**: Printing variable values; tracing message flow in concurrent programs.
- **Historical/stylistic notes**: Armstrong always starts a concurrent program with a `receive` loop that warns on unexpected messages.

# Examples

**Example 1** ("io:format Debugging"): A starting `receive` loop that warns on unexpected messages.

```erlang
loop(...) ->
    receive
        Any ->
            io:format("*** warning unexpected message:~p~n",[Any]),
            loop(...)
    end.
```

**Example 2** ("io:format Debugging"): The `NYI` macro for stub functions.

```erlang
-define(NYI(X),(begin
    io:format("*** NYI ~p ~p ~p~n",[?MODULE, ?LINE, X]),
    exit(nyi)
    end)).

glurk(X, Y) ->
    ?NYI({glurk, X, Y}).
```

# Relationships

## Builds Upon
- (Foundational debugging technique within this chapter.)

## Enables
- (No card depends on this concept.)

## Related
- **Runtime stack trace** — Print statements complement crash traces.
- **Process tracing** — Tracing observes behavior without modifying code; print statements modify code.
- **Erlang debugger** — Another debugging option for when print statements are not enough.

## Contrasts With
- **Erlang debugger** — The debugger lets you single-step and set breakpoints without editing code; io:format debugging requires inserting and later removing print calls.

# Common Errors

- **Error**: Printing very large data structures to the shell.
  **Correction**: Dump large structures to a file (e.g. with a `dump/2` helper) and inspect them in an editor.

- **Error**: Using bare `spawn` while debugging a concurrent program.
  **Correction**: Use `spawn_link` so abnormal exits print error messages.

# Common Confusions

- **Confusion**: Believing debugging Erlang requires a sophisticated debugger.
  **Clarification**: Single-assignment variables and no mutable state make print-statement debugging unusually effective; a debugger is often unnecessary.

# Source Reference

Chapter 21: "Profiling, Debugging, and Tracing", section "Debugging Techniques" (subsections "io:format Debugging" and "Dumping to a File").

# Verification Notes

- Definition source: Direct quotes from "Debugging Techniques" and "io:format Debugging".
- Confidence rationale: HIGH — the technique and its supporting practices are explicitly described with code.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
