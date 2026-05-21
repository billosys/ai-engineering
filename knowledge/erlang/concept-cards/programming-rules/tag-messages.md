---
concept: Tag Messages
slug: tag-messages
category: processes-concurrency
subcategory: processes-servers-messages
tier: intermediate
source: "Program Development Using Erlang — Programming Rules and Conventions"
source_slug: programming-rules
authors: "Klas Eriksson, Mike Williams, Joe Armstrong"
chapter: "Processes, Servers and Messages"
chapter_number: 5
pdf_page: null
section: "5.7 Tag messages"
extraction_confidence: high
aliases:
  - "tag messages"
  - "tagged messages"
prerequisites: []
extends: []
related:
  - flush-unknown-messages
  - encapsulate-message-passing-in-interface-functions
  - document-message-data-structures
contrasts_with: []
answers_questions:
  - "Why should all inter-process messages be tagged?"
  - "How should synchronous reply messages be tagged?"
---

# Quick Definition

Tag all messages — it makes the order of `receive` clauses less important and makes adding new messages safe.

# Core Definition

"All messages should be tagged. This makes the order in the receive statement less important and the implementation of new messages easier" (Programming Rules, 5.7). An untagged message like `{Mod, Func, Args}` creates a conflict when a new message such as `{get_status_info, From, Option}` is added below it. For synchronous messages, the reply should be tagged with a new atom describing it — e.g. an incoming `get_status_info` produces a reply tagged `status_info` — which also makes debugging easier.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Every message carries a tag (typically a leading atom).
2. Tagging makes `receive`-clause order less significant.
3. New message types can be added without clashing with existing patterns.
4. Synchronous replies are tagged with a distinct atom from the request.

# Construction / Recognition

## To Apply

1. Send `{execute, Mod, Func, Args}` rather than a bare `{Mod, Func, Args}`.
2. Tag the reply distinctly: request `get_status_info` → reply `status_info`.

## To Recognize a Violation

1. A `receive` clause matches an untagged tuple like `{Mod, Func, Args}`.

# Context & Application

A core process-design principle (section 5).

- **Typical contexts**: server `receive` loops.
- **Common applications**: a loop matching `{execute, ...}` and `{get_status_info, From, Option}`.

# Examples

**Example** (from source): the bad loop matches `{Mod, Funcs, Args}`, which conflicts once `{get_status_info, From, Option}` is added; the good loop matches `{execute, Mod, Funcs, Args}` and `{get_status_info, From, Option}`.

# Relationships

## Related

- **Flush unknown messages** — both keep `receive` loops robust as message sets grow.
- **Encapsulate message passing into interface functions** — interface functions construct the tagged messages.
- **Document all the principle data structures in messages** — tagged tuples are the documented message structure.

# Common Errors

- **Error**: Sending an untagged tuple whose shape happens to be unique today.
  **Correction**: Add a leading tag atom so future messages cannot collide with it.

# Common Confusions

- **Confusion**: Thinking a distinctively shaped tuple needs no tag.
  **Clarification**: A new message of the same shape will silently match the wrong clause; the tag prevents that.

# Source Reference

"Program Development Using Erlang — Programming Rules and Conventions", section 5.7 "Tag messages".

# Verification Notes

- Definition source: Direct adaptation of section 5.7.
- Confidence rationale: HIGH — the rule is stated explicitly with a bad/good example.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
