---
# === CORE IDENTIFICATION ===
concept: Service Discovery
slug: service-discovery

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
section: "Service Orientation and Microservices — Gproc"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - gproc
  - process registry

# === TYPED RELATIONSHIPS ===
prerequisites:
  - microservices-architecture
extends: []
related:
  - cluster
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is service discovery?"
  - "How do services find each other in a distributed system?"
---

# Quick Definition

Service discovery lets nodes publish and dynamically find one another's services via a registry of process metadata. Gproc is the Erlang application the book presents for this purpose.

# Core Definition

Service metadata in a service-oriented architecture "should be in a format that allows nodes to dynamically configure and publicize their services, which in turn allows other services to dynamically discover and use them" (Cesarini & Vinoski, p. 395). The book presents Gproc as the discovery tool: "Gproc is an application by Ulf Wiger used for service discovery. It provides a registry where you can store metadata that describes process roles and characteristics. It allows you to use any Erlang term to register a process, and allows multiple aliases to a single process. ... The registry is global, allowing the process metadata to be distributed and accessed across multiple nodes" (p. 395).

# Prerequisites

- **Service orientation and microservices** — Discovery is the mechanism that makes a service architecture dynamic; understand the pattern first.

# Key Properties

1. Lets nodes dynamically publicize their services and lets others discover them.
2. Backed by a registry of metadata describing process roles and characteristics.
3. Gproc allows any Erlang term to register a process.
4. Gproc allows multiple aliases to a single process.
5. Nonunique process properties can be stored and queried using match specifications and query list comprehensions.
6. Gproc's registry is global, distributing process metadata across multiple nodes.

# Construction / Recognition

## To Construct/Create:
1. Register each process/service with metadata describing its role and characteristics.
2. Use a global registry (such as Gproc) so the metadata is accessible across nodes.
3. Query the registry with match specifications to discover services.

## To Identify/Recognize:
1. Recognize service discovery by a queryable registry of service metadata accessible across nodes.

# Context & Application

- **Typical contexts**: Service-oriented and microservices architectures.
- **Common applications**: Publishing process roles, finding processes by property, distributing process metadata across a cluster.
- **Historical/stylistic notes**: Gproc and its documentation are on GitHub (Ulf Wiger).

# Examples

**Example 1** (p. 395): Gproc provides a registry where you store metadata describing process roles and characteristics, and allows you to use any Erlang term to register a process.

**Example 2** (p. 395): Gproc's nonunique process properties can be stored and queried using match specifications and query list comprehensions; the registry is global so metadata is accessible across multiple nodes.

# Relationships

## Builds Upon
- **Service orientation and microservices** — Discovery makes service architectures dynamic

## Enables
- Service discovery enables dynamic, decoupled connection of services across a cluster.

## Related
- **Cluster** — Discovery distributes metadata across cluster nodes

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Hardcoding service locations
  **Correction**: Publish service metadata to a registry so services can be discovered dynamically as nodes come and go.

# Common Confusions

- **Confusion**: Service discovery requires unique process names.
  **Clarification**: Gproc allows multiple aliases per process and nonunique properties that can be queried.

# Source Reference

Chapter 12: Distributed Architectures, "Service Orientation and Microservices — Gproc," page 395.

# Verification Notes

- Definition source: Synthesized from pp. 394-395; Gproc description quoted from p. 395.
- Confidence rationale: MEDIUM — the source describes service discovery and Gproc clearly but as a tool sidebar rather than a formally defined standalone concept.
- Uncertainties: The general notion of service discovery is described through the Gproc tool rather than abstractly.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
