---
concept: Deno CLI
slug: deno-cli
category: cli
subcategory: command-line interface
tier: foundational
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/getting_started/command_line_interface.md"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "Deno command line interface"
  - "deno CLI"
prerequisites:
  - deno
extends:
  - deno
related:
  - deno-run
  - deno-serve
  - deno-task
  - deno-compile
  - deno-bundle
  - deno-stability-and-releases
contrasts_with: []
answers_questions:
  - "How do I install Deno?"
  - "What commands does Deno provide?"
  - "How do I get help on Deno subcommands?"
---

# Quick Definition

The Deno CLI is a single-binary command-line program that runs scripts, manages dependencies, formats and lints code, runs tests, and compiles standalone executables -- all without external tooling.

# Core Definition

Deno is a command line program whose CLI "can be used to run scripts, manage dependencies, and even compile your code into standalone executables." The CLI is organized into subcommands grouped by purpose:

- **Execution**: `deno run`, `deno serve`, `deno task`, `deno repl`, `deno eval`
- **Dependency management**: `deno add`, `deno install`, `deno uninstall`, `deno remove`, `deno outdated`, `deno audit`
- **Tooling**: `deno bench`, `deno check`, `deno compile`, `deno fmt`, `deno lint`, `deno test`, `deno doc`, `deno publish`, `deno bundle`, `deno coverage`, `deno jupyter`

Each subcommand has its own flags and options. Help is available via `deno help`, `deno -h`, or `deno --help`.

# Prerequisites

- **Deno** -- The CLI is the primary interface for the Deno runtime; understanding what Deno is comes first.

# Key Properties

1. **Single binary** -- Deno is distributed as one executable with no external dependencies; it works on macOS (arm64 and x64), Linux (x64), and Windows (arm64 and x64).
2. **Subcommand architecture** -- Functionality is organized into subcommands (run, test, fmt, lint, check, compile, serve, task, etc.), each with dedicated flags.
3. **Common flags across subcommands** -- Watch mode (`--watch`), lock files (`--lock`, `--frozen`), cache/compilation flags (`--config`, `--import-map`, `--reload`), and permission flags apply to multiple subcommands.
4. **Watch mode and HMR** -- `--watch` auto-restarts on file changes; `--watch-hmr` attempts in-place hot module replacement and dispatches an `hmr` CustomEvent.
5. **Type checking integration** -- `deno check` type-checks without executing; `deno run --check` type-checks before execution. By default, `deno run` does not type-check.
6. **Self-update** -- `deno upgrade` updates the binary to the latest (or a specified) version.

# Construction / Recognition

## To Use:
1. Install Deno (shell script, Homebrew, npm, Scoop, Chocolatey, cargo, etc.).
2. Verify with `deno --version`.
3. Run a script: `deno run main.ts`.
4. View available commands: `deno help`.

## To Identify:
- A single `deno` binary in `$PATH`.
- Subcommand-based invocation pattern: `deno <subcommand> [flags] [args]`.

# Context & Application

- **Development workflow**: The CLI replaces separate tools for linting (`deno lint`), formatting (`deno fmt`), testing (`deno test`), type-checking (`deno check`), and benchmarking (`deno bench`).
- **CI/CD**: The same subcommands used locally drive CI pipelines.
- **Deployment**: `deno compile` produces standalone executables; `deno serve` runs HTTP servers; `deno bundle` produces single-file JS output.

# Examples

**Example 1** (from source): Running a local script.
```shell
deno run main.ts
```
(Section: "An example subcommand - deno run")

**Example 2** (from source): Running a remote script directly from a URL.
```shell
deno run https://docs.deno.com/examples/scripts/hello_world.ts
```
(Section: "An example subcommand - deno run")

**Example 3** (from source): Using watch mode during development.
```shell
deno run --watch main.ts
```
(Section: "Watch mode")

# Relationships

## Builds Upon
- **Deno** -- The CLI is the primary user-facing interface to the Deno runtime.

## Enables
- **deno-run** -- Running scripts and applications.
- **deno-serve** -- Running HTTP servers.
- **deno-task** -- Running project tasks.
- **deno-compile** -- Compiling to standalone executables.
- **deno-bundle** -- Bundling to single JS files.

## Related
- **deno-stability-and-releases** -- Release channels and `deno upgrade`.
- **deno-in-ci** -- CLI subcommands drive CI pipelines.

## Contrasts With
- Node.js CLI -- Node requires separate tools for linting, formatting, testing, and TypeScript compilation.

# Common Errors

- **Error**: Placing permission flags after the script name (e.g., `deno run net_client.ts --allow-net`).
  **Correction**: Flags must come before the script name; anything after the script name is passed as a script argument.

- **Error**: Expecting `deno run` to type-check by default.
  **Correction**: `deno run` does not type-check. Use `deno check` or `deno run --check` for type checking.

# Common Confusions

- **Confusion**: `deno check` and `deno run` do the same thing.
  **Clarification**: `deno check` only type-checks without executing; `deno run` executes without type-checking (unless `--check` is passed).

- **Confusion**: All subcommands type-check code.
  **Clarification**: Only `deno bench`, `deno check`, `deno compile`, and `deno test` perform local type checking by default. `deno run`, `deno eval`, and `deno repl` do not.

# Source Reference

- runtime/getting_started/command_line_interface.md: Full CLI overview, watch mode, HMR, flags.
- runtime/reference/cli/index.md: Complete subcommand listing.
- runtime/getting_started/installation.md: Installation methods and `deno upgrade`.

# Verification Notes

- High confidence: CLI structure and behavior are explicitly documented across multiple source files.
- Type-checking table reproduced directly from source.
- Flag ordering pitfall quoted directly from source.
