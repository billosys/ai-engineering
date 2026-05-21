---
concept: Minimize Trapping Exits
slug: minimize-trapping-exits
category: fault-tolerance
subcategory: processes-servers-messages
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Processes, Servers and Messages"
chapter_number: 5
pdf_page: null
section: "5.12 Trapping exits"
extraction_confidence: high
aliases:
  - "trapping exits"
  - "trap_exit"
  - "don't toggle trapping exits"
prerequisites: []
extends: []
related:
  - one-role-per-process
  - identify-the-error-kernel
contrasts_with: []
answers_questions:
  - "How many processes should trap exit signals?"
  - "Is it acceptable for a process to toggle trapping exits?"
---

# Quick Definition

As few processes as possible should trap exit signals, and a process should either trap exits or not — never "toggle" the setting.

# Core Definition

"As few processes as possible should trap exit signals. Processes should either trap exits or they should not. It is usually very bad practice for a process to 'toggle' trapping exits" (Programming Rules, 5.12).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The number of processes that trap exits is kept as small as possible.
2. A process's exit-trapping status is fixed — either on or off.
3. Toggling exit-trapping at runtime is bad practice.

# Construction / Recognition

## To Apply

1. Let only the few processes that genuinely supervise others trap exits.
2. Set a process's `trap_exit` status once and leave it.

## To Recognize a Violation

1. Many processes trap exits, or a process turns exit-trapping on and off during its life.

# Context & Application

A core process-design principle (section 5).

- **Typical contexts**: supervision — a small set of supervisor processes traps exits.
- **Common applications**: a supervisor trapping exits while its workers do not.

# Examples

The source states the rule directly; no code listing is given.

# Relationships

## Related

- **Each process should only have one "role"** — exit-trapping belongs to the supervisor role.
- **Identify the error kernel** — exit-trapping concentrates in the part of the system that handles failure.

# Common Errors

- **Error**: Toggling `process_flag(trap_exit, ...)` on and off within a process.
  **Correction**: Decide once whether the process traps exits and keep it fixed.

# Common Confusions

- **Confusion**: Thinking widespread exit-trapping makes a system more robust.
  **Clarification**: It does the opposite — robustness comes from a few supervisors trapping exits while most processes simply crash.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 5.12 "Trapping exits".

# Verification Notes

- Definition source: Direct adaptation of section 5.12.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
