---
# === CORE IDENTIFICATION ===
concept: Client Functions
slug: client-functions

# === CLASSIFICATION ===
category: api-design
subcategory: client-api
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Behaviors"
chapter_number: 2
pdf_page: 72
section: "The Client Functions"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - client API
  - functional interface
  - client interface

# === TYPED RELATIONSHIPS ===
prerequisites:
  - client-server-design-pattern
extends: []
related:
  - the-server-loop
  - message-passing-under-the-hood
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the client API of a server?"
  - "Why hide message passing behind a functional interface?"
---

# Quick Definition

Client functions form the client API: the functions client processes call to access a server's services. They hide the message-passing protocol behind a functional interface.

# Core Definition

"We refer to the functions called by client processes to control and access the services of a server process as the client API. It is always good practice, for readability and maintainability, to hide message passing and protocol in a functional interface. The client functions in the running example do exactly this" (Cesarini & Vinoski, p. 62). In the frequency example, the sending of requests and receiving of replies is "encapsulating ... in the `call/1` and `reply/2` functions. They contain code that otherwise would have to be cloned for every message sent and received." The client functions "are called and executed in the scope of the client process." By hiding the protocol, "we are able to change it without affecting the code outside of the frequency module, client calls included."

# Prerequisites

- **Client-server design pattern** — Client functions are the client-facing half of the client-server pattern.

# Key Properties

1. Client functions are the API that client processes call.
2. They execute in the scope of the *client* process, not the server.
3. They hide the message-passing protocol behind a functional interface.
4. Common send/receive code is factored into a `call/1` helper.
5. Hiding the protocol lets it change without affecting callers.
6. The client functions, their message contents, and the server name are specific; the `call`/`reply` mechanism is largely generic.

# Construction / Recognition

## To Construct:
1. Write one exported function per server operation (e.g., `allocate/0`, `deallocate/1`).
2. Have each build the request term and delegate to a `call/1` helper.
3. Implement `call/1` to send the request and `receive` the reply.

## To Recognize:
1. Exported functions in the server's module that wrap `!` sends and `receive`s.

# Context & Application

- **Typical contexts**: Every client-server module's public interface.
- **Common applications**: `start/0`, `stop/0`, `allocate/0`, `deallocate/1` in the frequency module.
- **Historical/stylistic notes**: Hiding the protocol in client functions later allows replacing it (e.g., adding references and monitors) without touching callers.

# Examples

**Example 1** (p. 62): The frequency client functions and the `call/1`/`reply/2` helpers:

```erlang
stop() -> call(stop).
allocate() -> call(allocate).
deallocate(Freq) -> call({deallocate, Freq}).
call(Message) ->
    frequency ! {request, self(), Message},
    receive {reply, Reply} -> Reply end.
reply(Pid, Reply) ->
    Pid ! {reply, Reply}.
```

**Example 2** (p. 63): The "anomaly" — `call/1` references the hardcoded registered name `frequency`, which is the only non-generic part of the helper.

# Relationships

## Builds Upon
- **Client-server design pattern** — Client functions are its client-facing component.

## Enables
- *(none specific in scope)*

## Related
- **The server loop** — Receives the requests the client functions send.
- **Message passing under the hood** — `call/1` is later hardened against race conditions.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Letting callers send raw messages to the server instead of going through client functions.
  **Correction**: Always route access through the client API so the protocol can evolve independently.

# Common Confusions

- **Confusion**: Thinking client functions run in the server process.
  **Clarification**: They run in the *client* process — they merely send messages to, and await replies from, the server.

# Source Reference

Chapter 2: Behaviors, Section "The Client Functions," pages 62-64. See Figures 3-5 and 3-6 (the message protocol and frequency server messages).

# Verification Notes

- Definition source: Direct quotes from pp. 62-63.
- Confidence rationale: HIGH — explicit definition and code example.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
