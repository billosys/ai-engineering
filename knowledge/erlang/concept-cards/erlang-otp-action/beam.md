---
# === CORE IDENTIFICATION ===
concept: BEAM
slug: beam

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
  - "Bogdan's Erlang Abstract Machine"
  - Erlang virtual machine
  - Erlang VM emulator
  - byte-code emulator

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-runtime-system
extends:
  - erlang-runtime-system
related:
  - beam-file
  - compiling-modules
  - scheduler
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is BEAM?"
  - "What does the BEAM emulator do?"
  - "Is it necessary to compile Erlang to native code?"
---

# Quick Definition

BEAM (Bogdan's Erlang Abstract Machine) is the Erlang virtual machine emulator inside ERTS — the part that executes Erlang programs after they have been compiled to byte code.

# Core Definition

"One particularly important part of ERTS is the Erlang virtual machine emulator: this is the part that executes Erlang programs after they have been compiled to byte code. This virtual machine is known as Bogdan's Erlang Abstract Machine (BEAM) and is very efficient" (Chapter 1, section 1.4). Although it is also possible to compile Erlang programs to native machine code, this is not usually necessary, because the BEAM emulator is fast enough. The book notes there is no clear-cut line between the virtual machine and ERTS as a whole.

# Prerequisites

- **Erlang runtime system** — BEAM is a part of ERTS.

# Key Properties

1. BEAM is the virtual machine emulator within ERTS.
2. It executes Erlang programs after they are compiled to byte code.
3. "BEAM" stands for Bogdan's Erlang Abstract Machine.
4. It is efficient enough that native compilation is usually unnecessary.
5. There is no clear-cut line between BEAM and ERTS as a whole.

# Construction / Recognition

## To Identify/Recognize:
1. Erlang source is compiled to byte code (a `.beam` file).
2. The BEAM emulator loads and executes that byte code.
3. The emulator version is printed at shell startup, e.g. "Erlang (BEAM) emulator version 5.6.5."

# Context & Application

- **Typical contexts**: Running any compiled Erlang code.
- **Common applications**: Default execution mode for Erlang programs.
- **Historical/stylistic notes**: Native compilation exists as an option but is rarely needed because BEAM is fast.

# Examples

**Example 1** (section 1.4): "This virtual machine is known as Bogdan's Erlang Abstract Machine (BEAM) and is very efficient."

**Example 2** (Chapter 2, section 2.1.1): The shell startup banner reads "Erlang (BEAM) emulator version 5.6.5 [smp:2]," naming the BEAM emulator.

# Relationships

## Builds Upon
- **Erlang runtime system** — BEAM is the emulator part of ERTS.

## Enables
- Execution of compiled Erlang byte code.

## Related
- **BEAM file** — the `.beam` byte-code file BEAM loads and runs.
- **Compiling modules** — produces the byte code BEAM executes.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Compiling Erlang to native code for routine performance.
  **Correction**: The BEAM emulator is fast enough that native compilation is usually unnecessary.

# Common Confusions

- **Confusion**: Believing BEAM and ERTS are sharply distinct.
  **Clarification**: There is no clear-cut line; people say "Erlang VM" to mean the emulator and runtime system together.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.4 "The Erlang runtime system and virtual machine." See also the shell banner in Chapter 2, section 2.1.1.

# Verification Notes

- Definition source: Direct adaptation from section 1.4.
- Confidence rationale: HIGH — BEAM is explicitly named and defined.
- Uncertainties: None.
- Cross-reference status: `beam-file` and `compiling-modules` are planned cards in this source.
- Re-extraction notes: Fresh extraction; no prior card.
