---
# === CORE IDENTIFICATION ===
concept: Asynchronous Message Passing
slug: asynchronous-message-passing

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
section: "Asynchronous Message Passing"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_server:cast"
  - handle_cast
  - asynchronous request
  - cast

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
extends: []
related: []
contrasts_with:
  - synchronous-message-passing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does a gen_server handle asynchronous messages?"
  - "What does handle_cast/2 return?"
  - "When should I use a cast instead of a call?"
---

# Quick Definition

Asynchronous message passing in a `gen_server` is done with `gen_server:cast/2`: it sends a request, immediately returns `ok`, and the server handles it later in `handle_cast/2` without replying.

# Core Definition

"If the client needs to send a message to the server but does not expect a reply, it can use asynchronous requests. This is done using the `gen_server:cast/2` library function" (Cesarini & Vinoski, p. 84). `gen_server:cast(Name, Message)` returns `ok`. "As soon as the cast/2 call has sent its request, it returns the atom ok. On the server side, the request is stored in the process mailbox and handled sequentially. When it is received, the Message is passed on to the `handle_cast/2` callback function." The callback "has to return a tuple of the format `{noreply, NewLoopData}`."

# Prerequisites

- **Gen_server** — `cast/2` and `handle_cast/2` are part of the `gen_server` behavior.

# Key Properties

1. `gen_server:cast(Name, Message)` sends an asynchronous request and immediately returns `ok`.
2. The client does not wait for and receives no reply.
3. The server stores the request in its mailbox and handles it in `handle_cast/2`.
4. `handle_cast(Message, LoopData)` returns `{noreply, NewLoopData}`.
5. Good candidates for casts are client functions whose return value is a hardcoded `ok`.
6. Casts rely on side effects executed in the callback module.

# Construction / Recognition

## To Construct:
1. Write a client function calling `gen_server:cast(Name, Message)`.
2. Implement a `handle_cast/2` clause matching the message.
3. Perform the side effect, then return `{noreply, NewLoopData}`.

## To Recognize:
1. A `gen_server:cast/2` client function paired with `handle_cast/2` clauses.

# Context & Application

- **Typical contexts**: Fire-and-forget operations where no result is needed.
- **Common applications**: `deallocate/1` always returns `ok`, so it is a perfect cast.
- **Historical/stylistic notes**: Synchronous calls are still preferred when you must know the server is alive or want to throttle request rate.

# Examples

**Example 1** (p. 84): Asynchronous deallocation in the frequency server:

```erlang
deallocate(Frequency) ->
    gen_server:cast(frequency, {deallocate, Frequency}).
handle_cast({deallocate, Freq}, Frequencies) ->
    NewFrequencies = deallocate(Frequencies, Freq),
    {noreply, NewFrequencies}.
```

`deallocate/1` returns `ok` immediately; the server processes the request later.

# Relationships

## Builds Upon
- **Gen_server** — Asynchronous casts are a `gen_server` facility.

## Enables
- *(none specific in scope)*

## Related
- *(none additional)*

## Contrasts With
- **Synchronous message passing** — `call/2` blocks for a reply; `cast/2` returns `ok` immediately and gets no reply.

# Common Errors

- **Error**: Bypassing `gen_server:cast` with `Pid ! Msg` to save microseconds.
  **Correction**: Don't — it makes code hard to debug and discards OTP's guarantees; optimize only from measured evidence.

# Common Confusions

- **Confusion**: Thinking a cast guarantees the request was handled.
  **Clarification**: `cast/2` only guarantees the message was sent; it returns `ok` before the server processes anything.

# Source Reference

Chapter 3: Generic Servers, Section "Asynchronous Message Passing," pages 84-85. See Figure 4-4 (asynchronous message passing).

# Verification Notes

- Definition source: Direct quotes from p. 84.
- Confidence rationale: HIGH — explicit definition with the frequency example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
