---
concept: deno run
slug: deno-run
category: cli
subcategory: execution commands
tier: foundational
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/getting_started/command_line_interface.md"
chapter_number: null
pdf_page: null
section: "An example subcommand - deno run"
extraction_confidence: high
aliases:
  - "deno run command"
prerequisites:
  - deno-cli
extends:
  - deno-cli
related:
  - deno-serve
  - deno-task
  - deno-compile
  - web-platform-apis
  - deno-namespace-apis
contrasts_with:
  - deno-serve
  - deno-check
answers_questions:
  - "How do I run a TypeScript or JavaScript file in Deno?"
  - "What distinguishes `deno run` from `deno serve`?"
  - "What distinguishes `deno check` from `deno run`?"
  - "How does TypeScript support relate to the runtime?"
---

# Quick Definition

`deno run` executes a JavaScript or TypeScript file (local, remote, or piped via stdin) with optional permission flags and watch mode, without type-checking by default.

# Core Definition

The `deno run` subcommand is the primary way to execute scripts in Deno. It accepts a local file path, an HTTPS URL, or stdin as input. TypeScript files are transpiled on the fly with no configuration required. By default, `deno run` does **not** perform type checking -- it only transpiles and executes. To add type checking, pass `--check` (or use `deno check` separately).

Scripts run in Deno's secure sandbox: no file, network, or environment access is granted unless explicit permission flags (e.g., `--allow-net`, `--allow-read`) are provided before the script name. Arguments placed after the script name are passed to the script via `Deno.args`.

# Prerequisites

- **deno-cli** -- `deno run` is a subcommand of the Deno CLI.

# Key Properties

1. **Runs TypeScript natively** -- No `tsc` or `tsconfig.json` needed; Deno transpiles TypeScript automatically.
2. **No type checking by default** -- Only transpilation occurs unless `--check` is specified.
3. **Permission-gated execution** -- Access to network, filesystem, environment, etc. must be granted via `--allow-*` flags.
4. **Multiple input sources** -- Local files, remote URLs, and piped stdin (`deno run -`).
5. **Watch mode** -- `--watch` restarts the process on file changes; `--watch-hmr` attempts in-place hot module replacement.
6. **Script arguments** -- Anything after the script name is passed as arguments, not runtime flags.

# Construction / Recognition

## To Use:
1. Run a local file: `deno run main.ts`
2. Run a remote file: `deno run https://example.com/script.ts`
3. Run from stdin: `cat main.ts | deno run -`
4. With permissions: `deno run --allow-net --allow-read main.ts`
5. With watch mode: `deno run --watch main.ts`
6. With type checking: `deno run --check main.ts`

## To Identify:
- Invocation pattern: `deno run [flags] <script> [script-args]`
- Flags must precede the script name.

# Context & Application

- **Development**: The most frequently used subcommand for running applications during development; combined with `--watch` for live-reloading.
- **Scripting**: Can run remote scripts directly from URLs without downloading first.
- **Production**: Typically used with explicit permission flags for security.

# Examples

**Example 1** (from source): Running a local TypeScript file.
```shell
deno run main.ts
```

**Example 2** (from source): Running a remote script.
```shell
deno run https://docs.deno.com/examples/scripts/hello_world.ts
```

**Example 3** (from source): Passing script arguments.
```shell
$ deno run main.ts arg1 arg2 arg3
[ "arg1", "arg2", "arg3" ]
```

**Example 4** (from source): Correct vs incorrect flag ordering.
```shell
# Good. We grant net permission to net_client.ts.
deno run --allow-net net_client.ts

# Bad! --allow-net was passed to Deno.args, throws a net permission error.
deno run net_client.ts --allow-net
```

# Relationships

## Builds Upon
- **deno-cli** -- `deno run` is the primary execution subcommand.

## Enables
- Running any JavaScript, TypeScript, or JSX/TSX script in the Deno runtime.

## Related
- **deno-task** -- Runs named tasks from `deno.json`, often wrapping `deno run`.
- **web-platform-apis** -- APIs available during `deno run` execution.
- **deno-namespace-apis** -- `Deno.*` APIs available during execution.

## Contrasts With
- **deno serve** -- `deno serve` is specialized for HTTP servers with automatic scaling; `deno run` is general-purpose script execution.
- **deno check** -- `deno check` only type-checks without executing; `deno run` executes without type-checking by default.

# Common Errors

- **Error**: Placing `--allow-net` after the script name.
  **Correction**: Permission flags must come before the script path; flags after the script name become script arguments.

- **Error**: Assuming `deno run` type-checks TypeScript.
  **Correction**: `deno run` transpiles but does not type-check. Use `deno run --check` or `deno check` for type checking.

# Common Confusions

- **Confusion**: `deno run` and `deno serve` are interchangeable for HTTP servers.
  **Clarification**: `deno serve` provides automatic multi-core scaling and expects an exported `fetch` handler; `deno run` requires manually calling `Deno.serve()` and runs single-threaded by default.

- **Confusion**: TypeScript support means type errors block execution.
  **Clarification**: Deno's TypeScript support is about zero-config transpilation. Type checking is opt-in via `--check`.

# Source Reference

- runtime/getting_started/command_line_interface.md: Sections "An example subcommand - deno run", "Passing script arguments", "Argument and flag ordering", "Watch mode", "Type checking flags".

# Verification Notes

- High confidence: `deno run` behavior is explicitly documented with examples.
- Flag ordering pitfall quoted verbatim from source.
- Type-checking default verified against the type-checking mode table in source.
