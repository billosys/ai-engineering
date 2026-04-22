---
# === CORE IDENTIFICATION ===
concept: Command
slug: command

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
section: "Core Concepts - Command"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "clap::Command"
  - "clap_builder::Command"
  - App

# === TYPED RELATIONSHIPS ===
prerequisites:
  - clap-crate
extends: []
related:
  - arg
  - arg-group
  - arg-matches
  - clap-builder-api
  - subcommand
  - command-settings
  - help-template
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Command struct in clap?"
  - "How do I define a CLI application using clap's builder API?"
  - "What are the main method categories on Command?"
  - "How do I parse command-line arguments with Command?"
---

# Quick Definition

`Command` is the central struct in clap's builder API for defining a command-line interface. It holds argument definitions, subcommands, parser behavior settings, and help output configuration, and provides the `get_matches` family of methods to trigger runtime parsing.

# Core Definition

The `Command` struct is documented as the type used to "Build a command-line interface. This includes defining arguments, subcommands, parser behavior, and help output. Once all configuration is complete, the `Command::get_matches` family of methods starts the runtime-parsing process. These methods then return information about the user supplied arguments (or lack thereof)." When deriving a `Parser`, you can use `CommandFactory::command` to access the underlying `Command` (command.rs, line 36).

The struct organizes its API into five sections:
- **Basic API** -- `new`, `arg`, `args`, `subcommand`, `group`, `get_matches` and variants
- **Application-wide Settings** -- settings propagated to all subcommands
- **Command-specific Settings** -- settings applying only to the current command
- **Subcommand-specific Settings** -- settings controlling subcommand behavior
- **Reflection** -- getters for inspecting the configured command

# Prerequisites

- **clap-crate** -- Command is part of the clap crate; understanding the crate's purpose and APIs is needed to use it in context.

# Key Properties

1. Created with `Command::new(name)` where the name is typically the binary name
2. Arguments are added via `.arg()` and `.args()` methods, accepting `Arg` values
3. Subcommands are added via `.subcommand()` and `.subcommands()`, accepting nested `Command` values
4. Argument groups are added via `.group()` and `.groups()`
5. Parsing is triggered by `.get_matches()` (exits on error) or `.try_get_matches()` (returns `Result`)
6. `.get_matches_from()` variants accept custom iterators instead of reading `env::args_os`
7. `.try_get_matches_from_mut()` does not consume the `Command`, allowing re-use
8. `.debug_assert()` validates the command configuration in debug builds
9. Help and version output can be rendered without parsing via `.render_help()`, `.render_version()`, `.render_usage()`
10. Supports lazy initialization of subcommand definitions via `.defer()`

# Construction / Recognition

## To Build a Command:
1. Call `Command::new("program_name")` to create the command
2. Chain `.version()`, `.author()`, `.about()` for metadata
3. Add arguments with `.arg(Arg::new("name").short('n')...)`
4. Add subcommands with `.subcommand(Command::new("sub")...)`
5. Configure settings (e.g., `.color()`, `.styles()`, `.help_template()`)
6. Call `.get_matches()` or `.try_get_matches()` to parse

## To Recognize Command Usage:
1. Look for `Command::new(...)` as the entry point
2. Chained method calls (`.arg()`, `.subcommand()`, `.version()`, etc.)
3. Terminates with a `get_matches` variant

# Context & Application

`Command` is the heart of clap's builder API. Every CLI application using clap's builder pattern starts by constructing a `Command`. The struct uses the builder pattern extensively -- nearly every method returns `Self` for chaining. For derive API users, the `Command` is generated automatically but can be accessed via `CommandFactory::command()` for customization.

**Key design decisions:**
- The first argument to `get_matches_from` is assumed to be the binary name (configurable via `no_binary_name`)
- Contradictory argument/setting configurations cause panics in debug builds
- `try_get_matches` does NOT auto-exit on `--help`/`--version` -- it returns errors that the caller must handle

# Examples

**Example 1** (command.rs, line 36): Basic Command construction:
```rust
use clap::{Command, Arg};

let m = Command::new("My Program")
    .author("Me, me@mail.com")
    .version("1.0.2")
    .about("Explains in brief what the program does")
    .arg(Arg::new("in_file"))
    .after_help("Longer explanation to appear after the options when \
        displaying the help information from --help or -h")
    .get_matches();
```

**Example 2** (command.rs, line 148): Adding arguments:
```rust
use clap::{Command, arg, Arg};

Command::new("myprog")
    .arg(
        Arg::new("debug")
            .short('d')
            .help("turns on debugging mode")
    )
    .arg(
        arg!(-c --config <CONFIG> "Optionally sets a config file to use")
    );
```

**Example 3** (command.rs, line 693): Non-exiting parse with error handling:
```rust
use clap::{Command, Arg};

let matches = Command::new("myprog")
    .try_get_matches()
    .unwrap_or_else(|e| e.exit());
```

# Relationships

## Builds Upon
- **clap-crate** -- Command is the primary type in the clap crate

## Enables
- **arg-matches** -- `get_matches()` returns `ArgMatches` containing parsed results
- **subcommand** -- subcommands are nested `Command` instances
- **help-generation** -- Command drives automatic help output

## Related
- **arg** -- arguments are added to Command via `.arg()`
- **arg-group** -- argument groups are added via `.group()`
- **clap-builder-api** -- Command is the central type in the builder pattern
- **command-factory-trait** -- bridges the derive API to Command
- **command-settings** -- configurable behaviors on Command
- **help-template** -- customizes Command's help output format

# Common Errors

- **Error**: Calling `.get_matches()` in a test or library context where process exit is undesirable.
  **Correction**: Use `.try_get_matches_from()` which returns a `Result` instead of exiting.

- **Error**: Forgetting that `try_get_matches` does not exit on `--help`/`--version`.
  **Correction**: Match on `ErrorKind::DisplayHelp` and `ErrorKind::DisplayVersion` and call `Error::exit()` or `std::process::exit()`.

- **Error**: Calling `.mut_arg("name", ...)` with an argument name that was never added.
  **Correction**: `mut_arg` panics if the argument is undefined. Ensure the argument was previously added with `.arg()`.

# Common Confusions

- **Confusion**: Thinking `Command::new("name")` sets the binary filename.
  **Clarification**: The name is only used for display purposes in help and version output. It does not change the actual binary name on disk.

- **Confusion**: Assuming all `get_matches` variants behave the same on `--help`.
  **Clarification**: `get_matches()` and `get_matches_from()` auto-exit. `try_get_matches()` and `try_get_matches_from()` return an `Error` with kind `DisplayHelp` that the caller must handle.

- **Confusion**: Believing Command settings always apply to subcommands.
  **Clarification**: Only "Application-wide Settings" propagate to subcommands. "Command-specific Settings" (name, about, version, help_template, etc.) apply only to the current command.

# Source Reference

Section 1: Core Concepts - Command, from `clap_builder/src/builder/command.rs`. Struct definition at line 36. Impl blocks: Basic API (line 115), Application-wide Settings (line 1161), Command-specific Settings (line 1846), Subcommand-specific Settings (line 2576), Reflection (line 3706).

# Verification Notes

- Definition: Directly quoted from the struct-level documentation at line 36
- API organization: The five impl-block headings are taken verbatim from source comments
- `try_get_matches` behavior: Explicitly documented warning in source
- Confidence: HIGH -- the struct is extensively documented with clear descriptions and examples
- Cross-references: All slugs reference planned cards in this or other agent extraction sets
