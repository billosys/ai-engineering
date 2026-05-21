---
# === CORE IDENTIFICATION ===
concept: I/O and Scheduling
slug: io-and-scheduling

# === CLASSIFICATION ===
category: performance
subcategory: runtime-system
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.4.2 I/O and scheduling"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - event-based I/O
  - nonblocking I/O
  - I/O model

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scheduler
extends:
  - scheduler
related:
  - erlang-runtime-system
  - erlang-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Erlang handle I/O?"
  - "Why does I/O not block the whole Erlang system?"
  - "What is event-based I/O in Erlang?"
---

# Quick Definition

Erlang's I/O model is event-based and nonblocking, integrated with the process scheduler so that one process doing I/O never stops the whole system.

# Core Definition

"One of the things that many concurrent languages get wrong is that they don't think much about I/O... they make the entire system or a large subset of it block while any process is doing I/O" (Chapter 1, section 1.4.2). Erlang avoids this: "At the lowest levels of the system, Erlang does all I/O in an event-based way, which lets a program handle each chunk of data as it enters or leaves the system in a nonblocking manner." This reduces the need to set up and tear down connections and removes the need for OS-based locking and context switching. The Erlang runtime system integrates the event-based I/O system with its process scheduler, so the programmer gets the benefits with none of the hassle — making it easier to build highly available systems.

# Prerequisites

- **Scheduler** — Erlang's I/O is integrated with the process scheduler.

# Key Properties

1. Erlang does all I/O in an event-based way at the lowest levels.
2. Each chunk of data is handled as it enters or leaves the system, nonblocking.
3. A single process doing I/O does not stop the whole system.
4. It reduces connection setup/teardown and removes OS-based locking and context switching.
5. The event-based I/O system is integrated with the process scheduler by ERTS.

# Construction / Recognition

## To Identify/Recognize:
1. I/O operations are dispatched as events rather than blocking calls.
2. The scheduler keeps running other processes while I/O is pending.
3. The system stays responsive under heavy I/O load.

# Context & Application

- **Typical contexts**: Highly available, low-latency systems handling many connections.
- **Common applications**: Network servers handling large numbers of simultaneous clients.
- **Historical/stylistic notes**: The book references Dan Kegel's 2001 paper "The C10K Problem" as background; Erlang solved this class of problem two decades ago.

# Examples

**Example 1** (section 1.4.2): The book cites Dan Kegel's "The C10K Problem" (2001) as an overview of nonblocking-I/O approaches, all of which are complex and painful to implement — which is why the Erlang runtime does most of it for you.

**Example 2** (section 1.4.2): Erlang integrates the event-based I/O system with its process scheduler, so "you get all the benefits with none of the hassle."

# Relationships

## Builds Upon
- **Scheduler** — I/O handling is woven into the scheduler.

## Enables
- Highly available, low-latency systems.

## Related
- **Erlang runtime system** — ERTS implements the I/O subsystem.
- **Erlang process** — processes do I/O without blocking the system.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Assuming a blocking I/O call in one process halts the runtime.
  **Correction**: Erlang's event-based I/O keeps the rest of the system running while I/O is pending.

# Common Confusions

- **Confusion**: Believing event-based I/O must be programmed explicitly as in other languages.
  **Clarification**: The runtime handles the event-based machinery; the programmer gets the benefits without the complexity.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.4.2 "I/O and scheduling."

# Verification Notes

- Definition source: Direct adaptation from section 1.4.2.
- Confidence rationale: HIGH — the event-based, nonblocking I/O model is explicitly described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
