---
# === CORE IDENTIFICATION ===
concept: Rust Compiler Development Guide Overview
slug: compiler-guide-overview

# === CLASSIFICATION ===
category: compiler-development
subcategory: overview
tier: foundational

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Getting Started, About This Guide"
chapter_number: 0
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rustc dev guide"
  - "compiler contribution guide"
  - "rustc contributor onboarding"
  - "t-compiler getting started"
  - "contributing to the Rust compiler"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - building-rustc
  - compiler-testing
  - compiler-debugging
  - contributing-to-rustc
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rustc dev guide and what does it cover?"
  - "How is the Rust compiler documentation organized?"
  - "Where do I ask questions about contributing to rustc?"
  - "What are good starting points for contributing to the Rust compiler?"
  - "How do I find experts on specific parts of the compiler?"
  - "What resources exist beyond the rustc dev guide itself?"
  - "What types of contributions are available beyond code changes?"
---

# Quick Definition

The Rust Compiler Dev Guide documents how rustc (the Rust compiler) works and how to contribute to its development. It is organized into sections covering building and debugging, contribution procedures, bootstrapping, high-level architecture, source code representation, supporting infrastructure, analysis, and code generation. The guide is open source and explicitly invites questions, emphasizing that "nobody on `t-compiler` feels this way" about wasting experts' time.

# Core Definition

The guide serves two primary purposes: documenting how the Rust compiler works internally, and helping new contributors get involved. It is "meant to be a quick guide for the most useful things" rather than comprehensive documentation.

The guide is organized into nine major parts:

1. **Building and debugging rustc** -- how to build, debug, and profile the compiler
2. **Contributing to Rust** -- procedures for contribution, Git/GitHub workflows, feature stabilization
3. **Bootstrapping** -- how the compiler builds itself using previous versions
4. **High-level Compiler Architecture** -- stages of the compile process
5. **Source Code Representation** -- transforming source code into compiler-internal forms
6. **Supporting Infrastructure** -- CLI conventions, entry points, errors, and lints
7. **Analysis** -- type checking and other properties verification
8. **MIR to Binaries** -- generating linked machine code
9. **Appendices** -- reference material including a glossary

The guide acknowledges the constant-change nature of the codebase: "rustc is a real production-quality product, being worked upon continuously by a sizeable set of contributors. As such, it has its fair share of codebase churn and technical debt."

# Prerequisites

No compiler-specific prerequisites. General programming experience is assumed. The guide welcomes contributors at all levels and suggests starting with Clippy or diagnostic issues for newcomers.

# Key Properties

1. **t-compiler Zulip is the primary communication channel**: The compiler team communicates via the `#t-compiler` channel on Zulip, with `#t-compiler/help` for questions about how the compiler works
2. **Finding experts via triagebot**: The `triagebot.toml` file in the Rust repo contains `[assign*]` sections mapping compiler areas to people with expertise
3. **Finding experts via git history**: Running `git shortlog -n <release-tag>.. compiler/<crate>/` reveals recent contributors to specific compiler components
4. **Multiple entry points for contributors**: Issues labeled `E-easy`, `E-medium`, `E-help-wanted`, and `E-mentor` are starting places; Clippy and diagnostic issues are especially newcomer-friendly
5. **Abandoned PRs can be picked up**: PRs with the `S-inactive` label represent work that can be continued by new contributors
6. **Writing tests is a low-barrier entry**: Issues labeled `E-needs-test` need regression tests, offering a way to learn the testing infrastructure
7. **The guide itself is open source**: Hosted on GitHub, contributions to the guide are welcome and follow the same PR process

# Construction / Recognition

## Getting Started as a Contributor:

1. Ask questions on Zulip (`#t-compiler/help`) -- questions are explicitly encouraged
2. Find work via [issue search](https://github.com/rust-lang/rust/issues) with labels like `E-easy` or `E-mentor`
3. Consider starting with Clippy contributions to learn the process and compiler internals
4. Look at diagnostic issues for self-contained work that does not require deep compiler knowledge
5. Browse abandoned PRs (`S-inactive` label) for work that can be continued
6. Write regression tests for issues labeled `E-needs-test`

## Other Contribution Paths:

- Writing documentation (doc comments for compiler code)
- Triaging issues (categorizing, replicating, minimizing)
- Answering questions on users.rust-lang.org or Stack Overflow
- Participating in the RFC process
- Building community libraries requested in RFCs

# Context & Application

- **New compiler contributors**: The guide is the primary onboarding resource for anyone wanting to work on rustc itself
- **Existing contributors**: Reference material for understanding unfamiliar parts of the compiler
- **Tool developers**: Contributors to cargo, miri, rustup, and other Rust project tools
- **Standard library developers**: The guide points to the separate [std-dev-guide](https://std-dev-guide.rust-lang.org/) for library contributions

# Examples

**Example 1**: Finding experts on name resolution since a specific release:
```console
$ git shortlog -n 1.68.2.. compiler/rustc_resolve/
```
Ignore "Rollup merge" commits and commits by `@bors`.

**Example 2**: Communication etiquette -- the guide recommends including context when pinging someone, and preferring public topics so others can benefit from the questions and answers.

**Example 3**: The guide lists key complementary resources:
- [rustc API docs](https://doc.rust-lang.org/nightly/nightly-rustc/rustc_middle) -- rustdoc for compiler internals
- [Forge](https://forge.rust-lang.org/) -- infrastructure docs and team procedures
- [compiler-team repo](https://github.com/rust-lang/compiler-team) -- team procedures and working groups
- Google with `site:doc.rust-lang.org` for cross-documentation search

# Relationships

## Builds Upon
- None -- this is the entry point for compiler development

## Enables
- **building-rustc** -- how to actually clone and build the compiler
- **compiler-testing** -- the test infrastructure described in the guide
- **compiler-debugging** -- debugging and profiling techniques
- **contributing-to-rustc** -- the formal contribution procedures

## Related
- **rust-book-overview** -- the user-facing Rust introduction (vs. this developer-facing guide)

## Contrasts With
- None within this source

# Common Errors

- **Error**: Hesitating to ask questions, feeling like you are wasting experts' time.
  **Correction**: The guide explicitly states "nobody on `t-compiler` feels this way. Contributors are important to us."

- **Error**: Searching only labeled issues for contribution opportunities.
  **Correction**: "Not all important or beginner work has issue labels." Tracking issues, recurring work, and abandoned PRs are additional sources of work.

- **Error**: Using LLM tools to write formal-sounding messages when communicating with the team.
  **Correction**: The guide advises: "Avoid using LLM tools that generate long, complex words. In daily teamwork, simple and clear words are best for easy understanding."

# Common Confusions

- **Confusion**: The rustc dev guide is comprehensive documentation of the compiler.
  **Clarification**: The guide is explicitly "not intended to be comprehensive; it is meant to be a quick guide for the most useful things." Many idealized designs described in the guide are "not fully realized yet."

- **Confusion**: You need deep compiler knowledge to contribute.
  **Clarification**: Diagnostic issues, test writing, documentation, and issue triaging all require minimal background knowledge. Clippy has specifically invested in making its contribution process newcomer-friendly.

- **Confusion**: Contributing to Rust means contributing to the `rust-lang/rust` repo.
  **Clarification**: There are many other projects (cargo, miri, rustup, etc.) with their own contribution processes. The standard library also has a separate dev guide.

# Source Reference

Chapter 0: Getting Started (211 lines) and About This Guide (118 lines), totaling 328 lines. Covers the guide's purpose, communication channels, finding experts, entry points for contributors, and other resources. The content is developer-facing, targeted at people wanting to contribute to the Rust compiler itself.

# Verification Notes

- Definition source: Direct content from the Getting Started and About This Guide sections
- Key Properties: All items supported by source text
- Confidence rationale: HIGH -- canonical onboarding material with explicit, clear guidance
- Uncertainties: None for this overview material
- Cross-reference status: Related slugs reference other cards in this compiler-guide extraction set
