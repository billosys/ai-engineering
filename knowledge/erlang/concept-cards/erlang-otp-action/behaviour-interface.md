---
# === CORE IDENTIFICATION ===
concept: Behaviour Interface
slug: behaviour-interface

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
  - behaviour contract
  - callback interface

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-behaviour
extends:
  - otp-behaviour
related:
  - behaviour-callback-module
  - behaviour-container
  - gen-server
contrasts_with:
  - behaviour-callback-module
  - behaviour-container

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a behaviour interface?"
  - "Which functions make up the gen_server behaviour interface?"
  - "How does the behaviour interface act as a contract?"
---

# Quick Definition

The behaviour interface is the specific set of callback functions and associated calling conventions that a behaviour defines. It is the contract that lets an implementation module plug into the generic behaviour container.

# Core Definition

The behaviour interface is a specific set of functions and associated calling conventions (Ch. 3, "Components of a behaviour"). For example, the `gen_server` behaviour interface contains six functions: `init/1`, `handle_call/3`, `handle_cast/2`, `handle_info/2`, `terminate/2`, and `code_change/3`. The interface is the contract that allows the behaviour implementation (the programmer's code) to leverage the power of the behaviour container.

# Prerequisites

- **OTP behaviour** — The interface is one of the three parts of a behaviour; understanding the behaviour concept is required first.

# Key Properties

1. It is a fixed set of functions with defined calling conventions, not code itself.
2. The `gen_server` interface comprises exactly six functions: `init/1`, `handle_call/3`, `handle_cast/2`, `handle_info/2`, `terminate/2`, `code_change/3`.
3. An implementation module must export every function of the interface to fully conform.
4. The interface functions are commonly called *callbacks*.
5. It acts as the contract between the callback module and the container.

# Construction / Recognition

## To Recognize the Interface:
1. Identify which behaviour the module declares with `-behaviour(...)`.
2. The interface is the documented callback set for that behaviour (six functions for `gen_server`).
3. The compiler warns if an implementation module fails to export an interface function.

# Context & Application

The interface concept lets OTP separate "what must be provided" from "who provides it." Because the interface is fixed, the generic container can call back into any conforming module.

- **Typical contexts**: Defining the contract for `gen_server`, `supervisor`, `application`, `gen_event`, `gen_fsm`.
- **Common applications**: The compiler uses the `-behaviour` attribute plus the interface to validate that all callbacks are exported.

# Examples

**Example 1** (Ch. 3, "Components of a behaviour"): The `gen_server` interface lists `init/1`, `handle_call/3`, `handle_cast/2`, `handle_info/2`, `terminate/2`, `code_change/3`.

**Example 2** (Ch. 3, Listing 3.1): The minimal `gen_server` implementation module exports exactly these six functions, satisfying the interface.

# Relationships

## Builds Upon
- **OTP behaviour** — The interface is one of the three components of a behaviour.

## Enables
- **behaviour-callback-module** — The implementation must satisfy the interface.

## Related
- **behaviour-container** — The container calls back through the interface functions.
- **gen-server** — Defines a concrete six-function interface.

## Contrasts With
- **behaviour-callback-module** — The interface is the contract; the callback module is the code fulfilling it.
- **behaviour-container** — The interface is the contract; the container is the running generic process.

# Common Errors

- **Error**: Omitting one of the interface functions from the callback module.
  **Correction**: Export all interface functions; the compiler issues a warning otherwise, and the module does not fully conform.

# Common Confusions

- **Confusion**: Thinking the interface is the library code.
  **Clarification**: The interface is only the set of functions and calling conventions; the generic code is in the behaviour container's library module.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.1.2 "Behaviour basics," subsection "Components of a behaviour." See Listing 3.1.

# Verification Notes

- Definition source: Direct adaptation of "Components of a behaviour."
- Confidence rationale: HIGH — explicit definition with the six-function enumeration.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
