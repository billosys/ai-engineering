---
# === CORE IDENTIFICATION ===
concept: Process Spawning
slug: process-spawning

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: process-lifecycle
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "The Erlang/OTP platform"
chapter_number: 1
pdf_page: null
section: "1.1.4 Programming with processes in Erlang"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - spawn
  - creating a process
  - spawning

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - pid
  - bif
  - lightweight-process
  - process-termination
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you create a process in Erlang?"
  - "What does spawn return?"
  - "How lightweight is spawning a process?"
---

# Quick Definition

Process spawning is creating a new Erlang process to run a given function. The `spawn` function starts a separate process and returns a fresh pid identifying it.

# Core Definition

Erlang's syntax for creating processes is straightforward. Calling `spawn(io, format, ["erlang!"])` starts a separate process that executes the function call `io:format("erlang!")` and then quits (Chapter 1, section 1.1.4). The `spawn` function has several variants; another takes a single reference to a named zero-argument function. "Every call to `spawn` yields a fresh process identifier that uniquely identifies the new child process," which can then be used to send messages to the child. Spawning in Erlang is cheap — "about as much work as allocating an object in your average object-oriented language" — and Erlang can spawn hundreds of thousands of processes on commodity hardware.

# Prerequisites

- **Erlang process** — spawning is how a process comes into existence.

# Key Properties

1. `spawn` starts a new, separate process.
2. Every `spawn` call returns a fresh, unique pid for the child.
3. The pid is used to send messages to the new process.
4. Spawning is cheap — comparable to allocating an object.
5. `spawn` has several variants (module/function/args form, and a single-function-reference form).

# Construction / Recognition

## To Construct/Create:
1. Choose the code the new process should run (a module:function/args, or a fun).
2. Call `spawn` with that code, e.g. `spawn(io, format, ["erlang!"])`.
3. Capture the returned pid.
4. Use the pid to send the new process messages.

# Context & Application

- **Typical contexts**: Building any concurrent Erlang system; one spawn per concurrent activity.
- **Common applications**: One process per request/connection/task; spawning short-lived workers.
- **Historical/stylistic notes**: `spawn` is one of the auto-imported functions from the `erlang` module, so it needs no module prefix.

# Examples

**Example 1** (section 1.1.4): `spawn(io, format, ["erlang!"])` starts a process that prints "erlang!" on the console and then quits.

**Example 2** (Listing 1.1): A variant of `spawn` gets a single reference to "the function named `ping` that takes zero arguments," and `self()` provides the current pid passed to the child so it knows where to reply.

# Relationships

## Builds Upon
- **Erlang process** — spawning brings a process into being.

## Enables
- **Pid** — spawn yields the new process's pid.
- **Message passing** — the returned pid is the address for messages.

## Related
- **Lightweight process** — spawning is cheap because processes are lightweight.
- **Built-in function** — `spawn` is a BIF in the `erlang` module.

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Hesitating to spawn processes out of fear that they are expensive.
  **Correction**: Spawning is cheap in Erlang — comparable to allocating an object; use processes freely for concurrent activities.

# Common Confusions

- **Confusion**: Thinking `spawn` has only one form.
  **Clarification**: It has several variants; the module/function/args form is the simplest.

# Source Reference

Chapter 1: The Erlang/OTP platform, section 1.1.4 "Programming with processes in Erlang," "Creating a process: spawning" subsection. See also Listing 1.1.

# Verification Notes

- Definition source: Direct adaptation from section 1.1.4.
- Confidence rationale: HIGH — spawning is explicitly demonstrated and described.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs.
- Re-extraction notes: Fresh extraction; no prior card.
