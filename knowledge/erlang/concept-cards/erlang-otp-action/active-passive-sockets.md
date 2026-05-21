---
# === CORE IDENTIFICATION ===
concept: Active and Passive Sockets
slug: active-passive-sockets

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: networking
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding an HTTP interface to the cache"
chapter_number: 11
pdf_page: null
section: "11.2.2. Implementing a generic web server behaviour"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "{active, true}"
  - "{active, false}"
  - "{active, once}"
  - socket active mode

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - tcp-server-pattern
  - gen-web-server
  - tcp-interface-application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between active and passive sockets in Erlang?"
  - "What does {active, once} do?"
  - "Why can an active socket cause an out-of-memory situation?"
---

# Quick Definition

An Erlang socket can be active (incoming data arrives as messages automatically), passive (the owner must read explicitly), or `{active, once}` (active for one message, then automatically passive).

# Core Definition

A `gen_tcp` socket's `active` option controls how incoming data is delivered. In active mode (`{active, true}`), the Erlang runtime reads data from the socket as quickly as it can and passes it on as Erlang messages to the socket's owner — clean and event-driven, but with no flow control: a fast sender can grow the message queue until memory is exhausted. In passive mode (`{active, false}`), the owner process must explicitly read data with `gen_tcp:recv`, which is less Erlang-like but lets TCP's built-in flow control block the sender. The third option, `{active, once}`, puts the socket in active mode until one message is received, then automatically reverts to passive mode — combining event-driven style with flow control ("Erlang and OTP in Action," Ch. 11, Sections 11.2.2 and 11.2.2 "The gws_server module").

# Prerequisites

- **Process** — Active-mode delivery sends data to the socket's owning process.

# Key Properties

1. `{active, true}` — incoming data is auto-delivered as `{tcp, Socket, Data}` messages; no flow control.
2. `{active, false}` — the owner must call `gen_tcp:recv` explicitly; TCP flow control blocks fast senders.
3. `{active, once}` — active for exactly one message, then automatically passive; re-enabled with `inet:setopts(Socket, [{active, once}])`.
4. A dedicated socket from `accept` inherits the listening socket's active setting.
5. Active mode risks out-of-memory if a client sends faster than the receiver consumes.
6. `{active, once}` is the recommended compromise: event-driven code plus flow control.

# Construction / Recognition

## To Construct/Create:
1. Pass `{active, true|false|once}` in the option list to `gen_tcp:listen` or `gen_tcp:accept`.
2. For `{active, once}`, after handling each message call `inet:setopts(Socket, [{active, once}])` to re-arm.

## To Identify/Recognize:
1. Look for the `active` option in `gen_tcp:listen`/`inet:setopts` calls, or repeated `{active, once}` re-arming in a receive loop.

# Context & Application

- **Typical contexts**: Choosing a flow-control strategy for a TCP server.
- **Common applications**: `tcp_interface` uses `{active, true}` for simplicity; `gen_web_server` uses `{active, once}` for flow control while keeping event-driven code.
- **Historical/stylistic notes**: Active mode "has more of an Erlang/OTP feel" but lacks flow control.

# Examples

**Example 1** (Section 11.2.2 "The gws_server module"): A loop calls `inet:setopts(Socket, [{active,once}])`, waits for `{tcp, Socket, Data}`, handles it, then loops back to re-enable `{active, once}`.

**Example 2** (Listing 11.6): The `gws_connection_sup` opens its listening socket with `{active, false}` along with `binary`, `{packet, http_bin}`, and `{reuseaddr, true}`.

# Relationships

## Builds Upon
- **Process** — Active sockets deliver data to a process mailbox.

## Enables
- **gen_web_server** — Uses `{active, once}` to handle HTTP with flow control.

## Related
- **Concurrent TCP server pattern** — Socket mode is a key design choice in TCP servers.
- **tcp_interface application** — Uses active-mode sockets.

# Common Errors

- **Error**: Using `{active, true}` for a server exposed to untrusted, fast clients.
  **Correction**: Use `{active, once}` (or passive mode) so TCP flow control prevents mailbox-driven memory exhaustion.

- **Error**: Forgetting to re-arm `{active, once}` after handling a message.
  **Correction**: Call `inet:setopts(Socket, [{active, once}])` in every clause that should continue reading.

# Common Confusions

- **Confusion**: Thinking `{active, once}` stays active.
  **Clarification**: It delivers exactly one message and then automatically reverts to passive mode until re-armed.

# Source Reference

Chapter 11: "Adding an HTTP interface to the cache," Section 11.2.2 — sidebar "TCP flow control and active/passive sockets" and subsection "The gws_server module and the use of {active, once}."

# Verification Notes

- Definition source: Direct adaptation of the flow-control sidebar and the `{active, once}` subsection.
- Confidence rationale: HIGH — the book explicitly defines all three modes and their trade-offs.
- Uncertainties: None.
- Cross-reference status: `process` owned by Agent 1.
- Re-extraction notes: Fresh extraction; no prior card existed.
