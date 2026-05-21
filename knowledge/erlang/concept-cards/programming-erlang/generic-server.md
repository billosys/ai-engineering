---
# === CORE IDENTIFICATION ===
concept: The Generic Server
slug: generic-server

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: server-abstraction
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introducing OTP"
chapter_number: 22
pdf_page: null
section: "The Road to the Generic Server"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "generic server"
  - "the road to the generic server"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - message-passing
  - callback-module
extends: []
related:
  - gen-server
  - behaviour
  - hot-code-swapping
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the generic server idea?"
  - "How is a server abstracted into a generic part and a callback?"
---

# Quick Definition

The generic server is the idea of factoring a server into a generic component (handling concurrency and error handling) and a problem-specific callback module. The book builds it incrementally as `server1` through `server5`, converging on the real `gen_server`.

# Core Definition

The generic server is an abstraction obtained by separating "the nonfunctional parts of the problem from the functional parts of the problem" (Programming Erlang, "The Road to the Generic Server"). The book writes four little servers — `server1`, `server2`, `server3`, `server4` — each slightly different, where `server4` is similar to the real gen_server. Each server is a process that registers a name, loops with a `State`, receives `{From, Request}` messages, calls `Mod:handle(Request, State)` in the callback module, sends the reply back, and recurses with the new state. The generic part captures "the quintessential nature of a server"; the callback supplies pure sequential code. The author calls this "the most important section in the entire book."

# Prerequisites

- **Process** — a generic server is a long-lived process.
- **Message passing** — clients communicate with the server via `!` and `receive`.
- **Callback module** — the generic server is parameterized by a callback module.

# Key Properties

1. A server is a process with state that changes state when it receives messages.
2. The generic part handles `spawn`, `register`, `send`, `receive`, and the loop.
3. The callback part handles only the request-to-response transformation, sequentially.
4. Successive versions add features: transactions (`server2`), hot code swapping (`server3`), both combined (`server4`), become-anything (`server5`).
5. Generalizing in small transformation steps is the technique the reader is meant to repeat for their own abstractions.

# Construction / Recognition

## To Construct (the basic Server 1 pattern):
1. `start(Name, Mod)` registers a process running `loop(Name, Mod, Mod:init())`.
2. `rpc(Name, Request)` sends `{self(), Request}` and waits for `{Name, Response}`.
3. `loop` receives `{From, Request}`, computes `{Response, State1} = Mod:handle(Request, State)`, replies, and recurses.

## To Recognize:
1. A `start`/`rpc`/`loop` trio parameterized by a `Mod` argument is a generic server.
2. If the callback contains no concurrency code, the server framework is generic.

# Context & Application

- **Typical contexts**: The conceptual foundation for understanding `gen_server` and OTP behaviours.
- **Common applications**: `name_server` runs as the callback for the hand-written generic servers; the technique scales to "hundreds of servers" in a single product.
- **Historical/stylistic notes**: The book deliberately builds the abstraction by hand before showing the real `gen_server`, so the reader understands how `gen_server` works internally.

# Examples

**Example 1** ("Server 1: The Basic Server"): The minimal generic server:

```erlang
start(Name, Mod) ->
    register(Name, spawn(fun() -> loop(Name, Mod, Mod:init()) end)).

loop(Name, Mod, State) ->
    receive
        {From, Request} ->
            {Response, State1} = Mod:handle(Request, State),
            From ! {Name, Response},
            loop(Name, Mod, State1)
    end.
```

**Example 2** ("Server 5: Even More Fun"): `server5` does nothing until sent `{become, F}`, then evaluates `F()` to become any kind of server.

# Relationships

## Builds Upon
- **Callback module** — the generic server is parameterized by one.

## Enables
- **gen_server** — the production behaviour that is "the logical conclusion of a succession of successively sophisticated servers."

## Related
- **Behaviour** — the generic server is the worked example of what a behaviour factors out.
- **Hot code swapping** — added to the generic server in `server3` and `server4`.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Looping with the new state after a handler crashes.
  **Correction**: For transaction semantics (server2), loop with the *original* state if the handler raised an exception.

- **Error**: Hard-coding the server name in the callback, preventing reuse.
  **Correction**: Parameterize the name; the book had to clone `name_server` into `name_server1` because of this.

# Common Confusions

- **Confusion**: Thinking the hand-written servers are production-ready.
  **Clarification**: The book warns these example servers "have one or two extremely small and subtle errors"; use the real `gen_server` for production.

- **Confusion**: Believing each new server needs a new callback.
  **Clarification**: Changing the server while keeping the callback constant changes only the nonfunctional behaviour.

# Source Reference

Chapter 22: Introducing OTP, section "The Road to the Generic Server" (Server 1 through Server 5). No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes and code from "The Road to the Generic Server".
- Confidence rationale: HIGH — the section is an explicit, worked construction of the generic server idea.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
