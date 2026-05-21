---
concept: Group Modules In Subdirectories By Functionality
slug: group-modules-in-subdirectories
category: core-idioms
subcategory: source-code-layout
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Source Code Layout"
chapter_number: null
pdf_page: null
section: "Group modules in subdirectories by functionality"
extraction_confidence: high
aliases:
  - "module subdirectories"
  - "package directories"
prerequisites: []
extends: []
related:
  - no-god-modules
  - move-code-to-independent-applications
contrasts_with: []
answers_questions:
  - "How should I organize modules when a project has many of them?"
---

# Quick Definition

When a project has many modules, group them into subdirectories named for what each "package" does.

# Core Definition

"When having lots of modules, use subdirectories for them, named with a nice descriptive name for what that 'package' does" (Inaka, "Group modules in subdirectories by functionality"). Directory structure reflects functional grouping so related modules live together.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Subdirectories group modules by functional area.
2. Each subdirectory's name describes the package's purpose.
3. It is a PR-rejection rule under Source Code Layout.
4. If using an `Emakefile`, it must be configured to handle the subdirectory layout.

# Construction / Recognition

## To Apply

1. Identify functional clusters among your modules.
2. Create a descriptively named subdirectory per cluster and move the modules into it.
3. Update `Emakefile`/build configuration to compile the subdirectories.

## To Recognize a Violation

1. Dozens of modules sit flat in a single `src/` directory with no grouping.

# Context & Application

A PR-blocking convention under Source Code Layout.

- **Typical contexts**: large applications with many modules.
- **Common applications**: `src/<feature>/` subdirectories.

# Examples

The source provides no code example for this guideline; it gives a build-configuration note instead: remember to configure your `Emakefile` to handle subdirectories if you use one.

# Relationships

## Related

- **No God modules** — both keep a codebase navigable as it grows.
- **Move stuff to independent applications** — the next step up when a cluster becomes truly independent.

# Common Errors

- **Error**: Adding subdirectories but forgetting to update the build files.
  **Correction**: Update `Emakefile`/`rebar.config` so the new paths are compiled.

# Common Confusions

- **Confusion**: Expecting a code example.
  **Clarification**: This guideline is about directory layout; the source intentionally gives only a build-config note.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Source Code Layout", guideline "Group modules in subdirectories by functionality".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule; no code example exists in the source (noted above).
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
