---
# === CORE IDENTIFICATION ===
concept: Biome Assist
slug: biome-assist

# === CLASSIFICATION ===
category: assist
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "assist/index.mdx"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - assist
  - Biome assist tool

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome
extends: []
related:
  - biome-check-command
  - assist-actions
  - suppression-comments
contrasts_with:
  - biome-linter

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is Biome Assist?"
  - "What distinguishes Biome Assist from the Biome Linter?"
---

# Quick Definition
Biome Assist is a tool that offers code actions to improve code quality and developer experience, such as sorting properties, simplifying expressions, and performing refactorings.

# Core Definition
Biome Assist offers a series of actions meant to improve code quality and developer experience. Contrary to linter rules, assist actions always offer a code fix. They might sort properties or fields, simplify binary expressions, perform refactorings, and more. Assist actions are not meant to catch bugs or impose a particular coding style.

# Prerequisites
Requires understanding of Biome as a toolchain. Biome Assist is enabled by default as part of Biome.

# Key Properties
1. Assist actions always offer a code fix (unlike lint rules, which may only report)
2. Actions are not meant to catch bugs or impose coding style
3. Assist code fixes are generally safe to apply; breakage is considered a bug
4. Actions are semantically close to LSP code actions
5. Biome Assist is enabled by default, with some rules in the recommended set
6. Actions are organized into groups (e.g., Source)

# Construction / Recognition
To configure Biome Assist, use the `assist` key in `biome.json`:
```json
{
  "assist": {
    "enabled": true,
    "actions": {
      "source": {
        "useSortedKeys": "on"
      }
    }
  }
}
```

Assist works best in editors/IDEs but can be enforced via the CLI `check` command. To run only assist actions: `biome check --formatter-enabled=false --linter-enabled=false`. To disable enforcement: `biome check --enforce-assist=false`.

# Context & Application
Assist is most useful in editor/IDE workflows where actions can be applied on save via code actions (e.g., `source.fixAll.biome`). It is also enforceable through the CLI for CI pipelines.

# Examples
From `assist/index.mdx`: The `useSortedKeys` action sorts keys in objects. Its code action name is `source.action.useSortedKeys.biome`, which can be configured in VS Code's `editor.codeActionsOnSave`.

The Source group contains actions that can be safely applied upon saving a document and typically don't change program functionality.

# Relationships
## Builds Upon
- biome (the Biome toolchain)

## Enables
- assist-actions (individual actions within the assist tool)

## Related
- biome-check-command (CLI integration)
- suppression-comments (suppressing assist actions)

## Contrasts With
- biome-linter: Linter rules catch bugs and enforce coding style, and may not offer a fix. Assist actions always offer a fix and are not for bugs or style enforcement.

# Common Errors
1. Running `biome check` without disabling formatter/linter when only assist is desired
2. Forgetting that `--enforce-assist=false` is needed to avoid errors when assist actions haven't been applied

# Common Confusions
1. Confusing assist actions with lint rules — assist always provides a fix and is not about bug detection or style
2. Assuming assist is disabled by default — it is enabled by default

# Source Reference
- `sources-md/biome/assist/index.mdx`

# Verification Notes
Extracted directly from the Assist overview page. All properties and distinctions are explicitly stated in the source.
