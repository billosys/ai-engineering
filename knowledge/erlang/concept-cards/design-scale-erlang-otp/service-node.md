---
# === CORE IDENTIFICATION ===
concept: Service Node
slug: service-node

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
  - service node

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semantic-node-type
extends:
  - semantic-node-type
related:
  - front-end-node
  - logic-node
contrasts_with:
  - front-end-node
  - logic-node

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a service node?"
  - "How do I split a system into node types?"
---

# Quick Definition

A service node provides a service — such as a database, authentication server, or payment gateway — to the logic nodes. It may itself bridge to third-party services and APIs.

# Core Definition

"Service nodes ... provide a service to the logic nodes. Such a service could be a database, an authentication server, or a payment gateway. Service nodes could themselves provide connectivity toward third-party services and APIs" (Cesarini & Vinoski, p. 379). Service nodes are the third of the three semantic node types and sit downstream of the logic nodes.

# Prerequisites

- **Semantic node type** — Service node is one of the three semantic node types; understand the classification first.

# Key Properties

1. Provides a backing service to logic nodes (database, authentication, payment, etc.).
2. May provide connectivity toward third-party services and APIs.
3. Sits downstream of logic nodes; front-end nodes should not contact it directly.
4. Often I/O-bound (e.g., a node managing a database needs a fast hard disk).

# Construction / Recognition

## To Construct/Create:
1. Implement or wrap the backing service (database, auth server, payment gateway).
2. Expose an interface that logic nodes call.
3. Optionally provide connectivity to external third-party APIs.

## To Identify/Recognize:
1. A node is a service node if its purpose is to serve other node types with a discrete service.

# Context & Application

- **Typical contexts**: The bottom tier of a three-layer distributed architecture.
- **Common applications**: Databases, authentication servers, payment gateways, analytics and storage clusters.
- **Historical/stylistic notes**: In a star architecture, service nodes connected to each other can be used for storage and analytics, scaling dynamically based on load (p. 390).

# Examples

**Example 1** (p. 379): An authentication server that the logic node consults during login is a service node.

**Example 2** (p. 399): The authentication server's interface — `auth(UserId, Password) -> {ok, UserData} | {error, unknown_user | bad_password | user_suspended | password_expired}` — backed by a UserTable.

# Relationships

## Builds Upon
- **Semantic node type** — A service node is a specific semantic node type

## Enables
- Service nodes provide the backing services that logic nodes depend on.

## Related
- **Logic node** — The service node's upstream counterpart
- **Front-end node** — Should not contact service nodes directly

## Contrasts With
- **Logic node** — Service provides a backing service; logic implements business logic
- **Front-end node** — Service is the deepest tier; front-end is the outermost

# Common Errors

- **Error**: Exposing service-node interfaces to front-end nodes or untrusted networks
  **Correction**: Keep service nodes behind a firewall in a safe environment, reachable only via logic nodes.

# Common Confusions

- **Confusion**: A service node must be written in Erlang.
  **Clarification**: A service node could be a database "possibly (but not necessarily) written in Erlang" (p. 379).

# Source Reference

Chapter 12: Distributed Architectures, "Node Types and Families," pages 379-381.

# Verification Notes

- Definition source: Direct quote from p. 379.
- Confidence rationale: HIGH — explicit definition in source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
