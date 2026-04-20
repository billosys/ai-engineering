---
# === CORE IDENTIFICATION ===
concept: Biome Daemon
slug: biome-daemon

# === CLASSIFICATION ===
category: architecture
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "internals/architecture.mdx"
chapter_number: null
pdf_page: null
section: "Daemon"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "daemon"
  - "Biome server"
  - "background server"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome
extends: []
related:
  - biome-scanner
  - concrete-syntax-tree
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Biome daemon?"
  - "How does Biome use a server-client architecture?"
---

# Quick Definition
The Biome daemon is a long-running background server process that Biome spawns to handle requests from editors and the CLI using a server-client architecture.

# Core Definition
Biome uses a server-client architecture to run its tasks. A daemon is a long-running server that Biome spawns in the background and uses to process requests from the editor and CLI. This architecture allows Biome to maintain state and provide fast responses to editor requests without reinitializing on every operation.

# Prerequisites
- biome: Must understand what Biome is and its role as a toolchain

# Key Properties
1. **Server-client architecture** -- Biome operates with a background server and client requests
2. **Long-running process** -- The daemon persists in the background rather than starting fresh for each operation
3. **Dual client support** -- Processes requests from both the editor (IDE extensions) and the CLI
4. **Background spawning** -- Biome automatically spawns the daemon as needed

# Construction / Recognition
The daemon is spawned automatically by Biome when needed. It runs in the background and is typically not something developers interact with directly. Its presence can be observed through process listings showing a Biome server process.

# Context & Application
The daemon architecture is essential for editor integration, where rapid responses to formatting and linting requests are needed as the developer types. By maintaining a long-running process, Biome avoids the startup cost of re-parsing configurations, re-scanning the file system, and re-initializing internal state for every keystroke or save event.

# Examples
From internals/architecture.mdx, "Daemon" section:
- "Biome uses a server-client architecture to run its tasks."
- "A daemon is a long-running server that Biome spawns in the background and uses to process requests from the editor and CLI."

# Relationships
## Builds Upon
- biome

## Enables
- Fast editor integration
- Persistent state between operations

## Related
- biome-scanner (scanner results can be cached by the daemon)
- concrete-syntax-tree (parsed trees can be maintained by the daemon)

## Contrasts With
- One-shot CLI execution (starting a fresh process for each command)

# Common Errors
1. Not realizing the daemon may need to be restarted after configuration changes
2. Running multiple daemon instances unintentionally in different project roots

# Common Confusions
1. **Daemon vs. CLI** -- The CLI can operate with or without the daemon. The daemon is primarily important for editor integration where persistent state improves performance.

# Source Reference
- internals/architecture.mdx: "Daemon" section (noted as work in progress)

# Verification Notes
- Medium confidence: The daemon section is marked as "Work in progress" in the source, so the description is brief. The core definition is explicitly stated, but details about implementation are not provided.
