---
# === CORE IDENTIFICATION ===
concept: Application Controller
slug: application-controller

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
  - "application_controller"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
extends: []
related:
  - application-master
  - distributed-application
contrasts_with:
  - application-master

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP application?"
  - "How does an application relate to its supervision tree?"
---

# Quick Definition

The application controller is a single process started on every Erlang node that manages all OTP applications, starting a pair of application master processes for each one.

# Core Definition

Behind the scenes in the Erlang VM a process called the application controller starts on every node (Cesarini & Vinoski, p. 205). For every OTP application, the controller starts a pair of processes called the *application master*; it is the master that starts and monitors the top-level supervisor. The application controller is responsible for loading, starting, stopping, and unloading applications, and for honoring application dependencies. It also converts the `included_applications` list into an environment variable, and reads the system configuration file passed via `erl -config` (pp. 205, 217).

# Prerequisites

- **OTP application** — The application controller exists to manage OTP applications.

# Key Properties

1. Exactly one application controller process runs per node.
2. It starts a pair of application master processes for each application.
3. It loads, starts, stops, and unloads applications as whole units.
4. It enforces application start/stop ordering based on dependencies.
5. It reads the system configuration file (`erl -config filename`).

# Construction / Recognition

## To Construct/Create:
1. Nothing to construct — the controller starts automatically on every node.

## To Identify/Recognize:
1. A single per-node VM process named `application_controller`.
2. It is the parent of the application master processes.

# Context & Application

- **Typical contexts**: Present on every running Erlang node.
- **Common applications**: Coordinating which applications start at boot; reading config files.
- **Historical/stylistic notes**: The book notes you tell the application controller which config file to read at VM startup with `erl -config filename` (p. 217).

# Examples

**Example 1** (p. 205, Figure 9-2): The application controller starting a pair of application master processes per OTP application.

**Example 2** (p. 217): The application controller reading a system configuration file specified with `erl -config bsc.config`.

## Worked Example

The book does not give a code listing for the controller; it is a VM-internal process. Telling it which config file to use (p. 217):

```text
erl -config bsc.config
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- **Application master** — The controller starts the master process pair for each application.

## Related
- **Distributed application** — Managed by a related process, the *distributed application controller* (`dist_ac`).

## Contrasts With
- **Application master** — The controller is one per node and manages *all* applications; a master pair exists *per* application and manages that application's top-level supervisor.

# Common Errors

- **Error**: Expecting the controller to start an application whose dependencies are not running.
  **Correction**: Provide dependencies first or use `application:ensure_all_started/1`; the controller starts applications only in dependency order.

# Common Confusions

- **Confusion**: Confusing the application controller with the application master.
  **Clarification**: There is one controller per node; it starts a master *pair* per application. The master, not the controller, monitors the application's top-level supervisor.

# Source Reference

Chapter 8: Applications, "How Applications Run" and "Environment Variables," pages 205, 217. See Figure 9-2 (Application controller).

# Verification Notes

- Definition source: Direct adaptation from p. 205.
- Confidence rationale: HIGH — explicitly named and described with a figure.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
