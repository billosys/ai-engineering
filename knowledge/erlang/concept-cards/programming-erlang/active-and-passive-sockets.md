---
# === CORE IDENTIFICATION ===
concept: Active and Passive Sockets
slug: active-and-passive-sockets

# === CLASSIFICATION ===
category: distribution
subcategory: socket-programming
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Programming with Sockets"
chapter_number: 17
pdf_page: null
section: "Active and Passive Sockets"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "{active, true | false | once}"
  - "active once"
  - "traffic shaping"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-tcp-module
  - message-passing
extends: []
related:
  - inet-module
  - controlling-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between an active and a passive socket?"
  - "How do I control the flow of data to a server?"
  - "What does {active, once} do?"
---

# Quick Definition

Erlang sockets can be opened in active, active-once, or passive mode. Active sockets push incoming data to the controlling process as messages; passive sockets require the process to pull data with `gen_tcp:recv`; active-once delivers exactly one message then must be re-armed.

# Core Definition

"Erlang sockets can be opened in one of three modes: active, active once, or passive. This is done by including an option `{active, true | false | once}` in the `Options` argument" ("Active and Passive Sockets"). With `{active, true}`, "the controlling process will be sent `{tcp, Socket, Data}` messages as data is received. There is no way the controlling process can control the flow of these messages." With `{active, false}` (passive), "the controlling process has to call `gen_tcp:recv(Socket, N)` to receive data" — it controls flow by choosing when to call `recv`. `{active, once}` "creates a socket that is active but only for the reception of one message; after it has received this message, it must be reenabled before it can receive the next message" — done by calling `inet:setopts(Socket, [{active, once}])`.

# Prerequisites

- **gen_tcp module** — The `{active, ...}` option is passed to `gen_tcp:connect` / `gen_tcp:listen`.
- **Message passing** — Active sockets deliver data via the controlling process's mailbox.

# Key Properties

1. `{active, true}` — active (nonblocking): data is pushed as `{tcp, Socket, Data}` messages; flow cannot be controlled.
2. `{active, false}` — passive (blocking): data is pulled with `gen_tcp:recv(Socket, N)`; flow is fully controlled.
3. `{active, once}` — hybrid: active for exactly one message, then must be re-armed with `inet:setopts`.
4. An active server can be flooded by a rogue client and may crash.
5. A passive server cannot wait on more than one socket at a time.
6. `{active, once}` is the best of both worlds and enables traffic shaping.

# Construction / Recognition

## Active (nonblocking) reception:
1. Open with `{active, true}`.
2. Loop receiving `{tcp, Socket, Data}` messages.

## Passive (blocking) reception:
1. Open with `{active, false}`.
2. Loop calling `gen_tcp:recv(Socket, N)`, matching `{ok, B}` or `{error, closed}`.

## Hybrid (partial-blocking) reception:
1. Open with `{active, once}`.
2. Receive one `{tcp, Socket, Data}` message.
3. Call `inet:setopts(Socket, [{active, once}])` to re-arm, then loop.

# Context & Application

- **Typical contexts**: Choosing flow-control behavior for TCP servers.
- **Common applications**: Active for servers known to keep up with demand; passive to block overactive clients; active-once for traffic shaping while still waiting on multiple sockets.
- **Historical/stylistic notes**: `{active, once}` lets a user implement advanced flow control (traffic shaping) and prevents a server from being flooded.

# Examples

**Example 1** ("Active Message Reception"): a server opened with `{active, true}` loops on `{tcp, Socket, Data}` and "cannot control the flow of messages."

**Example 2** ("Passive Message Reception"): a server opened with `{active, false}` calls `gen_tcp:recv(Socket, N)` and "cannot be crashed by an overactive client."

**Example 3** ("The Hybrid Approach"): a server opened with `{active, once}` calls `inet:setopts(Sock, [{active, once}])` after each message.

# Relationships

## Related
- **inet module** — `inet:setopts` re-arms an `{active, once}` socket and switches modes.
- **Controlling process** — Active and active-once sockets deliver messages to the controlling process.

# Common Errors

- **Error**: Using `{active, true}` for a server that cannot keep up with its clients.
  **Correction**: Use `{active, false}` or `{active, once}` so a fast client cannot flood the message buffers and crash the system.

- **Error**: Forgetting to re-arm an `{active, once}` socket.
  **Correction**: Call `inet:setopts(Socket, [{active, once}])` after processing each message.

# Common Confusions

- **Confusion**: Thinking passive mode is always the right choice.
  **Clarification**: In passive mode you can wait for data from only one socket; for servers waiting on multiple sockets, the `{active, once}` hybrid is needed.

# Source Reference

Chapter 17: "Programming with Sockets", section "Active and Passive Sockets", subsections "Active Message Reception", "Passive Message Reception", and "The Hybrid Approach".

# Verification Notes

- Definition source: Direct quotes from "Active and Passive Sockets".
- Confidence rationale: HIGH — the three modes are explicitly defined.
- Uncertainties: None.
- Cross-reference status: Verified; canonical slugs used.
- Re-extraction notes: Fresh extraction; overwrites prior card.
