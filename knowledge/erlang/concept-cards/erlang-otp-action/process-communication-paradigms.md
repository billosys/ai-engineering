---
# === CORE IDENTIFICATION ===
concept: Process Communication Paradigms
slug: process-communication-paradigms

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
  - four process communication paradigms
  - approaches to process communication

# === TYPED RELATIONSHIPS ===
prerequisites:
  - concurrency
extends: []
related:
  - shared-memory-with-locks
  - software-transactional-memory
  - futures-and-promises
  - message-passing
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the four process communication paradigms?"
  - "How do concurrent systems share information?"
  - "Where does Erlang's message passing fit among communication paradigms?"
---

# Quick Definition

The four process communication paradigms are the major approaches concurrent systems use to share information: shared memory with locks, software transactional memory, futures/promises, and message passing.

# Core Definition

The central problem in all concurrent systems is sharing information: if a problem is split into tasks, how should those tasks communicate? (Chapter 1, section 1.1.3). The book discusses four approaches that have gained mindshare: **shared memory with locks** (the oldest and still most popular), **software transactional memory (STM)**, **futures and promises**, and **message passing**. They are presented to give an overview of how current languages and systems handle communication and to highlight what is different about Erlang, which uses asynchronous message passing.

# Prerequisites

- **Concurrency** — communication paradigms only matter once a problem is split into concurrent tasks.

# Key Properties

1. There are four paradigms surveyed: shared memory with locks, STM, futures/promises, message passing.
2. Shared memory with locks is the mainstream, oldest technique.
3. STM treats memory like a database, using transactions instead of locks.
4. Futures/promises outsource a computation; reading an unready value blocks.
5. Message passing copies data between isolated processes; Erlang uses it asynchronously.

# Construction / Recognition

## To Identify/Recognize:
1. Determine how tasks share data: through shared cells, transactions, deferred results, or copied messages.
2. Locks and STM both rest on shared, mutable memory.
3. Futures and message passing both pass data; futures couple sender and reader, message passing does not.

# Context & Application

- **Typical contexts**: Evaluating the trade-offs of a concurrency model.
- **Common applications**: Choosing or understanding a language's concurrency primitives.
- **Historical/stylistic notes**: The book calls shared memory "the GOTO of our time" — ubiquitous but error-prone — and argues message passing, while not the flashiest, is the most practical for systems engineering.

# Examples

**Example 1** (section 1.1.3): STM is found in the GHC implementation of Haskell and in Clojure.

**Example 2** (section 1.1.3): Futures/promises appear in languages like E and MultiLisp, as a library in Java, and resemble I-vars/M-vars in Id and dataflow variables in Oz.

# Relationships

## Builds Upon
- **Concurrency** — these paradigms answer how concurrent tasks communicate.

## Enables
- This is a survey concept; the four paradigms are its members.

## Related
- **Shared memory with locks** — paradigm one.
- **Software transactional memory** — paradigm two.
- **Futures and promises** — paradigm three.
- **Message passing** — paradigm four, used by Erlang.

## Contrasts With
- None — this card is the umbrella concept; contrasts live among its members.

# Common Errors

- **Error**: Assuming message passing and shared memory are interchangeable.
  **Correction**: They have fundamentally different failure and reasoning properties.

# Common Confusions

- **Confusion**: Treating STM as fundamentally different from shared memory.
  **Clarification**: The book considers STM at its core a variant of shared memory with locks.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.1.3 "Four process communication paradigms."

# Verification Notes

- Definition source: Synthesized from the section 1.1.3 overview.
- Confidence rationale: HIGH — the four paradigms are explicitly enumerated.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
