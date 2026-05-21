---
# === CORE IDENTIFICATION ===
concept: Server Loop
slug: server-loop

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-patterns
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "A Whirlwind Tour of Erlang"
chapter_number: 2
pdf_page: null
section: "The File Server Process"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - receive loop
  - infinite server loop
  - tail-recursive loop

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - message-passing
  - recursion
  - pattern-matching
related:
  - spawn
  - function-clause
extends: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does gen_server relate to the client/server pattern?"
  - "How do I spawn a process and send it messages?"
---

# Quick Definition

A server loop is the standard Erlang pattern for a long-lived process: a function that waits in a `receive` block for a command, handles it, then calls itself again to wait for the next command. Tail-call optimization keeps it running in constant space forever.

# Core Definition

Armstrong shows the loop skeleton (Chapter 2, "The File Server Process"):

```erlang
loop(Dir) ->
    %% wait for a command
    receive
        Command ->
            ... do something ...
    end,
    loop(Dir).
```

"This is how we write an infinite loop in Erlang. ... In the loop we wait to receive a command; when we receive a command, we obey the command and then call ourselves again to get the next command. ... This is the standard way of writing a loop in Erlang. Just call yourself as the last thing you do." Because the recursive call is the last action, "Erlang applies a so-called tail-call optimization to the code, which means that this function will run in constant space." `loop` is "a function that never returns" — and in a concurrent language that is not a problem, because the loop runs in its own process in parallel with everything else.

# Prerequisites

- **Process** — A server loop runs inside a long-lived process.
- **Message passing** — The loop waits for messages and replies to them.
- **Recursion** — The loop continues by calling itself.
- **Pattern matching** — The `receive` block selects which message to handle.

# Key Properties

1. It is a function (conventionally `loop/N`) that never returns.
2. It blocks on a `receive` until a message arrives.
3. After handling the message, the last action is a call to itself.
4. The tail-recursive self-call runs in constant space (tail-call optimization).
5. State (e.g., the current directory) is carried as the loop function's arguments.
6. The infinite loop is safe because it runs concurrently in its own process.

# Construction / Recognition

## To Write a Server Loop:
1. Define a function such as `loop(State)`.
2. Inside it, write `receive` with one clause per kind of request.
3. Handle each request (often by replying to a `Client` PID).
4. End the function body with a self-call `loop(State)` (updating state arguments as needed).
5. Spawn the process with `spawn(Module, loop, [InitialState])`.

## To Recognize It:
1. A function whose body is a `receive ... end` followed by a call to itself.
2. The function appears in a `spawn(...)` call and is exported.

# Context & Application

- **Typical contexts**: Servers — the file server, and by extension any request-handling process.
- **Common applications**: The hand-written precursor to OTP's `gen_server` behaviour.
- **Historical/stylistic notes**: "A server is just a program that services requests in an infinite loop and that runs in parallel with any other tasks that we want to perform."

# Examples

**Example 1** (Chapter 2, "The File Server Process"): `afile_server:loop/1` receives `{Client, list_dir}` or `{Client, {get_file, File}}`, replies to `Client`, then calls `loop(Dir)` again — an infinite request-handling loop.

**Example 2** (Chapter 2, skeleton): The reduced form `loop(Dir) -> receive Command -> ... end, loop(Dir).` is given as "how we write an infinite loop in Erlang."

# Relationships

## Builds Upon
- **Recursion** — The loop continues by tail-recursive self-calls.
- **Message passing** — The loop's purpose is to receive and reply to messages.
- **Process** — The loop is the body of a long-lived process.

## Enables
- The hand-written server loop is the conceptual basis for the OTP `gen_server` behaviour (developed in a later chapter).

## Related
- **Spawn** — Starts the process that runs the loop.
- **Function clause** — Each `receive` branch is selected by a pattern, mirroring clause selection.

## Contrasts With
- No directly contrasting concept in these chapters.

# Common Errors

- **Error**: Doing work *after* the recursive call instead of making it the last action.
  **Correction**: The self-call must be the final expression so tail-call optimization keeps the loop in constant space.

- **Error**: Worrying that an infinite loop will exhaust the stack.
  **Correction**: A tail-recursive loop runs in constant space; it will not run out of stack.

# Common Confusions

- **Confusion**: Thinking a function that "never returns" is a bug.
  **Clarification**: In concurrent Erlang a server loop deliberately never returns; it runs in its own process alongside everything else.

- **Confusion**: Believing the loop must store state in a global or mutable variable.
  **Clarification**: State is threaded through the loop's function arguments (e.g., `loop(Dir)`); each iteration passes the current state.

# Source Reference

"Programming Erlang, Second Edition," Chapter 2: A Whirlwind Tour of Erlang, section "The File Server Process" (including the "Just for the curious" tail-call note). EPUB-origin source; no page numbers.

# Verification Notes

- Definition source: Direct quotation and code skeleton from Chapter 2, "The File Server Process."
- Confidence rationale: HIGH — the loop pattern and its tail-call rationale are explicitly explained.
- Uncertainties: Tier set to intermediate because the pattern requires recursion and message passing as prerequisites.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
