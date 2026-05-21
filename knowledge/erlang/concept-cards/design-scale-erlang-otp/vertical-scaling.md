---
# === CORE IDENTIFICATION ===
concept: Vertical Scaling
slug: vertical-scaling

# === CLASSIFICATION ===
category: performance
subcategory: scaling
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "Horizontal and Vertical Scaling"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - scaling up
  - scale up

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scalability
extends:
  - scalability
related:
  - horizontal-scaling
  - amdahls-law
  - single-point-of-failure
contrasts_with:
  - horizontal-scaling

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is vertical scaling?"
  - "What distinguishes horizontal from vertical scaling?"
---

# Quick Definition

Vertical scaling, also called scaling up, increases capacity by using a more powerful single computer — bigger chips, more cores and memory, faster disks.

# Core Definition

"Vertical scalability, also referred to as scaling up ... You have a single server that guarantees strong consistency of your data. You just add larger chips, faster clock cycles, more cores and memory, a faster disk, and more network interfaces" (Cesarini & Vinoski, p. 425). But this approach "is dated, because servers can only get so big, and the bigger they get, the more expensive they become. And you need at least two, because a super fast computer can still be a single point of failure" (p. 426).

# Prerequisites

- **Scalability** — Vertical scaling is one way to achieve scalability; understand scalability first.

# Key Properties

1. Increases capacity by upgrading a single computer.
2. Adds larger chips, faster clocks, more cores and memory, faster disks, more network interfaces.
3. A single server can guarantee strong consistency of its data.
4. Limited — servers can only get so big, and bigger servers cost disproportionately more.
5. A single super-fast computer is still a single point of failure, so at least two are needed.
6. Amdahl's Law limits the benefit of adding cores.

# Construction / Recognition

## To Construct/Create:
1. Upgrade the existing server's chips, cores, memory, disk, and network interfaces.
2. Provide at least a second machine to avoid a single point of failure.

## To Identify/Recognize:
1. Recognize vertical scaling when capacity grows by upgrading one machine rather than adding nodes.

# Context & Application

- **Typical contexts**: Single-server systems prioritizing strong consistency and simplicity.
- **Common applications**: Small systems before the move to distribution becomes necessary.
- **Historical/stylistic notes**: The approach is "dated"; with thousands of cores, a single VM cannot optimally use the hardware, and Amdahl's Law applies to the VM's own sequential code (p. 426).

# Examples

**Example 1** (p. 425): Scaling up means adding larger chips, faster clock cycles, more cores and memory, a faster disk, and more network interfaces to a single server.

**Example 2** (p. 426): Even a super-fast computer can be a single point of failure, so you need at least two — at which point you might as well scale horizontally.

# Relationships

## Builds Upon
- **Scalability** — Vertical scaling is a way to achieve scalability

## Enables
- Vertical scaling enables capacity growth without distribution, for simple systems.

## Related
- **Horizontal scaling** — The alternative scaling axis
- **Amdahls law** — Limits the benefit of adding cores when scaling up
- **Single point of failure** — A single scaled-up server is still a single point of failure

## Contrasts With
- **Horizontal scaling** — Vertical upgrades one machine; horizontal adds nodes/hardware

# Common Errors

- **Error**: Relying solely on a single, ever-bigger server
  **Correction**: Servers can only get so big and a single one is a single point of failure; you need at least two, which favors horizontal scaling.

# Common Confusions

- **Confusion**: Vertical scaling has unlimited headroom.
  **Clarification**: Servers can only get so big and become disproportionately expensive; Amdahl's Law also caps the benefit of more cores.

# Source Reference

Chapter 14: Scaling Out, "Horizontal and Vertical Scaling," pages 425-426.

# Verification Notes

- Definition source: Direct quote from pp. 425-426.
- Confidence rationale: HIGH — the source explicitly defines scaling up.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
