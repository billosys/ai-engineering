---
# === CORE IDENTIFICATION ===
concept: OTP Behaviour
slug: otp-behaviour

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
  - behavior
  - "OTP behavior"
  - generic behaviour

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - message-passing
  - erlang-module
extends: []
related:
  - gen-server
  - supervisor
  - otp-application
  - behaviour-interface
  - behaviour-callback-module
  - behaviour-container
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP behaviour?"
  - "Why do OTP behaviours divide code into a generic and an application-specific part?"
  - "What advantages do OTP behaviours give over plain Erlang processes?"
---

# Quick Definition

An OTP behaviour is a formalization of a common process-oriented programming pattern (such as a server) that splits the pattern into a reusable generic part and an application-specific implementation part, joined by a well-defined interface.

# Core Definition

Behaviours are a way of formalizing common patterns in process-oriented programming. The concept of a server, for example, covers a large portion of all the processes one ever needs to write, and rewriting that code for every new server-like process would be pointless and bug-prone. An OTP behaviour instead takes such a recurring pattern and divides it into two halves: the generic part (provided by OTP as well-tested library code) and the application-specific implementation part (provided by the programmer). These communicate via a simple, well-defined interface (Ch. 3, "Behaviour basics"). The British spelling "behaviour" is used because the Erlang/OTP documentation uses it.

# Prerequisites

- **Process** — Behaviours are templates for processes; understanding processes is required to understand what a behaviour instantiates.
- **Message passing** — The generic and implementation halves, and behaviour containers, coordinate through Erlang messages.
- **Erlang module** — A behaviour implementation is a callback module; the generic library code is also a module.

# Key Properties

1. Divides a recurring process pattern into a generic part and an application-specific part.
2. The two parts communicate through a simple, well-defined interface.
3. The generic library code is well tested and shared across all uses of the behaviour.
4. Standard behaviours include `gen_server`, `gen_event`, `gen_fsm` (worker behaviours), `supervisor`, and `application`.
5. Code built on behaviours fits into the larger OTP framework, gaining features such as supervision for free.

# Construction / Recognition

## To Use a Behaviour:
1. Choose the behaviour that matches your process pattern (e.g. `gen_server` for a server).
2. Write a callback module that exports the functions the behaviour interface requires.
3. Add a `-behaviour(...)` attribute naming the behaviour, so the compiler can check the exports.
4. Call the behaviour library's start function to instantiate a container process using your callback module.

## To Recognize a Behaviour Implementation:
1. Look for a `-behaviour(Name)` module attribute.
2. Look for exported callback functions matching the named behaviour's interface.

# Context & Application

Behaviours are the foundation of writing canonical, concurrent, fault-tolerant OTP code. The book argues that writing pure Erlang processes with message passing correctly and without OTP is an advanced topic to be avoided when possible.

- **Typical contexts**: Servers, supervisors, applications, event handlers, finite state machines.
- **Common applications**: Any long-lived process that should be supervised and follow OTP conventions.

Working with behaviours has four stated advantages: developers get more done with less code; the code is solid because it has well-tested library code at its core; the code fits into the larger OTP framework (gaining supervision for free); and the code is easier to understand because it follows a well-known pattern.

# Examples

**Example 1** (Ch. 3, "Behaviour basics"): The generic server, `gen_server`, is described as the most common and useful kind of OTP behaviour; the `tr_server` module of the chapter is its implementation half.

**Example 2** (Ch. 3): `gen_tcp` is explicitly noted as *not* a behaviour, despite the `gen_` name prefix.

# Relationships

## Builds Upon
- **Process** — A behaviour is a template for processes of a particular type.

## Enables
- **gen_server** — A specific worker behaviour built on the behaviour concept.
- **supervisor** — A behaviour for processes that monitor other processes.
- **otp-application** — A behaviour for packaging and starting subsystems.

## Related
- **behaviour-interface** — The set of callback functions and calling conventions.
- **behaviour-callback-module** — The application-specific implementation half.
- **behaviour-container** — The process running the generic library code.

## Contrasts With
- This is a foundational OTP concept; the book draws no direct contrast.

# Common Errors

- **Error**: Assuming any module named `gen_*` is a behaviour.
  **Correction**: `gen_tcp` is a plain library module, not a behaviour; check for a behaviour interface and the `-behaviour` attribute.

- **Error**: Reimplementing server/supervisor patterns by hand instead of using a behaviour.
  **Correction**: Use the standard behaviour so you get tested library code and OTP integration.

# Common Confusions

- **Confusion**: Believing a behaviour is a single thing.
  **Clarification**: The word "behaviour" is overloaded and can refer to the interface, the implementation (callback module), or the container.

- **Confusion**: Thinking behaviours are like classes that you instantiate once.
  **Clarification**: A behaviour is a template; you may instantiate one or thousands of container processes from the same callback module.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.1.2 "Behaviour basics," including the subsections "Components of a behaviour" and "Instantiating a behaviour." See Listing 3.1 (minimal gen_server behaviour implementation module).

# Verification Notes

- Definition source: Direct adaptation of the "Behaviour basics" prose.
- Confidence rationale: HIGH — the source explicitly and extensively defines the concept.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group and Agent-1 foundational slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
