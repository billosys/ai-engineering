---
concept: Encapsulate Message Passing In Interface Functions
slug: encapsulate-message-passing-in-interface-functions
category: api-design
subcategory: processes-servers-messages
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Processes, Servers and Messages"
chapter_number: 5
pdf_page: null
section: "5.10 Interface functions"
extraction_confidence: high
aliases:
  - "interface functions"
  - "hide the message protocol"
prerequisites: []
extends: []
related:
  - tag-messages
  - dont-leak-private-data-structures
  - use-generic-server-functions
contrasts_with: []
answers_questions:
  - "Should other modules send messages to a process directly?"
  - "Why hide a process's message protocol behind interface functions?"
---

# Quick Definition

Use interface functions for talking to a process — encapsulate message passing in functions and keep the message protocol hidden from other modules.

# Core Definition

"Use functions for interfaces whenever possible, avoid sending messages directly. Encapsulate message passing into interface functions" (Programming Rules, 5.10). The message protocol is internal information and should be hidden from other modules. There are cases where this is not possible, but the default is an interface function that performs the send and receive.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Other modules call interface functions, not raw `!`/`receive`.
2. Each interface function encapsulates the send (and any reply receive).
3. The message protocol is internal and hidden from callers.
4. A few cases genuinely cannot be encapsulated this way.

# Construction / Recognition

## To Apply

1. For each request a process accepts, export an interface function that sends the message and receives the reply.
2. Keep the message tuples private to the process's module.

## To Recognize a Violation

1. Another module sends a message directly to the process instead of calling an interface function.

# Context & Application

A core process-design principle (section 5).

- **Typical contexts**: server processes consumed by other modules.
- **Common applications**: a `fileserver` module exporting `open_file/1` that sends `{open_file_request, FileName}` and receives `{open_file_response, Result}`.

# Examples

**Example** (from source): the `fileserver` module exports `open_file/1`, which does `fileserver ! {open_file_request, FileName}` and then `receive {open_file_response, Result} -> Result end` — the protocol stays inside the function.

# Relationships

## Related

- **Tag messages** — interface functions build the tagged request/reply messages.
- **Don't allow private data structure to leak out of a module** — the message protocol is private data kept internal.
- **Use generic functions for servers and protocol handlers** — generic servers provide the call/cast interface mechanism.

# Common Errors

- **Error**: Letting callers `!` messages straight to a process.
  **Correction**: Provide interface functions; keep the message tuples private.

# Common Confusions

- **Confusion**: Thinking the message tuple *is* the API.
  **Clarification**: The message protocol is an internal detail; the interface functions are the API.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 5.10 "Interface functions".

# Verification Notes

- Definition source: Direct adaptation of section 5.10.
- Confidence rationale: HIGH — the rule is stated explicitly with a code example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
