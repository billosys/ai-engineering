---
# === CORE IDENTIFICATION ===
concept: Receive Expression
slug: receive-expression

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
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - receive
  - selective receive

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process-mailbox
  - pattern-matching
extends: []
related:
  - send-operator
  - message-passing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a receive expression?"
  - "How does a process retrieve messages from its mailbox?"
---

# Quick Definition

A receive expression is the construct a process uses to search its mailbox and retrieve messages, at the process's convenience.

# Core Definition

A process "can then search and retrieve messages from the mailbox at its convenience using a `receive` expression" (Chapter 1, section 1.1.4). The example in Listing 1.1 uses a `receive` expression that "grabs the first available message." The receive expression lets a process consume messages from its mailbox on its own schedule, rather than being forced to handle them as they arrive.

# Prerequisites

- **Process mailbox** — `receive` retrieves messages stored in the mailbox.
- **Pattern matching** — `receive` clauses match against message contents.

# Key Properties

1. `receive` retrieves messages from the calling process's own mailbox.
2. The process consumes messages at its convenience, not as they arrive.
3. It can search the mailbox (in the simplest case, grabbing the first available message).
4. It is the counterpart of the `!` send operator.

# Construction / Recognition

## To Construct/Create:
1. Within a process, write a `receive` expression with one or more clauses.
2. Each clause is a pattern matched against messages in the mailbox.
3. The first matching message is removed and the corresponding clause body runs.

# Context & Application

- **Typical contexts**: Any process that consumes incoming messages.
- **Common applications**: Server loops; waiting for replies; event handling.
- **Historical/stylistic notes**: OTP behaviours such as `gen_server` encapsulate the `receive` loop so application code rarely writes raw `receive`.

# Examples

**Example 1** (Listing 1.1, "Process communication in Erlang"): A `receive` expression grabs the first available message from the mailbox.

# Relationships

## Builds Upon
- **Process mailbox** — `receive` consumes the mailbox.

## Enables
- Message-driven process behavior and server loops.

## Related
- **Send operator** — `!` deposits the messages that `receive` retrieves.
- **Message passing** — `receive` is the receiving half of message passing.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Assuming messages must be handled in arrival order.
  **Correction**: `receive` can search the mailbox and select messages by pattern.

# Common Confusions

- **Confusion**: Believing a process is blocked from doing anything until a message arrives.
  **Clarification**: The process chooses when to call `receive` and consumes messages at its convenience.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.1.4 "Programming with processes in Erlang," "How processes talk" subsection. See Listing 1.1.

# Verification Notes

- Definition source: Synthesized from the brief description in section 1.1.4 (Chapter 1 introduces `receive` but does not give its full syntax; detailed treatment is in later sections of Chapter 2 on process operations).
- Confidence rationale: MEDIUM — Chapter 1 introduces `receive` only briefly; full syntax is deferred.
- Uncertainties: Selective-receive semantics are not detailed in the read portion of the source.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
