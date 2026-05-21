---
# === CORE IDENTIFICATION ===
concept: Talking to a Java Node from Erlang
slug: talking-to-java-node-from-erlang

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
section: "13.1.5. Talking to the Java node from Erlang"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Erlang-to-Java messaging"
  - "sending messages to a Jinterface mailbox"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-mbox
  - epmd
  - message-passing
extends: []
related:
  - jinterface-message-handling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you send a message from Erlang to a Java node?"
  - "Why must an Erlang node be started before a Jinterface node?"
  - "How do you address a named mailbox on a remote node?"
---

# Quick Definition

From Erlang, a Jinterface Java node is just another node: you reach a named mailbox on it with `{Name, Node} ! Message` and receive its replies with ordinary `receive`.

# Core Definition

From the Erlang side, a Java node based on Jinterface behaves just like any other Erlang node, and you communicate with it using plain message-passing. Because Jinterface does not start EPMD itself, the simplest approach is to start a normal Erlang node first; whenever an Erlang node starts, it ensures EPMD is running on the host, and EPMD keeps running afterward. To send a message to a named mailbox without knowing its pid, you use the form `{Name, Node} ! Message`. After the first reply, the returned identifier can be used to send further messages directly (Chapter 13, Section 13.1.5).

# Prerequisites

- **OtpMbox** — The Java side's named mailbox is the message target.
- **EPMD** — Nodes find each other via EPMD, which must already be running.
- **Message passing** — Communication uses ordinary Erlang send and receive.

# Key Properties

1. The Java node is indistinguishable from an Erlang node from the Erlang side.
2. Jinterface does not start EPMD; start an Erlang node first so EPMD is launched.
3. A named mailbox is addressed with `{MailboxName, Node} ! Message`.
4. `net_adm:ping(JavaNode)` confirms connectivity, returning `pong`.
5. The Java side's reply carries an identifier that can be used directly for subsequent sends.
6. The Erlang and Java nodes must share the same magic cookie and the same name form (short or long).

# Construction / Recognition

## To Construct/Create:
1. Start an Erlang node: `erl -sname erlangNode -setcookie secret` (this also starts EPMD).
2. Start the Java node with the matching cookie.
3. From the Erlang shell, ping it: `net_adm:ping(javaNode@frodo).` → `pong`.
4. Send to its named mailbox: `{theMailbox, javaNode@frodo} ! {self(), "Eric"}.`.
5. Receive the reply: `receive {Mbox, Msg} -> Msg end.`.
6. Use the returned `Mbox` identifier for further sends: `Mbox ! {self(), "Martin"}.`.

# Context & Application

- **Typical contexts**: Driving or testing a Jinterface node from the Erlang shell or from Erlang code.
- **Common applications**: The `sc_hbase` module sends `{put|get|delete, ...}` request tuples to the `hbase_server` mailbox on the HBase Java node.
- **Historical/stylistic notes**: The chapter walks through an interactive shell session greeting "Eric" and "Martin".

# Examples

**Example 1** (Section 13.1.5): `{theMailbox, javaNode@frodo} ! {self(), "Eric"}.` then `receive {Mbox, Msg} -> Msg end.` yields `"Greetings from Java, Eric!"`.

**Example 2** (Section 13.1.5): After the first reply, `Mbox ! {self(), "Martin"}.` sends directly to the mailbox pid, returning `{<5569.1.0>,"Greetings from Java, Martin!"}`.

# Relationships

## Related
- **Jinterface message-handling loop** — The Java-side counterpart that receives these messages.
- **Registered process** — Addressing a named mailbox uses the same `{Name, Node}` form as a registered Erlang process.

# Common Errors

- **Error**: Starting the Java node before any Erlang node, so EPMD is not running.
  **Correction**: Start an Erlang node first; EPMD then stays up for the Java node to register with.

- **Error**: Using a different cookie or name form on the two sides.
  **Correction**: Use the same cookie and consistently short or long names.

# Common Confusions

- **Confusion**: Believing a special API is needed to talk to a Java node.
  **Clarification**: Ordinary `!` and `receive` work; the Java node looks like any Erlang node.

# Source Reference

Chapter 13: Communication between Erlang and Java via Jinterface, Section 13.1.5 "Talking to the Java node from Erlang."

# Verification Notes

- Definition source: Direct adaptation of Section 13.1.5, including the shell session.
- Confidence rationale: HIGH — the interaction is explicitly demonstrated.
- Uncertainties: None.
- Cross-reference status: References Agent 1- and Agent 3-owned slugs by name per instructions.
- Re-extraction notes: Fresh extraction; no prior card.
</content>
