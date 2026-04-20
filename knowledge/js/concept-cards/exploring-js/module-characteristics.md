---
concept: Module Characteristics
slug: module-characteristics
category: modules
subcategory: null
tier: intermediate
source: "Exploring JavaScript"
source_slug: exploring-js
authors: "Dr. Axel Rauschmayer"
chapter: "Modules"
chapter_number: 29
pdf_page: null
section: "29.4.3 Characteristics of JavaScript modules"
extraction_confidence: high
aliases:
  - "module properties"
prerequisites:
  - ecmascript-module
extends: []
related:
  - scripts-vs-modules
contrasts_with: []
answers_questions:
  - "What concepts underpin the module system?"
---

# Quick Definition

JavaScript modules share core characteristics: one module per file, local scope, explicit exports/imports, singleton behavior, and no global variables.

# Core Definition

As described in "Exploring JavaScript" Ch. 29, looking at CommonJS and AMD, JavaScript module systems share these characteristics: one module per file, executed in local "module scope" (not global), entities are private by default, exports must be explicitly marked, imports identify other modules via specifiers, modules are singletons (imported only once), and no global variables are used.

# Prerequisites

- ECMAScript module

# Key Properties

1. One module per file.
2. Local scope (not global).
3. Private by default; explicit exports.
4. Singletons: only one instance regardless of import count.
5. No global variables; module specifiers serve as identifiers.
6. Code executed once on first import.

# Construction / Recognition

These characteristics apply to all JavaScript module systems (CommonJS, AMD, ESM).

# Context & Application

Understanding these shared characteristics helps appreciate the design of ESM and work across different module systems.

# Examples

From the source text (Ch. 29, section 29.4.3):

The singleton property:
```
// Even if imported by modules A, B, and C,
// the module code only runs once.
```

# Relationships

## Related
- **Scripts vs Modules** -- scripts lack these properties

# Source Reference

Chapter 29: Modules, Section 29.4.3, lines 648-666.

# Verification Notes

- Definition source: synthesized
- Confidence rationale: Synthesized from explicit characteristic list
- Cross-reference status: verified
