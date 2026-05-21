---
# === CORE IDENTIFICATION ===
concept: Callback Module
slug: callback-module

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: otp-foundations
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introducing OTP"
chapter_number: 22
pdf_page: null
section: "The Road to the Generic Server"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "callback"
  - "handler module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp
  - pattern-matching
extends: []
related:
  - behaviour
  - generic-server
  - gen-server
  - gen-server-callbacks
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a callback module?"
  - "What code goes in a callback module versus the behaviour?"
---

# Quick Definition

A callback module is the user-written module that parameterizes an OTP behaviour, supplying the functional, problem-specific code. It contains pure sequential code — no spawn, send, receive, or register.

# Core Definition

A callback module is the module passed to a behaviour (or to a hand-written generic server) that provides the problem-specific functions the framework calls back into. In the book's first server, `server1:start(Name, Mod)` is parameterized with `Mod`, the callback module, and the server's loop calls `Mod:init()` and `Mod:handle(Request, State)`. The book stresses: "The callback had no code for concurrency, no spawn, no send, no receive, and no register. It is pure sequential code — nothing else. This means we can write client-server models without understanding anything about the underlying concurrency models" (Programming Erlang, "The Road to the Generic Server"). By OTP convention, the callback module also contains the client interface routines that callers use.

# Prerequisites

- **OTP** — the callback module exists to parameterize an OTP behaviour.
- **Pattern matching** — callback functions like `handle/2` dispatch on the shape of the request term.

# Key Properties

1. Contains only pure sequential code — no concurrency primitives.
2. Supplies the functional part of the problem; the behaviour supplies the nonfunctional part.
3. By OTP convention, also holds the client-facing interface routines in the same module.
4. The same callback module can run under different generic servers, changing nonfunctional behaviour without changing functional code.
5. Named modules are passed by atom (the module name) to the behaviour's start function.

# Construction / Recognition

## To Write a Callback Module:
1. Decide on a module name (e.g. `name_server`, `my_bank`).
2. Write the interface routines clients will call.
3. Write the callback functions the behaviour requires (e.g. `init`, `handle`).
4. Keep all code sequential — let the behaviour handle concurrency.

## To Recognize:
1. A module exporting `init/...` and `handle.../...` functions but no `spawn`/`receive` is a callback module.
2. A module passed as the `Mod` argument to a behaviour's `start`/`start_link` is the callback module.

# Context & Application

- **Typical contexts**: Every OTP server, supervisor, and event handler has a callback module.
- **Common applications**: `name_server` is the callback for `server1`; `my_bank` is the callback for `gen_server`.
- **Historical/stylistic notes**: The book demonstrates swapping the callback module of `server3` on the fly (`new_name_server`) without stopping the server.

# Examples

**Example 1** ("The Road to the Generic Server"): `name_server.erl` is a callback for `server1` — it exports `init/0`, `add/2`, `find/1`, `handle/2`:

```erlang
%% callback routines
init() -> dict:new().
handle({add, Name, Place}, Dict) -> {ok, dict:store(Name, Place, Dict)};
handle({find, Name}, Dict) -> {dict:find(Name, Dict), Dict}.
```

**Example 2** ("Server 2: A Server with Transactions"): "Note that the callback module for this server is exactly the same as the callback module we used for `server1`. By changing the server and keeping the callback module constant, we can change the nonfunctional behavior of the callback module."

# Relationships

## Builds Upon
- **OTP** — the callback module exists to plug into an OTP behaviour.

## Enables
- **Behaviour** — a behaviour is incomplete until parameterized by a callback module.
- **gen_server** — the gen_server callback module supplies `init/1`, `handle_call/3`, etc.

## Related
- **Generic server** — the hand-written precursor that first introduces the callback idea.
- **gen_server callbacks** — the specific callback functions a gen_server callback module exports.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Hard-compiling the server's registered name into the callback module.
  **Correction**: This prevents reuse of the callback under a differently named server, as the book notes when it has to copy `name_server` to `name_server1`.

- **Error**: Adding `spawn`/`receive` logic to the callback module.
  **Correction**: Concurrency belongs in the behaviour; keep the callback purely sequential.

# Common Confusions

- **Confusion**: Thinking the callback module *is* the server.
  **Clarification**: The callback module supplies functions; the running server process is created and driven by the behaviour.

- **Confusion**: Believing the interface routines and callback routines must be in separate modules.
  **Clarification**: The usual OTP convention combines both in the same module.

# Source Reference

Chapter 22: Introducing OTP, sections "The Road to the Generic Server" (Server 1, Server 2, Server 3). No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quotes and code from "The Road to the Generic Server".
- Confidence rationale: HIGH — the source explicitly defines and demonstrates callback modules.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
