---
# === CORE IDENTIFICATION ===
concept: Erlang-HBase Bridge Architecture
slug: erlang-hbase-bridge

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
section: "13.3. Building the bridge between Simple Cache and HBase"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Erlang-HBase bridge"
  - "sc_hbase bridge"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - jinterface
  - hbase-integration
  - otp-node-java
extends: []
related:
  - sc-hbase-protocol
  - hbase-connector
  - hbase-java-message-handling
  - cache-hbase-integration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What components make up the Erlang-HBase bridge?"
  - "How is responsibility divided between the Erlang and Java sides of the bridge?"
  - "Where should Java source for an Erlang application be placed?"
---

# Quick Definition

The Erlang-HBase bridge is a four-component design — one Erlang module plus three Java classes — that lets the Simple Cache store and retrieve Erlang terms in an HBase table.

# Core Definition

The bridge between Erlang and HBase is purpose-built as a back end for the cache, not a general HBase binding, which keeps the work manageable. It has four major components: the Erlang module `sc_hbase` (the API functions `put`, `get`, `delete`, wrapping a message-based protocol); the Java class `HBaseConnector` (implements the operations against the HBase Java API); the main Java class `HBaseNode` (the Java node that receives and dispatches Erlang requests); and the Java class `HBaseTask` (handles each request in its own thread, using `HBaseConnector` and replying to the Erlang client). The design uses a Java thread pool so requests are handled asynchronously (Chapter 13, Section 13.3, Figure 13.4).

# Prerequisites

- **Jinterface** — The Java side joins the Erlang cluster as a node.
- **HBase as a backing store** — The bridge fronts an HBase table.
- **OtpNode (Java node class)** — `HBaseNode` is built on an `OtpNode`.

# Key Properties

1. Four components: `sc_hbase` (Erlang) plus `HBaseConnector`, `HBaseNode`, `HBaseTask` (Java).
2. The Erlang side is a single module; the Java side is split into three classes for separation of responsibilities.
3. Requests are dispatched to a Java thread pool so multiple requests run concurrently.
4. Specific to the cache use case — deliberately not a general-purpose HBase binding.
5. Java source conventionally lives in a `java_src` directory (and C in `c_src`); compiled artifacts go under `priv`.
6. The bridge defines a small message-based protocol shared by both sides.

# Construction / Recognition

## To Construct/Create:
1. Create `simple_cache/java_src/` for the Java sources.
2. Write the Erlang module `sc_hbase` with `put`, `get`, `delete`.
3. Write `HBaseConnector.java` wrapping the HBase Java API.
4. Write `HBaseNode.java` — the Jinterface node that receives requests.
5. Write `HBaseTask.java` — a `Runnable` that processes one request per thread.
6. Compile the Java classes; place artifacts under `priv` for shipping.

# Context & Application

- **Typical contexts**: Connecting an OTP application to a JVM-based database.
- **Common applications**: Backing the Simple Cache with durable HBase storage.
- **Historical/stylistic notes**: The book notes that the single `OtpMbox` is a bottleneck even with the thread pool; for demanding applications, Erlang-style mitigations apply.

# Examples

**Example 1** (Figure 13.4): The bridge is drawn as one Erlang module communicating over the distribution protocol with three Java classes.

**Example 2** (Section 13.3.2 sidebar): Java code is placed in `java_src`, C code in `c_src`, and compiled DLLs/`.class`/`.jar` files under `priv`.

# Relationships

## Related
- **sc_hbase protocol** — The message protocol the Erlang module defines.
- **HBaseConnector class** — The Java wrapper over the HBase API.
- **HBase Java message handling** — The `HBaseNode`/`HBaseTask` request flow.
- **Cache-HBase integration** — How the cache module wires into this bridge.

# Common Errors

- **Error**: Mixing Java sources into the Erlang `src` directory.
  **Correction**: Keep Java in `java_src`, C in `c_src`, and compiled artifacts under `priv`.

- **Error**: Treating the bridge as a reusable general HBase client.
  **Correction**: It is intentionally cache-specific; generalizing it requires more work.

# Common Confusions

- **Confusion**: Believing the thread pool eliminates all bottlenecks.
  **Clarification**: The single `OtpMbox` remains a serialization point for incoming requests.

# Source Reference

Chapter 13: Communication between Erlang and Java via Jinterface, Section 13.3 "Building the bridge between Simple Cache and HBase," Figure 13.4.

# Verification Notes

- Definition source: Direct adaptation of Section 13.3 and Figure 13.4.
- Confidence rationale: HIGH — the four-component architecture is explicitly enumerated.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
