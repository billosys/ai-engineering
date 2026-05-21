---
# === CORE IDENTIFICATION ===
concept: gen_server Behaviour
slug: gen-server

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: gen-server
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introducing OTP"
chapter_number: 22
pdf_page: null
section: "Getting Started with gen_server"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "gen_server"
  - "generic server behaviour"
  - "-behaviour(gen_server)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - generic-server
  - behaviour
  - callback-module
extends:
  - generic-server
related:
  - gen-server-callbacks
  - gen-server-call
  - gen-server-cast
  - handle-info
  - supervisor
contrasts_with:
  - gen-event
  - generic-server

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a gen_server?"
  - "How does gen_server relate to the client/server pattern?"
  - "How do I write a gen_server callback module?"
---

# Quick Definition

`gen_server` is the standard OTP behaviour for implementing a client/server. You write a callback module exporting six functions; `gen_server` supplies all the concurrency, error handling, and the message loop.

# Core Definition

The Erlang module `gen_server` "is the kind of logical conclusion of a succession of successively sophisticated servers" (Programming Erlang, "The Road to the Generic Server"). It is the first major OTP behaviour. All the error handling and nonfunctional behaviour is factored into the generic part; the callback module is written in "regular sequential code." A `gen_server` is started with `gen_server:start_link(Name, Mod, InitArgs, Opts)`, which creates a generic server named `Name` with callback module `Mod`. Clients interact through `gen_server:call/2` (synchronous, returns a value) and `gen_server:cast/2` (asynchronous). The behaviour has been in industrial use since 1998, with hundreds of servers per product.

# Prerequisites

- **The generic server** — `gen_server` is the production conclusion of the hand-built generic servers.
- **Behaviour** — `gen_server` is an OTP behaviour, declared with `-behaviour(gen_server)`.
- **Callback module** — a `gen_server` is incomplete without its callback module.

# Key Properties

1. Declared in the callback module with `-behaviour(gen_server).`.
2. The callback module must export six functions: `init/1`, `handle_call/3`, `handle_cast/2`, `handle_info/2`, `terminate/2`, `code_change/3`.
3. Started with `gen_server:start_link({local, Name}, Mod, InitArgs, Opts)` for a local server, or `{global, Name}` for a cluster-wide server.
4. The generic part handles concurrency and error handling; the callback is pure sequential code.
5. Three-point recipe: decide a callback module name, write the interface functions, write the six callbacks.
6. Not a universal panacea — if the client-server pattern feels awkward, rethink the abstraction.

# Construction / Recognition

## To Construct a gen_server:
1. Decide on a callback module name (e.g. `my_bank`).
2. Write interface routines that each make exactly one `gen_server` call (e.g. `deposit(Who, Amount) -> gen_server:call(?MODULE, {add, Who, Amount}).`).
3. Start from the `gen_server` mini template and add `-behaviour(gen_server).`.
4. Fill in `init/1` to return `{ok, State}` and `handle_call/3` clauses matching each request term.
5. Start it with `gen_server:start_link({local, ?SERVER}, ?MODULE, [], [])`.

## To Recognize:
1. A module with `-behaviour(gen_server).` and the six exported callbacks is a gen_server.
2. Interface functions delegating to `gen_server:call`/`gen_server:cast` indicate a gen_server.

# Context & Application

- **Typical contexts**: Any client/server interaction; the back-end servers of a system.
- **Common applications**: `my_bank` (a payment system), `prime_server`, and `area_server` in the next chapter are all gen_servers.
- **Historical/stylistic notes**: In industrial use since 1998. An Emacs erlang-mode skeleton can generate the template; the book also includes it in an appendix.

# Examples

**Example 1** ("Getting Started with gen_server"): `my_bank` interface routines, each one `gen_server` call:

```erlang
start() -> gen_server:start_link({local, ?SERVER}, ?MODULE, [], []).
new_account(Who) -> gen_server:call(?MODULE, {new, Who}).
deposit(Who, Amount) -> gen_server:call(?MODULE, {add, Who, Amount}).
```

**Example 2** ("Getting Started with gen_server"): `my_bank:init/1` opens an ETS table as the server state: `init([]) -> {ok, ets:new(?MODULE,[])}.`

# Relationships

## Builds Upon
- **The generic server** — `gen_server` is the polished, production form of the hand-built servers.
- **Behaviour** — `gen_server` is one OTP behaviour.

## Enables
- **gen_server callbacks** — the six functions a gen_server callback module must supply.
- **Supervisor** — supervisors typically watch over gen_server workers.

## Related
- **gen_server:call** — synchronous request to a gen_server.
- **gen_server:cast** — asynchronous message to a gen_server.
- **handle_info** — callback for spontaneous messages.

## Contrasts With
- **gen_event** — handles events and pluggable handlers rather than a single client/server.
- **The generic server** — the hand-rolled precursor, not production-grade.

# Common Errors

- **Error**: Forgetting to define `?SERVER` before using it in `start_link`.
  **Correction**: The macro `?SERVER` is not defined by default; add `-define(SERVER, ?MODULE).`.

- **Error**: Doing slow synchronous I/O inside `handle_call`, blocking all other callers.
  **Correction**: Return `noreply` and delegate the reply to a spawned process for long-running work.

# Common Confusions

- **Confusion**: Thinking `gen_server` fits every problem.
  **Clarification**: The book warns it "is not a universal panacea"; if the client-server pattern feels awkward, modify the abstraction.

- **Confusion**: Believing the callback module needs concurrency code.
  **Clarification**: `gen_server` supplies the concurrency; the callback is pure sequential code.

# Source Reference

Chapter 22: Introducing OTP, sections "The Road to the Generic Server", "Getting Started with gen_server", "The gen_server Callback Structure", "Filling in the gen_server Template", "Digging Deeper". No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes and code from "Getting Started with gen_server" and surrounding sections.
- Confidence rationale: HIGH — `gen_server` is defined, templated, and worked through in full.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card. Canonical slug `gen-server` per extraction instructions.
