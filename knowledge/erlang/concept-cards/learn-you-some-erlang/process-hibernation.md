---
concept: Process Hibernation
slug: process-hibernation
category: processes-concurrency
subcategory: process-design
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "An Introduction to OTP"
chapter_number: 14
pdf_page: null
section: "The init Function"
extraction_confidence: high
aliases:
  - "hibernation"
  - "hibernate"
  - "erlang:hibernate"
prerequisites:
  - process
extends: []
related:
  - gen-server-init-callback
contrasts_with: []
answers_questions:
  - "What is process hibernation?"
  - "When should a process hibernate?"
---

# Process Hibernation

## Quick Definition

Process hibernation shrinks a process's memory footprint while it waits for a message, trading some CPU for reduced memory. A `gen_server` callback can request it by adding the atom `hibernate` to its return tuple.

## Core Definition

Hibernation "basically reduces the size of the process's state until it gets a message, at the cost of some processing power." A `gen_server` callback adds the atom `hibernate` to a return tuple (e.g. `{ok, State, hibernate}`) to request it; "if you are in doubt about using hibernation, you probably don't need it." The chapter gives the technical definition: when the BIF `erlang:hibernate(M,F,A)` is called, "the call stack for the currently running process is discarded (the function never returns). The garbage collection then kicks in, and what's left is one continuous heap that is shrunken to the size of the data in the process. This basically compacts all the data so the process takes less space." When the process next receives a message, `M:F` is called with `A` and execution resumes (Hébert, ch. 14, "The init Function," "A Closer Look at Hibernation" sidebar).

## Prerequisites

- **Process** — Hibernation operates on a process's memory

## Key Properties

1. Hibernation compacts a process's memory while it idly waits for a message
2. It trades CPU (garbage collection, stack discard) for reduced memory
3. Requested in a `gen_server` callback by adding `hibernate` to the return tuple
4. The BIF `erlang:hibernate(M,F,A)` discards the call stack — the calling function never returns
5. Garbage collection then shrinks the process to one compact heap
6. On the next message, `M:F(A)` is called and execution resumes
7. Rarely needed — "if you are in doubt... you probably don't need it"

## Construction / Recognition

## To Hibernate a Process

1. In a `gen_server` callback, return a tuple with `hibernate` appended (e.g. `{noreply, State, hibernate}`)
2. Or call the BIF `erlang:hibernate(Module, Function, Args)` directly
3. Expect the call stack to be discarded and the process compacted
4. Resume happens automatically when the next message arrives

## Examples

> **gen_server return tuples** (ch. 14): `{ok, State, hibernate}` from `init/1`, and `{noreply, NewState, hibernate}` from `handle_call`/`handle_cast`.
>
> **Technical definition** (ch. 14): "the call stack for the currently running process is discarded... what's left is one continuous heap that is shrunken to the size of the data in the process."

## Relationships

## Related

- **gen_server init callback** — `init/1` and the `handle_*` callbacks can all request hibernation

## Common Errors

- **Error**: Hibernating a process that receives messages frequently
  **Correction**: Hibernation costs CPU each cycle; use it only for processes that idle for long periods

## Common Confusions

- **Confusion**: Thinking hibernation pauses or suspends the process indefinitely
  **Clarification**: It only compacts memory; the process resumes automatically on the next message

## Source Reference

Chapter 14, "An Introduction to OTP," section "Callback to the Future," subsection "The init Function" and the "A Closer Look at Hibernation" sidebar.

## Verification Notes

- Definition and erlang:hibernate mechanics: directly from ch. 14
- Confidence: HIGH — explicitly described
