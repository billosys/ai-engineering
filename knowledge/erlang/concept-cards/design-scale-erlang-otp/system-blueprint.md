---
# === CORE IDENTIFICATION ===
concept: System Blueprint
slug: system-blueprint

# === CLASSIFICATION ===
category: applications-releases
subcategory: deployment-design
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Scaling Out"
chapter_number: 14
pdf_page: 424
section: "System Blueprints"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - system blueprints
  - cluster blueprint
  - resource blueprint

# === TYPED RELATIONSHIPS ===
prerequisites:
  - capacity-planning
  - cluster
extends: []
related:
  - node-family
  - elasticity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a system blueprint?"
  - "How do I formalize my distributed system's design for deployment?"
---

# Quick Definition

A system blueprint combines a resource blueprint (available hardware/cloud resources) and a cluster blueprint (logical node-family description) so a distributed system can be understood and deployed.

# Core Definition

"Your resource blueprint specifies the available resources on which to run your cluster. It includes descriptions of hardware specifications or cloud instances, routers, load balancers, firewalls, and other network components" (Cesarini & Vinoski, p. 438). "Your cluster blueprint ... is a logical description of your system, specifying node families and the connectivity within and among them ... Your cluster and resource blueprints are combined in what we call a system blueprint. With the system blueprint in hand, you can understand both how your distributed system is structured and how it can be deployed on hardware or cloud instances" (p. 438).

# Prerequisites

- **Capacity planning** — The cluster blueprint is derived from capacity-planning lessons.
- **Cluster** — A blueprint describes a cluster's structure.

# Key Properties

1. A system blueprint combines a resource blueprint and a cluster blueprint.
2. The resource blueprint specifies hardware/cloud instances, routers, load balancers, firewalls, and network components.
3. The cluster blueprint is a logical description specifying node families and their connectivity.
4. The cluster blueprint defines node-type ratios for a balanced system.
5. It is used by orchestration programs to scale the cluster in an orderly fashion.
6. Cluster blueprints are analogous to an Amazon autoscaling group but more detailed.

# Construction / Recognition

## To Construct/Create:
1. Build the resource blueprint: hardware/cloud instances, routers, load balancers, firewalls.
2. Build the cluster blueprint from capacity-planning lessons: node families, connectivity, node-type ratios.
3. Combine them into the system blueprint.
4. Validate the blueprint through capacity testing on target hardware.

## To Identify/Recognize:
1. Recognize a system blueprint as the combined logical-plus-resource description that lets a distributed system be deployed.

# Context & Application

- **Typical contexts**: Step 7 of designing a scalable system — formalizing design choices.
- **Common applications**: Driving orchestration programs; deploying a new cluster when one hits an upper limit.
- **Historical/stylistic notes**: Distributed cluster patterns (multiple instances of node types) are also called system blueprints (chapter 12, p. 381).

# Examples

**Example 1** (p. 438): The cluster blueprint defines the ratios of different node types needed for a balanced system, and is used by orchestration programs to scale the cluster without creating imbalances.

**Example 2** (p. 438): Cluster blueprints are analogous to an Amazon autoscaling group on AWS, but more detailed; when you hit an upper limit in one cluster, you deploy a new cluster.

# Relationships

## Builds Upon
- **Capacity planning** — The cluster blueprint is derived from capacity-planning lessons
- **Cluster** — A blueprint describes cluster structure

## Enables
- A system blueprint enables orderly, orchestrated deployment and scaling.

## Related
- **Node family** — Cluster blueprints specify node families and their connectivity
- **Elasticity** — Blueprints enable orderly elastic scaling

## Contrasts With
- None noted in this source.

# Common Errors

- **Error**: Treating a system blueprint as fixed
  **Correction**: The blueprint must be validated through capacity testing on target hardware and revisited as requirements evolve.

# Common Confusions

- **Confusion**: A system blueprint is just a hardware list.
  **Clarification**: It combines the hardware-oriented resource blueprint with the logical cluster blueprint describing node families and connectivity.

# Source Reference

Chapter 14: Scaling Out, "System Blueprints," page 438. See also Chapter 12, page 381 (distributed cluster patterns as system blueprints).

# Verification Notes

- Definition source: Direct quotes from p. 438.
- Confidence rationale: HIGH — the source dedicates a named section with explicit definitions of all three blueprint terms.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction — no pre-existing card for this concept.
