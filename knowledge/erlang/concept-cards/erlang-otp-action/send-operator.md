---
# === CORE IDENTIFICATION ===
concept: Send Operator
slug: send-operator

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
section: "1.1.4 Programming with processes in Erlang"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - bang operator
  - "! operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - message-passing
  - pid
extends: []
related:
  - process-mailbox
  - receive-expression
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the send operator in Erlang?"
  - "How do you send a message to a process?"
  - "What does the bang operator do?"
---

# Quick Definition

The send operator `!` (pronounced "bang") sends a message to a process, used in the form `Destination ! Message`. It is the most primitive form of process communication in Erlang.

# Core Definition

"The basic operator for sending a message is `!`, pronounced 'bang,' and it's used in the form 'Destination `!` Message'" (Chapter 1, section 1.1.4). The book describes this as "message passing at its most primitive, like mailing a postcard." The destination is typically a pid; the message is any Erlang term and is delivered as a read-only copy into the destination's mailbox. The OTP framework builds higher-level communication on top of this primitive.

# Prerequisites

- **Message passing** — `!` is the primitive that performs a send.
- **Pid** — the destination of a send is usually a process identifier.

# Key Properties

1. Written as `Destination ! Message`.
2. Pronounced "bang."
3. Asynchronous — the sender does not block waiting for delivery.
4. Delivers a read-only copy of the message to the destination's mailbox.
5. It is the most primitive process-communication construct; OTP layers more on top.

# Construction / Recognition

## To Construct/Create:
1. Obtain the destination pid.
2. Construct the message term.
3. Write `Destination ! Message`.

# Context & Application

- **Typical contexts**: Direct, low-level message sending between processes.
- **Common applications**: Implementing simple protocols; the building block under OTP's `gen_server` calls and casts.
- **Historical/stylistic notes**: In idiomatic OTP code, programmers usually use OTP abstractions rather than raw `!`.

# Examples

**Example 1** (Listing 1.1, "Process communication in Erlang"): The example uses `!` to send messages between two independent concurrent processes; the new process is passed `self()` so it knows where to reply.

**Example 2** (section 1.1.4): The book likens `Destination ! Message` to "mailing a postcard."

# Relationships

## Builds Upon
- **Message passing** — `!` is the concrete primitive of message passing.

## Enables
- **Process mailbox** — `!` deposits messages into a mailbox.

## Related
- **Receive expression** — the counterpart that retrieves sent messages.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Expecting `!` to block until the message is received.
  **Correction**: `!` is asynchronous; it returns immediately and tells you nothing about delivery or the receiver's fate.

# Common Confusions

- **Confusion**: Treating `!` as a high-level communication mechanism.
  **Clarification**: It is the most primitive form; OTP builds richer patterns above it.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.1.4 "Programming with processes in Erlang," "How processes talk" subsection. See Listing 1.1.

# Verification Notes

- Definition source: Direct quotation/adaptation from section 1.1.4.
- Confidence rationale: HIGH — the `!` operator is explicitly named and described.
- Uncertainties: `receive-expression` is treated in later sections of Chapter 2 (exceptions/process operations); referenced as a planned card.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
