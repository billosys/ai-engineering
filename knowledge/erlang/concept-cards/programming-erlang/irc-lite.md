---
# === CORE IDENTIFICATION ===
concept: IRC Lite
slug: irc-lite

# === CLASSIFICATION ===
category: distribution
subcategory: websockets
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Browsing with Websockets and Erlang"
chapter_number: 18
pdf_page: null
section: "IRC Lite"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "IRC lite"
  - "websocket chat program"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - browser-as-erlang-process
  - browser-server-protocol
  - process
extends: []
related:
  - json-message-bridge
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I build a chat application with websockets and Erlang?"
  - "How are multiple browsers coordinated by an Erlang server?"
  - "What is IRC Lite?"
---

# Quick Definition

IRC Lite is a fully functioning, simplified chat program built in the websockets chapter. It extends the chat widget into a multi-user IRC-style application with an Erlang server coordinating all connected browsers.

# Core Definition

IRC Lite is the chapter's capstone websocket example: "The IRC lite program is a fully functioning chat program" ("Exercises"). It builds on the chat widget — an HTML page with a nickname input, a Join button, a scrolling message area, a user list, and a live input — and extends it "to make a more realistic chat program" ("IRC Lite"). Each browser is an Erlang process; a centralized Erlang server tracks joined users and broadcasts messages to all participants. Messages such as `{'join':nick}` and chat text are sent to Erlang as JSON, and the server pushes `fill_div`/`append_div` commands back to every connected browser.

# Prerequisites

- **Browser as Erlang process** — Each chat participant's browser is modeled as a process.
- **Browser server protocol** — Chat messages and display updates use the `cmd`-based JSON protocol.
- **Process** — The Erlang server and per-browser processes are ordinary Erlang processes.

# Key Properties

1. A fully functioning, simplified chat program built entirely on websockets.
2. Extends the chat widget (nickname input, Join button, scroll area, user list, live input).
3. Uses a centralized Erlang server to coordinate all connected browsers.
4. Each browser is represented by an Erlang process.
5. Browser→server messages (join, chat text) are JSON; server→browser updates are `cmd`-keyed JSON commands.
6. Far simpler than the real IRC protocol — a deliberately reduced version.

# Construction / Recognition

## To build IRC Lite:
1. Create the chat widget HTML (nickname input, Join button, scroll and users divs, live input).
2. On Join, the browser calls `send_json({'join':val})`.
3. The Erlang server registers the user and updates the user list in every browser.
4. On chat input, the browser sends the text; the server broadcasts it as `append_div` commands to all participants.

# Context & Application

- **Typical contexts**: Multi-user real-time browser applications.
- **Common applications**: Demonstrates coordinating many browser processes through one Erlang server.
- **Historical/stylistic notes**: The chapter notes the real IRC protocol "is a lot longer than the version here"; exercises suggest adding authentication and removing the central server in favor of a peer network.

# Examples

**Example 1** ("Creating a Chat Widget", `chat1.html`): the Join button handler runs `send_json({'join':val})` with the nickname.

**Example 2** ("IRC Lite", `chat2.html`): the chat widget is extended with an `idle` div to make the more realistic IRC Lite client.

# Relationships

## Builds Upon
- **Browser server protocol** — IRC Lite is a full application of the `cmd`-based message protocol.

## Related
- **JSON message bridge** — All chat traffic is JSON maps/objects.

# Common Errors

- **Error**: Letting a crashed per-browser process lock the whole application.
  **Correction**: Add error recovery (a chapter exercise notes the `shell1.erl` process is primitive and locks on crash).

# Common Confusions

- **Confusion**: Thinking IRC Lite implements the real IRC protocol.
  **Clarification**: It is a deliberately simplified version; the real IRC protocol specification is far longer.

# Source Reference

Chapter 18: "Browsing with Websockets and Erlang", section "IRC Lite", building on "Creating a Chat Widget"; see also "Exercises".

# Verification Notes

- Definition source: Synthesized from "IRC Lite", "Creating a Chat Widget", and "Exercises".
- Confidence rationale: MEDIUM — the application is described and its widgets shown, but the full server code is presented in pieces / external repository rather than as one definitive listing.
- Uncertainties: Full server implementation details are in the `ezwebframe` repository.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction.
