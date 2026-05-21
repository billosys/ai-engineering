---
# === CORE IDENTIFICATION ===
concept: The Browser as an Erlang Process
slug: browser-as-erlang-process

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
section: "Creating a Digital Clock"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "browser bridge"
  - "browser as a process"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - message-passing
  - websocket
extends: []
related:
  - json-message-bridge
  - browser-server-protocol
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does Erlang treat a web browser?"
  - "How do I control a browser from Erlang?"
  - "Why model the browser as a process?"
---

# Quick Definition

In the websocket framework, Erlang treats a web browser as just another Erlang process: to make the browser do something, Erlang sends it a message; when something happens in the browser, the browser sends Erlang a message.

# Core Definition

"Erlang thinks that the web browser is just another Erlang process, which simplifies our programming model, putting everything into the same conceptual framework" ("Browsing with Websockets and Erlang", chapter intro). "We're going to pretend that a web browser is an Erlang process. If we want the browser to do something, we'll send it a message; if something happens within the browser that we need to attend to, the browser will send us a message." On the Erlang side, a process variable named `Browser` represents the browser, and code like `Browser ! #{cmd => fill_div, id => clock, txt => current_time()}` updates the display. Armstrong calls this "very beautiful code" — "We've tamed the browser. It looks like an Erlang process."

# Prerequisites

- **Process** — The browser is modeled as a process with a pid.
- **Message passing** — Communication uses the `!` send operator and `receive`.
- **Websocket** — The browser-as-process abstraction is implemented over a websocket.

# Key Properties

1. The browser is represented in Erlang by a process (bound to a variable like `Browser`).
2. To change the browser, Erlang sends it a message with `Browser ! Message`.
3. When the user interacts (clicks, types), the browser sends Erlang a message.
4. Server-side code uses ordinary `receive` to handle browser events.
5. Everything — Erlang code and browser code — lives in the same message-passing conceptual framework.
6. Extending the system means adding a small JavaScript function for each new message.

# Construction / Recognition

## To control a browser from Erlang:
1. A freshly spawned Erlang process receives the `Browser` pid (e.g., `start(Browser)`).
2. Send commands with `Browser ! #{cmd => ..., ...}`.
3. Handle user events with `receive {Browser, #{...}} -> ... end`.

# Context & Application

- **Typical contexts**: Building interactive browser applications driven entirely from Erlang.
- **Common applications**: The clock, interaction, browser shell, chat, and IRC examples each have an Erlang process that drives a browser.
- **Historical/stylistic notes**: The abstraction unifies inside-Erlang and outside-Erlang programming — "we don't have one way of doing things inside Erlang and another way of doing things outside Erlang."

# Examples

**Example 1** ("Creating a Digital Clock", `clock1.erl`): `start(Browser)` sends `Browser ! #{cmd => fill_div, id => clock, txt => current_time()}` then loops; a `{Browser, #{clicked => <<"stop">>}}` message moves the process to its idle state.

**Example 2** ("Basic Interaction", `interact1.erl`): `running(Browser)` receives `{Browser, #{entry => <<"input">>, txt => Bin}}` and replies with an `append_div` command.

# Relationships

## Builds Upon
- **Message passing** — The browser abstraction is entirely message passing.

## Related
- **JSON message bridge** — Messages to/from the browser are JSON maps.
- **Browser server protocol** — Defines the structure of the messages exchanged.

# Common Errors

- **Error**: Writing browser-control code in a different style from ordinary Erlang process code.
  **Correction**: Use plain `!` and `receive` — the browser is just a process.

# Common Confusions

- **Confusion**: Thinking the browser literally runs the BEAM.
  **Clarification**: The browser is *modeled as* a process via a websocket; cowboy and `websock.js` bridge the message passing.

# Source Reference

Chapter 18: "Browsing with Websockets and Erlang", chapter introduction and sections "Creating a Digital Clock" and "Basic Interaction".

# Verification Notes

- Definition source: Direct quotes from chapter intro and "Creating a Digital Clock".
- Confidence rationale: HIGH — the abstraction is explicitly and repeatedly stated.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction; overwrites prior card.
