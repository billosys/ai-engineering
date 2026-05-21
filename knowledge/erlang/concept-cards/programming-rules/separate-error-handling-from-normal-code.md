---
concept: Separate Error Handling And Normal Case Code
slug: separate-error-handling-from-normal-code
category: error-handling
subcategory: error-handling
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Error Handling"
chapter_number: 4
pdf_page: null
section: "4.1 Separate error handling and normal case code"
extraction_confidence: high
aliases:
  - "separate error handling"
  - "let it crash"
  - "normal case code"
prerequisites: []
extends: []
related:
  - dont-program-defensively
  - identify-the-error-kernel
  - one-role-per-process
contrasts_with: []
answers_questions:
  - "Should error-handling code be mixed with normal-case code?"
  - "What should a process do when its normal-case code fails?"
---

# Quick Definition

Don't clutter normal-case code with exception handling — program the normal case, and if it fails, let the process report the error and crash; handle recovery in a different process.

# Core Definition

"Don't clutter code for the 'normal case' with code designed to handle exceptions. As far as possible you should only program the normal case" (Programming Rules, 4.1). If the normal-case code fails, the process should report the error and crash as soon as possible — don't try to fix up the error and continue. Error handling belongs in a different process. Clean separation of recovery code and normal-case code greatly simplifies the overall design.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Normal-case code is written without exception-handling clutter.
2. On failure, a process reports the error and crashes immediately.
3. A process does not try to patch up an error and continue.
4. Error recovery happens in a separate process.
5. A permanent record (error log) of diagnostic information is kept.

# Construction / Recognition

## To Apply

1. Write the worker process to handle only the normal case.
2. Let failures crash it; place recovery logic in a separate (supervising) process.

## To Recognize a Violation

1. Normal-case functions are interleaved with code that patches up and continues from errors.

# Context & Application

A core error-handling principle (section 4).

- **Typical contexts**: worker processes and their supervisors.
- **Common applications**: a worker that crashes on failure while a supervisor restarts it.

# Examples

The source states the principle and cross-references "Each process should only have one 'role'"; no code listing is given.

# Relationships

## Related

- **Do not program "defensively"** — both keep the normal path clean and let failures crash.
- **Identify the error kernel** — recovery belongs to the part of the system that must be correct.
- **Each process should only have one "role"** — recovery is a separate role from normal work.

# Common Errors

- **Error**: Catching an error in the worker and trying to continue.
  **Correction**: Report and crash; recover in a separate process.

# Common Confusions

- **Confusion**: Thinking crashing loses information.
  **Clarification**: The crash is logged; a permanent diagnostic record is kept for later analysis.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 4.1 "Separate error handling and normal case code".

# Verification Notes

- Definition source: Direct adaptation of section 4.1.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
