---
# === CORE IDENTIFICATION ===
concept: HBase Java Node with a Thread Pool
slug: hbase-java-message-handling

# === CLASSIFICATION ===
category: distribution
subcategory: foreign-integration
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Communication between Erlang and Java via Jinterface"
chapter_number: 13
pdf_page: null
section: "13.3.3-13.3.4. Java message handling / The HBaseTask class"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "HBaseNode"
  - "HBaseTask"
  - "thread-pool message handling"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - jinterface-message-handling
  - hbase-connector
  - sc-hbase-protocol
extends:
  - jinterface-message-handling
related:
  - erlang-hbase-bridge
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the HBase Java node process requests concurrently?"
  - "What is the role of HBaseTask?"
  - "How does the Java node decide between a four- and five-element request tuple?"
---

# Quick Definition

The HBase Java node (`HBaseNode`) runs a receive loop that, for each request, enqueues an `HBaseTask` onto a thread pool; each task uses `HBaseConnector` to do the work and replies to the Erlang caller.

# Core Definition

The main framework of the HBase Java node resembles the basic Jinterface example but processes each message in a separate thread rather than one at a time. Because starting a thread per request would be too inefficient in Java, the code uses a thread-pool class (`ExecutorService` from `java.util.concurrent`). `HBaseNode` initializes the node, mailbox, an `HBaseConnector`, and the thread pool; its `process()` loop receives each message, deconstructs it, builds an `HBaseTask`, and submits the task to the pool. `HBaseTask` implements `Runnable`; its `run` method dispatches by action to `doGet`, `doPut`, or `doDelete`, each of which uses the connector and sends a reply tuple back to the originating pid (Chapter 13, Sections 13.3.3-13.3.4, Listings 13.2-13.4).

# Prerequisites

- **Jinterface message-handling loop** — `HBaseNode.process()` is a specialization of this loop.
- **HBaseConnector class** — `HBaseTask` calls the connector to perform operations.
- **sc_hbase protocol** — The node decodes the request tuples this protocol defines.

# Key Properties

1. `HBaseNode` holds the `OtpNode`, `OtpMbox`, `HBaseConnector`, and an `ExecutorService` thread pool.
2. The `process()` loop receives each message, decomposes it, and submits an `HBaseTask` to the pool — it does not send replies itself.
3. A request tuple of arity four is a `get` or `delete`; arity five is a `put` (with a value); any other arity is an error.
4. `HBaseTask` implements `Runnable`; `run` dispatches to `doGet`/`doPut`/`doDelete` by action string.
5. Each task sends a reply tuple `{reply, Ref, Result}` back to the caller via the mailbox.
6. Malformed messages are printed and skipped; no reply can be sent because the sender is unknown.
7. The single `OtpMbox` remains a bottleneck even though tasks run concurrently.

# Construction / Recognition

## To Construct/Create:
1. In `HBaseNode`'s constructor, create the node, mailbox, an `HBaseConnector`, and an `ExecutorService` thread pool.
2. In `process()`, loop: receive a message, cast and deconstruct it.
3. Branch on tuple arity — four → `get`/`delete`, five → `put` — building an `HBaseTask`.
4. Submit the task to the thread pool.
5. In `HBaseTask.run`, dispatch by action to `doGet`/`doPut`/`doDelete`, each replying with `mbox.send(from, reply)`.

# Context & Application

- **Typical contexts**: A Jinterface node that must handle many requests with bounded concurrency.
- **Common applications**: The Java side of the Erlang-HBase bridge.
- **Historical/stylistic notes**: The book contrasts Java's expensive threads with Erlang's cheap processes, motivating the thread pool.

# Examples

**Example 1** (Listing 13.3): `HBaseNode.process()` extracts each message, checks its arity, builds an `HBaseTask` (with `null` data for four-element tuples), and submits it to the pool.

**Example 2** (Listing 13.4): `HBaseTask.doGet` wraps `conn.get(key)` in an `OtpErlangBinary`, catches `NullPointerException` to produce a `not_found` atom, and sends `{reply, ref, result}` back.

# Relationships

## Builds Upon
- **Jinterface message-handling loop** — Adds a thread pool and request dispatch to the basic loop.

## Related
- **Erlang-HBase bridge** — `HBaseNode` and `HBaseTask` are two of its four components.

# Common Errors

- **Error**: Spawning a fresh Java thread per request.
  **Correction**: Use a thread pool (`ExecutorService`); unbounded thread creation is too costly in Java.

- **Error**: Trying to reply to a malformed request.
  **Correction**: Without a valid request tuple the sender's pid is unknown; just log and skip.

# Common Confusions

- **Confusion**: Thinking the thread pool removes the mailbox bottleneck.
  **Clarification**: All requests still funnel through one `OtpMbox`; the pool only parallelizes processing after receipt.

# Source Reference

Chapter 13: Communication between Erlang and Java via Jinterface, Sections 13.3.3 "Java message handling" and 13.3.4 "The HBaseTask class," Listings 13.2-13.4.

# Verification Notes

- Definition source: Direct adaptation of Sections 13.3.3-13.3.4 and Listings 13.2-13.4.
- Confidence rationale: HIGH — the node, task, and thread-pool design are explicitly shown.
- Uncertainties: None.
- Cross-reference status: All cross-references are Agent 5-owned slugs.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
