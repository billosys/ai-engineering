---
# === CORE IDENTIFICATION ===
concept: Behaviour Container
slug: behaviour-container

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: behaviour-fundamentals
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
  - behaviour process
  - generic process

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-behaviour
  - behaviour-interface
  - erlang-process
extends:
  - otp-behaviour
related:
  - behaviour-callback-module
  - behaviour-instantiation
  - process-type
  - gen-server
contrasts_with:
  - behaviour-callback-module
  - behaviour-interface

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a behaviour container?"
  - "What does the behaviour container do for you?"
  - "Where does the generic behaviour code run?"
---

# Quick Definition

A behaviour container is a process that runs the generic library code of a behaviour and uses a callback module to handle application-specific work. It handles the hard parts of concurrent, fault-tolerant OTP code.

# Core Definition

The container is the third part of a behaviour: a process that runs code from a library module and uses implementation callback modules to handle application-specific things (Ch. 3, "Components of a behaviour"). Technically a container could consist of multiple closely cooperating processes, but usually there is only one. The library module has the same name as the behaviour and contains the generic code, including functions to start new containers. Behaviour containers handle much of what is challenging about writing canonical, concurrent, fault-tolerant OTP code: synchronous messaging, process initialization, process cleanup and termination, and hooks into larger OTP patterns such as code change and supervision trees. "Container" is the authors' own term; the OTP documentation usually speaks only of "the process."

# Prerequisites

- **OTP behaviour** — The container is one of the three parts of a behaviour.
- **Behaviour interface** — The container calls back into the callback module through the interface.
- **Process** — A container is itself a process with identity and state, including a mailbox.

# Key Properties

1. It is a process (occasionally several) running generic library code.
2. The library module name matches the behaviour name (e.g. the `gen_server` module).
3. It dispatches into a callback module through the behaviour interface functions.
4. It handles synchronous messaging, initialization, cleanup, termination, code change, and supervision hooks.
5. It is a living thing with its own identity and state, like an object but running code in parallel.

# Construction / Recognition

## To Create a Container:
1. Call the behaviour library's start function (e.g. `gen_server:start_link/4`).
2. Pass the callback module name as an argument.
3. The library spawns a new container process and runs the callback module's `init` function.

## To Recognize One:
1. In introspection tools, a container process is often executing generic framework code (e.g. `gen_server:loop/6`), not your own code.

# Context & Application

The container is what makes "more done with less code" possible: all the boilerplate of reliable concurrent programming lives in the container's library code.

- **Typical contexts**: Every running `gen_server`, `supervisor`, or `application` instance is a container.
- **Common applications**: When debugging, remember that a process's current function is often inside the container's framework code, so the registered name matters more for identification.

# Examples

**Example 1** (Ch. 3): For `gen_server`, the generic code sits in the `gen_server` module in `stdlib`; calling `gen_server:start(...,foo,...)` creates a new container that uses `foo` as its callback module.

**Example 2** (Ch. 5, Pman): The `tr_sup` process shows its current function as `gen_server:loop/6` — the container's framework code — because supervisors are built on `gen_server`.

# Relationships

## Builds Upon
- **OTP behaviour** — The container is the generic-running part.

## Enables
- **behaviour-instantiation** — Instantiating a behaviour creates a container.

## Related
- **behaviour-callback-module** — The container dispatches into a callback module.
- **process-type** — Containers of the same behaviour are processes of the same type.
- **gen-server** — A common behaviour whose container is the `gen_server` module.

## Contrasts With
- **behaviour-callback-module** — The container runs generic code; the callback module is application code.
- **behaviour-interface** — The interface is the contract; the container is the running process.

# Common Errors

- **Error**: Expecting a behaviour process to be executing your code at all times.
  **Correction**: When idle, a behaviour container hangs in its generic loop (e.g. `gen_server:loop/6`).

# Common Confusions

- **Confusion**: Thinking "the process" and "the callback module" are the same.
  **Clarification**: The container is the process; the callback module is just code it dispatches into.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.1.2 "Behaviour basics," subsection "Components of a behaviour" (and the "Containers" sidebar). Container observation in Chapter 5, Section 5.2 "Pman."

# Verification Notes

- Definition source: Direct adaptation of "Components of a behaviour" and the "Containers" sidebar.
- Confidence rationale: HIGH — explicit definition; "container" is the authors' own term and they say so.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
