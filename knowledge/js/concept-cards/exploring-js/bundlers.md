---
concept: Bundlers
slug: bundlers
category: web-development
subcategory: tooling
tier: foundational
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Next steps: overview of web development"
chapter_number: 49
pdf_page: null
section: "49.3.1.3 Bundlers"
extraction_confidence: high
aliases:
  - module bundlers
  - JS bundlers
prerequisites: []
extends: []
related:
  - javascript-tools-overview
  - tree-shaking
  - transpilers
contrasts_with: []
answers_questions:
  - "What JavaScript-related tools should I know about?"
---

# Quick Definition

Bundlers compile and optimize a JavaScript app's many source files and library dependencies into fewer output files for deployment, using techniques like tree-shaking to minimize size.

# Core Definition

"Exploring JavaScript" Ch. 49: "Bundlers compile and optimize the code of a JavaScript app. The input of a bundler is many files -- all of the app's code plus the libraries it uses. A bundler combines these input files to produce fewer output files (which tends to improve performance)." Bundlers minimize output via tree-shaking: "only those module exports are put in the output that are imported somewhere."

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. Combine many files into fewer output files
2. Tree-shaking: dead code elimination based on import analysis
3. Often handle transpilation and minification as well
4. Popular bundlers: Vite (framework-like), esbuild, Rollup, Rolldown, Parcel, Rspack, TurboPack, webpack

# Construction / Recognition

Bundlers are configured via configuration files and CLI tools, not demonstrated inline.

# Context & Application

Essential for deploying modern JavaScript applications. Fewer files improve loading performance.

# Examples

From the source, popular bundlers are categorized:
- More like a framework: Vite
- More like a library: esbuild, Rollup, Rolldown
- Somewhere between: Parcel, Rspack, TurboPack, webpack

(Ch. 49, Section 49.3.1.3, lines 301-331)

# Relationships

## Related
- **Tree-shaking** -- key optimization technique
- **Transpilers** -- bundlers often incorporate transpilation

# Common Errors

- **Error**: Not configuring tree-shaking, resulting in oversized bundles
  **Correction**: Ensure exports are properly structured for tree-shaking (use ES modules)

# Common Confusions

- **Confusion**: Bundlers are only for production
  **Clarification**: Many bundlers (like Vite) also serve development builds with hot module replacement

# Source Reference

Chapter 49: Next steps: overview of web development, Section 49.3.1.3, lines 301-331.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit definition with tool list
- Cross-reference status: verified
