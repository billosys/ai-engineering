---
concept: Child Processes
slug: node-child-processes
category: node-apis
subcategory: child processes
tier: intermediate
source: "JavaScript: The Definitive Guide, 7th Edition"
source_slug: js-definitive-guide
authors: "David Flanagan"
chapter: "Server-Side JavaScript with Node"
chapter_number: 16
pdf_page: 637
section: "16.10 Working with Child Processes"
extraction_confidence: high
aliases:
  - "child_process module"
  - exec
  - spawn
  - fork
prerequisites:
  - node-programming-model
extends: []
related:
  - node-worker-threads
contrasts_with: []
answers_questions:
  - "What distinguishes Web Workers from Node worker threads?"
---

# Quick Definition

Node's "child_process" module provides functions to run external programs: `execSync()`/`exec()` run shell commands, `execFileSync()`/`execFile()` run executables directly, `spawn()` provides streaming I/O, and `fork()` runs Node scripts with an IPC channel.

# Core Definition

The child_process module offers multiple ways to run external programs. `execSync()` blocks and returns output as a string/Buffer. `exec()` is the async equivalent with a callback receiving (error, stdout, stderr). `execFileSync()`/`execFile()` bypass the shell for security. `spawn()` returns a ChildProcess with streaming stdout/stderr/stdin. `fork()` is specialized for running Node modules with built-in message passing via `send()` and "message" events (Flanagan, Ch. 16, pp. 637-642).

# Prerequisites

- **node-programming-model** — Child processes run within Node's environment.

# Key Properties

1. `execSync(command)`: synchronous, runs in a shell, returns stdout.
2. `execFile(file, args)`: async, no shell, safer for untrusted input.
3. `spawn(file, args)`: streaming I/O via ChildProcess.stdout/stderr/stdin.
4. `fork(modulePath)`: runs a Node module with IPC (send/message).
5. Options include `cwd`, `env`, `timeout`, `maxBuffer`, `shell`.

# Construction / Recognition

```javascript
const child_process = require("child_process");
let listing = child_process.execSync("ls -l", {encoding: "utf8"});
let child = child_process.fork(`${__dirname}/child.js`);
child.send({x: 4, y: 3});
child.on("message", msg => console.log(msg.hypotenuse));
```

# Context & Application

Used for running system commands, parallelizing CPU-intensive work across processes, and integrating with external tools.

# Examples

From the source (p. 641): Using `fork()` to send a message to a child process that computes a hypotenuse and sends the result back.

# Relationships

## Builds Upon
- **node-programming-model** — Processes run within Node's environment

## Enables
- System automation, parallel computation

## Related
- **node-worker-threads** — Lighter-weight alternative for CPU-intensive work

## Contrasts With
- (None)

# Common Errors

- **Error**: Passing unsanitized user input to `execSync()`.
  **Correction**: Use `execFileSync()` (no shell) to avoid command injection attacks.

# Common Confusions

- **Confusion**: `fork()` is the same as Unix fork().
  **Clarification**: Node's `fork()` starts a new Node process running a specified module; it is not a process clone.

# Source Reference

Chapter 16: Server-Side JavaScript with Node, Section 16.10, pages 637-642.

# Verification Notes

- Definition source: Direct from source text
- Confidence rationale: All four functions clearly documented
- Uncertainties: None
- Cross-reference status: Verified
