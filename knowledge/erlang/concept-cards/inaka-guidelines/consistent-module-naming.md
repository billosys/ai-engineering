---
concept: Stick To One Convention For Naming Modules
slug: consistent-module-naming
category: core-idioms
subcategory: naming
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Naming"
chapter_number: null
pdf_page: null
section: "Stick to one convention for naming modules"
extraction_confidence: high
aliases:
  - "module naming convention"
  - "module name prefixes"
prerequisites: []
extends: []
related:
  - function-name-format
  - consistent-concept-naming
contrasts_with: []
answers_questions:
  - "How should I name modules consistently across a project?"
---

# Quick Definition

Pick one module-naming convention for a project and stick to it (e.g., `ik_something` vs `iksomething` vs `something`).

# Core Definition

"Stick to one convention when naming modules (i.e: ik_something vs iksomething vs something)" (Inaka, "Stick to one convention for naming modules"). Whatever prefix/separator scheme a project adopts, every module follows it, giving the system coherence.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A project adopts a single module-naming scheme.
2. Every module name conforms to that scheme (prefix and separators).
3. The benefit is system-wide coherence.
4. It is a PR-rejection rule under Naming.

# Construction / Recognition

## To Apply

1. Decide on a project prefix scheme (e.g., `xmpl_` prefix).
2. Name all modules accordingly.

## To Recognize a Violation

1. Some modules carry the project prefix and others do not.

# Context & Application

A PR-blocking convention under Naming.

- **Typical contexts**: applications with a house module prefix.
- **Common applications**: `xmpl_house`, `xmpl_user` — both prefixed — rather than `house` plus `xmpl_user`.

# Examples

**Example 1** — bad: `house.erl` (unprefixed) alongside `xmpl_user.erl` (prefixed).

**Example 2** — good: `xmpl_house.erl` and `xmpl_user.erl` — both follow the same prefix scheme.

# Relationships

## Related

- **Function Names** — same "one naming convention" discipline at the function level.
- **Be consistent when naming concepts** — consistency principle applied to module names.

# Common Errors

- **Error**: Adding a new module without the project's established prefix.
  **Correction**: Follow the existing scheme so the module set stays coherent.

# Common Confusions

- **Confusion**: Thinking the *choice* of convention matters most.
  **Clarification**: The source's point is consistency — pick one and apply it uniformly.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Naming", guideline "Stick to one convention for naming modules".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule with bad/good example files.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
