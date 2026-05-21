---
# === CORE IDENTIFICATION ===
concept: Process-per-Value Cache Design
slug: cache-system-design

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-design
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Implementing a caching system"
chapter_number: 6
pdf_page: null
section: "6.2 The design of your cache"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - simple cache design
  - "process-per-value cache"
  - "Simple Cache architecture"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - otp-application
extends: []
related:
  - sc-element
  - sc-store
  - application-api-module
  - simple-one-for-one
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is the Simple Cache designed?"
  - "Why store each cached value in its own process?"
  - "What modules make up the Simple Cache application?"
---

# Quick Definition

The Simple Cache design stores each cached value in its own process and keeps a mapping from each key to that process, so every value can have its own life cycle.

# Core Definition

The Simple Cache stores key/value pairs where keys are unique and each key maps to a single value (Ch. 6, Section 6.2). The core idea is to use a separate process to store each value, and to map each key to its corresponding process. This may seem strange, but for a cache it makes sense, because every value may have its own life cycle (e.g. its own lease/expiry); Erlang's support for large numbers of lightweight processes makes the approach practical. The cache is built from five modules: `simple_cache` (the user API), `sc_app` (the application behaviour), `sc_sup` (the root supervisor), `sc_store` (the key-to-pid mapping), and `sc_element` (the value-storage processes). To retrieve a value, you first look up the storage process's pid in `sc_store`, then query that process — an indirect key-to-value mapping.

# Prerequisites

- **Process** — Each value lives in its own lightweight process.
- **OTP application** — The cache is built as a single OTP application.

# Key Properties

1. Stores unique key/value pairs; each key maps to one value.
2. Each cached value is stored in its own separate process.
3. Each key maps to its value's storage process — an indirect key-to-value mapping.
4. Built from five modules: `simple_cache`, `sc_app`, `sc_sup`, `sc_store`, `sc_element`.
5. Per-value processes make per-value life cycles (leases) trivial.
6. Relies on Erlang's cheap, numerous lightweight processes.

# Construction / Recognition

## To Build the Cache (high level):
1. Create an OTP application skeleton (`sc_app`, `sc_sup`).
2. Implement `sc_element` — a `gen_server` per stored value.
3. Implement `sc_store` — the key-to-pid mapping (ETS-backed).
4. Implement `simple_cache` — the user-facing API tying it together.

# Context & Application

The design is the running narrative of Part 2: a cache to speed up the Erlware website by caching package listings locally, keyed by URL.

- **Typical contexts**: A local, in-memory, single-machine cache for speeding up a web server.
- **Common applications**: Caching package-listing pages keyed by URL.

# Examples

**Example 1** (Ch. 6, Table 6.1): The five modules — `simple_cache`, `sc_app`, `sc_sup`, `sc_store`, `sc_element` — and their purposes.

**Example 2** (Ch. 6, Figure 6.5): A key maps indirectly to its value: key → storage process pid → stored value.

# Relationships

## Related
- **sc-element** — The per-value storage processes.
- **sc-store** — The key-to-pid mapping.
- **application-api-module** — `simple_cache` is the front-end API.
- **simple-one-for-one** — The supervision strategy used for the storage processes.

## Contrasts With
- This is a design; the source draws no direct contrast.

# Common Errors

- **Error**: Assuming a process per value is wasteful.
  **Correction**: Erlang processes are lightweight; per-value processes make per-value leases and life cycles trivial.

# Common Confusions

- **Confusion**: Thinking keys map directly to values.
  **Clarification**: The mapping is indirect — key to storage-process pid, then pid to value.

# Source Reference

Chapter 6: Implementing a caching system, Sections 6.1 and 6.2, Table 6.1 and Figures 6.3–6.5.

# Verification Notes

- Definition source: Direct adaptation of Sections 6.1–6.2.
- Confidence rationale: HIGH — explicit, dedicated design section.
- Uncertainties: None.
- Cross-reference status: References Agent-1 slug `process` and planned cards.
- Re-extraction notes: Fresh extraction; no prior card existed.
