---
# === CORE IDENTIFICATION ===
concept: Synchronizing Clients with gen_server:reply
slug: synchronizing-clients

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Generic Servers"
chapter_number: 3
pdf_page: 96
section: "Synchronizing Clients"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_server:reply"
  - deferred reply
  - rendezvous
  - From field

# === TYPED RELATIONSHIPS ===
prerequisites:
  - synchronous-message-passing
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can a gen_server delay its reply to a client?"
  - "What is the From field used for?"
---

# Quick Definition

A `gen_server` can defer a synchronous reply by returning `{noreply, NewState}` from `handle_call/3` and later calling `gen_server:reply(From, Reply)`, using the saved `From` to answer the client when ready.

# Core Definition

For a server that "has to wait for both requests before responding to the first," the solution uses the `From` field: "Instead of returning a reply back to the behavior loop, we return `{noreply, NewState}`. We then use the From attribute and the function `gen_server:reply(From, Reply)` to later send back the reply to the client when it suits us" (Cesarini & Vinoski, p. 88). The saved `From` may be stored "as part of the NewState or in a table or database." `gen_server:reply/2` can also send "an immediate acknowledgment" before a long computation. `From` "is a tuple containing the client pid and a unique reference," but it must be treated "as an opaque data type" since its representation may change.

# Prerequisites

- **Synchronous message passing** — Deferred replies build on `handle_call/3` and the synchronous `call` protocol.

# Key Properties

1. `handle_call/3` may return `{noreply, NewState}` instead of `{reply, ...}`.
2. The `From` argument identifies the waiting client.
3. `gen_server:reply(From, Reply)` later sends the reply to that client.
4. `From` can be saved in loop data, a table, or a database between calls.
5. `From` is a `{ClientPid, Reference}` tuple but must be treated as opaque.
6. Deferred replies enable client rendezvous and immediate acknowledgments before long work.

# Construction / Recognition

## To Construct:
1. In `handle_call/3`, save `From` somewhere and return `{noreply, NewState}`.
2. When ready, call `gen_server:reply(From, Reply)` to answer the client.

## To Recognize:
1. A `handle_call/3` clause returning `{noreply, ...}` and a `gen_server:reply/2` call elsewhere.

# Context & Application

- **Typical contexts**: Synchronizing two clients; acknowledging a request before a long computation.
- **Common applications**: A server that needs data from two requests before answering either.
- **Historical/stylistic notes**: This pattern keeps the client's synchronous semantics while freeing the server to reply on its own schedule.

# Examples

**Example 1** (p. 89): Immediate acknowledgment before slow work:

```erlang
handle_call({add, Data}, From, Sum) ->
    gen_server:reply(From, ok),
    timer:sleep(1000),
    NewSum = add(Data, Sum),
    io:format("From:~p, Sum:~p~n",[From, NewSum]),
    {noreply, NewSum}.
```

The client receives `ok` immediately while the server keeps working.

# Relationships

## Builds Upon
- **Synchronous message passing** — Deferred replies extend the `handle_call/3` mechanism.

## Enables
- *(none specific in scope)*

## Related
- *(none additional)*

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Pattern matching `From` as a tuple and depending on its internal shape.
  **Correction**: Treat `From` as an opaque value; pass it only to `gen_server:reply/2`.

# Common Confusions

- **Confusion**: Thinking `handle_call/3` must always reply immediately.
  **Clarification**: It may return `{noreply, NewState}` and reply later via `gen_server:reply(From, Reply)`.

# Source Reference

Chapter 3: Generic Servers, Section "Synchronizing Clients," pages 88-89. See Figure 4-5 (rendezvous with generic servers).

# Verification Notes

- Definition source: Direct quotes from pp. 88-89.
- Confidence rationale: HIGH — explicit definition with a worked example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
