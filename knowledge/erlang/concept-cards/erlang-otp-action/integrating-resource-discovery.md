---
# === CORE IDENTIFICATION ===
concept: Integrating Resource Discovery
slug: integrating-resource-discovery

# === CLASSIFICATION ===
category: distribution
subcategory: resource-discovery
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding distribution to the cache with Mnesia"
chapter_number: 9
pdf_page: null
section: "9.3.3 Integrating resource discovery to find other cache instances"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "resource discovery integration"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - resource-discovery
  - distributed-cache
extends: []
related:
  - resource-trading
  - cluster-contact-node
  - mnesia-dynamic-replication
  - otp-application
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is resource discovery integrated into an application?"
  - "How does the cache publish itself and find other instances?"
  - "Where in the application startup does resource discovery go?"
---

# Quick Definition

Integrating resource discovery means packaging it as its own application and having the host application, at startup, publish its local resource, declare the resource type it wants, trigger trading, and wait for results.

# Core Definition

Integrating resource discovery is the step of wiring the generic resource discovery system into a host application (Ch. 9, Section 9.3.3). Because resource discovery is a generic service usable by any application, it should be packaged as an application in its own right — with its own directory structure, `.app` file, `_app` module, and `_sup` module — and placed alongside the host application. The host's `.app` file is updated to declare the dependency on `resource_discovery` (and `mnesia`). At startup, in `sc_app:start/2` right after joining the cluster, the cache: publishes itself with `resource_discovery:add_local_resource(simple_cache, node())` (an "I have"); declares interest with `resource_discovery:add_target_resource_type(simple_cache)` (an "I want"); calls `resource_discovery:trade_resources()`; and then `timer:sleep(?WAIT_FOR_RESOURCES)` to wait a reasonable time for the asynchronous trading to share results — after which the node knows all other cache instances and they know it.

# Prerequisites

- **resource-discovery** — Integration wires the discovery system into an application.
- **distributed-cache** — The cache is the application integrating discovery.

# Key Properties

1. Resource discovery is packaged as its own OTP application.
2. The host application declares a dependency on `resource_discovery`.
3. At startup the host publishes a local resource ("I have").
4. The host declares a target resource type ("I want").
5. The host triggers `trade_resources()` and then sleeps to await results.
6. After integration, all instances know about each other.

# Construction / Recognition

## To Integrate Resource Discovery:
1. Package resource discovery as a standalone application alongside the host.
2. Add the dependency to the host's `.app` file.
3. In `start/2`, call `add_local_resource(Type, node())` and `add_target_resource_type(Type)`.
4. Call `trade_resources()`, then `timer:sleep(WaitTime)`.

## To Recognize:
1. Startup code calling `add_local_resource`, `add_target_resource_type`, and `trade_resources` integrates discovery.

# Context & Application

- **Typical contexts**: Any application that must locate peers in a cluster.
- **Common applications**: The Simple Cache finding other cache instances before initializing storage.
- **Historical/stylistic notes**: The integration code goes in `sc_app:start/2` right after the cluster-join code and before `sc_store:init()`.

# Examples

**Example 1** (Section 9.3.3): `resource_discovery:add_local_resource(simple_cache, node())` publishes the cache; `resource_discovery:add_target_resource_type(simple_cache)` declares it wants other caches.

**Example 2** (Section 9.3.3, Listing 9.6): `sc_app:start/2` calls `ensure_contact()`, then the three resource-discovery functions, then `timer:sleep(?WAIT_FOR_RESOURCES)` (2500 ms), then `sc_store:init()`.

# Relationships

## Builds Upon
- **resource-discovery** — Integration deploys and uses the discovery system.
- **distributed-cache** — The cache is the host application.

## Enables
- **mnesia-dynamic-replication** — Discovered instances are the nodes the cache replicates with.

## Related
- **resource-trading** — Integration triggers trading at startup.
- **cluster-contact-node** — Integration happens right after the cluster-join step.
- **OTP application** — Resource discovery is packaged as its own application.

## Contrasts With
- None.

# Common Errors

- **Error**: Querying discovered resources immediately after `trade_resources()`.
  **Correction**: Trading is asynchronous; `timer:sleep` for a reasonable interval so results can propagate first.

# Common Confusions

- **Confusion**: Squeezing resource discovery into the host application as internal code.
  **Clarification**: It is generic; package it as its own application and depend on it.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.3.3 "Integrating resource discovery to find other cache instances," Listings 9.5 and 9.6.

# Verification Notes

- Definition source: Directly adapted from Section 9.3.3.
- Confidence rationale: HIGH — the book shows the integration code explicitly.
- Uncertainties: None.
- Cross-reference status: Verified.
