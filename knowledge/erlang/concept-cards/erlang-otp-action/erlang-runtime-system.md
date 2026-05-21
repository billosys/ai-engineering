---
# === CORE IDENTIFICATION ===
concept: Erlang Runtime System
slug: erlang-runtime-system

# === CLASSIFICATION ===
category: performance
subcategory: runtime-system
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.4 The Erlang runtime system and virtual machine"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - ERTS
  - Erlang Run-Time System
  - Erlang VM

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - beam
  - scheduler
  - garbage-collector
  - io-and-scheduling
  - erlang-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang runtime system?"
  - "What does ERTS do?"
  - "What is the relationship between ERTS and the Erlang VM?"
---

# Quick Definition

The Erlang Run-Time System (ERTS) is the core C-language implementation that handles all low-level work in Erlang: processes, memory, message passing, I/O, and distribution.

# Core Definition

"The core of the standard Erlang implementation is something called the Erlang Run-Time System application (ERTS): this is a big chunk of code written in the C programming language, and it's responsible for all the low-level stuff in Erlang" (Chapter 1, section 1.4). It lets Erlang talk to the file system and console, handles memory, implements Erlang processes, controls how processes are distributed over CPU resources, handles message passing between processes, and lets processes on two different machines (each in its own ERTS instance) talk to each other. Erlang runs on any operating system ERTS can be ported to. The book notes there is no clear-cut line between the virtual machine and ERTS as a whole; people often say "Erlang VM" to mean the emulator and runtime system together.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. ERTS is written in the C programming language.
2. It is responsible for all low-level work in Erlang.
3. It implements Erlang processes and schedules them over CPU resources.
4. It handles message passing, including between separate ERTS instances on different machines.
5. ERTS generally runs as a single OS process (named `beam` or `werl` in OS process listings).
6. Erlang runs on any OS that ERTS can be ported to.

# Construction / Recognition

## To Identify/Recognize:
1. Look for the OS process named `beam` or `werl`.
2. Recognize ERTS as the C layer beneath all Erlang code.
3. Each running Erlang node is one ERTS instance.

# Context & Application

- **Typical contexts**: Every running Erlang system.
- **Common applications**: Hosting Erlang processes, handling I/O, enabling distribution.
- **Historical/stylistic notes**: Three runtime aspects highlighted as central to Erlang's power are the scheduler, the I/O model, and the garbage collector.

# Examples

**Example 1** (section 1.4): ERTS lets processes on two different machines, each in its own ERTS instance, talk to each other as if they were on the same machine.

**Example 2** (section 1.4.1): ERTS generally runs as a single operating system process, usually found under the name `beam` or `werl` in OS process listings.

# Relationships

## Builds Upon
- This is a foundational concept.

## Enables
- **BEAM** — the virtual machine emulator is a part of ERTS.
- **Scheduler**, **garbage collector**, **I/O and scheduling** — runtime subsystems.
- **Erlang process** — ERTS implements processes.

## Related
- **BEAM** — often conflated with ERTS as a whole under the name "Erlang VM."

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Treating ERTS and the BEAM emulator as cleanly separate components.
  **Correction**: The book notes there is no clear-cut line; "Erlang VM" often means the emulator and runtime system together.

# Common Confusions

- **Confusion**: Thinking ERTS is the Erlang language.
  **Clarification**: ERTS is the C-language runtime that executes compiled Erlang and provides low-level services.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.4 "The Erlang runtime system and virtual machine."

# Verification Notes

- Definition source: Direct adaptation from section 1.4.
- Confidence rationale: HIGH — ERTS is explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
