---
# === CORE IDENTIFICATION ===
concept: Demilitarized Zone
slug: demilitarized-zone

# === CLASSIFICATION ===
category: distribution
subcategory: networking
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Distributed Architectures"
chapter_number: 12
pdf_page: 378
section: "Networking"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - DMZ
  - perimeter network

# === TYPED RELATIONSHIPS ===
prerequisites:
  - front-end-node
extends: []
related:
  - sockets-and-ssl-transport
  - distributed-erlang
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a demilitarized zone in a distributed architecture?"
  - "How do I choose network protocols for my nodes?"
---

# Quick Definition

A demilitarized zone (DMZ), or perimeter network, is a physical or logical part of the network that exposes front-end nodes to an untrusted network while shielding the back-end logic and service nodes.

# Core Definition

A DMZ "is a physical or logical part of the network that exposes your nodes to an untrusted network (i.e., the Internet) used by the clients to access your services. DMZs were traditionally implemented in the hardware through the arrangement of managed network elements, and in the software using firewalls and other security measures. In cloud computing environments you do not get the hardware component, and have to instead mimic it through network connections and firewall rules" (Cesarini & Vinoski, p. 383). By creating an additional layer of security around back-end nodes, it reduces the risk of intrusion into logic and service nodes by not exposing their interfaces.

# Prerequisites

- **Front-end node** — A DMZ houses front-end nodes; understand them first.

# Key Properties

1. A physical or logical network region exposing nodes to an untrusted network.
2. Houses front-end nodes; back-end logic and service nodes stay outside it.
3. Traditionally implemented with managed network elements and firewalls.
4. In the cloud, mimicked through network connections and firewall rules.
5. Reduces intrusion risk by not exposing the interfaces of logic and service nodes.

# Construction / Recognition

## To Construct/Create:
1. Place front-end nodes in the perimeter network region.
2. Separate them from logic/service nodes with firewalls and security measures.
3. In the cloud, use network connections and firewall rules to mimic the hardware DMZ.

## To Identify/Recognize:
1. A DMZ is the network layer between the untrusted Internet and the trusted back-end.

# Context & Application

- **Typical contexts**: Security-conscious deployments, e.g., an e-commerce site.
- **Common applications**: Shielding logic and service nodes from direct Internet exposure.
- **Historical/stylistic notes**: "Gone are the days when no one knew about Erlang and when security through obscurity was enough to safeguard you" (p. 383).

# Examples

**Example 1** (p. 383, Figure 13-2): Placing front-end nodes of an e-commerce site in a DMZ to reduce the risk of intrusion into logic and service nodes.

**Example 2** (pp. 383-384): Because access to front-end nodes via distributed Erlang would also mean access to logic and service nodes, communication across the DMZ must use sockets — possibly encrypted — authenticating every request.

# Relationships

## Builds Upon
- **Front-end node** — A DMZ is where front-end nodes are placed

## Enables
- A DMZ enables a secure separation between untrusted clients and trusted back-end nodes.

## Related
- **Sockets and ssl transport** — Used instead of distributed Erlang across the DMZ
- **Distributed Erlang** — Avoided across the DMZ for security reasons

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Connecting DMZ front-end nodes to logic nodes with distributed Erlang
  **Correction**: Use sockets, possibly encrypted, so a compromised front-end node does not grant full access to back-end nodes.

# Common Confusions

- **Confusion**: A DMZ requires dedicated hardware.
  **Clarification**: In cloud environments there is no hardware component; the DMZ is mimicked through network connections and firewall rules with the same end result.

# Source Reference

Chapter 12: Distributed Architectures, "Networking," pages 382-384. See Figure 13-2.

# Verification Notes

- Definition source: Direct quote from p. 383.
- Confidence rationale: HIGH — explicit definition in source.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
