---
# === CORE IDENTIFICATION ===
concept: Client-Server Model
slug: client-server-model

# === CLASSIFICATION ===
category: otp-behaviours
subcategory: design-patterns
tier: foundational

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "gen_server Behaviour"
chapter_number: null
pdf_page: null
section: "Client-Server Principles"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "client-server relation"
  - "client-server principles"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - gen-server
  - gen-server-call
  - gen-server-cast
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the client-server model in OTP?"
  - "How does the client-server model relate to gen_server?"
---

# Quick Definition

The client-server model in OTP is characterized by a central server process and an arbitrary number of client processes, used for resource management where multiple clients share a common resource managed by the server.

# Core Definition

According to the gen_server Behaviour chapter: "The client-server model is characterized by a central server and an arbitrary number of clients. The client-server model is used for resource management operations, where several different clients want to share a common resource. The server is responsible for managing this resource."

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. One central server process manages a shared resource.
2. An arbitrary number of client processes interact with the server.
3. Clients send queries (requests) to the server.
4. The server sends replies back to clients.
5. Used for resource management operations.
6. In OTP, formalized by the `gen_server` behaviour.

# Construction / Recognition

## To Construct/Create:
1. Identify the shared resource to be managed.
2. Implement a server process using `gen_server` to manage the resource state.
3. Define a client API (interface functions) that sends requests to the server.
4. Use synchronous calls when clients need replies and asynchronous casts when they do not.

## To Identify/Recognize:
1. A process that maintains state and responds to requests from other processes.
2. Multiple processes send requests to a single managing process.
3. Communication follows a query/reply pattern.

# Context & Application

The client-server model is the foundational design pattern behind `gen_server`, the most widely used OTP behaviour. Any scenario where multiple processes need coordinated access to a shared resource — such as a pool of channels, a database connection, or a configuration store — is modeled as a client-server relation in OTP.

# Examples

**Example 1** (gen_server_concepts.md, "Client-Server Principles"): The source provides a diagram showing three client processes communicating with a single server process. Clients send queries (solid arrows) and receive replies (dashed arrows). The channel allocation server (`ch3`) is the running example: clients call `alloc()` to request a channel and `free(Ch)` to release one.

# Relationships

## Builds Upon
- No prerequisites — this is a foundational design pattern.

## Enables
- **gen_server** — gen_server is the OTP formalization of the client-server model
- **gen_server:call** — the synchronous request mechanism (query with reply)
- **gen_server:cast** — the asynchronous request mechanism (query without reply)

## Related
- **Behaviour** — the client-server model is one of the patterns formalized by OTP behaviours

## Contrasts With
- No direct contrasts in the source.

# Common Errors

- **Error**: Having clients directly access shared state instead of going through the server.
  **Correction**: All access to the shared resource should be mediated by the server process to ensure consistency and serialization.

# Common Confusions

- **Confusion**: Thinking "client" and "server" are fixed roles for processes.
  **Clarification**: Any process can act as a client when it sends a request to a gen_server. The same process could be a server for some resource and a client of another server.

# Source Reference

OTP Design Principles, "gen_server Behaviour" chapter, "Client-Server Principles" section (gen_server_concepts.md).

# Verification Notes

- Definition source: Directly quoted from gen_server_concepts.md "Client-Server Principles" section.
- Confidence rationale: High — explicitly defined in a dedicated section of the source.
- Uncertainties: None.
- Cross-reference status: References gen-server, gen-server-call, gen-server-cast (planned cards).
