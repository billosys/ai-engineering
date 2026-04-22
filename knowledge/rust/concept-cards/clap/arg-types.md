---
# === CORE IDENTIFICATION ===
concept: Argument Types
slug: arg-types

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
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - "argument kinds"
  - "flags vs options vs positional"
  - "flag"
  - "option"
  - "positional argument"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - arg
  - arg-action
extends: []
related:
  - command
  - arg-matches
  - value-parser
  - clap-builder-api
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the three kinds of command-line arguments in clap?"
  - "How does clap distinguish between a flag, an option, and a positional argument?"
  - "How do I create a flag in clap?"
  - "How do I create an option that takes a value?"
  - "How do positional arguments work in clap?"
---

# Quick Definition

Clap recognizes three kinds of command-line arguments: **flags** (boolean switches like `--verbose`), **options** (named arguments that take values like `--config file.toml`), and **positional arguments** (unnamed values identified by position like `<FILE>`). All three are represented by the `Arg` struct; their kind is determined by the presence of `short`/`long` names and the configured action.

# Core Definition

The source does not define a separate type or enum for argument kinds. Instead, the distinction emerges from the `Arg` struct's configuration. The `Arg::new()` documentation states: "By default, an Arg is Positional, see `Arg::short` or `Arg::long` to turn it into an option. Accept a single value, see `Arg::action` to override this" (arg.rs, line 96). The `is_positional()` reflection method returns `true` if the argument has no `short` or `long` name set (arg.rs, line 4415).

The three kinds:
1. **Positional arguments**: No `short` or `long` set. Identified by position in the command line. Example: `program file.txt` where `file.txt` is positional.
2. **Options**: Have `short` and/or `long` set, with an action that takes values (`ArgAction::Set` or `ArgAction::Append`). Example: `--config file.toml` or `-c file.toml`.
3. **Flags**: Have `short` and/or `long` set, with an action that does NOT take values (`ArgAction::SetTrue`, `ArgAction::SetFalse`, or `ArgAction::Count`). Example: `--verbose` or `-v`.

# Prerequisites

- **arg** -- Understanding the Arg struct is necessary to understand how the three kinds are configured.
- **arg-action** -- The action determines whether a named argument is a flag (no value) or an option (takes a value).

# Key Properties

1. **Positional arguments** are the default: `Arg::new("name")` with no `short`/`long` is positional
2. **Adding `.short()` or `.long()` converts a positional into a named argument** (option or flag)
3. **The action determines flag vs option**: `SetTrue`/`SetFalse`/`Count` make a flag; `Set`/`Append` make an option
4. **Positional arguments are ordered**: they are matched by position among other positionals, not by position in the overall argument list
5. **Positional index starts at 1**: set explicitly with `.index(N)` or assigned automatically in order of definition
6. **Only the last positional may accept a variable number of values** (via `.num_args(1..)`)
7. **Flags do not consume values from the command line**: `--verbose` is complete on its own
8. **Options consume one or more following values**: `--config file.toml` consumes `file.toml`
9. **Short flags can be combined**: `-v -d` can be written as `-vd`
10. **Options accept values via space, equals, or adjacent**: `-c file`, `-c=file`, `-cfile` are all valid

# Construction / Recognition

## To Create a Positional Argument:
1. `Arg::new("input")` -- no `short`/`long` means positional
2. Optionally set `.index(1)` for explicit ordering
3. The name is used as the display name in help: `<input>`

## To Create a Flag:
1. `Arg::new("verbose").short('v').long("verbose")`
2. Set `.action(ArgAction::SetTrue)` for a boolean flag
3. Or `.action(ArgAction::Count)` for a counting flag (e.g., `-vvv`)
4. Retrieve with `matches.get_flag("verbose")` or `matches.get_count("verbose")`

## To Create an Option:
1. `Arg::new("config").short('c').long("config")`
2. Set `.action(ArgAction::Set)` (this is the default)
3. Set `.value_name("FILE")` for the help placeholder
4. Retrieve with `matches.get_one::<String>("config")`

## To Distinguish at Runtime:
1. Call `arg.is_positional()` -- returns `true` if no `short`/`long` is set
2. Check `arg.get_short()` and `arg.get_long()` for named argument names
3. The action's `takes_values()` method distinguishes flags from options

# Context & Application

Understanding the three argument kinds is fundamental to designing a CLI with clap. The distinction drives how the parser interprets tokens on the command line:

- **Positional arguments** are consumed in order -- they are the "bare" values without any prefix
- **Named arguments** (options and flags) are identified by their `-` or `--` prefix
- The `--` separator forces everything after it to be treated as positional, even if it starts with `-`

**Common CLI patterns:**
- `grep PATTERN FILE` -- two positional arguments
- `ls -la --color=auto` -- flags (`-l`, `-a`) and an option (`--color`)
- `cargo build --release --target x86_64` -- a flag (`--release`) and an option (`--target`)

**Design guidance from the source:** The `required` method documentation explicitly advises against making flags required: "Flags shouldn't be required by default. This is because if a flag were to be required, it should simply be implied. No additional information is required from user" (arg.rs, line 697).

# Examples

**Example 1** (arg.rs, line 96): Positional argument (default):
```rust
use clap::{Command, Arg};

let m = Command::new("prog")
    .arg(Arg::new("input"))  // positional by default
    .get_matches_from(vec!["prog", "myfile.txt"]);

assert_eq!(m.get_one::<String>("input").unwrap(), "myfile.txt");
```

**Example 2** (arg.rs, line 135): Option with short and long:
```rust
use clap::{Command, Arg, ArgAction};

let m = Command::new("prog")
    .arg(Arg::new("config")
        .short('c')
        .long("config")
        .action(ArgAction::Set))
    .get_matches_from(vec!["prog", "-c", "file.toml"]);

assert_eq!(m.get_one::<String>("config").map(String::as_str), Some("file.toml"));
```

**Example 3** (arg.rs, line 469): Positional and flag together:
```rust
use clap::{Command, Arg, ArgAction};

let m = Command::new("prog")
    .arg(Arg::new("mode").index(1))
    .arg(Arg::new("debug").long("debug").action(ArgAction::SetTrue))
    .get_matches_from(vec!["prog", "--debug", "fast"]);

// index(1) means "first positional", not "first argument"
assert_eq!(m.get_one::<String>("mode").unwrap(), "fast");
assert_eq!(m.get_flag("debug"), true);
```

**Example 4** (arg.rs, line 4415): Checking if an argument is positional:
```rust
use clap::Arg;

let arg = Arg::new("foo");
assert_eq!(arg.is_positional(), true);

let arg = Arg::new("foo").long("foo");
assert_eq!(arg.is_positional(), false);
```

# Relationships

## Builds Upon
- **arg** -- All three argument kinds use the same `Arg` struct
- **arg-action** -- The action is what distinguishes flags from options

## Enables
- **arg-matches** -- Different argument kinds are retrieved differently from ArgMatches

## Related
- **command** -- Arguments of all kinds are added to a Command
- **value-parser** -- Options and positionals use value parsers for type conversion
- **clap-builder-api** -- Argument kind is a fundamental builder API concept

# Common Errors

- **Error**: Defining an option with `ArgAction::Set` (the default) but forgetting to provide a value on the command line.
  **Correction**: Options with `Set` require a value. If you want a flag, use `ArgAction::SetTrue`.

- **Error**: Defining a variable-length positional (`.num_args(1..)`) that is not the last positional, causing a panic.
  **Correction**: Only the last positional argument may accept a variable number of values.

- **Error**: Expecting positional arguments to be parsed in order of the overall argument list rather than among other positionals.
  **Correction**: The index is relative to other positionals only. `--flag` tokens are parsed separately and do not affect positional indexing.

# Common Confusions

- **Confusion**: Believing there is a separate type or enum for flags, options, and positional arguments.
  **Clarification**: All three are represented by `Arg`. The distinction is purely configurational: presence/absence of `short`/`long` and the chosen `ArgAction`.

- **Confusion**: Thinking an argument with only `.short()` but no `.long()` might still be positional.
  **Clarification**: Setting either `short` or `long` makes the argument a named argument (option or flag), never positional.

- **Confusion**: Assuming `--flag value` means `value` is consumed by `flag`.
  **Clarification**: Whether `value` is consumed depends on the action. With `ArgAction::SetTrue` (a flag), `value` is NOT consumed and would be treated as a positional or cause an error. With `ArgAction::Set` (an option), `value` IS consumed.

# Source Reference

Section 2: Arguments (Arg), from `clap_builder/src/builder/arg.rs`. The three-kind distinction is implicit across the Arg API. Key methods: `Arg::new` (line 96, documents default as positional), `Arg::short` (line 135), `Arg::long` (line 192), `Arg::index` (line 469), `Arg::is_positional` (line 4415), `Arg::required` (line 697, guidance on flag requirements).

# Verification Notes

- Default behavior: "By default, an Arg is Positional" -- directly quoted from Arg::new docs (line 96)
- is_positional: Verified from source at line 4415, returns true when no short/long is set
- Flag vs option distinction: Synthesized from the interaction of `short`/`long` and `ArgAction` -- the source does not have a single definition but the behavior is demonstrated across multiple examples
- Required flag guidance: Direct quote from `required` method docs (line 697)
- Positional indexing: "The index refers to position according to other positional argument" -- direct from `index` docs (line 469)
- Confidence: MEDIUM -- the three-kind taxonomy is not explicitly defined as a concept in the source; it is synthesized from the behavior of `short`, `long`, `action`, and `is_positional` methods
- Cross-references: All slugs verified against planned extractions
