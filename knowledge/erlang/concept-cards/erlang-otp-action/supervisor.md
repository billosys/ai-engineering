---
# === CORE IDENTIFICATION ===
concept: Supervisor
slug: supervisor

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "OTP applications and supervision"
chapter_number: 4
pdf_page: null
section: "4.2 Adding fault tolerance with supervisors"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - supervisor behaviour
  - "supervisor behavior"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-behaviour
  - process-link
  - gen-server
extends:
  - otp-behaviour
related:
  - supervision-tree
  - root-supervisor
  - supervisor-restart-strategy
  - child-specification
  - supervisor-implementation
  - worker-process
  - simple-one-for-one
contrasts_with:
  - worker-process
  - gen-server

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP supervisor?"
  - "What does a supervisor do when a process crashes?"
  - "What behaviour do supervisors implement?"
---

# Quick Definition

A supervisor is an OTP process that monitors other processes and takes action — typically restarting them — if anything goes wrong. Supervisors are one of the core features of Erlang/OTP.

# Core Definition

Supervisors are one of the most important features of OTP: they monitor other processes and take action if anything goes wrong, restarting the failed process or possibly escalating the problem to a higher level (Ch. 4 introduction; Section 4.2). An active OTP application consists of one or more processes that do the work; those processes are started indirectly by supervisors, which are responsible for supervising them and restarting them if necessary. You create a supervisor by writing a module that implements the `supervisor` behaviour. Supervisors are themselves built on the `gen_server` behaviour. Layering supervisors into supervision trees allows highly fault-tolerant systems.

# Prerequisites

- **OTP behaviour** — A supervisor is implemented as a behaviour.
- **Process link** — Supervision relies on process links to detect child failure.
- **gen_server behaviour** — The `supervisor` behaviour is internally built on `gen_server`.

# Key Properties

1. Monitors other processes (its children) and acts when they fail.
2. Implemented by a module with `-behaviour(supervisor)`.
3. Started with `supervisor:start_link/3`.
4. The `init/1` callback returns `{ok, {RestartStrategy, Children}}`.
5. Children can be workers or other supervisors, forming a supervision tree.
6. Internally built on `gen_server`.

# Construction / Recognition

## To Implement a Supervisor:
1. Write a module with `-behaviour(supervisor)`.
2. Provide a `start_link` API function calling `supervisor:start_link/3`.
3. Implement `init/1` returning `{ok, {RestartStrategy, Children}}`.
4. Specify the restart strategy and a list of child specifications.

## To Recognize One:
1. Look for `-behaviour(supervisor)` and an `init/1` returning the supervisor spec tuple.

# Context & Application

Supervisors are what make Erlang/OTP fault-tolerant: workers do the work, supervisors keep them alive.

- **Typical contexts**: Every active application has at least a root supervisor.
- **Common applications**: `tr_sup` supervises `tr_server`; `sc_sup` is a factory for `sc_element` processes.

# Examples

**Example 1** (Ch. 4, Listing 4.3): `tr_sup` is the root supervisor of `tcp_rpc`, supervising the single `tr_server` worker.

**Example 2** (Ch. 5): Killing the `tr_sup` process via Appmon kills the whole `tcp_rpc` application, because the processes are linked.

# Relationships

## Builds Upon
- **OTP behaviour** — A supervisor is a behaviour.
- **gen_server behaviour** — Supervisors are internally built on `gen_server`.

## Enables
- **supervision-tree** — Supervisors layered into a tree.
- **root-supervisor** — The top supervisor of an application.

## Related
- **supervisor-restart-strategy** — How a supervisor reacts to failures.
- **child-specification** — Describes each supervised process.
- **supervisor-implementation** — How a supervisor module is written.

## Contrasts With
- **worker-process** — A worker does actual work; a supervisor only monitors and restarts.
- **gen_server** — A `gen_server` is a worker behaviour; `supervisor` only supervises (though built on `gen_server`).

# Common Errors

- **Error**: Putting application logic in supervisor `init/1`.
  **Correction**: Keep supervisors small and reliable; minimize code in them.

# Common Confusions

- **Confusion**: Thinking a supervisor does the application's work.
  **Clarification**: Supervisors only monitor and restart; workers do the actual work.

# Source Reference

Chapter 4: OTP applications and supervision, Section 4.2 "Adding fault tolerance with supervisors," Figure 4.2 and Listing 4.3.

# Verification Notes

- Definition source: Direct adaptation of the chapter introduction and Section 4.2.
- Confidence rationale: HIGH — explicit, repeated definition in the source.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slug `process-link` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
