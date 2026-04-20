---
# === CORE IDENTIFICATION ===
concept: Liquid Template Object
slug: liquid-template-object

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
section: "liquid::Template"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "compiled template"
  - "Template struct"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - liquid-parser
  - liquid-template-language
extends:
  - liquid-parser
related:
  - liquid-value-system
  - objectview-valueview-traits
  - cobalt-config-struct
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Liquid Rust crate relate to Ruby Liquid?"
  - "What must I understand before using the Cobalt Rust API?"
---

# Quick Definition
The `Template` struct in the `liquid` Rust crate represents a compiled Liquid template that can be rendered with global variables, producing a `String` output or writing to an `io::Write` target.

# Core Definition
`liquid::Template` is an opaque struct (private fields) produced by `Parser::parse()` or `Parser::parse_file()`. It represents a fully compiled Liquid template. The struct provides two rendering methods: `render(&self, globals: &dyn ObjectView) -> Result<String>`, which renders the template into a `String`, and `render_to(&self, writer: &mut dyn Write, globals: &dyn ObjectView) -> Result<()>`, which renders into any type implementing `std::io::Write`. The `globals` parameter must implement the `ObjectView` trait, which is typically satisfied by `liquid::Object` (a type alias for a map of string keys to Liquid values) or any custom type deriving `ObjectView`. The `Template` is `Send + Sync` and can be shared across threads for concurrent rendering (source: liquid rustdoc, `struct.Template.html`).

# Prerequisites
- Understanding of the Parser and ParserBuilder for creating templates (see `liquid-parser`)
- Understanding of ObjectView trait for providing template data (see `objectview-valueview-traits`)
- Understanding of the Liquid value system for constructing global variables (see `liquid-value-system`)

# Key Properties
1. **`render(&self, globals: &dyn ObjectView) -> Result<String>`**: Renders the template using the provided global variables, returning the result as a `String`.
2. **`render_to(&self, writer: &mut dyn Write, globals: &dyn ObjectView) -> Result<()>`**: Renders directly to a writer (e.g., `File`, `Vec<u8>`, `stdout`), avoiding intermediate `String` allocation for large templates.
3. **Opaque struct**: Internal fields are private; you interact with templates only through `render` and `render_to`.
4. **Thread-safe**: Implements `Send + Sync`, allowing templates to be compiled once and rendered concurrently.
5. **Immutable rendering**: The `render` method takes `&self`, meaning the template is not modified during rendering. Multiple calls with different globals are safe.
6. **Created by Parser**: Templates are not constructed directly; they are always produced by `Parser::parse()` or `Parser::parse_file()`.

# Construction / Recognition
## To Create:
```rust
let parser = liquid::ParserBuilder::with_stdlib()
    .build().unwrap();

// From a string
let template = parser.parse("Hello, {{ name }}!").unwrap();

// From a file
let template = parser.parse_file("template.liquid").unwrap();
```

## To Render:
```rust
// Render to String
let globals = liquid::object!({ "name": "World" });
let output = template.render(&globals).unwrap();
assert_eq!(output, "Hello, World!");

// Render to writer
let mut buffer = Vec::new();
template.render_to(&mut buffer, &globals).unwrap();
```

# Context & Application
- **Typical contexts**: Server-side rendering, static site generation, template-based code generation, email template rendering.
- **When to use `render`**: When you need the output as a `String` (most common case).
- **When to use `render_to`**: When writing directly to a file or network stream to avoid memory allocation for large outputs.
- **Scope**: Each `Template` instance represents one parsed template.

# Examples
**Example 1** (source: liquid rustdoc, Parser::parse): Render with global variables

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

**Example 2** (source: liquid rustdoc, Parser::parse): Render with empty globals

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
- `liquid-parser`: Templates are produced by the parser.
- `objectview-valueview-traits`: The `globals` parameter must implement `ObjectView`.

## Enables
- Rendering Liquid templates in Rust applications.
- String output or streaming output to writers.

## Related
- `liquid-value-system`: Global variables use the Liquid value types.
- `cobalt-config-struct`: Cobalt's build process internally creates and renders templates.

## Contrasts With
- Ruby Liquid `Template`: In Ruby, `Liquid::Template.parse(str).render(hash)` is the equivalent. The Rust version separates parsing (via `Parser`) from the template object, and uses trait objects (`&dyn ObjectView`) instead of Ruby hashes.

# Common Errors
1. **Passing wrong type as globals**: The `globals` parameter must implement `ObjectView`. Using a raw `HashMap` without the right key/value types will fail to compile.
2. **Ignoring render errors**: `render()` returns `Result`; template evaluation errors (e.g., accessing missing keys when strict mode is on) must be handled.

# Common Confusions
1. **Template is not the parser**: You cannot add filters or tags to a Template; those must be registered on the `ParserBuilder` before compilation.
2. **`render` vs. `render_to`**: Both produce the same output; the difference is where the output goes (String vs. writer).

# Source Reference
- liquid rustdoc: `liquid::Template` (v0.26.11).
- Source: `src/liquid/template.rs`.

# Verification Notes
- Method signatures and trait implementations confirmed from `sources-html/liquid/struct.Template.html`.
