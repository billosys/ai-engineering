---
# === CORE IDENTIFICATION ===
concept: OtpMbox (Jinterface Mailbox)
slug: otp-mbox

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
section: "13.1.2. The OtpMbox class"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "OtpMbox"
  - "Jinterface mailbox"
  - "named mailbox"
  - "anonymous mailbox"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - jinterface
  - otp-node-java
  - message-passing
extends: []
related:
  - jinterface-data-mapping
contrasts_with:
  - erlang-process

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OtpMbox?"
  - "How do you send and receive messages from a Java node?"
  - "What is the difference between a named and an anonymous mailbox?"
---

# Quick Definition

`OtpMbox` is the Jinterface mailbox class used to send and receive messages between a Java node and other Erlang nodes. It behaves like an Erlang process mailbox but is not owned by any process.

# Core Definition

`OtpMbox` objects are used to interact with other nodes in an Erlang cluster. They behave like Erlang process mailboxes, but they do not belong to any process. In the Jinterface model, a mailbox identifier serves the same purpose, from a communication standpoint only, as an Erlang process identifier: it is an address to which messages can be sent. Jinterface lets you manage Java threads as you like and gives direct access to the mailbox abstraction so threads can communicate via messages. Mailboxes are created by asking an `OtpNode` to manufacture one; they may be named (registered on the local node) or anonymous. The two fundamental methods are `send` and `receive` (Chapter 13, Section 13.1.2).

# Prerequisites

- **Jinterface** — `OtpMbox` is part of the Jinterface library.
- **OtpNode (Java node class)** — Mailboxes are created from an `OtpNode` object.
- **Message passing** — Mailboxes are the endpoints of Erlang-style message passing.

# Key Properties

1. Behaves like an Erlang process mailbox but belongs to no process.
2. Created by calling `node.createMbox(...)` on an `OtpNode`.
3. A *named* mailbox is registered on the local node; messages can be sent to it by name, like a registered Erlang process.
4. An *anonymous* mailbox has no name; you need its pid or a direct object reference to interact with it.
5. The core API methods are `send` and `receive`; several variations exist.
6. `receive()` returns the first message in the mailbox, or blocks until a message arrives, yielding an `OtpErlangObject`.

# Construction / Recognition

## To Construct/Create:
1. Obtain an `OtpNode` instance.
2. For a named mailbox: `OtpMbox named_mbox = node.createMbox("myNamedMbox");`.
3. For an anonymous mailbox: `OtpMbox anon_mbox = node.createMbox();`.

## To Identify/Recognize:
1. A named mailbox is reachable from Erlang via `{Name, Node} ! Message`.
2. An anonymous mailbox is reachable only via its pid or object reference.

# Context & Application

- **Typical contexts**: All message exchange in a Jinterface program flows through `OtpMbox` objects.
- **Common applications**: The `HBaseNode` example uses a single named mailbox (`hbase_server`) as the known entry point for cache requests; reply mailboxes send results back with `mbox.send(from, reply)`.
- **Historical/stylistic notes**: The book notes that a single `OtpMbox` is a communication bottleneck under heavy load even when a thread pool is used.

# Examples

**Example 1** (Section 13.1.3): `anon_mbox.send("myNamedMbox", aTuple);` sends a tuple from the anonymous mailbox to the named one.

**Example 2** (Section 13.1.3): `OtpErlangObject msg = named_mbox.receive();` blocks until a message arrives and returns it as an `OtpErlangObject`.

**Example 3** (Listing 13.4): In `HBaseTask`, the reply tuple is sent back to the Erlang caller with `mbox.send(from, reply)`.

# Relationships

## Related
- **Jinterface data mapping** — Messages sent and received are `OtpErlangObject` instances.
- **Registered process** — A named mailbox plays the role of a registered process from the cluster's view.

## Contrasts With
- **Process** — An Erlang process has its own mailbox; an `OtpMbox` is a free-standing mailbox not tied to any process or thread.

# Common Errors

- **Error**: Expecting an anonymous mailbox to be reachable by name from Erlang.
  **Correction**: Give the mailbox a name with `createMbox("name")`, or share its pid.

- **Error**: Calling `receive()` on a thread that must stay responsive.
  **Correction**: `receive()` blocks until a message arrives; use a dedicated thread or a timed variant.

# Common Confusions

- **Confusion**: Believing each `OtpMbox` is bound to a Java thread, like an Erlang process owns its mailbox.
  **Clarification**: Mailboxes are independent of threads; any thread can use any mailbox.

# Source Reference

Chapter 13: Communication between Erlang and Java via Jinterface, Section 13.1.2 "The OtpMbox class," with usage in Sections 13.1.3-13.1.5 and Listings 13.2-13.4.

# Verification Notes

- Definition source: Direct adaptation of Section 13.1.2.
- Confidence rationale: HIGH — the class is explicitly defined and demonstrated.
- Uncertainties: None.
- Cross-reference status: References Agent 1- and Agent 3-owned slugs by name per instructions.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
