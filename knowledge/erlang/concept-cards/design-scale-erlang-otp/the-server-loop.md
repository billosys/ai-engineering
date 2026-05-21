---
# === CORE IDENTIFICATION ===
concept: The Server Loop
slug: the-server-loop

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: process-design
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Behaviors"
chapter_number: 2
pdf_page: 72
section: "The Server Loop"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - receive-evaluate loop
  - loop data
  - process state

# === TYPED RELATIONSHIPS ===
prerequisites:
  - client-server-design-pattern
  - tail-recursion
extends: []
related:
  - client-functions
  - server-internal-functions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the server loop in a client-server process?"
  - "What is loop data?"
---

# Quick Definition

The server loop is the tail-recursive receive-evaluate loop at the heart of a server process: it waits for a request, handles it, replies, and loops with updated loop data.

# Core Definition

"Server processes iterate in a receive-evaluate loop. They wait for client requests, handle them, return a result, and loop again, waiting for the next message to arrive. With every iteration, they may update their process state and might generate side effects" (Cesarini & Vinoski, p. 64). The loop carries *loop data* (also called *process state*) — "a variable that stores process data between calls" (p. 57) — passed to the "tail-recursive loop/1 call" each iteration (p. 65). "Looping is generic. The protocol used to send and receive messages is generic, but the messages and replies themselves aren't" (p. 65). "By the lack of a call to loop/1 we make the process terminate normally" (p. 65).

# Prerequisites

- **Client-server design pattern** — The server loop is the server-side core of that pattern.
- **Tail recursion** — The loop calls itself tail-recursively to run in constant memory.

# Key Properties

1. The loop is a `receive` expression handling each request type in a clause.
2. After handling a request, it replies and tail-recursively calls itself.
3. Loop data (process state) is passed as an argument each iteration.
4. Each iteration may update loop data and produce side effects.
5. Looping and the message protocol are generic; the messages, handling, and replies are specific.
6. Omitting the recursive `loop/1` call causes the process to terminate normally.

# Construction / Recognition

## To Construct:
1. Write `loop(State)` with a `receive` block.
2. Add one clause per request type; compute the reply and new state.
3. Send the reply, then tail-recursively call `loop(NewState)`.
4. For a stop request, reply and omit the `loop/1` call so the process terminates.

## To Recognize:
1. A `loop/1` function that is a `receive` ending in a self-call.

# Context & Application

- **Typical contexts**: The server-side engine of any client-server process.
- **Common applications**: The frequency server's `loop/1` handling `allocate`, `{deallocate, Freq}`, and `stop`.
- **Historical/stylistic notes**: This loop becomes the `gen_server`'s built-in receive-evaluate loop.

# Examples

**Example 1** (p. 64): The frequency server loop:

```erlang
loop(Frequencies) ->
    receive
        {request, Pid, allocate} ->
            {NewFrequencies, Reply} = allocate(Frequencies, Pid),
            reply(Pid, Reply),
            loop(NewFrequencies);
        {request, Pid , {deallocate, Freq}} ->
            NewFrequencies = deallocate(Frequencies, Freq),
            reply(Pid, ok),
            loop(NewFrequencies);
        {request, Pid, stop} ->
            reply(Pid, ok)
    end.
```

**Example 2** (p. 65): The `stop` clause omits `loop/1`, causing a normal termination — as opposed to an abnormal termination from a runtime error.

# Relationships

## Builds Upon
- **Client-server design pattern** — The loop is the server-side mechanism of the pattern.

## Enables
- *(none specific in scope)*

## Related
- **Client functions** — Send the requests the loop receives.
- **Server-internal functions** — Helper functions the loop calls to do the actual work.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Forgetting to tail-recurse `loop/1` after a non-stop request.
  **Correction**: Every non-terminating clause must end with the `loop/1` call, or the server stops unexpectedly.

# Common Confusions

- **Confusion**: Thinking the loop data variable itself is generic.
  **Clarification**: Storing loop data is generic; the *type and value* of the loop data are specific to the server.

# Source Reference

Chapter 2: Behaviors, Section "The Server Loop," pages 64-66.

# Verification Notes

- Definition source: Direct quotes from pp. 57, 64-65.
- Confidence rationale: HIGH — explicit definition with the frequency loop example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
