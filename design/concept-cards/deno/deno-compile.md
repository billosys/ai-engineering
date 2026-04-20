---
concept: deno compile
slug: deno-compile
category: cli
subcategory: tooling commands
tier: intermediate
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/reference/cli/index.md"
chapter_number: null
pdf_page: null
section: "Tooling"
extraction_confidence: medium
aliases:
  - "deno compile command"
  - "Deno standalone executable"
prerequisites:
  - deno-cli
  - deno-run
extends:
  - deno-cli
related:
  - deno-bundle
  - deno-in-docker
contrasts_with:
  - deno-bundle
answers_questions:
  - "How do I compile a Deno script into a standalone executable?"
  - "Can Deno produce binaries that don't require Deno to be installed?"
---

# Quick Definition

`deno compile` compiles a TypeScript or JavaScript program and all its dependencies into a single, self-contained executable binary that runs without requiring Deno to be installed.

# Core Definition

The `deno compile` subcommand produces a standalone executable from a Deno program. The output binary embeds the Deno runtime, the application code, and all dependencies into a single file. The CLI overview states that Deno can be used to "compile your code into standalone executables." The compiled binary can be distributed and run on the target platform without any Deno installation.

`deno compile` performs local type checking by default (unlike `deno run`).

# Prerequisites

- **deno-cli** -- `deno compile` is a subcommand of the Deno CLI.
- **deno-run** -- Understanding script execution and permission flags is needed, as permissions are baked into the compiled binary.

# Key Properties

1. **Self-contained output** -- The binary includes the Deno runtime, application code, and all dependencies.
2. **No runtime dependency** -- The output runs without Deno installed on the target system.
3. **Cross-compilation** -- Can target different OS/architecture combinations.
4. **Type-checks by default** -- Unlike `deno run`, `deno compile` performs local type checking.
5. **Permission embedding** -- Permission flags specified at compile time are embedded in the binary.
6. **Affected by lock files and cache flags** -- Integrity checking and cache flags apply.

# Construction / Recognition

## To Use:
1. Compile a script: `deno compile main.ts`
2. Compile with a custom output name: `deno compile -o myapp main.ts`
3. Compile with permissions: `deno compile --allow-net --allow-read main.ts`

## To Identify:
- Invocation: `deno compile [flags] <script>`
- Produces a platform-specific binary file.

# Context & Application

- **Distribution**: Ship applications as single binaries without requiring users to install Deno.
- **CLI tools**: Build command-line tools from TypeScript/JavaScript.
- **Docker**: Can be combined with Docker for minimal container images (copy just the binary).

# Examples

**Example 1** (synthesized from CLI reference and overview): Compiling a script.
```shell
deno compile -o myapp main.ts
./myapp
```

**Example 2** (synthesized): Compiling with network permissions.
```shell
deno compile --allow-net=api.example.com main.ts
```

# Relationships

## Builds Upon
- **deno-cli** -- Subcommand of the CLI.

## Enables
- Standalone binary distribution of Deno applications.

## Related
- **deno-bundle** -- Bundles to a single JS file (not an executable); can be complementary.
- **deno-in-docker** -- Compiled binaries can simplify Docker images.

## Contrasts With
- **deno-bundle** -- `deno bundle` produces a single JavaScript file; `deno compile` produces a standalone binary with the runtime embedded.

# Common Errors

- **Error**: Forgetting to specify permissions at compile time.
  **Correction**: Permissions are embedded at compile time. If the application needs network access, include `--allow-net` in the compile command.

# Common Confusions

- **Confusion**: `deno compile` and `deno bundle` produce the same thing.
  **Clarification**: `deno compile` produces a standalone binary (includes the Deno runtime). `deno bundle` produces a single JavaScript file that still needs a runtime to execute.

# Source Reference

- runtime/reference/cli/index.md: "deno compile - compile a program into a standalone executable."
- runtime/getting_started/command_line_interface.md: "compile your code into standalone executables", type checking table showing `deno compile` uses local type checking.

# Verification Notes

- Medium confidence: Purpose and behavior confirmed from CLI reference listing and the type-checking table. Detailed compile flags are documented in a separate reference page outside this agent's source scope.
