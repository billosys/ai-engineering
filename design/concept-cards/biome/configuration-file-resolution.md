---
# === CORE IDENTIFICATION ===
concept: Configuration File Resolution
slug: configuration-file-resolution

# === CLASSIFICATION ===
category: configuration
subcategory: file discovery
tier: foundational

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "guides/configure-biome.mdx"
chapter_number: null
pdf_page: null
section: "Configuration file resolution"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "config resolution"
  - "config discovery"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-configuration
extends: []
related:
  - monorepo-support
  - biome-cli
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I install and set up Biome?"
  - "How does biome.json configuration relate to CLI options?"
---

# Quick Definition
The algorithm Biome uses to locate its configuration file, searching the current working directory, then parent directories, and finally the user's home directory.

# Core Definition
Biome discovers its configuration by searching for files in a specific priority order (`biome.json`, `biome.jsonc`, `.biome.json`, `.biome.jsonc`) across three location tiers: (1) the current working directory (CLI execution directory or editor project root), (2) parent directories traversed recursively upward, and (3) the OS-specific home configuration directory. If no file is found, Biome uses its built-in defaults.

# Prerequisites
- biome-configuration: Must understand what the configuration file contains.

# Key Properties
1. File name priority: `biome.json` > `biome.jsonc` > `.biome.json` > `.biome.jsonc`.
2. Location search order: CWD, then parent folders (recursive), then home directory.
3. Home directory paths are OS-specific: `$XDG_CONFIG_HOME` or `~/.config/biome` on Linux, `~/Library/Application Support/biome` on macOS, `AppData\Roaming\biome\config` on Windows.
4. The "current working directory" differs by context: CLI uses the shell's CWD; editors use the project root.
5. Falls back to default configuration if no file is found anywhere.
6. Supports nested configuration files for monorepo use.

# Construction / Recognition
To control which configuration Biome uses:
- Place `biome.json` in the project root for standard projects.
- Use nested `biome.json` files in subdirectories for monorepo setups.
- Use `--config-path` CLI flag to override automatic resolution.
- Place a configuration in the home directory for user-wide defaults.

# Context & Application
Resolution order matters in monorepos where multiple `biome.json` files exist at different directory levels. A command run from a subdirectory will find the nearest configuration file, not necessarily the root one.

# Examples
From the source, given this directory structure:

```
app/
  backend/
    biome.json
    package.json
  frontend/
    legacy/
      package.json
    new/
      package.json
    biome.json
```

- Commands in `app/backend/` use `app/backend/biome.json`.
- Commands in `app/frontend/legacy/` or `app/frontend/new/` use `app/frontend/biome.json`.

(From guides/configure-biome.mdx, "Configuration file resolution" section)

# Relationships
## Builds Upon
- biome-configuration
## Enables
- monorepo-support (nested configs leverage resolution order)
## Related
- biome-cli (CWD affects resolution)
## Contrasts With
None.

# Common Errors
1. Running Biome from an unexpected directory and picking up the wrong configuration file.
2. Forgetting that a home-directory config applies when no project-level config exists.

# Common Confusions
1. Assuming the editor and CLI always use the same working directory -- they may differ.
2. Not realizing that parent directory traversal means a config file several levels up can apply to deeply nested files.

# Source Reference
- guides/configure-biome.mdx, "Configuration file resolution" section

# Verification Notes
Directly and explicitly documented in the source with enumerated search order. High confidence.
