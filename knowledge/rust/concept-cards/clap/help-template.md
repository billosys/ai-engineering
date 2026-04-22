---
# === CORE IDENTIFICATION ===
concept: Help Template
slug: help-template

# === CLASSIFICATION ===
category: builder-api
subcategory: null
tier: advanced

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
  - help_template
  - "Command::help_template"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - command
  - command-settings
extends: []
related:
  - help-generation
  - clap-styling
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I customize the help output format in clap?"
  - "What template tags are available for help templates?"
  - "How do I create a custom help layout?"
---

# Quick Definition

`help_template` is a `Command` method that overrides clap's default help layout using a string template with curly-brace tags like `{name}`, `{version}`, `{usage}`, and `{all-args}`.

# Core Definition

The `help_template` method "Sets the help template to be used, overriding the default format. Tags are given inside curly brackets." This is a command-specific setting (not propagated to subcommands), meaning each command can have its own help layout (command.rs, line 2246).

The template system uses curly-brace delimited tags that are replaced at render time with the corresponding content from the `Command` configuration.

# Prerequisites

- **command** -- `help_template` is a method on `Command`; understanding how to build a Command is needed.
- **command-settings** -- `help_template` is a command-specific setting; understanding the settings categories helps contextualize its scope.

# Key Properties

1. Template tags (all enclosed in curly brackets):
   - `{name}` -- display name for the (sub-)command
   - `{bin}` -- binary name (deprecated)
   - `{version}` -- version number
   - `{author}` -- author information
   - `{author-with-newline}` -- author followed by `\n`
   - `{author-section}` -- author preceded and followed by `\n`
   - `{about}` -- general description (from `Command::about` or `Command::long_about`)
   - `{about-with-newline}` -- about followed by `\n`
   - `{about-section}` -- about preceded and followed by `\n`
   - `{usage-heading}` -- automatically generated usage heading
   - `{usage}` -- automatically generated or given usage string
   - `{all-args}` -- help for all arguments including titles
   - `{options}` -- help for options only
   - `{positionals}` -- help for positional arguments only
   - `{subcommands}` -- help for subcommands only
   - `{tab}` -- standard tab size used within clap
   - `{after-help}` -- help from `Command::after_help` or `Command::after_long_help`
   - `{before-help}` -- help from `Command::before_help` or `Command::before_long_help`
2. This is a command-specific setting -- it does NOT propagate to subcommands
3. Each subcommand can define its own `help_template`
4. When not set, clap uses a sensible default layout

# Construction / Recognition

## To Create a Help Template:
1. Define a string containing the desired layout with template tags
2. Call `.help_template("your template string")` on a `Command`
3. Tags are replaced with the corresponding values at render time
4. Literal text outside tags is preserved as-is

## To Recognize Help Template Usage:
1. Look for `.help_template(...)` in Command builder chains
2. Look for curly-brace tags like `{name}`, `{all-args}`, `{usage}` in string literals

# Context & Application

Help templates are useful when the default clap help layout doesn't match the desired output format. Common reasons to customize include: reordering sections, adding custom branding, creating minimal help output, or matching the style of an existing CLI tool being ported to Rust.

**Related methods for help customization:**
- `before_help()` / `after_help()` -- add text without changing the layout
- `override_help()` -- completely replace the help with static text
- `override_usage()` -- replace only the usage line
- `flatten_help(true)` -- show subcommand summaries inline
- `next_help_heading()` -- group arguments under custom headings

# Examples

**Example 1** (command.rs, line 2246): Brief help template:
```rust
use clap::Command;

Command::new("myprog")
    .version("1.0")
    .help_template("{name} ({version}) - {usage}");
```

**Example 2** (command.rs, line 2246): Full application help template:
```rust
use clap::Command;

Command::new("myprog")
    .version("1.0")
    .help_template("\
{before-help}{name} {version}
{author-with-newline}{about-with-newline}
{usage-heading} {usage}

{all-args}{after-help}
");
```

# Relationships

## Builds Upon
- **command** -- `help_template` is a method on `Command`
- **command-settings** -- `help_template` is in the command-specific settings category

## Related
- **help-generation** -- help templates customize how auto-generated help is laid out
- **clap-styling** -- styles control the colors/formatting within the help template output

# Common Errors

- **Error**: Using an invalid tag name (e.g., `{desc}` instead of `{about}`).
  **Correction**: Only the documented tags are recognized. Invalid tags are rendered as literal text. Refer to the list of valid tags.

- **Error**: Setting `help_template` on the top-level command and expecting subcommands to use it.
  **Correction**: `help_template` is command-specific and does not propagate. Set it on each command individually.

- **Error**: Using `{bin}` instead of `{name}`.
  **Correction**: `{bin}` is deprecated. Use `{name}` for the display name of the command.

# Common Confusions

- **Confusion**: Thinking `help_template` and `override_help` do the same thing.
  **Clarification**: `help_template` provides a layout template with dynamic tag substitution. `override_help` replaces the entire help output with a static string (no auto-generation).

- **Confusion**: Expecting `{all-args}` and `{options}` + `{positionals}` + `{subcommands}` to be identical.
  **Clarification**: `{all-args}` includes all argument types with their section titles. The individual tags (`{options}`, `{positionals}`, `{subcommands}`) let you control their order and placement independently.

# Source Reference

Section 1: Core Concepts - Command, from `clap_builder/src/builder/command.rs`, method `help_template` at line 2246. Also references the `help_template.rs` output module for rendering (lines 878-977 of the source docs).

# Verification Notes

- Tag list: Enumerated directly from the method documentation at line 2246
- Deprecation of `{bin}`: Noted in source as "(deprecated)"
- Examples: Both taken directly from the source documentation
- Confidence: HIGH -- the method is explicitly documented with a complete tag reference and examples
- Cross-references: `help-generation` and `clap-styling` are in Agent 5's scope
