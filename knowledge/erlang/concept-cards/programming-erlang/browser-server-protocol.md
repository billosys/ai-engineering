---
# === CORE IDENTIFICATION ===
concept: The Browser/Server Protocol
slug: browser-server-protocol

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
  - "browser server protocol"
  - "cmd protocol"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - websocket
  - json-message-bridge
extends: []
related:
  - browser-as-erlang-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What protocol do Erlang and the browser use to communicate?"
  - "How does a message from Erlang change the browser?"
  - "How are browser commands structured?"
---

# Quick Definition

The browser/server protocol is the simple convention by which Erlang and the browser exchange JSON command messages over a websocket: each message names a `cmd`, and the browser dispatches it to the matching JavaScript function.

# Core Definition

"The Browser server protocol is extremely simple. It makes use of JSON messages sent over a websocket" ("The Browser Server Protocol"). To change something in the browser, Erlang sends a JSON list of command objects, each of which "must contain a key called `cmd`." The browser's `onMessage` callback parses the JSON with `JSON.parse` and calls `do_cmds`, which iterates the list: "For each object `x` in the list, the system checks whether there is a function called `x.cmd`, and if there is, it calls `x.cmd(x)`." So `{cmd:'fill_div', id:'id123', txt:'abc'}` causes `fill_div({cmd:'fill_div', id:'id123', txt:'abc'})` to run. In the other direction, a browser event calls `send_json(x)`, which "encodes the argument `x` as a JSON term and writes it to the websocket"; it arrives in Erlang via `websocket.erl` as a message to the controlling process.

# Prerequisites

- **Websocket** — The protocol's messages travel over a websocket.
- **JSON message bridge** — Messages are JSON (maps in Erlang, objects in the browser).

# Key Properties

1. Messages are JSON, sent over a websocket.
2. Erlang→browser messages are a list of command objects; each object must have a `cmd` key.
3. The browser dispatches each command by calling the JavaScript function named by `cmd`, passing the object itself.
4. Browser→Erlang messages are sent with `send_json(x)` and arrive as messages to the controlling process.
5. The protocol is easily extensible — add a new command by writing a small JavaScript function with the matching name.
6. Unknown commands trigger a `bad_command` alert in the browser.

# Construction / Recognition

## Erlang to browser:
1. Erlang sends a command object such as `{cmd:'fill_div', id:'id123', txt:'abc'}` (as a map).
2. cowboy delivers it as JSON; the browser's `onMessage` parses it.
3. `do_cmds` calls the function named by `cmd`, e.g., `fill_div(o)`.

## Browser to Erlang:
1. A browser event handler calls `send_json({'clicked':txt})`.
2. The JSON is written to the websocket.
3. `websocket.erl` converts it to a frame sent to the controlling process.

# Context & Application

- **Typical contexts**: Defining how a browser application is driven from Erlang.
- **Common applications**: Commands like `fill_div` and `append_div` used by the clock, interaction, shell, chat, and IRC examples.
- **Historical/stylistic notes**: "This method of encoding and evaluating commands is easily extensible so we can add more commands to the interface as necessary."

# Examples

**Example 1** ("Sending a Message from Erlang to the Browser"): Erlang sends `[{cmd:'fill_div', id:'id123', txt:'abc'}]`; the browser runs `fill_div({cmd:'fill_div', id:'id123', txt:'abc'})`.

**Example 2** ("Messages from the Browser to Erlang"): a button click runs `send_json({'clicked':txt})`.

# Relationships

## Builds Upon
- **JSON message bridge** — The protocol is the structured use of JSON messages.

## Related
- **Browser as Erlang process** — The protocol is how the browser-as-process abstraction is realized concretely.

# Common Errors

- **Error**: Sending a command object without a `cmd` key.
  **Correction**: Every command object must include `cmd`; otherwise the browser cannot dispatch it.

- **Error**: Sending a command whose `cmd` names no JavaScript function.
  **Correction**: Define a JavaScript function with the same name as the command before using it.

# Common Confusions

- **Confusion**: Thinking the protocol needs a complex specification.
  **Clarification**: It is deliberately minimal — a list of `cmd`-keyed JSON objects dispatched by name.

# Source Reference

Chapter 18: "Browsing with Websockets and Erlang", section "The Browser Server Protocol", subsections "Sending a Message from Erlang to the Browser" and "Messages from the Browser to Erlang".

# Verification Notes

- Definition source: Direct quotes from "The Browser Server Protocol".
- Confidence rationale: HIGH — the protocol is explicitly and completely described.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction; overwrites prior card.
