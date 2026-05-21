---
# === CORE IDENTIFICATION ===
concept: Software Transactional Memory
slug: software-transactional-memory

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
  - STM
  - transactional memory

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process-communication-paradigms
extends:
  - process-communication-paradigms
related:
  - shared-memory-with-locks
contrasts_with:
  - message-passing

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is software transactional memory?"
  - "How does STM avoid locks?"
  - "What are the drawbacks of STM?"
---

# Quick Definition

Software transactional memory (STM) is a process-communication paradigm that treats memory like a database, using optimistic transactions instead of locks to decide what gets written and when.

# Core Definition

STM "treats memory more like a traditional database, using *transactions* to decide what gets written and when" (Chapter 1, section 1.1.3). The implementation typically avoids locks by working optimistically: a sequence of read and write accesses is treated as a single operation; if two processes try to access the shared region at the same time, each in its own transaction, only one succeeds, and the others are told they failed and should retry after checking the new contents. The book considers STM at its core a variant of shared memory with locks. It can currently be found in the GHC implementation of Haskell and in the JVM-based language Clojure.

# Prerequisites

- **Process communication paradigms** — STM is one of the four surveyed approaches.

# Key Properties

1. Memory is treated like a database with transactions.
2. Transactions are optimistic — they avoid locks.
3. On contention, one transaction succeeds and the rest must retry.
4. No process waits for another to release a lock.
5. There is overhead from the transaction system and from extra memory to hold pending writes.

# Construction / Recognition

## To Identify/Recognize:
1. Look for read/write sequences grouped into transactions.
2. Look for retry logic when a transaction fails due to contention.
3. Recognize the absence of explicit lock/unlock operations.

# Context & Application

- **Typical contexts**: Haskell (GHC) and Clojure concurrency.
- **Common applications**: Optimistic concurrent updates to shared state where contention is low.
- **Historical/stylistic notes**: The book calls STM a lively research topic and suggests it may be more useful at the OS level than at the application level; ideally there would be hardware support for transactional memory.

# Examples

**Example 1** (section 1.1.3): STM is found in the GHC implementation of the Haskell programming language and in Clojure.

**Example 2** (section 1.1.3): The book notes the main drawback is having to retry failed transactions, which could fail repeatedly under contention.

# Relationships

## Builds Upon
- **Process communication paradigms** — one of the four members.
- **Shared memory with locks** — the book considers STM a variant of shared memory.

## Enables
- Lock-free optimistic updates to shared state.

## Related
- **Shared memory with locks** — STM addresses the same problem without explicit locks.

## Contrasts With
- **Message passing** — STM still relies on shared memory; message passing does not.

# Common Errors

- **Error**: Assuming transactions never need to be repeated.
  **Correction**: Failed transactions must be retried, and they can fail repeatedly under contention.

# Common Confusions

- **Confusion**: Believing STM eliminates the problems of shared memory.
  **Clarification**: The book classifies STM as at its core a variant of shared memory with locks.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.1.3 "Four process communication paradigms," "Software transactional memory (STM)" subsection.

# Verification Notes

- Definition source: Direct adaptation from section 1.1.3.
- Confidence rationale: HIGH — STM is explicitly defined and its trade-offs discussed.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
