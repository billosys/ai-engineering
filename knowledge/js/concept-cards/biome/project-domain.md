---
# === CORE IDENTIFICATION ===
concept: Project Domain
slug: project-domain

# === CLASSIFICATION ===
category: linter-domains
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "linter/domains.mdx"
chapter_number: null
pdf_page: null
section: "Project"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "project-level analysis"
  - "module graph rules"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linter-domains
  - biome-linter
extends:
  - linter-domains
related:
  - types-domain
  - nursery-rules
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the project domain?"
  - "How does the Scanner relate to project-domain rules?"
  - "Why is the Biome linter slower with project-domain rules?"
---

# Quick Definition
The project domain contains lint rules that perform project-level analysis using Biome's module graph for dependency resolution, requiring the Scanner to crawl the entire project.

# Core Definition
The project domain contains rules that perform project-level analysis, including module graph construction and dependency resolution. When rules belonging to this domain are enabled, Biome's Scanner crawls the entire project to build the necessary information. This scanning phase has a measurable performance impact on the linting process. The Scanner is opt-in -- it is triggered only when a project-domain rule is enabled.

# Prerequisites
- linter-domains
- biome-linter

# Key Properties
1. **Scanner dependency** -- Enabling project-domain rules triggers the Scanner
2. **Module graph** -- Rules use the project's module graph for dependency resolution
3. **Performance impact** -- Scanning adds overhead: roughly 2s for ~2k files, ~8s for ~5k files (vs. ~800ms and ~1s without)
4. **Memory impact** -- Scans `.d.ts` files inside `node_modules`, including transitive dependencies, which increases memory usage
5. **Opt-in** -- The Scanner only runs when a project-domain rule is enabled

# Construction / Recognition
```json
{
  "linter": {
    "domains": {
      "project": "recommended"
    }
  }
}
```

Project-domain rules include:
- `noPrivateImports` (recommended)
- `noUndeclaredDependencies`
- `noUnresolvedImports`
- `useImportExtensions`
- `useJsonImportAttributes`
- `noDeprecatedImports`
- `noImportCycles`

# Context & Application
The project domain enables powerful cross-file analysis that single-file linters cannot perform. Rules like `noImportCycles` detect circular dependencies, `noUnresolvedImports` catches broken imports, and `noUndeclaredDependencies` finds imports from packages not listed in `package.json`. The trade-off is performance: the Scanner must crawl the entire project and its `node_modules`.

# Examples
From linter/index.mdx, FAQ section:
- "Since Biome v2, we've extended its architecture with a tool called Scanner. The Scanner is responsible for crawling your project files and creating important information such as the module graph and the inferred types."
- Performance benchmarks: "~2k files: ~800ms without Scanner, ~2s with Scanner; ~5k files: ~1000ms without Scanner, ~8s with Scanner"
- "The Scanner is opt-in, and it's triggered only when a rule that belongs to the project domain is enabled."

From linter/domains.mdx, "Project" section:
- "This domain contains rules that perform project-level analysis. This includes our module graph for dependency resolution."

# Relationships
## Builds Upon
- linter-domains

## Enables
- Cross-file import validation
- Circular dependency detection
- Dependency declaration validation

## Related
- types-domain (also triggers the Scanner)
- nursery-rules (some project rules may be in nursery)

## Contrasts With
- Single-file rule groups that do not require the Scanner

# Common Errors
1. Enabling project-domain rules without expecting the performance impact
2. Not understanding why memory usage increases -- Biome scans `.d.ts` files from transitive dependencies

# Common Confusions
1. **Why scan transitive dependencies?** -- Libraries can export types from their dependencies, so Biome must resolve the full dependency graph
2. **Project domain vs. types domain** -- Project domain focuses on module graph and imports; types domain focuses on type inference

# Source Reference
- linter/domains.mdx: "Project" section
- linter/index.mdx: FAQ sections on slowness and memory usage

# Verification Notes
- High confidence: Project domain behavior and Scanner relationship are explicitly documented
- Performance numbers taken directly from source FAQ
