---
# === CORE IDENTIFICATION ===
concept: "gen_server:call (Synchronous Request)"
slug: gen-server-call

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
section: "Synchronous Requests - Call"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "gen_server call"
  - "synchronous request"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - client-server-model
extends: []
related:
  - gen-server-init
contrasts_with:
  - gen-server-cast

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does gen_server:call relate to handle_call?"
  - "What distinguishes synchronous (call) from asynchronous (cast) requests?"
  - "How do I send a synchronous request to a gen_server?"
---

# Quick Definition

`gen_server:call/2` sends a synchronous request to a gen_server and blocks until the server processes it and returns a reply via `handle_call/3`.

# Core Definition

According to the gen_server Behaviour chapter: "The request is made into a message and sent to the gen_server. When the request is received, the gen_server calls handle_call(Request, From, State), which is expected to return a tuple {reply,Reply,State1}. Reply is the reply that is to be sent back to the client, and State1 is a new value for the state of the gen_server."

# Prerequisites

- **gen_server** — call is a mechanism provided by the gen_server behaviour.
- **Client-Server Model** — call implements the synchronous query/reply pattern.

# Key Properties

1. `gen_server:call/2` takes the server name/pid and the request term.
2. The call is synchronous — the caller blocks until a reply is received.
3. The gen_server invokes `handle_call(Request, From, State)` in the callback module.
4. `handle_call/3` must return `{reply, Reply, NewState}`.
5. `Reply` is sent back to the caller; `NewState` becomes the server's new state.
6. The server name used in `call/2` must match the name used when starting the gen_server.

# Construction / Recognition

## To Construct/Create:
1. Define an interface function that calls `gen_server:call(ServerName, Request)`.
2. Implement `handle_call(Request, From, State)` in the callback module.
3. Return `{reply, Reply, NewState}` from `handle_call/3`.

## To Identify/Recognize:
1. Client code calls `gen_server:call/2` or `gen_server:call/3`.
2. The callback module implements `handle_call/3`.
3. The return value is `{reply, Reply, NewState}`.

# Context & Application

Synchronous calls are used when the client needs a result from the server before continuing. In the source's channel allocation example, `alloc()` uses a call because the client needs to know which channel was allocated. The caller process is blocked until the gen_server processes the request and sends back the reply.

# Examples

**Example 1** (gen_server_concepts.md, "Synchronous Requests - Call"): The interface function and callback for channel allocation:
```erlang
alloc() ->
    gen_server:call(ch3, alloc).
```

```erlang
handle_call(alloc, _From, Chs) ->
    {Ch, Chs2} = alloc(Chs),
    {reply, Ch, Chs2}.
```
"In this case, the reply is the allocated channel Ch and the new state is the set of remaining available channels Chs2."

# Relationships

## Builds Upon
- **gen_server** — call is one of the two primary request mechanisms
- **Client-Server Model** — call implements the synchronous query/reply pattern

## Enables
- No specific downstream concepts.

## Related
- **gen_server:init** — init establishes the initial state that handle_call operates on

## Contrasts With
- **gen_server:cast** — cast is asynchronous (fire-and-forget) and uses `handle_cast/2` returning `{noreply, NewState}`, while call is synchronous and uses `handle_call/3` returning `{reply, Reply, NewState}`.

# Common Errors

- **Error**: Returning `{noreply, State}` from `handle_call/3` without sending a manual reply.
  **Correction**: `handle_call/3` should normally return `{reply, Reply, NewState}`. If using `{noreply, NewState}`, you must send the reply manually using `gen_server:reply/2`.

- **Error**: Using `call` when no reply is needed.
  **Correction**: Use `gen_server:cast/2` for fire-and-forget requests where no reply is needed.

# Common Confusions

- **Confusion**: Thinking `gen_server:call/2` is the same as a function call.
  **Clarification**: `gen_server:call/2` sends a message to another process and waits for a reply. It involves inter-process communication, not a direct function invocation.

# Source Reference

OTP Design Principles, "gen_server Behaviour" chapter, "Synchronous Requests - Call" section (gen_server_concepts.md).

# Verification Notes

- Definition source: Directly quoted from gen_server_concepts.md "Synchronous Requests - Call" section.
- Confidence rationale: High — explicitly described with code examples in the source.
- Uncertainties: None.
- Cross-reference status: References gen-server, client-server-model, gen-server-cast, gen-server-init (planned cards).
