---
# === CORE IDENTIFICATION ===
concept: cobalt debug
slug: cobalt-debug

# === CLASSIFICATION ===
category: cli
subcategory: commands
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Troubleshooting"
chapter_number: null
pdf_page: null
section: "Useful commands"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "debug command"
  - "troubleshooting commands"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cobalt-init
  - installation
extends: []
related:
  - cobalt-build
  - cobalt-configuration-file
  - syntax-highlighting
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use cobalt debug?"
---

# Quick Definition

`cobalt debug` provides a set of subcommands (`config`, `files`, `highlight`) for inspecting site configuration, file collections, and syntax highlighting settings to aid in troubleshooting.

# Core Definition

The `cobalt debug` command "Displays site debug information" through several subcommands: `config`, `files`, and `highlight` (source: Usage doc page, "debug" section). The Troubleshooting doc page provides detailed usage: `cobalt debug config` shows the configuration after processing defaults; `cobalt debug files <collection>` lists files for a given collection (pages, posts, assets) with optional `--draft` and `--trace` flags; and `cobalt debug highlight` shows available themes and language syntaxes (source: Troubleshooting doc page, "Useful commands" section). The `--trace` flag is especially useful for understanding ignore patterns and why files are excluded.

# Prerequisites

- **Installation** -- Cobalt must be installed
- **cobalt init** -- a Cobalt site must exist to inspect

# Key Properties

1. **`cobalt debug config`** -- "Show config after processing defaults, etc" (source: Troubleshooting doc page).
2. **`cobalt debug files <collection>`** -- shows all files for a given collection: `pages`, `posts`, or `assets` (source: Troubleshooting doc page).
3. **`--draft` flag** -- `cobalt debug files posts --draft` includes draft posts in the listing (source: Troubleshooting doc page).
4. **`--trace` flag** -- provides detailed information about ignore patterns and why files or directories were ignored (source: Troubleshooting doc page).
5. **`cobalt debug highlight themes`** -- lists supported code highlight themes (source: Troubleshooting doc page).
6. **`cobalt debug highlight syntaxes`** -- lists supported code highlight language syntaxes (source: Troubleshooting doc page).
7. **Verbose flags on all commands** -- all cobalt commands support `--verbose` (or `-vv` for maximum verbosity) for additional context (source: Troubleshooting doc page).

# Construction / Recognition

## To Construct/Create:
1. Run `cobalt debug config` to inspect the resolved configuration.
2. Run `cobalt debug files pages` to see all page files.
3. Run `cobalt debug files posts --draft` to see all posts including drafts.
4. Run `cobalt debug files assets --trace` to see assets with ignore pattern details.
5. Run `cobalt debug highlight themes` to list available syntax highlighting themes.
6. Run `cobalt debug highlight syntaxes` to list supported language syntaxes.

## To Identify/Recognize:
1. Debug output provides internal state information not visible during normal build/serve operations.
2. Trace output explains file inclusion/exclusion decisions.

# Context & Application

- **Typical contexts**: Troubleshooting build issues, understanding why files are missing from output, verifying configuration, checking available syntax highlighting options.
- **Common applications**: Diagnosing missing pages or posts, verifying ignore patterns, selecting syntax highlighting themes, understanding the effective configuration after defaults are applied.

# Examples

**Example 1** (source: Troubleshooting doc page): Show resolved configuration:
```console
$ cobalt debug config
```

**Example 2** (source: Troubleshooting doc page): Show all page files:
```console
$ cobalt debug files pages
```

**Example 3** (source: Troubleshooting doc page): Show all posts including drafts:
```console
$ cobalt debug files posts --draft
```

**Example 4** (source: Troubleshooting doc page): Show assets with trace information:
```console
$ cobalt debug files assets --trace
```
`--trace` is useful to know: "What the final `ignore` pattern is", "Why files or directories where ignored", etc. (source: Troubleshooting doc page).

**Example 5** (source: Troubleshooting doc page): List syntax highlighting themes and syntaxes:
```console
$ cobalt debug highlight themes
$ cobalt debug highlight syntaxes
```

**Example 6** (source: Troubleshooting doc page): Using verbose flags for additional detail:
```console
$ cobalt build --verbose        # Show some additional context
$ cobalt build -vv              # Show everything
```

# Relationships

## Builds Upon
- **cobalt init** -- a site must exist to debug
- **cobalt-configuration-file** -- `debug config` inspects the resolved configuration

## Enables
- Troubleshooting of build and serve issues
- Understanding of effective configuration

## Related
- **cobalt-build** -- debug helps troubleshoot build issues
- **syntax-highlighting** -- `debug highlight` inspects syntax highlighting configuration

## Contrasts With
- No direct contrasts within scope.

# Common Errors

- **Error**: Not understanding why a file is excluded from the build.
  **Correction**: Use `cobalt debug files <collection> --trace` to see the ignore patterns and reasons for file exclusion.

# Common Confusions

- **Confusion**: `cobalt debug` is a single command without subcommands.
  **Clarification**: `cobalt debug` has multiple subcommands: `config`, `files`, and `highlight`. Each serves a different diagnostic purpose. `cobalt debug` alone may not produce useful output; a subcommand is needed.

# Source Reference

Usage doc page, "debug" section; Troubleshooting doc page, "Useful commands" section. Source: Cobalt documentation.

# Verification Notes

- Definition source: Direct from Usage doc page ("debug" section) and Troubleshooting doc page
- Confidence rationale: High -- all subcommands and flags are documented with explicit examples
- Uncertainties: The complete list of debug subcommands may not be exhaustive in the documentation; only `config`, `files`, and `highlight` are documented
- Cross-reference status: References to cobalt-init, cobalt-build, cobalt-configuration-file, syntax-highlighting verified against planned card slugs
