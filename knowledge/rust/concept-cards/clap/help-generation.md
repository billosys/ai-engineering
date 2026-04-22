---
concept: Help Generation
slug: help-generation
category: cli-framework
subcategory: output-formatting
tier: foundational

source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Help and Usage Output"

extraction_confidence: high

aliases:
  - "automatic help"
  - "help output"
  - "usage output"
  - "HelpTemplate"
  - "clap help"

prerequisites:
  - command
  - arg

extends: []

related:
  - clap-styling
  - clap-derive-api
  - clap-builder-api

contrasts_with: []

answers_questions:
  - "How does clap generate help output automatically?"
  - "How do I customize the help template in clap?"
  - "What is HelpTemplate and how do I use it?"
  - "How does clap organize help output for arguments and subcommands?"
---

## Quick Definition

Clap automatically generates formatted help and usage output for CLI applications, using `AutoHelp` for default rendering or `HelpTemplate` for customizable template-driven output that controls the layout of binary names, argument listings, and subcommand sections.

## Core Definition

Clap's help generation system is implemented in the `clap_builder/src/output/` module. The `write_help` function serves as the entry point for writing parser help to a stream. Two main structs handle rendering: `AutoHelp` provides clap's auto-generated help, while `HelpTemplate` wraps a writer stream and provides fine-grained methods for generating help sections. `HelpTemplate::write_templated_help` renders help according to a template defined via `Command::help_template`, enabling full customization of help layout. The template system supports writing display names, binary names, all arguments (options, flags, positional args), subcommands, and custom sections. Arguments are sorted by length and display order before rendering. Short flags, long flags, value names, and help text are written with proper alignment padding (Section 10: Help and Usage Output, `clap_builder/src/output/help_template.rs`).

## Prerequisites

- **Command** -- Help is generated for a `Command` and its arguments; `Command::help_template` controls the template
- **Arg** -- Each argument's help text, value names, and metadata are rendered in the help output

## Key Properties

1. `AutoHelp` provides the default auto-generated help writer
2. `HelpTemplate` wraps a writer stream for customizable help generation
3. `HelpTemplate::write_templated_help` renders help using the template defined by `Command::help_template`
4. `write_display_name` writes the display name of the command
5. `write_bin_name` writes the binary name of the command
6. `write_all_args` writes help for all arguments (options, flags, args, subcommands) including section titles
7. `write_args` sorts arguments by length and display order before writing
8. `write_arg` writes help for a single argument including short/long flags, value names, and description
9. Alignment padding is calculated between argument switches/values and their about message
10. `will_args_wrap` determines whether next-line help will be used for arguments
11. Subcommand help is written through dedicated subcommand handling methods
12. Help output respects `Command::term_width` for terminal wrapping (requires `wrap_help` feature)

## Construction / Recognition

### To Use Default Help

1. Define your `Command` with arguments and subcommands
2. Clap automatically adds `--help` / `-h` flags
3. When the user passes `--help`, clap generates and displays help, then exits with code 0

### To Customize Help Layout

1. Define a help template string with placeholders
2. Apply it with `Command::help_template("template string")`
3. The template controls which sections appear and in what order
4. Use `HelpTemplate` methods for programmatic control

### To Write Help Programmatically

1. Create a `HelpTemplate` instance with `HelpTemplate::new`
2. Call individual methods: `write_display_name`, `write_all_args`, etc.
3. Compose output in any order needed

## Context & Application

Help generation is one of clap's core value propositions -- it transforms argument definitions into polished, professional help output without manual formatting. The automatic help system handles common cases well, showing usage lines, argument groups with headers, short/long flag alignment, and subcommand listings. For applications needing custom layouts (e.g., man-page style, grouped by functionality, or with additional prose sections), `HelpTemplate` and `Command::help_template` provide the customization surface. The `wrap_help` feature enables terminal-width-aware wrapping, which is important for narrow terminals.

**Typical contexts:**
- Default help output for most CLI applications
- Custom help templates for complex tools with many subcommands
- Programmatic help generation for documentation tools

## Examples

**Example 1** (Section 10, AutoHelp): The `AutoHelp` struct provides clap's default auto-generated help writer:
```rust
// AutoHelp is used internally by clap when --help is invoked
// Most applications use it implicitly through Command
let cmd = Command::new("myapp")
    .about("My application")
    .arg(Arg::new("input").help("Input file"));
// --help automatically uses AutoHelp
```

**Example 2** (Section 10, HelpTemplate): Creating a custom help template instance:
```rust
// HelpTemplate wraps a writer stream and provides methods like:
// - write_display_name: writes the command display name
// - write_bin_name: writes the binary name
// - write_all_args: writes all argument help with titles
// - write_arg: writes help for a single argument
```

**Example 3** (Section 10, write_templated_help): The template-driven help system:
```rust
// Command::help_template controls the layout
// HelpTemplate::write_templated_help renders according to that template
// See Command::help_template documentation for template syntax
```

## Relationships

### Builds Upon

- **Command** -- Help is generated for a Command; `Command::help_template` controls layout
- **Arg** -- Each Arg contributes its help text, value names, short/long flags to the output

### Enables

- **clap-styling** -- Styles are applied to help output sections (headers, literals, placeholders)

### Related

- **clap-error-handling** -- Help requests are handled through the error system (exit code 0 via stdout)
- **Derive API** -- Derive macros generate help text from doc comments and attributes
- **Builder API** -- Builder methods like `.about()`, `.help()`, `.help_heading()` feed into help generation

## Common Errors

- **Error**: Forgetting to set `about` on the Command, resulting in a bare help output
  **Correction**: Always set `.about("description")` on your Command for informative help

- **Error**: Setting a custom help template that omits the arguments section
  **Correction**: Ensure your template includes the appropriate placeholder for argument listings

- **Error**: Expecting `wrap_help` behavior without enabling the feature
  **Correction**: Terminal-width-aware wrapping requires the `wrap_help` feature flag

## Common Confusions

- **Confusion**: Thinking `--help` and `-h` always show the same output
  **Clarification**: By default both show the same help, but `Command::long_help` and `Arg::long_help` can provide extended help shown only with `--help`

- **Confusion**: Believing help generation requires explicit code
  **Clarification**: Clap adds `--help` automatically; you only need custom code if you want to customize the help layout or trigger help programmatically

- **Confusion**: Confusing `AutoHelp` with `HelpTemplate`
  **Clarification**: `AutoHelp` is the default auto-generated writer; `HelpTemplate` provides fine-grained control over help section rendering and supports custom templates

## Source Reference

Clap Documentation, Section 10: "Help and Usage Output" (clap-source-docs). Source files: `clap_builder/src/output/help.rs` (write_help entry point), `clap_builder/src/output/help_template.rs` (AutoHelp struct, HelpTemplate struct with methods: write_templated_help, write_display_name, write_bin_name, write_all_args, write_args, write_arg, short, long, align_to_about, help, will_args_wrap, subcmd).

## Verification Notes

- Definition: Synthesized from Section 10 module and struct documentation
- Key Properties: All items from direct method documentation in source
- Examples: Source provides method signatures and doc comments but few standalone examples; examples are illustrative based on documented APIs
- Confidence: HIGH -- Section 10 provides clear struct and method documentation, though the section focuses on internal API rather than user-facing usage patterns
- Cross-references: `command`, `arg`, `clap-styling` verified against other agents' planned extractions
- Uncertainties: Template syntax details are referenced via `Command::help_template` but the full syntax is documented in the Command section, not Section 10
