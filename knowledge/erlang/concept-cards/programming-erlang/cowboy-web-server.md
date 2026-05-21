---
# === CORE IDENTIFICATION ===
concept: Cowboy Web Server
slug: cowboy-web-server

# === CLASSIFICATION ===
category: distribution
subcategory: websockets
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Browsing with Websockets and Erlang"
chapter_number: 18
pdf_page: null
section: "Browsing with Websockets and Erlang"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - cowboy
  - "Erlang web server"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - websocket
extends: []
related:
  - browser-as-erlang-process
  - json-message-bridge
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What web server does the book use for websockets?"
  - "How does Erlang manage the websocket protocol?"
  - "What is cowboy?"
---

# Quick Definition

Cowboy is a simple Erlang web server. In the websockets chapter it manages the socket and the websocket protocol, acting as the bridge that lets Erlang code exchange messages with a browser.

# Core Definition

"To interface the Erlang runtime system to websockets, we run a simple Erlang web server, called cowboy, to manage the socket and the websocket protocol" ("Browsing with Websockets and Erlang", chapter intro). Cowboy is the third component the browser examples require — alongside the code running in the browser and the code running in the Erlang server — and it is "an Erlang server that understands the websockets protocol." Details of installing cowboy are covered in the book's "Third-Party Programs" chapter. The full example framework is in the `ezwebframe` repository, which uses cowboy.

# Prerequisites

- **Websocket** — Cowboy exists in this chapter to manage the websocket protocol.

# Key Properties

1. Cowboy is a simple Erlang web server.
2. It manages the underlying socket and the websocket protocol.
3. It is the third required component for the browser examples (browser code, server code, cowboy).
4. It bridges JSON messages between Erlang processes and the browser.
5. Installation is covered in the book's "Third-Party Programs" chapter; the full framework is in the `ezwebframe` GitHub repository.

# Construction / Recognition

## To use cowboy in the websocket examples:
1. Install cowboy (per the "Third-Party Programs" chapter / `ezwebframe` repo).
2. Run cowboy as the Erlang web server understanding the websocket protocol.
3. Write browser code and Erlang server code; cowboy carries messages between them.

# Context & Application

- **Typical contexts**: Serving websocket-based browser applications from Erlang.
- **Common applications**: Underpins every websocket example in the chapter — clock, interaction, browser shell, chat, IRC.
- **Historical/stylistic notes**: The book treats cowboy as infrastructure — "we'll look at the code that runs in the browser and in the server but not the code for the server itself."

# Examples

**Example 1** ("Browsing with Websockets and Erlang"): cowboy is the Erlang server that "understands the websockets protocol" and is required to run all six chapter examples.

# Relationships

## Related
- **Browser as Erlang process** — Cowboy is the machinery that makes the browser-as-process abstraction work.
- **JSON message bridge** — Cowboy carries JSON messages between Erlang and the browser.

# Common Errors

- **Error**: Expecting the browser examples to run without a websocket-aware server.
  **Correction**: Cowboy (or an equivalent) must be running to manage the websocket protocol.

# Common Confusions

- **Confusion**: Thinking cowboy is part of the standard Erlang distribution.
  **Clarification**: Cowboy is a third-party program; its installation is covered separately.

# Source Reference

Chapter 18: "Browsing with Websockets and Erlang", chapter introduction (cowboy is referenced; its code is not shown in this chapter).

# Verification Notes

- Definition source: Direct quote from chapter introduction.
- Confidence rationale: MEDIUM — cowboy is named and its role described, but the chapter deliberately does not show its code or detail its API.
- Uncertainties: Cowboy's internals are out of scope for this chapter.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction; overwrites prior card.
