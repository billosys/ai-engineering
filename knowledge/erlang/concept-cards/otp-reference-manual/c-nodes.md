---
# === CORE IDENTIFICATION ===
concept: C Nodes
slug: c-nodes

# === CLASSIFICATION ===
category: distribution
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Distributed Erlang"
chapter_number: null
pdf_page: null
section: "C Nodes"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - C node
  - Erl_Interface node

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-node
  - hidden-nodes
  - distributed-erlang-system
extends:
  - hidden-nodes
related:
  - port-drivers
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a C node in Erlang?"
  - "How does a C node participate in a distributed Erlang system?"
  - "What library is used to implement C nodes?"
---

# Quick Definition
A C node is a C program written to act as a hidden node in a distributed Erlang system. It uses the Erl_Interface library to communicate with Erlang nodes using the Erlang distribution protocol.

# Core Definition
The Erlang Reference Manual states: "A _C node_ is a C program written to act as a hidden node in a distributed Erlang system. The library _Erl_Interface_ contains functions for this purpose." (Distributed Erlang chapter, "C Nodes" section).

# Prerequisites
- **erlang-node** -- C nodes participate as nodes in the distributed system
- **hidden-nodes** -- C nodes act as hidden nodes
- **distributed-erlang-system** -- C nodes are part of the distributed system

# Key Properties
1. Written in C
2. Acts as a hidden node in the distributed system
3. Uses the Erl_Interface (ei) library
4. Communicates using the Erlang distribution protocol
5. Can send and receive Erlang terms
6. Does not appear in `nodes/0` (because it is hidden)
7. Connections must be set up explicitly (hidden node behavior)

# Construction / Recognition
## To Construct/Create:
1. Write a C program using the Erl_Interface (ei) library
2. The program connects to the Erlang cluster using the distribution protocol
3. It registers as a hidden node

## To Identify/Recognize:
1. C nodes appear in `nodes(hidden)` or `nodes(connected)`, not in `nodes/0`
2. A C node communicates using Erlang term format but runs native C code

# Context & Application
C nodes provide an alternative to ports and NIFs for integrating C code with Erlang. Unlike ports (which communicate via stdin/stdout) or NIFs (which run inside the VM), C nodes run as separate OS processes that participate in the distribution protocol. This provides both isolation (crashes do not affect the Erlang VM) and the ability to use all distribution features (message passing, links, monitors).

**Typical contexts:**
- Integrating C/C++ services into an Erlang system
- Running computationally intensive C code as a separate node
- Legacy system integration where the C program needs to be a peer rather than a subprocess

# Examples
**Example 1** (Distributed Erlang, "C Nodes" section): "A _C node_ is a C program written to act as a hidden node in a distributed Erlang system. The library _Erl_Interface_ contains functions for this purpose."

**Example 2** (Distributed Erlang, "C Nodes" section): Resources for implementing C nodes: the Erl_Interface application documentation and the Interoperability Tutorial.

# Relationships
## Builds Upon
- **erlang-node** -- C nodes are nodes in the distributed system
- **hidden-nodes** -- C nodes act as hidden nodes
- **distributed-erlang-system** -- C nodes participate in distribution

## Enables
Nothing directly.

## Related
- **port-drivers** -- Port drivers are an alternative C integration mechanism (in-VM vs. separate process)

## Contrasts With
No direct contrasts within this chapter, though conceptually C nodes contrast with port drivers (separate process vs. in-VM).

# Common Errors
- **Error**: Expecting a C node to appear in `nodes/0`
  **Correction**: C nodes are hidden nodes. Use `nodes(hidden)` or `nodes(connected)` to see them.

# Common Confusions
- **Confusion**: Confusing C nodes with NIFs or port drivers
  **Clarification**: C nodes run as separate OS processes communicating over the distribution protocol. NIFs and port drivers run inside the Erlang VM. C nodes provide process isolation at the cost of communication overhead.

# Source Reference
Distributed Erlang chapter, "C Nodes" section.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- concise, explicit definition
- Uncertainties: None -- the section is brief but the definition is clear
- Cross-reference status: All referenced slugs correspond to planned cards
