---
concept: Built-in Value Parsers
slug: builtin-value-parsers
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
  - "StringValueParser"
  - "OsStringValueParser"
  - "PathBufValueParser"
  - "BoolValueParser"
  - "BoolishValueParser"
  - "FalseyValueParser"
  - "NonEmptyStringValueParser"
  - "RangedI64ValueParser"
  - "RangedU64ValueParser"
  - "EnumValueParser"
  - "MapValueParser"
  - "TryMapValueParser"
  - "builtin parsers"
prerequisites:
  - value-parser
  - typed-value-parser
extends:
  - typed-value-parser
related:
  - arg
  - arg-matches
  - possible-value
  - value-enum-derive
contrasts_with: []
answers_questions:
  - "What built-in value parsers does clap provide?"
  - "How do I parse booleans, numbers, paths, and strings with clap?"
  - "What is the difference between BoolValueParser, BoolishValueParser, and FalseyValueParser?"
  - "How do I restrict a numeric argument to a range?"
---

# Quick Definition

Clap provides a comprehensive set of built-in `TypedValueParser` implementations for common types: `StringValueParser`, `OsStringValueParser`, `PathBufValueParser` for text/path values; `BoolValueParser`, `BoolishValueParser`, `FalseyValueParser` for boolean variants; `RangedI64ValueParser` and `RangedU64ValueParser` for bounded numbers; `EnumValueParser` for `ValueEnum` types; and `NonEmptyStringValueParser` for non-empty text.

# Core Definition

Clap ships with multiple `TypedValueParser` implementations that cover common argument types. Each parser converts raw `OsStr` input into a specific Rust type with appropriate validation. The parsers are designed for composability: they can be used directly, passed to `Arg::value_parser`, or combined with `map`/`try_map` to build more complex parsers. The `value_parser!` macro provides shorthand access to many of these parsers (Clap Documentation, Section 4: Value Parsers, lines 900-2070).

**String/Path parsers:** `StringValueParser` (any string), `OsStringValueParser` (raw OS string), `PathBufValueParser` (file paths, rejects empty), `NonEmptyStringValueParser` (non-empty strings).

**Boolean parsers:** `BoolValueParser` (strict `true`/`false`), `BoolishValueParser` (accepts `true`/`yes`/`on`/`1` and `false`/`no`/`off`/`0`, case-insensitive), `FalseyValueParser` (false-like strings are `false`, everything else is `true`).

**Numeric parsers:** `RangedI64ValueParser<T>` (signed integers with range bounds, generic over output type), `RangedU64ValueParser<T>` (unsigned integers with range bounds).

**Enum parser:** `EnumValueParser<T>` (parses `ValueEnum` types by matching variant names).

**Combinators:** `MapValueParser` (wraps `TypedValueParser::map`), `TryMapValueParser` (wraps `TypedValueParser::try_map`).

# Prerequisites

- **value-parser** — Built-in parsers are used via the `ValueParser` system
- **typed-value-parser** — All built-in parsers implement the `TypedValueParser` trait

# Key Properties

1. **StringValueParser**: Accepts any valid UTF-8 string; implementation for `ValueParser::string()`
2. **OsStringValueParser**: Accepts any OS string including non-UTF-8; implementation for `ValueParser::os_string()`
3. **PathBufValueParser**: Converts to `PathBuf`; rejects empty strings; implementation for `ValueParser::path_buf()`
4. **NonEmptyStringValueParser**: Like `StringValueParser` but rejects empty strings
5. **BoolValueParser**: Strict — accepts only `"true"` and `"false"`; implementation for `ValueParser::bool()`
6. **BoolishValueParser**: Lenient — accepts `true/yes/on/1` and `false/no/off/0` (case-insensitive); rejects all other inputs
7. **FalseyValueParser**: Most lenient — treats `false/no/off/0/""` as `false`, everything else as `true`
8. **RangedI64ValueParser<T>**: Parses signed integers, validates against a range, converts to target type `T` (e.g., `i32`, `i16`); note that `Arg::allow_negative_numbers` or `Arg::allow_hyphen_values` is required to accept negative values
9. **RangedU64ValueParser<T>**: Parses unsigned integers, validates against a range, converts to target type `T` (e.g., `u32`, `u16`)
10. **EnumValueParser<T>**: Matches string input against `ValueEnum` variant names; returns the typed enum variant

# Construction / Recognition

## To Use via value_parser! Macro

1. `value_parser!(bool)` -> `BoolValueParser`
2. `value_parser!(String)` -> `StringValueParser`
3. `value_parser!(PathBuf)` -> `PathBufValueParser`
4. `value_parser!(u16)` -> `RangedI64ValueParser::<u16>` (with `.range()` support)
5. `value_parser!(ColorChoice)` -> `EnumValueParser::<ColorChoice>` (for `ValueEnum` types)

## To Construct Directly

1. `StringValueParser::new()`, `OsStringValueParser::new()`, `PathBufValueParser::new()`
2. `BoolValueParser::new()`, `BoolishValueParser::new()`, `FalseyValueParser::new()`
3. `NonEmptyStringValueParser::new()`
4. `RangedI64ValueParser::<i32>::new().range(-1..200)`
5. `RangedU64ValueParser::<u32>::new().range(0..200)`
6. `EnumValueParser::<ColorChoice>::new()`

## To Use Range Shorthand

1. `.value_parser(3000..4000)` creates `RangedI64ValueParser` producing `i64`
2. `.value_parser(3000..)` for open-ended range
3. `.value_parser(..3000)` for upper-bounded range
4. For specific output type: `.value_parser(clap::value_parser!(u16).range(3000..))`

# Context & Application

The built-in parsers cover the vast majority of CLI argument types. Understanding the three boolean parser variants is particularly important, as each suits different use cases.

**Typical contexts:**

- `BoolValueParser`: Flag arguments where strict `true`/`false` input is expected
- `BoolishValueParser`: User-friendly boolean arguments accepting various representations (`yes`, `on`, `1`, etc.)
- `FalseyValueParser`: Arguments where the default behavior is "on" and users need to explicitly disable
- `RangedI64ValueParser`/`RangedU64ValueParser`: Port numbers, retry counts, timeout values, any bounded integers
- `NonEmptyStringValueParser`: Hostnames, identifiers, or any argument that must not be blank
- `EnumValueParser`: Mode selection with type-safe enum output instead of strings

**Design note:** The `value_parser!` macro is the recommended entry point. Direct construction (`SomeParser::new()`) is primarily useful when composing parsers via `map`/`try_map`.

# Examples

**Example 1** (Section 4, FalseyValueParser doc): Boolean parsing with lenient false detection:

```rust
let value_parser = clap::builder::FalseyValueParser::new();
// Everything that isn't false-like is true:
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("100")).unwrap(), true);
// False-like values:
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("false")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("No")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("0")).unwrap(), false);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("")).unwrap(), false);
```

**Example 2** (Section 4, BoolishValueParser doc): Strict bool-like parsing:

```rust
let value_parser = clap::builder::BoolishValueParser::new();
// Rejects non-boolean strings:
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("random")).is_err());
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("100")).is_err());
// Accepts bool-like strings (case-insensitive):
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("Yes")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("oN")).unwrap(), true);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("oFF")).unwrap(), false);
```

**Example 3** (Section 4, RangedI64ValueParser doc): Range-bounded integer parsing:

```rust
let value_parser = clap::builder::RangedI64ValueParser::<i32>::new().range(-1..200);
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("-200")).is_err()); // out of range
assert!(value_parser.parse_ref(&cmd, arg, OsStr::new("300")).is_err());  // out of range
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("-1")).unwrap(), -1);
assert_eq!(value_parser.parse_ref(&cmd, arg, OsStr::new("50")).unwrap(), 50);
```

**Example 4** (Section 4, EnumValueParser doc): Parsing a `ValueEnum` type:

```rust
let mut cmd = clap::Command::new("raw")
    .arg(
        clap::Arg::new("color")
            .value_parser(clap::builder::EnumValueParser::<ColorChoice>::new())
            .required(true)
    );

let m = cmd.try_get_matches_from_mut(["cmd", "always"]).unwrap();
let color: ColorChoice = *m.get_one("color").expect("required");
assert_eq!(color, ColorChoice::Always);
```

# Relationships

## Builds Upon

- **typed-value-parser** — All built-in parsers implement the `TypedValueParser` trait
- **value-parser** — Built-in parsers are used via the `ValueParser` wrapper

## Enables

- (none)

## Related

- **arg** — Parsers are attached to arguments via `Arg::value_parser`
- **arg-matches** — The parser's output type determines what `get_one::<T>` returns
- **possible-value** — `PossibleValuesParser` and `EnumValueParser` use possible values for validation
- **value-enum-derive** — `EnumValueParser` works with types that derive `ValueEnum`

## Contrasts With

- (none)

# Common Errors

- **Error**: Using `RangedI64ValueParser` for negative values without enabling `Arg::allow_negative_numbers` or `Arg::allow_hyphen_values`.
  **Correction**: Clap interprets leading hyphens as flags by default. To accept negative numbers, chain `.allow_negative_numbers(true)` or `.allow_hyphen_values(true)` on the `Arg`.

- **Error**: Using `BoolishValueParser` when `FalseyValueParser` semantics are intended, causing unexpected rejections of inputs like `"random"`.
  **Correction**: `BoolishValueParser` is strict — it rejects any string that is not a recognized boolean representation. `FalseyValueParser` treats everything non-false as `true`.

# Common Confusions

- **Confusion**: Thinking all three boolean parsers are interchangeable.
  **Clarification**: They have very different semantics:
  - `BoolValueParser`: Only `"true"` and `"false"`
  - `BoolishValueParser`: Recognizes `true/yes/on/1` and `false/no/off/0` (rejects everything else)
  - `FalseyValueParser`: Only recognizes false values (`false/no/off/0/""`); everything else is `true`

- **Confusion**: Thinking `.value_parser(3000..4000)` produces `u16`.
  **Clarification**: Bare range literals create a `RangedI64ValueParser` that produces `i64`. To get a specific type like `u16`, use `value_parser!(u16).range(3000..)`.

# Source Reference

Section 4: Value Parsers, from `repos/clap/clap_builder/src/builder/value_parser.rs`, lines 900-2070. Covers `StringValueParser` (line 900), `OsStringValueParser` (line 948), `PathBufValueParser` (line 990), `EnumValueParser` (line 1040), `PossibleValuesParser` (line 1156), `RangedI64ValueParser` (line 1268), `RangedU64ValueParser` (line 1475), `BoolValueParser` (line 1672), `FalseyValueParser` (line 1736), `BoolishValueParser` (line 1831), `NonEmptyStringValueParser` (line 1932), `MapValueParser` (line 2010), `TryMapValueParser` (line 2069).

# Verification Notes

- All parser definitions: Directly from struct-level doc comments in the source
- Boolean parser semantics: Verified against the parse_ref assertion examples in the source for all three parsers
- Range parser note about negative numbers: Directly from the `RangedI64ValueParser` doc comment warning
- The `value_parser!` to parser mapping: Synthesized from source context and `ValueParserFactory` impls
- Confidence: HIGH — every parser has explicit documentation and behavioral examples in the source
- Cross-references: `value-parser`, `typed-value-parser`, `arg`, `arg-matches`, `possible-value`, `value-enum-derive` are planned or extracted by other agents
- Uncertainties: None
