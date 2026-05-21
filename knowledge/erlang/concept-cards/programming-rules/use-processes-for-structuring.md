---
concept: Use Processes For Structuring The System
slug: use-processes-for-structuring
category: processes-concurrency
subcategory: processes-servers-messages
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Processes, Servers and Messages"
chapter_number: 5
pdf_page: null
section: "5.2 Use processes for structuring the system"
extraction_confidence: high
aliases:
  - "processes as structuring elements"
  - "don't overuse processes"
prerequisites: []
extends: []
related:
  - one-process-per-concurrent-activity
  - implement-process-in-one-module
contrasts_with: []
answers_questions:
  - "When should I use a process instead of a function call?"
---

# Quick Definition

Processes are the basic system-structuring element — but don't use a process and message passing where a plain function call would do.

# Core Definition

"Processes are the basic system structuring elements. But don't use processes and message passing when a function call can be used instead" (Programming Rules, 5.2). Processes structure the system; they are not a substitute for ordinary sequential function calls.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Processes are the primary structuring element of an Erlang system.
2. A process is not used where a function call suffices.
3. Message passing carries overhead and complexity a function call does not.

# Construction / Recognition

## To Apply

1. Use a process to model a structural or concurrent element of the system.
2. Use a plain function call for sequential computation.

## To Recognize a Violation

1. A process and message round-trip is used where a direct function call would do.

# Context & Application

A core process-design principle (section 5).

- **Typical contexts**: deciding whether a unit of work needs its own process.
- **Common applications**: keeping pure computation as function calls, reserving processes for structure.

# Examples

The source states the principle directly; no code listing is given.

# Relationships

## Related

- **Assign exactly one parallel process to each true concurrent activity** — the positive criterion for when a process *is* warranted.
- **Implement a process in one module** — companion process-design rule.

# Common Errors

- **Error**: Spawning a process for work that is purely sequential.
  **Correction**: Use a function call; reserve processes for structural/concurrent elements.

# Common Confusions

- **Confusion**: Thinking more processes always means a better Erlang design.
  **Clarification**: Processes structure the system, but overuse adds needless message-passing complexity.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 5.2 "Use processes for structuring the system".

# Verification Notes

- Definition source: Direct adaptation of section 5.2.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
