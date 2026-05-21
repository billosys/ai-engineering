---
# === CORE IDENTIFICATION ===
concept: OtpNode (Java Node Class)
slug: otp-node-java

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
section: "13.1.1. The OtpNode class"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "OtpNode"
  - "OtpNode class"
  - "Java node"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - jinterface
  - erlang-node
  - magic-cookie
extends:
  - erlang-node
related:
  - otp-mbox
  - epmd
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the OtpNode class?"
  - "How do you start a Java node with Jinterface?"
  - "How do you give a Java node a cookie?"
---

# Quick Definition

`OtpNode` is the Jinterface Java class that represents an Erlang node. Creating an `OtpNode` instance starts a node that can connect to and communicate with other (real or Java) Erlang nodes.

# Core Definition

In the Jinterface library, the Erlang node concept is represented by the `OtpNode` class. An `OtpNode` object provides the means of connecting to and interacting with other nodes, which may or may not be real Erlang nodes. Like a normal Erlang node, a node implemented with `OtpNode` has a node name and optionally an authentication cookie. Starting a node in Java requires only creating an instance of the class. `OtpNode` hides all of the underlying communication, connection handling, and protocol negotiation, making it a relatively simple task to hook Java code into an Erlang cluster (Chapter 13, Section 13.1.1).

# Prerequisites

- **Jinterface** — `OtpNode` is a class provided by the Jinterface library.
- **Erlang node** — `OtpNode` is the Java realization of the Erlang node concept, including node naming rules.
- **Magic cookie** — A node may take a cookie argument for authorizing connections.

# Key Properties

1. Constructing an `OtpNode` instance starts a node; no separate start call is needed.
2. If the name string contains an `@` character it is used verbatim as the full node name (e.g. `myNode@frodo.erlware.org`); otherwise `@` plus the local hostname is appended, forming a short name (e.g. `myNode@frodo`).
3. Short-name vs. long-name rules match Erlang's `-sname` and `-name` flags; all connected nodes in a cluster must use the same form.
4. An optional second constructor argument sets the authentication cookie.
5. The class hides underlying connection handling and the distribution protocol.
6. An `OtpNode` is used to manufacture `OtpMbox` mailbox objects.

# Construction / Recognition

## To Construct/Create:
1. Create a node with just a name: `OtpNode node = new OtpNode("myJavaNode");`.
2. Or create a node with a name and a cookie: `OtpNode node = new OtpNode("myJavaNode", "secretcookie");`.
3. Use the node object to create mailboxes via `createMbox()`.

# Context & Application

- **Typical contexts**: The entry point of any Jinterface-based program that joins an Erlang cluster.
- **Common applications**: In the book, the `JInterfaceExample` and `HBaseNode` classes each hold a single `OtpNode` field, initialized in their constructors.
- **Historical/stylistic notes**: The class deliberately mirrors the behaviour of a real Erlang node so that, from the Erlang side, the Java node is indistinguishable from any other.

# Examples

**Example 1** (Section 13.1.1): `OtpNode node = new OtpNode("myJavaNode");` — start a node with a generated short name.

**Example 2** (Section 13.1.4): The `JInterfaceExample` constructor runs `node = new OtpNode(nodeName, cookie);` then `mbox = node.createMbox(mboxName);`.

# Relationships

## Builds Upon
- **Erlang node** — `OtpNode` is the Java incarnation of the node concept, sharing the naming and cookie rules.

## Enables
- **OtpMbox** — Mailboxes are created by asking an `OtpNode` to manufacture them.

## Related
- **EPMD** — The node must be able to reach EPMD on the host to be found by other nodes.

# Common Errors

- **Error**: Mixing short and long node names between the Java node and the Erlang nodes.
  **Correction**: Ensure every node in the cluster uses the same naming form; include or omit a dotted host part consistently.

- **Error**: Creating an `OtpNode` with a cookie that differs from the Erlang nodes' cookie.
  **Correction**: Pass the same cookie string used by `-setcookie` on the Erlang side.

# Common Confusions

- **Confusion**: Thinking a separate `start()` call is needed after constructing an `OtpNode`.
  **Clarification**: The node is live as soon as the constructor returns.

# Source Reference

Chapter 13: Communication between Erlang and Java via Jinterface, Section 13.1.1 "The OtpNode class."

# Verification Notes

- Definition source: Direct adaptation of Section 13.1.1.
- Confidence rationale: HIGH — the class is explicitly defined and demonstrated.
- Uncertainties: None.
- Cross-reference status: References Agent 3-owned slugs by name per instructions.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
