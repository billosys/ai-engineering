---
concept: The erl Command
slug: erl-command
category: tooling
subcategory: runtime-commands
tier: foundational
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erl"
chapter_number: null
pdf_page: null
section: "erl"
extraction_confidence: high
aliases:
  - "erl"
  - "erl program"
  - "Erlang runtime launcher"
prerequisites: []
extends: []
related:
  - emulator-flags
  - init-flags
  - erlc-command
  - escript
  - epmd
contrasts_with: []
answers_questions:
  - "How do I start the Erlang runtime system with erl?"
  - "What is the erl command?"
  - "What kinds of arguments does erl accept?"
  - "What distinguishes emulator flags from init flags and plain arguments?"
---

# Quick Definition

The `erl` program starts an Erlang runtime system. Its arguments are divided into three categories: emulator flags (starting with `+`), flags (starting with `-`), and plain arguments, each processed by different parts of the system.

# Core Definition

The erl command documentation states: "The `erl` program starts an Erlang runtime system. The exact details (for example, whether `erl` is a script or a program and which other programs it calls) are system-dependent."

Arguments are categorized as follows:

- **Emulator flags** (`+` prefix): Control the behavior of the BEAM emulator itself (e.g., `+S` for schedulers, `+P` for process limit). As the documentation says: "Any argument starting with character `+` is interpreted as an emulator flag."
- **Flags** (`-` prefix): Passed to the Erlang runtime's `init` system process. These are further divided into init flags (interpreted by `init` directly) and user flags (stored by `init` and retrievable via `init:get_argument/1`).
- **Plain arguments**: Not interpreted. Retrievable via `init:get_plain_arguments/0`. They can occur before the first flag or after a `--` or `-extra` flag.

# Prerequisites

None -- this is the primary entry point for running Erlang.

# Key Properties

1. Arguments are read left to right; later flags override earlier flags
2. Emulator flags (`+`) configure the VM itself before Erlang code runs
3. Flags (`-`) are passed to the `init` process for the Erlang-level runtime
4. The `init` process interprets init flags and stores user flags
5. Plain arguments after `--` or `-extra` are available to application code
6. A small number of `-` flags are actually emulator flags (e.g., `-version`, `-instr`)
7. Environment variables `ERL_AFLAGS` (prepended), `ERL_ZFLAGS`/`ERL_FLAGS` (appended) extend the command line
8. On Unix, `SIGUSR1` forces a crash dump and `SIGTERM` triggers `init:stop/0`

# Construction / Recognition

## To Construct/Create:

Start Erlang with `erl` followed by arguments:

```text
% erl +W w -sname arnie +S 2 -s my_init -extra +bertie
```

In this example: `+W w` and `+S 2` are emulator flags, `-s my_init` is an init flag, `-sname arnie` is a user flag, and `+bertie` after `-extra` is a plain argument.

## To Identify/Recognize:

1. A `+` prefix indicates an emulator flag
2. A `-` prefix indicates an init or user flag
3. Anything after `--` or `-extra` is a plain argument
4. `init:get_argument/1` retrieves user flags; `init:get_plain_arguments/0` retrieves plain arguments

# Context & Application

The `erl` command is the primary way to start an Erlang node for interactive development, testing, and production. In production deployments, `erl` is typically wrapped by `run_erl` (Unix) or `erlsrv` (Windows) for embedded systems. For scripting, `escript` provides an alternative that bypasses the need for explicit compilation.

The `.erlang` startup file in the user's home directory is evaluated on start if present, allowing customization of the environment (e.g., adding code paths). A `user_default` module can be loaded to extend the shell with custom commands.

# Examples

**Example 1** (erl documentation, "erl <arguments>" section): Demonstrating the three argument types:

```text
% erl +W w -sname arnie +S 2 -s my_init -extra +bertie
(arnie@host)1> init:get_argument(sname).
{ok,[["arnie"]]}
(arnie@host)2> init:get_plain_arguments().
["+bertie"]
```

**Example 2** (erl documentation, "erl <arguments>" section): User-defined flags:

```text
% erl -myflag 1
1> init:get_argument(myflag).
{ok,[["1"]]}
2> init:get_plain_arguments().
[]
```

# Relationships

## Related

- **emulator-flags** -- The `+` flags that configure the BEAM VM (schedulers, process limits, memory)
- **init-flags** -- The `-` flags interpreted by the `init` process (boot, eval, name, setcookie)
- **erlc-command** -- The Erlang compiler command, often used before `erl` to compile modules
- **escript** -- An alternative to `erl` for running short Erlang programs without prior compilation
- **epmd** -- The Erlang Port Mapper Daemon, started automatically when erl runs in distributed mode

# Common Errors

- **Error**: Confusing emulator flag syntax with init flag syntax (e.g., writing `-S 4` instead of `+S 4`)
  **Correction**: Emulator flags always start with `+`, init/user flags with `-`

- **Error**: Expecting flags after `-extra` to be interpreted as flags
  **Correction**: Everything after `-extra` is treated as plain arguments, even if prefixed with `+` or `-`

# Common Confusions

- **Confusion**: Believing all `-` flags are init flags
  **Clarification**: The `init` process interprets some `-` flags directly (init flags like `-boot`, `-eval`, `-s`) and stores the rest as user flags (like `-sname`, `-setcookie`), which are read by other parts of the system like Kernel

- **Confusion**: Thinking `ERL_FLAGS` and `ERL_AFLAGS` are equivalent
  **Clarification**: `ERL_AFLAGS` content is added to the beginning of the command line, while `ERL_FLAGS` and `ERL_ZFLAGS` are added to the end

# Source Reference

"erl" command documentation, sections "Description", "erl <arguments>", "Flags", "Emulator Flags", "Environment Variables", "Signals", and "Configuration".

# Verification Notes

- Argument categorization: Directly from the "erl <arguments>" section
- Examples: Verbatim from source
- Environment variables: Directly from the "Environment Variables" section
- Signal handling: Directly from the "Signals" section
- Confidence: HIGH -- all content drawn from explicit documentation
