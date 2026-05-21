---
# === CORE IDENTIFICATION ===
concept: Websocket
slug: websocket

# === CLASSIFICATION ===
category: distribution
subcategory: websockets
tier: foundational

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Browsing with Websockets and Erlang"
chapter_number: 18
pdf_page: null
section: "Browsing with Websockets and Erlang"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - websockets
  - "HTML5 websocket"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - browser-as-erlang-process
  - cowboy-web-server
  - json-message-bridge
contrasts_with:
  - tcp-socket

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a websocket?"
  - "How does a browser communicate with an Erlang program?"
  - "What makes websockets different from ordinary HTTP?"
---

# Quick Definition

A websocket is a bidirectional, asynchronous socket — part of the HTML5 standard — that passes messages between a web browser and an external program such as the Erlang runtime system.

# Core Definition

"Websockets are part of the HTML5 standard and are bidirectional asynchronous sockets that can be used to pass messages between a browser and an external program. In our case, the external program is the Erlang runtime system" ("Browsing with Websockets and Erlang", chapter intro). Websockets make it possible to treat a browser as just another Erlang process: "If we want the browser to do something, we'll send it a message; if something happens within the browser that we need to attend to, the browser will send us a message. All of this is possible thanks to websockets." In the browser, a websocket is created with `new WebSocket(wsUri)` and an `onmessage` callback handles incoming messages.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Part of the HTML5 standard.
2. Bidirectional — messages flow both browser→server and server→browser.
3. Asynchronous — either side can send a message at any time.
4. Connects a browser to an external program (here, the Erlang runtime).
5. Created in JavaScript with `new WebSocket(wsUri)`; messages handled by an `onmessage` callback.
6. In the book's framework, all websocket messages are JSON.

# Construction / Recognition

## To use a websocket (browser side):
1. Create the websocket: `websocket = new WebSocket(wsUri)`.
2. Set `websocket.onmessage = onMessage` to handle incoming messages.
3. Write to the socket (e.g., via `send_json`) to send messages out.

## To use a websocket (Erlang side):
1. Run a websocket-aware web server (cowboy) to manage the protocol.
2. Send and receive messages to/from the browser process.

# Context & Application

- **Typical contexts**: Interactive browser applications driven by a server.
- **Common applications**: The chapter's clock, interaction, browser-shell, chat, and IRC examples all use websockets.
- **Historical/stylistic notes**: Websockets let message passing extend outside Erlang, unifying browser and server into one conceptual framework.

# Examples

**Example 1** ("Creating a Digital Clock"): the browser calls `connect("localhost", 2233, "clock1")`, which opens a websocket to `http://localhost:2233`.

**Example 2** ("The Browser Server Protocol"): `websocket = new WebSocket(wsUri); websocket.onmessage = onMessage;` sets up the websocket and its message callback.

# Relationships

## Related
- **Browser as Erlang process** — Websockets make the browser behave like an Erlang process.
- **cowboy web server** — Manages the websocket protocol on the Erlang side.
- **JSON message bridge** — Websocket messages are encoded as JSON.

## Contrasts With
- **TCP socket** — A raw TCP socket carries an undifferentiated byte stream; a websocket carries discrete bidirectional messages and is an HTML5 browser feature.

# Common Errors

- **Error**: Trying to connect a browser to Erlang without a websocket-aware server.
  **Correction**: Run cowboy (or similar) to manage the websocket protocol on the Erlang side.

# Common Confusions

- **Confusion**: Thinking websockets are just ordinary HTTP requests.
  **Clarification**: A websocket is a persistent, bidirectional, asynchronous channel — either side can send a message at any time, unlike request/response HTTP.

# Source Reference

Chapter 18: "Browsing with Websockets and Erlang", chapter introduction and section "The Browser Server Protocol".

# Verification Notes

- Definition source: Direct quote from chapter introduction.
- Confidence rationale: HIGH — websockets are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction; overwrites prior card.
