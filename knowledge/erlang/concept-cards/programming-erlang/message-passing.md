---
# === CORE IDENTIFICATION ===
concept: Message Passing
slug: message-passing

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: communication
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Concurrent Programming"
chapter_number: 12
pdf_page: null
section: "The Concurrency Primitives"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "send"
  - "the send operator"
  - "!"
  - "Pid ! Message"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
extends: []
related:
  - spawn
  - receive
  - mailbox
  - process-identifier
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Erlang processes communicate with each other?"
  - "What is the send operator?"
  - "Is message sending synchronous or asynchronous?"
---

# Quick Definition

Message passing is how Erlang processes communicate: `Pid ! Message` sends `Message` to the process identified by `Pid`. Sending is asynchronous — the sender does not wait.

# Core Definition

`Pid ! Message` "sends `Message` to the process with identifier `Pid`. Message sending is asynchronous. The sender does not wait but continues with what it was doing. `!` is called the send operator" (Armstrong, "Concurrent Programming," "The Concurrency Primitives"). The value of `Pid ! M` is defined to be `M` itself; because of this, `Pid1 ! Pid2 ! ... ! Msg` sends `Msg` to all of `Pid1`, `Pid2`, and so on. When a message is sent to a process, "the message is put into the mailbox of the process." Message passing is the *only* way Erlang processes interact, since they share no memory.

# Prerequisites

- **Process** — Messages are sent between processes; you must know what a process is.

# Key Properties

1. The send operator is `!`; the form is `Pid ! Message`.
2. Sending is asynchronous — the sender continues immediately, without waiting.
3. The value of `Pid ! M` is `M`, so sends can be chained: `Pid1 ! Pid2 ! Msg`.
4. A sent message is placed in the recipient's mailbox.
5. Delivery is unacknowledged — the sender is not told whether the message was received or understood.
6. It is the only inter-process interaction mechanism (processes share no memory).
7. Any Erlang term may be sent as a message.

# Construction / Recognition

## To Construct/Create:
1. Obtain the recipient's Pid (from `spawn`, `self()`, or a registered name).
2. Write `Pid ! Message`, where `Message` is any Erlang term.
3. To get a reply, include `self()` in the message so the recipient knows where to reply.

## To Identify/Recognize:
1. The `!` operator marks a message send.
2. A message of the form `{self(), Request}` indicates a request that expects a reply.

# Context & Application

- **Typical contexts**: All inter-process communication; client/server request/response patterns.
- **Common applications**: Sending requests to servers; replying to clients via a `From` Pid carried in the request.
- **Historical/stylistic notes**: Because the sender does not know to whom to reply, the client must include its own address: `Pid ! {self(), {rectangle, 6, 10}}`.

# Examples

**Example 1** ("The Concurrency Primitives"): `Pid ! {rectangle, 6, 10}` sends a tuple message to the area-server process; the shell then prints `{rectangle,6,10}` because the value of `Pid ! M` is `M`.

**Example 2** ("Introducing Client-Server"): `Pid ! {self(), {rectangle, 6, 10}}` — the client includes `self()` as a reply address so the server can respond.

**Example 3** ("Introducing Client-Server"): Inside the server, `From ! Width * Ht` sends the computed area back to the client identified by `From`.

# Relationships

## Builds Upon
- **Process** — Messages travel between processes.

## Enables
- **Mailbox** — Sent messages land in the recipient's mailbox.
- **receive** — `receive` extracts messages that were sent.

## Related
- **Spawn** — Provides the Pid used as a send target.
- **Process identifier** — The address a message is sent to.

## Contrasts With
- None.

# Common Errors

- **Error**: Sending a request without including a reply address, so the server cannot respond.
  **Correction**: Send `{self(), Request}` so the server knows the `From` Pid.

- **Error**: Assuming a `!` send guarantees the message was processed.
  **Correction**: Sending is asynchronous and unacknowledged; to confirm, await a reply message.

# Common Confusions

- **Confusion**: Thinking `!` blocks until the recipient handles the message.
  **Clarification**: `!` is asynchronous — the sender continues at once; the message just enters the mailbox.

- **Confusion**: Believing message passing copies a reference to shared data.
  **Clarification**: Processes share no memory; the message term is delivered into a separate process's mailbox.

# Source Reference

Chapter 12: "Concurrent Programming," sections "The Concurrency Primitives" and "Introducing Client-Server." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct quotes of the `!` send operator from "The Concurrency Primitives."
- Confidence rationale: HIGH — the operator and its semantics are defined explicitly.
- Uncertainties: None.
- Cross-reference status: Canonical slug `message-passing`; cross-refs verified.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
