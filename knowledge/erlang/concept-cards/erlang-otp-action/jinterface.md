---
# === CORE IDENTIFICATION ===
concept: Jinterface
slug: jinterface

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
section: "13.1. Integrating Erlang with Java using Jinterface"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Jinterface library"
  - "OtpErlang.jar"
  - "com.ericsson.otp.erlang"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distributed-erlang
  - erlang-node
  - message-passing
extends:
  - distributed-erlang
related:
  - otp-node-java
  - otp-mbox
  - jinterface-data-mapping
  - epmd
contrasts_with:
  - port

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Jinterface?"
  - "How do you make a Java program act as an Erlang node?"
  - "How does Jinterface differ from using ports for foreign code?"
---

# Quick Definition

Jinterface is a Java library that makes the Erlang distribution layer available to Java programs, letting a Java application masquerade as a node in an Erlang cluster.

# Core Definition

Jinterface is a library written in Java that makes the Erlang distribution layer available to Java programs. It does not expose this in an idiomatic Java way; instead it mirrors the Erlang distribution model with as little modification as possible. Nearly every Erlang construct has a matching Java class, from nodes and mailboxes down to granular objects like tuples and atoms. With Jinterface, foreign Java code communicates over the Erlang distribution protocol rather than through ports, so from the Erlang side the Java program behaves just like any other Erlang node. The library code belongs to the Java package `com.ericsson.otp.erlang` and ships with Erlang/OTP as `OtpErlang.jar` (Chapter 13, Section 13.1).

# Prerequisites

- **Distributed Erlang** — Jinterface participates in the Erlang distribution protocol; understanding nodes and clusters is required.
- **Erlang node** — A Jinterface program presents itself to the cluster as a node.
- **Message passing** — Communication with the Java node uses ordinary Erlang message-passing.

# Key Properties

1. Written in Java; ships with Erlang/OTP as the `jinterface` application (`OtpErlang.jar` under `priv`).
2. Exposes the Erlang distribution model directly rather than wrapping it in idiomatic Java APIs.
3. The Java node communicates over the Erlang distribution protocol — no ports, no custom marshalling protocol.
4. Provides Java classes mirroring Erlang concepts: `OtpNode`, `OtpMbox`, and the `OtpErlang*` data-type classes.
5. Code belongs to the package `com.ericsson.otp.erlang`, imported with `import com.ericsson.otp.erlang.*;`.
6. Suitable for bridging to Java libraries (the book uses it to reach the HBase Java API).

# Construction / Recognition

## To Construct/Create:
1. Locate the `OtpErlang.jar` shipped with Erlang/OTP (e.g. `.../lib/erlang/lib/jinterface-1.5.1/priv/OtpErlang.jar`).
2. In the Java source, `import com.ericsson.otp.erlang.*;`.
3. Compile with `javac -cp /path/to/OtpErlang.jar YourProgram.java`.
4. Run with `java -cp .:/path/to/OtpErlang.jar YourProgram ...`, supplying the JAR on the class path.
5. In the program, create an `OtpNode` and one or more `OtpMbox` mailboxes.

# Context & Application

- **Typical contexts**: Integrating Erlang systems with code or libraries that live in the JVM.
- **Common applications**: The chapter uses Jinterface to build a bridge between the Simple Cache application and the HBase database's Java API.
- **Historical/stylistic notes**: An alternative to ports (Chapter 12); the same techniques generalize to a bridge for any Java library.

# Examples

**Example 1** (Section 13.1): Jinterface is presented as a contrast to ports — the foreign code masquerades as an Erlang node and speaks the distribution protocol directly.

**Example 2** (Section 13.1.4): The `JInterfaceExample.java` program imports `com.ericsson.otp.erlang.*` and is compiled with `javac -cp /path/to/OtpErlang.jar JInterfaceExample.java`.

# Relationships

## Builds Upon
- **Distributed Erlang** — Jinterface joins the distribution layer as a peer node.

## Enables
- **OtpNode (Java node class)** — The node abstraction Jinterface provides.
- **OtpMbox** — The mailbox abstraction Jinterface provides.

## Related
- **Jinterface data mapping** — The `OtpErlang*` classes that marshal data.
- **EPMD** — Java nodes rely on EPMD for node discovery but do not start it themselves.

## Contrasts With
- **Erlang port** — Ports are a general way to talk to foreign code via stdin/stdout; Jinterface instead makes the foreign code a full distribution peer.

# Common Errors

- **Error**: Forgetting the `OtpErlang.jar` on the class path at compile or run time.
  **Correction**: Pass `-cp /path/to/OtpErlang.jar` to both `javac` and `java`.

- **Error**: Starting a Jinterface program without any Erlang node running, expecting EPMD to be available.
  **Correction**: Start an Erlang node first so EPMD is launched on the host.

# Common Confusions

- **Confusion**: Believing Jinterface gives an idiomatic Java API for Erlang.
  **Clarification**: It deliberately exposes the Erlang model with little modification; the API is Erlang-shaped, not Java-shaped.

# Source Reference

Chapter 13: Communication between Erlang and Java via Jinterface, Section 13.1 "Integrating Erlang with Java using Jinterface."

# Verification Notes

- Definition source: Direct adaptation of the introduction to Section 13.1.
- Confidence rationale: HIGH — Jinterface is explicitly defined and described.
- Uncertainties: None.
- Cross-reference status: References Agent 3- and Agent 4-owned slugs by name per instructions.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
