---
# === CORE IDENTIFICATION ===
concept: Supervision Tree
slug: supervision-tree

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Making a System with OTP"
chapter_number: 23
pdf_page: null
section: "The Supervision Tree"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "supervision tree"
  - "supervisor tree"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
  - process
extends: []
related:
  - restart-strategy
  - child-specification
  - otp-application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a supervision tree?"
  - "How do I build a supervision tree?"
---

# Quick Definition

A supervision tree is a tree of processes: the upper processes (supervisors) monitor the lower processes (workers) and restart them if they fail. Workers may themselves be supervisors, building deeper trees.

# Core Definition

"A supervision tree is a tree of processes. The upper processes (supervisors) in the tree monitor the lower processes (workers) in the tree and restart the lower processes if they fail" (Programming Erlang, "The Supervision Tree"). The tree's structure is specified in a supervisor callback module's `init/1`, which returns a restart strategy and a list of child specifications. Because a child's `Type` may be `supervisor` rather than `worker`, "we can construct a tree of supervisors by adding supervisor processes in place of worker processes." There are two types of supervision tree depending on the restart strategy used at each node: one-for-one and one-for-all.

# Prerequisites

- **Supervisor** — supervision trees are built from supervisor processes.
- **Process** — both supervisors and workers are processes.

# Key Properties

1. A tree whose internal nodes are supervisors and whose leaves are workers.
2. Supervisors monitor and restart the processes beneath them.
3. A child of type `supervisor` makes that node an internal node, deepening the tree.
4. Each supervisor node applies its own restart strategy (`one_for_one` or `one_for_all`).
5. The tree's shape is declared, not coded — it comes from supervisor `init/1` return values.
6. The mechanism is the structural basis of Erlang's fault tolerance.

# Construction / Recognition

## To Construct a Supervision Tree:
1. Write a top-level supervisor callback module.
2. In its `init/1`, return a restart strategy plus child specifications for the workers (and any sub-supervisors).
3. For nested supervision, give a child the `Type` `supervisor` and point it at another supervisor callback module.
4. Start the tree by starting the top-level supervisor (often from an application's `start/2`).

## To Recognize:
1. A supervisor whose child specifications include children of type `supervisor` is an internal node of a supervision tree.

# Context & Application

- **Typical contexts**: The structural backbone of every fault-tolerant OTP system.
- **Common applications**: The `sellaprime` supervision tree has `sellaprime_supervisor` over the `area_server` and `prime_server` workers.
- **Historical/stylistic notes**: The chapter's exercises extend the idea — pools of prime-tester servers under a supervisor hierarchy, restarting everything if a load balancer crashes.

# Examples

**Example 1** ("The Supervision Tree"): `sellaprime_supervisor:init/1` returns `{ok, {{one_for_one, 3, 10}, [<area_server spec>, <prime_server spec>]}}` — a one-level tree with one supervisor over two workers.

**Example 2** ("The Supervision Tree"): The book notes that giving a child `Type = supervisor` lets you "construct a tree of supervisors by adding supervisor processes in place of worker processes."

# Relationships

## Builds Upon
- **Supervisor** — supervision trees are composed of supervisor processes.
- **Process** — every node in the tree is a process.

## Enables
- **OTP application** — an application packages a supervision tree as a startable/stoppable unit.

## Related
- **Restart strategy** — each supervisor node uses a restart strategy.
- **Child specification** — the tree's children are declared as child specifications.

## Contrasts With
- (No direct contrast within this chapter.)

# Common Errors

- **Error**: Putting all workers under a single supervisor when their failures are unrelated.
  **Correction**: Group workers into sub-supervisors so a one-for-all restart only affects truly coupled processes.

- **Error**: Building the tree imperatively in code.
  **Correction**: The tree shape is declared via supervisor `init/1` return values, not spawned by hand.

# Common Confusions

- **Confusion**: Thinking a supervision tree is a data structure.
  **Clarification**: It is a tree of *live processes* — supervisors and workers — connected by monitoring relationships.

- **Confusion**: Believing only leaves can fail and be restarted.
  **Clarification**: A sub-supervisor is itself a child and can be restarted by the supervisor above it.

# Source Reference

Chapter 23: Making a System with OTP, section "The Supervision Tree". No page numbers (EPUB-origin source). See Figure 10 (one-for-one vs one-for-all supervision trees).

# Verification Notes

- Definition source: Direct quote from "The Supervision Tree".
- Confidence rationale: HIGH — the supervision tree is explicitly defined and illustrated with a figure.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards in this batch.
- Re-extraction notes: Fresh extraction; no pre-existing card. Canonical slug `supervision-tree` per extraction instructions.
