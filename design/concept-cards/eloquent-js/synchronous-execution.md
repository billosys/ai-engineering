---
# === CORE IDENTIFICATION ===
concept: Synchronous Execution
slug: synchronous-execution

# === CLASSIFICATION ===
category: asynchronous-programming
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Eloquent JavaScript, 4th Edition"
source_slug: eloquent-js
authors: "Marijn Haverbeke"
chapter: "Asynchronous Programming"
chapter_number: 11
pdf_page: null
section: "Asynchronicity"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - synchronous programming
  - blocking execution

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
extends: []
related:
  - asynchronous-programming
contrasts_with:
  - asynchronous-programming

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes synchronous from asynchronous code?"
---

# Quick Definition
In synchronous programming, things happen one at a time -- when a function performs a long-running action, it returns only when the action has finished, blocking the program in the meantime.

# Core Definition
"In a *synchronous* programming model, things happen one at a time. When you call a function that performs a long-running action, it returns only when the action has finished and it can return the result. This stops your program for the time the action takes." (Eloquent JavaScript, Ch. 11, lines 56-60)

# Prerequisites
- **Functions**: Understanding how function calls and return values work

# Key Properties
1. Operations execute sequentially, one after another
2. Each operation must complete before the next one begins
3. Waiting for actions to finish is *implicit* -- it happens automatically
4. The total time for multiple operations is the sum of all individual operation times

# Construction / Recognition
Synchronous code is the default in most programming contexts: regular function calls, loops, and expressions all execute synchronously.

# Context & Application
Synchronous execution is straightforward and easy to reason about, but becomes problematic when operations take a long time (e.g., network requests), as the entire program blocks.

# Examples
From the source: "In a synchronous environment, where the request function returns only after it has done its work, the easiest way to perform this task is to make the requests one after the other. This has the drawback that the second request will be started only when the first has finished." (lines 75-79)

# Relationships
## Builds Upon
- Basic function calls and return values
## Enables
- Simple, linear program flow that is easy to understand
## Related
- Thread-based concurrency as an alternative for parallel synchronous work
## Contrasts With
- Asynchronous programming, where operations can overlap

# Common Errors
- **Error**: Performing slow I/O operations synchronously in a browser, causing the UI to freeze
  **Correction**: Use asynchronous patterns for operations that may take significant time

# Common Confusions
- **Confusion**: Synchronous code is always bad for performance
  **Clarification**: Synchronous execution is perfectly fine for CPU-bound operations; it only becomes problematic for I/O-bound operations where waiting wastes time

# Source Reference
Chapter 11: Asynchronous Programming, Section "Asynchronicity", lines 53-115 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Clearly defined as contrast to asynchronous model
- Cross-reference status: verified
