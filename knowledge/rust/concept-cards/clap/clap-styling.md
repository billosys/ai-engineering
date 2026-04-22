---
concept: Clap Styling
slug: clap-styling
category: cli-framework
subcategory: output-formatting
tier: advanced

source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Styling and Formatting"

extraction_confidence: high

aliases:
  - "clap themes"
  - "clap terminal styling"
  - "StyledStr"
  - "ColorChoice"
  - "Styles struct"

prerequisites:
  - command
  - help-generation

extends: []

related:
  - clap-error-handling
  - clap-cargo

contrasts_with: []

answers_questions:
  - "How do I customize the colors and styles of clap help output?"
  - "What is the Styles struct in clap and how do I use it?"
  - "How do I disable colors in clap output?"
  - "What is StyledStr and how does it handle ANSI codes?"
  - "How do I create clap v3-style coloring?"
---

## Quick Definition

Clap's styling system uses the `Styles` struct to define terminal colors and styles for different help and error output elements (headers, usage, literals, placeholders, errors, context), `StyledStr` for ANSI-encoded styled text, and `ColorChoice` for controlling when colors are used.

## Core Definition

The `clap::builder::styling` module provides `Styles`, a struct that defines terminal styling for help and error output. Each element of the output has a configurable style: `header` for section headings, `error` for error headings, `usage` for usage lines, `literal` for command-line syntax like `--help`, `placeholder` for value names, `valid` for suggested usage highlights, `invalid` for invalid usage highlights, `context` for contextual information like `[default: false]`, and `context_value` for values within context. The `Styles::styled()` constructor provides sensible defaults, while `Styles::plain()` disables all styling. Custom styles are built using the builder pattern with `anstyle::Style` values (e.g., `AnsiColor::Yellow.on_default()`). Styles are applied to a Command via `Command::styles`. The `StyledStr` struct holds text with embedded ANSI escape codes and is used throughout clap for styled output. `ColorChoice` controls color preferences with variants for auto-detection, always-on, and always-off (Section 11: Styling and Formatting, and Section 14 styling module in `clap_builder/src/builder/styling.rs`).

## Prerequisites

- **Command** -- Styles are applied via `Command::styles()`
- **Help Generation** -- Styling affects the visual appearance of help and error output

## Key Properties

1. `Styles::styled()` creates the default terminal styling
2. `Styles::plain()` creates styling with no terminal colors
3. `Styles::header(style)` sets the style for general headings (e.g., `help_heading`)
4. `Styles::error(style)` sets the style for error headings
5. `Styles::usage(style)` sets the style for usage headings
6. `Styles::literal(style)` sets the style for command-line syntax like `--help`
7. `Styles::placeholder(style)` sets the style for value descriptions/names
8. `Styles::valid(style)` sets the style for highlighted suggested usage
9. `Styles::invalid(style)` sets the style for highlighted invalid usage
10. `Styles::context(style)` sets the style for context annotations like `[default: false]`
11. `Styles::context_value(style)` specializes the value style within context; falls back to `context` if not set
12. `StyledStr` holds terminal-styled text with ANSI escape codes; `Display` impl is color-unaware
13. `StyledStr::ansi()` displays using ANSI escape code styling
14. `ColorChoice` enum has variants for auto, always, and never color output
15. Each style element has a corresponding getter (e.g., `get_header()`, `get_error()`)

## Construction / Recognition

### To Apply Custom Styling

1. Import `clap::builder::styling::*`
2. Create styles with `Styles::styled()` and chain style setters
3. Use `AnsiColor` values from `anstyle` (e.g., `AnsiColor::Yellow.on_default()`)
4. Apply to command with `Command::styles(my_styles)`

### To Recreate clap v3 Styling

1. Use `Styles::styled()` as the base
2. Set `.header(AnsiColor::Yellow.on_default())`
3. Set `.usage(AnsiColor::Green.on_default())`
4. Set `.literal(AnsiColor::Green.on_default())`
5. Set `.placeholder(AnsiColor::Green.on_default())`

### To Disable Colors

1. Use `Styles::plain()` for no styling
2. Or use `ColorChoice::Never` to disable color globally

## Context & Application

Styling customization is important for tools that need to match an existing brand or project aesthetic. The default clap v4 styling uses bold and underline effects. Some projects prefer the clap v3 color scheme (green/yellow based), which can be recreated using the builder pattern shown in the source. The `color_print` crate's `cstr!` macro can be used to embed styled text in `after_help` and other string fields. The `StyledStr` type transparently converts from `&str` containing ANSI codes, making it easy to use pre-styled text in help messages.

**Typical contexts:**
- Matching cargo-style output (see `clap-cargo` CLAP_STYLING constant)
- Creating consistent theming across a suite of CLI tools
- Disabling colors for CI environments or piped output

## Examples

**Example 1** (Section 14, Styles): Recreating clap v3 styling:
```rust
use clap::builder::styling::*;
let styles = Styles::styled()
    .header(AnsiColor::Yellow.on_default())
    .usage(AnsiColor::Green.on_default())
    .literal(AnsiColor::Green.on_default())
    .placeholder(AnsiColor::Green.on_default());
```

**Example 2** (Section 11, StyledStr): Using `color_print::cstr!` for styled after_help:
```rust
let after_help: &'static str = color_print::cstr!(
    r#"<bold><underline>Examples</underline></bold>

  <dim>$</dim> <bold>mybin --input file.toml</bold>
"#);

let cmd = clap::Command::new("mybin")
    .after_help(after_help);
```

**Example 3** (Section 11, ColorChoice): ColorChoice provides `possible_values()` for use as an argument value type, allowing users to control color output.

## Relationships

### Builds Upon

- **Command** -- Styles are applied via `Command::styles()`
- **Help Generation** -- Styling modifies the visual appearance of help output

### Related

- **clap-error-handling** -- Error output is styled using the `error` and `invalid` styles
- **clap-cargo** -- The `clap_cargo::style::CLAP_STYLING` constant provides cargo-compatible styling for use with `Command::styles`

## Common Errors

- **Error**: Forgetting to call `Styles::styled()` before chaining style setters, starting from default unstyled state
  **Correction**: Always start with `Styles::styled()` (not `Styles::plain()`) if you want styling as a base

- **Error**: Passing `StyledStr` to contexts that strip ANSI codes and getting raw escape sequences
  **Correction**: Use `StyledStr`'s `Display` impl (color-unaware) for plain output, or `.ansi()` for ANSI-styled output

## Common Confusions

- **Confusion**: Thinking `Styles::plain()` and `ColorChoice::Never` do the same thing
  **Clarification**: `Styles::plain()` removes all styling definitions; `ColorChoice::Never` tells the output system not to emit ANSI codes, but the styles are still defined

- **Confusion**: Believing `context_value` inherits from a different style than `context`
  **Clarification**: If `context_value` is not explicitly set, it falls back to the `context` style, not to the global default

## Source Reference

Clap Documentation, Section 11: "Styling and Formatting" (clap-source-docs, `clap_builder/src/builder/styled_str.rs` for StyledStr, `clap_builder/src/util/color.rs` for ColorChoice) and Section 14: "Other Topics" (clap-source-docs, `clap_builder/src/builder/styling.rs` for Styles struct, style element methods, and reflection getters).

## Verification Notes

- Definition: Synthesized from Section 11 (StyledStr, ColorChoice) and Section 14 (Styles struct with all style methods)
- Key Properties: All items directly from source method documentation
- Examples: Examples 1 and 2 taken directly from source code examples
- Confidence: HIGH -- Styles struct is fully documented with clear method descriptions, code examples, and the v3 styling example
- Cross-references: `command`, `help-generation`, `clap-cargo` verified against planned extractions
- Uncertainties: None; styling API is well-documented
