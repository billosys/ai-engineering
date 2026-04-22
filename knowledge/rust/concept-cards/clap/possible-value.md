---
concept: PossibleValue
slug: possible-value
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
  - "PossibleValue"
  - "possible value"
  - "PossibleValuesParser"
  - "enumerated values"
prerequisites:
  - value-parser
extends: []
related:
  - arg
  - value-enum-derive
  - typed-value-parser
  - shell-completions
contrasts_with: []
answers_questions:
  - "How do I restrict an argument to a set of allowed values in clap?"
  - "What is PossibleValue and when should I use it instead of plain strings?"
  - "How do I add help text or aliases to possible values?"
---

# Quick Definition

`PossibleValue` represents a single allowed value for an argument, optionally with a help description, hidden aliases, and a visibility flag. `PossibleValuesParser` uses a collection of `PossibleValue` instances to restrict and validate argument input against an enumerated set.

# Core Definition

`PossibleValue` is "a possible value of an argument" that is "used for specifying possible values of Args." The source notes that "most likely you can use strings, rather than `PossibleValue` as it is only required to hide single values from help messages and shell completions or to attach help to possible values." Each `PossibleValue` has a name (used for matching), optional help text (shown in completions), a hide flag (to exclude from help/completions), and hidden aliases (alternative names that are accepted but not displayed). `PossibleValuesParser` is the corresponding parser that verifies input against a set of `PossibleValue` entries and returns a `String` (Clap Documentation, Section 4: Value Parsers).

# Prerequisites

- **value-parser** — `PossibleValuesParser` is a specific kind of `ValueParser` for enumerated values; understanding the parser system is needed

# Key Properties

1. Created via `PossibleValue::new("name")` — the name is used for matching and display
2. `.help("description")` adds a short help string shown in completions where supported
3. `.hide(true)` hides the value from help messages and shell completions while still accepting it
4. `.alias("alt")` and `.aliases(["alt1", "alt2"])` add hidden alternative names that are accepted during parsing
5. `.matches(value, ignore_case)` tests whether a string matches this value's name or any alias
6. `PossibleValuesParser::new(["a", "b", "c"])` creates a parser from an iterable of values
7. String arrays passed to `Arg::value_parser` are automatically converted to `PossibleValuesParser`
8. The output type of `PossibleValuesParser` is always `String`

# Construction / Recognition

## To Define PossibleValues with Help or Aliases

1. Create values: `PossibleValue::new("fast")`, `PossibleValue::new("slow").help("slower than fast")`
2. Hide secret values: `PossibleValue::new("secret speed").hide(true)`
3. Add aliases: `PossibleValue::new("slow").alias("not-fast")`
4. Pass to the argument: `.value_parser([PossibleValue::new("fast"), PossibleValue::new("slow").help("...")])`

## To Use Simple String Enumeration (No Help/Aliases Needed)

1. Pass a string array directly: `.value_parser(["always", "auto", "never"])`
2. This is automatically converted to a `PossibleValuesParser`
3. Retrieve the selected value: `matches.get_one::<String>("arg")`

## To Use PossibleValuesParser Explicitly

1. Construct: `PossibleValuesParser::new(["always", "auto", "never"])`
2. Pass to argument: `.value_parser(PossibleValuesParser::new(...))`

# Context & Application

`PossibleValue` and `PossibleValuesParser` are used when an argument accepts a fixed set of string values, like `--color always|auto|never`. For simple cases, string arrays are sufficient. `PossibleValue` becomes necessary when you need per-value help text (for richer shell completions), hidden values (accepted but not advertised), or aliases (alternative spellings).

**Typical contexts:**

- CLI arguments with mode selection: `--output json|yaml|toml`
- Color mode flags: `--color always|auto|never`
- Values with deprecated names that should still be accepted via aliases
- Secret or experimental modes hidden from help output

**Alternative:** For Rust enums, prefer `EnumValueParser` with `ValueEnum` derive, which provides the same functionality with type-safe enum variants instead of strings.

# Examples

**Example 1** (Section 4, PossibleValue struct doc): Defining possible values with help text and a hidden value:

```rust
let cfg = Arg::new("config")
    .action(ArgAction::Set)
    .value_name("FILE")
    .value_parser([
        PossibleValue::new("fast"),
        PossibleValue::new("slow").help("slower than fast"),
        PossibleValue::new("secret speed").hide(true)
    ]);
```

**Example 2** (Section 4, PossibleValue::matches doc): Testing whether a value matches, including case-insensitive matching:

```rust
let arg_value = PossibleValue::new("fast").alias("not-slow");

assert!(arg_value.matches("fast", false));
assert!(arg_value.matches("not-slow", false));
assert!(arg_value.matches("FAST", true));   // case-insensitive
assert!(!arg_value.matches("FAST", false));  // case-sensitive
```

**Example 3** (Section 4, PossibleValuesParser struct doc): Using `PossibleValuesParser` explicitly:

```rust
let mut cmd = clap::Command::new("raw")
    .arg(
        clap::Arg::new("color")
            .value_parser(
                clap::builder::PossibleValuesParser::new(["always", "auto", "never"])
            )
            .required(true)
    );

let m = cmd.try_get_matches_from_mut(["cmd", "always"]).unwrap();
let color: &String = m.get_one("color").expect("required");
assert_eq!(color, "always");
```

# Relationships

## Builds Upon

- **value-parser** — `PossibleValuesParser` is a specific `TypedValueParser` implementation

## Enables

- (none)

## Related

- **arg** — Possible values constrain what an `Arg` accepts
- **value-enum-derive** — The derive-based alternative for enum types with possible values
- **typed-value-parser** — `PossibleValuesParser` implements `TypedValueParser`
- **shell-completions** — `PossibleValue` help text and visibility affect shell completion output

## Contrasts With

- (none)

# Common Errors

- **Error**: Using `PossibleValue` when simple strings would suffice, adding unnecessary complexity.
  **Correction**: As the source notes, "most likely you can use strings, rather than `PossibleValue`." Only use `PossibleValue` when you need help text, hidden values, or aliases.

- **Error**: Expecting `PossibleValuesParser` to return a typed enum variant.
  **Correction**: `PossibleValuesParser` always returns `String`. For typed enum output, use `EnumValueParser` with a `ValueEnum` type.

# Common Confusions

- **Confusion**: Thinking `PossibleValue::hide(true)` prevents the value from being accepted.
  **Clarification**: `hide` only controls visibility in help and completions. Hidden values are still accepted during parsing.

- **Confusion**: Thinking aliases appear in help output.
  **Clarification**: Aliases are always hidden. They provide alternative accepted spellings but never appear in help messages or completions.

# Source Reference

Section 4: Value Parsers, from `repos/clap/clap_builder/src/builder/possible_value.rs`, lines 6-210, and `repos/clap/clap_builder/src/builder/value_parser.rs`, lines 1156-1210 (PossibleValuesParser). Covers PossibleValue struct, `new`, `help`, `hide`, `alias`, `aliases`, reflection methods, and `matches`.

# Verification Notes

- Definition: Directly quoted from the struct-level doc comment on `PossibleValue` (line 6)
- The "most likely you can use strings" note: Direct quotation from the source
- PossibleValuesParser semantics: Documented with usage and semantics examples
- Confidence: HIGH — explicit definition with code examples for all methods
- Cross-references: `value-parser`, `arg`, `value-enum-derive`, `typed-value-parser`, `shell-completions` are planned or extracted by other agents
- Uncertainties: None
