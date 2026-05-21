---
# === CORE IDENTIFICATION ===
concept: HBase as a Backing Store for a Cache
slug: hbase-integration

# === CLASSIFICATION ===
category: distribution
subcategory: foreign-integration
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Communication between Erlang and Java via Jinterface"
chapter_number: 13
pdf_page: null
section: "13.0 / 13.2. Installing and configuring HBase"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "HBase"
  - "HBase backing store"
  - "persistent backing store"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - jinterface
extends: []
related:
  - erlang-hbase-bridge
  - cache-hbase-integration
contrasts_with:
  - mnesia

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is HBase?"
  - "Why use HBase as a backing store for an Erlang cache?"
  - "How is an HBase table for the cache created and configured?"
---

# Quick Definition

HBase is a Hadoop-project database, based on Google's Bigtable design, used in the book as a reliable persistent backing store behind the in-memory Simple Cache.

# Core Definition

HBase is a database from the Hadoop project, based on Google's Bigtable database design, offering a fast and reliable store for big data sets. Integrating with HBase lets cache users rely on its robust, well-understood storage and distribution model and store as much data as they want. In the book's design, the cache acts as a fast memory-resident front end to a reliable backing store: a lookup checks Mnesia first and falls back to HBase, while writes always go to both HBase and Mnesia. HBase is accessed from Erlang via its Java API made reachable through Jinterface (Chapter 13 introduction; Section 13.2).

# Prerequisites

- **Jinterface** — HBase is reached from Erlang through a Java node built with Jinterface.

# Key Properties

1. A Hadoop-project database based on Google's Bigtable design.
2. Stores everything as binary data — keys and values are sequences of bytes, with no declared field types.
3. Requires an SSH server (`sshd`) running on the host, and needs the Hadoop Common distribution to compile against.
4. Started from its install directory with `./bin/start-hbase.sh`.
5. Tables are created from the HBase shell, e.g. a `cache` table with a single `value` field.
6. Serves as a persistent backing store while the cache stays in memory-resident Mnesia.

# Construction / Recognition

## To Construct/Create:
1. Download and unpack HBase and the Hadoop Common distribution.
2. Ensure `sshd` is running on the host.
3. Start HBase: `cd hbase-<version>` then `./bin/start-hbase.sh`.
4. Open the shell: `./bin/hbase shell`.
5. Create the table: `create 'cache', {NAME => 'value'}`.

# Context & Application

- **Typical contexts**: A durable store behind a fast in-memory cache.
- **Common applications**: The Simple Cache stores cached objects in an external HBase cluster so data is preserved essentially forever.
- **Historical/stylistic notes**: The book deliberately keeps HBase coverage minimal — enough to run a working backing store, not a full HBase tutorial.

# Examples

**Example 1** (Section 13.2.2): `create 'cache', {NAME => 'value'}` creates a table named `cache` with one field `value`.

**Example 2** (Chapter 13 introduction): On a lookup miss the cache pulls data from HBase, inserts it into Mnesia, and returns it; on a write it stores to both HBase and Mnesia.

# Relationships

## Related
- **Erlang-HBase bridge** — The Jinterface bridge that makes HBase reachable from Erlang.
- **Cache-HBase integration** — How the cache's lookup/insert/delete use HBase.

## Contrasts With
- **Mnesia** — Mnesia is the in-memory front-end store; HBase is the durable, virtually unbounded backing store behind it.

# Common Errors

- **Error**: Starting HBase without an SSH server installed.
  **Correction**: Install and run `sshd`; HBase connects back to localhost over SSH during startup.

- **Error**: HBase failing with "Java could not be found".
  **Correction**: Add an `export JAVA_HOME` line pointing to the JDK in `conf/hbase-env.sh`.

# Common Confusions

- **Confusion**: Thinking HBase needs typed columns like a relational database.
  **Clarification**: HBase stores everything as raw bytes; no field types are declared.

# Source Reference

Chapter 13: Communication between Erlang and Java via Jinterface, chapter introduction and Section 13.2 "Installing and configuring HBase."

# Verification Notes

- Definition source: Direct adaptation of the chapter intro sidebar and Section 13.2.
- Confidence rationale: HIGH — HBase's role and configuration are explicitly described.
- Uncertainties: HBase install details are version-specific (book uses 0.20.3).
- Cross-reference status: References Agent 3-owned slug `mnesia` by name per instructions.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
