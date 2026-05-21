---
# === CORE IDENTIFICATION ===
concept: Instantiating a Behaviour
slug: behaviour-instantiation

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
  - starting a behaviour
  - instantiating a behaviour

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-behaviour
  - behaviour-container
extends:
  - behaviour-container
related:
  - process-type
  - gen-server-start-link
  - behaviour-callback-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean to instantiate a behaviour?"
  - "How do you start a new behaviour container process?"
  - "Why are there start and start_link functions in behaviour libraries?"
---

# Quick Definition

Instantiating a behaviour means starting a new container process from a behaviour, using a library API function (typically `start` or `start_link`). The behaviour acts as a template for processes of a particular type.

# Core Definition

The whole point of a behaviour is to provide a template for processes of a particular type. Every behaviour library module has one or more API functions — generally called `start` and/or `start_link` — for starting a new container process; the book calls this *instantiating* the behaviour (Ch. 3, "Instantiating a behaviour"). In some cases an implementation module is written so there can be only one instance at a time; in others, thousands of simultaneous instances run the same code with different data. When callback code runs, it is executed by a container — a process with identity and state, including its mailbox.

# Prerequisites

- **OTP behaviour** — Instantiation produces an instance of a behaviour.
- **Behaviour container** — The thing instantiation creates is a container process.

# Key Properties

1. Performed by calling a behaviour library API function, typically `start` or `start_link`.
2. Produces a new container process running the generic library code.
3. The callback module name is passed to the start function.
4. A behaviour may be instantiated once (singleton) or many times (thousands of instances).
5. All instances run the same code but differ in their individual state.

# Construction / Recognition

## To Instantiate a Behaviour:
1. Choose the start function (`start` or `start_link`).
2. Pass the callback module name and any startup arguments.
3. The library spawns the container, which runs the callback module's `init` and then returns.

# Context & Application

Instantiation is the bridge from a static behaviour template to live processes. The `start_link` variant additionally links the new process to its caller, hooking it into supervision.

- **Typical contexts**: Starting a `gen_server`, a `supervisor`, or any behaviour-based process.
- **Common applications**: Calling `gen_server:start_link/4` from an API function; calling `supervisor:start_link/3` from a `_sup` module.

# Examples

**Example 1** (Ch. 3): `gen_server:start(...,foo,...)` creates a new `gen_server` container that uses `foo` as a callback module.

**Example 2** (Ch. 3, "Singleton process"): `tr_server` is instantiated as a singleton — registered under the name from the `SERVER` macro so only one instance can run at a time.

# Relationships

## Builds Upon
- **Behaviour container** — Instantiation creates a container.

## Enables
- **process-type** — Instances of a behaviour are processes of the same type.

## Related
- **gen-server-start-link** — A specific instantiation function.
- **behaviour-callback-module** — Passed as an argument when instantiating.

## Contrasts With
- This is a process step; the source draws no direct contrast.

# Common Errors

- **Error**: Registering two instances of a singleton behaviour under the same name.
  **Correction**: Processes cannot share a registered name; modify the program if you need multiple instances.

# Common Confusions

- **Confusion**: Thinking a behaviour can be instantiated only once.
  **Clarification**: A behaviour is a template; you may instantiate one or thousands of containers from the same callback module.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.1.2 "Behaviour basics," subsection "Instantiating a behaviour" (and the "Process type" and "Singleton process" sidebars).

# Verification Notes

- Definition source: Direct adaptation of "Instantiating a behaviour."
- Confidence rationale: HIGH — the source explicitly names and defines the term.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
