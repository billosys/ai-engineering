---
# === CORE IDENTIFICATION ===
concept: "gen_server:cast (Asynchronous Request)"
slug: gen-server-cast

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server-callbacks
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_server Behaviour"
chapter_number: null
pdf_page: null
section: "Asynchronous Requests - Cast"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "gen_server cast"
  - "asynchronous request"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - client-server-model
extends: []
related:
  - gen-server-init
contrasts_with:
  - gen-server-call

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does gen_server:cast relate to handle_cast?"
  - "What distinguishes synchronous (call) from asynchronous (cast) requests?"
  - "How do I send an asynchronous request to a gen_server?"
---

# Quick Definition

`gen_server:cast/2` sends an asynchronous (fire-and-forget) request to a gen_server without waiting for a reply; the server processes it via `handle_cast/2`.

# Core Definition

According to the gen_server Behaviour chapter: "The request is made into a message and sent to the gen_server. cast, and thus free, then returns ok." When the request is received, "the gen_server calls handle_cast(Request, State), which is expected to return a tuple {noreply,State1}. State1 is a new value for the state of the gen_server."

# Prerequisites

- **gen_server** — cast is a mechanism provided by the gen_server behaviour.
- **Client-Server Model** — cast implements the asynchronous notification pattern.

# Key Properties

1. `gen_server:cast/2` takes the server name/pid and the request term.
2. The cast is asynchronous — it returns `ok` immediately without waiting for the server.
3. The gen_server invokes `handle_cast(Request, State)` in the callback module.
4. `handle_cast/2` must return `{noreply, NewState}`.
5. No reply is sent to the caller.
6. Can also return `{stop, Reason, NewState}` to signal the gen_server should terminate.

# Construction / Recognition

## To Construct/Create:
1. Define an interface function that calls `gen_server:cast(ServerName, Request)`.
2. Implement `handle_cast(Request, State)` in the callback module.
3. Return `{noreply, NewState}` from `handle_cast/2`.

## To Identify/Recognize:
1. Client code calls `gen_server:cast/2`.
2. The callback module implements `handle_cast/2`.
3. The return value is `{noreply, NewState}` (or `{stop, Reason, NewState}`).

# Context & Application

Asynchronous casts are used when the client does not need a reply and should not block. In the source's channel allocation example, `free(Ch)` uses a cast because the client only needs to tell the server to release a channel — there is no meaningful result to wait for. Cast is also used to implement stop requests for standalone gen_servers.

# Examples

**Example 1** (gen_server_concepts.md, "Asynchronous Requests - Cast"): The interface function and callback for freeing a channel:
```erlang
free(Ch) ->
    gen_server:cast(ch3, {free, Ch}).
```

```erlang
handle_cast({free, Ch}, Chs) ->
    Chs2 = free(Ch, Chs),
    {noreply, Chs2}.
```
"In this case, the new state is the updated list of available channels Chs2."

**Example 2** (gen_server_concepts.md, "Stopping"): Using cast to implement a stop request:
```erlang
stop() ->
    gen_server:cast(ch3, stop).

handle_cast(stop, State) ->
    {stop, normal, State};
```

# Relationships

## Builds Upon
- **gen_server** — cast is one of the two primary request mechanisms
- **Client-Server Model** — cast implements the fire-and-forget pattern

## Enables
- **gen_server:terminate** — returning `{stop, Reason, State}` from handle_cast triggers termination

## Related
- **gen_server:init** — init establishes the initial state that handle_cast operates on

## Contrasts With
- **gen_server:call** — call is synchronous and blocks the caller; handle_call returns `{reply, Reply, NewState}`. Cast is asynchronous and returns `ok` immediately; handle_cast returns `{noreply, NewState}`.

# Common Errors

- **Error**: Using cast when the client needs a result.
  **Correction**: Use `gen_server:call/2` when the client needs to receive a reply from the server.

- **Error**: Returning `{reply, Reply, NewState}` from `handle_cast/2`.
  **Correction**: `handle_cast/2` must return `{noreply, NewState}` or `{stop, Reason, NewState}` — there is no client waiting for a reply.

# Common Confusions

- **Confusion**: Assuming cast guarantees the request has been processed.
  **Clarification**: `gen_server:cast/2` returns `ok` immediately after sending the message. The request has not necessarily been processed yet — it is queued in the server's mailbox.

# Source Reference

OTP Design Principles, "gen_server Behaviour" chapter, "Asynchronous Requests - Cast" section (gen_server_concepts.md).

# Verification Notes

- Definition source: Directly quoted from gen_server_concepts.md "Asynchronous Requests - Cast" section.
- Confidence rationale: High — explicitly described with code examples in the source.
- Uncertainties: None.
- Cross-reference status: References gen-server, client-server-model, gen-server-call, gen-server-init, gen-server-terminate (planned cards).
