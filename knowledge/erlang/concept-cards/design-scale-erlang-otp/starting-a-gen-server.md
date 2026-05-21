---
# === CORE IDENTIFICATION ===
concept: Starting a Generic Server
slug: starting-a-gen-server

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
section: "Starting a Server"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - start_link
  - "gen_server:start_link/4"
  - init/1 callback

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
extends: []
related:
  - registering-behaviors
  - linking-behaviors
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I start a gen_server?"
  - "What does the init/1 callback return?"
  - "Why is gen_server startup synchronous?"
---

# Quick Definition

A generic server is started with `gen_server:start_link/4`, which spawns and links the process, registers it, and synchronously calls the `init/1` callback to build the server state.

# Core Definition

"Generic servers and other OTP behaviors are started not with the spawn BIFs, but with dedicated functions that do more behind the scenes than just spawn a process" (Cesarini & Vinoski, p. 79). `gen_server:start_link({local,Name},Mod,Args,Opts)` returns `{ok, Pid} | ignore | {error, Reason}`. "When the gen_server process has been spawned, it is registered with the alias Name, subsequently calling the init/1 function in the callback module Mod" (p. 80). "If successful, init/1 callback function returns `{ok, LoopData}`" (p. 81). "Starting a generic server behavior process is a synchronous operation. Only when init/1 callback function returns `{ok, LoopData}` to the server loop does the `gen_server:start_link/4` function return `{ok, Pid}`" (p. 81).

# Prerequisites

- **Gen_server** — Starting a server is the entry point into using the `gen_server` behavior.

# Key Properties

1. `gen_server:start_link/4` takes `{local,Name}` (or other NameScope), `Mod`, `Args`, `Opts`.
2. It returns `{ok, Pid}`, `ignore`, or `{error, Reason}`.
3. The process is spawned, linked, registered, then `init/1` is called in `Mod`.
4. `Args` is passed to `init/1` whole — a list is passed as a list, not splatted into arity.
5. `init/1` returns `{ok, LoopData}` on success, `ignore` or `{stop, Reason}` on failure.
6. Startup is synchronous: `start_link/4` returns only after `init/1` returns `{ok, LoopData}`.
7. A `{timeout, Ms}` option bounds startup time, after which `start_link/4` returns `{error, timeout}`.

# Construction / Recognition

## To Construct:
1. Write a client `start_link/N` that calls `gen_server:start_link({local, Name}, Mod, Args, Opts)`.
2. Implement `init/1` to build the loop data and return `{ok, LoopData}`.
3. On startup failure, return `ignore` or `{stop, Reason}` from `init/1`.

## To Recognize:
1. A `gen_server:start_link/4` call paired with an `init/1` callback returning `{ok, LoopData}`.

# Context & Application

- **Typical contexts**: Bringing a server up, typically under a supervisor.
- **Common applications**: The frequency server's `start/0` calling `gen_server:start_link/4`.
- **Historical/stylistic notes**: Synchronous startup gives deterministic, reproducible startup errors — valuable for troubleshooting.

# Examples

**Example 1** (p. 80): Starting the frequency server:

```erlang
start() ->
    gen_server:start_link({local, frequency}, frequency, [], []).
init(_Args) ->
    Frequencies = {get_frequencies(), []},
    {ok, Frequencies}.
get_frequencies() -> [10,11,12,13,14,15].
```

**Example 2** (p. 80): If you pass `[foo, bar]` as `Args`, "`init([foo,bar])` will be called, not `init(foo, bar)`" — a common Erlang-to-OTP mistake.

# Relationships

## Builds Upon
- **Gen_server** — Starting is the first step of using the behavior.

## Enables
- *(none specific in scope)*

## Related
- **Registering behaviors** — The first argument chooses the registration scope.
- **Linking behaviors** — `start_link` links the server to its parent.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Expecting a list passed as `Args` to be spread across multiple `init` parameters.
  **Correction**: `Args` is passed whole; `init/1` always receives one argument.
- **Error**: Using `spawn`/`spawn_link` to start a behavior.
  **Correction**: Use the behavior's `start`/`start_link` functions, which do more than spawn.

# Common Confusions

- **Confusion**: Thinking server startup is asynchronous.
  **Clarification**: `start_link/4` is synchronous — it returns only after `init/1` completes, giving reproducible startup behavior.

# Source Reference

Chapter 3: Generic Servers, Section "Starting a Server," pages 79-82. See Figure 4-2 (starting a generic server).

# Verification Notes

- Definition source: Direct quotes from pp. 79-81.
- Confidence rationale: HIGH — explicit treatment with a worked example.
- Uncertainties: None.
- Cross-reference status: `registering-behaviors` and `linking-behaviors` are planned Chapter 3 cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
