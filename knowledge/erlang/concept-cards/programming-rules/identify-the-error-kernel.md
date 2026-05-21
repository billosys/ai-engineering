---
concept: Identify The Error Kernel
slug: identify-the-error-kernel
category: fault-tolerance
subcategory: error-handling
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Error Handling"
chapter_number: 4
pdf_page: null
section: "4.2 Identify the error kernel"
extraction_confidence: high
aliases:
  - "error kernel"
  - "system kernel"
prerequisites: []
extends: []
related:
  - separate-error-handling-from-normal-code
  - dont-program-defensively
contrasts_with: []
answers_questions:
  - "What is the error kernel of a system?"
  - "What distinguishes the error kernel from ordinary application code?"
---

# Quick Definition

The error kernel is the part of the system that must be correct; identifying it is a basic element of system design.

# Core Definition

"One of the basic elements of system design is identifying which part of the system has to be correct and which part does not have to be correct" (Programming Rules, 4.2). As in conventional OS design — where the kernel must be correct but user applications need not be — the first part of system design is to identify the part that must be correct: the **error kernel**. The error kernel often holds a real-time, memory-resident database storing the state of the hardware.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The error kernel is the portion of the system that must be correct.
2. Code outside the kernel does not all have to be correct — its failures are contained.
3. Identifying the kernel is among the first steps of system design.
4. The error kernel often holds a memory-resident database of hardware state.

# Construction / Recognition

## To Apply

1. Early in design, decide which part of the system must be correct.
2. Concentrate correctness effort there; allow non-kernel code to fail and be recovered.

## To Recognize a Candidate

1. A subsystem whose failure would compromise the integrity of the whole system — that belongs in the kernel.

# Context & Application

A core error-handling principle (section 4).

- **Typical contexts**: overall system architecture and fault-tolerance design.
- **Common applications**: designating a correct-by-design core that holds critical state.

# Examples

The source draws an analogy to operating-system design: the OS kernel must be correct, while a failing user application affects only itself, not system integrity.

# Relationships

## Related

- **Separate error handling and normal case code** — recovery code conceptually belongs to the kernel.
- **Do not program "defensively"** — non-kernel code may simply crash and be recovered.

# Common Errors

- **Error**: Treating the whole system as equally critical.
  **Correction**: Identify the minimal error kernel and focus correctness there.

# Common Confusions

- **Confusion**: Equating the error kernel with the entire codebase.
  **Clarification**: It is deliberately *small* — the minimal part that must be correct; the rest is allowed to fail.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 4.2 "Identify the error kernel".

# Verification Notes

- Definition source: Direct adaptation of section 4.2.
- Confidence rationale: HIGH — the concept is stated explicitly with an OS analogy.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
