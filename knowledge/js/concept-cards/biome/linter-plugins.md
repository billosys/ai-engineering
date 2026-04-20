---
# === CORE IDENTIFICATION ===
concept: Linter Plugins
slug: linter-plugins

# === CLASSIFICATION ===
category: plugins
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Biome Documentation"
source_slug: biome
authors: "Biome Contributors"
chapter: "linter/plugins.mdx"
chapter_number: null
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Biome plugins"
  - "GritQL plugins"
  - "custom lint rules"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - biome-linter
  - lint-rules
extends: []
related:
  - rule-severity
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create custom lint rules in Biome?"
  - "What are Biome linter plugins?"
  - "What is GritQL in the context of Biome?"
---

# Quick Definition
Biome linter plugins are custom lint rules written in GritQL that match specific code patterns and emit diagnostic messages using the `register_diagnostic()` function.

# Core Definition
Biome Linter supports GritQL plugins that allow users to match specific code patterns and register customized diagnostic messages for them. A plugin is a `.grit` file containing a GritQL pattern that uses `register_diagnostic()` to emit diagnostics when matched. Plugins are enabled in `biome.json` under the `plugins` array and run on all supported files during `biome lint` or `biome check`.

# Prerequisites
- biome-linter
- lint-rules (understanding what rules do)

# Key Properties
1. **GritQL-based** -- Plugins are written in GritQL, a pattern-matching language
2. **Pattern matching** -- Match code snippets using GritQL's template syntax
3. **register_diagnostic()** -- The primary API function for emitting diagnostics, with arguments: `span` (required), `message` (required), `severity` (optional, defaults to `error`)
4. **Target languages** -- JavaScript (default) and CSS; other languages not yet supported
5. **File extension** -- Plugin files must use the `.grit` extension
6. **Configuration** -- Enabled via `"plugins": ["./path-to-plugin.grit"]` in `biome.json`
7. **Severity levels** -- Diagnostics support `hint`, `info`, `warn`, and `error` (default: `error`)

# Construction / Recognition
1. Create a `.grit` file with a GritQL pattern:
```grit
`$fn($args)` where {
    $fn <: `Object.assign`,
    register_diagnostic(
        span = $fn,
        message = "Prefer object spread instead of `Object.assign()`"
    )
}
```

2. Register the plugin in `biome.json`:
```json
{
    "plugins": ["./path-to-plugin.grit"]
}
```

3. For CSS plugins, specify the target language:
```grit
language css;

`$selector { $props }` where {
    $props <: contains `color: $color` as $rule,
    not $selector <: r"\.color-.*",
    register_diagnostic(
        span = $rule,
        message = "Don't set explicit colors. Use `.color-*` classes instead."
    )
}
```

# Context & Application
Plugins extend Biome's built-in rule set with project-specific or organization-specific patterns. They are useful for enforcing custom coding conventions, deprecating internal API usage, or catching domain-specific anti-patterns. Plugins currently support JavaScript (and its super-languages like TypeScript, JSX) and CSS.

# Examples
From linter/plugins.mdx:
- Object.assign detection plugin: matches `Object.assign()` calls and suggests object spread syntax
- CSS color enforcement plugin: matches selectors setting `color` outside `.color-*` classes
- Plugin output example:
  ```
  /packages/.../introspect.ts:12:17 plugin
    Prefer object spread instead of `Object.assign()`
  ```

# Relationships
## Builds Upon
- biome-linter
- lint-rules

## Enables
- Custom organizational coding standards enforcement
- Project-specific pattern detection

## Related
- rule-severity (plugins support severity via register_diagnostic)

## Contrasts With
- Built-in rules (plugins are user-defined, not part of Biome's rule set)

# Common Errors
1. Forgetting the `.grit` extension -- Biome requires it to recognize the file as a plugin
2. Not specifying `language css;` for CSS plugins -- JavaScript is assumed by default
3. Expecting languages beyond JavaScript and CSS to be supported

# Common Confusions
1. **Plugins vs. built-in rules** -- Plugins cannot provide code fixes; they only emit diagnostics
2. **GritQL vs. regular expressions** -- GritQL matches AST patterns, not text patterns, making it more precise than regex

# Source Reference
- linter/plugins.mdx: Full page describing GritQL plugin creation and API

# Verification Notes
- High confidence: Plugins are explicitly documented with examples and API reference
- Both JavaScript and CSS examples taken directly from source
- register_diagnostic arguments verified from source
