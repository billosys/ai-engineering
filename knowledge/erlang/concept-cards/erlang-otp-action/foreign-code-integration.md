---
# === CORE IDENTIFICATION ===
concept: Foreign Code Integration Mechanisms
slug: foreign-code-integration

# === CLASSIFICATION ===
category: tooling
subcategory: interoperability
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Integrating with foreign code using ports and NIFs"
chapter_number: 12
pdf_page: null
section: "12.1. Ports and NIFs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - foreign function interface
  - interfacing with C
  - FFI

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
extends: []
related:
  - port
  - linked-in-driver
  - nif
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What mechanisms does Erlang provide for interfacing with foreign code?"
  - "How does Erlang's approach to foreign code differ from a typical FFI?"
  - "Which foreign-code mechanism should you choose first?"
---

# Quick Definition

Erlang integrates with foreign (e.g., C) code through three low-level mechanisms — plain ports, linked-in port drivers, and NIFs — plus the distribution-based C node approach, each trading safety against speed.

# Core Definition

Like most languages, Erlang allows interfacing to code written in other languages, but its standard mechanism is unusual: instead of a foreign function interface (FFI) that links C code into the host language, Erlang extends the message-passing paradigm — foreign code behaves much like a separate Erlang process, represented on the Erlang side by a process-like object called a *port*. There are three low-level mechanisms for interfacing between Erlang and other languages: plain ports, linked-in port drivers, and NIFs. Plain ports are a safe and easy way to hook up an external program over standard I/O; linked-in port drivers offer greater speed at the price of safety; NIFs are an efficient but perilous way of hooking in library functions. Foreign code can also be integrated via the distribution mechanism as a C node or Java node ("Erlang and OTP in Action," Ch. 12, introduction and Section 12.1).

# Prerequisites

- **Process** — Erlang models foreign code as something process-like that exchanges messages.

# Key Properties

1. Erlang uses message passing rather than a conventional FFI for foreign code.
2. Plain ports — safe, language-neutral, run foreign code as an external OS process; usually fast enough.
3. Linked-in port drivers — faster shared-library code, but can crash the entire VM.
4. NIFs — minimal-overhead C functions callable like BIFs, but a bug can crash the whole VM.
5. C nodes / Java nodes — foreign programs that masquerade as Erlang nodes via the distribution protocol.
6. The recommended default is a plain port; optimize to a driver or NIF only when proven necessary.

# Construction / Recognition

## To Construct/Create:
1. Start with a plain port: write an external program reading stdin/writing stdout.
2. If speed is proven insufficient, convert to a linked-in driver or a NIF.
3. For node-level integration, use Erl_Interface (`ei`) or Jinterface to build a C/Java node.

## To Identify/Recognize:
1. Calls to `open_port/2`, `erl_ddll:load/2`, or `erlang:load_nif/2`, or a foreign program registered as an Erlang node.

# Context & Application

- **Typical contexts**: Reusing existing C libraries, controlling hardware, or talking to Java code.
- **Common applications**: The chapter integrates the YAJL JSON C library three different ways.
- **Historical/stylistic notes**: NIFs were new as of the book's writing; for simple tasks a C node is usually overkill.

# Examples

**Example 1** (Section 12.1): "Whenever in doubt, you should always start with a plain implementation using ports and then optimize later if it turns out that you need more speed."

**Example 2** (Chapter introduction): A C or Java program using Erl_Interface (`ei`) or Jinterface can masquerade as an Erlang node, communicating via the Erlang distribution protocol.

# Relationships

## Enables
- **Port** — The primary, safe integration mechanism.
- **Linked-in driver** — A faster but riskier mechanism.
- **NIF** — An efficient, perilous mechanism.
- **C node** — A distribution-based integration mechanism.

# Common Errors

- **Error**: Reaching for a NIF or linked-in driver as the first integration choice.
  **Correction**: Start with a plain port; move to a driver or NIF only when you have proven you need the speed.

# Common Confusions

- **Confusion**: Expecting Erlang to provide a conventional FFI.
  **Clarification**: Erlang extends message passing instead; foreign code looks like a process behind a port.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," chapter introduction and Section 12.1 "Ports and NIFs."

# Verification Notes

- Definition source: Direct adaptation of the chapter introduction and Section 12.1.
- Confidence rationale: HIGH — the book explicitly enumerates and characterizes the mechanisms.
- Uncertainties: None.
- Cross-reference status: `process` owned by Agent 1; `c-node` referenced for Ch. 13 (Agent 5).
- Re-extraction notes: Fresh extraction; no prior card existed.
