---
# === CORE IDENTIFICATION ===
concept: gen_server as a Port Program Proxy
slug: port-program-as-proxy

# === CLASSIFICATION ===
category: tooling
subcategory: interoperability
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Integrating with foreign code using ports and NIFs"
chapter_number: 12
pdf_page: null
section: "12.2.1. The Erlang side of the port"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - port proxy process
  - exit_status handling

# === TYPED RELATIONSHIPS ===
prerequisites:
  - port
  - port-owner
  - gen-server
extends: []
related:
  - open-port
  - supervisor
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you detect that a port's external program has failed?"
  - "How can a gen_server act as a proxy for an external program?"
  - "How is an external program restart tied to OTP supervision?"
---

# Quick Definition

Wrapping a port in a `gen_server` lets the server act as a proxy for the external program — detecting its exit via the `exit_status` message and restarting it, optionally through OTP supervision.

# Core Definition

Because the theme of the book is Erlang and OTP, the process that owns a port should be implemented as a `gen_server`. When the port is created with the `exit_status` option, the server receives an out-of-band message when the external program exits, which it can use to track and manage the program — for example, restarting it by reopening the port. A more elegant approach is to make the `gen_server` a true proxy for the external program: make the server a transient child of a supervisor, and if the external program exits with a nonzero status, shut down the server with a non-`normal` reason, causing the supervisor to restart the entire server. This creates a one-to-one relationship between process restarts and external-program restarts, enabling SASL logging and OTP restart strategies ("Erlang and OTP in Action," Ch. 12, Section 12.2.1).

# Prerequisites

- **Port** — The proxy manages a port.
- **Port owner** — The `gen_server` is the port's owner.
- **gen_server** — The proxy is a `gen_server`.

# Key Properties

1. The port-owning process is implemented as a `gen_server`.
2. With the `exit_status` port option, the server receives `{Port, {exit_status, Status}}` when the program exits.
3. The server can react in `handle_info` — e.g., reopen the port to restart the program.
4. A more elegant design makes the server a *transient* child of a supervisor.
5. On a nonzero external exit, the server stops with a non-`normal` reason, so the supervisor restarts it.
6. This yields a one-to-one mapping between process restarts and external-program restarts.
7. It lets the integration benefit from SASL logging and OTP restart strategies.

# Construction / Recognition

## To Construct/Create:
1. Open the port with the `exit_status` option.
2. Add a `handle_info({Port, {exit_status, Status}}, State)` clause.
3. Either reopen the port directly, or stop the server with a non-`normal` reason and let a supervisor restart it.
4. For the proxy design, register the `gen_server` as a transient child of a supervisor.

## To Identify/Recognize:
1. A `gen_server` owning a port, with a `handle_info` clause matching `{Port, {exit_status, _}}`.

# Context & Application

- **Typical contexts**: Making a port-connected external program fault-tolerant.
- **Common applications**: `jp_server` proxying the `jp_prog` JSON parser; particularly useful when integrating with a hardware driver.
- **Historical/stylistic notes**: Blocking the `gen_server` call until the port responds also lets the server provide concurrency control for a single-client external program.

# Examples

**Example 1** (Section 12.2.1): `handle_info({Port, {exit_status, Status}}, #state{port=Port}=State)` logs the exit and calls `create_port()` to reopen the port, returning `{noreply, State#state{port=NewPort}}`.

**Example 2** (Section 12.2.1): Making the `gen_server` a transient supervisor child and stopping it with a non-`normal` reason on nonzero exit causes the supervisor to restart the whole server — and thus the external program.

# Relationships

## Builds Upon
- **Port** — The proxy wraps a port.
- **gen_server** — The proxy is implemented as a `gen_server`.
- **Port owner** — The proxy is the owning process.

## Related
- **open_port BIF** — The `exit_status` option enables failure detection.
- **supervisor** — The proxy design relies on supervisor restart.

# Common Errors

- **Error**: Opening the port without the `exit_status` option but expecting to detect program failure.
  **Correction**: Pass `exit_status` so the owner receives `{Port, {exit_status, Status}}` messages.

- **Error**: Stopping the proxy server with reason `normal` after a nonzero external exit.
  **Correction**: Stop with a non-`normal` reason so the supervisor treats it as a failure and restarts.

# Common Confusions

- **Confusion**: Thinking the port itself can be supervised by an OTP supervisor.
  **Clarification**: Supervisors manage processes; the `gen_server` proxy is supervised, and it in turn manages the port.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Section 12.2.1 "The Erlang side of the port" — subsections "Communicating with the port" and "Detecting failure."

# Verification Notes

- Definition source: Direct adaptation of Section 12.2.1.
- Confidence rationale: HIGH — the book explicitly describes both the `exit_status` and the supervisor-proxy approaches.
- Uncertainties: None.
- Cross-reference status: `gen-server`, `supervisor` owned by Agent 2.
- Re-extraction notes: Fresh extraction; no prior card existed.
