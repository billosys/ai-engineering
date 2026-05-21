---
# === CORE IDENTIFICATION ===
concept: Service Orientation and Microservices
slug: microservices-architecture

# === CLASSIFICATION ===
category: distribution
subcategory: architectural-patterns
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Distributed Architectures"
chapter_number: 12
pdf_page: 378
section: "Service Orientation and Microservices"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - microservices
  - SOA
  - service-oriented architecture

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semantic-node-type
extends: []
related:
  - service-discovery
  - cluster
  - peer-to-peer-architecture
contrasts_with:
  - peer-to-peer-architecture

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a microservices architecture?"
  - "What distributed architectural patterns can I choose?"
---

# Quick Definition

Service orientation and microservices are architectural patterns in which loosely coupled processes or nodes provide standalone services to one another, connected by a service bus, together delivering the system's functionality.

# Core Definition

Microservices and service-oriented architectures (SOA) are "similar in concept to the client-server paradigm where processes and nodes (or node families) provide services to other nodes and processes. These services, often standalone or loosely coupled, together provide the functionality required by your system. They are often expressed in terms of an API, where each service (or function) implements an action invoked by a node requesting the service" (Cesarini & Vinoski, p. 394). Services are connected by a service bus and use a protocol describing how they exchange and interpret messages, described with service metadata.

# Prerequisites

- **Semantic node type** — Microservices map onto node types providing services; understand node classification first.

# Key Properties

1. Loosely coupled, standalone services together provide the system's functionality.
2. Each service is expressed as an API implementing an action invoked by a requester.
3. Services are connected by a service bus running over a network.
4. A service bus uses a protocol describing how services exchange and interpret messages.
5. Service metadata describes what each service does and the data it requires, enabling dynamic discovery.
6. Standardized protocols allow combining ready-made or multi-language components.
7. SOA is considered heavyweight by some but its ideas are fundamental to microservices.

# Construction / Recognition

## To Construct/Create:
1. Package functionality as standalone, loosely coupled services with APIs.
2. Connect them via a service bus running a chosen protocol (SOAP, HTTP, AMQP).
3. Describe each service with metadata so others can dynamically discover and use it.
4. Package services generically to encourage reuse across services and systems.

## To Identify/Recognize:
1. Recognize the pattern by independently deployable services communicating over a bus via well-defined APIs.

# Context & Application

- **Typical contexts**: Enterprise systems and scalable distributed systems.
- **Common applications**: Client front-end interfaces, authentication databases, logging, alarming, logic and service nodes packaged as reusable services.
- **Historical/stylistic notes**: SOA is "considered heavyweight and old-fashioned by some" but widely used in enterprise systems; its ideas are fundamental to microservices (p. 394).

# Examples

**Example 1** (p. 394, Figure 13-9): A service-oriented architecture whose services include client front-end interfaces, authentication databases, logging, alarming, logic nodes, and other service nodes.

**Example 2** (pp. 394-395): Messages between services are often defined using JSON, XML, Protocol Buffers, Erlang terms, or OMG IDL; requests can be sent using SOAP, HTTP, or AMQP, over web services, Java RMI, Thrift, or Erlang RPC.

# Relationships

## Builds Upon
- **Semantic node type** — Services map onto node types providing functionality

## Enables
- **Service discovery** — Microservices rely on dynamic discovery via metadata
- **Cluster** — Each cluster of nodes can provide a set of services

## Related
- **Service discovery** — The mechanism for finding services dynamically
- **Cluster** — Clusters often provide sets of microservices

## Contrasts With
- **Peer to peer architecture** — Microservices follow a client-server model where some node types serve others; p2p has all nodes equal

# Common Errors

- **Error**: Ignoring the encoding/parsing overhead of standardized protocols
  **Correction**: Standardized protocols aid reuse and multi-language interoperability but add overhead in data size and request encoding/parsing — account for it.

# Common Confusions

- **Confusion**: Microservices and SOA are unrelated.
  **Clarification**: They are similar in concept; SOA's ideas are fundamental to microservices.

# Source Reference

Chapter 12: Distributed Architectures, "Service Orientation and Microservices," pages 394-396. See Figure 13-9.

# Verification Notes

- Definition source: Direct quote from p. 394.
- Confidence rationale: HIGH — the source dedicates a named section to the pattern with explicit characterization.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
