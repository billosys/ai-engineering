---
concept: Onion-Layered Design
slug: onion-layered-design
category: fault-tolerance
subcategory: design
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building an Application"
chapter_number: 18
pdf_page: null
section: "The Onion Layer Theory"
extraction_confidence: high
aliases:
  - onion layer theory
  - process segregation
  - layered supervision design
prerequisites:
  - supervision-tree
  - error-kernel
extends: []
related:
  - error-kernel
  - supervision-tree
contrasts_with: []
answers_questions:
  - "What concepts precede building an OTP application?"
  - "How do supervisors relate to the \"let it crash\" philosophy?"
---

# Onion-Layered Design

## Quick Definition

Onion-layered design organises a supervision tree by failure risk: protected, vital code sits near the root, while riskier, failure-prone code is pushed into outer layers — a form of process segregation.

## Core Definition

"The idea of an onion-layered system is to allow all of these different states to be protected correctly by isolating different kinds of code from each other. In other words, it's process segregation." Within the same tree, "operations that are more failure-prone can be placed deeper in the tree, and the processes that cannot afford to crash are closer to the root of the tree" (Ch. 18, "The Onion Layer Theory").

## Prerequisites

- **Supervision tree** — Onion layers are layers of supervision.
- **Error kernel** — The innermost layer is the error kernel.

## Key Properties

1. Each layer of supervision shields the layers above from failures and state loss below.
2. Related operations belong in the same supervision tree; unrelated ones in separate trees.
3. Riskier operations go deeper; processes that must not crash go closer to the root.
4. The innermost, most-protected region is the error kernel.
5. Static state can be injected by supervisors; recomputable dynamic state can be rebuilt on restart; non-recomputable state must be protected by depth.

## Construction / Recognition

## To Apply Onion-Layered Design

1. Classify each piece of state: static, dynamic-recomputable, dynamic-non-recomputable.
2. Place non-recomputable, vital code near the root (the error kernel).
3. Place fragile, failure-prone code in deeper layers.
4. Keep related code in one tree; isolate unrelated subsystems into separate trees.
5. Add supervision layers as shields between risk levels.

## Context & Application

The book uses onion-layered design to drive the `ppool` architecture. Because all pools sit under one supervisor, a pool restarting too often could take down the others — so an extra supervision layer (`ppool_supersup`) is added so pools are independent. Separating a sockets pool from a log-files pool ensures "incorrect code or messy permissions in the log file section ... won't be drowning out the processes in charge of the sockets."

## Examples

**Example 1** (Ch. 18): The `ppool` tree gains a top-level `ppool_supersup` so one misbehaving pool cannot crash sibling pools.

**Example 2** (Ch. 18): Sockets pool and log-files pool are kept in independent subtrees so failures in one are isolated from the other.

## Relationships

## Builds Upon

- **Supervision tree** — Onion layers are supervision layers.
- **Error kernel** — The center of the onion.

## Common Errors

- **Error**: Putting all subsystems under one flat supervisor.
  **Correction**: Add supervision layers so a noisy subsystem cannot trip the restart limit for unrelated ones.

## Common Confusions

- **Confusion**: Thinking deeper-in-the-tree means more important.
  **Clarification**: It is the reverse — deeper means *riskier* and less protected; the root is the most protected, most vital region.

## Source Reference

Chapter 18: "Building an Application," sections "The Onion Layer Theory" and "A Pool's Tree."

## Verification Notes

- Definition: Direct quotes from "The Onion Layer Theory."
- Key Properties: Synthesised from the three-kinds-of-state discussion and the `ppool` tree rationale.
- Confidence: HIGH — explicitly named and described.
