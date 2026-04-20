---
# === CORE IDENTIFICATION ===
concept: Resources
slug: deno-resources

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
section: "Resources"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rid"
  - "resource id"
  - "resource ids"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-architecture
extends: []
related:
  - deno
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are Deno resources?"
  - "What is a rid in Deno?"
---

# Quick Definition
Resources (AKA `rid`) are Deno's version of file descriptors -- integer values used to refer to open files, sockets, and other concepts.

# Core Definition
In Deno's architecture, resources are integer-valued identifiers (resource IDs, or `rid`) that refer to open files, sockets, and other system concepts. They are directly analogous to file descriptors in Unix/Linux. The standard resources mirror Unix conventions: rid 0 is stdin, rid 1 is stdout, and rid 2 is stderr. Resources can be queried and closed programmatically through the `Deno` namespace API.

# Prerequisites
- deno-architecture: Understanding of Deno's internal architecture and the Linux analogy

# Key Properties
1. **Integer-valued** -- Each resource is identified by an integer, just like Unix file descriptors
2. **Standard streams** -- Default resources are stdin (0), stdout (1), and stderr (2)
3. **Queryable** -- `Deno.resources()` returns a map of all currently open resources
4. **Closeable** -- `Deno.close(rid)` closes a resource by its ID
5. **Broad scope** -- Resources represent not just files but also sockets and other OS-level concepts

# Construction / Recognition
```ts
console.log(Deno.resources());
// { 0: "stdin", 1: "stdout", 2: "stderr" }
Deno.close(0);
console.log(Deno.resources());
// { 1: "stdout", 2: "stderr" }
```

# Context & Application
Resources are used internally by Deno to track all open handles to system objects. Developers can use `Deno.resources()` for diagnostic purposes, such as checking for resource leaks in tests. Understanding resources is valuable for debugging and for contributors working on the Deno runtime itself.

# Examples
From runtime/contributing/architecture.md, section "Resources":
- Querying resources: `Deno.resources()` returns `{ 0: "stdin", 1: "stdout", 2: "stderr" }`
- Closing a resource: `Deno.close(0)` closes stdin, after which `Deno.resources()` returns `{ 1: "stdout", 2: "stderr" }`

# Relationships
## Builds Upon
- deno-architecture (resources are one of the core architectural concepts)

## Related
- deno (the runtime that manages resources)

## Contrasts With
- Unix file descriptors (analogous concept in the operating system)

# Common Errors
1. Forgetting to close resources -- can lead to resource leaks, particularly with file and socket handles

# Common Confusions
1. **Resources vs. file handles** -- Resources encompass more than just files; they include sockets, timers, and other system-level concepts

# Source Reference
- runtime/contributing/architecture.md, section "Resources": Definition and code examples for Deno resources

# Verification Notes
- High confidence: Resources are explicitly defined with code examples in the architecture documentation
