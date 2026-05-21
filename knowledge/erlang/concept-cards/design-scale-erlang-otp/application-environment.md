---
# === CORE IDENTIFICATION ===
concept: Application Environment
slug: application-environment

# === CLASSIFICATION ===
category: applications-releases
subcategory: applications
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: "Francesco Cesarini & Steve Vinoski"
chapter: "Applications"
chapter_number: 8
pdf_page: 222
section: "Environment Variables"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "application environment variables"
  - "application configuration parameters"
  - "env"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
  - application-resource-file
extends: []
related:
  - application-controller
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I package, start, and configure a release?"
  - "How do I structure an OTP application?"
---

# Quick Definition

The application environment is the set of `{Key, Value}` configuration parameters belonging to an application, used to initialize its behaviors. Values come from the `.app` file and can be overridden by a system config file or the command line.

# Core Definition

Erlang uses environment variables mainly to obtain configuration parameters when initializing application behaviors (Cesarini & Vinoski, p. 217). They are set in the `env` attribute of the application resource file and can be retrieved with `application:get_env/1,2` and `get_all_env/0,1`. They are *not* operating-system environment variables. Default values in the `.app` file can be overridden, in order of increasing precedence, by a system configuration file (a `.config` file passed with `erl -config`), and by command-line flags (`erl -application key value`). Values can also be set at runtime with `application:set_env`, though the book advises caution (pp. 217-219).

# Prerequisites

- **OTP application** — Environment variables belong to an application.
- **Application resource file** — Defaults are set in the `.app` file's `env` property.

# Key Properties

1. A list of `{Key, Value}` tuples per application.
2. Defaults are declared in the `env` property of the `.app` file.
3. Retrieved with `application:get_env(Key)` / `get_env(App, Key)` / `get_all_env/0,1`.
4. Inside an application's supervision tree, the application name may be omitted (the runtime uses the process's group leader).
5. Overridable, lowest to highest precedence: `.app` file → system config file → command-line `-application` flag.
6. They are distinct from OS environment variables.

# Construction / Recognition

## To Construct/Create:
1. Declare defaults in the `.app` file's `env` property.
2. Override per deployment in a `.config` system configuration file.
3. Optionally override at startup with `erl -application key value`.

## To Identify/Recognize:
1. `{Key, Value}` pairs returned by `application:get_all_env(App)`.
2. The `env` property in the `.app` file.

# Context & Application

- **Typical contexts**: Configuring application behaviors at startup.
- **Common applications**: Supplying `sasl` logging settings; supplying the `bsc` frequency list.
- **Historical/stylistic notes**: The book warns that command-line overrides should not be used for production; stick to `.app` and `.config` files for clarity (p. 218).

# Examples

**Example 1** (p. 219): A `bsc.config` file overriding `sasl`'s `errlog_type` and `sasl_error_logger`, and setting `bsc`'s `frequencies` to `[1,2,3,4,5,6]`.

**Example 2** (p. 220): `frequency:get_frequencies/0` reading the `frequencies` env variable, defaulting to a hardcoded list if `undefined`.

## Worked Example

A system configuration file setting environment variables (p. 219):

```erlang
[{sasl, [{errlog_type, error}, {sasl_error_logger, tty}]},
 {bsc,  [{frequencies, [1,2,3,4,5,6]}]}].
```

Reading a variable in code (p. 220):

```erlang
get_frequencies() ->
    case application:get_env(frequencies) of
        {ok, FreqList} -> FreqList;
        undefined      -> [10,11,12,13,14,15]
    end.
```

# Relationships

## Builds Upon
- *(none)*

## Enables
- *(none)*

## Related
- **Application controller** — Reads the system configuration file that supplies environment values.

## Contrasts With
- *(none)*

# Common Errors

- **Error**: Using `application:set_env` on a third-party application at runtime.
  **Correction**: Changing env variables of an application you do not know well after it has started can cause inconsistent state; prefer `.app`/`.config` files.

- **Error**: Confusing application env variables with OS environment variables.
  **Correction**: They are unrelated; application env variables are OTP configuration parameters.

# Common Confusions

- **Confusion**: Thinking the application name is always required to read an env variable.
  **Clarification**: A process inside the application's supervision tree may omit it; the runtime resolves the application from the process's group leader.

# Source Reference

Chapter 8: Applications, "Environment Variables," pages 217-220.

# Verification Notes

- Definition source: Direct adaptation from pp. 217-220.
- Confidence rationale: HIGH — explicitly defined with config-file and code examples.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
