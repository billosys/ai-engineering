---
concept: Prefer The https Protocol For Dependency URLs
slug: https-for-dependency-urls
category: tooling
subcategory: tools
tier: foundational
source: "Erlang Coding Standards & Guidelines"
source_slug: inaka-guidelines
authors: Inaka
chapter: "Tools"
chapter_number: null
pdf_page: null
section: "Prefer the https protocol when specifying dependency locations"
extraction_confidence: high
aliases:
  - "https dependency URLs"
  - "https over git protocol"
prerequisites: []
extends: []
related:
  - lock-your-dependencies
contrasts_with: []
answers_questions:
  - "Which protocol should I use for dependency repository URLs?"
---

# Quick Definition

When specifying dependencies in `erlang.mk` Makefiles or `rebar.config`, prefer the `https` protocol for the dependency repository URL.

# Core Definition

"When specifying dependencies in erlang.mk Makefiles or rebar.config, prefer using the https protocol to download the dependency repository" (Inaka, "Prefer the https protocol when specifying dependency locations"). Repository URLs use `https://` rather than the git or ssh protocols.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Dependency repository URLs use the `https` protocol.
2. It applies to both `erlang.mk` Makefiles and `rebar.config`.
3. HTTPS is GitHub's recommended protocol and is easier for CI.
4. It is a PR-rejection rule under Tools.

# Construction / Recognition

## To Apply

1. Write dependency URLs as `https://github.com/owner/repo.git`.

## To Recognize a Violation

1. A dependency URL uses `git://` or an `ssh`/SCP-style `git@` form.

# Context & Application

A PR-blocking convention under Tools.

- **Typical contexts**: `deps` in `rebar.config`, `DEPS` URLs in `erlang.mk`.
- **Common applications**: the source links example `dep_protocol.makefile` and `dep_protocol.config` files.

# Examples

The source illustrates this with linked example files (`src/dependency_protocol/dep_protocol.makefile` and `dep_protocol.config`) rather than inline code.

# Relationships

## Related

- **Lock your dependencies** — companion rule on how dependencies are specified.

# Common Errors

- **Error**: Using a `git://` or `git@github.com:` URL for a dependency.
  **Correction**: Use the `https://` URL form.

# Common Confusions

- **Confusion**: Thinking the protocol is purely a matter of taste.
  **Clarification**: HTTPS is GitHub's official recommendation and avoids CI key-management friction.

# Source Reference

"Erlang Coding Standards & Guidelines" — Inaka. Section "Tools", guideline "Prefer the https protocol when specifying dependency locations". Links GitHub's protocol-comparison guidance.

# Verification Notes

- Definition source: Direct quote from the guideline.
- Confidence rationale: HIGH — explicit rule; examples are linked files (noted above).
- Uncertainties: None.
- Cross-reference status: `lock-your-dependencies` is a planned card in this extraction.
