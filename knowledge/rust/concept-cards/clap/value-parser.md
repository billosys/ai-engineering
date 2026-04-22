---
concept: ValueParser
slug: value-parser
category: builder-api
subcategory: value-conversion
tier: foundational
source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Value Parsers"
extraction_confidence: high
aliases:
  - "ValueParser"
  - "value parser"
  - "Arg::value_parser"
  - "value_parser!"
prerequisites: []
extends: []
related:
  - arg
  - arg-matches
  - typed-value-parser
  - builtin-value-parsers
  - possible-value
contrasts_with: []
answers_questions:
  - "How does clap convert raw string arguments into typed values?"
  - "What is ValueParser and how do I use it?"
  - "How do I parse command-line arguments into types like u16 or PathBuf?"
---

# Quick Definition

`ValueParser` defines how clap converts a raw argument string into a validated, typed value. It is specified via `Arg::value_parser(...)` and supports strings, booleans, numbers, paths, enumerated values, ranges, and custom parsing functions.

# Core Definition

`ValueParser` is the type that "defines how to convert a raw argument value into a validated and typed value for use within an application." It is specified with `Arg::value_parser`. Clap provides three main entry points: the `value_parser!` macro for automatically selecting an implementation for a given type, `ValueParser::new` for wrapping any `TypedValueParser` implementation, and direct construction from string arrays or numeric ranges. The parsed values are then retrieved from `ArgMatches` via `get_one::<T>`, where `T` must match the parser's output type (Clap Documentation, Section 4: Value Parsers).

# Prerequisites

This is a foundational concept with no prerequisites within this source. Familiarity with `Arg` (how arguments are defined) provides useful context.

# Key Properties

1. Set on an argument via `Arg::value_parser(...)` — this is the recommended way to control argument types since clap v4
2. The `value_parser!` macro selects a parser automatically for common types: `value_parser!(u16)`, `value_parser!(bool)`, `value_parser!(PathBuf)`, `value_parser!(String)`
3. String arrays create a `PossibleValuesParser`: `.value_parser(["always", "auto", "never"])`
4. Numeric ranges create a `RangedI64ValueParser`: `.value_parser(3000..4000)` or `.value_parser(3000..)`
5. Custom parsing via closures: `ValueParser::new(|s: &str| -> Result<T, E> { ... })`
6. Convenience constructors: `ValueParser::bool()`, `ValueParser::string()`, `ValueParser::os_string()`, `ValueParser::path_buf()`
7. Any `TypedValueParser` can be converted to `ValueParser` via `From`

# Construction / Recognition

## To Use a Built-in Value Parser

1. For standard types, use the `value_parser!` macro: `.value_parser(clap::value_parser!(u16))`
2. For enumerated string values, pass an array: `.value_parser(["always", "auto", "never"])`
3. For ranged integers, pass a range: `.value_parser(3000..4000)` or `.value_parser(3000..)`
4. For specialized parsers, construct directly: `.value_parser(NonEmptyStringValueParser::new())`

## To Use a Custom Value Parser

1. Define a function `fn parse(s: &str) -> Result<T, E>` where `E: Into<Box<dyn Error>>`
2. Wrap it: `.value_parser(ValueParser::new(parse))`
3. Alternatively, implement the `TypedValueParser` trait for full control

## To Retrieve Parsed Values

1. The type parameter in `get_one::<T>` must match the parser's output type
2. For `value_parser!(u16)`, use `get_one::<u16>("name")`
3. For string-array parsers, the output type is `String`: `get_one::<String>("name")`

# Context & Application

`ValueParser` is the central mechanism for type safety in clap's builder API. Before clap v4, string validation was ad-hoc; `ValueParser` standardizes the conversion from raw `OsStr` input to typed Rust values.

**Typical contexts:**

- Converting command-line port numbers to `u16` with range validation
- Accepting file paths as `PathBuf` with non-empty validation
- Restricting an argument to an enumerated set of string values
- Parsing custom types from string representations

**Design pattern:** The `value_parser!` macro and `From` impls provide ergonomic shortcuts so that most users never need to implement `TypedValueParser` directly. The macro handles `bool`, `String`, `OsString`, `PathBuf`, all integer types, and any type implementing `ValueEnum`.

# Examples

**Example 1** (Section 4, ValueParser struct doc): Complete example showing string enumeration, non-empty string, and ranged integer parsers together:

```rust
let mut cmd = clap::Command::new("raw")
    .arg(
        clap::Arg::new("color")
            .long("color")
            .value_parser(["always", "auto", "never"])
            .default_value("auto")
    )
    .arg(
        clap::Arg::new("hostname")
            .long("hostname")
            .value_parser(clap::builder::NonEmptyStringValueParser::new())
            .action(clap::ArgAction::Set)
            .required(true)
    )
    .arg(
        clap::Arg::new("port")
            .long("port")
            .value_parser(clap::value_parser!(u16).range(3000..))
            .action(clap::ArgAction::Set)
            .required(true)
    );
```

**Example 2** (Section 4, ValueParser::new doc): Custom parsing function for key=value pairs:

```rust
type EnvVar = (String, Option<String>);
fn parse_env_var(env: &str) -> Result<EnvVar, std::io::Error> {
    if let Some((var, value)) = env.split_once('=') {
        Ok((var.to_owned(), Some(value.to_owned())))
    } else {
        Ok((env.to_owned(), None))
    }
}

let mut cmd = clap::Command::new("raw")
    .arg(
        clap::Arg::new("env")
            .value_parser(clap::builder::ValueParser::new(parse_env_var))
            .required(true)
    );
```

# Relationships

## Builds Upon

- (none within this source — foundational)

## Enables

- **typed-value-parser** — `TypedValueParser` is the trait that `ValueParser` wraps
- **builtin-value-parsers** — The specific parser structs that implement `TypedValueParser`

## Related

- **arg** — `ValueParser` is set on an `Arg` via `Arg::value_parser`
- **arg-matches** — Parsed values are retrieved from `ArgMatches` using the type produced by the `ValueParser`
- **possible-value** — `PossibleValuesParser` uses `PossibleValue` to define enumerated choices

## Contrasts With

- (none)

# Common Errors

- **Error**: Using `.value_parser(clap::value_parser!(u16))` but retrieving with `get_one::<String>("port")`.
  **Correction**: The type parameter in `get_one::<T>` must match the parser's output type. Use `get_one::<u16>("port")` for a `u16` parser.

- **Error**: Passing a string literal instead of an array for enumerated values: `.value_parser("always")`.
  **Correction**: Pass an array of values: `.value_parser(["always", "auto", "never"])`. A single string is not a valid `ValueParser` input.

# Common Confusions

- **Confusion**: Thinking `value_parser!(u16).range(3000..)` produces an `i64`.
  **Clarification**: The `value_parser!` macro with a specific type preserves that type. `value_parser!(u16).range(3000..)` produces `u16`. However, using a bare range like `.value_parser(3000..4000)` without the macro produces `i64`.

- **Confusion**: Thinking that `.value_parser(["a", "b"])` stores `&str` values.
  **Clarification**: String-array value parsers always produce `String`. Retrieve with `get_one::<String>`, not `get_one::<&str>`.

# Source Reference

Section 4: Value Parsers, from `repos/clap/clap_builder/src/builder/value_parser.rs`, lines 10-530. Covers the `ValueParser` struct definition, `new`, `bool`, `string`, `os_string`, `path_buf` constructors, and `From` impls for ranges and string arrays.

# Verification Notes

- Definition: Directly quoted from the struct-level doc comment on `ValueParser` (line 10)
- Constructor methods: Documented individually with code examples in the source
- Range-to-ValueParser conversions: Multiple `From` impls documented (lines 309-495)
- Confidence: HIGH — explicit definition with extensive code examples
- Cross-references: `arg`, `arg-matches`, `typed-value-parser`, `builtin-value-parsers`, `possible-value` are planned or extracted by other agents
- Uncertainties: None
