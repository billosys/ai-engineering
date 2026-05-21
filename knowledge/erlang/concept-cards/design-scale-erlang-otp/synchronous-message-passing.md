---
# === CORE IDENTIFICATION ===
concept: Synchronous Message Passing
slug: synchronous-message-passing

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Generic Servers"
chapter_number: 3
pdf_page: 96
section: "Synchronous Message Passing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_server:call"
  - handle_call
  - synchronous call

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
extends: []
related:
  - synchronizing-clients
  - call-timeouts
contrasts_with:
  - asynchronous-message-passing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a gen_server handle synchronous messages?"
  - "What does handle_call/3 return?"
  - "What is the difference between synchronous and asynchronous message passing?"
---

# Quick Definition

Synchronous message passing in a `gen_server` is done with `gen_server:call/2`: it sends a request and blocks until `handle_call/3` produces a reply, which becomes the call's return value.

# Core Definition

"While Erlang has asynchronous message passing built in as part of the language, there is nothing stopping us from implementing synchronous calls using existing primitives. This is what the `gen_server:call/2` function does. It sends a synchronous Message to the server and waits for a Reply while the server handles the request in a callback function. The Reply is passed as the return value to the call" (Cesarini & Vinoski, p. 82). "Upon receiving a synchronous request, the `handle_call(Message, _From, LoopData)` callback function is invoked." The callback returns `{reply, Reply, NewLoopData}` — the atom `reply` tells the `gen_server` to send `Reply` back to the client, and `NewLoopData` becomes the next loop state.

# Prerequisites

- **Gen_server** — `call/2` and `handle_call/3` are part of the `gen_server` behavior.

# Key Properties

1. `gen_server:call(Name, Message)` sends a synchronous request and returns the `Reply`.
2. The client blocks until the server replies.
3. The server invokes `handle_call(Message, _From, LoopData)`.
4. `_From` carries a unique request identifier and client info — treat it as opaque.
5. `handle_call/3` returns `{reply, Reply, NewLoopData}`.
6. The request and reply carry a unique tag/reference matching them together.
7. There should be one `handle_call/3` clause per request, selected by pattern matching.

# Construction / Recognition

## To Construct:
1. Write a client function calling `gen_server:call(Name, Message)`.
2. Implement one `handle_call/3` clause per request type.
3. Compute the reply and new loop data; return `{reply, Reply, NewLoopData}`.

## To Recognize:
1. A `gen_server:call/2` client function paired with `handle_call/3` clauses.

# Context & Application

- **Typical contexts**: Requests that need a result back from the server.
- **Common applications**: `allocate/0` must be synchronous because the caller needs the allocated frequency; also pinging a server to confirm it is alive, and throttling request rate.
- **Historical/stylistic notes**: `gen_server:call` hides the reference tagging and corner cases discussed in Chapter 2.

# Examples

**Example 1** (p. 83): Synchronous allocation in the frequency server:

```erlang
allocate() ->
    gen_server:call(frequency, {allocate, self()}).
handle_call({allocate, Pid}, _From, Frequencies) ->
    {NewFrequencies, Reply} = allocate(Frequencies, Pid),
    {reply, Reply, NewFrequencies}.
```

`allocate/0` returns `{ok, Frequency}` or `{error, no_frequency}`.

# Relationships

## Builds Upon
- **Gen_server** — Synchronous calls are a `gen_server` facility.

## Enables
- **Synchronizing clients** — `handle_call/3` may defer the reply via `{noreply, ...}`.

## Related
- **Call timeouts** — A synchronous `call` has a built-in 5-second timeout.

## Contrasts With
- **Asynchronous message passing** — `cast/2` does not wait for or receive a reply.

# Common Errors

- **Error**: Using a `case` statement inside one `handle_call/3` clause to dispatch all messages.
  **Correction**: Use a separate `handle_call/3` clause per request and let pattern matching pick it.
- **Error**: Treating `_From` as a tuple and depending on its shape.
  **Correction**: Use `From` only as an opaque value passed to `gen_server:reply/2`.

# Common Confusions

- **Confusion**: Thinking Erlang has no synchronous messaging.
  **Clarification**: Erlang's primitives are asynchronous, but `gen_server:call/2` builds synchronous request/reply on top of them.

# Source Reference

Chapter 3: Generic Servers, Section "Synchronous Message Passing," pages 82-83. See Figure 4-3 (synchronous message passing).

# Verification Notes

- Definition source: Direct quotes from pp. 82-83.
- Confidence rationale: HIGH — explicit definition with the frequency example.
- Uncertainties: None.
- Cross-reference status: `synchronizing-clients` and `call-timeouts` are planned Chapter 3 cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
