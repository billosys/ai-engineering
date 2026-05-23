---
concept: The erlc Command
slug: erlc-command
category: tooling
subcategory: compilation
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "erlc"
chapter_number: null
pdf_page: null
section: "erlc"
extraction_confidence: high
aliases:
  - "erlc"
  - "Erlang compiler command"
prerequisites:
  - erl-command
extends: []
related:
  - erl-command
  - escript
contrasts_with: []
answers_questions:
  - "How do I compile Erlang source code from the command line?"
  - "What compilers does erlc support?"
  - "What are the key erlc flags?"
---

# Quick Definition

The `erlc` program provides a common command-line interface to all compilers in the Erlang system. It determines which compiler to invoke based on the input file extension and supports uniform flags for include paths, output directories, macros, and warning levels.

# Core Definition

The documentation states: "The `erlc` program provides a common way to run all compilers in the Erlang system. Depending on the extension of each input file, `erlc` invokes the appropriate compiler. Regardless of which compiler is used, the same flags are used to provide parameters, such as include paths and output directory."

An important note: "The current working directory, `.`, is not included in the code path when running the compiler. This is to avoid loading Beam files from the current working directory that could potentially be in conflict with the compiler or the Erlang/OTP system used by the compiler."

**Supported file types and their compilers:**
- `.erl` -- Erlang source code, generates `.beam` files
- `.S` -- Erlang assembler source, generates `.beam` files
- `.core` -- Core Erlang source, generates `.beam` files
- `.abstr` -- Erlang abstract format, generates `.beam` files
- `.yrl` -- Yecc source (parser generator), generates `.erl` files
- `.mib` -- SNMP MIB definitions, generates `.bin` files
- `.bin` -- Compiled SNMP MIB, generates `.hrl` files
- `.rel` -- Release script, generates boot files
- `.asn1` -- ASN.1 files, generates `.erl`, `.hrl`, and `.asn1db` files
- `.idl` -- IDL files for IC (Interface Compiler)

**Key flags:**
- `-I <Dir>` -- Add include directory (searched in reverse order of specification)
- `-o <Dir>` -- Output directory (default: current working directory)
- `-D<Name>[=<Value>]` -- Define a macro (value can be any Erlang term)
- `-W` / `-W<Number>` -- Set warning level (default 1; `-W0` disables warnings)
- `-Werror` -- Treat all warnings as errors
- `-v` -- Verbose output
- `-b <Type>` -- Output file type
- `+<Term>` -- Pass an Erlang term directly to the compiler (e.g., `+export_all`)
- `-M` -- Produce Makefile dependency rules instead of compiling
- `-enable-feature <Feature>` / `-disable-feature <Feature>` -- Control language features

# Prerequisites

- **erl-command** -- `erlc` invokes the Erlang runtime internally to run compilers

# Key Properties

1. File extension determines which compiler is invoked
2. The current working directory is intentionally excluded from the code path during compilation
3. Include file search order: current directory of the file server, base name directory of the compiled file, then `-I` directories (last specified searched first)
4. The `+<Term>` syntax passes terms directly to the compiler (e.g., `+debug_info`, `+export_all`)
5. Makefile dependency generation (`-M`, `-MF`, `-MMD`) supports build system integration
6. A compile server (`-server` or `ERLC_USE_SERVER=yes`) can speed up multi-file builds by reusing a running Erlang system
7. The compile server is a hidden node using the Erlang distribution, one per user

# Construction / Recognition

## To Construct/Create:

Compile an Erlang source file:

```text
erlc -I include -o ebin -W2 +debug_info src/mymodule.erl
```

Generate Makefile dependencies:

```text
erlc -M src/mymodule.erl
```

Enable the compile server for faster builds:

```text
ERLC_USE_SERVER=yes erlc -o ebin src/*.erl
```

## To Identify/Recognize:

1. The `erlc` command is the standard way to compile Erlang files from the shell
2. It operates on files with recognized extensions
3. Build tools like rebar3 invoke erlc (or its API equivalent) internally

# Context & Application

While `erlc` is the direct compiler command, most Erlang projects use build tools like rebar3 that invoke it internally. However, `erlc` is essential for understanding the compilation pipeline, for custom build scripts, and for compiling non-Erlang files (Yecc grammars, ASN.1 specifications, SNMP MIBs) that the build tool may not handle directly.

The compile server feature is useful for large projects: "Whether it will speed up the build depends on the nature of the project and the build machine." The server restarts automatically when Erlang versions, erl options, or working directories change, ensuring correctness at the cost of some startup overhead.

# Examples

**Example 1** (erlc documentation, "Generally Useful Flags" section): Passing a compiler option:

```text
erlc +export_all file.erl
```

**Example 2**: Compiling with include path, output directory, and debug info:

```text
erlc -I include -o ebin +debug_info src/myapp.erl
```

# Relationships

## Related

- **erl-command** -- `erlc` uses `erl` internally; the `ERLC_EMULATOR` environment variable controls which emulator is used
- **escript** -- An alternative approach that runs Erlang source without prior compilation

# Common Errors

- **Error**: Expecting the current working directory to be in the code path during compilation
  **Correction**: The documentation explicitly states that `.` is excluded from the code path to avoid conflicts

- **Error**: Quoting `+<Term>` values incorrectly on the shell
  **Correction**: "On Unix, terms containing tuples and lists must be quoted. Terms containing spaces must be quoted on all platforms."

# Common Confusions

- **Confusion**: Thinking `erlc` only compiles `.erl` files
  **Clarification**: `erlc` handles multiple file types including `.yrl`, `.mib`, `.asn1`, `.rel`, `.S`, `.core`, `.abstr`, and `.idl`

- **Confusion**: Believing the compile server is always beneficial
  **Clarification**: The server must restart when working directories, Erlang versions, or erl options change. "Build systems that build files randomly across multiple directories in parallel will probably not benefit from the compile server."

# Source Reference

"erlc" command documentation, covering "Description", "Generally Useful Flags", "Special Flags", "Supported Compilers", "Compile Server", and "Environment Variables" sections.

# Verification Notes

- Supported file types and compilers: Directly from "Supported Compilers" section
- Flag descriptions: Directly from "Generally Useful Flags" section
- Compile server behavior: Directly from "Compile Server" section
- Code path exclusion: Verbatim from "Description" section
- Confidence: HIGH -- all content from explicit documentation
