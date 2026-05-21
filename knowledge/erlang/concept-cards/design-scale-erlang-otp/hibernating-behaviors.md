---
# === CORE IDENTIFICATION ===
concept: Hibernating Behaviors
slug: hibernating-behaviors

# === CLASSIFICATION ===
category: performance
subcategory: memory
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Generic Servers"
chapter_number: 3
pdf_page: 96
section: "Hibernating Behaviors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - hibernate
  - process hibernation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
extends: []
related:
  - gen-server-timeouts
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does hibernating a gen_server do?"
  - "When should I use hibernate?"
---

# Quick Definition

Returning the atom `hibernate` (in place of a timeout value) makes a `gen_server` shed its call stack, run a full garbage collection, and shrink its memory footprint until the next message arrives.

# Core Definition

"If instead of a timeout value or the atom infinity we return the atom hibernate, the server will reduce its memory footprint and enter a wait state. You will want to use hibernate when servers that receive intermittent, memory-intensive requests are causing the system to run low on memory. Using hibernate will discard the call stack and run a full-sweep garbage collection, placing everything in one continuous heap. The allocated memory is then shrunk to the size of the data on the heap. The server will remain in this state until it receives a new message" (Cesarini & Vinoski, p. 97).

# Prerequisites

- **Gen_server** — `hibernate` is returned in a `gen_server` callback tuple, in the timeout position.

# Key Properties

1. `hibernate` is returned in place of a timeout value in a callback's return tuple.
2. It discards the process's call stack.
3. It runs a full-sweep garbage collection, placing data in one continuous heap.
4. Allocated memory is shrunk to the size of the heap data.
5. The server stays hibernated until it receives a new message.
6. There is a cost: a full-sweep GC before hibernating and another soon after waking.

# Construction / Recognition

## To Construct:
1. Return `hibernate` instead of a timeout in the callback's return tuple.
2. Use it only when no messages are expected for the foreseeable future and memory must be reclaimed.

## To Recognize:
1. A callback return tuple ending in the atom `hibernate`.

# Context & Application

- **Typical contexts**: Servers that receive intermittent, memory-intensive requests and idle in between.
- **Common applications**: Reclaiming memory from a server that will be quiet for a while.
- **Historical/stylistic notes**: The book warns against using hibernation preemptively — for busy processes it likely costs more than it saves; benchmark under stress before adopting it.

# Examples

The source provides no standalone code example for `hibernate`; it describes the mechanism in prose and notes that `hibernate` is returned in the same tuple position as a `Timeout` value (p. 97).

# Relationships

## Builds Upon
- **Gen_server** — `hibernate` is part of the `gen_server` callback return protocol.

## Enables
- *(none specific in scope)*

## Related
- **Generic server timeouts** — `hibernate` occupies the same return-tuple slot as a `Timeout` value.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Hibernating a busy server as a preemptive optimization.
  **Correction**: Hibernate only an idle server; for a busy one the GC cost likely exceeds any saving — benchmark first.

# Common Confusions

- **Confusion**: Thinking hibernation is free memory savings.
  **Clarification**: It triggers a full-sweep GC before hibernating and another after waking; it pays off only for genuinely idle, memory-heavy servers.

# Source Reference

Chapter 3: Generic Servers, Section "Hibernating Behaviors," page 97.

# Verification Notes

- Definition source: Direct quotes from p. 97.
- Confidence rationale: HIGH — explicit, complete description of the mechanism and its costs.
- Uncertainties: The source provides no code example for this concept; the Examples section notes this honestly.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
