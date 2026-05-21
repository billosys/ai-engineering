---
# === CORE IDENTIFICATION ===
concept: The sys Module
slug: the-sys-module

# === CLASSIFICATION ===
category: production-ops
subcategory: behavior-inspection
tier: intermediate

# === PROVENANCE ===
source: Designing for Scalability with Erlang/OTP
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Controlling OTP Behaviors"
chapter_number: 4
pdf_page: 120
section: "The sys Module"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - sys
  - "sys module"
  - system module

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gen-server
extends: []
related:
  - sys-tracing-and-logging
  - system-message
  - custom-trace-functions
  - behavior-statistics-status-state
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the sys module relate to OTP behaviors?"
  - "How do I trace and inspect an OTP process with the sys module?"
---

# Quick Definition

The `sys` module is a built-in OTP module that gives you generic access to any behavior process — letting you generate trace events, inspect and manipulate behavior state, and send and receive system messages without writing any new code.

# Core Definition

The `sys` module is the standard interface through which OTP exposes the built-in functionality every behavior process inherits. Through it you can "generate trace events, inspect and manipulate behavior state, as well as send and receive system messages" (Cesarini & Vinoski, p. 120). All of this functionality works on the standard OTP behaviors (`gen_server`, `gen_fsm`/`gen_statem`, `gen_event`, `supervisor`), and can also be reused when you define your own behaviors (p. 120). Because the `sys` calls are synchronous calls into the behavior process, every function accepts an optional `Timeout` argument that overrides the default 5-second timeout (p. 105).

# Prerequisites

- **Generic server** — `sys` operates on behavior processes; understanding how a `gen_server` receive-evaluate loop and loop data work is needed before its inspection calls make sense.

# Key Properties

1. Works uniformly on all standard OTP behaviors and on user-defined behaviors.
2. Functionality groups: tracing/logging, custom trace functions, statistics, status and state inspection, suspend/resume.
3. Every call is a synchronous request to the behavior process, so each accepts an optional `[,Timeout]` argument (functions of arity 2 and 3).
4. Requires no changes to the behavior's callback module — it operates entirely from the outside.
5. The `get_state/1`, `replace_state/2`, and `get_status/1` functions are intended only for debugging and troubleshooting live systems.

# Construction / Recognition

## To Use the sys Module:
1. Identify a running behavior process by registered name or pid.
2. Call the relevant `sys` function (e.g., `sys:trace/2`, `sys:get_state/1`, `sys:statistics/2`).
3. Optionally pass a `Timeout` as the last argument to override the 5-second default.

## To Recognize sys Usage:
1. Look for calls qualified with the `sys:` module prefix in shell sessions or operational scripts.
2. `*DBG*` printouts in the shell indicate `sys`-driven tracing is active.

# Context & Application

- **Typical contexts**: Live debugging, production troubleshooting, software upgrades, and edge-condition testing.
- **Common applications**: Turning on tracing or logging, inspecting loop data, gathering statistics, suspending a process during a hot upgrade.
- **Historical/stylistic notes**: The book parks "online tracing" here and revisits it in Chapter 10 when implementing custom behaviors, noting the `sys` module applies equally to behaviors you write yourself (p. 120, p. 134).

# Examples

**Example 1** (p. 120): Starting a `frequency` server and calling `sys:trace(frequency, true)` to stream system events to the shell.

**Example 2** (p. 124-125): `sys:get_status(frequency)` returns a full status tuple, and `sys:get_state(frequency)` returns just the loop data — `{[], [{15,<0.33.0>}, ...]}`.

# Relationships

## Builds Upon
- **Generic server** — `sys` exposes the built-in machinery shared by every behavior, of which `gen_server` is the canonical example.

## Enables
- **sys-tracing-and-logging** — Tracing and logging are accessed through `sys`.
- **system-message** — `sys` sends and receives the system messages behaviors exchange.
- **custom-trace-functions** — Installed via `sys:install/2`.
- **behavior-statistics-status-state** — Gathered via `sys:statistics/2`, `sys:get_status/1`, `sys:get_state/1`.

## Related
- **spawn-options** — Both `sys` debug options and spawn options are passed through the behavior's `Opts` field.

## Contrasts With
- *(None — the `sys` module is a unique facility with no direct counterpart.)*

# Common Errors

- **Error**: Calling `sys:suspend/1` inside business logic to pause a process.
  **Correction**: Never suspend processes in business logic; the only acceptable way to "suspend" is a `receive` clause with no matching messages. Reserve `sys:suspend/1` for upgrades and edge-case testing.

# Common Confusions

- **Confusion**: Believing `sys` functionality requires special hooks in your callback module.
  **Clarification**: The `sys` module works on standard behaviors out of the box; no callback changes are needed. Only the optional `format_status/2` callback customizes its output.

# Source Reference

Chapter 4: Controlling OTP Behaviors, Section "The sys Module," pages 120-127. See especially "The sys Module Recap" (pp. 125-127) listing all covered functions.

# Verification Notes

- Definition source: Direct quote from p. 120.
- Confidence rationale: HIGH — the source explicitly introduces and names the module, lists its function set, and devotes a recap section to it.
- Uncertainties: None.
- Cross-reference status: Verified — all referenced slugs are planned cards in this extraction batch.
- Re-extraction notes: Fresh extraction; no pre-existing card for this source.
