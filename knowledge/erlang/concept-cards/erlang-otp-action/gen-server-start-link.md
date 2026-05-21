---
# === CORE IDENTIFICATION ===
concept: gen_server:start_link
slug: gen-server-start-link

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
section: "3.2.3 The API section"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_server:start_link/4"
  - start_link

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
  - process-link
extends:
  - gen-server
related:
  - gen-server-init
  - gen-server-call
  - gen-server-cast
  - behaviour-instantiation
  - supervisor
contrasts_with:
  - gen-server-call
  - gen-server-cast

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does gen_server:start_link do?"
  - "How do you start and link to a gen_server?"
  - "What callback does start_link invoke?"
---

# Quick Definition

`gen_server:start_link/4` starts a new `gen_server` container process and simultaneously links to it, blocking the caller until the server's `init/1` callback has completed.

# Core Definition

`gen_server:start_link/4` starts a `gen_server` container process and simultaneously links to it (Ch. 3, Table 3.3). When called, it spawns a new `gen_server` container process, optionally registers it on the local node, and waits until the process has been initialized by running the `init/1` callback of the implementation module before returning to the caller. At that point the server is up, fully initialized, and ready to accept messages. Its associated callback is `Module:init/1`. The four arguments are: the registration spec (e.g. `{local, ?SERVER}`), the callback module (typically `?MODULE`), the argument list passed on to `init/1`, and a list of extra options.

# Prerequisites

- **gen_server behaviour** — `start_link` is a `gen_server` library function.
- **Process link** — `start_link` links the new process to its caller.

# Key Properties

1. Spawns a new `gen_server` container process.
2. Simultaneously links the new process to the caller.
3. Optionally registers the process (e.g. `{local, Name}`).
4. Blocks the caller until `init/1` completes.
5. Its associated callback is `Module:init/1`.
6. The third argument is passed as-is to `init/1`.

# Construction / Recognition

## To Use start_link:
1. Call `gen_server:start_link(RegSpec, Module, Args, Options)`.
2. Pass `{local, ?SERVER}` to register locally under a name.
3. Pass `?MODULE` as the callback module.
4. Pass the data `init/1` needs as a list in `Args`.
5. Wrap the call in an API function so users see only the relevant arguments.

# Context & Application

`start_link` is the standard way to bring up a `gen_server` so it is hooked into OTP's supervision structures — the link is what lets a supervisor know its child has died.

- **Typical contexts**: The body of a server's `start_link` API function; a supervisor's child start MFA.
- **Common applications**: `tr_server:start_link/1` calls `gen_server:start_link({local, ?SERVER}, ?MODULE, [Port], [])`.

# Examples

**Example 1** (Ch. 3): `gen_server:start_link({local, ?SERVER}, ?MODULE, [Port], [])` spawns the `tr_server` container, registers it locally, and runs `init([Port])`.

**Example 2** (Ch. 6): `sc_element:start_link/2` calls `gen_server:start_link/3` without registering a name, because many `sc_element` processes exist.

# Relationships

## Builds Upon
- **gen_server behaviour** — `start_link` is one of its library functions.

## Enables
- **gen-server-init** — `start_link` triggers the `init/1` callback.
- **supervisor** — `start_link` provides the link a supervisor relies on.

## Related
- **behaviour-instantiation** — `start_link` instantiates the behaviour.

## Contrasts With
- **gen-server-call** — `call` sends a synchronous request to an existing server; `start_link` creates one.
- **gen-server-cast** — `cast` sends an asynchronous message; `start_link` creates the server.

# Common Errors

- **Error**: Letting `init/1` do slow work, leaving the `start_link` caller blocked.
  **Correction**: Return a `0` timeout from `init/1` to defer slow startup work to `handle_info/2`.

# Common Confusions

- **Confusion**: Thinking `start_link` returns before the server is ready.
  **Clarification**: It blocks until `init/1` finishes, guaranteeing the server is operational on return.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Sections 3.2.3 and 3.2.4. See Listing 3.3, Tables 3.3 and 3.5.

# Verification Notes

- Definition source: Direct adaptation of Tables 3.3/3.5 and the API discussion.
- Confidence rationale: HIGH — explicit treatment in the source.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slug `process-link` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
