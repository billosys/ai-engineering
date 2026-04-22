---
concept: Shell Completions
slug: shell-completions
category: tooling
subcategory: shell-integration
tier: intermediate

source: "Clap Documentation"
source_slug: clap
authors: "The Clap Contributors"
chapter: "clap-source-docs"
chapter_number: null
pdf_page: null
section: "Shell Completions"

extraction_confidence: high

aliases:
  - "clap_complete"
  - "shell completion generation"
  - "tab completion"
  - "CompleteEnv"
  - "Generator trait"

prerequisites:
  - command
  - clap-builder-api

extends:
  - value-hint

related:
  - clap-derive-api
  - clap-cargo

contrasts_with: []

answers_questions:
  - "How do I generate shell completions for a clap CLI?"
  - "What shells does clap_complete support?"
  - "What is the difference between AOT and runtime completion generation?"
  - "How do I use CompleteEnv for environment-based completions?"
  - "How do I write a custom completion generator?"
  - "How do I provide custom completion candidates for an argument?"
---

## Quick Definition

The `clap_complete` crate generates shell completion scripts for clap-based CLIs, supporting Bash, Zsh, Fish, Elvish, and PowerShell through both ahead-of-time (AOT) script generation via the `Generator` trait and runtime environment-activated completions via `CompleteEnv`.

## Core Definition

`clap_complete` provides two approaches to shell completions. The **AOT (ahead-of-time)** approach uses `generate_to` (compile-time, typically in `build.rs`) or `generate` (runtime, user-triggered) to produce static shell completion scripts. The `Generator` trait defines the interface with `file_name` and `generate`/`try_generate` methods, and the `Shell` enum implements it for all built-in shells (Bash, Zsh, Fish, Elvish, PowerShell). The **environment-activated** approach uses `CompleteEnv`, which intercepts a special environment variable (`COMPLETE=<shell>`) to generate completions dynamically from the actual binary, providing better accuracy. `CompleteEnv::with_factory` accepts a closure returning a `Command`, and `.complete()` processes the request. Custom completion candidates are supported through `ArgValueCompleter`, `ArgValueCandidates`, `SubcommandCandidates`, the `ValueCompleter` trait, the `ValueCandidates` trait, and `PathCompleter`. The `CompletionCandidate` struct represents a shell-agnostic completion with value, help text, grouping tag, display order, and visibility settings (Section 12: Shell Completions, `clap_complete/src/`).

## Prerequisites

- **Command** -- Completions are generated from a `Command` definition
- **Builder API** -- Command and argument structure drives completion generation

## Key Properties

1. **AOT generation**: `generate_to(Shell, &mut cmd, "name", outdir)` writes completion file at compile time
2. **Runtime generation**: `generate(Shell, &mut cmd, "name", &mut io::stdout())` outputs completions at runtime
3. `Generator` trait requires `file_name(&self, name: &str) -> String` and `generate(&self, cmd: &Command, buf: &mut dyn Write)`
4. `Shell` enum variants: `Bash`, `Zsh`, `Fish`, `Elvish`, `PowerShell`
5. `Shell::from_env()` detects the user's current shell from the `SHELL` environment variable
6. `Shell::from_shell_path(path)` parses a shell from a path to its executable
7. **CompleteEnv**: `CompleteEnv::with_factory(cli).complete()` activates environment-based completions
8. Environment activation uses `COMPLETE=<shell>` variable (e.g., `source <(COMPLETE=bash your_program)`)
9. `CompleteEnv` benefits: no double Command generation, no interference with CLI logic
10. `CompletionCandidate::new(value)` creates candidates with `.help()`, `.id()`, `.tag()`, `.display_order()`, `.hide()` builders
11. `ArgValueCompleter::new(completer)` provides custom completions for an argument
12. `PathCompleter` completes file paths with `.any()`, `.file()`, `.dir()`, `.stdio()`, `.filter()` methods
13. `ValueCompleter` and `ValueCandidates` traits enable user-provided completion logic
14. Shell completion registration should be re-sourced on upgrade due to unstable interface
15. Fish generator currently only supports named options, not positional arguments

## Construction / Recognition

### To Generate Completions at Compile Time (build.rs)

1. Separate your `Command` definition into a reusable function (e.g., `build_cli()`)
2. Add `clap` and `clap_complete` to `[build-dependencies]` in Cargo.toml
3. In `build.rs`, call `generate_to(Bash, &mut cmd, "myapp", outdir)?`
4. To generate for all shells: loop over `Shell::value_variants()`
5. The output file will be at `<OUT_DIR>/<bin_name>.<shell_ext>`

### To Generate Completions at Runtime

1. Add a `--generate` argument with `value_parser!(Shell)`
2. When the argument is present, call `generate(shell, &mut cmd, "myapp", &mut io::stdout())`
3. User redirects output: `myapp --generate bash > completions.bash`

### To Use Environment-Activated Completions

1. Add `CompleteEnv::with_factory(cli).complete()` at the start of `main()`
2. Users source completions: `source <(COMPLETE=bash your_program)` in shell config
3. Completions are generated dynamically from the actual binary

### To Provide Custom Completion Candidates

1. Implement `ValueCompleter` trait with `fn complete(&self, current: &OsStr) -> Vec<CompletionCandidate>`
2. Attach with `#[arg(add = ArgValueCompleter::new(my_completer))]` in derive API
3. Or use `PathCompleter::file()` / `PathCompleter::dir()` for path completion

## Context & Application

Shell completions significantly improve CLI usability by providing tab-completion for commands, flags, values, and file paths. The AOT approach produces static scripts that can be distributed with packages but may become stale. The environment-activated approach (`CompleteEnv`) is newer and preferred for accuracy since completions always reflect the actual binary, but requires re-sourcing on upgrade. Custom completers are useful for dynamic values like database names, container IDs, or API resources. The `clap_complete_nushell` crate extends support to nushell.

**Typical contexts:**
- Package distribution with pre-generated completion scripts
- Self-installing completions via `CompleteEnv` and shell rc files
- IDE-style completion for complex CLIs with dynamic values

## Examples

**Example 1** (Section 12, generate_to): Compile-time generation in build.rs:
```rust
use clap_complete::{generate_to, shells::Bash};
use std::env;

include!("src/cli.rs");

fn main() -> Result<(), std::io::Error> {
    let outdir = match env::var_os("OUT_DIR") {
        None => return Ok(()),
        Some(outdir) => outdir,
    };
    let mut cmd = build_cli();
    let path = generate_to(Bash, &mut cmd, "myapp", outdir)?;
    println!("cargo:warning=completion file is generated: {path:?}");
    Ok(())
}
```

**Example 2** (Section 12, generate): Runtime generation with shell argument:
```rust
use clap::{Command, Arg, ValueHint, value_parser, ArgAction};
use clap_complete::{generate, Generator, Shell};
use std::io;

fn build_cli() -> Command {
    Command::new("example")
        .arg(Arg::new("file").help("some input file").value_hint(ValueHint::AnyPath))
        .arg(Arg::new("generator").long("generate").action(ArgAction::Set)
            .value_parser(value_parser!(Shell)))
}

fn main() {
    let matches = build_cli().get_matches();
    if let Some(generator) = matches.get_one::<Shell>("generator").copied() {
        let mut cmd = build_cli();
        generate(generator, &mut cmd, cmd.get_name().to_string(), &mut io::stdout());
    }
}
```

**Example 3** (Section 12, CompleteEnv): Environment-activated completions:
```rust
use clap_complete::CompleteEnv;

fn cli() -> clap::Command {
    clap::Command::new("myapp") // ...
}

fn main() {
    CompleteEnv::with_factory(cli).complete();
    // ... rest of application logic
}
// User sources: echo "source <(COMPLETE=bash myapp)" >> ~/.bashrc
```

**Example 4** (Section 12, PathCompleter): Custom path completion with derive:
```rust
use clap::Parser;
use clap_complete::engine::{ArgValueCompleter, PathCompleter};

#[derive(Debug, Parser)]
struct Cli {
    #[arg(long, add = ArgValueCompleter::new(PathCompleter::file()))]
    custom: Option<String>,
}
```

## Relationships

### Builds Upon

- **Command** -- Completions are generated from the Command structure
- **ValueHint** -- `Arg::value_hint` provides shell-specific hints for completion (paths, URLs, usernames, etc.)

### Enables

- Better CLI usability through tab completion in all major shells

### Related

- **Derive API** -- `#[arg(add = ...)]` attaches custom completers in the derive API
- **clap-cargo** -- Cargo plugins benefit from completions for cargo-specific arguments

## Common Errors

- **Error**: Caching CompleteEnv registration script output and reusing stale completions
  **Correction**: The interface between shell registration script and the binary is unstable; re-source completions on upgrade

- **Error**: Forgetting to call `build_cli()` twice (once for parsing, once for completion generation)
  **Correction**: The `Command` is consumed by `get_matches`; create a fresh instance for `generate`

- **Error**: Writing to stdout before `CompleteEnv::complete()` has run
  **Correction**: `CompleteEnv` may need to intercept stdout for completions; place it at the very start of main

## Common Confusions

- **Confusion**: Thinking AOT and CompleteEnv completions serve the same purpose identically
  **Clarification**: AOT generates static scripts that can go stale; CompleteEnv generates dynamically from the actual binary for perfect accuracy, but requires the binary to be available at completion time

- **Confusion**: Believing `Shell::from_env()` always returns a shell
  **Clarification**: It returns `None` if `SHELL` is unset (except on Windows where it defaults to PowerShell) or if the shell is unsupported

- **Confusion**: Expecting Fish completions to include positional argument completions
  **Clarification**: The Fish generator currently only supports named options (-o/--option), not positional arguments

## Source Reference

Clap Documentation, Section 12: "Shell Completions" (clap-source-docs). Source files: `clap_complete/src/aot/generator/mod.rs` (Generator trait, generate, generate_to), `clap_complete/src/aot/shells/` (Bash, Zsh, Fish, Elvish, PowerShell, Shell enum), `clap_complete/src/env/mod.rs` (CompleteEnv, Shells, EnvCompleter trait), `clap_complete/src/engine/` (complete function, CompletionCandidate, ArgValueCompleter, ArgValueCandidates, SubcommandCandidates, ValueCompleter, ValueCandidates, PathCompleter). Also see companion file `clap-complete.md`.

## Verification Notes

- Definition: Synthesized from Section 12 module, trait, struct, and function documentation
- Key Properties: All items directly from source documentation
- Examples: All four examples taken directly from source code examples
- Confidence: HIGH -- Section 12 is the largest section (~1700 lines) with extensive documentation, code examples, and both AOT and CompleteEnv approaches thoroughly covered
- Cross-references: `command`, `clap-builder-api`, `value-hint`, `clap-derive-api` verified against other agents' planned extractions
- Uncertainties: None; completions API is extensively documented
