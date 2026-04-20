---
# === CORE IDENTIFICATION ===
concept: Cobalt Config Struct
slug: cobalt-config-struct

# === CLASSIFICATION ===
category: rust-api
tier: advanced

# === PROVENANCE ===
source: "Cobalt Static Site Generator Documentation"
source_slug: cobalt
authors: "Cobalt contributors (cobalt-org)"
chapter: "Cobalt API Reference"
chapter_number: null
pdf_page: null
section: "cobalt::cobalt_model::Config"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Config struct"
  - "cobalt_model::Config"
  - "programmatic site config"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cobalt-configuration-file
  - liquid-template-language
extends:
  - cobalt-configuration-file
related:
  - cobalt-build
  - liquid-parser
  - liquid-template-object
  - directory-structure
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I understand before using the Cobalt Rust API?"
---

# Quick Definition
The `cobalt::cobalt_model::Config` struct (re-exported as `cobalt::Config`) is the Rust representation of a complete Cobalt site configuration, containing all fields needed to programmatically build a site using the `cobalt::build(config)` function.

# Core Definition
The `Config` struct in `cobalt::cobalt_model` (v0.20.4) contains 14 public fields that represent the full configuration for a Cobalt site build. It is the parameter type for the `cobalt::build(config: Config) -> Result<()>` function, which is described as "the primary build function that transforms a directory into a site." The struct includes paths for source and destination, page extensions, ignore patterns, page and post collection configurations, site metadata, layout path, Liquid template builder settings, Markdown builder settings, syntax highlighting configuration, asset builder settings, and minification options. It can be constructed from a YAML configuration file using `Config::from_config(source: cobalt_config::Config) -> Result<Self>`. The struct derives `Clone`, `Debug`, `Default`, `Display`, and `Serialize` (source: cobalt rustdoc, `cobalt_model/struct.Config.html`, `fn.build.html`).

# Prerequisites
- Understanding of the `_cobalt.yml` configuration file and its fields (see `cobalt-configuration-file`)
- Rust programming fundamentals
- Understanding of Cobalt's build process (see `cobalt-build`)

# Key Properties
## Public Fields
1. **`source: PathBuf`**: Path to the source directory containing site content.
2. **`destination: PathBuf`**: Path to the output directory for the built site.
3. **`ignore: Vec<KString>`**: Gitignore-style patterns for files to ignore.
4. **`page_extensions: Vec<KString>`**: File extensions that identify template pages (e.g., `md`, `liquid`).
5. **`include_drafts: bool`**: Whether to include draft posts in the build.
6. **`pages: Collection`**: Configuration for the pages collection.
7. **`posts: Collection`**: Configuration for the posts collection.
8. **`site: Site`**: Site-wide metadata (title, description, base_url, etc.).
9. **`layouts_path: PathBuf`**: Path to the layouts directory.
10. **`liquid: LiquidBuilder`**: Configuration for the Liquid template engine.
11. **`markdown: MarkdownBuilder`**: Configuration for the Markdown processor.
12. **`syntax: Arc<SyntaxHighlight>`**: Syntax highlighting configuration (shared reference-counted).
13. **`assets: AssetsBuilder`**: Configuration for asset processing (including Sass).
14. **`minify: Minify`**: Configuration for HTML/CSS minification.

## Methods
15. **`from_config(source: cobalt_config::Config) -> Result<Self>`**: Constructs a `Config` from the deserialized YAML configuration file representation.

## Traits Implemented
16. **`Clone`**: Can be duplicated.
17. **`Debug`**: Can be debug-formatted.
18. **`Default`**: Provides a default configuration.
19. **`Display`**: Can be formatted as a string.
20. **`Serialize`**: Can be serialized (e.g., to YAML/JSON).

# Construction / Recognition
## Creating from a YAML config file:
```rust
use cobalt::Config;
use cobalt_config;

// Load and parse the YAML config file
let yaml_config: cobalt_config::Config = /* load from _cobalt.yml */;
let config = Config::from_config(yaml_config).unwrap();
```

## Creating with defaults:
```rust
let config = cobalt::Config::default();
```

## Building a site programmatically:
```rust
let config = cobalt::Config::default();
// ... modify config fields as needed ...
cobalt::build(config).unwrap();
```

# Context & Application
- **Typical contexts**: Building Cobalt sites programmatically from Rust code, creating custom build tools that wrap Cobalt, testing Cobalt builds programmatically.
- **When to use**: When you want to control Cobalt's build process from Rust code rather than using the CLI.
- **Scope**: Represents the complete configuration for a single site build.

# Examples
**Example 1** (source: cobalt rustdoc, fn.build): Programmatic site build

```rust
// The primary build function signature
pub fn build(config: Config) -> Result<()>

// Usage:
let mut config = cobalt::Config::default();
config.source = std::path::PathBuf::from("./my-site");
config.destination = std::path::PathBuf::from("./output");
cobalt::build(config).expect("Site build failed");
```

**Example 2** (source: cobalt rustdoc, struct.Config): Accessing config fields

```rust
let config = cobalt::Config::default();
println!("Source: {:?}", config.source);
println!("Destination: {:?}", config.destination);
println!("Include drafts: {}", config.include_drafts);
```

# Relationships
## Builds Upon
- `cobalt-configuration-file`: The struct is the Rust representation of `_cobalt.yml`.

## Enables
- `cobalt-build`: The `cobalt::build(config)` function takes `Config` as its parameter.
- Programmatic Cobalt site building from Rust code.

## Related
- `liquid-parser`: The `liquid: LiquidBuilder` field configures the Liquid template engine.
- `directory-structure`: The `source`, `destination`, `layouts_path` fields correspond to directory structure concepts.
- `liquid-template-object`: Templates are created and rendered as part of the build process configured by this struct.

## Contrasts With
- `_cobalt.yml` file: The YAML file is the user-facing configuration; `Config` is the Rust-side representation. They contain the same information but `Config` includes additional resolved/computed fields.

# Common Errors
1. **Invalid paths**: Setting `source` or `destination` to non-existent paths will cause the build to fail.
2. **Missing `from_config` conversion**: Directly constructing `Config` without `from_config` may miss default resolution logic that the YAML parser provides.

# Common Confusions
1. **`cobalt::Config` vs. `cobalt_config::Config`**: `cobalt_config::Config` is the raw deserialized YAML structure; `cobalt::cobalt_model::Config` is the resolved, ready-to-build configuration. The `from_config` method converts between them.
2. **`Config` re-export**: `cobalt::Config` is a re-export of `cobalt::cobalt_model::Config`.

# Source Reference
- cobalt rustdoc: `cobalt::cobalt_model::Config` (v0.20.4), `cobalt::build`.
- Source: `src/cobalt/cobalt_model/config.rs`.

# Verification Notes
- All 14 fields, the `from_config` method, and trait implementations confirmed from `sources-html/cobalt/cobalt_model/struct.Config.html`. The `build` function signature confirmed from `sources-html/cobalt/fn.build.html`.
