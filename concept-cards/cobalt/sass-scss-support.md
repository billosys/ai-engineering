---
# === CORE IDENTIFICATION ===
concept: Sass and SCSS Support
slug: sass-scss-support

# === CLASSIFICATION ===
category: assets
tier: intermediate

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Docs::Assets"
chapter_number: null
pdf_page: null
section: "Sass"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Sass compilation"
  - "SCSS support"
  - "CSS preprocessing"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - assets
  - cobalt-configuration-file
  - directory-structure
extends:
  - assets
related:
  - cobalt-build
  - cobalt-configuration-file
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I use Sass/SCSS with Cobalt?"
---

# Quick Definition
Cobalt has built-in Sass/SCSS compilation support since v0.12.2, with the output CSS style configurable in `_cobalt.yml` under `assets.sass.style`.

# Core Definition
Cobalt includes default support for Sass (Syntactically Awesome Style Sheets) since version 0.12.2. Sass and SCSS files in the source directory are automatically compiled to CSS during the build process and output to the destination directory. The CSS output style is configurable site-wide in `_cobalt.yml` under the `assets.sass.style` key, which accepts four values: `Nested` (default), `Expanded`, `Compact`, or `Compressed` (source: Cobalt docs, "Assets" page, "Sass" section; "Configuration" page, `assets` settings).

# Prerequisites
- Understanding of assets and how they are handled (see `assets`)
- Understanding of the Cobalt configuration file (see `cobalt-configuration-file`)
- Basic knowledge of Sass/SCSS CSS preprocessor syntax

# Key Properties
1. **Built-in support**: No plugins or external tools needed; Sass compilation is part of Cobalt's build process.
2. **Available since v0.12.2**: Sass support was added in Cobalt version 0.12.2.
3. **Output style options**: Four CSS output formats are available:
   - `Nested` (default): Indented CSS reflecting Sass nesting structure.
   - `Expanded`: Standard, fully expanded CSS.
   - `Compact`: Each rule on a single line.
   - `Compressed`: Minified CSS with no whitespace.
4. **Configuration location**: `assets.sass.style` in `_cobalt.yml`.

# Construction / Recognition
## To Construct/Create:
1. Place `.sass` or `.scss` files in the source directory.
2. Optionally configure the output style in `_cobalt.yml`.
3. Run `cobalt build`; Sass files will be compiled to CSS automatically.

## Configuration example:
```yaml
# _cobalt.yml
assets:
  sass:
    style: Nested
```

# Context & Application
- **Typical contexts**: Styling a Cobalt site using Sass variables, mixins, nesting, and other Sass features.
- **When to use**: When you prefer writing styles in Sass/SCSS rather than plain CSS.
- **Scope**: Site-wide; all Sass/SCSS files in the source are compiled.

# Examples
**Example 1** (source: Cobalt docs, Configuration page): Setting compressed output

```yaml
assets:
  sass:
    style: Compressed
```

This produces minified CSS output suitable for production deployment.

# Relationships
## Builds Upon
- `assets`: Sass files are a type of asset that undergoes transformation (compilation) rather than simple copying.
- `cobalt-configuration-file`: Output style is configured in `_cobalt.yml`.

## Enables
- Using Sass/SCSS features (variables, mixins, nesting, partials) in Cobalt sites.
- Producing optimized CSS output through the `Compressed` style option.

## Related
- `cobalt-build`: Sass compilation occurs during the build step.
- `directory-structure`: Sass files must be in the source directory to be processed.

## Contrasts With
- Plain CSS assets that are simply copied to the destination without transformation.

# Common Errors
1. **Invalid style value**: The `style` field only accepts `Nested`, `Expanded`, `Compact`, or `Compressed`. Other values will cause an error.
2. **Expecting Sass partials starting with `_` to be compiled as standalone files**: Sass partials (files starting with `_`) are typically imported by other Sass files rather than compiled independently. Cobalt follows standard Sass conventions here.

# Common Confusions
1. **Sass vs. SCSS syntax**: Sass (`.sass`) uses indentation-based syntax, while SCSS (`.scss`) uses curly-brace syntax. Both are supported.
2. **Asset compilation vs. asset copying**: Unlike plain assets that are mirrored directly, Sass files are compiled to CSS before being placed in the destination.

# Source Reference
- Cobalt Documentation, "Docs::Assets" page, "Sass" section.
- Cobalt Documentation, "Docs::Configuration" page, `assets` section.

# Verification Notes
- Sass support availability (since v0.12.2) and configuration options are documented in the source. The four style options come from the configuration page.
