---
concept: Use Generic Functions For Servers And Protocol Handlers
slug: use-generic-server-functions
category: otp-behaviours
subcategory: processes-servers-messages
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Processes, Servers and Messages"
chapter_number: 5
pdf_page: null
section: "5.6 Use generic functions for servers and protocol handlers wherever possible"
extraction_confidence: high
aliases:
  - "generic server"
  - "generic protocol handler"
prerequisites: []
extends: []
related:
  - implement-process-in-one-module
  - write-tail-recursive-servers
  - abstract-common-patterns
contrasts_with: []
answers_questions:
  - "Should I write servers from scratch or use a generic server?"
---

# Quick Definition

Use generic server and protocol-handler functions — such as the standard generic server — wherever possible.

# Core Definition

"In many circumstances it is a good idea to use generic server programs such as the generic server implemented in the standard libraries. Consistent use of a small set of generic servers will greatly simplify the total system structure" (Programming Rules, 5.6). The same applies to most protocol-handling software.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Servers are built on generic server programs rather than written from scratch.
2. A small, consistently used set of generic servers simplifies overall system structure.
3. The same generic approach applies to protocol handlers.

# Construction / Recognition

## To Apply

1. Build servers on the standard library's generic server.
2. Reuse a small set of generic handlers across the system.

## To Recognize a Candidate

1. A bespoke server loop is being written where a generic server would serve.

# Context & Application

A core process-design principle (section 5).

- **Typical contexts**: servers and protocol handlers.
- **Common applications**: the standard generic server (the ancestor of OTP's `gen_server`).

# Examples

The source refers to "the generic server implemented in the standard libraries"; no code listing is given.

# Relationships

## Related

- **Implement a process in one module** — generic servers structure the loop while keeping it in one module.
- **Write tail-recursive servers** — generic servers handle tail-recursion correctly for you.
- **Abstract out common patterns of code or behavior** — a generic server is server-pattern abstraction.

# Common Errors

- **Error**: Hand-writing a server loop for each new server.
  **Correction**: Build on a generic server; reuse a small consistent set.

# Common Confusions

- **Confusion**: Thinking generic servers limit flexibility.
  **Clarification**: They simplify the *total* system structure; consistency across servers outweighs bespoke loops.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 5.6 "Use generic functions for servers and protocol handlers wherever possible".

# Verification Notes

- Definition source: Direct adaptation of section 5.6.
- Confidence rationale: HIGH — the rule is stated explicitly.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
