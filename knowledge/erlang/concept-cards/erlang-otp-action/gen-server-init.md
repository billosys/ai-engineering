---
# === CORE IDENTIFICATION ===
concept: gen_server init/1 Callback
slug: gen-server-init

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
section: "3.2.4 The callback function section"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "init/1"
  - initialization callback

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - behaviour-callback-section
extends:
  - behaviour-callback-section
related:
  - gen-server-start-link
  - gen-server-handle-info
  - gen-server-timeout
  - gen-server-handle-call
contrasts_with:
  - gen-server-terminate

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does the gen_server init/1 callback do?"
  - "What should init/1 return?"
  - "How is initial server state set up?"
---

# Quick Definition

`init/1` is the `gen_server` initialization callback, invoked when a container starts. It sets up the process's initial state and returns it to the container.

# Core Definition

`init/1` is the initialization callback, called whenever a new `gen_server` container is started — for example, via `gen_server:start_link/4` (Ch. 3, Section 3.2.4). The `start_link` library function blocks the caller until `init/1` has completed, ensuring the process is fully operational before it processes requests. `init/1` conventionally takes a single argument, which is a list (the argument list passed to `start_link`). It returns a tuple such as `{ok, State}` or `{ok, State, Timeout}`, where `State` is the initial process state (often a record) and the optional third element is a timeout value. A timeout of `0` triggers an immediate timeout, forcing a `handle_info/2` timeout message to run right after initialization.

# Prerequisites

- **gen_server behaviour** — `init/1` is a `gen_server` callback.
- **Behaviour callback function section** — `init/1` lives in the callback section.

# Key Properties

1. Called when a `gen_server` container starts.
2. `start_link` blocks until `init/1` returns.
3. Conventionally takes a single list argument.
4. Returns `{ok, State}` or `{ok, State, Timeout}`.
5. A `0` timeout in the return value triggers an immediate `handle_info/2` timeout.

# Construction / Recognition

## To Write init/1:
1. Match the argument list passed from `start_link` (e.g. `init([Port]) ->`).
2. Perform setup work (create sockets, capture timestamps, etc.).
3. Build the initial `#state{}` record.
4. Return `{ok, State}` — add a `0` timeout to defer slow startup to `handle_info/2`.

# Context & Application

`init/1` is the place to establish everything the server needs before serving requests. Slow setup should be deferred via the timeout trick so the `start_link` caller is not left hanging.

- **Typical contexts**: Opening sockets, creating ETS tables, reading configuration.
- **Common applications**: `tr_server:init([Port])` opens a listening socket and returns `{ok, #state{...}, 0}`; `sc_element:init/1` records start time and lease, returning a timeout for lease management.

# Examples

**Example 1** (Ch. 3): `tr_server:init([Port])` creates a listening socket with `gen_tcp:listen` and returns `{ok, #state{port=Port, lsock=LSock}, 0}` — the `0` forcing an immediate timeout.

**Example 2** (Ch. 6): `sc_element:init/1` converts the start time to Gregorian seconds and fills the state record with value, lease time, and start time, using the third tuple element for the lease timeout.

# Relationships

## Builds Upon
- **Behaviour callback function section** — `init/1` is one of its callbacks.

## Related
- **gen-server-start-link** — `start_link` triggers `init/1`.
- **gen-server-timeout** — A `0` timeout from `init/1` defers startup work.
- **gen-server-handle-info** — Receives the timeout message `init/1` schedules.

## Contrasts With
- **gen-server-terminate** — `init/1` runs at startup; `terminate/2` runs at shutdown.

# Common Errors

- **Error**: Doing slow, blocking work directly in `init/1`.
  **Correction**: Return a `0` timeout and do the slow work in the `handle_info/2` timeout clause.

# Common Confusions

- **Confusion**: Thinking `init/1` can take any argument shape.
  **Clarification**: By convention `init/1` always takes a list, even a single-element one.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.4 "The callback function section." See Listing 3.4 and the "gen_server timeout events" sidebar.

# Verification Notes

- Definition source: Direct adaptation of Section 3.2.4.
- Confidence rationale: HIGH — explicit, detailed treatment in the source.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
