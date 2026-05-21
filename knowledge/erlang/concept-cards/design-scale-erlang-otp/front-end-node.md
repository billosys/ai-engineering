---
# === CORE IDENTIFICATION ===
concept: Front-End Node
slug: front-end-node

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
  - front-end node
  - web server node
  - gateway node

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semantic-node-type
extends:
  - semantic-node-type
related:
  - logic-node
  - service-node
  - demilitarized-zone
contrasts_with:
  - logic-node
  - service-node

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a front-end node?"
  - "How do I split a system into node types?"
---

# Quick Definition

A front-end node provides external connectivity to clients, keeping connections open, handling incoming requests, formatting them, and passing them on to logic nodes. It is the gateway of a distributed Erlang system.

# Core Definition

"Front-end nodes are responsible for providing external connectivity to clients and handling all incoming requests. They act as gateways, keeping client connections open as needed, formatting inbound requests and outbound responses, and passing the requests onward to the nodes handling the business logic. They are part of the server-side software, serving, but not running, the presentation layer" (Cesarini & Vinoski, p. 379).

# Prerequisites

- **Semantic node type** — Front-end node is one of the three semantic node types; understand the classification first.

# Key Properties

1. Provides external connectivity to clients (web browsers, mobile apps).
2. Acts as a gateway, keeping client connections open as needed.
3. Formats inbound requests and outbound responses (e.g., parsing JSON into Erlang terms and back).
4. Passes requests onward to logic nodes; should avoid communicating directly with service nodes.
5. Part of the server-side software — serves the presentation layer but does not run it.
6. Often placed in a demilitarized zone (DMZ) for security.

# Construction / Recognition

## To Construct/Create:
1. Run an Erlang web server (e.g., Yaws, Webmachine, Cowboy) on the node.
2. Keep pools of client connections open.
3. Parse inbound requests into Erlang terms and forward them to logic nodes.
4. Encode logic-node responses and return them to clients.

## To Identify/Recognize:
1. A node is a front-end node if its job is external connectivity and request/response formatting, not business logic.

# Context & Application

- **Typical contexts**: The entry point of a three-layer distributed architecture.
- **Common applications**: HTTP request handling; keeping millions of TCP connections open; placement in a DMZ to shield logic and service nodes.
- **Historical/stylistic notes**: Front-end nodes may be memory-bound (many idle connections) or CPU-bound (heavy JSON/XML parsing), requiring different hardware (p. 408).

# Examples

**Example 1** (p. 380): In the e-commerce login example, a web server running on the front-end node receives a REST/JSON login request, parses it into Erlang terms, and forwards the login request, user ID, and encrypted password to the logic node.

**Example 2** (p. 383, Figure 13-2): Front-end nodes placed in a demilitarized zone (perimeter network) to reduce the risk of intrusion into logic and service nodes.

# Relationships

## Builds Upon
- **Semantic node type** — A front-end node is a specific semantic node type

## Enables
- **Logic node** — Front-end nodes forward parsed requests to logic nodes

## Related
- **Logic node** — The front-end's downstream counterpart
- **Demilitarized zone** — Front-end nodes are typically placed in a DMZ

## Contrasts With
- **Logic node** — Front-end handles connectivity/formatting; logic handles business logic
- **Service node** — Front-end nodes should avoid communicating directly with service nodes

# Common Errors

- **Error**: Having front-end nodes communicate directly with service nodes
  **Correction**: Although not illegal, it leads to poor structure; route through the logic node, which is the important intermediary and checkpoint (p. 381).

- **Error**: Connecting front-end and logic nodes with distributed Erlang in a DMZ deployment
  **Correction**: Use sockets (possibly encrypted) so an intruder who compromises a front-end node does not gain full access to logic and service nodes.

# Common Confusions

- **Confusion**: Front-end nodes run the presentation layer.
  **Clarification**: They serve the presentation layer but do not run it; they are server-side software.

# Source Reference

Chapter 12: Distributed Architectures, "Node Types and Families," pages 379-381, and "Networking," pages 382-384. See Figures 13-1 and 13-2.

# Verification Notes

- Definition source: Direct quote from p. 379.
- Confidence rationale: HIGH — explicit definition in source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
