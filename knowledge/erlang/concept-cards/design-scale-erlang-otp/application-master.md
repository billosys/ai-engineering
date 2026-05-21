---
# === CORE IDENTIFICATION ===
concept: Application Master
slug: application-master

# === CLASSIFICATION ===
category: applications-releases
subcategory: applications
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Applications"
chapter_number: 8
pdf_page: 222
section: "How Applications Run"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "application master processes"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - application-controller
extends: []
related:
  - supervisor
  - application-behaviour
contrasts_with:
  - application-controller

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP application?"
  - "How does an application relate to its supervision tree?"
---

# Quick Definition

The application master is the pair of processes the application controller starts for each OTP application; it starts and monitors that application's top-level supervisor and takes action if the supervisor terminates.

# Core Definition

For every OTP application, the application controller starts a pair of processes called the application master; it is the master that starts and monitors the top-level supervisor and takes action if it terminates (Cesarini & Vinoski, p. 205). When an application starts, the master spawns the top-level supervisor, which in turn starts the remainder of the supervision tree; when the application is stopped, the master terminates the top-level supervisor, propagating the shutdown exit signal to all behavior processes in the tree. One of the master processes calls the `Mod:start(StartType, StartArgs)` callback (pp. 205-209).

# Prerequisites

- **OTP application** — The master manages one OTP application.
- **Application controller** — The controller starts the master process pair.

# Key Properties

1. A pair of processes exists per OTP application.
2. Started by the application controller.
3. It spawns and monitors the application's top-level supervisor.
4. It calls the application callback module's `start/2` function.
5. On stop, it terminates the top-level supervisor, propagating `shutdown` through the tree.
6. It takes action if the top-level supervisor terminates.

# Construction / Recognition

## To Construct/Create:
1. Nothing to construct — the controller starts the master automatically per application.

## To Identify/Recognize:
1. Two linked processes associated with an application.
2. One is linked to the application's top-level supervisor (visible in the observer's Applications tab).

# Context & Application

- **Typical contexts**: One master pair per running application on a node.
- **Common applications**: Bridging the application controller and the application's supervision tree.
- **Historical/stylistic notes**: In the observer tool, the book points out the two application master processes for the `bsc` app, one linked to the `bsc` top-level supervisor (p. 216).

# Examples

**Example 1** (p. 205, Figure 9-2): The application master starting and monitoring the top-level supervisor.

**Example 2** (p. 216): The observer's Applications tab showing the two `bsc` application master processes, one linked to the `bsc` top-level supervisor.

## Worked Example

The book does not give a code listing for the master; it is a VM-internal process. Observing it (p. 216):

```text
1> observer:start().
%% Applications tab > bsc: two application master processes,
%% one linked to the bsc top-level supervisor
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- *(none)*

## Related
- **Supervisor** — The master spawns and monitors the application's top-level supervisor.
- **Application behaviour** — A master process calls the application callback module's `start/2`.

## Contrasts With
- **Application controller** — One controller per node manages all applications; one master pair per application manages that application's supervision tree.

# Common Errors

- **Error**: Assuming the application keeps running after its top-level supervisor crashes.
  **Correction**: The master monitors the top-level supervisor and takes action when it terminates — a crashed top-level supervisor takes the application down.

# Common Confusions

- **Confusion**: Thinking there is one application master process per application.
  **Clarification**: The controller starts a *pair* of application master processes for each application.

# Source Reference

Chapter 8: Applications, "How Applications Run" and "The Observer Tool," pages 205, 216. See Figure 9-2 (Application controller).

# Verification Notes

- Definition source: Direct adaptation from p. 205.
- Confidence rationale: HIGH — explicitly named and described, confirmed by the observer walkthrough.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
