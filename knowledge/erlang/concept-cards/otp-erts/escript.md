---
concept: Escript
slug: escript
category: tooling
subcategory: scripting
tier: intermediate
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "escript"
chapter_number: null
pdf_page: null
section: "escript"
extraction_confidence: high
aliases:
  - "escript"
  - "Erlang script"
  - "erlang scripting"
prerequisites:
  - erl-command
extends: []
related:
  - erl-command
  - erlc-command
  - init-flags
contrasts_with: []
answers_questions:
  - "What is an escript?"
  - "How do I write and run an escript?"
  - "How do I pass emulator arguments to an escript?"
  - "Can an escript contain precompiled code?"
---

# Quick Definition

An escript is a way to run short Erlang programs without compiling them first. Escripts must contain a `main/1` function that receives command-line arguments as a list of strings. They support a shebang line, emulator arguments via the `%%!` directive, and can contain source code, precompiled beam code, or an entire archive.

# Core Definition

The documentation states: "`escript` provides support for running short Erlang programs without having to compile them first, and an easy way to retrieve the command-line arguments. `escript`s are created by either writing them by hand or using `escript:create/2`."

**Script structure:**
1. **Line 1** (optional): Interpreter line (`#!/usr/bin/env escript`) -- used on Unix for direct execution
2. **Line 2** (optional): Emacs mode directive (`%% -*- erlang -*-`) or encoding comment
3. **Line 2 or 3** (optional): Emulator arguments line (`%%! -sname factorial -mnesia debug verbose`) -- must start with `%%!`
4. **Body**: Erlang source code, inlined beam file, or inlined archive

**Key rules:**
- The script must always contain a `main/1` function
- `main/1` receives a list of strings representing command-line arguments
- If `main/1` returns successfully, exit status is 0
- If an exception occurs, a short message is printed and exit status is 127
- Use `halt(ExitCode)` to return a custom non-zero exit code
- By default (since OTP 27), scripts are compiled before execution; use `-mode(interpret).` to force interpretation
- Module declaration and export declaration of `main/1` are both optional

**Invocation methods:**
- Direct execution on Unix: `./script-name arg1 arg2` (requires executable bit)
- Via escript program: `escript script-name.escript arg1 arg2` (works on all platforms)

# Prerequisites

- **erl-command** -- Escripts run on the Erlang runtime; the `%%!` directive passes flags to `erl`

# Key Properties

1. Scripts are checked for syntactic and semantic correctness before running
2. Warnings are printed but do not prevent execution; errors prevent execution (exit status 127)
3. The `%%!` line passes arguments directly to the emulator (like erl flags)
4. The `epp` preprocessor processes source scripts, enabling macros and `-include_lib` directives
5. Since OTP 27, scripts are compiled by default (previously interpreted by default)
6. `-mode(interpret).` forces interpretation, which is slower but does not require the compiler application
7. Escripts can contain precompiled beam code or an entire Erlang archive (zip)
8. `escript:script_name/0` retrieves the pathname of the running script
9. Environment variables understood by `erl` also affect `escript`

# Construction / Recognition

## To Construct/Create:

Write a script file:

```erlang
#!/usr/bin/env escript
%% -*- erlang -*-
%%! -sname factorial -mnesia debug verbose
main([String]) ->
    try
        N = list_to_integer(String),
        F = fac(N),
        io:format("factorial ~w = ~w\n", [N,F])
    catch
        _:_ ->
            usage()
    end;
main(_) ->
    usage().

usage() ->
    io:format("usage: factorial integer\n"),
    halt(1).

fac(0) -> 1;
fac(N) -> N * fac(N-1).
```

Make it executable and run:

```text
$ chmod u+x factorial
$ ./factorial 5
factorial 5 = 120
```

Or run without the executable bit:

```text
$ escript factorial 5
factorial 5 = 120
```

## To Identify/Recognize:

1. Files starting with `#!/usr/bin/env escript` or `#!/usr/local/bin/escript`
2. Files with `.escript` extension
3. Erlang source files containing a `main/1` function intended for script use
4. The `%%!` directive line passing emulator arguments

# Context & Application

Escripts are ideal for command-line utilities, build scripts, deployment tools, and quick prototypes written in Erlang. They fill the gap between the interactive shell and full OTP releases. For production systems, OTP releases are preferred, but escripts work well for tooling and automation.

Precompiled escripts and archive escripts enable distribution of self-contained Erlang programs. Escripts can be bundled with an Erlang runtime to create standalone, relocatable tools: "In such a standalone system, the `escript`(s) should be located in the top `bin` directory of the standalone system and given `.escript` as file extension."

Escript options for development:
- `-c` -- Forces compilation regardless of mode attribute
- `-d` -- Starts the debugger and sets a breakpoint in `main/1`
- `-i` -- Forces interpretation regardless of mode attribute
- `-s` -- Syntax/semantic check only, does not run the script

# Examples

**Example 1** (escript documentation, "Description" section): The factorial escript showing shebang, emacs directive, emulator flags, and the main/1 entry point:

```erlang
#!/usr/bin/env escript
%% -*- erlang -*-
%%! -sname factorial -mnesia debug verbose
main([String]) ->
    try
        N = list_to_integer(String),
        F = fac(N),
        io:format("factorial ~w = ~w\n", [N,F])
    catch
        _:_ ->
            usage()
    end;
main(_) ->
    usage().

usage() ->
    io:format("usage: factorial integer\n"),
    halt(1).

fac(0) -> 1;
fac(N) -> N * fac(N-1).
```

**Example 2** (escript documentation, "Precompiled escripts" section): Running precompiled or archive escripts:

```text
$ escript factorial.erl 5
factorial 5 = 120
$ escript factorial.beam 5
factorial 5 = 120
$ escript factorial.zip 5
factorial 5 = 120
```

# Relationships

## Builds Upon

- **erl-command** -- Escript runs on the Erlang runtime; `%%!` flags and erl environment variables apply

## Related

- **erlc-command** -- The compiler used when escript compiles source code
- **init-flags** -- Emulator arguments in the `%%!` line follow the same syntax as erl flags

# Common Errors

- **Error**: Forgetting to make the script executable on Unix (`chmod +x`)
  **Correction**: "Erlang scripts do not work on Unix platforms if the execution bit for the script file is not set"

- **Error**: Not providing a `main/1` function
  **Correction**: "An Erlang script file must always contain the `main/1` function"

- **Error**: Expecting `main/1` to receive atoms or parsed values
  **Correction**: All arguments are passed as strings in a list; parse them explicitly in the function

# Common Confusions

- **Confusion**: Thinking escripts are always interpreted
  **Clarification**: Since OTP 27, scripts are compiled by default. The old default (interpretation) can be forced with `-mode(interpret).` in the script

- **Confusion**: Believing the first line must be a shebang
  **Clarification**: "The header is optional, so you directly can 'execute' an Erlang module, Beam file, or archive file without adding any header to them" -- but then you must invoke via `escript filename`

# Source Reference

"escript" command documentation, covering "Description", "Precompiled escripts", "Bundling escripts", and "Options Accepted By escript" sections.

# Verification Notes

- Script structure and rules: Directly from "Description" section
- Factorial example: Verbatim from source
- OTP 27 compilation change: Directly from source ("Before Erlang/OTP 27 the script would be interpreted by default")
- Bundling instructions: Directly from "Bundling escripts" section
- Confidence: HIGH -- all content from explicit documentation
