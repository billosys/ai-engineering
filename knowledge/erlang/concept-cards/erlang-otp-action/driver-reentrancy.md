---
# === CORE IDENTIFICATION ===
concept: Linked-in Driver Reentrancy
slug: driver-reentrancy

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
section: "12.3.1. Understanding linked-in drivers"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - reentrant driver code
  - instance-specific data

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linked-in-driver
extends: []
related:
  - driver-callbacks
  - driver-memory-management
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why must linked-in driver code be reentrant?"
  - "What is instance-specific data in a driver?"
  - "Why are global variables dangerous in a linked-in driver?"
---

# Quick Definition

Linked-in driver code must be reentrant — usable by multiple simultaneous port instances — which means it must use per-instance allocated memory instead of global variables.

# Core Definition

The same linked-in driver code can be activated any number of times for separate port instances that may have overlapping lifetimes. Because all these instances execute within the memory of the Erlang VM, possibly running as different threads, the driver code must be designed to be *reentrant* — executable by multiple simultaneous callers — and must not depend on global variables or locks. There are two kinds of long-lived data in C: global (external) variables, which are shared by all callers and cause corruption, and dynamically allocated memory, where each caller allocates its own. A driver should keep all per-port state in dynamically allocated *instance-specific data*, so each port has its own working memory ("Erlang and OTP in Action," Ch. 12, Section 12.3.1).

# Prerequisites

- **Linked-in port driver** — Reentrancy is a requirement specific to driver code.

# Key Properties

1. One set of driver code may back many concurrently live port instances.
2. Driver instances run within the Erlang VM, possibly as different threads.
3. Reentrant code is executable by multiple simultaneous callers and avoids global variables and locks.
4. Global (external) C variables are shared across all instances — callers overwrite each other's data.
5. Instance-specific data is dynamically allocated memory, separate per port instance.
6. Instance-specific data is typically allocated in the driver's `start` callback.
7. It is analogous to the state record of a `gen_server`.

# Construction / Recognition

## To Construct/Create:
1. Define a C struct holding the per-instance (per-port) state.
2. Allocate one in the `start` callback; return a pointer cast to `ErlDrvData`.
3. Have the VM pass that `ErlDrvData` handle to every other callback so each call sees its own state.
4. Avoid global variables and locks entirely.

## To Identify/Recognize:
1. Driver code whose per-port state lives in a dynamically allocated struct passed via `ErlDrvData`, with no global state.

# Context & Application

- **Typical contexts**: Writing correct linked-in drivers used by multiple ports.
- **Common applications**: A counter driver: with global state, five counter ports corrupt one shared variable; with instance-specific data each port has its own counter.
- **Historical/stylistic notes**: The book stresses making the original port code well-structured so the driver conversion is easy.

# Examples

**Example 1** (Section 12.3.1, Figures 12.5–12.6): A nonreentrant counter driver using a global variable has five ports stomping on the same memory; a reentrant version gives each port its own counter.

**Example 2** (Section 12.3.2): For the JSON driver, the instance-specific `drv_data_t` struct stores only the Erlang port, allocated in `drv_start`.

# Relationships

## Builds Upon
- **Linked-in port driver** — Reentrancy is a constraint on driver code.

## Related
- **Driver callbacks** — Instance-specific data is created in `start` and passed to other callbacks.
- **Linked-in driver memory management** — Per-instance memory must be allocated with `driver_alloc`.

# Common Errors

- **Error**: Storing per-port state in a global C variable.
  **Correction**: Use dynamically allocated instance-specific data, one per port instance.

- **Error**: Relying on locks to make global state safe in a driver.
  **Correction**: Driver code must be reentrant without depending on global variables or locks.

# Common Confusions

- **Confusion**: Thinking a single port instance means global variables are fine.
  **Clarification**: A user may open many ports on the same driver; all of them share globals and corrupt each other.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Section 12.3.1 "Understanding linked-in drivers." See Figures 12.5 and 12.6.

# Verification Notes

- Definition source: Direct adaptation of Section 12.3.1.
- Confidence rationale: HIGH — the book explicitly explains reentrancy and instance-specific data.
- Uncertainties: None.
- Cross-reference status: `linked-in-driver` owned by this agent.
- Re-extraction notes: Fresh extraction; no prior card existed.
