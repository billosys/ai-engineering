---
# === CORE IDENTIFICATION ===
concept: Behaviour API Section
slug: behaviour-api-section

# === CLASSIFICATION ===
category: api-design
subcategory: module-layout
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Writing a TCP-based RPC service"
chapter_number: 3
pdf_page: null
section: "3.2.3 The API section"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - API section
  - "programmer interface"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - canonical-behaviour-module-layout
  - gen-server
extends:
  - canonical-behaviour-module-layout
related:
  - gen-server-start-link
  - gen-server-call
  - gen-server-cast
  - server-protocol-hiding
  - behaviour-callback-section
contrasts_with:
  - behaviour-callback-section

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the API section of a behaviour module?"
  - "Why are API functions thin wrappers around gen_server library calls?"
  - "What functions belong in a server's API section?"
---

# Quick Definition

The API section is the part of a behaviour module that provides the programmer interface — the functions through which the outside world interacts with the module, typically thin wrappers around `gen_server` library calls.

# Core Definition

The API section is the second canonical section of a behaviour implementation module (Ch. 3, Section 3.2.3). All functionality made available to users of the module — who do not care how it is implemented — is provided through application programming interface (API) functions. For a generic server, users mainly want to start server processes and to send messages and receive answers. The API functions are basically simple wrappers around three primary `gen_server` library calls (`start_link`, `call`, `cast`), hiding those implementation details. A startup function should be placed first in the API section as a point of style.

# Prerequisites

- **Canonical behaviour module layout** — The API section is its second part.
- **gen_server behaviour** — API functions wrap `gen_server` library calls.

# Key Properties

1. It is the second of the four canonical sections.
2. Its functions are exported and carry function-level EDoc (`@doc`, `@spec`).
3. API functions are thin wrappers around `gen_server:start_link`, `call`, and `cast`.
4. The startup function is placed first in the section by convention.
5. The API hides the server protocol from users (see protocol hiding).

# Construction / Recognition

## To Write an API Section:
1. Place the `start`/`start_link` functions first.
2. Add one wrapper function per supported operation.
3. Each wrapper calls `gen_server:call` (for synchronous) or `gen_server:cast` (for asynchronous).
4. Add `@doc` and `@spec` EDoc annotations to each function.

# Context & Application

The API section is the module's face to the world; clients call it without knowing the message protocol or that `gen_server` is involved.

- **Typical contexts**: The public surface of any server module.
- **Common applications**: `tr_server` exposes `start_link/0`, `start_link/1`, `get_count/0`, `stop/0`.

# Examples

**Example 1** (Ch. 3, Listing 3.3 / Table 3.4): The `tr_server` API — `start_link/1`, `start_link/0`, `get_count/0`, `stop/0` — each a wrapper around a `gen_server` library call.

**Example 2** (Ch. 3): `get_count()` wraps `gen_server:call(?SERVER, get_count)`; `stop()` wraps `gen_server:cast(?SERVER, stop)`.

# Relationships

## Builds Upon
- **Canonical behaviour module layout** — The API section is its second part.

## Related
- **gen-server-start-link** / **gen-server-call** / **gen-server-cast** — Library calls wrapped here.
- **server-protocol-hiding** — A key purpose of the API section.

## Contrasts With
- **behaviour-callback-section** — API functions are executed by clients; callbacks are executed by the container.

# Common Errors

- **Error**: Exposing raw `gen_server:call`/`cast` to users instead of wrapping them.
  **Correction**: Provide API functions so the protocol stays hidden and changeable.

# Common Confusions

- **Confusion**: Thinking API functions run in the server process.
  **Clarification**: API code is executed by the calling client process, not the server container.

# Source Reference

Chapter 3: Writing a TCP-based RPC service, Section 3.2.3 "The API section." See Listing 3.3, Tables 3.3 and 3.4, and the "@spec tag" subsection.

# Verification Notes

- Definition source: Direct adaptation of Section 3.2.3.
- Confidence rationale: HIGH — explicit treatment with a dedicated section.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
