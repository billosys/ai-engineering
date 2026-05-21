---
# === CORE IDENTIFICATION ===
concept: Resource Discovery
slug: resource-discovery

# === CLASSIFICATION ===
category: distribution
subcategory: resource-discovery
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Introducing distributed Erlang/OTP"
chapter_number: 8
pdf_page: null
section: "8.3 The nuts and bolts of resource discovery"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "resource discovery system"
  - "service discovery"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-erlang
  - erlang-cluster
extends: []
related:
  - resource-discovery-terminology
  - resource-discovery-algorithm
  - gen-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is resource discovery?"
  - "Why use resource discovery instead of hardcoded service locations?"
  - "What benefits does a dynamic resource discovery system provide?"
---

# Quick Definition

Resource discovery is a peer-to-peer mechanism that lets services in an Erlang cluster locate one another dynamically — like yellow pages — without hardcoded knowledge of where each resource lives.

# Core Definition

Resource discovery is a technique that lets providers and consumers of services in a cluster find one another without prior knowledge of the system layout, replacing hardcoded resource locations. The book builds a resource discovery application that functions like the yellow pages: each node in the cluster runs a local instance, and each instance discovers and caches information about the available resources in the cluster. This distributed, dynamic approach is flexible and powerful — there is no single point of failure (it is peer-to-peer), no hardcoded network topology, easier scaling, the ability to run many services in one node, and easier upgrades since removed services become unregistered and new ones are discovered as they come online (Ch. 8, Section 8.3).

# Prerequisites

- **distributed-erlang** — Resource discovery operates over distributed nodes.
- **erlang-cluster** — Discovery happens within a cluster of connected nodes.

# Key Properties

1. Lets services find each other without hardcoded locations.
2. Peer-to-peer — no single point of failure.
3. Each node runs a local instance that caches discovered resources.
4. Works with one node as well as many (location transparent).
5. Supports dynamic add/remove of services.
6. Removes the need to recompile or reconfigure when topology changes.

# Construction / Recognition

## To Use Resource Discovery:
1. Run a resource discovery server on each node.
2. Register local resources ("I have") and target resource types ("I want").
3. Trigger resource trading so nodes exchange this information.
4. Fetch discovered resources of a wanted type when needed.

## To Recognize:
1. Code that publishes local resources and queries the cluster for resource types by tag uses resource discovery.

# Context & Application

- **Typical contexts**: Dynamic clusters, cloud environments, systems whose topology changes.
- **Common applications**: Letting cache instances find each other; locating logging or other services.
- **Historical/stylistic notes**: The book's version is a deliberately simple single-module exercise; a fuller multi-module OTP version exists at erlware.org.

# Examples

**Example 1** (Section 8.3): The discovery system functions "a bit like the yellow pages" — each node caches information about available resources in the cluster.

**Example 2** (Section 9.3.3): The Simple Cache uses resource discovery to publish itself as a `simple_cache` resource and to find other cache instances in the cluster.

# Relationships

## Builds Upon
- **distributed-erlang** — Resource discovery is a distributed application.
- **erlang-cluster** — It operates across cluster nodes.

## Enables
- None.

## Related
- **resource-discovery-terminology** — Defines resource, resource type, resource tuple.
- **resource-discovery-algorithm** — The synchronization procedure between nodes.
- **gen_server** — The discovery server is implemented as a `gen_server`.

## Contrasts With
- None.

# Common Errors

- **Error**: Relying on stale discovery data after nodes have crashed.
  **Correction**: The simple version does not auto-clean vanished nodes; periodically re-ping and re-trade to keep data fresh.

# Common Confusions

- **Confusion**: Assuming resource discovery requires multicast/broadcast networking.
  **Clarification**: The book's version is implemented entirely with Erlang message passing; multicast is one alternative, not a requirement.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.3 "The nuts and bolts of resource discovery," subsections 8.3.1–8.3.3.

# Verification Notes

- Definition source: Synthesized from Section 8.3's introduction.
- Confidence rationale: HIGH — the book devotes a full section to motivating and building it.
- Uncertainties: None.
- Cross-reference status: Verified.
