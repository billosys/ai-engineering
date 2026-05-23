---
concept: Match Specification Tracing Functions
slug: match-spec-tracing
category: production-ops
subcategory: tracing
tier: advanced
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Match Specifications in Erlang"
chapter_number: null
pdf_page: null
section: "Functions Allowed Only for Tracing"
extraction_confidence: high
aliases:
  - "match spec tracing actions"
  - "trace match body functions"
prerequisites:
  - match-specification
extends:
  - match-specification
related:
  - match-spec-ets
contrasts_with:
  - match-spec-ets
answers_questions:
  - "What tracing-specific functions are available in match specifications?"
  - "How do I use return_trace and exception_trace in match specifications?"
  - "How do I control trace messages from within a match specification?"
---

# Quick Definition

Match specifications used for tracing have access to special action functions in the MatchBody that are not available in ETS. These include `return_trace`, `exception_trace`, `caller`, `caller_line`, `message`, `silent`, `enable_trace`, `disable_trace`, `trace`, and others that control trace behavior and extract runtime information.

# Core Definition

When a match specification is used in a tracing context (via `trace:function/4`), the MatchBody is executed for its side effects rather than a return value. The tracing context provides additional action functions that control trace message generation, enable/disable trace flags, capture caller information, and manipulate sequential trace tokens. These functions are forbidden in ETS match specifications (Ericsson AB, "Match Specifications in Erlang," section "Functions Allowed Only for Tracing").

Key tracing-only functions fall into several categories:

- **Trace message control**: `return_trace`, `exception_trace`, `message`, `silent`
- **Caller information**: `caller`, `caller_line`, `current_stacktrace`
- **Trace flag manipulation**: `enable_trace`, `disable_trace`, `trace`
- **Sequential tracing**: `is_seq_trace`, `set_seq_token`, `get_seq_token`
- **Diagnostics**: `process_dump`, `display`
- **Trace control word**: `get_tcw`, `set_tcw`

# Prerequisites

- **match-specification** -- Understanding the match specification grammar and structure is essential before using tracing-specific functions

# Key Properties

1. All tracing action functions can only appear in the MatchBody part
2. `return_trace` causes a `return_from` trace message upon function return; it **destroys tail-recursiveness** and can cause memory exhaustion on long-running server processes
3. `exception_trace` works like `return_trace` plus generates `exception_from` messages on exceptions, regardless of whether the exception is caught
4. `message` sets additional data appended to trace messages; `{message, false}` suppresses the trace message entirely; `{message, true}` restores default behavior
5. `silent` suppresses call trace messages for the current process when set to `true`, even if `{message, true}` is called; useful for conditional tracing
6. `caller` returns `{Module, Function, Arity}` or `undefined`; `caller_line` additionally returns `{File, Line}` source location when available
7. `current_stacktrace` returns the call stack in the same format as `catch`, truncated to `backtrace_depth`
8. `enable_trace`/`disable_trace`/`trace` manipulate trace flags on the current process or a specified process

# Construction / Recognition

## Using return_trace

```erlang
[{['$1'],
  [{is_list, '$1'}],
  [{return_trace}]}]
```

This traces calls where the first argument is a list and also captures the return value.

## Using message to Filter

```erlang
[{['$1', '$2'],
  [{'>', '$2', 100}],
  [{message, {{'$1', '$2'}}}]},
 {'_', [], [{message, false}]}]
```

The first clause appends `{Arg1, Arg2}` to the trace message when `Arg2 > 100`; the second clause suppresses trace messages for all other calls.

## Using silent for Conditional Tracing

```erlang
[{'$1',
  [{'==',{hd, '$1'},verbose}],
  [{trace, [silent],[]}]},
 {'$1',
  [{'==',{hd, '$1'},silent}],
  [{trace, [],[silent]}]}]
```

Removes the `silent` trace flag when the first argument is `verbose`, and adds it when it is `silent`.

# Context & Application

Tracing match specifications are used in production debugging scenarios where fine-grained control over which calls generate trace messages is critical. Common patterns include:

- **Conditional return tracing**: Only capture return values for calls matching specific argument patterns
- **Silent mode toggling**: Temporarily suppress trace output to reduce noise, re-enabling when specific conditions are met
- **Caller capture**: Determine which function invoked the traced function, useful for understanding call chains
- **Dynamic trace flag management**: Enable/disable tracing on other processes from within a match specification

**Critical warning from source**: `return_trace` and `exception_trace` destroy tail-call optimization. On perpetual server processes, these must only be active for limited periods or the emulator will consume all memory and crash. If `silent` is active, tail-recursiveness is preserved.

# Examples

**Add return_trace only for arity-3 calls** (source: "Match Specifications in Erlang," section "Tracing Examples"):

```erlang
[{'$1',
  [{'==',{length, '$1'},3}],
  [{return_trace}]},
 {'_',[],[]}]
```

**Generate trace only if trace control word is set to 1** (source: same section):

```erlang
[{'_',
  [{'==',{get_tcw},{const, 1}}],
  []}]
```

**Generate trace only if sequential trace token is set** (source: same section):

```erlang
[{'_',
  [{'==',{is_seq_trace},{const, 1}}],
  []}]
```

**Append process dump to trace when all three args are equal numbers** (source: same section):

```erlang
[{['$1', '$1', '$1'],
  [{is_number, '$1'}],
  [{message, {process_dump}}]},
 {'_', [], [{set_seq_token, label, 4711}]}]
```

# Relationships

## Extends

- **match-specification** -- Tracing functions extend the base match specification grammar with additional MatchBody actions

## Contrasts With

- **match-spec-ets** -- ETS match specifications return values and cannot use side-effect functions; tracing match specifications execute for side effects and have access to tracing-only actions

# Common Errors

- **Error**: Using `return_trace` on a tail-recursive server loop without time-limiting
  **Correction**: Only activate `return_trace` for limited periods on long-running processes, or use `silent` to preserve tail-recursiveness

- **Error**: Expecting `caller` to always return a valid MFA tuple
  **Correction**: `caller` returns `undefined` when the calling function cannot be determined, particularly for BIFs not written in Erlang

- **Error**: Placing tracing action functions in the MatchConditions part
  **Correction**: Action functions like `return_trace`, `message`, `caller` are only allowed in the MatchBody part

# Common Confusions

- **Confusion**: `{message, false}` disables tracing entirely
  **Clarification**: It only suppresses the trace message for the current function call; tracing remains active for subsequent calls that match

- **Confusion**: `silent` and `{message, false}` do the same thing
  **Clarification**: `silent` sets a persistent mode on the process that inhibits all future call trace messages until turned off; `{message, false}` only affects the current call

- **Confusion**: `return_trace` only affects the return value
  **Clarification**: It fundamentally changes the execution model by preventing tail-call optimization, which has memory implications for long-running processes

# Source Reference

"Match Specifications in Erlang," sections "Functions Allowed Only for Tracing" and "Tracing Examples." The source provides detailed descriptions of each tracing-only function, explicit warnings about `return_trace` destroying tail-recursiveness, and multiple tracing examples demonstrating `return_trace`, `message`, `silent`, `get_tcw`, `is_seq_trace`, and `set_seq_token`.

# Verification Notes

- All function descriptions: Directly from source section "Functions Allowed Only for Tracing"
- return_trace tail-recursion warning: Explicitly stated -- "this match specification function destroys that property"
- silent behavior: Directly from source description of `silent`
- message special cases (false, true): Directly from source description of `message`
- Examples: Verbatim from source "Tracing Examples" section
- Confidence: HIGH -- all content directly from official ERTS documentation
