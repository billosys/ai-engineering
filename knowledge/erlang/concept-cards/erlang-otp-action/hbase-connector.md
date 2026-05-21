---
# === CORE IDENTIFICATION ===
concept: HBaseConnector Wrapper Class
slug: hbase-connector

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
section: "13.3.2. The HBaseConnector class"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "HBaseConnector"
  - "HBase API wrapper"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-hbase-bridge
  - hbase-integration
extends: []
related:
  - hbase-java-message-handling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the HBaseConnector class for?"
  - "How does HBaseConnector hide the HBase Java API?"
  - "How are get, put, and delete implemented against HBase?"
---

# Quick Definition

`HBaseConnector` is a thin Java wrapper class that exposes just `get`, `put`, and `delete` over the HBase Java API, so the rest of the bridge code never touches HBase directly.

# Core Definition

`HBaseConnector` is a small wrapper layer around the core interaction with the HBase system. The HBase Java API is general and somewhat baroque; the connector reduces it to the three operations the bridge needs — `put`, `get`, and `delete` — so the rest of the code does not have to know anything about HBase. It holds a single `HTable` member, constructed with a default `HBaseConfiguration` and the name of the `cache` table. All parameters passed to HBase are byte arrays, since HBase treats everything as sequences of bytes; isolating that awkwardness is a key reason for the wrapper (Chapter 13, Section 13.3.2).

# Prerequisites

- **Erlang-HBase bridge** — `HBaseConnector` is the bridge component that touches HBase.
- **HBase as a backing store** — The connector operates on the configured `cache` table.

# Key Properties

1. Wraps the HBase Java API down to three methods: `get`, `put`, `delete`.
2. Holds one `HTable` object, built from a default `HBaseConfiguration` and the table name `cache`.
3. All keys and values cross the HBase boundary as `byte[]`.
4. `get(byte[] key)` retrieves a `Result`, navigates a `NavigableMap` with the field name `"value"` and an empty domain, and returns the value bytes.
5. `put(byte[] key, byte[] value)` builds a `Put`, adds the value under field `"value"` and empty domain, and writes it.
6. `delete(byte[] key)` builds a `Delete` and passes it to `table.delete`.
7. A missing key causes `get` to throw a `NullPointerException`.

# Construction / Recognition

## To Construct/Create:
1. Import `org.apache.hadoop.hbase.HBaseConfiguration`, `org.apache.hadoop.hbase.client.*`, and `java.util.NavigableMap`.
2. In the constructor, create an `HTable` with `new HBaseConfiguration()` and the table name `cache`.
3. Implement `get`, `put`, `delete` using `Get`, `Put`, and `Delete` objects.
4. Compile with `hbase-<version>.jar` and `hadoop-<version>-core.jar` on the class path.

# Context & Application

- **Typical contexts**: An adapter layer isolating a verbose third-party API.
- **Common applications**: `HBaseTask` calls `HBaseConnector.get/put/delete`, staying independent of HBase details.
- **Historical/stylistic notes**: The book keeps the connector classes in the empty Java package for simplicity.

# Examples

**Example 1** (Section 13.3.2): `put` does `Put put = new Put(key); put.add("value".getBytes(), "".getBytes(), value); table.put(put);`.

**Example 2** (Section 13.3.2): `delete` does `Delete del = new Delete(key); table.delete(del);`.

# Relationships

## Related
- **HBase Java message handling** — `HBaseTask` uses an `HBaseConnector` to perform requested operations.

# Common Errors

- **Error**: Passing String keys/values directly to HBase.
  **Correction**: HBase wants `byte[]`; convert with `.getBytes()` and let the connector hide it.

- **Error**: Not handling the `NullPointerException` thrown by `get` on a missing key.
  **Correction**: Catch it in the caller and translate it to a `not_found` reply.

# Common Confusions

- **Confusion**: Expecting `get` to return `null` for a missing key.
  **Clarification**: It throws a `NullPointerException`; the caller converts that to `not_found`.

# Source Reference

Chapter 13: Communication between Erlang and Java via Jinterface, Section 13.3.2 "The HBaseConnector class."

# Verification Notes

- Definition source: Direct adaptation of Section 13.3.2 and the `get`/`put`/`delete` listings.
- Confidence rationale: HIGH — the class is explicitly defined and shown.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
