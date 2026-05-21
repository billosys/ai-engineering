---
concept: Implement A Process In One Module
slug: implement-process-in-one-module
category: processes-concurrency
subcategory: processes-servers-messages
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Processes, Servers and Messages"
chapter_number: 5
pdf_page: null
section: "5.1 Implement a process in one module"
extraction_confidence: high
aliases:
  - "one process per module"
  - "process top loop in one module"
prerequisites: []
extends: []
related:
  - use-generic-server-functions
  - one-role-per-process
contrasts_with: []
answers_questions:
  - "How should the code for a process be distributed across modules?"
---

# Quick Definition

Keep the code for a single process — especially its top loop — in one module, and put no more than one kind of process per module.

# Core Definition

"Code for implementing a single process should be contained in one module" (Programming Rules, 5.1). A process may call functions in any library, but the code for its "top loop" must be in a single module — splitting it across modules makes the control flow extremely hard to follow. Conversely, no more than one kind of process should be implemented in a single module. Using generic server libraries to structure the control flow is still fine.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A process's top-loop code lives in one module.
2. The top loop is not split across several modules.
3. At most one kind of process is implemented per module.
4. Generic server libraries may still be used to structure control flow.

# Construction / Recognition

## To Apply

1. Place a process's loop and message handling in a single module.
2. Give each distinct kind of process its own module.

## To Recognize a Violation

1. A process's top loop spans multiple modules, or one module implements several kinds of process.

# Context & Application

A core process-design principle (section 5).

- **Typical contexts**: servers and other long-lived processes.
- **Common applications**: one module per server process.

# Examples

The source states the principle directly; no code listing is given.

# Relationships

## Related

- **Use generic functions for servers and protocol handlers** — generic servers structure the loop without violating this rule.
- **Each process should only have one "role"** — companion process-design rule.

# Common Errors

- **Error**: Spreading a process's loop logic across helper modules.
  **Correction**: Keep the top loop in one module; call libraries for the rest.

# Common Confusions

- **Confusion**: Thinking using a generic server splits the process across modules.
  **Clarification**: The source explicitly allows generic server libraries — they structure, not fragment, the control flow.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 5.1 "Implement a process in one module".

# Verification Notes

- Definition source: Direct adaptation of section 5.1.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
