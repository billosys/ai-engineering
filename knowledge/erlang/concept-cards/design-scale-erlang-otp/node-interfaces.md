---
# === CORE IDENTIFICATION ===
concept: Node Interfaces
slug: node-interfaces

# === CLASSIFICATION ===
category: api-design
subcategory: distributed-interfaces
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Distributed Architectures"
chapter_number: 12
pdf_page: 378
section: "Interfaces"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - node interface
  - exported node interface

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semantic-node-type
extends: []
related:
  - logic-node
  - service-node
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I define the interfaces between nodes?"
  - "How do I define my node interfaces, state, and data model?"
---

# Quick Definition

A node interface is the set of functions, arguments, return values, and data model that a node exports for other nodes to call. Defining them is the fourth step of designing a distributed architecture.

# Core Definition

"Once you've split your node into node types and defined what services they will provide and how they will communicate with each other, the time comes to specify the interfaces the nodes export" (Cesarini & Vinoski, p. 396). Interfaces "are not only used by other nodes when sending requests; they will be used to implement the business logic, to test the nodes on a standalone basis, and to run end-to-end tests of the system" (p. 397). For each story or feature, you determine the function to call, the arguments, the data model, calls to other nodes, destructive operations, and the return values.

# Prerequisites

- **Semantic node type** — You define interfaces after splitting the system into node types.

# Key Properties

1. An interface specifies the function to call when accessing the node.
2. It specifies the arguments needed to fulfill a request.
3. It specifies the data model of tables and state the node must hold.
4. It specifies calls to other nodes (repeating the analysis for each).
5. It records destructive operations — table updates and state changes resulting from a call.
6. It specifies the return values of each call.
7. Defining interfaces validates the earlier choice of node-type split and is an iterative process.

# Construction / Recognition

## To Construct/Create:
1. Break the system down into stories and features (client actions or external events).
2. For each action, determine the function, arguments, data model, downstream calls, destructive operations, and return values.
3. Abstract and simplify; consider positive use cases and only business-logic errors at this stage.
4. Iterate, rearranging tables and reducing data duplication.

## To Identify/Recognize:
1. Recognize a node interface as a documented API plus the state/data model backing it.

# Context & Application

- **Typical contexts**: Step 4 of designing a distributed architecture.
- **Common applications**: Implementing business logic, standalone node testing, end-to-end testing.
- **Historical/stylistic notes**: At the interface-design stage, ignore parse errors, crashes, and connectivity issues — those are handled by later retry-strategy steps; only business-logic errors should appear (p. 398).

# Examples

**Example 1** (p. 398, Table 13-1): The web front-end node interface `login(UserId, Password) -> {ok, SessionId} | {error, login_failed}` with no tables or state.

**Example 2** (pp. 398-399, Table 13-1): The logic node interface `login(UserId, Password) -> {ok, SessionId} | {error, login_failed | user_suspended | password_expired}` backed by a SessionTable and UserTable.

# Relationships

## Builds Upon
- **Semantic node type** — Interfaces are defined after the system is split into node types

## Enables
- Defining interfaces enables business-logic implementation, standalone testing, and end-to-end testing.

## Related
- **Logic node** — Interfaces are exported by logic nodes among others
- **Service node** — Service nodes export interfaces to logic nodes

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Trying to enumerate every failure case while first defining interfaces
  **Correction**: At this stage think of positive use cases; cover only errors defined in the business logic, leaving crashes and network errors to the retry-strategy step.

# Common Confusions

- **Confusion**: The first interface design will be correct.
  **Clarification**: Interface design is iterative — "Don't think you'll get it right on your first try" (p. 399); expect to rearrange tables and reduce data duplication.

# Source Reference

Chapter 12: Distributed Architectures, "Interfaces," pages 396-399. See Table 13-1 (Interfaces and tables).

# Verification Notes

- Definition source: Synthesized from pp. 396-399; key phrases quoted directly.
- Confidence rationale: HIGH — the source dedicates a named section with an explicit checklist and worked table.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
