---
# === CORE IDENTIFICATION ===
concept: Web Workers
slug: web-workers

# === CLASSIFICATION ===
category: async-programming
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Foundations of asynchronous programming in JavaScript"
chapter_number: 42
pdf_page: null
section: "42.2.2 How can we avoid blocking the browser?"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases:
  - Worker
  - background worker

# === TYPED RELATIONSHIPS ===
prerequisites:
  - event-loop
extends: []
related:
  - blocking-the-javascript-process
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What concepts are prerequisite to understanding Promises?"
---

# Quick Definition

A Web Worker is a heavyweight process that runs concurrently with the main JavaScript process, has its own runtime environment, and communicates with the main thread via message passing.

# Core Definition

"Exploring JavaScript" Ch. 42 describes Web Workers as a way to perform operations in a separate process: "A Web Worker is a heavyweight process that runs concurrently to the main process. It has its own runtime environment (global variables, etc.). It is completely isolated; communication happens via message passing."

# Prerequisites

- **Event loop** -- understanding why separate processes are sometimes needed

# Key Properties

1. Runs in a separate process with its own runtime environment
2. Completely isolated from the main thread
3. Communication via message passing only
4. Heavyweight compared to async patterns within the main thread

# Construction / Recognition

Web Workers are created via the `Worker` constructor and communicate through `postMessage()` and `onmessage` handlers.

# Context & Application

Used for CPU-intensive operations that would block the main thread (image processing, complex calculations, data parsing). Not a replacement for async patterns but a complement for truly parallel computation.

# Examples

Referenced in the source as one of three strategies to avoid blocking the browser. Detailed usage is documented at MDN Web Workers API.

(Ch. 42, Section 42.2.2, lines 161-167)

# Relationships

## Builds Upon
- **Event loop** -- Web Workers provide true parallelism beyond the event loop

## Related
- **Blocking the JavaScript process** -- Web Workers are one solution to blocking

# Common Errors

- **Error**: Trying to access the DOM from a Web Worker
  **Correction**: Workers are isolated; they cannot access the DOM directly

# Common Confusions

- **Confusion**: Web Workers and async functions serve the same purpose
  **Clarification**: Async functions handle I/O-bound waiting; Web Workers handle CPU-bound parallel computation

# Source Reference

Chapter 42: Foundations of asynchronous programming in JavaScript, Section 42.2.2, lines 161-167.

# Verification Notes

- Definition source: direct quotation from source
- Confidence rationale: brief but explicit definition; details deferred to MDN
- Cross-reference status: unverified (external reference)
