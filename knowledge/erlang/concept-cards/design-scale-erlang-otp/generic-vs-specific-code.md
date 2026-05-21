---
# === CORE IDENTIFICATION ===
concept: Generic Versus Specific Code
slug: generic-vs-specific-code

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: behavior-concept
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Behaviors"
chapter_number: 2
pdf_page: 72
section: "Design Patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - generic and specific code
  - reusable versus project-specific code

# === TYPED RELATIONSHIPS ===
prerequisites:
  - client-server-design-pattern
extends: []
related:
  - otp-behaviors
  - callback-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the difference between generic and specific code?"
  - "Which parts of a client-server program are reusable?"
---

# Quick Definition

Generic code is the part of a client-server program that does not change from one implementation to another and can be packaged into reusable libraries; specific code is the project-specific business logic.

# Core Definition

Behaviors rest on splitting code into two parts. "Sending a client request to a server will be generic. It can be done in a uniform manner across any client-server architecture, irrespective of what the server does. What will be specific, however, are the contents of that message" (Cesarini & Vinoski, p. 57). Generic includes spawning the server, storing loop data, sending requests, sending replies, receiving replies, and stopping the server; specific includes initializing the server state, the loop data itself, the client requests, handling client requests, the contents of the server reply, and cleaning up (Table 3-1, p. 58). Crucially, "while the functions and BIFs might be considered generic, expressions in the functions and arguments passed to them aren't" (p. 61).

# Prerequisites

- **Client-server design pattern** — The generic/specific split is identified by analyzing a concrete client-server program.

# Key Properties

1. Generic code is uniform across all client-server implementations.
2. Specific code is the project's business logic.
3. Generic: spawning the server, storing loop data, sending requests, sending replies, receiving replies, stopping the server.
4. Specific: initializing server state, the loop data, the client requests, handling them, the reply contents, cleaning up.
5. A generic function may still take specific arguments — the mechanism is generic, the data is specific.
6. Separating the two lets generic parts be packaged as reusable libraries.

# Construction / Recognition

## To Construct:
1. Take a working client-server module.
2. Ask of each expression: would this change in another client-server program?
3. Mark unchanging mechanisms as generic, changing logic and data as specific.
4. Move generic code to a library module, leaving specific code in the callback module.

## To Recognize:
1. Spawning, registering, looping, and the message protocol are generic; module name, request types, handlers, and state are specific.

# Context & Application

- **Typical contexts**: Refactoring a hand-written server toward an OTP behavior.
- **Common applications**: Extracting the frequency server's generic parts into a `server` module.
- **Historical/stylistic notes**: This analysis is the conceptual core of why OTP behaviors exist.

# Examples

**Example 1** (p. 58, Table 3-1): The generic/specific table — e.g., "Spawning the server" is generic while "Initializing the server state" is specific; "Sending requests to the server" is generic while "The client requests" are specific.

**Example 2** (p. 61): In `start() -> register(frequency, spawn(frequency, init, []))`, the spawning/registering mechanism is generic, but the registered name `frequency`, the callback module, and the `init` arguments are specific.

# Relationships

## Builds Upon
- **Client-server design pattern** — The pattern whose code is being classified.

## Enables
- **Callback module** — The specific code becomes the callback module.
- **OTP behaviors** — Packaging the generic code yields a behavior library.

## Related
- *(none additional)*

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Classifying a function as fully generic because its name is uniform.
  **Correction**: A generic function can still receive specific arguments — separate the mechanism from the data.

# Common Confusions

- **Confusion**: Thinking the message protocol's contents are generic because the protocol structure is.
  **Clarification**: The protocol *envelope* (e.g., `{request, Pid, Message}`) is generic, but the `Message` contents are specific.

# Source Reference

Chapter 2: Behaviors, Section "Design Patterns" and "Extracting Generic Behaviors," pages 56-67. See Table 3-1 (client-server generic and specific code).

# Verification Notes

- Definition source: Direct quotes from pp. 57-61 and Table 3-1.
- Confidence rationale: HIGH — explicit, repeated treatment with a summary table.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
