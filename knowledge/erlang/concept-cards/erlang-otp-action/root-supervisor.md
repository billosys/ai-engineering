---
# === CORE IDENTIFICATION ===
concept: Root Supervisor
slug: root-supervisor

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
  - top-level supervisor
  - "_sup module"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
  - application-behaviour
extends:
  - supervisor
related:
  - supervision-tree
  - application-behaviour
  - supervisor-implementation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a root supervisor?"
  - "Who starts the root supervisor?"
  - "What is the naming convention for the root supervisor module?"
---

# Quick Definition

The root supervisor is the top-level supervisor of an active application — the grandparent of all the application's processes — started by the application behaviour's `start/2` callback.

# Core Definition

Every active application has a root supervisor whose job is to manage the processes of the application (Ch. 4, Section 4.1). It is the root of the application's supervision tree and the grandparent of all the processes that will be part of the application (Section 4.1.3). The application behaviour module's `start/2` callback provides the point from which the root supervisor is started and must return its process ID as `{ok, Pid}`. The common naming convention for the module implementing the root supervisor behaviour is `<application-name>_sup`.

# Prerequisites

- **Supervisor** — The root supervisor is a supervisor.
- **Application behaviour** — The application behaviour's `start/2` starts the root supervisor.

# Key Properties

1. The top-level supervisor of an active application.
2. The root of the application's supervision tree.
3. The grandparent of all the application's processes.
4. Started from the application behaviour module's `start/2` callback.
5. Named by convention `<application-name>_sup`.

# Construction / Recognition

## To Set Up a Root Supervisor:
1. Write a `<app>_sup` module implementing the `supervisor` behaviour.
2. Give it a `start_link/0` API function calling `supervisor:start_link/3`.
3. Call `<app>_sup:start_link()` from the application behaviour's `start/2`.
4. Return the resulting `{ok, Pid}` from `start/2`.

# Context & Application

The root supervisor is the single point from which the whole application tree grows; killing it tears down the application.

- **Typical contexts**: The top of every active application's process tree.
- **Common applications**: `tr_sup` is the root supervisor of `tcp_rpc`; `sc_sup` is the root supervisor of `simple_cache`.

# Examples

**Example 1** (Ch. 4, Listing 4.3): `tr_sup` is the root supervisor of `tcp_rpc`, started by `tr_app:start/2` via `tr_sup:start_link()`.

**Example 2** (Ch. 5): In Appmon, the third process from the top of the `tcp_rpc` view is the root supervisor, started by `tr_sup:start_link()`, with a child `tr_server`.

# Relationships

## Builds Upon
- **Supervisor** — The root supervisor is a supervisor.

## Related
- **application-behaviour** — `start/2` starts the root supervisor.
- **supervision-tree** — The root supervisor is the root of the tree.
- **supervisor-implementation** — The `_sup` module is written like any supervisor.

## Contrasts With
- This is a structural role; the source draws no direct contrast.

# Common Errors

- **Error**: Embedding the `start_link` call inside `tr_app:start/2` instead of a separate `_sup` module.
  **Correction**: Separate responsibilities — keep supervisor details in the `_sup` module.

# Common Confusions

- **Confusion**: Thinking the application master is the root supervisor.
  **Clarification**: The application master processes are part of the `application` container; they call `start/2`, which in turn starts the root supervisor.

# Source Reference

Chapter 4: OTP applications and supervision, Sections 4.1, 4.1.3, and 4.2. See the "Naming the root supervisor behaviour module" sidebar and Listing 4.3.

# Verification Notes

- Definition source: Direct adaptation of Sections 4.1 and 4.1.3.
- Confidence rationale: HIGH — explicit definition in the source.
- Uncertainties: None.
- Cross-reference status: Slugs reference planned cards in this chapter group.
- Re-extraction notes: Fresh extraction; no prior card existed.
