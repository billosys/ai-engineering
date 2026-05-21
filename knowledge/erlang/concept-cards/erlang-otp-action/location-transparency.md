---
# === CORE IDENTIFICATION ===
concept: Location Transparency
slug: location-transparency

# === CLASSIFICATION ===
category: distribution
subcategory: distribution-fundamentals
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Introducing distributed Erlang/OTP"
chapter_number: 8
pdf_page: null
section: "8.1.2 Location transparency"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "location transparent"
  - "transparent process addressing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - message-passing
extends: []
related:
  - distributed-erlang
  - process-communication-by-copying
  - erlang-node
  - remote-shell
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is location transparency?"
  - "Why is the ! operator location transparent?"
  - "How does location transparency change how you design systems?"
---

# Quick Definition

Location transparency means the send operation `!` works identically whether the recipient process is on the local machine or a remote one; all routing information is encoded in the process identifier.

# Core Definition

Location transparency is the property that the method of communication between processes — and even its syntax — is the same regardless of whether the recipient is on the local machine or a remote machine. The `!` (send) operation is location transparent: the recipient can be on any machine, and all the information needed to guide the message to the right location is encoded in the process identifier. Erlang guarantees that process identifiers are unique across the network, even across machines. This means programs need no changes when moving from one machine to many, and a program built for a dozen machines can be tested on a single laptop. The book stresses that location transparency liberates programming style — once cross-machine communication is the normal state of things rather than a threshold to cross, you can design systems previously too complicated to contemplate (Ch. 8, Section 8.1.2).

# Prerequisites

- **message-passing** — Location transparency is a property of the message-passing send operation.

# Key Properties

1. The `!` send operation behaves identically for local and remote recipients.
2. Routing information is encoded entirely in the process identifier.
3. Process identifiers are unique across the whole network.
4. Programs need no change to scale from one machine to many.
5. One of the two features that make Erlang distribution possible.
6. Also enables features like remote shells.

# Construction / Recognition

## How It Works:
1. A pid (or `{Name, Node}` tuple) carries the destination, including which node.
2. `Pid ! Msg` routes the message to that node automatically.
3. The same code runs unchanged whether the target is local or remote.

## To Recognize:
1. Code that sends to a pid without checking where the process lives relies on location transparency.

# Context & Application

- **Typical contexts**: All distributed Erlang programming.
- **Common applications**: Remote shells; resource discovery; talking to a registered process on a named node.
- **Historical/stylistic notes**: The book jokes that the syntax for sending to a remote process is "exactly the same" as for a local one.

# Examples

**Example 1** (Section 8.1.2): `Pid ! "my message"` is shown as the syntax for sending both to a local process and to a process on a different machine — they are identical.

**Example 2** (Section 8.2.6): Remote shells work because the shell process communicates by message passing and does not care whether its console is on the same node — a direct demonstration of location transparency.

# Relationships

## Builds Upon
- **message-passing** — Location transparency is a property of the send operation.

## Enables
- **distributed-erlang** — Location transparency is one of the two pillars of distribution.
- **remote-shell** — Remote shells are a consequence of location transparency.

## Related
- **process-communication-by-copying** — The complementary pillar.
- **erlang-node** — The destination node is encoded in the pid.

## Contrasts With
- None.

# Common Errors

- **Error**: Assuming `Name ! Msg` reaches a process on a remote node.
  **Correction**: A bare registered name refers to the local node; use `{Name, Node}` to target a remote node.

# Common Confusions

- **Confusion**: Thinking location transparency hides all differences between local and remote.
  **Clarification**: Syntax and semantics of sending are identical, but network delays and failures still introduce nondeterminism.

# Source Reference

Chapter 8: Introducing distributed Erlang/OTP, Section 8.1.2 "Location transparency."

# Verification Notes

- Definition source: Directly adapted from Section 8.1.2.
- Confidence rationale: HIGH — the book explicitly defines and emphasizes the concept.
- Uncertainties: None.
- Cross-reference status: Verified.
