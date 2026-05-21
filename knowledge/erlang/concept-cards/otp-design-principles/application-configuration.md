---
# === CORE IDENTIFICATION ===
concept: Application Configuration
slug: application-configuration

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-runtime
tier: intermediate

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Applications"
chapter_number: null
pdf_page: null
section: "Configuring an Application"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "configuration parameters"
  - "application environment"
  - "app env"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - application
  - application-resource-file
extends: []
related:
  - application-controller
  - distributed-application-configuration
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I create an OTP application?"
---

# Quick Definition

Application configuration is the mechanism by which OTP applications receive runtime parameters, defined as `{Par, Val}` tuples in the `.app` file's `env` key and overridable via system configuration files or command-line arguments.

# Core Definition

According to the OTP Design Principles "Applications" chapter: "An application can be configured using configuration parameters. These are a list of `{Par,Val}` tuples specified by a key `env` in the `.app` file." Configuration values can be retrieved at runtime via `application:get_env(App, Par)`. The source describes a three-level override hierarchy: values in the `.app` file can be overridden by a system configuration file (`Name.config`), and those can be overridden by command-line arguments (`-ApplName Par Val`).

# Prerequisites

- **Application** — configuration parameters belong to an application.
- **Application Resource File** — the `.app` file's `env` key provides default values.

# Key Properties

1. Defined as `{Par, Val}` tuples in the `env` key of the .app file.
2. `Par` must be an atom; `Val` can be any Erlang term.
3. Retrieved at runtime with `application:get_env(App, Par)`.
4. Three-level override hierarchy (lowest to highest priority):
   - Default values in the `.app` file's `env` key.
   - Values in a system configuration file (`Name.config`, loaded with `-config Name`).
   - Command-line arguments (`-ApplName Par1 Val1 ... ParN ValN`).
5. System configuration file format: `[{Application1, [{Par11,Val11},...]},...].`
6. When using release handling, the system configuration file must be named `sys.config`.

# Construction / Recognition

## To Construct/Create:
1. Define default values in the `.app` file using the `env` key: `{env, [{file, "/usr/local/log"}]}`.
2. Optionally create a system configuration file `Name.config` to override defaults.
3. Start Erlang with `-config Name` to load the configuration file.
4. Optionally pass command-line overrides with `-ApplName Par Val`.

## To Identify/Recognize:
1. The `env` key in an application's `.app` file.
2. Calls to `application:get_env/2` in application code.
3. `.config` files containing application configuration tuples.

# Context & Application

Application configuration provides a standardized way to parameterize OTP applications without modifying code. The override hierarchy allows the same application to run with different settings in different environments: defaults in the .app file for development, a sys.config for production releases, and command-line overrides for ad-hoc testing.

# Examples

**Example 1** (applications.md, "Configuring an Application"): Defining a configuration parameter in the .app file and reading it at runtime:
```erlang
{application, ch_app,
 [...
  {env, [{file, "/usr/local/log"}]}
 ]}.
```
```erlang
1> application:start(ch_app).
ok
2> application:get_env(ch_app, file).
{ok,"/usr/local/log"}
```

**Example 2** (applications.md, "Configuring an Application"): Overriding via a system configuration file `test.config`:
```erlang
[{ch_app, [{file, "testlog"}]}].
```
```erlang
% erl -config test
1> application:start(ch_app).
ok
2> application:get_env(ch_app, file).
{ok,"testlog"}
```

**Example 3** (applications.md, "Configuring an Application"): Overriding via command-line arguments:
```erlang
% erl -ch_app file '"testlog"'
1> application:start(ch_app).
ok
2> application:get_env(ch_app, file).
{ok,"testlog"}
```

# Relationships

## Builds Upon
- **Application** — configuration parameters belong to an application.
- **Application Resource File** — the .app file provides default configuration values.

## Enables
- **Distributed Application Configuration** — distributed applications use Kernel configuration parameters for node coordination.

## Related
- **Application Controller** — the controller stores and provides access to configuration values.
- **Release Handling** — release handling requires `sys.config` as the system configuration file.

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Forgetting to quote Erlang terms when passing configuration via the command line.
  **Correction**: The source shows command-line values must be valid Erlang terms, e.g., `'"testlog"'` (single-quoted to protect the double quotes from the shell).

# Common Confusions

- **Confusion**: Thinking command-line configuration values override the system configuration file at load time.
  **Clarification**: All three levels (`.app` defaults, system config file, command-line) participate in a priority hierarchy. Command-line values have the highest priority, then system config file values, then `.app` defaults.

# Source Reference

OTP Design Principles, "Applications" chapter, "Configuring an Application" section (applications.md).

# Verification Notes

- Definition source: Directly from applications.md "Configuring an Application" section with all three override examples quoted.
- Confidence rationale: High — explicitly documented with format, API, and three concrete examples.
- Uncertainties: None.
- Cross-reference status: References application, application-resource-file, application-controller, distributed-application-configuration.
