---
concept: Write Tail-Recursive Servers
slug: write-tail-recursive-servers
category: processes-concurrency
subcategory: processes-servers-messages
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Processes, Servers and Messages"
chapter_number: 5
pdf_page: null
section: "5.9 Write tail-recursive servers"
extraction_confidence: high
aliases:
  - "tail-recursive server"
  - "tail recursion"
  - "server loop memory growth"
prerequisites: []
extends: []
related:
  - use-generic-server-functions
  - flush-unknown-messages
contrasts_with: []
answers_questions:
  - "Why must server loops be tail-recursive?"
  - "What distinguishes a tail-recursive server loop from a non-tail-recursive one?"
---

# Quick Definition

All server loops must be tail-recursive — otherwise the server consumes memory until the system runs out.

# Core Definition

"All servers must be tail-recursive, otherwise the server will consume memory until the system runs out of it" (Programming Rules, 5.9). A recursive `loop()` call must be the last action in its clause; placing any expression (such as a trailing `io:format`) after the `receive` makes the loop non-tail-recursive and causes unbounded stack growth.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. The recursive call to the loop is the last action in each clause.
2. A non-tail-recursive loop grows memory without bound until the system fails.
3. Any expression placed after the `receive` breaks tail-recursion.
4. A generic server library avoids this mistake automatically.

# Construction / Recognition

## To Apply

1. Make `loop()` the final expression in every clause that continues the server.
2. Put any "going down" output *inside* the terminating clause, not after the `receive`.

## To Recognize a Violation

1. An expression (e.g. `io:format("Server going down")`) follows the `receive ... end`.

# Context & Application

A core process-design principle (section 5).

- **Typical contexts**: hand-written server `receive` loops.
- **Common applications**: putting the shutdown message inside the `stop ->` clause.

# Examples

**Example** (from source): the bad `loop/0` ends with `io:format("Server going down")` *after* the `receive` — "NOT tail-recursive"; the good `loop/0` puts that output inside the `stop ->` clause, leaving the `receive` as the clause's last expression.

# Relationships

## Related

- **Use generic functions for servers and protocol handlers** — generic servers make this mistake impossible.
- **Flush unknown messages** — the `Other` clause must also loop tail-recursively.

# Common Errors

- **Error**: Adding cleanup output after the `receive ... end`.
  **Correction**: Move it inside the terminating clause; keep `receive` last.

# Common Confusions

- **Confusion**: Thinking a server loop that "works in testing" is fine.
  **Clarification**: A non-tail-recursive loop leaks memory slowly — it fails only after long uptime, exactly when it matters.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 5.9 "Write tail-recursive servers".

# Verification Notes

- Definition source: Direct adaptation of section 5.9.
- Confidence rationale: HIGH — the rule is stated explicitly with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
