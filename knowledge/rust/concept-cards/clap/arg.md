---
# === CORE IDENTIFICATION ===
concept: Arg
slug: arg

# === CLASSIFICATION ===
category: builder-api
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Arguments (Arg)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "clap::Arg"
  - "clap_builder::Arg"
  - "argument"
  - "CLI argument"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - command
extends: []
related:
  - arg-action
  - arg-group
  - arg-types
  - arg-settings
  - arg-matches
  - value-parser
  - value-hint
  - clap-builder-api
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Arg struct in clap?"
  - "How do I define a command-line argument using clap's builder API?"
  - "What are the main configuration categories on Arg?"
  - "How does Arg differ from a positional argument, option, or flag?"
  - "What is the relationship between Arg and Command?"
---

# Quick Definition

`Arg` is the struct that represents an individual command-line argument in clap's builder API. It defines the name, kind (flag, option, or positional), value handling, help text, and relationship rules for a single argument in the CLI.

# Core Definition

The source documents `Arg` as "the abstract representation of a command line argument. Used to set all the options and relationships that define a valid argument for the program." There are two ways to construct an `Arg`: using the builder pattern with manual method chaining, or using the `arg!` macro for a more concise usage-string syntax. You can also combine both approaches (arg.rs, line 31).

The struct organizes its builder methods into five documented categories:
- **Basic API** -- `new`, `id`, `short`, `long`, `alias`, `index`, `required`, `requires`, `exclusive`, `global`, `action`
- **Value Handling** -- `action`, `value_parser`, `num_args`, `value_name`, `value_delimiter`, `default_value`, `env`
- **Help** -- `help`, `long_help`, `display_order`, `help_heading`, `hide`, `hide_possible_values`
- **Advanced Argument Relations** -- `group`, `default_value_if`, `required_unless_present`, `required_if_eq`, `requires_if`, `conflicts_with`, `overrides_with`
- **Reflection** -- getters like `get_id`, `get_short`, `get_long`, `get_default_values`, `is_positional`

# Prerequisites

- **command** -- Arguments are added to a `Command` via `.arg()` and `.args()`; understanding Command is required to use Arg in context.

# Key Properties

1. Created with `Arg::new(name)` where the name uniquely identifies the argument
2. By default, an `Arg` is positional and accepts a single value; adding `.short()` or `.long()` turns it into a named option or flag
3. The argument kind (flag, option, positional) is determined by the presence of `short`/`long` and the action
4. Uses builder pattern -- nearly every method returns `Self` for chaining
5. The `.action()` method controls parsing behavior (Set, Append, SetTrue, Count, etc.)
6. The `.value_parser()` method controls type parsing and validation
7. `.required(true)` makes the argument mandatory; positional arguments default to required if there is no default value
8. `.num_args()` controls how many values are parsed per occurrence
9. `.env()` allows reading a value from an environment variable as a fallback
10. `.conflicts_with()` and `.requires()` establish inter-argument relationships
11. The argument name is also used as the display name for positional arguments in help output

# Construction / Recognition

## To Define an Arg with the Builder Pattern:
1. Call `Arg::new("name")` with a unique identifier
2. Optionally add `.short('c')` and/or `.long("config")` to make it a named argument
3. Set the action with `.action(ArgAction::Set)` or `.action(ArgAction::SetTrue)` etc.
4. Optionally set `.value_parser(...)` for typed parsing
5. Add `.help("description")` for help text
6. Set `.required(true)` if the argument must be present
7. Add to a command with `Command::new("prog").arg(arg)`

## To Define an Arg with the Macro:
1. Use `arg!(-c --config <FILE> "description")` for a short+long option
2. Use `arg!(<INPUT> "description")` for a required positional argument
3. Use `arg!([OUTPUT] "description")` for an optional positional argument

## To Recognize Argument Kind:
1. Has `.short()` or `.long()` with `ArgAction::SetTrue` -> flag
2. Has `.short()` or `.long()` with `ArgAction::Set` -> option (takes a value)
3. Has neither `.short()` nor `.long()` -> positional argument

# Context & Application

`Arg` is one of the two foundational types in clap's builder API (alongside `Command`). Every command-line parameter your program accepts is represented by an `Arg` instance. The struct follows clap's design philosophy of being a flexible builder that configures every aspect of argument behavior: parsing, validation, help display, and inter-argument relationships.

**Typical usage pattern:**
- Define each argument as an `Arg`, configure it via chained methods, then add it to a `Command`
- Use `ArgAction` to control how the parser reacts when it encounters the argument
- Use `value_parser` to control what types are accepted and how they are validated
- Use relationship methods (`requires`, `conflicts_with`, `required_if_eq`) to express complex validation rules

**Design note:** The name passed to `Arg::new()` serves multiple purposes: it is the lookup key in `ArgMatches`, the display name for positional arguments in help/usage, and the identifier used in relationship rules.

# Examples

**Example 1** (arg.rs, line 31): Builder pattern argument definition:
```rust
use clap::{Arg, arg, ArgAction};

let cfg = Arg::new("config")
    .short('c')
    .long("config")
    .action(ArgAction::Set)
    .value_name("FILE")
    .help("Provides a config file to myprog");
```

**Example 2** (arg.rs, line 31): Usage-string macro equivalent:
```rust
use clap::arg;

let input = arg!(-i --input <FILE> "Provides an input file to the program");
```

**Example 3** (arg.rs, line 469): Positional argument with explicit index:
```rust
use clap::{Command, Arg, ArgAction};

let m = Command::new("prog")
    .arg(Arg::new("mode").index(1))
    .arg(Arg::new("debug").long("debug").action(ArgAction::SetTrue))
    .get_matches_from(vec!["prog", "--debug", "fast"]);

assert_eq!(m.get_one::<String>("mode").unwrap(), "fast");
```

**Example 4** (arg.rs, line 763): Argument requirements:
```rust
use clap::{Command, Arg, ArgAction};

let res = Command::new("prog")
    .arg(Arg::new("cfg")
        .action(ArgAction::Set)
        .requires("input")
        .long("config"))
    .arg(Arg::new("input"))
    .try_get_matches_from(vec!["prog", "--config", "file.conf"]);
// Error: "input" is required when "config" is used
assert!(res.is_err());
```

# Relationships

## Builds Upon
- **command** -- Arguments are always added to a `Command`

## Enables
- **arg-matches** -- After parsing, argument values are accessed via `ArgMatches`
- **arg-types** -- The Arg struct is how flags, options, and positional arguments are all defined

## Related
- **arg-action** -- Controls parsing behavior when the argument is encountered
- **arg-group** -- Groups of Args can be validated together
- **arg-settings** -- Low-level per-argument boolean settings
- **value-parser** -- Configures typed parsing and validation
- **value-hint** -- Hints for shell completion
- **clap-builder-api** -- Arg is a core type in the builder pattern
- **possible-value** -- Enumerates allowed values for an argument

## Contrasts With
- **command** -- Command defines the application; Arg defines an individual parameter

# Common Errors

- **Error**: Defining a positional argument but also setting `.short()` or `.long()`, expecting it to still be positional.
  **Correction**: Adding `short` or `long` converts a positional into a named option/flag. To keep it positional, omit `short`/`long`.

- **Error**: Using `.num_args(0..)` with a positional argument after it, causing the parser to consume the positional's value.
  **Correction**: Use a fixed count, a delimiter, or `ArgAction::Append` to control where the option's values end.

- **Error**: Not specifying `.action(ArgAction::Set)` for an option that takes a value, relying on the default.
  **Correction**: While `Set` is the default action, being explicit about the action makes the intent clear, especially when distinguishing flags from options.

# Common Confusions

- **Confusion**: Believing that the name in `Arg::new("name")` must match the long flag.
  **Clarification**: The name is an internal identifier used in `ArgMatches` lookups and relationship rules. The long flag is set separately via `.long("flag-name")` and can differ.

- **Confusion**: Thinking `.required(true)` is needed for flags.
  **Clarification**: Flags are boolean switches -- requiring them would mean the user must always pass them, which defeats their purpose. The source explicitly recommends against this except for destructive operations.

- **Confusion**: Assuming `.index(1)` means "first argument on the command line."
  **Clarification**: The index refers to position among other positional arguments only, not position in the overall argument list. Named arguments (options/flags) are not counted.

# Source Reference

Section 2: Arguments (Arg), from `clap_builder/src/builder/arg.rs`. Struct definition at line 31. Impl blocks: Basic API (line 94), Value Handling (line 953), Help (line 2216), Advanced Argument Relations (line 2843), Reflection (line 4165).

# Verification Notes

- Definition: Directly quoted from the struct-level documentation at line 31
- API organization: Five impl-block headings taken from source comments
- Default behavior: "By default, an Arg is positional" is explicit in Arg::new docs (line 96)
- Required flag advice: Taken verbatim from the `required` method docs (line 697)
- Index clarification: Explicitly documented in `index` method docs (line 469)
- Confidence: HIGH -- the struct is extensively documented with clear descriptions and copious examples
- Cross-references: All slugs verified against other agent extraction sets
