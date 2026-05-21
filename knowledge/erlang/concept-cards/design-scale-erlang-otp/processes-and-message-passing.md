---
# === CORE IDENTIFICATION ===
concept: Processes and Message Passing
slug: processes-and-message-passing

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: processes
tier: foundational

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Introducing Erlang"
chapter_number: 1
pdf_page: 40
section: "Processes and Message Passing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - spawn
  - pid
  - process identifier
  - asynchronous message passing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - tail-recursion
extends: []
related:
  - selective-receive
  - links
  - monitors
  - schedulers-and-reductions
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Erlang processes communicate?"
  - "What is a pid?"
  - "Why is Erlang message passing asynchronous?"
  - "What foundational Erlang concepts underpin the OTP behaviors?"
---

# Quick Definition

Erlang processes are lightweight, memory-isolated units of concurrency that communicate solely by asynchronous message passing. A process is created with `spawn`, which returns a pid used as the address for messages.

# Core Definition

"Concurrency is at the heart of the Erlang programming model. Processes are lightweight, meaning that creating them involves negligible time and memory overhead. Processes do not share memory, and instead communicate with each other through message passing. Messages are copied from the stack of the sending process to the heap of the receiving one" (Cesarini & Vinoski, p. 29). "Processes are created via the `spawn(Mod, Func, Args)` BIF or one of its variants. The result of a spawn call is a process identifier, normally referred to as a pid" (p. 30). "Erlang message passing is asynchronous: the expression that sends a message to a process returns immediately and always appears to be successful, even when the receiving process doesn't exist" (p. 31). Delivered messages "are placed in the mailbox of the receiving process in the same order in which they are received."

# Prerequisites

- **Tail recursion** — A long-lived process loops by tail-recursively calling its loop function, so it can run in constant memory space.

# Key Properties

1. Processes are lightweight; millions can run within one VM.
2. Processes share no memory; messages are copied between processes.
3. `spawn(Mod, Func, Args)` creates a process and returns its pid.
4. The `!` operator sends a message; `self()` returns the caller's own pid.
5. Message sending is asynchronous and always appears to succeed, even to a nonexistent process.
6. Messages land in the recipient's mailbox in arrival order and are read with `receive`.
7. Failure of one process can be isolated because tasks are standalone with no shared memory.

# Construction / Recognition

## To Construct:
1. Call `spawn(Mod, Func, Args)` to start a process running `Func` in `Mod`.
2. Send messages with `Pid ! Message`.
3. Include `self()` in messages so the receiver can reply.
4. Receive replies with a `receive` expression.

## To Identify:
1. Look for `spawn`/`spawn_link` calls and `!` send operators.
2. A `receive ... end` block marks message consumption.

# Context & Application

- **Typical contexts**: Modeling each truly concurrent activity as its own process.
- **Common applications**: Servers, workers, and the echo loop pattern.
- **Historical/stylistic notes**: Memory isolation gives Erlang predictable soft real-time behavior and underpins fault isolation.

# Examples

**Example 1** (p. 30): The echo process — `go/0` spawns `loop/0`, exchanges messages, then stops it:

```erlang
-module(echo).
-export([go/0, loop/0]).
go() ->
    Pid = spawn(echo, loop, []),
    Pid ! {self(), hello},
    receive
        {Pid, Msg} ->
            io:format("~w~n",[Msg])
    end,
    Pid ! stop.
loop() ->
    receive
        {From, Msg} ->
            From ! {self(), Msg},
            loop();
        stop ->
            ok
    end.
```

# Relationships

## Builds Upon
- *(none — foundational)*

## Enables
- **Selective receive** — Mailbox messages are consumed via pattern-matching `receive`.
- **Links** and **Monitors** — Mechanisms layered on processes for failure detection.

## Related
- **Schedulers and reductions** — The BEAM machinery that runs processes concurrently.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Sending a message and assuming the receiver exists or got it.
  **Correction**: Sends are asynchronous and always "succeed"; use monitors/links to detect a missing or dead receiver.

# Common Confusions

- **Confusion**: Believing Erlang processes are OS threads sharing memory.
  **Clarification**: They are VM-level, memory-isolated, and far cheaper than OS threads.

# Source Reference

Chapter 1: Introducing Erlang, Section "Processes and Message Passing," pages 29-31. See Figure 2-1 (spawning a process).

# Verification Notes

- Definition source: Direct quotes from pp. 29-31.
- Confidence rationale: HIGH — explicit definitions and the echo example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
