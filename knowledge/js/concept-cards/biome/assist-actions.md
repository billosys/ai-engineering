---
# === CORE IDENTIFICATION ===
concept: Assist Actions
slug: assist-actions

# === CLASSIFICATION ===
category: assist
subcategory: code actions
tier: intermediate

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "assist/index.mdx"
chapter_number: null
pdf_page: null
section: "Groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - assist code actions
  - source actions

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-assist
extends:
  - biome-assist
related:
  - biome-check-command
  - suppression-comments
contrasts_with:
  - biome-linter

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes Biome Assist from the Biome Linter?"
  - "What is Biome Assist?"
---

# Quick Definition
Assist actions are individual code transformations within Biome Assist that always provide a fix, organized into groups such as Source, and executable via IDE code actions or CLI.

# Core Definition
Assist actions are the individual operations offered by Biome Assist. Each action always offers a code fix — unlike lint rules, which may only report a diagnostic. Actions are semantically close to LSP code actions and are divided into groups. The Source group represents actions that can be safely applied upon saving and typically don't change program functionality.

# Prerequisites
- biome-assist (understanding what the Assist tool is)

# Key Properties
1. Every assist action provides a code fix (never report-only)
2. Actions are organized into groups (currently: Source)
3. Each action has a code action identifier (e.g., `source.action.useSortedKeys.biome`)
4. Source group actions are safe to apply on save and don't change program functionality
5. Actions can be individually enabled/disabled in `biome.json`
6. Actions can be suppressed using suppression comments

# Construction / Recognition
To enable a specific action in `biome.json`:
```json
{
  "assist": {
    "actions": {
      "source": {
        "useSortedKeys": "on"
      }
    }
  }
}
```

To configure IDE on-save behavior, add the action's code action identifier to editor settings. For VS Code, use `editor.codeActionsOnSave` with values like `source.action.useSortedKeys.biome`.

# Context & Application
Assist actions are used when you want automated code improvements that go beyond formatting but aren't about catching bugs. They are ideal for enforcing structural consistency (e.g., sorted keys) across a codebase.

# Examples
From `assist/index.mdx`: The `useSortedKeys` action sorts object keys. Its code action is `source.action.useSortedKeys.biome`. The general fix-all code action is `source.fixAll.biome`.

Most action names follow a consistent pattern, but some exceptions exist (e.g., `organizeImports`), so consult individual action documentation.

# Relationships
## Builds Upon
- biome-assist (the Assist tool that contains these actions)

## Enables
- Consistent code structure through automated transformations

## Related
- biome-check-command (CLI enforcement of actions)
- suppression-comments (disabling actions for specific code)

## Contrasts With
- biome-linter: Lint rules detect bugs and enforce style; they may not have a fix. Assist actions always have a fix and focus on code quality improvements.

# Common Errors
1. Not consulting individual action documentation for the correct code action identifier
2. Assuming all actions follow the same naming pattern (some like `organizeImports` differ)

# Common Confusions
1. Thinking assist actions and lint rules serve the same purpose — they are complementary but distinct
2. Assuming Source group actions might break code — they are designed to be safe

# Source Reference
- `sources-md/biome/assist/index.mdx`, sections "Use assist actions in your IDE", "Groups"

# Verification Notes
Extracted from the Assist overview. The distinction between assist actions and lint rules is explicitly stated.
