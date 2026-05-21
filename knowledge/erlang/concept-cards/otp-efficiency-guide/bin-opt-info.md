---
concept: bin_opt_info Compiler Option
slug: bin-opt-info
category: compiler-optimization
subcategory: binary-optimization
tier: advanced
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Constructing and Matching Binaries"
chapter_number: null
pdf_page: null
section: "Option bin_opt_info"
extraction_confidence: high
aliases:
  - "bin_opt_info"
  - "+bin_opt_info"
  - "binary optimization info"
prerequisites:
  - match-context
  - sub-binary
  - binary-matching-efficiency
extends: []
related:
  - compiler-binary-optimization
  - binary-append-optimization
contrasts_with: []
answers_questions:
  - "What is the bin_opt_info compiler option?"
  - "How do I verify binary matching optimizations?"
---

# Quick Definition

The `bin_opt_info` compiler option causes the Erlang compiler to print diagnostic warnings about binary optimizations -- reporting where match contexts are reused, where sub binaries must be created, and where optimizations cannot be applied. It is intended for temporary diagnostic use, not as a permanent build option.

# Core Definition

The `bin_opt_info` option causes the compiler to print a lot of information about binary optimizations. It can be given either to the compiler or `erlc` as `+bin_opt_info`, or set through the environment variable `ERL_COMPILER_OPTIONS=bin_opt_info`. The option is not meant to be a permanent option added to Makefiles, because all messages that it generates cannot be eliminated. Therefore, passing the option through the environment is in most cases the most practical approach (Ericsson/OTP Team, "Constructing and Matching Binaries," section "Option bin_opt_info").

# Prerequisites

- **match-context** -- Understanding match contexts is needed to interpret the "match context reused" messages
- **sub-binary** -- Understanding sub binaries is needed to interpret the "binary created" messages
- **binary-matching-efficiency** -- The overall matching optimization framework that `bin_opt_info` reports on

# Key Properties

1. Diagnostic compiler option, not intended for permanent use in Makefiles
2. Can be passed via `erlc +bin_opt_info Mod.erl`
3. Can be set via environment variable: `export ERL_COMPILER_OPTIONS=bin_opt_info`
4. Environment variable approach is recommended as the most practical
5. Generates warnings that cannot all be eliminated (hence not for permanent use)
6. Reports "OPTIMIZED: match context reused" when the compiler avoids creating a sub binary
7. Reports "NOT OPTIMIZED" or "BINARY CREATED" when a sub binary must be created, with a reason

# Construction / Recognition

## Using bin_opt_info

1. Set the environment variable: `export ERL_COMPILER_OPTIONS=bin_opt_info`
2. Compile the module: `erlc Mod.erl`
3. Read the warnings to determine which clauses are optimized and which are not
4. Unset the variable when done: `unset ERL_COMPILER_OPTIONS`

## Interpreting the Output

1. **"OPTIMIZED: match context reused"** -- The compiler successfully avoids creating a sub binary; the match context is passed directly to the next function
2. **"NOT OPTIMIZED: binary is returned from the function"** -- A sub binary must be created because the binary value is returned
3. **"BINARY CREATED: binary is returned from the function"** -- Same as above (variant wording)

# Context & Application

`bin_opt_info` is the primary diagnostic tool for verifying that binary matching code is being optimized as expected. In performance-critical binary processing code (protocol parsers, codec implementations), verifying match context reuse can be the difference between O(n) and O(n^2) binary handling.

**Typical contexts:**
- Debugging performance issues in binary parsing code
- Verifying that a refactoring did not break binary matching optimizations
- Understanding compiler decisions about match context vs. sub binary creation
- Learning how the binary matching optimizer works

**Best practice:** Use the environment variable approach for one-off diagnostics. Never add `bin_opt_info` to Makefiles or rebar configs permanently.

# Examples

**Compiler invocation** (source: "Option bin_opt_info" section):

```erlang
erlc +bin_opt_info Mod.erl
```

Or via environment variable:

```
export ERL_COMPILER_OPTIONS=bin_opt_info
```

**Example output** (source: same section):

```
./efficiency_guide.erl:60: Warning: NOT OPTIMIZED: binary is returned from the function
./efficiency_guide.erl:62: Warning: OPTIMIZED: match context reused
```

**Annotated code with bin_opt_info results** (source: same section):

```erlang
after_zero(<<0,T/binary>>) ->
         %% BINARY CREATED: binary is returned from the function
    T;
after_zero(<<_,T/binary>>) ->
         %% OPTIMIZED: match context reused
    after_zero(T);
after_zero(<<>>) ->
    <<>>.
```

The first clause must create a sub binary because `T` is returned. The second clause reuses the match context because `T` is passed directly to a recursive call.

# Relationships

## Related

- **compiler-binary-optimization** -- The compiler optimizations that `bin_opt_info` reports on (construction side)
- **binary-append-optimization** -- `bin_opt_info` can also reveal information about construction optimizations

# Common Errors

- **Error**: Adding `+bin_opt_info` permanently to the build configuration
  **Correction**: Use it temporarily via the environment variable. The warnings cannot all be eliminated, so they would clutter every build.

- **Error**: Ignoring "NOT OPTIMIZED" warnings in performance-critical code
  **Correction**: Each such warning means a sub binary is being created. In hot loops, investigate whether restructuring could allow match context reuse.

# Common Confusions

- **Confusion**: Thinking "NOT OPTIMIZED" or "BINARY CREATED" warnings indicate a bug
  **Clarification**: These are normal and expected in many cases (e.g., when a binary must be returned from a function). They indicate where optimization cannot be applied, not errors.

- **Confusion**: Believing all warnings can be eliminated through better code
  **Clarification**: The source explicitly states that "all messages that it generates cannot be eliminated." Some sub binary creation is inherent to the program's logic.

# Source Reference

"Constructing and Matching Binaries," section "Option bin_opt_info." The source provides the two invocation methods (compiler flag and environment variable), example output format, and an annotated code example showing how to interpret the warnings.

# Verification Notes

- Definition: Directly from source -- "Use the bin_opt_info option to have the compiler print a lot of information about binary optimizations"
- Invocation methods: Both explicitly shown in source
- Environment variable recommendation: Explicitly stated -- "passing the option through the environment is in most cases the most practical approach"
- Not for permanent use: Explicitly stated -- "bin_opt_info is not meant to be a permanent option added to your Makefiles"
- Warning formats: Directly from source example output
- Annotated code example: Directly from source
- Confidence: HIGH -- explicit section with clear usage instructions and examples in official OTP documentation
