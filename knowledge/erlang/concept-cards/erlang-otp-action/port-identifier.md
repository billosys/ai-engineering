---
# === CORE IDENTIFICATION ===
concept: Port Identifier
slug: port-identifier

# === CLASSIFICATION ===
category: data-types
subcategory: identifiers
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Erlang language essentials"
chapter_number: 2
pdf_page: null
section: "2.2.7 Pids, ports, and references"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - port id

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-term
extends:
  - erlang-term
related:
  - pid
  - reference
  - port
contrasts_with:
  - pid

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a port identifier?"
  - "How does a port differ from a process?"
  - "How is a port identifier displayed?"
---

# Quick Definition

A port identifier is the data type identifying a port — an entity much like a process, except that it communicates with the world outside Erlang and cannot run Erlang code.

# Core Definition

"A *port* is much like a process, except that it can also communicate with the world outside Erlang (and can't do much else — in particular, it can't run any code). Hence, *port identifiers* are closely related to pids" (Chapter 2, section 2.2.7). The shell prints a port identifier in the form `#Port<0.472>`. This card covers the *port identifier* data type as introduced in Chapter 2; the full mechanics of ports for foreign-code integration are treated in a later chapter.

# Prerequisites

- **Erlang term** — a port identifier is a kind of term.

# Key Properties

1. A port identifier identifies a port.
2. A port is much like a process but communicates with the world outside Erlang.
3. A port cannot run Erlang code.
4. Port identifiers are closely related to pids.
5. The shell prints them as `#Port<0.472>`.

# Construction / Recognition

## To Identify/Recognize:
1. A value printed by the shell as `#Port<...>` is a port identifier.
2. It is obtained when a port is opened, not by typing the printed form.
3. It is used like a pid as a communication endpoint.

# Context & Application

- **Typical contexts**: Communicating with external programs, files, or sockets.
- **Common applications**: Integration with foreign code (detailed in a later chapter).
- **Historical/stylistic notes**: Chapter 2 introduces only the identifier data type; the book defers full port mechanics.

# Examples

**Example 1** (section 2.2.7): The shell prints port identifiers in the form `#Port<0.472>`.

**Example 2** (section 2.2.7): A port is described as "much like a process, except that it can also communicate with the world outside Erlang."

# Relationships

## Builds Upon
- **Erlang term** — a port identifier is a term.

## Enables
- Communication with entities outside the Erlang runtime.

## Related
- **Pid** — port identifiers are closely related to pids.
- **Reference** — another identifier data type in the same family.
- **Port** — the full port mechanism (covered in a later chapter).

## Contrasts With
- **Pid** — a pid identifies a process that runs Erlang code; a port identifier identifies a port that talks to the outside world but runs no code.

# Common Errors

- **Error**: Expecting a port to run Erlang code like a process.
  **Correction**: A port only communicates with the world outside Erlang; it cannot run code.

# Common Confusions

- **Confusion**: Treating a port identifier as the same thing as a pid.
  **Clarification**: They are closely related but distinct types; a port has different capabilities than a process.

# Source Reference

Chapter 2: Erlang language essentials, section 2.2.7 "Pids, ports, and references," "Port identifiers" subsection.

# Verification Notes

- Definition source: Direct adaptation from section 2.2.7.
- Confidence rationale: HIGH — the port identifier data type is explicitly described.
- Uncertainties: Full port mechanics are deferred to a later chapter owned by another agent (slug `port`).
- Cross-reference status: `port` is owned by a later-chapter agent; referenced as related.
- Re-extraction notes: Fresh extraction; no prior card. Created as `port-identifier` to avoid colliding with the Chapter 12 `port` card.
