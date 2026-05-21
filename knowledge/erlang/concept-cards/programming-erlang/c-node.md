---
# === CORE IDENTIFICATION ===
concept: C-Node
slug: c-node

# === CLASSIFICATION ===
category: tooling
subcategory: interfacing
tier: advanced

# === PROVENANCE ===
source: Programming Erlang, Second Edition
source_slug: programming-erlang
authors: Joe Armstrong
chapter: "Interfacing Techniques"
chapter_number: 15
pdf_page: null
section: "Advanced Interfacing Techniques"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "C nodes"
  - "C-nodes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - node
  - distributed-erlang
extends:
  - node
related:
  - linked-in-driver
  - nif
contrasts_with:
  - port-program

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a C-node?"
  - "How can a C program appear as an Erlang node?"
  - "How does a C-node differ from a port program?"
---

# Quick Definition

A C-node is a node implemented in C that obeys the Erlang distribution protocol, so that a real distributed Erlang node can talk to it and treat it as if it were an Erlang node.

# Core Definition

C-nodes are nodes implemented in C that obey the Erlang distribution protocol (Chapter 15, "Advanced Interfacing Techniques"). A "real" distributed Erlang node can talk to a C-node and will think the C-node is an Erlang node — provided it doesn't try to do anything fancy on the C-node, such as sending it Erlang code to execute. C-nodes are one of the advanced interfacing techniques the chapter mentions but does not develop in detail; they are described in the Interoperability tutorial in the official Erlang documentation.

# Prerequisites

- **Node** — A C-node presents itself as a node; understand Erlang nodes first.
- **Distributed Erlang** — A C-node participates in a distributed Erlang system by speaking the distribution protocol.

# Key Properties

1. A C-node is a node implemented in C.
2. It obeys the Erlang distribution protocol.
3. A real distributed Erlang node can communicate with it as if it were an Erlang node.
4. It cannot do everything a real node can — e.g. it cannot execute Erlang code sent to it.
5. It is one of the advanced interfacing techniques, documented in the Interoperability tutorial.

# Construction / Recognition

## To Use a C-Node (per the source's overview):
1. Implement the C program so it obeys the Erlang distribution protocol.
2. Connect it to a distributed Erlang node, which will treat it as a node.
3. Consult the Interoperability tutorial for the detailed procedure.

## To Recognize It:
1. Look for a non-Erlang program appearing in `nodes()` as a participant.
2. Distinguish it from a port program, which is reached through a port rather than the distribution protocol.

# Context & Application

- **Typical contexts**: Integrating C programs into a distributed Erlang system as peers.
- **Common applications**: The book defers concrete examples to the Interoperability tutorial.
- **Historical/stylistic notes**: The chapter mentions C-nodes only briefly, pointing to the official documentation for detail.

# Examples

**Example 1** (Chapter 15, "Advanced Interfacing Techniques"): The book states a real distributed Erlang node "can talk to a C-node and will think that the C-node is an Erlang node (provided it doesn't try to do anything fancy on the C-node like sending it Erlang code to execute)."

**Example 2** (Chapter 15): The source provides no inline code example; it points to the Interoperability tutorial at the Erlang documentation site.

# Relationships

## Builds Upon
- **Node** — a C-node is a node implementation, just written in C.

## Enables
- Participation of C programs in distributed Erlang as peer nodes.

## Related
- **Linked-in driver** and **NIF** — the other advanced interfacing techniques mentioned in the chapter.

## Contrasts With
- **Port program** — a port program is an external process reached through a port; a C-node is reached as a peer node via the distribution protocol.

# Common Errors

- **Error**: Sending Erlang code to a C-node to execute.
  **Correction**: A C-node cannot execute Erlang code; restrict interactions to what the distribution protocol supports.
- **Error**: Confusing a C-node with a port program.
  **Correction**: A C-node speaks the distribution protocol as a node; a port program speaks the port byte-stream protocol.

# Common Confusions

- **Confusion**: A C-node is a fully capable Erlang node.
  **Clarification**: It only speaks the distribution protocol; it cannot do everything a real Erlang node can.
- **Confusion**: A C-node and a port program are the same interfacing technique.
  **Clarification**: They differ in mechanism — distribution protocol vs. port byte stream.

# Source Reference

Chapter 15: Interfacing Techniques, section "Advanced Interfacing Techniques" (the "C-Nodes" description); further detail in the Erlang Interoperability tutorial.

# Verification Notes

- Definition source: Direct adaptation of the brief "C-Nodes" description.
- Confidence rationale: MEDIUM — C-nodes are named and characterized, but the chapter gives only a short overview and defers detail to the Interoperability tutorial.
- Uncertainties: No inline code example or API in the source; the card stays at the overview level.
- Cross-reference status: Slugs match canonical `node`/`distributed-erlang` and planned chapter cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
