---
# === CORE IDENTIFICATION ===
concept: Futures and Promises
slug: futures-and-promises

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
  - futures
  - promises
  - I-vars
  - dataflow variables

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process-communication-paradigms
extends:
  - process-communication-paradigms
related:
  - message-passing
contrasts_with:
  - message-passing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a future or promise?"
  - "How do futures work for concurrent communication?"
  - "What makes future-based programs brittle?"
---

# Quick Definition

A future (or promise) is the result of a computation outsourced to another process; it can be passed around like any value, but reading it blocks until the value is ready.

# Core Definition

"The basic idea is that a future is a result of a computation that has been outsourced to some other process, possibly on another CPU or a completely different computer" (Chapter 1, section 1.1.3). A future can be passed around like any other object, but if someone wants to read the value and it is not ready yet, they have to wait for it to be done. The concept has several variants and is found in languages such as E and MultiLisp, as a library in Java, and resembles I-vars and M-vars in Id and Glasgow Haskell, concurrent logic variables in Concurrent Prolog, and dataflow variables in Oz.

# Prerequisites

- **Process communication paradigms** — futures are one of the four surveyed approaches.

# Key Properties

1. A future holds the result of a computation outsourced to another process.
2. The computing process may be on another CPU or a different computer.
3. A future can be passed around like any other value.
4. Reading an unready future blocks until the value is available.
5. It is conceptually simple but makes programs brittle under remote or network failure.

# Construction / Recognition

## To Identify/Recognize:
1. Look for a placeholder value representing a not-yet-computed result.
2. Look for code that transparently blocks when the value is accessed.
3. Recognize that the future hides whether the computation runs locally or remotely.

# Context & Application

- **Typical contexts**: Languages like E, MultiLisp, and Oz; Java's future libraries.
- **Common applications**: Passing around results of outsourced computations in concurrent systems.
- **Historical/stylistic notes**: The book describes futures as a "more modern approach" relative to shared memory.

# Examples

**Example 1** (section 1.1.3): Futures are found in E and MultiLisp and as a library in Java.

**Example 2** (section 1.1.3): They are similar to I-vars and M-vars in Id and Glasgow Haskell, concurrent logic variables in Concurrent Prolog, and dataflow variables in Oz.

# Relationships

## Builds Upon
- **Process communication paradigms** — one of the four members.

## Enables
- Transparent passing of deferred computation results.

## Related
- **Message passing** — both pass data between concurrent activities.

## Contrasts With
- **Message passing** — futures couple reader and producer with an implicit blocking dependency; message passing decouples sender and receiver.

# Common Errors

- **Error**: Reading a future without handling the case where the remote computation or network failed.
  **Correction**: Code accessing the value may have no recovery path if the value is still missing and the connection is dead; design for that failure.

# Common Confusions

- **Confusion**: Believing futures make concurrent code robust because they are conceptually simple.
  **Clarification**: They make the program brittle in the face of remote-process or network failure.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.1.3 "Four process communication paradigms," "Futures, promises, and similar" subsection.

# Verification Notes

- Definition source: Direct adaptation from section 1.1.3.
- Confidence rationale: HIGH — futures are explicitly defined and discussed.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
