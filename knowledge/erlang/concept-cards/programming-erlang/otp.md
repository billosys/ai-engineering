---
# === CORE IDENTIFICATION ===
concept: OTP (Open Telecom Platform)
slug: otp

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: otp-foundations
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Introducing OTP"
chapter_number: 22
pdf_page: null
section: "Introducing OTP"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Open Telecom Platform"
  - "OTP libraries"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - process
  - message-passing
extends: []
related:
  - behaviour
  - gen-server
  - supervisor
  - otp-application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is OTP?"
  - "What concepts are needed before using OTP behaviours?"
---

# Quick Definition

OTP (the Open Telecom Platform) is an application operating system shipped with the standard Erlang distribution: a set of libraries, behaviours, and procedures for building large-scale, fault-tolerant, distributed applications.

# Core Definition

OTP "stands for the Open Telecom Platform. The name is actually misleading, because OTP is far more general than you might think. It's an application operating system and a set of libraries and procedures used for building large-scale, fault-tolerant, distributed applications" (Programming Erlang, "Introducing OTP"). It was developed at the Swedish telecom company Ericsson and is used within Ericsson for building fault-tolerant systems. The standard Erlang distribution contains the OTP libraries. OTP also bundles ready-made tools — a web server, an FTP server, a CORBA ORB, and telecom-protocol implementations (H248, SNMP, an ASN.1-to-Erlang cross-compiler) — all written in Erlang.

# Prerequisites

- **Process** — OTP behaviours wrap long-lived processes; you must understand processes before using OTP.
- **Message passing** — OTP servers and supervisors communicate by sending and receiving messages.

# Key Properties

1. Ships as part of the standard Erlang distribution — no separate install.
2. Provides reusable application frameworks called *behaviours*.
3. Supplies fault tolerance, scalability, and dynamic code upgrade through the behaviours themselves.
4. Originated at Ericsson for fault-tolerant telecom systems and is used in commercial products.
5. Far more general than its "telecom" name suggests — used for any large-scale fault-tolerant system.

# Construction / Recognition

## To Use OTP:
1. Identify the part of your problem that fits a standard pattern (a server, a supervisor, an event handler).
2. Pick the matching OTP behaviour (`gen_server`, `supervisor`, `gen_event`, `application`).
3. Write a callback module supplying only the functional, problem-specific code.
4. Let the behaviour handle the nonfunctional concerns (concurrency, error handling, code upgrade).

## To Recognize:
1. Code that declares `-behaviour(...)` is participating in the OTP framework.
2. A system started with `erl -boot start_sasl` is running the OTP production environment.

# Context & Application

- **Typical contexts**: Production back-end systems, fault-tolerant servers, distributed applications.
- **Common applications**: Building servers, supervision trees, error logging, alarm handling, and packaged applications.
- **Historical/stylistic notes**: Developed at Ericsson; used in industrial products since 1998. Erlang's nine-9s reliability claim rests on correct use of the OTP behaviours.

# Examples

**Example 1** ("Introducing OTP"): The book introduces OTP by stating it contains "a complete web server, an FTP server, a CORBA ORB," and telecom-protocol tools, all written in Erlang.

**Example 2** ("Introducing OTP"): The chapter promises to study one OTP behaviour, `gen_server`, in detail — the central practical entry point into OTP.

# Relationships

## Builds Upon
- **Process** — OTP behaviours are structured wrappers around processes.

## Enables
- **Behaviour** — the core abstraction OTP provides.
- **gen_server** — the most commonly used OTP behaviour.
- **Supervisor** — the OTP fault-tolerance mechanism.
- **OTP application** — the unit of packaging in OTP.

## Related
- **Message passing** — the communication substrate OTP servers rely on.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Assuming OTP is only for telecom applications because of its name.
  **Correction**: OTP is a general-purpose framework for any fault-tolerant system.

- **Error**: Hand-rolling concurrency and error handling instead of using OTP behaviours.
  **Correction**: Let OTP behaviours supply the nonfunctional parts; write only sequential callback code.

# Common Confusions

- **Confusion**: Believing OTP is a separate product you must download.
  **Clarification**: The OTP libraries ship inside the standard Erlang distribution.

- **Confusion**: Thinking OTP is a runtime separate from Erlang.
  **Clarification**: OTP is a set of libraries, behaviours, and procedures layered on the Erlang runtime, not a different language or VM.

# Source Reference

Chapter 22: Introducing OTP, opening section "Introducing OTP". No page numbers (EPUB-origin source).

# Verification Notes

- Definition source: Direct quote from chapter opening of "Introducing OTP".
- Confidence rationale: HIGH — the source explicitly defines OTP in its first paragraph.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this extraction batch.
- Re-extraction notes: Fresh extraction; no pre-existing card.
