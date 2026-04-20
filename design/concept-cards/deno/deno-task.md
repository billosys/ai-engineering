---
concept: deno task
slug: deno-task
category: cli
subcategory: execution commands
tier: foundational
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "runtime/reference/cli/index.md"
chapter_number: null
pdf_page: null
section: "Execution"
extraction_confidence: medium
aliases:
  - "deno task command"
  - "Deno task runner"
prerequisites:
  - deno-cli
extends:
  - deno-cli
related:
  - deno-run
contrasts_with: []
answers_questions:
  - "How do I define and run project tasks in Deno?"
  - "What is the Deno equivalent of npm scripts?"
---

# Quick Definition

`deno task` is Deno's built-in task runner that executes named commands defined in the `tasks` field of `deno.json`, analogous to npm scripts in `package.json`.

# Core Definition

The `deno task` subcommand runs named tasks defined in the project's `deno.json` configuration file. It serves the same purpose as `npm run` or `yarn run` -- providing a standard way to define and execute project-specific commands. Tasks are defined as shell command strings in the `"tasks"` object of `deno.json`.

# Prerequisites

- **deno-cli** -- `deno task` is a subcommand of the Deno CLI.

# Key Properties

1. **Configuration-based** -- Tasks are defined in the `"tasks"` field of `deno.json`.
2. **Shell command execution** -- Task values are shell command strings, not JavaScript.
3. **Built-in** -- No additional packages needed; part of the Deno CLI.
4. **Cross-platform** -- Deno provides a cross-platform shell implementation for task execution.

# Construction / Recognition

## To Use:
1. Define tasks in `deno.json`:
```json
{
  "tasks": {
    "dev": "deno run --watch main.ts",
    "test": "deno test --allow-all",
    "build": "deno compile -o myapp main.ts"
  }
}
```
2. Run a task: `deno task dev`
3. List tasks: `deno task`

## To Identify:
- Invocation: `deno task <task-name>`
- Tasks defined in `deno.json` under the `"tasks"` key.

# Context & Application

- **Development workflows**: Define common development commands (dev server, test, build) as named tasks.
- **CI/CD**: Reference tasks in CI pipelines for consistent command execution.
- **Team collaboration**: Standardize project commands so all developers use the same invocations.

# Examples

**Example 1** (synthesized from CLI reference): Defining and running a development task.
```json
{
  "tasks": {
    "dev": "deno run --watch --allow-net main.ts"
  }
}
```
```shell
deno task dev
```

# Relationships

## Builds Upon
- **deno-cli** -- Subcommand of the CLI.

## Enables
- Standardized project command definitions.

## Related
- **deno-run** -- Tasks often wrap `deno run` invocations.

## Contrasts With
- npm scripts -- Same concept, but `deno task` uses `deno.json` instead of `package.json` and includes a cross-platform shell.

# Common Errors

- **Error**: Running `deno task` without a `deno.json` file in the project.
  **Correction**: Create a `deno.json` with a `"tasks"` field.

# Common Confusions

- **Confusion**: `deno task` can only run Deno commands.
  **Clarification**: Tasks are arbitrary shell commands; they can invoke any program, not just `deno`.

# Source Reference

- runtime/reference/cli/index.md: "deno task - run a task" listing.

# Verification Notes

- Medium confidence: The CLI reference confirms `deno task` as a task runner. The `deno.json` tasks configuration is well-established but detailed documentation resides in a separate reference page not included in this agent's source scope.
