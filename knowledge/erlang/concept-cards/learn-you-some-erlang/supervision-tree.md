---
concept: Supervision Tree
slug: supervision-tree
category: fault-tolerance
subcategory: supervision
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Who Supervises the Supervisors?"
chapter_number: 17
pdf_page: null
section: "Supervisor Concepts"
extraction_confidence: high
aliases:
  - supervision hierarchy
  - process tree
prerequisites:
  - supervisor
  - worker-process
extends: []
related:
  - supervisor
  - error-kernel
  - onion-layered-design
contrasts_with: []
answers_questions:
  - "What is a supervisor?"
  - "How do supervisors relate to the \"let it crash\" philosophy?"
  - "What must I understand before using supervisors?"
---

# Supervision Tree

## Quick Definition

A supervision tree is a hierarchy of supervisors and workers, where supervisors supervise other supervisors and workers, giving an application a structured, restartable, cleanly-terminable shape.

## Core Definition

The book describes supervision as forming a tree: "Supervisors can supervise workers and other supervisors." Hand-rolled supervisors could only "have a chain of supervisors, not a tree"; OTP supervisors let "you have more than one worker per supervisor" (Ch. 17, "Supervisor Concepts" and chapter introduction). The whole structure rooted at a top supervisor is the supervision tree.

## Prerequisites

- **Supervisor** — Internal nodes of the tree.
- **Worker process** — Leaves of the tree.

## Key Properties

1. Internal nodes are supervisors; leaves are workers.
2. A supervisor can supervise both workers and child supervisors.
3. Adding a layer of supervision shields the layers above from failures and state loss below.
4. The tree enables well-ordered VM shutdown: the top supervisor terminates and each child is asked to terminate in turn.
5. Every process should belong to a supervision tree — unsupervised processes are unaccountable.
6. Restart limits at each level mean a failing subtree can be given up while the rest survives.

## Construction / Recognition

## To Design a Supervision Tree

1. Place processes that cannot afford to crash near the root.
2. Place the riskiest, failure-prone processes deeper in the tree.
3. Group related operations under the same subtree; keep unrelated ones in separate trees.
4. Choose each supervisor's restart strategy to match its children's dependencies.

## Context & Application

The supervision tree is the structural backbone of OTP applications. Chapter 18's onion-layer theory builds directly on it: a tree's depth maps to risk, with the *error kernel* (the code that must not fail) closest to the root. Chapter 19's `ppool` application starts its whole supervision tree with a single `application:start/1` call.

## Examples

**Example 1** (Ch. 18): The process-pool tree — `ppool_supersup` at the top, a `ppool_sup` per pool, each with a `ppool_serv` and a `ppool_worker_sup` (`simple_one_for_one`) over the actual workers.

**Example 2** (Ch. 17): The `band_supervisor` with four musician workers is a small one-level tree.

## Relationships

## Builds Upon

- **Supervisor** — Supervisors are the internal nodes.
- **Worker process** — Workers are the leaves.

## Related

- **error-kernel** — The most-protected core of the tree.
- **onion-layered-design** — Organises the tree by failure risk.

## Common Errors

- **Error**: Putting fragile and critical processes at the same depth in one subtree.
  **Correction**: Push risky processes deeper and keep critical ones near the root.

## Common Confusions

- **Confusion**: Thinking a supervision tree is just a single supervisor with workers.
  **Clarification**: Supervisors supervise other supervisors, so real applications form multi-level trees, not flat lists.

## Source Reference

Chapter 17: "Who Supervises the Supervisors?", section "Supervisor Concepts" and the chapter introduction; structural application in Chapter 18, "A Pool's Tree."

## Verification Notes

- Definition: Adapted from "Supervisor Concepts" and the chapter intro.
- Key Properties: Synthesised from the shutdown discussion and the onion-layer connection.
- Confidence: HIGH — the tree concept is explicit and central.
