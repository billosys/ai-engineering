---
# === CORE IDENTIFICATION ===
concept: Port Identifier
slug: port-identifier

# === CLASSIFICATION ===
category: data-types
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Data Types"
chapter_number: null
pdf_page: null
section: "Port Identifier"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - port

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-term
  - pid
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an Erlang term?"
---

# Quick Definition
A port identifier identifies an Erlang port, which is a mechanism for communicating with external programs or OS resources. Port identifiers are returned by `open_port/2`.

# Core Definition
The Erlang Reference Manual states: "A port identifier identifies an Erlang port." Port identifiers are returned by `open_port/2` and tested with the `is_port/1` BIF. Ports provide the interface between Erlang processes and external programs or operating system resources (Data Types, "Port Identifier" section).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Identifies an Erlang port
2. Created/returned by `open_port/2`
3. Tested with `is_port/1` BIF
4. Used for communication with external programs and OS resources

# Construction / Recognition
## To Construct/Create:
1. Call `open_port/2` to open a port and receive a port identifier

## To Identify/Recognize:
1. Use `is_port/1` BIF to test whether a term is a port identifier

# Context & Application
Port identifiers are used when Erlang needs to interface with external programs (via port drivers or C nodes), file descriptors, or other OS-level resources. They enable Erlang's approach to interoperability: external programs communicate with Erlang through ports, maintaining the isolation and fault-tolerance properties of the system.

# Examples
The source does not provide shell examples for port identifiers in this section, but references the "Ports and Port Drivers" chapter for details.

# Relationships
## Builds Upon
This is a foundational type with no prerequisites.

## Enables
No direct dependents within this extraction scope.

## Related
- **erlang-term** -- Port identifiers are a kind of term
- **pid** -- Both are identifiers; pids identify processes, ports identify external interfaces

## Contrasts With
No direct contrasts within this source.

# Common Errors
- **Error**: Confusing port identifiers with network ports (TCP/UDP port numbers)
  **Correction**: Erlang port identifiers are handles to port objects, not TCP/UDP port numbers

# Common Confusions
- **Confusion**: Assuming ports are the same as processes
  **Clarification**: Ports are interfaces to external programs; processes are Erlang-level concurrent units. They use different identifier types (port vs. pid).

# Source Reference
Data Types chapter, "Port Identifier" section. References "Ports and Port Drivers" chapter for details.

# Verification Notes
- Definition source: Direct from source ("A port identifier identifies an Erlang port.")
- Confidence rationale: High -- explicit definition, though brief
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned cards
