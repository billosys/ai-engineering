---
# === CORE IDENTIFICATION ===
concept: Logic Node
slug: logic-node

# === CLASSIFICATION ===
category: distribution
subcategory: node-model
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Distributed Architectures"
chapter_number: 12
pdf_page: 378
section: "Node Types and Families"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - logic node
  - back-end node
  - business logic node

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semantic-node-type
extends:
  - semantic-node-type
related:
  - front-end-node
  - service-node
contrasts_with:
  - front-end-node
  - service-node

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a logic node?"
  - "How do I split a system into node types?"
---

# Quick Definition

A logic node, also called a back-end node, implements the system's business logic, handling client requests forwarded from front-end nodes. It is the important intermediary and checkpoint of a three-layer architecture.

# Core Definition

"Logic nodes, also commonly referred to as back-end nodes, implement the system's business logic. They contain all of the code needed to handle client requests forwarded from the front-end nodes. They might also cache session data and access external services in other nodes when handling requests" (Cesarini & Vinoski, p. 379). Regardless of the architectural pattern, "the logic node is an important intermediary and checkpoint" — front-end nodes should avoid communicating directly with service nodes (p. 381).

# Prerequisites

- **Semantic node type** — Logic node is one of the three semantic node types; understand the classification first.

# Key Properties

1. Implements the system's business logic.
2. Contains all code needed to handle client requests forwarded from front-end nodes.
3. May cache session data locally.
4. May access external services in service nodes when handling requests.
5. Acts as the intermediary and checkpoint between front-end and service nodes.
6. Typically needs more cores and memory (computationally intensive routing and logic).

# Construction / Recognition

## To Construct/Create:
1. Place all business-logic code on the node.
2. Receive parsed requests from front-end nodes.
3. Validate requests, authenticate via service nodes, and cache session state as needed.
4. Return results to the front-end node.

## To Identify/Recognize:
1. A node is a logic node if it runs business logic and mediates between front-end and service nodes.

# Context & Application

- **Typical contexts**: The middle tier of a three-layer distributed architecture.
- **Common applications**: Request validation, session creation and caching, routing requests to service nodes.
- **Historical/stylistic notes**: For security, logic nodes can use distributed Erlang transparently among themselves behind a firewall, while communicating with front-end nodes over sockets (pp. 383-384).

# Examples

**Example 1** (p. 380): In the e-commerce login example, the logic node checks request validity, authenticates the user via an authentication server, creates and caches a session ID and record locally, and returns the session ID to the front-end node.

**Example 2** (p. 398): The logic node generalizes login error cases — returning `login_failed`, `user_suspended`, or `password_expired` — without revealing whether the UserId or Password is incorrect, as a security measure.

# Relationships

## Builds Upon
- **Semantic node type** — A logic node is a specific semantic node type

## Enables
- **Service node** — Logic nodes route requests onward to service nodes

## Related
- **Front-end node** — The logic node's upstream counterpart
- **Service node** — The logic node's downstream counterpart

## Contrasts With
- **Front-end node** — Logic handles business logic; front-end handles connectivity
- **Service node** — Logic implements the system's own logic; service provides a backing service

# Common Errors

- **Error**: Bypassing the logic node so front-end nodes talk straight to service nodes
  **Correction**: Route through the logic node — it is the architectural intermediary and checkpoint.

# Common Confusions

- **Confusion**: "Back-end node" means the database.
  **Clarification**: The logic/back-end node runs business logic; the database is a service node.

# Source Reference

Chapter 12: Distributed Architectures, "Node Types and Families," pages 379-381, and "Interfaces," pages 396-399.

# Verification Notes

- Definition source: Direct quote from p. 379.
- Confidence rationale: HIGH — explicit definition in source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
