---
# === CORE IDENTIFICATION ===
concept: The dbg Trace Library
slug: dbg-trace-library

# === CLASSIFICATION ===
category: production-ops
subcategory: tracing
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Profiling, Debugging, and Tracing"
chapter_number: 21
pdf_page: null
section: "Using the Trace Libraries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - dbg
  - "trace libraries"
  - ttb
  - ms_transform

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process-tracing
extends:
  - process-tracing
related:
  - io-format-debugging
contrasts_with:
  - process-tracing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the dbg trace library?"
  - "How do I trace Erlang code without using the raw trace BIFs?"
  - "What trace libraries does Erlang provide?"
---

# Quick Definition

`dbg` is a library module that provides a simplified, higher-level interface to the Erlang trace BIFs, hiding their low-level details. It is one of three trace-related libraries, alongside `ttb` and `ms_transform`.

# Core Definition

The trace libraries let you perform the same traces as the raw BIFs but without the low-level detail. "We can perform the same trace ... using the library module `dbg`. This hides all the details of the low-level Erlang BIFs" ("Using the Trace Libraries"). The book names three modules to read up on for tracing:

- `dbg` — provides a simplified interface to the Erlang trace BIFs.
- `ttb` — yet another interface to the trace BIFs; higher level than `dbg`.
- `ms_transform` — makes match specifications for use in the tracer software.

For fine-grained control you write custom tracing on the trace BIFs; for quick experiments the library code is sufficient.

# Prerequisites

- **Process tracing** — `dbg` is a convenience layer over the trace BIFs; understanding what is being traced requires understanding process tracing.

# Key Properties

1. `dbg` is a library wrapper over the low-level Erlang trace BIFs.
2. It hides the details of `erlang:trace/3` and `erlang:trace_pattern/3`.
3. `dbg:tracer/0` starts a tracer; `dbg:tpl/4` sets a traced pattern; `dbg:p/2` selects processes/flags.
4. `dbg:fun2ms/1` converts a fun into a match specification.
5. `ttb` is a higher-level trace interface than `dbg`.
6. `ms_transform` builds match specifications for the tracer.
7. Library tracing is good for quick experiments; raw BIFs are for fine-grained custom tracing.

# Construction / Recognition

## To Trace with dbg:
1. Start a tracer with `dbg:tracer()`.
2. Set a trace on the target function with `dbg:tpl(Mod, Fun, '_', MatchSpec)`, building the match spec via `dbg:fun2ms(...)`.
3. Select which processes and event types to trace with `dbg:p(all, [c])`.
4. Run the code; trace output is printed automatically.

## To Recognize:
1. Look for `dbg:tracer`, `dbg:tpl`, `dbg:p`, `dbg:fun2ms`, or `ttb:` calls.

# Context & Application

The trace libraries make tracing accessible without writing trace BIF code.

- **Typical contexts**: Quick tracing experiments during development or diagnosis.
- **Common applications**: Tracing a module's function calls and return values with a few `dbg` calls.
- **Historical/stylistic notes**: For fine-grained control, custom code on the trace BIFs is still preferred.

# Examples

**Example 1** ("Using the Trace Libraries"): Tracing `tracer_test:fib/1` with `dbg`.

```erlang
test1() ->
    dbg:tracer(),
    dbg:tpl(tracer_test,fib,'_',
            dbg:fun2ms(fun(_) -> return_trace() end)),
    dbg:p(all,[c]),
    tracer_test:fib(4).
```

**Example 2** ("Using the Trace Libraries"): Running `test1()` prints the call/return trace, e.g. `(<0.34.0>) call tracer_test:fib(4)` and `(<0.34.0>) returned from tracer_test:fib/1 -> 5` — the same result as a hand-written BIF tracer.

# Relationships

## Builds Upon
- **Process tracing** — `dbg` is a higher-level interface over the trace BIFs.

## Enables
- (No card depends on this concept.)

## Related
- **io:format debugging** — Another low-effort way to observe program behavior.

## Contrasts With
- **Process tracing** — Raw trace BIFs give fine-grained custom control; `dbg` trades that for a simple interface suited to quick experiments.

# Common Errors

- **Error**: Hand-writing match specifications for use with `dbg`.
  **Correction**: Use `dbg:fun2ms/1` (or `ms_transform`) to generate match specifications from a fun.

- **Error**: Reaching for `dbg` when very fine-grained tracing control is needed.
  **Correction**: For fine-grained control, write custom tracing on the trace BIFs; use `dbg` for quick experiments.

# Common Confusions

- **Confusion**: Thinking `dbg`, `ttb`, and `ms_transform` do the same job.
  **Clarification**: `dbg` is a simplified BIF interface, `ttb` is an even higher-level interface, and `ms_transform` builds the match specifications the tracers use.

# Source Reference

Chapter 21: "Profiling, Debugging, and Tracing", section "Tracing Messages and Process Execution", subsection "Using the Trace Libraries".

# Verification Notes

- Definition source: Direct quotes from "Using the Trace Libraries".
- Confidence rationale: HIGH — `dbg` and the three trace modules are explicitly described with a worked example.
- Uncertainties: `ttb` and `ms_transform` are named but not demonstrated in the book.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card.
