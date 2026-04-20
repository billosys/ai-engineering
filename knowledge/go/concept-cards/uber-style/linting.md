---
concept: Linting
slug: linting
category: tooling
subcategory: static-analysis
tier: foundational
source: "Uber Go Style Guide"
source_slug: uber-style
authors: "Prashant Varanasi, Simon Newton"
chapter: "Linting"
chapter_number: 6
pdf_page: null
section: "Linting"
extraction_confidence: high
aliases:
  - Go linters
  - golangci-lint
  - lint runner
prerequisites: []
extends: []
related:
  - format-strings-outside-printf
  - naming-printf-style-functions
contrasts_with: []
answers_questions:
  - "What linters does the Uber Go Style Guide recommend?"
  - "What lint runner should I use for Go?"
---

# Quick Definition

The Uber Go Style Guide recommends a minimum set of linters -- errcheck, goimports, revive, govet, and staticcheck -- and recommends golangci-lint as the lint runner for Go projects. Consistent linting across a codebase is more important than any specific linter choice.

# Core Definition

The Uber Go Style Guide emphasizes that consistent linting across a codebase matters more than any particular "blessed" set of linters. The guide recommends the following minimum set of linters:

- **errcheck**: Ensures that errors are handled.
- **goimports**: Formats code and manages imports.
- **revive**: Points out common style mistakes (modern successor to the deprecated golint).
- **govet**: Analyzes code for common mistakes.
- **staticcheck**: Performs various static analysis checks.

For running these linters, the guide recommends **golangci-lint** due to its performance in larger codebases and its ability to configure and run many linters simultaneously. Teams are encouraged to add additional linters that make sense for their projects beyond this base set.

# Prerequisites

- Basic Go development environment setup
- Understanding of static analysis concepts

# Key Properties

1. **Consistency over perfection**: Lint consistently across the codebase; the specific set of linters matters less than uniform application.
2. **Minimum recommended set**: errcheck, goimports, revive, govet, staticcheck.
3. **revive replaces golint**: revive is the modern, faster successor to the now-deprecated golint.
4. **golangci-lint as runner**: Recommended for performance and multi-linter configuration.
5. **Extensible**: Teams should add project-specific linters beyond the base set.
6. **Configuration file**: The Uber guide repo provides an example `.golangci.yml` configuration file.

# Construction / Recognition

**Example golangci-lint configuration (conceptual):**

A `.golangci.yml` file at the project root configures which linters to enable and their settings. The Uber Go Style Guide repository provides a reference configuration.

**Running linters:**

```shell
golangci-lint run
```

# Context & Application

Linting should be integrated into the development workflow -- ideally as part of CI/CD pipelines and pre-commit hooks. The recommended linters catch a broad range of issues: unhandled errors (errcheck), import formatting (goimports), style violations (revive), common bugs (govet), and deeper static analysis (staticcheck).

# Examples

**Minimum linter set:**

| Linter | Purpose |
|---|---|
| errcheck | Ensure errors are handled |
| goimports | Format code and manage imports |
| revive | Catch common style mistakes |
| govet | Analyze code for common mistakes |
| staticcheck | Various static analysis checks |

# Relationships

- **format-strings-outside-printf**: govet's Printf family check is one of the static analysis benefits enabled by proper linting setup.
- **naming-printf-style-functions**: govet's `-printfuncs` flag extends Printf checking to custom functions.

# Common Errors

1. Not running linters consistently -- some files or packages are linted while others are not.
2. Using golint instead of revive -- golint is deprecated.
3. Not configuring errcheck -- unhandled errors are a common source of bugs in Go.

# Common Confusions

- **golint vs revive**: golint is deprecated. revive is its modern, faster replacement with more features.
- **golangci-lint vs individual linters**: golangci-lint is a runner that orchestrates multiple linters, not a linter itself. It provides unified configuration and output.

# Source Reference

Uber Go Style Guide, "Linting" chapter, including "Lint Runners" sub-section.

# Verification Notes

Confidence: high. The recommended linters, runner, and rationale are directly stated in the source text.
