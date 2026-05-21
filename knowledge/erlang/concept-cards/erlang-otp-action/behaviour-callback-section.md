---
# === CORE IDENTIFICATION ===
concept: Behaviour Callback Function Section
slug: behaviour-callback-section

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: module-layout
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
  - callback section
  - "callback function section"
  - "behaviour interface section"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - canonical-behaviour-module-layout
  - behaviour-interface
  - gen-server
extends:
  - canonical-behaviour-module-layout
related:
  - gen-server-init
  - gen-server-handle-call
  - gen-server-handle-cast
  - gen-server-handle-info
  - behaviour-api-section
contrasts_with:
  - behaviour-api-section

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the callback function section of a behaviour module?"
  - "Where are the gen_server callbacks implemented?"
  - "How do API functions relate to callback functions?"
---

# Quick Definition

The callback function section is the part of a behaviour module that implements the callback functions required by the behaviour interface — the functions the container calls back into to do the real work.

# Core Definition

The callback function section is the third canonical section of a behaviour implementation module (Ch. 3, Section 3.2.4). Each `gen_server` library function used in the API corresponds to a specific callback specified by the `gen_server` behaviour interface, and these callbacks must be implemented here. The container calls back into these functions: `gen_server:start_link/4` triggers `Module:init/1`; `gen_server:call/2` triggers `Module:handle_call/3`; `gen_server:cast/2` triggers `Module:handle_cast/2`. The `handle_info/2` callback corresponds to no library function — it handles out-of-band messages. This is where most of the real work is done.

# Prerequisites

- **Canonical behaviour module layout** — The callback section is its third part.
- **Behaviour interface** — The section implements the interface's callbacks.
- **gen_server behaviour** — The callbacks belong to the `gen_server` interface.

# Key Properties

1. It is the third of the four canonical sections.
2. Its functions are exported (the interface requires it); EDoc is optional.
3. Each callback corresponds to a `gen_server` library function — except `handle_info/2`.
4. `init/1` ← `start_link/4`; `handle_call/3` ← `call/2`; `handle_cast/2` ← `cast/2`.
5. The callbacks' return tuples tell the container what to do next.

# Construction / Recognition

## To Write the Callback Section:
1. Implement `init/1` to set up initial process state.
2. Implement `handle_call/3` for synchronous protocol messages.
3. Implement `handle_cast/2` for asynchronous protocol messages.
4. Implement `handle_info/2` for out-of-band messages and timeouts.
5. Implement `terminate/2` and `code_change/3`.

# Context & Application

The callback section holds the domain logic; the container drives it. Reading code, this section tells you how the server reacts to each message.

- **Typical contexts**: The body of any `gen_server`/`supervisor`/`application` callback module.
- **Common applications**: `tr_server`'s callbacks (Listings 3.4–3.5) parse and execute RPC requests.

# Examples

**Example 1** (Ch. 3, Table 3.5): The library-function-to-callback mapping, with `handle_info/2` marked N/A because it has no associated library function.

**Example 2** (Ch. 3, Listings 3.4–3.5): `tr_server`'s six callbacks — `init/1` creating the listening socket, `handle_call/3` returning the request count, `handle_cast/2` stopping the server, `handle_info/2` accepting connections and handling TCP data.

# Relationships

## Builds Upon
- **Canonical behaviour module layout** — The callback section is its third part.

## Related
- **gen-server-init** / **gen-server-handle-call** / **gen-server-handle-cast** / **gen-server-handle-info** — The callbacks implemented here.

## Contrasts With
- **behaviour-api-section** — Callbacks run in the container process; API functions run in the client.

# Common Errors

- **Error**: Failing to export a callback function.
  **Correction**: The behaviour interface requires every callback to be exported; the compiler warns otherwise.

# Common Confusions

- **Confusion**: Thinking every callback has a matching library function.
  **Clarification**: `handle_info/2` has no corresponding `gen_server` library function — it handles out-of-band messages.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.4 "The callback function section." See Listings 3.4 and 3.5 and Table 3.5.

# Verification Notes

- Definition source: Direct adaptation of Section 3.2.4.
- Confidence rationale: HIGH — explicit treatment with a dedicated section.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
