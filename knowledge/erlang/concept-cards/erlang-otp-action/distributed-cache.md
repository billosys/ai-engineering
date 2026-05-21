---
# === CORE IDENTIFICATION ===
concept: Distributed Cache
slug: distributed-cache

# === CLASSIFICATION ===
category: distribution
subcategory: communication-strategy
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding distribution to the cache with Mnesia"
chapter_number: 9
pdf_page: null
section: "9.1 Distributing the cache"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "distributed cache application"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-erlang
  - erlang-cluster
extends: []
related:
  - asynchronous-communication
  - synchronous-communication
  - mnesia
  - location-transparency
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a distributed cache?"
  - "Why does the Simple Cache need to become distributed?"
  - "What part of the cache actually needs to be distributed?"
---

# Quick Definition

A distributed cache is a cache whose instances on different nodes are aware of each other and share data, so any instance can answer a query regardless of which node originally stored the data.

# Core Definition

A distributed cache is a cache in which each instance is aware of the others, so any instance can return the current value for a key regardless of which server last saved it. The book extends the Simple Cache into one to support session storage behind a stateless load balancer: because a user's successive requests may be served by different web servers, session data must be available to all of them. Crucially, the cache is structured so storage-element processes hold the data and a table maps each key to the process identifier of its storage element — and because of Erlang's location transparency, only that key-to-pid table needs to be distributed, not the data itself. Storage processes can stay on the node where they were created as long as every node has access to the key-to-pid mapping; Mnesia is used to distribute that table (Ch. 9, Sections 9.1 and 9.1.3).

# Prerequisites

- **distributed-erlang** — A distributed cache spans multiple nodes.
- **erlang-cluster** — The cache instances are nodes in a cluster.

# Key Properties

1. Cache instances on different nodes are mutually aware.
2. Any instance can return the value for any key.
3. Storage-element processes hold the actual data.
4. A key-to-pid table maps keys to their storage processes.
5. Only the key-to-pid table needs to be distributed, not the data.
6. Location transparency lets storage processes stay on their original node.

# Construction / Recognition

## To Build a Distributed Cache:
1. Choose a communication strategy (asynchronous vs. synchronous).
2. Distribute the key-to-pid mapping table (e.g., with Mnesia).
3. Make each cache aware of the other nodes (join the cluster).
4. Use resource discovery to find peer cache instances.
5. Bring the shared table into dynamic replication.

## To Recognize:
1. A cache whose key-to-pid table is shared across nodes is a distributed cache.

# Context & Application

- **Typical contexts**: Session storage behind a stateless load balancer; shared runtime state.
- **Common applications**: The book's Simple Cache turned into a session store for the Erlware site.
- **Historical/stylistic notes**: Fetching data from a storage process on another server is still far faster than re-fetching from the original source.

# Examples

**Example 1** (Section 9.1): A user logs in on one web server but the next page is served from another; without a distributed cache, the second server cannot find the session.

**Example 2** (Section 9.1.3, Figure 9.7): Two cache instances share a replicated key-to-pid table; only the table is distributed, and storage processes are reached via location transparency.

# Relationships

## Builds Upon
- **distributed-erlang** — The cache spans distributed nodes.
- **erlang-cluster** — Cache instances form a cluster.

## Enables
- None.

## Related
- **asynchronous-communication** / **synchronous-communication** — The two candidate strategies for the cache.
- **mnesia** — Used to distribute the key-to-pid table.
- **location-transparency** — Lets storage processes stay put while only the table is shared.

## Contrasts With
- None.

# Common Errors

- **Error**: Distributing the cached data itself across all nodes.
  **Correction**: Only the key-to-pid table needs distributing; location transparency lets storage processes stay on their node.

# Common Confusions

- **Confusion**: Thinking a distributed cache must copy all values to every node.
  **Clarification**: It distributes the key-to-pid mapping; the data stays in storage processes reached transparently.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.1 "Distributing the cache," subsection 9.1.3 "If you only had a distributed table…," Figures 9.1 and 9.7.

# Verification Notes

- Definition source: Synthesized from Sections 9.1 and 9.1.3.
- Confidence rationale: HIGH — the book extensively describes the distributed cache design.
- Uncertainties: None.
- Cross-reference status: Verified.
