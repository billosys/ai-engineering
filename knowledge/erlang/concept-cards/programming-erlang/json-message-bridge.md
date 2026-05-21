---
# === CORE IDENTIFICATION ===
concept: JSON Message Bridge to the Browser
slug: json-message-bridge

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
section: "The Browser Server Protocol"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "JSON over websockets"
  - "maps as JSON messages"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - websocket
  - browser-as-erlang-process
extends: []
related:
  - browser-server-protocol
  - cowboy-web-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are messages exchanged between Erlang and the browser?"
  - "How do Erlang maps relate to JavaScript objects?"
  - "What format do websocket messages use in the browser examples?"
---

# Quick Definition

The JSON message bridge is the convention that all messages between Erlang and the browser are JSON: on the Erlang side they appear as maps, and in the browser they appear as JavaScript objects, with cowboy translating between the two.

# Core Definition

"To simplify things, we assume that all messages between Erlang and the browser are JSON messages. On the Erlang side of the application these messages appear as Erlang maps ... and in the browser these messages appear as JavaScript objects" ("Browsing with Websockets and Erlang", chapter intro). When Erlang sends a map such as `#{cmd => fill_div, id => clock, txt => <<"16:30:52">>}`, it is converted into the JavaScript object `{cmd:'fill_div', id:'clock', txt:'16:30:52'}` and dispatched in the browser. In the browser, `send_json(x)` "encodes the argument `x` as a JSON term and writes it to the websocket"; on arrival in Erlang it becomes a map. "The small conceptual gap between the Erlang and JavaScript representations of the messages simplifies programming."

# Prerequisites

- **Websocket** — JSON messages travel over the websocket connection.
- **Browser as Erlang process** — The bridge is what makes the browser look like a process exchanging messages.

# Key Properties

1. Every message between Erlang and the browser is JSON.
2. On the Erlang side a message is a map; in the browser it is a JavaScript object.
3. Map keys become object keys (e.g., `cmd`, `id`, `txt`).
4. The conceptual gap between Erlang maps and JavaScript objects is small, simplifying programming.
5. The browser's `send_json(x)` encodes a value as JSON and writes it to the websocket.
6. Incoming browser messages are decoded with `JSON.parse` in the browser and arrive as maps in Erlang.

# Construction / Recognition

## To send a message Erlang → browser:
1. Construct a map with a `cmd` key, e.g., `#{cmd => fill_div, id => clock, txt => Text}`.
2. Send it to the `Browser` process with `Browser ! Map`.
3. cowboy encodes it as JSON; the browser's `onMessage` callback parses and dispatches it.

## To send a message browser → Erlang:
1. In a browser event handler, call `send_json({'clicked':txt})`.
2. The JSON is written to the websocket and arrives in Erlang as a map.

# Context & Application

- **Typical contexts**: Browser applications driven from Erlang via websockets.
- **Common applications**: The chapter's clock, interaction, shell, chat, and IRC examples all exchange JSON maps.
- **Historical/stylistic notes**: The book notes the code uses maps, introduced in Erlang R17.

# Examples

**Example 1** ("Creating a Digital Clock"): Erlang sends `Browser ! #{cmd => fill_div, id => clock, txt => <<"16:30:52">>}`.

**Example 2** ("Messages from the Browser to Erlang"): a button click evaluates `send_json({'clicked':txt})` which arrives in Erlang as a map.

# Relationships

## Related
- **Browser server protocol** — Defines the structure of the JSON command messages carried by the bridge.
- **cowboy web server** — Performs the websocket/JSON translation between Erlang and the browser.

# Common Errors

- **Error**: Sending a JSON command object without a `cmd` key.
  **Correction**: Each command object must contain a `cmd` key so the browser can dispatch it.

# Common Confusions

- **Confusion**: Thinking Erlang and the browser must use different message representations.
  **Clarification**: The bridge keeps them nearly identical — a map on one side, a JavaScript object on the other.

# Source Reference

Chapter 18: "Browsing with Websockets and Erlang", chapter introduction and section "The Browser Server Protocol".

# Verification Notes

- Definition source: Direct quotes from chapter intro and "The Browser Server Protocol".
- Confidence rationale: HIGH — the JSON/map/object correspondence is explicitly stated.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction.
