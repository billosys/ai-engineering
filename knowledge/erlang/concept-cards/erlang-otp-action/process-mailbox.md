---
# === CORE IDENTIFICATION ===
concept: Process Mailbox
slug: process-mailbox

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
  - mailbox
  - message queue

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - message-passing
extends: []
related:
  - send-operator
  - receive-expression
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a process mailbox?"
  - "Where do incoming messages go?"
  - "How does a process retrieve its messages?"
---

# Quick Definition

A process mailbox is the per-process queue where incoming messages are stored as they arrive, until the process chooses to retrieve them with a receive expression.

# Core Definition

"Each process has a mailbox where incoming messages are stored as they arrive, even if the receiving process is currently busy, and the messages are kept there until the process decides to check the mailbox" (Chapter 1, section 1.1.4). The process "can then search and retrieve messages from the mailbox at its convenience using a `receive` expression." A process having its own mailbox is part of what makes processes independent agents: a sender can deliver a message without the receiver being ready, and the receiver consumes messages on its own schedule.

# Prerequisites

- **Erlang process** — every process owns a mailbox.
- **Message passing** — the mailbox holds the messages that message passing delivers.

# Key Properties

1. Each process has exactly one mailbox.
2. Incoming messages are stored in the mailbox as they arrive.
3. Messages are queued even when the receiving process is busy.
4. Messages stay in the mailbox until the process decides to check it.
5. A process retrieves messages with a `receive` expression, which can search the mailbox.

# Construction / Recognition

## To Identify/Recognize:
1. Each spawned process automatically has a mailbox.
2. Sending with `!` deposits a copy into the destination's mailbox.
3. A `receive` expression scans and removes messages from it.

# Context & Application

- **Typical contexts**: Every Erlang process that receives messages.
- **Common applications**: Buffering requests for a server process; decoupling sender pace from receiver pace.
- **Historical/stylistic notes**: The mailbox enables the asynchronous "send-and-pray" style — the sender need not be suspended while a message is being delivered.

# Examples

**Example 1** (Listing 1.1, "Process communication in Erlang"): The example `receive` expression grabs the first available message from the mailbox.

**Example 2** (section 1.1.4): Even if the receiving process is busy, incoming messages still accumulate in its mailbox until it checks them.

# Relationships

## Builds Upon
- **Erlang process** — the mailbox is part of every process.

## Enables
- **Receive expression** — the `receive` construct consumes mailbox contents.

## Related
- **Send operator** — `!` deposits messages into a mailbox.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Assuming a message is lost if the receiver is busy when it is sent.
  **Correction**: Messages wait in the mailbox until the process checks it.

# Common Confusions

- **Confusion**: Thinking a process must be actively waiting to receive a message.
  **Clarification**: Messages are buffered in the mailbox; the process retrieves them at its convenience.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.1.4 "Programming with processes in Erlang," "How processes talk" subsection. See Listing 1.1.

# Verification Notes

- Definition source: Direct adaptation from section 1.1.4.
- Confidence rationale: HIGH — the mailbox is explicitly described.
- Uncertainties: None.
- Cross-reference status: `send-operator` and `receive-expression` are planned cards in this source.
- Re-extraction notes: Fresh extraction; no prior card.
