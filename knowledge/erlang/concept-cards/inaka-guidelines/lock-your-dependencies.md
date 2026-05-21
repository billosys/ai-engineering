---
concept: Lock Your Dependencies
slug: lock-your-dependencies
category: tooling
subcategory: tools
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Tools"
chapter_number: null
pdf_page: null
section: "Lock your dependencies"
extraction_confidence: high
aliases:
  - "dependency locking"
  - "pin dependency versions"
  - "no master branch deps"
prerequisites: []
extends: []
related:
  - https-for-dependency-urls
  - avoid-dynamic-calls
contrasts_with: []
answers_questions:
  - "What does \"lock your dependencies\" mean?"
  - "How do I lock a dependency to a fixed version in rebar.config/erlang.mk?"
---

# Quick Definition

In `rebar.config` or `Erlang.mk`, pin each dependency to a specific tag or commit — never to `master`.

# Core Definition

"In your rebar.config or Erlang.mk, specify a tag or commit, but not master" (Inaka, "Lock your dependencies"). Each dependency is referenced by an immutable tag or commit hash so its content cannot change underneath you.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Dependencies are pinned to a tag or commit, not a moving branch.
2. `master` (or any branch) is disallowed as a dependency reference.
3. Pinning protects against sudden, unexpected upstream changes.
4. It is a PR-rejection rule under Tools.

# Construction / Recognition

## To Apply

1. In the build file, reference each dependency by `{tag, "..."}` or a commit hash.
2. Bump the pin deliberately when you actually need a newer version.

## To Recognize a Violation

1. A dependency entry points at `master` or another branch.

# Context & Application

A PR-blocking convention under Tools.

- **Typical contexts**: `rebar.config` `deps`, `erlang.mk` `DEPS`.
- **Common applications**: the source links example `priv/Makefile` and `priv/rebar.config` files.

# Examples

The source illustrates this with linked example build files (`priv/Makefile` for erlang.mk, `priv/rebar.config` for rebar3) rather than inline code.

# Relationships

## Related

- **Prefer the https protocol for dependency URLs** — companion dependency-specification rule.
- **Avoid dynamic calls** — both favor predictable, statically determined behavior.

# Common Errors

- **Error**: Depending on a library's `master` branch.
  **Correction**: Pin to a known-good tag or commit; bump it intentionally.

# Common Confusions

- **Confusion**: Thinking tracking `master` keeps you "up to date."
  **Clarification**: It also makes builds non-reproducible and exposes you to surprise breakage.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Tools", guideline "Lock your dependencies".

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule; examples are linked build files (noted above).
- Uncertainties: None.
- Cross-reference status: all referenced slugs are planned cards in this extraction.
