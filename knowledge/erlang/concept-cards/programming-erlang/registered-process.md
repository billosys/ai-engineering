---
# === CORE IDENTIFICATION ===
concept: Registered Process
slug: registered-process

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-naming
tier: intermediate

# === PROVENANCE ===
source: "Programming Erlang, Second Edition"
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Concurrent Programming"
chapter_number: 12
pdf_page: null
section: "Registered Processes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "registered process"
  - "named process"
  - "register/2"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - process-identifier
extends: []
related:
  - message-passing
  - spawn
contrasts_with:
  - process-identifier

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a registered process in Erlang?"
  - "How do I send a message to a process without knowing its Pid?"
  - "What is the difference between registered and unregistered processes?"
---

# Quick Definition

A registered process is one published under an atom name, so any process can send it messages by name without knowing its Pid. Registration is done with the `register/2` BIF.

# Core Definition

Normally only a process's parent knows its Pid, which is secure but inconvenient. "Erlang has a method for publishing a process identifier so that any process in the system can communicate with this process. Such a process is called a registered process" (Armstrong, "Concurrent Programming," "Registered Processes"). Four BIFs manage them: `register(AnAtom, Pid)` registers `Pid` under the name `AnAtom` (failing if the name is already in use); `unregister(AnAtom)` removes the registration; `whereis(AnAtom) -> Pid | undefined` looks up the Pid for a name; and `registered() -> [atom()]` lists all registered names. Once registered, the name can be used directly as a send target: `area ! {rectangle, 4, 5}`. A registered process that dies is automatically unregistered.

# Prerequisites

- **Process** — Registration names a process.
- **Process identifier** — Registration binds an atom to a Pid; you must understand Pids.

# Key Properties

1. A registered process is published under an atom name visible system-wide.
2. `register(AnAtom, Pid)` registers; it fails if `AnAtom` is already registered.
3. `unregister(AnAtom)` removes a registration.
4. `whereis(AnAtom)` returns the Pid, or `undefined` if not registered.
5. `registered()` returns the list of all registered names.
6. A registered name can be used directly as the target of `!`.
7. A registered process that dies is automatically unregistered.

# Construction / Recognition

## To Construct/Create:
1. Spawn the process to obtain its Pid.
2. Call `register(Name, Pid)` with a chosen atom `Name`.
3. Other processes then send messages with `Name ! Message`.

## To Identify/Recognize:
1. A `register(...)` call, or a send to an atom (`area ! ...`) rather than a Pid variable.
2. `whereis(Name)` returning a Pid confirms the name is registered.

# Context & Application

- **Typical contexts**: Long-lived services that many clients must reach without passing Pids around.
- **Common applications**: A registered clock, server, or shared service; sending to a service by a well-known name.
- **Historical/stylistic notes**: The `clock` module registers its ticking process with `register(clock, spawn(fun() -> tick(Time, Fun) end))`, so `clock ! stop` can stop it.

# Examples

**Example 1** ("Registered Processes"): `Pid = spawn(area_server0, loop, [])` then `register(area, Pid)`; afterward `area ! {rectangle, 4, 5}` prints `Area of rectangle is 20`.

**Example 2** ("Registered Processes"): The `clock` module — `start(Time, Fun) -> register(clock, spawn(fun() -> tick(Time, Fun) end)).` and `stop() -> clock ! stop.`

# Relationships

## Builds Upon
- **Process** and **Process identifier** — Registration binds an atom name to a process's Pid.

## Enables
- **Message passing** — A registered name can be used as a `!` target.

## Related
- **Spawn** — The process is spawned, then registered.

## Contrasts With
- **Process identifier** — A Pid is private (known only to the parent); a registered name is public and system-wide.

# Common Errors

- **Error**: Calling `register/2` with a name that is already registered.
  **Correction**: Registration fails for an in-use name; choose a free name or `unregister` the old one first.

- **Error**: Sending to a registered name after the process has died.
  **Correction**: A dead registered process is auto-unregistered; check with `whereis/1` (returns `undefined`).

# Common Confusions

- **Confusion**: Thinking registration is required to communicate with a process.
  **Clarification**: Pids work fine; registration is a convenience for publishing a process system-wide.

- **Confusion**: Believing a registered name persists after the process dies.
  **Clarification**: The system automatically unregisters a registered process when it dies.

# Source Reference

Chapter 12: "Concurrent Programming," section "Registered Processes." EPUB source — no page numbers.

# Verification Notes

- Definition source: Direct adaptation of the four registration BIFs and the `clock` example.
- Confidence rationale: HIGH — registration is defined explicitly with all four BIFs.
- Uncertainties: None.
- Cross-reference status: Canonical slug `registered-process`; cross-refs verified.
- Re-extraction notes: Fresh extraction; new card (no prior file).
