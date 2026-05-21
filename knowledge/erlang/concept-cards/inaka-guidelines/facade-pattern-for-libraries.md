---
concept: Use The Facade Pattern On Libraries
slug: facade-pattern-for-libraries
category: api-design
subcategory: suggestions
tier: intermediate
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Suggestions & Great Ideas"
chapter_number: null
pdf_page: null
section: "Use the facade pattern on libraries"
extraction_confidence: high
aliases:
  - "facade pattern"
  - "library facade module"
prerequisites: []
extends: []
related:
  - dont-use-export-all
  - move-code-to-independent-applications
  - encapsulate-otp-apis
contrasts_with: []
answers_questions:
  - "What is the facade pattern for an Erlang library?"
  - "How do I make a library easier to use?"
---

# Quick Definition

Give a library a facade — a single module that exposes its main functions — to simplify usage and serve as self-documentation.

# Core Definition

"The facade pattern is great to simplify library usage and serves as a form of self-documentation" (Inaka, "Use the facade pattern on libraries"). A facade module collects the library's relevant entry-point functions in one place so a user does not have to hunt across modules.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A single facade module gathers the library's main functions.
2. The facade is curated — it exposes the basic-use functions, not every exported function.
3. It both simplifies usage and documents the library's intended use.
4. This is a "Suggestion & Great Idea" — advisory, not a PR-blocking rule.

# Construction / Recognition

## To Apply

1. Decide which functions represent the library's basic, intended use.
2. Re-export or wrap them in one facade module.
3. Resist dumping every exported function into the facade.

## To Recognize a Candidate

1. Library users must call into many internal modules to accomplish common tasks.

# Context & Application

A "Suggestion & Great Idea" — advisory; does not by itself block a PR.

- **Typical contexts**: reusable libraries with several internal modules.
- **Common applications**: the source cites `kafkerl` (`src/kafkerl.erl`) as a facade module.

# Examples

**Example 1** (from source): the `kafkerl` library's `kafkerl.erl` module acts as the facade over the library's internals.

# Relationships

## Related

- **Don't export_all** — both keep the exposed surface deliberate; a facade is curated, not exhaustive.
- **Move stuff to independent applications** — an extracted library is the natural place to add a facade.
- **Encapsulate OTP server APIs** — both present a clean, intentional API.

# Common Errors

- **Error**: Building a facade that re-exports every function in the library.
  **Correction**: Expose only the functions that show the library's basic use.

# Common Confusions

- **Confusion**: Thinking a facade should be comprehensive.
  **Clarification**: A curated, smaller facade lowers the learning curve; an exhaustive one does not.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Suggestions & Great Ideas", guideline "Use the facade pattern on libraries".

# Verification Notes

- Definition source: Direct quote plus paraphrase of the reasoning.
- Confidence rationale: HIGH — explicit suggestion with a real-world example link.
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
