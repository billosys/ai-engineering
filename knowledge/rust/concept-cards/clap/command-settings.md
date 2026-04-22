---
# === CORE IDENTIFICATION ===
concept: Command Settings
slug: command-settings

# === CLASSIFICATION ===
category: builder-api
subcategory: null
tier: intermediate

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
  - application-wide settings
  - command-specific settings
  - subcommand-specific settings

# === TYPED RELATIONSHIPS ===
prerequisites:
  - command
extends: []
related:
  - subcommand
  - help-template
  - clap-styling
  - help-generation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the different categories of Command settings?"
  - "Which settings propagate to subcommands and which do not?"
  - "How do I control help, version, and error behavior in clap?"
  - "What application-wide settings does clap provide?"
---

# Quick Definition

Command settings are configuration methods on `Command` organized into three categories: application-wide settings (propagated to all subcommands), command-specific settings (applying only to the current command), and subcommand-specific settings (controlling how subcommands behave within a parent).

# Core Definition

The `Command` struct organizes its configuration into three distinct impl blocks with different propagation semantics:

1. **Application-wide Settings** (command.rs, line 1161): "These settings will apply to the top-level command and all subcommands, by default. Some settings can be overridden in subcommands."
2. **Command-specific Settings** (command.rs, line 1846): "These apply only to the current command and are not inherited by subcommands."
3. **Subcommand-specific Settings** (command.rs, line 2576): Settings that configure how subcommands are identified, displayed, and interact with the parent command.

# Prerequisites

- **command** -- Settings are methods on the `Command` struct; understanding `Command` is required.

# Key Properties

1. **Application-wide Settings** (propagated to subcommands):
   - `no_binary_name(bool)` -- do not assume first arg is binary name
   - `ignore_errors(bool)` -- try not to fail on parse errors
   - `args_override_self(bool)` -- later occurrences replace earlier ones
   - `dont_delimit_trailing_values(bool)` -- disable value delimiting after `--`
   - `color(ColorChoice)` -- when to use colored output
   - `styles(Styles)` -- terminal output styling
   - `term_width(usize)` / `max_term_width(usize)` -- help wrapping width
   - `disable_version_flag(bool)` -- remove auto-generated `--version`
   - `propagate_version(bool)` -- propagate version to subcommands
   - `next_line_help(bool)` -- put help text on the next line after the argument
   - `disable_help_flag(bool)` -- remove auto-generated `--help`
   - `disable_help_subcommand(bool)` -- remove auto-generated `help` subcommand
   - `disable_colored_help(bool)` -- disable colored help output
   - `help_expected(bool)` -- panic if an argument lacks help text
   - `hide_possible_values(bool)` -- don't show possible values in help
   - `infer_long_args(bool)` -- allow unambiguous prefix matching for long args
   - `infer_subcommands(bool)` -- allow unambiguous prefix matching for subcommands

2. **Command-specific Settings** (NOT propagated):
   - `name(str)` / `bin_name(str)` / `display_name(str)` -- naming
   - `author(str)` / `about(str)` / `long_about(str)` -- metadata
   - `version(str)` / `long_version(str)` -- version strings
   - `before_help(str)` / `after_help(str)` -- additional help text
   - `override_usage(str)` / `override_help(str)` -- replace auto-generated text
   - `help_template(str)` -- customize help layout
   - `flatten_help(bool)` -- show subcommand summaries in parent help
   - `next_help_heading(str)` -- group arguments under a custom heading
   - `arg_required_else_help(bool)` -- show help when no arguments given
   - `allow_missing_positional(bool)` -- allow skipping optional positionals

3. **Subcommand-specific Settings** (controlling subcommand behavior):
   - `short_flag(char)` / `long_flag(str)` -- invoke subcommand via flag syntax
   - `alias(str)` / `aliases([str])` -- hidden alternative names
   - `visible_alias(str)` / `visible_aliases([str])` -- shown alternative names
   - `display_order(usize)` / `hide(bool)` -- help display control
   - `subcommand_required(bool)` -- error if no subcommand given
   - `allow_external_subcommands(bool)` -- accept unknown subcommands
   - `args_conflicts_with_subcommands(bool)` -- prevent mixing args with subcommands
   - `subcommand_precedence_over_arg(bool)` -- stop greedy arg consumption at subcommand
   - `subcommand_negates_reqs(bool)` -- subcommand overrides parent requirements
   - `multicall(bool)` -- dispatch on binary name

# Construction / Recognition

## To Configure Settings:
1. Chain setting methods on a `Command` instance
2. Application-wide settings can go on the top-level command and will propagate
3. Command-specific settings must be set on each command individually
4. Subcommand-specific settings are set on the parent command that contains subcommands

## To Determine Setting Scope:
1. Check which impl block the method belongs to in the source
2. Look for "NOTE: This choice is propagated to all child subcommands" in the doc
3. Application-wide settings include the propagation note; command-specific settings do not

# Context & Application

Understanding the three-category organization is essential for correctly configuring multi-level CLI applications. A common mistake is setting a property like `help_template` on the top-level command and expecting it to apply to subcommands -- it won't, because it's a command-specific setting. Conversely, `styles` and `color` are application-wide and automatically propagate.

**Practical patterns:**
- Use `arg_required_else_help(true)` to show help when the user runs the program with no arguments
- Use `propagate_version(true)` to avoid setting version on every subcommand
- Use `help_expected(true)` during development to ensure all arguments have help text
- Use `infer_subcommands(true)` for user-friendly prefix matching (e.g., `git co` matching `git commit`)

# Examples

**Example 1** (command.rs, line 1166): Application-wide setting -- no binary name:
```rust
use clap::{Command, arg};

let m = Command::new("myprog")
    .no_binary_name(true)
    .arg(arg!(<cmd> ... "commands to run"))
    .get_matches_from(vec!["command", "set"]);
```

**Example 2** (command.rs, line 1332): Application-wide setting -- custom styles:
```rust
use clap::{Command, builder::styling};

const STYLES: styling::Styles = styling::Styles::styled()
    .header(styling::AnsiColor::Green.on_default().bold())
    .usage(styling::AnsiColor::Green.on_default().bold())
    .literal(styling::AnsiColor::Blue.on_default().bold())
    .placeholder(styling::AnsiColor::Cyan.on_default());

Command::new("myprog").styles(STYLES).get_matches();
```

**Example 3** (command.rs, line 2388): Command-specific setting -- help on no args:
```rust
use clap::Command;

Command::new("myprog")
    .arg_required_else_help(true);
```

# Relationships

## Builds Upon
- **command** -- settings are methods on the `Command` struct

## Related
- **subcommand** -- subcommand-specific settings control subcommand behavior
- **help-template** -- `help_template()` is a command-specific setting for customizing help layout
- **clap-styling** -- `styles()` is an application-wide setting for terminal output appearance
- **help-generation** -- many settings control how help is generated and displayed

# Common Errors

- **Error**: Setting `disable_help_flag(true)` without providing a custom help mechanism.
  **Correction**: When disabling the auto-generated `--help`, you must provide your own help argument or the user will have no way to access help.

- **Error**: Setting `term_width` or `max_term_width` without the `wrap_help` feature flag.
  **Correction**: These settings require the `wrap_help` feature to be enabled.

- **Error**: Expecting `infer_subcommands` to work with ambiguous prefixes.
  **Correction**: Inference only works when the prefix uniquely identifies a single subcommand. Ambiguous prefixes still produce errors.

# Common Confusions

- **Confusion**: Thinking all settings propagate to subcommands.
  **Clarification**: Only settings in the "Application-wide Settings" category propagate. Command-specific settings like `about`, `version`, `help_template`, and `override_usage` do NOT propagate.

- **Confusion**: Confusing `disable_help_flag` with `disable_help_subcommand`.
  **Clarification**: `disable_help_flag` removes the `--help`/`-h` flag. `disable_help_subcommand` removes the auto-generated `help` subcommand. They are independent.

- **Confusion**: Thinking `term_width` is per-command.
  **Clarification**: `term_width` and `max_term_width` apply globally, not on a per-command basis, even though they are in the application-wide settings section.

# Source Reference

Section 1: Core Concepts - Command, from `clap_builder/src/builder/command.rs`. Application-wide Settings impl at line 1161, Command-specific Settings impl at line 1846, Subcommand-specific Settings impl at line 2576. Reflection (getter methods) impl at line 3706.

# Verification Notes

- Category descriptions: Directly quoted from impl block doc comments
- Propagation behavior: Confirmed via "NOTE" annotations in individual method docs
- Setting lists: Enumerated from method headers in each impl block
- Confidence: HIGH -- the three-category organization is explicitly documented with clear propagation semantics
- Cross-references: `clap-styling` and `help-generation` are in Agent 5's scope
