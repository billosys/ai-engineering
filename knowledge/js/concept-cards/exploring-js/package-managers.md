---
concept: Package Managers
slug: package-managers
category: web-development
subcategory: tooling
tier: foundational
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Next steps: overview of web development"
chapter_number: 49
pdf_page: null
section: "49.3.4 Package managers"
extraction_confidence: high
aliases:
  - npm
  - dependency management
prerequisites: []
extends: []
related:
  - javascript-tools-overview
contrasts_with: []
answers_questions:
  - "What JavaScript-related tools should I know about?"
---

# Quick Definition

Package managers install and manage JavaScript library dependencies. npm is the most popular, with alternatives Yarn and pnpm using the same registry. JSR (JavaScript Registry) is a newer registry focused on TypeScript.

# Core Definition

"Exploring JavaScript" Ch. 49: "The most popular package manager for JavaScript is npm. It started as a package manager for Node.js but has since also become dominant for client-side web development and tools of any kind." Alternatives: Yarn (different approach, npm-compatible), pnpm (space-saving), and JSR (JavaScript Registry, TypeScript-focused, Deno-native).

# Prerequisites

Foundational concept with no prerequisites.

# Key Properties

1. npm: most popular, dominant for both server and client-side
2. Yarn: alternative with features npm later adopted
3. pnpm: focused on saving disk space
4. JSR: newer registry, TypeScript-focused, Deno-native, works with all managers
5. Yarn and pnpm use npm's package registry

# Construction / Recognition

Package management via CLI: `npm install`, `yarn add`, `pnpm add`, etc.

# Context & Application

Package managers are essential for managing dependencies in any JavaScript project.

# Examples

From the source: npm is used for "client-side web development and tools of any kind."

(Ch. 49, Section 49.3.4, lines 377-397)

# Relationships

## Related
- **JavaScript tools overview** -- package managers are one tool category

# Common Errors

- **Error**: Committing `node_modules` to version control
  **Correction**: Add `node_modules` to `.gitignore`; use lock files for reproducibility

# Common Confusions

- **Confusion**: npm is only for Node.js server-side code
  **Clarification**: npm is the standard for all JavaScript packages including frontend libraries and tools

# Source Reference

Chapter 49: Next steps: overview of web development, Section 49.3.4, lines 377-397.

# Verification Notes

- Definition source: direct from source text
- Confidence rationale: explicit section with alternatives
- Cross-reference status: verified
