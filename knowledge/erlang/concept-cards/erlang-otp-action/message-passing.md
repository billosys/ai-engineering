---
# === CORE IDENTIFICATION ===
concept: Message Passing
slug: message-passing

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-communication
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.1.3 Four process communication paradigms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - process communication
  - send-and-pray

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - process-mailbox
  - send-operator
  - receive-expression
  - distributed-erlang
  - location-transparency
contrasts_with:
  - shared-memory-with-locks
  - software-transactional-memory
  - futures-and-promises

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Erlang processes communicate?"
  - "What is message passing?"
  - "Why are Erlang's message-passing primitives asynchronous?"
---

# Quick Definition

Message passing is Erlang's process-communication mechanism: a process sends a read-only copy of data to another process's mailbox. Erlang's message-passing primitives are asynchronous.

# Core Definition

Because Erlang processes share no internal data, they must communicate by copying: "If one process wants to exchange information with another, it sends a message; that message is a read-only copy of the data the sender has" (Chapter 1, section 1.1.2). The receiving process effectively gets a separate copy, and nothing it does to that copy is observable by the sender; the only way to communicate back is to send another message in the reverse direction (section 1.1.3). Message passing comes in two flavors — *synchronous* (sender waits until the message arrives) and *asynchronous* (sender proceeds immediately). In Erlang the primitives are asynchronous ("send-and-pray"), because the synchronous form is easily built on top by having the receiver send an explicit reply. A key consequence: communication works the same whether sender and receiver are on the same computer or separated by a network.

# Prerequisites

- **Erlang process** — message passing is communication *between* processes.

# Key Properties

1. Messages are read-only copies of the sender's data.
2. The receiver's modifications to its copy are invisible to the sender.
3. Erlang's primitives are asynchronous; the sender does not block.
4. Synchronous communication is built on asynchronous by having the receiver reply explicitly.
5. Communication is identical for local and remote processes.
6. Copying large structures can be expensive, so message size and complexity should be managed.

# Construction / Recognition

## To Construct/Create:
1. Obtain the destination pid (e.g. from `spawn` or `self()`).
2. Use the `!` (send) operator: `Destination ! Message`.
3. The message is copied into the destination process's mailbox.
4. The receiver later retrieves it with a `receive` expression.

# Context & Application

- **Typical contexts**: All inter-process interaction in Erlang.
- **Common applications**: Request/response protocols, event notification, distributing work across nodes.
- **Historical/stylistic notes**: The book argues message passing is the most practical and flexible of the four communication paradigms from a systems-engineering perspective. Most idiomatic messages are small, so copying overhead is usually negligible.

# Examples

**Example 1** (Listing 1.1, "Process communication in Erlang"): Two independent concurrent processes communicate; `self()` produces the current process's identifier, which is passed to the new process so it knows where to reply.

**Example 2** (section 1.1.4): Spawning the function `ping` with zero arguments and sending messages to the resulting pid demonstrates Erlang's process communication "in a nutshell."

# Relationships

## Builds Upon
- **Erlang process** — messages travel between isolated processes.

## Enables
- **Distributed Erlang** — copy-based semantics make distribution natural.
- **Location transparency** — same communication syntax local or remote.

## Related
- **Process mailbox** — incoming messages are stored there.
- **Send operator** — the `!` primitive.
- **Receive expression** — retrieves messages from the mailbox.

## Contrasts With
- **Shared memory with locks** — message passing avoids locks and shared state entirely.
- **Software transactional memory** — no transactions, retries, or contention.
- **Futures and promises** — no implicit blocking on a remote value.

# Common Errors

- **Error**: Sending very large data structures as messages.
  **Correction**: Copying large structures is expensive; keep messages small and manage their complexity.

- **Error**: Assuming a successful send means the receiver acted on the message.
  **Correction**: Asynchronous send tells you nothing about what the receiver did next; it may have died immediately.

# Common Confusions

- **Confusion**: Believing the receiver shares the same data object as the sender.
  **Clarification**: The receiver gets a personal, read-only copy.

- **Confusion**: Thinking Erlang has built-in synchronous messaging.
  **Clarification**: The primitives are asynchronous; synchronous behavior is layered on by sending explicit replies.

# Source Reference

Chapter 1: The Erlang/OTP platform, sections 1.1.2, 1.1.3 "Four process communication paradigms" (Message passing subsection), and 1.1.4 "Programming with processes in Erlang." See Listing 1.1.

# Verification Notes

- Definition source: Direct adaptation from sections 1.1.2 and 1.1.3.
- Confidence rationale: HIGH — message passing is explicitly defined and discussed at length.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
