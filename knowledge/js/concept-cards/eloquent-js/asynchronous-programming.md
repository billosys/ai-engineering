---
# === CORE IDENTIFICATION ===
concept: Asynchronous Programming
slug: asynchronous-programming

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
  - async programming
  - asynchrony

# === TYPED RELATIONSHIPS ===
prerequisites:
  - function
  - closure
extends: []
related:
  - synchronous-execution
  - callback
  - promise
  - event-loop
contrasts_with:
  - synchronous-execution

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes synchronous from asynchronous code?"
  - "What must I know before using promises and async/await?"
---

# Quick Definition
Asynchronous programming is a model that allows multiple things to happen at the same time, where a program continues to run while waiting for long-running actions to complete.

# Core Definition
"An *asynchronous* model allows multiple things to happen at the same time. When you start an action, your program continues to run. When the action finishes, the program is informed and gets access to the result (for example, the data read from disk)." (Eloquent JavaScript, Ch. 11, lines 63-67)

# Prerequisites
- **Functions**: Asynchronous programming relies heavily on passing functions as callbacks or handlers
- **Closures**: Callback functions need to capture variables from their surrounding scope

# Key Properties
1. The program does not stop while waiting for a long-running action
2. Waiting for actions to finish is *explicit* and under the programmer's control
3. Asynchronicity is contagious -- any function that calls an asynchronous function must itself be asynchronous
4. Both browsers and Node.js make potentially slow operations asynchronous

# Construction / Recognition
Asynchronous code is recognized by:
- Use of callbacks, promises, or async/await
- Operations that involve network requests, file I/O, or timers
- Code that registers handlers to be called when something completes

# Context & Application
Used whenever a program must perform operations that take unpredictable amounts of time, such as network requests, file reading, or waiting for user input, without blocking other work.

# Examples
From the source text, comparing synchronous and asynchronous approaches:
"In a synchronous environment, where the request function returns only after it has done its work, the easiest way to perform this task is to make the requests one after the other. This has the drawback that the second request will be started only when the first has finished. The total time taken will be at least the sum of the two response times." (lines 75-80)

In the asynchronous model, both requests can be started simultaneously, and the program is notified when each completes.

# Relationships
## Builds Upon
- Functions and closures form the foundation for asynchronous patterns
## Enables
- Callbacks, promises, and async/await as specific async patterns
- Non-blocking I/O in browsers and Node.js
## Related
- Event loop (the mechanism that schedules async callbacks)
## Contrasts With
- Synchronous execution (where operations block until complete)

# Common Errors
- **Error**: Treating asynchronous code as if it runs synchronously (e.g., expecting a return value immediately)
  **Correction**: Use callbacks, promises, or await to handle the eventual result

# Common Confusions
- **Confusion**: Asynchronous means parallel or multi-threaded
  **Clarification**: JavaScript is single-threaded; asynchronous operations are scheduled on the event loop, not run simultaneously on multiple threads. "Both prominent JavaScript programming platforms---browsers and Node.js---make operations that might take a while asynchronous, rather than relying on threads." (lines 118-120)

# Source Reference
Chapter 11: Asynchronous Programming, Section "Asynchronicity", lines 53-123 of 11-asynchronous-programming.md.

# Verification Notes
- Definition source: direct quotation
- Confidence rationale: Central topic of chapter with extensive direct definitions
- Cross-reference status: verified against chapter summary
