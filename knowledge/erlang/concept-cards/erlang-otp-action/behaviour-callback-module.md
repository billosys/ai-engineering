---
# === CORE IDENTIFICATION ===
concept: Behaviour Callback Module
slug: behaviour-callback-module

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
  - behaviour implementation
  - callback module
  - implementation module

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-behaviour
  - behaviour-interface
  - erlang-module
extends:
  - otp-behaviour
related:
  - behaviour-container
  - behaviour-module-header
  - gen-server
contrasts_with:
  - behaviour-interface
  - behaviour-container

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a behaviour callback module?"
  - "What does the -behaviour attribute do?"
  - "How does a callback module conform to a behaviour?"
---

# Quick Definition

A behaviour callback module is the application-specific implementation half of a behaviour: an Erlang module that exports the functions required by the behaviour interface and declares the behaviour it implements.

# Core Definition

A behaviour implementation is a callback module that exports the functions required by the interface (Ch. 3, "Components of a behaviour"). It is the application-specific code that the programmer provides. The implementation module should also contain a `-behaviour(...)` attribute that names the behaviour it implements; this allows the compiler to check that the module exports all the functions of the interface. If any interface function is missing, the compiler issues a warning that the module does not fully conform.

# Prerequisites

- **OTP behaviour** — The callback module is one of the three parts of a behaviour.
- **Behaviour interface** — The callback module must export the functions defined by the interface.
- **Erlang module** — A callback module is an ordinary Erlang module.

# Key Properties

1. It is the application-specific (programmer-provided) half of a behaviour.
2. It exports every callback function required by the behaviour interface.
3. It declares `-behaviour(Name)` so the compiler can verify conformance.
4. The container calls back into this module through the interface functions.
5. One callback module may be used to spawn many container processes of the same type.

# Construction / Recognition

## To Construct a Callback Module:
1. Create a module file whose name follows project naming conventions.
2. Add `-module(Name)` and `-behaviour(BehaviourName)` attributes.
3. Export the behaviour interface functions (and any API functions).
4. Implement each interface function.

## To Recognize One:
1. Look for the `-behaviour(...)` attribute.
2. Confirm the exported functions match the named behaviour's interface.

# Context & Application

The callback module is where the programmer's domain logic lives; everything generic is handled by the container.

- **Typical contexts**: `tr_server` (a `gen_server` callback module), `tr_sup` (a `supervisor` callback module), `tr_app` (an `application` callback module).
- **Common applications**: Naming convention `<application-name>_app` for application callback modules and `<application-name>_sup` for root supervisor modules.

# Examples

**Example 1** (Ch. 3, Listing 3.1): The minimal `gen_server` implementation module — `-behaviour(gen_server)` plus the six exported callbacks — is a complete (if trivial) callback module.

**Example 2** (Ch. 3): When you call `gen_server:start(...,foo,...)`, a new container is created that uses `foo` as the callback module.

# Relationships

## Builds Upon
- **OTP behaviour** — The callback module is the implementation half.

## Enables
- **behaviour-container** — The container needs a callback module to dispatch into.

## Related
- **behaviour-module-header** — The header section of a callback module.
- **gen-server** — A common behaviour whose callback modules are written this way.

## Contrasts With
- **behaviour-interface** — The interface is the contract; the callback module is the code that fulfills it.
- **behaviour-container** — The container runs generic library code; the callback module holds application code.

# Common Errors

- **Error**: Forgetting the `-behaviour(...)` attribute.
  **Correction**: Add it so the compiler can warn about missing callbacks.

- **Error**: Putting code for more than one process type into a single callback module.
  **Correction**: A module should contain code for only one type of process (apart from API code).

# Common Confusions

- **Confusion**: Thinking the callback module runs on its own.
  **Clarification**: Callback code is executed by a container process; the module by itself is just code.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.1.2 "Behaviour basics," subsection "Components of a behaviour." See Listing 3.1.

# Verification Notes

- Definition source: Direct adaptation of "Components of a behaviour."
- Confidence rationale: HIGH — explicit definition in the source.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
