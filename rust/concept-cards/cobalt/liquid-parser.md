---
# === CORE IDENTIFICATION ===
concept: Liquid Parser and ParserBuilder
slug: liquid-parser

# === CLASSIFICATION ===
category: rust-api
tier: advanced

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Liquid API Reference"
chapter_number: null
pdf_page: null
section: "liquid::Parser / liquid::ParserBuilder"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Liquid Rust parser"
  - "template parser"
  - "ParserBuilder"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - liquid-template-language
extends: []
related:
  - liquid-template-object
  - liquid-value-system
  - objectview-valueview-traits
  - cobalt-config-struct
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Liquid Rust crate relate to Ruby Liquid?"
  - "What must I understand before using the Cobalt Rust API?"
  - "What distinguishes Cobalt's Liquid from Ruby Liquid?"
---

# Quick Definition
The `Parser` and `ParserBuilder` structs in the `liquid` Rust crate (v0.26.11) provide the programmatic API for compiling Liquid template strings into `Template` objects, using a builder pattern that allows registering the standard library, custom tags, custom blocks, custom filters, and partial-template compilers.

# Core Definition
The `liquid::ParserBuilder` is a builder struct that configures and creates a `liquid::Parser`. The standard workflow is `ParserBuilder::with_stdlib().build().unwrap().parse("template string")`, which creates a parser with the full Liquid standard library (tags, blocks, and filters), compiles the parser, and then parses a template string into a `Template` object. `ParserBuilder` provides methods for incremental configuration: `new()` creates an empty builder, `with_stdlib()` creates one pre-loaded with the standard library, `stdlib()` adds the standard library to an existing builder, `block()` / `tag()` / `filter()` register custom extensions, `partials()` configures partial-template compilation, and `build()` produces a `Parser`. The `Parser` struct itself has `parse(&self, text: &str) -> Result<Template>` for parsing strings and `parse_file(&self, file: P) -> Result<Template>` for parsing files. Both `Parser` and `ParserBuilder` implement `ParserReflection` for introspecting registered blocks, tags, filters, and partials (source: liquid rustdoc, `struct.Parser.html`, `struct.ParserBuilder.html`).

# Prerequisites
- Understanding of Liquid template language concepts (see `liquid-template-language`)
- Rust programming fundamentals (ownership, Result types, builder pattern)
- Understanding of Liquid value types for providing template data (see `liquid-value-system`)

# Key Properties
## ParserBuilder
1. **`new()`**: Creates an empty parser builder with no registered tags, blocks, or filters.
2. **`with_stdlib()`**: Creates a parser builder pre-loaded with the standard Liquid library.
3. **`stdlib()`**: Adds the standard library to an existing builder (method chaining).
4. **`block(b)`**: Registers a custom block parser.
5. **`tag(t)`**: Registers a custom tag parser.
6. **`filter(f)`**: Registers a custom filter parser.
7. **`partials(n)`**: Configures the partial-template compiler (e.g., `EagerCompiler<InMemorySource>`).
8. **`build()`**: Produces a `Result<Parser>`.
9. **Default partial compiler**: `EagerCompiler<InMemorySource>`.

## Parser
10. **`parse(&self, text: &str) -> Result<Template>`**: Parses a Liquid template string.
11. **`parse_file(&self, file: P) -> Result<Template>`**: Parses a Liquid template from a file path.
12. **`new()`**: Creates a default parser (no stdlib).
13. **Thread-safe**: `Parser` implements `Send + Sync`, so it can be shared across threads.
14. **Clonable**: `Parser` implements `Clone`.

# Construction / Recognition
## Standard usage pattern:
```rust
// Create a parser with the standard library
let parser = liquid::ParserBuilder::with_stdlib()
    .build()
    .unwrap();

// Parse a template string
let template = parser.parse("Liquid! {{num | minus: 2}}").unwrap();

// Parse a template file
let template = parser.parse_file("path/to/template.liquid").unwrap();
```

## Custom extensions:
```rust
let parser = liquid::ParserBuilder::with_stdlib()
    .filter(MyCustomFilter)
    .tag(MyCustomTag)
    .block(MyCustomBlock)
    .build()
    .unwrap();
```

# Context & Application
- **Typical contexts**: Building Cobalt-like static site generators, embedding Liquid templates in Rust applications, server-side rendering with Liquid templates.
- **When to use ParserBuilder**: When you need to customize the parser with custom filters, tags, or blocks, or when you need to configure partial compilation.
- **When to use Parser::new()**: When you want a bare parser without any standard library features (rare).
- **Scope**: The Parser is the entry point for all Liquid template compilation in Rust.

# Examples
**Example 1** (source: liquid rustdoc, crate overview): Complete parse-and-render workflow

```rust
let template = liquid::ParserBuilder::with_stdlib()
    .build().unwrap()
    .parse("Liquid! {{num | minus: 2}}").unwrap();

let globals = liquid::object!({
    "num": 4f64
});

let output = template.render(&globals).unwrap();
assert_eq!(output, "Liquid! 2".to_string());
```

**Example 2** (source: liquid rustdoc, Parser::parse): Minimal template

```rust
let template = liquid::ParserBuilder::with_stdlib()
    .build().unwrap()
    .parse("Liquid!").unwrap();

let globals = liquid::Object::new();
let output = template.render(&globals).unwrap();
assert_eq!(output, "Liquid!".to_string());
```

# Relationships
## Builds Upon
- `liquid-template-language`: The parser compiles Liquid template syntax into executable templates.

## Enables
- `liquid-template-object`: `parse()` and `parse_file()` produce `Template` objects.
- Programmatic Liquid template processing in Rust applications.

## Related
- `liquid-value-system`: Values are passed to templates for rendering.
- `objectview-valueview-traits`: Template data must implement these traits.
- `cobalt-config-struct`: Cobalt uses the Liquid parser internally as part of its build process.

## Contrasts With
- Ruby Liquid parser: The Rust `ParserBuilder` pattern does not exist in Ruby Liquid; Ruby uses `Liquid::Template.parse()` directly. The Rust version provides more explicit control over which features are loaded.

# Common Errors
1. **Forgetting `with_stdlib()`**: Creating a parser with `ParserBuilder::new().build()` produces a parser without any standard tags or filters, causing template compilation to fail on standard constructs.
2. **Unwrapping without error handling**: Both `build()` and `parse()` return `Result` types that should be properly handled.

# Common Confusions
1. **ParserBuilder vs. Parser**: `ParserBuilder` is for configuration; `Parser` is the compiled, immutable parser. You cannot add extensions after calling `build()`.
2. **Rust Liquid vs. Ruby Liquid**: The Rust implementation is a separate codebase that aims for compatibility with Ruby Liquid templates, but has its own API design using Rust idioms (builder pattern, trait-based values).

# Source Reference
- liquid rustdoc: `liquid::Parser` (v0.26.11), `liquid::ParserBuilder`.
- Source: `src/liquid/parser.rs`.

# Verification Notes
- All methods, type signatures, and examples confirmed from the HTML rustdoc at `sources-html/liquid/struct.Parser.html` and `sources-html/liquid/struct.ParserBuilder.html`.
