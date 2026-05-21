---
# === CORE IDENTIFICATION ===
concept: Upgrading in Distributed Environments
slug: upgrading-in-distributed-environments

# === CLASSIFICATION ===
category: distribution
subcategory: release-upgrades
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "Release Upgrades"
chapter_number: 11
pdf_page: 336
section: "Upgrading in Distributed Environments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - sync_nodes
  - synchronized distributed upgrade
  - rolling upgrade

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release-upgrade
extends: []
related:
  - low-level-instructions
  - installing-an-upgrade
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I upgrade a release across distributed nodes?"
  - "How do I perform a release upgrade?"
---

# Quick Definition

Upgrading in distributed environments is the synchronized upgrade of multiple nodes, coordinated by the `sync_nodes` instruction. It is safe only for small, reliable clusters; for larger or unreliable networks, rolling upgrades one node at a time are recommended.

# Core Definition

Synchronized software upgrades in distributed environments are possible by including the `sync_nodes` low-level instruction in the `.appup` file; the generated `relup` script then synchronizes with the other nodes also waiting to be upgraded and upgrades them when they too attempt to synchronize (Cesarini & Vinoski, p. 352-354, pdf p. 336). Synchronization is triggered by `{sync_nodes, Id, NodeList}` or `{sync_nodes, Id, {Mod, Func, ArgList}}`. For larger clusters, clusters across data centers, or unreliable networks, the recommended approach is a *rolling upgrade* — upgrading one node at a time after ensuring new-release nodes interoperate with old-release nodes.

# Prerequisites

- **Release upgrade** — Distributed upgrading extends the release-upgrade procedure across nodes; that concept comes first.

# Key Properties

1. `sync_nodes` is a low-level `.appup` instruction enabling synchronized distributed upgrades.
2. Two forms: `{sync_nodes, Id, NodeList}` (hardcoded nodes) and `{sync_nodes, Id, {Mod, Func, ArgList}}` (computed nodes).
3. `Id` can be any valid Erlang term; remote nodes must run the same instruction with the same `Id`.
4. There is no timeout — the local node hangs until all remote nodes execute `sync_nodes` or connectivity is lost.
5. Losing connectivity (partition or crash) restarts the node with the old release.
6. Poorly synchronized upgrades can hang the whole cluster or cause cascading restart failures.
7. Synchronized distributed upgrades are recommended only for small, reliable clusters.
8. For larger or unreliable clusters, use rolling upgrades — one node at a time — with backward-compatible, interoperable releases.

# Construction / Recognition

## To Perform a Synchronized Distributed Upgrade:
1. Add a `sync_nodes` instruction to the `.appup` file.
2. Choose an `Id` and ensure all nodes run the same instruction with it.
3. Generate the `relup`; install the upgrade on each node.
4. Each node synchronizes and upgrades when all nodes reach `sync_nodes`.

## To Perform a Rolling Upgrade Instead:
1. Verify old and new releases are backward-compatible and interoperable.
2. Upgrade a few nodes, monitor them, then continue across the cluster.

# Context & Application

- **Typical contexts**: Upgrading clustered systems where nodes have cross-node dependencies.
- **Common applications**: Synchronized upgrades for small clusters in one subrack; rolling upgrades for data-center-scale or cloud clusters.
- **Historical/stylistic notes**: Distributed Erlang was originally intended for clusters behind firewalls in the same data center or subrack — often on the same backplane as the controlled hardware.

# Examples

**Example 1** (p. 353): The two synchronization instructions:

```erlang
{sync_nodes, Id, NodeList}
{sync_nodes, Id, {Mod,Func,ArgList}}
```

`NodeList` can be hardcoded, or the second form invokes `apply(Mod, Func, ArgList)` to get the list of nodes recognizing `Id`.

**Example 2** (p. 354): If connectivity to a remote node is lost during synchronization, the node restarts with the old release; there is no timeout, so the local node hangs until all remote nodes synchronize or connectivity is lost.

# Relationships

## Builds Upon
- **Release upgrade** — Distributed upgrading extends release upgrades across nodes.

## Related
- **Low-level instructions** — `sync_nodes` is a low-level `.appup`/`relup` instruction.
- **Installing an upgrade** — Each node still installs the upgrade locally.

# Common Errors

- **Error**: Using synchronized distributed upgrades on a large or unreliable cluster.
  **Correction**: Use rolling upgrades one node at a time; synchronized upgrades risk hangs and cascading restart failures.

- **Error**: Running `sync_nodes` with mismatched `Id`s across nodes.
  **Correction**: All participating nodes must execute the same instruction with the same `Id` for synchronization to succeed.

# Common Confusions

- **Confusion**: Thinking `sync_nodes` has a timeout.
  **Clarification**: There is no timeout — the local node hangs until all remote nodes synchronize or connectivity is lost.

- **Confusion**: Believing synchronized distributed upgrades are always the right choice.
  **Clarification**: They suit only small, reliable clusters; rolling upgrades are recommended otherwise.

# Source Reference

Chapter 11: Release Upgrades, section "Upgrading in Distributed Environments," pages 352-354 (pdf p. 336).

# Verification Notes

- Definition source: Direct adaptation of pp. 352-354.
- Confidence rationale: HIGH — the source explicitly describes `sync_nodes`, its forms, risks, and the rolling-upgrade alternative.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
