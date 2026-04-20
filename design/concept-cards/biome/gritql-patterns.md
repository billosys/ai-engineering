---
# === CORE IDENTIFICATION ===
concept: GritQL Patterns
slug: gritql-patterns

# === CLASSIFICATION ===
category: gritql
subcategory: patterns
tier: advanced

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "reference/gritql.mdx"
chapter_number: null
pdf_page: null
section: "Patterns"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - GritQL code snippets
  - GritQL queries

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gritql
extends:
  - gritql
related:
  - biome-linter
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before writing GritQL plugins?"
  - "How does GritQL relate to linter plugins?"
---

# Quick Definition
GritQL patterns are the building blocks of GritQL queries, combining code snippets, variables, conditions, and node matching to perform structural code searches.

# Core Definition
GritQL patterns are the primary mechanism for structural code matching. Patterns include code snippets (source code in backticks), variables (`$name` placeholders that match any node), conditions (`where` clauses with operators like match `<:` and `or`), and direct syntax node matching (using Biome's PascalCase node names like `JsIfStatement`). Patterns compose to create precise structural queries.

# Prerequisites
- gritql (understanding what GritQL is and its role in Biome)

# Key Properties
1. **Code snippets**: Source code wrapped in backticks that matches structurally
2. **Variables**: `$`-prefixed identifiers that match any node; same variable name enforces equality
3. **Conditions**: `where` clauses that constrain matches using operators
4. **Match operator** (`<:`): Tests whether a variable matches a specific pattern
5. **Or operator**: Matches any of several alternatives (e.g., `or { \`log\`, \`warn\` }`)
6. **Node matching**: Direct matching against Biome syntax nodes using PascalCase names (e.g., `JsIfStatement()`)
7. **Node names**: Discoverable via Biome Playground syntax tree or `.ungram` files in the repository
8. Biome's grammar may change between versions, potentially breaking node-based patterns

# Construction / Recognition
Code snippet pattern:
```grit
`console.log($message)`
```

Variable reuse enforces structural equality:
```grit
`$fn && $fn()`
```

Condition with match operator:
```grit
`console.$method($message)` where {
    $method <: or { `log`, `info`, `warn`, `error` }
}
```

Direct node matching with diagnostic registration:
```grit
engine biome(1.0)
language js(typescript,jsx)

JsIfStatement() as $stmt where {
  register_diagnostic(
    span=$stmt,
    message="Found an if statement"
  )
}
```

JSON node matching:
```grit
language json
JsonMember(name = JsonMemberName(value = `"version"`))
```

# Context & Application
Patterns are used in two main contexts: the `biome search` CLI command for ad-hoc structural search, and analyzer plugins for custom lint rules. Writing effective plugins requires understanding all pattern types and how they compose. Node matching provides the most precise control but is sensitive to Biome version changes.

# Examples
From `reference/gritql.mdx`:

Simple structural match — `\`console.log('Hello, world!')\`` matches regardless of whitespace or quote style.

Variable equality — `\`$fn && $fn()\`` matches `foo && foo()` and `foo.bar && foo.bar()` but not `foo && bar()`.

Conditions with or — matching multiple console methods:
```grit
`console.$method($message)` where {
    $method <: or { `log`, `info`, `warn`, `error` }
}
```

JSON with TreeSitter aliases — `JsonMember` can also be referenced as `pair`, `JsonObjectValue` as `object`, `JsonArrayValue` as `array`.

# Relationships
## Builds Upon
- gritql (the query language these patterns belong to)

## Enables
- Custom linter plugins through structural pattern matching
- Precise codebase search via `biome search`

## Related
- biome-linter (plugins use patterns to define custom rules)

## Contrasts With
None directly.

# Common Errors
1. Forgetting that same-named variables must match the same structure — `$fn && $fn()` won't match `foo && bar()`
2. Using node names that change between Biome versions without checking compatibility
3. Not specifying `engine biome(1.0)` and `language` declarations for plugin patterns

# Common Confusions
1. Thinking code snippets do textual matching — they do structural matching, ignoring formatting
2. Confusing GritQL variables with programming language variables — GritQL variables are pattern placeholders
3. Assuming TreeSitter node names work in Biome — Biome uses its own PascalCase node names (though JSON has TreeSitter aliases for compatibility)

# Source Reference
- `sources-md/biome/reference/gritql.mdx`, sections "Patterns", "Variables", "Conditions", "Matching Biome Syntax Nodes", "JSON Patterns"

# Verification Notes
All pattern types, operators, and examples are directly from the source. The version sensitivity caveat for node names is explicitly documented.
