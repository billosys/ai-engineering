---
# === CORE IDENTIFICATION ===
concept: Mnesia
slug: mnesia

# === CLASSIFICATION ===
category: distribution
subcategory: mnesia
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding distribution to the cache with Mnesia"
chapter_number: 9
pdf_page: null
section: "9.2 Distributed data storage with Mnesia"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Mnesia database"
  - "mnesia"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
extends: []
related:
  - mnesia-schema
  - mnesia-table
  - mnesia-transaction
  - ets
contrasts_with:
  - ets

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Mnesia?"
  - "What is Mnesia good for and what are its limits?"
  - "Why use Mnesia instead of an SQL database?"
---

# Quick Definition

Mnesia is Erlang/OTP's built-in lightweight, soft real-time, distributed, replicated, transactional data store; it stores Erlang terms natively and is best suited to modest amounts of data and small numbers of replicas.

# Core Definition

Mnesia is a lightweight, soft real-time, distributed, replicated, transactional data store native to Erlang/OTP. It excels at storing discrete chunks of Erlang data, particularly in RAM, and stores Erlang data as-is — you never need to rewrite your data into a particular format to put it in the database. Mnesia was not designed to replace SQL-style databases or to manage hundreds of gigabytes of persistent data across dozens of computers; the book recommends against that. It is, however, excellent for smaller numbers of replicas and smaller units of data — good for reasonable amounts of persistent (disk-backed) data and great for runtime data shared between processes, especially when the data must be distributed across nodes for fault tolerance or efficiency (Ch. 9, Section 9.2). The name is the Greek word for *memory* — chosen after management vetoed the developer's original choice of "Amnesia."

# Prerequisites

- **OTP application** — Mnesia is an OTP application that must be started.

# Key Properties

1. Lightweight, soft real-time, distributed, replicated, transactional data store.
2. Native to Erlang; stores Erlang terms without reformatting.
3. Best for small numbers of replicas and modest data sizes.
4. Supports RAM-only, disk-backed, and disk-only storage.
5. Not intended to replace SQL databases or hold hundreds of gigabytes.
6. Provides ACID transactions and dynamic replication.

# Construction / Recognition

## To Use Mnesia:
1. Start a node configured with a Mnesia directory.
2. Create a schema (`mnesia:create_schema/1`).
3. Start Mnesia (`mnesia:start()`).
4. Create tables, populate them, and query them.

## To Recognize:
1. Calls to the `mnesia` module (`create_table`, `transaction`, `dirty_read`, etc.) indicate Mnesia use.

# Context & Application

- **Typical contexts**: Runtime data shared between processes; modest persistent data.
- **Common applications**: Distributing the cache's key-to-pid table; a project database.
- **Historical/stylistic notes**: The name "Mnesia" came from chopping the "A" off "Amnesia."

# Examples

**Example 1** (Section 9.2): The key-to-pid mappings the distributed cache needs are described as "a good example" of runtime data that benefits from Mnesia.

**Example 2** (Section 9.2.1): The book builds a project database with User, Project, and Contributor tables to demonstrate Mnesia.

# Relationships

## Builds Upon
- **OTP application** — Mnesia is a startable OTP application.

## Enables
- **mnesia-schema** — A Mnesia database begins with a schema.
- **mnesia-table** — Data is stored in Mnesia tables.
- **mnesia-transaction** — Mnesia provides ACID transactions.

## Related
- **ets** — Mnesia tables resemble ETS tables and Mnesia can replace ETS for storage.

## Contrasts With
- **ets** — ETS is a local in-memory table store; Mnesia adds distribution, replication, persistence, and transactions.

# Common Errors

- **Error**: Using Mnesia to manage hundreds of gigabytes across dozens of machines.
  **Correction**: Mnesia is for modest data and few replicas; choose a different store for large-scale persistence.

# Common Confusions

- **Confusion**: Thinking Mnesia is an SQL database.
  **Clarification**: Mnesia stores Erlang terms natively; it is not an SQL-style database and was not meant to replace one.

# Source Reference

Chapter 9: Adding distribution to the cache with Mnesia, Section 9.2 "Distributed data storage with Mnesia," and the "How Mnesia got its name" sidebar.

# Verification Notes

- Definition source: Directly adapted from Section 9.2's opening definition.
- Confidence rationale: HIGH — the book opens the section with an explicit definition.
- Uncertainties: None.
- Cross-reference status: Verified; `ets` is owned by Agent 2.
