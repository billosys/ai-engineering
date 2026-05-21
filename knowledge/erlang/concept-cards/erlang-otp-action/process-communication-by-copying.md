---
# === CORE IDENTIFICATION ===
concept: Process Communication by Copying
slug: process-communication-by-copying

# === CLASSIFICATION ===
category: distribution
subcategory: distribution-fundamentals
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Introducing distributed Erlang/OTP"
chapter_number: 8
pdf_page: null
section: "8.1.1 Process communication by copying"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "communication by copying"
  - "copy semantics"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - message-passing
extends: []
related:
  - distributed-erlang
  - location-transparency
contrasts_with:
  - shared-memory-with-locks

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does communication by copying mean in Erlang?"
  - "Why does Erlang avoid shared memory between processes?"
  - "How does copy semantics make distribution possible?"
---

# Quick Definition

Process communication by copying means that when one Erlang process sends data to another, the receiver gets a private copy; nothing the sender does afterward affects it, so the same model works whether processes are local or remote.

# Core Definition

Process communication by copying is the property that Erlang processes communicate strictly by asynchronous message passing, with data transferred so the receiver effectively gets a separate copy. Nothing the sender does to the data afterward can be observed by the receiver, and vice versa; any further communication must happen through further messages. By taking sharing out of the picture, Erlang's creators made it possible to build transparent, fault-tolerant systems where one computer does not halt just because a neighbor crashes. This model works identically for processes on the same machine and on separate machines connected by a network — the only difference being the network transfer time (Ch. 8, Section 8.1.1). In practice, read-only shared memory may be used locally for efficiency, but the observable result is the same.

# Prerequisites

- **message-passing** — Communication by copying is a property of Erlang's message-passing mechanism.

# Key Properties

1. Sent data reaches the receiver as a private copy.
2. Sender mutations after sending are invisible to the receiver, and vice versa.
3. Communication is strictly asynchronous message passing.
4. No shared memory between processes (locally, read-only sharing may be used as an optimization).
5. The same semantics hold for local and remote processes.
6. One of the two features that make distribution possible.

# Construction / Recognition

## How It Works:
1. A process sends a term with `!` or via an API function.
2. The runtime transfers a copy of the term to the receiver's mailbox.
3. The receiver works with its own copy; further updates require new messages.

## To Recognize:
1. Any Erlang inter-process communication uses copy semantics — there is no alternative.

# Context & Application

- **Typical contexts**: All Erlang concurrency and distribution.
- **Common applications**: Sending a `dict` of resource tuples between nodes without marshalling, knowing the receiver cannot corrupt your structure.
- **Historical/stylistic notes**: Removing sharing was a deliberate design decision to enable fault tolerance and transparent distribution.

# Examples

**Example 1** (Section 8.1.1, Figures 8.2–8.3): Message passing on a single machine and between different machines differ only by network transfer time; in both cases the receiver gets a private copy.

**Example 2** (Ch. 8, resource discovery): A node can include an entire `dict` data structure as-is in a message, because copy semantics guarantee the receiver cannot mutate the sender's structure.

# Relationships

## Builds Upon
- **message-passing** — Copy semantics is how message passing transfers data.

## Enables
- **distributed-erlang** — Copy semantics is one of the two pillars of distribution.

## Related
- **location-transparency** — The complementary pillar of distribution.

## Contrasts With
- **shared-memory-with-locks** — The traditional model copying replaces; sharing ties processes to one machine and complicates fault tolerance.

# Common Errors

- **Error**: Expecting to mutate shared state visible to another process.
  **Correction**: There is no shared mutable state; communicate updates via further messages.

# Common Confusions

- **Confusion**: Believing copying makes Erlang slow for local communication.
  **Clarification**: Locally, read-only shared memory may be used as an optimization; the observable copy semantics are preserved either way.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.1.1 "Process communication by copying," Figures 8.1–8.3.

# Verification Notes

- Definition source: Directly adapted from Section 8.1.1.
- Confidence rationale: HIGH — the book explicitly defines and motivates the property.
- Uncertainties: None.
- Cross-reference status: Verified; `shared-memory-with-locks` exists as a card in this directory.
