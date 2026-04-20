---
# === CORE IDENTIFICATION ===
concept: GritQL
slug: gritql

# === CLASSIFICATION ===
category: gritql
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "reference/gritql.mdx"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Grit Query Language

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome
extends: []
related:
  - gritql-patterns
  - biome-linter
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is GritQL?"
  - "What must I know before writing GritQL plugins?"
  - "How does GritQL relate to linter plugins?"
---

# Quick Definition
GritQL is a structural search query language used in Biome for pattern-based code matching that ignores formatting details like whitespace and quote style.

# Core Definition
GritQL is a query language for performing structural searches on source code. It ignores trivia such as whitespace and quote type, focusing on syntactic structure. It offers features including code snippets (patterns), variables, conditions, and node matching. GritQL is open-source, created by Grit.io, and integrated into Biome for two purposes: analyzer plugins (linter plugins) and the `biome search` command.

# Prerequisites
Requires understanding of Biome as a toolchain.

# Key Properties
1. Performs structural (not textual) matching — ignores whitespace and quote differences
2. Supports code snippet patterns wrapped in backticks
3. Supports variables (prefixed with `$`) for flexible matching
4. Supports conditions via the `where` operator and match operator `<:`
5. Can match Biome's internal syntax nodes directly (e.g., `JsIfStatement`)
6. Currently supports JavaScript/TypeScript, CSS, and JSON
7. Used for linter plugins and the `biome search` CLI command
8. GritQL support in Biome is actively being developed; some features are still missing

# Construction / Recognition
GritQL queries are written as patterns. The simplest form is a code snippet in backticks:
```grit
`console.log('Hello, world!')`
```

Variables use `$` prefix:
```grit
`console.$method($message)`
```

Conditions use `where`:
```grit
`console.$method($message)` where {
    $method <: or { `log`, `info`, `warn`, `error` }
}
```

Node matching uses PascalCase node names:
```grit
JsIfStatement() as $stmt where {
  register_diagnostic(span=$stmt, message="Found an if statement")
}
```

# Context & Application
GritQL is the foundation for Biome's plugin system. Pure GritQL plugins can define custom lint rules through structural patterns. The `biome search` command uses GritQL for codebase-wide structural search. Future plans include JS/TS plugins that use GritQL for code selection.

# Examples
From `reference/gritql.mdx`:

Structural matching ignores formatting — this pattern:
```grit
`console.log('Hello, world!')`
```
matches both `console.log('Hello, world!')` and `console.log("Hello, world!")`.

Same variable appearing twice enforces equality:
```grit
`$fn && $fn()`
```
This matches `foo && foo()` and `foo.bar && foo.bar()` but not `foo && bar()`.

JSON pattern matching:
```grit
language json
`"foo": $value`
```

Shell usage note: backticks conflict with shell command invocation, so wrap GritQL queries in single quotes for `biome search`.

# Relationships
## Builds Upon
- biome (the toolchain integrating GritQL)

## Enables
- gritql-patterns (detailed pattern syntax)
- Linter plugins via structural matching
- Codebase-wide structural search via `biome search`

## Related
- biome-linter (GritQL powers linter plugins)

## Contrasts With
None directly; GritQL is the only structural search language in Biome.

# Common Errors
1. Using backticks in shell commands without quoting — shells interpret backticks as command invocations
2. Relying on GritQL features not yet supported in Biome — check the GitHub issue for current status

# Common Confusions
1. Expecting textual/regex matching — GritQL is structural, ignoring formatting details
2. Assuming all Grit.io features work in Biome — Biome's GritQL support is still being developed
3. Thinking GritQL is only for search — it also powers the plugin/linter system

# Source Reference
- `sources-md/biome/reference/gritql.mdx`

# Verification Notes
Extracted from the GritQL reference page. All features and limitations are explicitly documented. The integration status caveat is noted.
