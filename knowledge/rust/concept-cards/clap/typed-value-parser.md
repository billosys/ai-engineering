---
concept: TypedValueParser
slug: typed-value-parser
category: builder-api
subcategory: value-conversion
tier: intermediate
source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Value Parsers"
extraction_confidence: high
aliases:
  - "TypedValueParser"
  - "typed value parser"
  - "TypedValueParser trait"
  - "custom value parser"
prerequisites:
  - value-parser
extends:
  - value-parser
related:
  - arg
  - arg-matches
  - builtin-value-parsers
  - clap-error-handling
contrasts_with: []
answers_questions:
  - "How do I implement a custom value parser in clap?"
  - "What is the TypedValueParser trait?"
  - "How do I transform or validate parsed values with map and try_map?"
---

# Quick Definition

`TypedValueParser` is the trait that defines custom parsing and validation logic for clap argument values. It converts raw `OsStr` input into a specific Rust type, and all of clap's built-in parsers implement it. The trait also provides `map` and `try_map` combinators for transforming parsed values.

# Core Definition

`TypedValueParser` is a trait for "parse/validate argument values." It defines an associated `type Value` and a required method `parse_ref` that takes a `&Command`, an optional `&Arg`, and a `&OsStr`, returning `Result<Self::Value, clap::Error>`. As alternatives to implementing the trait directly, the source notes: "Use `Fn(&str) -> Result<T, E>` which implements `TypedValueParser`" or use "`TypedValueParser::map` or `TypedValueParser::try_map` to adapt an existing `TypedValueParser`." The trait also connects to the `value_parser!` macro via the `ValueParserFactory` trait (Clap Documentation, Section 4: Value Parsers).

# Prerequisites

- **value-parser** — `TypedValueParser` is the trait underlying `ValueParser`; understanding `ValueParser` is needed to know where custom parsers fit in the API

# Key Properties

1. Associated type `Value` defines the output type of the parser
2. Required method: `parse_ref(&self, cmd: &Command, arg: Option<&Arg>, value: &OsStr) -> Result<Self::Value, clap::Error>`
3. When `arg` is `None`, an external subcommand value is being parsed
4. `Fn(&str) -> Result<T, E>` automatically implements `TypedValueParser` — closures work directly
5. `map(f)` transforms the output value infallibly: `parser.map(|v| transform(v))`
6. `try_map(f)` transforms the output value fallibly: `parser.try_map(|v| validate(v))`
7. `possible_values()` can be optionally overridden to report enumerated values for help and completion
8. Any `TypedValueParser` can be converted to a type-erased `ValueParser` via `From`

# Construction / Recognition

## To Implement TypedValueParser

1. Define a struct for your parser (must be `Clone`)
2. Implement `TypedValueParser` with:
   - `type Value = YourType;`
   - `fn parse_ref(&self, cmd, arg, value) -> Result<Self::Value, clap::Error>`
3. Inside `parse_ref`, convert `value: &OsStr` to your type, returning `clap::Error` on failure
4. Optionally delegate to a built-in parser first, then apply additional validation

## To Use Closures Instead

1. Define a function `fn parse(s: &str) -> Result<T, E>` where `E: Into<Box<dyn Error>>`
2. Pass directly: `.value_parser(ValueParser::new(parse_fn))`

## To Compose with map/try_map

1. Start with an existing parser: `BoolishValueParser::new()`
2. Chain `.map(|b| if b { 10 } else { 5 })` for infallible transforms
3. Chain `.try_map(|os| validate(os))` for fallible transforms that may return errors

# Context & Application

`TypedValueParser` is the extension point for clap's value parsing system. While most users never need to implement it directly (closures and the `value_parser!` macro cover common cases), it is essential for:

**Typical contexts:**

- Implementing complex validation that depends on the `Command` or `Arg` context
- Creating reusable parser types that can be shared across arguments or projects
- Chaining transformations on built-in parsers via `map` and `try_map`
- Registering custom types with `value_parser!` via the `ValueParserFactory` trait

**Design note:** The `map` and `try_map` methods are particularly powerful for adapting existing parsers. For example, `OsStringValueParser::new().try_map(verify_ext)` can validate file extensions without writing a full `TypedValueParser` implementation.

# Examples

**Example 1** (Section 4, TypedValueParser trait doc): Full custom implementation that validates a `u32` is not equal to a specific value:

```rust
#[derive(Clone)]
struct CustomValueParser;

impl clap::builder::TypedValueParser for CustomValueParser {
    type Value = Custom;

    fn parse_ref(
        &self,
        cmd: &clap::Command,
        arg: Option<&clap::Arg>,
        value: &std::ffi::OsStr,
    ) -> Result<Self::Value, clap::Error> {
        let inner = clap::value_parser!(u32);
        let val = inner.parse_ref(cmd, arg, value)?;
        if val == 10 {
            let mut err = clap::Error::new(ErrorKind::ValueValidation).with_cmd(cmd);
            if let Some(arg) = arg {
                err.insert(ContextKind::InvalidArg, ContextValue::String(arg.to_string()));
            }
            err.insert(ContextKind::InvalidValue, ContextValue::String(val.to_string()));
            return Err(err);
        }
        Ok(Custom(val))
    }
}
```

**Example 2** (Section 4, TypedValueParser::map doc): Using `map` to transform a boolean into a `usize`:

```rust
Arg::new("flag")
    .long("flag")
    .action(clap::ArgAction::SetTrue)
    .value_parser(
        BoolishValueParser::new()
            .map(|b| -> usize { if b { 10 } else { 5 } })
    )
```

**Example 3** (Section 4, TypedValueParser::try_map doc): Using `try_map` to validate file extensions:

```rust
Arg::new("flag")
    .long("flag")
    .value_parser(
        OsStringValueParser::new()
            .try_map(|os| {
                let path = PathBuf::from(os);
                if path.extension() != Some(OsStr::new("rs")) {
                    return Err("only Rust files are supported");
                }
                Ok(path)
            })
    )
```

# Relationships

## Builds Upon

- **value-parser** — `TypedValueParser` is the typed trait that `ValueParser` wraps (type-erased)

## Enables

- **builtin-value-parsers** — All built-in parsers implement `TypedValueParser`

## Related

- **arg** — Custom parsers are attached to arguments via `Arg::value_parser`
- **arg-matches** — The `Value` type determines what `get_one::<T>` returns
- **clap-error-handling** — Custom parsers construct `clap::Error` for validation failures

## Contrasts With

- (none)

# Common Errors

- **Error**: Forgetting to derive or implement `Clone` on a custom parser struct.
  **Correction**: `TypedValueParser` requires `Clone`. Add `#[derive(Clone)]` to your parser struct.

- **Error**: Using `map` when the transformation can fail (returns `Result`).
  **Correction**: Use `try_map` for fallible transformations. `map` requires an infallible closure.

# Common Confusions

- **Confusion**: Thinking you must implement `TypedValueParser` for every custom type.
  **Clarification**: A simple `Fn(&str) -> Result<T, E>` closure automatically implements `TypedValueParser`. Full trait implementation is only needed for access to the `Command` and `Arg` context, or for reusable parser types.

- **Confusion**: Thinking `ValueParserFactory` and `TypedValueParser` are the same thing.
  **Clarification**: `ValueParserFactory` is a separate trait that registers a type with the `value_parser!` macro. It returns a `TypedValueParser` implementation but is not itself a parser.

# Source Reference

Section 4: Value Parsers, from `repos/clap/clap_builder/src/builder/value_parser.rs`, lines 660-870. Covers the `TypedValueParser` trait definition, `Value` associated type, `parse_ref`, `parse`, `possible_values`, `map`, and `try_map` methods. Also references `ValueParserFactory` (line 2241).

# Verification Notes

- Trait definition and alternatives: Directly quoted from the trait doc comment (line 660)
- `map` and `try_map` semantics: Documented with full code examples in the source
- `ValueParserFactory` integration: Documented with full example (line 2241)
- Confidence: HIGH — explicit trait definition with comprehensive code examples
- Cross-references: `value-parser`, `builtin-value-parsers`, `arg`, `arg-matches`, `clap-error-handling` are planned or extracted by other agents
- Uncertainties: None
