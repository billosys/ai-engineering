---
# === CORE IDENTIFICATION ===
concept: Deno Architecture
slug: deno-architecture

# === CLASSIFICATION ===
category: architecture
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/contributing/architecture.md"
chapter_number: null
pdf_page: null
section: "Deno and Linux analogy"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Deno internals"
  - "Deno internal architecture"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno
extends: []
related:
  - deno-resources
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is Deno's internal architecture organized?"
  - "What is the Linux analogy for Deno's architecture?"
---

# Quick Definition
Deno's internal architecture maps to a Linux analogy where ops are syscalls, resources are file descriptors, Web Workers are processes, and Tokio is the scheduler.

# Core Definition
Deno's architecture is best understood through an analogy with the Linux operating system. The runtime maps its internal concepts to familiar OS-level abstractions: **Ops** correspond to syscalls (the interface between JavaScript and the Rust-based runtime), **Resources** (identified by resource IDs or `rid`) correspond to file descriptors, **Web Workers** correspond to processes, and **Tokio** serves as the scheduler. The standard library (`@std` on JSR) corresponds to userland libraries (libc++/glib/boost), `Deno.metrics()` corresponds to `/proc/$$/stat`, and the documentation corresponds to man pages.

# Prerequisites
- deno: Understanding of Deno as a runtime

# Key Properties
1. **Ops as syscalls** -- Ops are the boundary between JavaScript and the Rust runtime, analogous to system calls in Linux
2. **Resources as file descriptors** -- Integer-valued resource IDs (`rid`) refer to open files, sockets, and other concepts
3. **Web Workers as processes** -- Web Workers provide isolated execution contexts, analogous to OS processes
4. **Tokio as scheduler** -- The Tokio async runtime handles scheduling of asynchronous operations
5. **Standard library as userland** -- `https://jsr.io/@std` provides the equivalent of userland libraries
6. **Metrics as proc stats** -- `Deno.metrics()` provides internal counters analogous to `/proc/$$/stat`

# Construction / Recognition
The architecture table from the documentation:

| Linux | Deno |
|-------|------|
| Processes | Web Workers |
| Syscalls | Ops |
| File descriptors (fd) | Resource ids (rid) |
| Scheduler | Tokio |
| Userland: libc++/glib/boost | https://jsr.io/@std |
| /proc/$$/stat | Deno.metrics() |
| man pages | deno types / https://docs.deno.com |

# Context & Application
Understanding Deno's architecture is important for contributors to the Deno runtime and for developers who need to understand how Deno manages system resources internally. The ops/resources model explains how JavaScript code interacts with the underlying operating system through the Rust layer.

# Examples
From runtime/contributing/architecture.md:
- Metrics example: `console.table(Deno.metrics())` displays internal counters including opsDispatched, opsCompleted, bytesSentControl, bytesSentData, and bytesReceived
- Conference reference: Bartek Iwanczuk's "Deno internals - how modern JS/TS runtime is built" at Paris Deno (Oct 2020)

# Relationships
## Builds Upon
- deno

## Enables
- deno-resources

## Related
- deno-security-model (ops enforce the permission boundary)

## Contrasts With
- Linux kernel architecture (analogous, not identical)

# Common Errors
1. Confusing ops with JavaScript function calls -- ops are specifically the Rust-JavaScript boundary, not general function calls

# Common Confusions
1. **Ops vs. regular functions** -- Ops are the specific mechanism for crossing the JavaScript-to-Rust boundary, similar to how syscalls cross the user-to-kernel boundary in Linux

# Source Reference
- runtime/contributing/architecture.md: Architecture overview with Linux analogy table, resources, and metrics

# Verification Notes
- High confidence: Architecture is explicitly described with a detailed analogy table
- Conference references provide additional context from core contributors
