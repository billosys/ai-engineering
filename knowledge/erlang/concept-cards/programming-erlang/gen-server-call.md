---
# === CORE IDENTIFICATION ===
concept: gen_server:call (Synchronous Call)
slug: gen-server-call

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introducing OTP"
chapter_number: 22
pdf_page: null
section: "Calling the Server"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_server:call"
  - "synchronous call"
  - "remote procedure call"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - gen-server-callbacks
extends: []
related:
  - gen-server-cast
  - handle-info
contrasts_with:
  - gen-server-cast

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is gen_server:call?"
  - "How does a client make a synchronous request to a gen_server?"
---

# Quick Definition

`gen_server:call(Name, Request)` makes a synchronous remote procedure call to a gen_server. It invokes `handle_call/3` in the callback module, and the client blocks until a reply comes back.

# Core Definition

"To call the server, the client program calls `gen_server:call(Name, Request)`. This results in `handle_call/3` in the callback module being called" (Programming Erlang, "Calling the Server"). `Request` — the second argument of `gen_server:call/2` — reappears as the first argument of `handle_call/3`; `From` is the PID of the requesting client process, and `State` is the current server state. When `handle_call` returns `{reply, Reply, NewState}`, `Reply` goes back to the client where it becomes the return value of `gen_server:call`, and `NewState` becomes the next state of the server. The interplay of `gen_server:call` and `handle_call` is used "for implementing remote procedure calls."

# Prerequisites

- **gen_server** — `call` is the client-side function of a gen_server.
- **gen_server callbacks** — `call` triggers the `handle_call/3` callback.

# Key Properties

1. Synchronous: the calling process blocks until the server replies.
2. `Request` passed to `call` becomes the first argument of `handle_call/3`.
3. The `Reply` element of `handle_call`'s `{reply, Reply, NewState}` is the return value of `call`.
4. A timeout can be supplied as a third argument (`gen_server:call(?MODULE, Term, Timeout)`).
5. Used to implement remote procedure calls against the server.
6. `handle_call` may instead return `{noreply, ...}` and delegate the reply to another process, but the client still waits.

# Construction / Recognition

## To Use gen_server:call:
1. Write an interface function that calls `gen_server:call(ServerName, RequestTerm)`.
2. In the callback module, write a `handle_call(RequestTerm, _From, State)` clause.
3. Return `{reply, Reply, NewState}` from `handle_call` to send `Reply` back to the caller.

## To Recognize:
1. An interface function delegating to `gen_server:call` performs a synchronous request.
2. A `handle_call/3` clause is the server-side counterpart of a `call`.

# Context & Application

- **Typical contexts**: Any request to a gen_server that expects a return value.
- **Common applications**: `my_bank:deposit(Who, Amount)` calls `gen_server:call(?MODULE, {add, Who, Amount})`; `prime_server:new_prime(N)` uses a 20000 ms timeout.
- **Historical/stylistic notes**: In `my_bank`, the interface routines each result in exactly one `gen_server:call`.

# Examples

**Example 1** ("Getting Started with gen_server"): `withdraw(Who, Amount) -> gen_server:call(?MODULE, {remove, Who, Amount}).`

**Example 2** ("The Prime Number Server", Ch. 23): `new_prime(N) -> gen_server:call(?MODULE, {prime, N}, 20000).` — a call with an explicit 20-second timeout.

# Relationships

## Builds Upon
- **gen_server** — `call` is a core part of the gen_server client API.

## Enables
- **gen_server callbacks** — `call` is what invokes `handle_call/3`.

## Related
- **handle_info** — handles messages that did *not* arrive via `call` or `cast`.

## Contrasts With
- **gen_server:cast** — `cast` is asynchronous with no return value; `call` is synchronous and returns a reply.

# Common Errors

- **Error**: Doing slow work directly inside `handle_call`, so every other caller waits.
  **Correction**: Return `{noreply, State}` and reply from a spawned process for long-running requests.

- **Error**: Expecting `call` to return without a matching `handle_call` clause.
  **Correction**: Every request term sent via `call` needs a corresponding `handle_call/3` clause, or the server crashes.

# Common Confusions

- **Confusion**: Thinking `gen_server:call` is asynchronous.
  **Clarification**: `call` is synchronous — the client blocks until the server replies (or the timeout fires).

- **Confusion**: Believing `From` is the message itself.
  **Clarification**: `From` is the PID of the requesting client; the message is `Request`.

# Source Reference

Chapter 22: Introducing OTP, section "Calling the Server" (within "The gen_server Callback Structure"). No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes from "Calling the Server".
- Confidence rationale: HIGH — explicitly defined with template and prose.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
