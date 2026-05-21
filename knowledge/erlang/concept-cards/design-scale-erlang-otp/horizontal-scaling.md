---
# === CORE IDENTIFICATION ===
concept: Horizontal Scaling
slug: horizontal-scaling

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
  - scaling out
  - scale out

# === TYPED RELATIONSHIPS ===
prerequisites:
  - scalability
extends:
  - scalability
related:
  - vertical-scaling
  - elasticity
  - amdahls-law
contrasts_with:
  - vertical-scaling

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is horizontal scaling?"
  - "What distinguishes horizontal from vertical scaling?"
---

# Quick Definition

Horizontal scaling, also called scaling out, increases capacity by adding more nodes and hardware — using cloud instances and commodity machines.

# Core Definition

"Scaling horizontally, also known as scaling out, is achieved using cloud instances and commodity hardware. If you need more processing power, you can rent, buy, or build your own machines and deploy extra nodes on them. Distributed systems, whether you want them or not, are your only viable approach. They will scale better, are much more cost-effective, and help you achieve high availability" (Cesarini & Vinoski, p. 426).

# Prerequisites

- **Scalability** — Horizontal scaling is one way to achieve scalability; understand scalability first.

# Key Properties

1. Increases capacity by adding more nodes and hardware.
2. Uses cloud instances and commodity hardware.
3. Distributed systems are the only viable approach to it.
4. Scales better and is more cost-effective than vertical scaling.
5. Helps achieve high availability.
6. Requires rethinking how applications are architected.

# Construction / Recognition

## To Construct/Create:
1. Rent, buy, or build commodity machines or cloud instances.
2. Deploy extra Erlang nodes on them.
3. Use the location transparency of processes so the system distributes across the cluster.
4. Re-architect applications for distribution.

## To Identify/Recognize:
1. Recognize horizontal scaling when capacity grows by adding machines/nodes rather than upgrading existing ones.

# Context & Application

- **Typical contexts**: Systems needing cost-effective growth and high availability.
- **Common applications**: Cloud deployments using commodity hardware; multicore machines where a single VM cannot use all cores.
- **Historical/stylistic notes**: With machines supporting thousands of cores, you must run multiple distributed VMs on a single computer to fully use the hardware — so you might as well scale horizontally (p. 426).

# Examples

**Example 1** (p. 426): Because Amdahl's Law applies to the sequential code in the Erlang VM itself, fully utilizing many-core hardware requires running multiple distributed VMs on a single computer.

**Example 2** (p. 426): In small clusters running distributed Erlang, Erlang/OTP scales vertically or horizontally in essentially the same way, using the location transparency of processes.

# Relationships

## Builds Upon
- **Scalability** — Horizontal scaling is a way to achieve scalability

## Enables
- **Elasticity** — Horizontal scaling enables adding/removing nodes at runtime
- Horizontal scaling enables high availability and cost-effective growth.

## Related
- **Vertical scaling** — The alternative scaling axis
- **Elasticity** — Runtime horizontal scaling
- **Amdahls law** — Motivates horizontal over vertical scaling

## Contrasts With
- **Vertical scaling** — Horizontal adds nodes/hardware; vertical upgrades a single machine

# Common Errors

- **Error**: Avoiding distributed systems to keep things simple
  **Correction**: For real scale and availability, distributed systems are the only viable approach — embrace horizontal scaling.

# Common Confusions

- **Confusion**: Horizontal scaling always behaves differently from vertical scaling in Erlang.
  **Clarification**: In small clusters running distributed Erlang, Erlang/OTP scales vertically or horizontally in essentially the same way, thanks to process location transparency.

# Source Reference

Chapter 14: Scaling Out, "Horizontal and Vertical Scaling," pages 424-426.

# Verification Notes

- Definition source: Direct quote from p. 426.
- Confidence rationale: HIGH — the source explicitly defines scaling out.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
