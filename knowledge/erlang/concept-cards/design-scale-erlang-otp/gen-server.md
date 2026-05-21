---
# === CORE IDENTIFICATION ===
concept: Generic Server (gen_server)
slug: gen-server

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Generic Servers"
chapter_number: 3
pdf_page: 96
section: "Generic Servers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - gen_server
  - generic server behavior
  - "gen_server: the behavior behind all behaviors"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-behaviors
  - callback-module
  - client-server-design-pattern
extends:
  - client-server-design-pattern
related:
  - behavior-directive
  - starting-a-gen-server
  - synchronous-message-passing
  - asynchronous-message-passing
  - gen-server-termination
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a generic server (gen_server)?"
  - "What callback functions does a gen_server require?"
  - "How do I implement a gen_server callback module?"
---

# Quick Definition

`gen_server` is the OTP behavior that implements the client-server pattern. It supplies all generic client-server code while invoking a developer-written callback module, handling many concurrency corner cases.

# Core Definition

"The `gen_server` module implements the client-server behavior we extracted in the previous chapter. It is part of the standard library application and available as part of the Erlang/OTP distribution. It contains the generic code that interfaces with the callback module through a set of callback functions" (Cesarini & Vinoski, p. 75). "Generic servers are the most commonly used behavior pattern, setting the foundations for other behaviors, all of which can be (and in the early days of OTP were) implemented using this module" (p. 75). The behavior and callback module functions "execute within the scope [of] the same server process." The required callbacks are `init/1`, `handle_call/3`, `handle_cast/2`, and `terminate/2` (plus `handle_info/2` and `code_change/3`).

# Prerequisites

- **OTP behaviors** — `gen_server` is one of the five OTP behaviors.
- **Callback module** — A `gen_server` is driven by a developer-written callback module.
- **Client-server design pattern** — `gen_server` packages exactly this pattern's generic parts.

# Key Properties

1. `gen_server` is the standard-library behavior for client-server processes.
2. It is the most commonly used behavior and the foundation for the others.
3. Behavior and callback functions run in the same server process.
4. Required callbacks: `init/1`, `handle_call/3`, `handle_cast/2`, `terminate/2`; also `handle_info/2`, `code_change/3`.
5. It provides functions to start and stop the server.
6. Message passing is encapsulated in two functions — one synchronous, one asynchronous.
7. It handles concurrency corner cases and offers timeouts (client- and server-side) and software-upgrade support.

# Construction / Recognition

## To Construct:
1. Declare `-behavior(gen_server)` in the callback module.
2. Implement and export `init/1`, `handle_call/3`, `handle_cast/2`, `handle_info/2`, `terminate/2`.
3. Start the server with `gen_server:start_link/4`.
4. Send requests with `gen_server:call/2` and `gen_server:cast/2`.

## To Recognize:
1. A module with `-behavior(gen_server)` and the `handle_call`/`handle_cast` callbacks.

# Context & Application

- **Typical contexts**: Any process modeling the client-server architecture.
- **Common applications**: The frequency server is reimplemented as a `gen_server` callback module.
- **Historical/stylistic notes**: All other OTP behaviors could historically be implemented on top of `gen_server`.

# Examples

**Example 1** (p. 77): The behavior directive and the callback set:

```erlang
-module(frequency).
-behavior(gen_server).
-export([start_link/1, init/1, ...]).
```

**Example 2** (p. 76): The four core callbacks — `init/1` initializes the server, `handle_call/3` handles synchronous requests, `handle_cast/2` handles asynchronous requests, and `terminate/2` handles termination.

# Relationships

## Builds Upon
- **Client-server design pattern** — `gen_server` is that pattern's generic code packaged as a library.

## Enables
- **Synchronous** and **asynchronous message passing** — Provided via `call/2` and `cast/2`.
- **Gen_server termination** — Stopping handled through callback return values.

## Related
- **Behavior directive** — Declares a module as a `gen_server`.
- **Starting a gen_server** — Done with `start_link/4`.

## Contrasts With
- *(none — gen_statem contrast is out of scope for these chapters)*

# Common Errors

- **Error**: Reimplementing client-server concurrency by hand.
  **Correction**: Use `gen_server`; it handles corner cases a hand-written server would miss.

# Common Confusions

- **Confusion**: Thinking each behavior is unrelated to the others.
  **Clarification**: `gen_server` is the foundation — the other behaviors could be (and originally were) built on it.

# Source Reference

Chapter 3: Generic Servers, Section "Generic Servers," pages 75-76. See Figure 4-1 (the callback and behavior modules).

# Verification Notes

- Definition source: Direct quotes from pp. 75-76.
- Confidence rationale: HIGH — explicit definition and callback enumeration.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
