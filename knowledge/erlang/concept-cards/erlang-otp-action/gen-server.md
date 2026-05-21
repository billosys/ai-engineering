---
# === CORE IDENTIFICATION ===
concept: gen_server Behaviour
slug: gen-server

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: generic-server
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Writing a TCP-based RPC service"
chapter_number: 3
pdf_page: null
section: "3.1.2 Behaviour basics"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - gen_server
  - generic server
  - "generic server behaviour"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-behaviour
  - behaviour-interface
  - behaviour-callback-module
  - message-passing
extends:
  - otp-behaviour
related:
  - gen-server-start-link
  - gen-server-call
  - gen-server-cast
  - gen-server-init
  - gen-server-handle-call
  - gen-server-handle-cast
  - gen-server-handle-info
  - gen-server-terminate
  - gen-server-code-change
  - supervisor
contrasts_with:
  - supervisor

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the gen_server behaviour?"
  - "What is the most common OTP behaviour?"
  - "What does gen_server do for you?"
---

# Quick Definition

`gen_server` is the OTP behaviour for implementing a generic server process: a long-lived process that holds state and responds to synchronous and asynchronous requests. It is the most common and useful OTP behaviour.

# Core Definition

`gen_server` (the generic server) is described as the most fundamental, most powerful, and most frequently used of the OTP behaviours (Ch. 3 introduction). It captures the general pattern of a server — a process that holds state and answers requests — and splits it into the generic `gen_server` library module (in `stdlib`) and a programmer-supplied callback module. The `gen_server` behaviour interface consists of six callback functions: `init/1`, `handle_call/3`, `handle_cast/2`, `handle_info/2`, `terminate/2`, and `code_change/3`. The library takes care of synchronous messaging, process initialization, cleanup and termination, and supervision hooks.

# Prerequisites

- **OTP behaviour** — `gen_server` is one specific behaviour.
- **Behaviour interface** — `gen_server` defines a six-function interface.
- **Behaviour callback module** — A `gen_server` is implemented as a callback module.
- **Message passing** — `gen_server` clients and servers communicate through (wrapped) messages.

# Key Properties

1. It is the most common and useful OTP behaviour.
2. Its interface has six callbacks: `init/1`, `handle_call/3`, `handle_cast/2`, `handle_info/2`, `terminate/2`, `code_change/3`.
3. The generic code lives in the `gen_server` module in `stdlib`.
4. It supports synchronous requests (`call`), asynchronous messages (`cast`), and out-of-band messages (`info`).
5. It blocks the caller of `start_link` until `init/1` finishes, so the server is fully operational before serving requests.
6. `supervisor` is itself built on top of `gen_server`.

# Construction / Recognition

## To Implement a gen_server:
1. Create a module with `-behaviour(gen_server)`.
2. Export the six callback functions plus any API functions.
3. Implement `init/1` to set up initial state.
4. Implement `handle_call/3`, `handle_cast/2`, `handle_info/2` for the protocol.
5. Implement `terminate/2` and `code_change/3`.
6. Provide API wrapper functions around `gen_server:start_link`, `call`, and `cast`.

## To Recognize One:
1. Look for the `-behaviour(gen_server)` attribute and the six exported callbacks.

# Context & Application

`gen_server` is the workhorse of OTP. The chapter builds the `tr_server` TCP RPC server on it; Chapter 6 builds the `sc_element` cache-storage processes on it.

- **Typical contexts**: Any process that holds state and answers requests; system services; per-value worker processes.
- **Common applications**: RPC servers, cache elements, registries, connection handlers.

# Examples

**Example 1** (Ch. 3, Listing 3.1): The minimal `gen_server` implementation module — `-behaviour(gen_server)` plus the six callbacks returning trivial values.

**Example 2** (Ch. 3): The `tr_server` module is a full `gen_server` implementing a TCP-based RPC server.

**Example 3** (Ch. 6): Each `sc_element` cache process is a `gen_server` keeping its value in state.

# Relationships

## Builds Upon
- **OTP behaviour** — `gen_server` is a concrete behaviour.

## Enables
- **supervisor** — The `supervisor` behaviour is built on `gen_server`.

## Related
- **gen-server-start-link** / **gen-server-call** / **gen-server-cast** — Library functions for the API.
- **gen-server-init** through **gen-server-code-change** — The six callbacks.

## Contrasts With
- **supervisor** — `gen_server` is a worker behaviour doing actual work; `supervisor` only monitors and restarts children (though supervisors are internally built on `gen_server`).

# Common Errors

- **Error**: Having a `gen_server` call its own API functions from within a callback.
  **Correction**: A server cannot call itself synchronously — the request is queued behind the current callback, causing a deadlock.

# Common Confusions

- **Confusion**: Thinking `gen_tcp` is a behaviour because of its `gen_` name.
  **Clarification**: `gen_tcp` is a plain library module; only modules like `gen_server` are behaviours.

# Source Reference

Chapter 3: Writing a TCP-based RPC service — introduction and Sections 3.1.2 through 3.2.4. See Listings 3.1–3.5, Tables 3.3–3.5, and the "A server should not call itself" sidebar in Section 3.3.

# Verification Notes

- Definition source: Synthesized from the chapter introduction and "Behaviour basics."
- Confidence rationale: HIGH — the source explicitly and repeatedly defines and uses `gen_server`.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
