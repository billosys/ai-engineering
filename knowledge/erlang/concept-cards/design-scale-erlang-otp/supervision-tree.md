---
# === CORE IDENTIFICATION ===
concept: Supervision Tree
slug: supervision-tree

# === CLASSIFICATION ===
category: applications-releases
subcategory: supervision
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Supervisors"
chapter_number: 7
pdf_page: 188
section: "Supervision Trees"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "supervision hierarchy"
  - "process supervision tree"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - supervisor
extends: []
related:
  - worker-process
  - restart-strategy
  - otp-application
  - error-kernel
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a supervision tree?"
  - "What concepts are needed before building a supervision tree?"
  - "How does an application relate to its supervision tree?"
---

# Quick Definition

A supervision tree is a hierarchical structure in which supervisors form the nodes and workers form the leaves, with each supervisor monitoring and handling the children in the subtree it started. It is the structural basis of fault tolerance in Erlang/OTP.

# Core Definition

Fault tolerance is achieved by creating supervision trees, where the supervisors are the nodes and the workers are the leaves. Supervisors on a particular level monitor and handle the children in the subtrees they have started (Cesarini & Vinoski, p. 170). In OTP, programs are structured with one or more supervision trees: workers that are similar in nature or have dependencies are grouped together under the same subtree, started in order of dependency (p. 173). The tree gives the system a generic, deterministic way to isolate and recover from failures.

# Prerequisites

- **Supervisor** — A supervision tree is built from supervisors; you must understand what a supervisor is and does before composing them into a tree.

# Key Properties

1. Supervisors are the internal nodes; workers are the leaves.
2. A child of a supervisor may itself be a supervisor or a worker, so trees can be arbitrarily deep.
3. Supervisors on a level monitor only the children in the subtrees they started.
4. Dependent processes are grouped into the same subtree and started in order of dependency (left to right).
5. Failures escalate upward: when a supervisor exceeds its restart threshold it terminates, passing the problem to its parent.
6. In diagrams, supervisors are squares and workers are circles; a double ring denotes a process that traps exits.

# Construction / Recognition

## To Construct/Create:
1. Identify workers and group those that are similar or interdependent.
2. Assign each group a supervisor; order children by dependency.
3. Choose a restart strategy per supervisor that reflects the group's dependency structure.
4. Compose supervisors into a hierarchy with a single top-level supervisor.
5. Package the top-level supervisor inside an OTP application.

## To Identify/Recognize:
1. There is exactly one top-level supervisor at the root.
2. Every process is reachable from the root by parent-child links.
3. Each non-leaf is a supervisor; each leaf is a worker.

# Context & Application

- **Typical contexts**: The structural backbone of every OTP application; the unit a release loads and starts.
- **Common applications**: Isolating faults so a crash affects only a subtree; escalating unrecoverable problems upward; recreating known-good state on restart.
- **Historical/stylistic notes**: The book stresses that the start order and restart strategy "form part of the supervision strategy of a system" and are often decided by an architect with a whole-system view (p. 174).

# Examples

**Example 1** (p. 173, Figure 8-2): The frequency allocator system — a top supervisor starts the overload event manager, then the frequency allocator, then a phone supervisor that manages all phone FSMs.

**Example 2** (p. 191): `bsc_sup`, the top-level supervisor that starts `freq_overload`, `frequency`, and `simple_phone_sup` (itself a supervisor), demonstrating a two-level tree.

## Worked Example

`bsc_sup` building a tree (p. 191):

```erlang
init(_) ->
    ChildSpecList = [child(freq_overload, worker),
                     child(frequency, worker),
                     child(simple_phone_sup, supervisor)],
    {ok,{{rest_for_one, 2, 3600}, ChildSpecList}}.
```

`simple_phone_sup` appears in the child list as a `supervisor`, making `bsc_sup` a node above another supervisor.

# Relationships

## Builds Upon
- **Supervisor** — Supervision trees are composed of supervisors as nodes.

## Enables
- **OTP application** — A normal application packages a supervision tree as a unit.
- **Error kernel** — The tree's escalation structure realizes the error-kernel design.

## Related
- **Worker process** — Workers form the leaves of the tree.
- **Restart strategy** — Each supervisor's strategy shapes how failures propagate within the tree.

## Contrasts With
- *(none — supervision trees have no natural contrast within this source)*

# Common Errors

- **Error**: Placing interdependent workers in different subtrees.
  **Correction**: Group dependent processes under the same supervisor so dependency-aware restart strategies can act on them.

- **Error**: Starting children in arbitrary order.
  **Correction**: Start children left to right in dependency order so `rest_for_one` and `one_for_all` restarts behave correctly.

# Common Confusions

- **Confusion**: Thinking the tree is just an organizational diagram.
  **Clarification**: The tree is a live runtime structure of linked processes; its shape directly determines fault isolation and recovery.

- **Confusion**: Believing every node restarts every failure locally.
  **Clarification**: Unrecoverable failures escalate up the tree until a supervisor high enough can resolve them.

# Source Reference

Chapter 7: Supervisors, "Supervision Trees" and "OTP Supervisors," pages 170-174. See Figures 8-1 and 8-2 (supervision trees).

# Verification Notes

- Definition source: Direct adaptation from p. 170 ("Fault tolerance is achieved by creating supervision trees...").
- Confidence rationale: HIGH — explicitly defined with figures and multiple concrete examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
</invoke>
