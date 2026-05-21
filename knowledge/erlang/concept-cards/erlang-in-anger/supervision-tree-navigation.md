---
concept: Supervision Tree Navigation
slug: supervision-tree-navigation
category: applications-releases
subcategory: supervision
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "How to Dive into a Code Base"
chapter_number: 1
pdf_page: null
section: "Regular Applications"
extraction_confidence: high
aliases:
  - "Top-down code base exploration"
prerequisites:
  - regular-application
  - supervisor-restart-strategy
extends: []
related:
  - behaviour-as-navigation-clue
  - application-dependency-graph
contrasts_with: []
answers_questions:
  - "How do I dive into an unfamiliar code base?"
  - "How do I navigate a supervision tree?"
---

# Quick Definition

Supervision tree navigation is the technique of exploring a regular OTP application top-down by following its supervisors, using process position and start order to infer importance and dependencies.

# Core Definition

From Chapter 1, section "Regular Applications": "This structure means it is easiest to navigate OTP applications in a top-down manner by exploring supervision subtrees." The top-level supervisor contains the specifications of all child processes it starts, and the tree is started in order, depth-first.

# Prerequisites

- `regular-application` — only regular applications have a supervision tree to navigate.
- `supervisor-restart-strategy` — restart strategies are a key clue read during navigation.

# Key Properties

1. The application starts a top-level supervisor and returns its pid; navigation starts there.
2. The higher a process resides in the tree, the more likely it is vital to the application's survival.
3. Children are started in order, depth-first; a process started later probably depends on processes started earlier.
4. Interdependent worker processes are typically grouped under the same supervisor and fail together — a deliberate choice, since restarting both from a blank slate is simpler than recovering corrupted state.
5. Combining supervision relationships with each worker's behaviour reveals a lot about the program.

# Construction / Recognition

To navigate: (1) find the application's callback module (`appname_app`) and the top-level supervisor it starts; (2) walk the tree depth-first; (3) treat higher and earlier-started processes as more vital; (4) read each supervisor's restart strategy to infer child relationships; (5) read each worker's behaviour to infer its role. The `observer` application visualizes individual supervision trees at runtime.

# Context & Application

This is the recommended primary method for understanding any regular OTP application you inherit or must debug. It turns the application's structure itself into documentation.

# Examples

From Chapter 1, section "Regular Applications": a process that "buffers socket communications and relays them to a finite-state machine in charge of understanding the protocol" is given as an example of interdependent workers regrouped under the same supervisor so they fail together.

# Relationships

## Builds Upon
- `regular-application` — provides the tree.
- `supervisor-restart-strategy` — read at each supervisor node.

## Enables
Effective debugging and maintenance of unfamiliar code.

## Related
- `behaviour-as-navigation-clue` — the per-worker complement to tree navigation.
- `application-dependency-graph` — the cross-application complement.

## Contrasts With
Nothing directly.

# Common Errors

- Reading modules alphabetically or at random instead of following the tree top-down, which loses the importance/dependency signal.

# Common Confusions

- A process started later is not necessarily *less* important overall — it is just likely to depend on earlier ones; height in the tree is the better importance signal.
- Some supervisors specify no children (children may be added dynamically, in a start phase, or the supervisor only exists to load `env` variables) — an empty supervisor is not necessarily a bug.

# Source Reference

Chapter 1: How to Dive into a Code Base, Section "Regular Applications". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: synthesized from Chapter 1, section "Regular Applications."
- Confidence rationale: high — all navigation heuristics stated explicitly in the source.
- Uncertainties: none.
- Cross-reference status: Verified
