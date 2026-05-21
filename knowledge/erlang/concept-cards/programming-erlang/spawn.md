---
# === CORE IDENTIFICATION ===
concept: Spawn
slug: spawn

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-creation
tier: foundational

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Concurrent Programming"
chapter_number: 12
pdf_page: null
section: "The Concurrency Primitives"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "spawn/1"
  - "spawn/3"
  - "spawn(Fun)"
  - "spawn(Mod, Func, Args)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
extends: []
related:
  - process-identifier
  - message-passing
  - receive
  - spawning-with-mfa-or-fun
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create a new process in Erlang?"
  - "What does spawn return?"
  - "How does spawn relate to message passing?"
---

# Quick Definition

`spawn` is the primitive that creates a new concurrent process. It returns the Pid of the new process, which runs in parallel with the caller.

# Core Definition

`spawn` is one of the three concurrency primitives. In its MFA form, `Pid = spawn(Mod, Func, Args)` "creates a new concurrent process that evaluates `apply(Mod, Func, Args)`. The new process runs in parallel with the caller. `spawn` returns a `Pid` ... You can use a `Pid` to send messages to the process. Note that the function `Func` with arity `length(Args)` must be exported from the module `Mod`." In its fun form, `Pid = spawn(Fun)` "creates a new concurrent process that evaluates `Fun()`" using the current value of the fun, which "does not have to be exported from the module" (Armstrong, "Concurrent Programming," "The Concurrency Primitives"). When a process is spawned with an MFA, "the latest version of the module defining the code is used."

# Prerequisites

- **Process** — `spawn` creates a process; you must understand what a process is.

# Key Properties

1. Two forms: `spawn(Mod, Func, Args)` (MFA) and `spawn(Fun)`.
2. Returns the Pid of the newly created process.
3. The new process runs in parallel with — and independently of — the caller.
4. For the MFA form, `Func` with arity `length(Args)` must be exported from `Mod`.
5. For the fun form, the fun need not be exported.
6. A new process gets a fresh mailbox created together with it.
7. The MFA form picks up the latest compiled version of the module's code.

# Construction / Recognition

## To Construct/Create:
1. Decide on the function the new process should run.
2. Call `spawn(Mod, Func, Args)` (export `Func/length(Args)` from `Mod`), or `spawn(fun() -> ... end)`.
3. Capture the returned Pid to send the process messages later.

## To Identify/Recognize:
1. A `spawn(...)` call whose result is bound to a Pid creates a process.
2. `?MODULE` as the first MFA argument is the idiomatic way to spawn a function in the current module.

# Context & Application

- **Typical contexts**: Starting a server's receive loop; creating workers; building client/server systems.
- **Common applications**: `spawn(Mod, loop, [])` to start a server; `spawn(fun() -> ... end)` for ad-hoc tasks.
- **Historical/stylistic notes**: A common concurrent template begins `start() -> spawn(?MODULE, loop, []).` Spawning is extremely fast (microseconds per process).

# Examples

**Example 1** ("The Concurrency Primitives"): `Pid = spawn(area_server0, loop, [])` creates a process evaluating `area_server0:loop()`, returning `<0.36.0>`.

**Example 2** ("Processes Are Cheap"): `spawn(fun() -> wait() end)` — the fun form, where `wait()` need not be exported.

**Example 3** ("Implementing a Timer"): `start(Time, Fun) -> spawn(fun() -> timer(Time, Fun) end).` spawns a timer process running a local function.

# Relationships

## Builds Upon
- **Process** — `spawn` is the means of bringing a process into existence.

## Enables
- **Process identifier** — `spawn` returns the Pid used to address the new process.
- **Message passing** — Once spawned, the process is sent messages via its Pid.

## Related
- **receive** — The spawned function typically contains a `receive` loop.
- **Spawning with MFAs or funs** — The choice between the two `spawn` forms.

## Contrasts With
- None.

# Common Errors

- **Error**: Using `spawn(Mod, Func, Args)` where `Func/length(Args)` is not exported from `Mod`.
  **Correction**: Export the spawned function, or use the `spawn(Fun)` form.

- **Error**: Assuming `spawn` returns the function's result.
  **Correction**: `spawn` returns a Pid immediately; the new process runs in parallel — results come back via messages.

# Common Confusions

- **Confusion**: Thinking `spawn` blocks until the new process finishes.
  **Clarification**: `spawn` returns at once; the spawned process runs concurrently with the caller.

- **Confusion**: Believing the two `spawn` forms are interchangeable.
  **Clarification**: They differ for dynamic code upgrade — the MFA form supports it, the fun form does not (see "Spawning with MFAs or funs").

# Source Reference

Chapter 12: "Concurrent Programming," sections "The Concurrency Primitives," "Processes Are Cheap," and "Spawning with MFAs or Funs." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct quotes of the two `spawn` forms from "The Concurrency Primitives."
- Confidence rationale: HIGH — both forms are defined explicitly.
- Uncertainties: None.
- Cross-reference status: Canonical slug `spawn`; cross-refs verified.
- Re-extraction notes: Fresh extraction; prior card for this slug overwritten.
