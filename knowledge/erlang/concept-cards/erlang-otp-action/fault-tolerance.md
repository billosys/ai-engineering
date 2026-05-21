---
# === CORE IDENTIFICATION ===
concept: Fault Tolerance
slug: fault-tolerance

# === CLASSIFICATION ===
category: fault-tolerance
subcategory: fault-tolerance-overview
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.2 Erlang's fault tolerance infrastructure"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - fault-tolerant systems
  - fault tolerance infrastructure

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - process-isolation
extends: []
related:
  - process-link
  - exit-signal
  - supervision
  - let-it-crash
  - distributed-erlang
  - exception
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is fault tolerance?"
  - "How does Erlang support fault tolerance?"
  - "Why does fault tolerance matter in real systems?"
---

# Quick Definition

Fault tolerance is a system's ability to deal with mistakes and unexpected problems without going to pieces. Erlang supports it through exception handling and a unique system of process links.

# Core Definition

"In order to deal with imperfections in code and data, just like aircraft engineers deal with imperfections in steel and aluminum, we need to have systems that are fault tolerant, that are able to deal with mistakes and don't go to pieces each time an unexpected problem occurs" (Chapter 1, section 1.2). Erlang provides two mechanisms: like many languages it has *exception handling* for catching errors in a particular piece of code, but it also has "a unique system of *process links* for handling process failures in an effective way." Process isolation is a pillar of fault tolerance — a crash in one process cannot corrupt another — and the highest levels of fault tolerance are achieved through distribution across machines.

# Prerequisites

- **Erlang process** — fault tolerance is organized around processes failing independently.
- **Process isolation** — contained failures are the basis of fault tolerance.

# Key Properties

1. A fault-tolerant system survives mistakes in code and data without collapsing.
2. Erlang provides exception handling for in-code error recovery.
3. Erlang provides process links for handling process failures.
4. Process isolation ensures a failure cannot corrupt unrelated processes.
5. Distribution across machines provides the highest levels of fault tolerance.

# Construction / Recognition

## To Construct/Create:
1. Isolate independent activities into separate processes.
2. Link related processes so failures propagate as a group.
3. Use supervisors to detect failures and restore a known-good state.
4. Distribute across machines to survive hardware failure.

# Context & Application

- **Typical contexts**: Real, live production systems where programmers and requirements are imperfect.
- **Common applications**: Telecom-grade systems, high-availability servers.
- **Historical/stylistic notes**: The book frames the "let it crash" philosophy as a powerful recipe for fault tolerance.

# Examples

**Example 1** (section 1.2): The analogy of aircraft engineers dealing with imperfections in steel and aluminum motivates building software that tolerates imperfect code and data.

**Example 2** (section 1.2.3): A corrupt input crashes a process in worker group A; the supervisor restores group A's base state and the system continues, while consuming group B is unaffected.

# Relationships

## Builds Upon
- **Erlang process** and **process isolation** — failures are contained per process.

## Enables
- **Supervision** — structured detection and recovery from failures.

## Related
- **Process link** — propagates failure among related processes.
- **Exit signal** — the signal generated on failure.
- **Let it crash** — the philosophy underpinning Erlang fault tolerance.
- **Exception** — exception handling catches errors in code.
- **Distributed Erlang** — distribution gives the highest fault tolerance.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Trying to defensively patch over every possible error in place.
  **Correction**: The Erlang philosophy is to let a faulty process crash cleanly and restart from a known-good state.

# Common Confusions

- **Confusion**: Believing fault tolerance means errors never happen.
  **Clarification**: It means the system continues functioning *despite* errors, by containing and recovering from them.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.2 "Erlang's fault tolerance infrastructure" (and its subsections 1.2.1–1.2.3).

# Verification Notes

- Definition source: Direct adaptation from section 1.2.
- Confidence rationale: HIGH — fault tolerance is explicitly introduced and its mechanisms named.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
