---
concept: Application Environment Variable
slug: application-environment-variable
category: applications-releases
subcategory: applications
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Count of Applications"
chapter_number: 20
pdf_page: null
section: "The Application File"
extraction_confidence: high
aliases:
  - "env tuple"
  - application configuration
  - application environment
prerequisites:
  - app-file
extends: []
related:
  - app-file
  - otp-application
contrasts_with: []
answers_questions:
  - "How do I structure an OTP application?"
  - "What is an OTP application?"
---

# Application Environment Variable

## Quick Definition

Application environment variables are an application's key/value configuration store, declared in the `.app` file's `{env, [{Key, Val}]}` tuple and read at runtime with `application:get_env`.

## Core Definition

"`{env, [{Key, Val}]}` ... is a list of key/values that can be used as a configuration for your application. They can be obtained at runtime by calling `application:get_env(Key)` or `application:get_env(AppName, Key)`" (Ch. 19, "The Application Resource File"). Chapter 20 adds: "This entire tuple gives us a key/value store for application-specific configuration variables. These variables will be accessible from all the processes running within the application, stored in memory."

## Prerequisites

- **App file** — Environment variables are declared in the `.app` file's `env` tuple.

## Key Properties

1. Declared as `{env, [{Key, Val}, ...]}` in the `.app` file.
2. Read with `application:get_env(Key)` (current app) or `application:get_env(AppName, Key)`.
3. Accessible from all processes within the application, stored in memory.
4. Can be overwritten at boot time or with `application:set_env(Application, Key, Value)`.
5. Because they are overridable, the `env` tuple is usually used for *default* values.
6. They serve as a substitute for ad-hoc external configuration files.

## Construction / Recognition

## To Use Environment Variables

1. Add `{env, [{Key, DefaultVal}, ...]}` to the `.app` file.
2. Read a value with `application:get_env(AppName, Key)`.
3. Override at boot (e.g. via the `erl` command line) or with `application:set_env/3`.

## Context & Application

`erlcount` defines three env variables: `directory` (where to look for `.erl` files), `max_files` (how many file descriptors at once), and `regex` (the list of regular expressions to run). The book notes env vars "can basically be used as a substitute configuration file for your app," sparing developers from "a bunch of configuration files to read in some arbitrary format." In Chapter 21, the release is run with `-erlcount directory '"<path>"'` to override `erlcount`'s `directory` env variable from the command line.

## Examples

**Example 1** (Ch. 20): `erlcount.app` declares `{env, [{directory, "."}, {regex, ["if\\s.+->", "case\\s.+\\sof"]}, {max_files, 10}]}`.

**Example 2** (Ch. 21): Running the release with `-erlcount directory '"/home/ferd/code/..."'` overrides the `directory` env variable.

## Relationships

## Builds Upon

- **App file** — Env variables live in the `env` tuple.

## Related

- **otp-application** — Env variables are per-application configuration.

## Common Errors

- **Error**: Using `application:get_env(Key)` from a process not in the intended application.
  **Correction**: Use `application:get_env(AppName, Key)` to be explicit about which application's env you read.

## Common Confusions

- **Confusion**: Confusing application environment variables with OS environment variables.
  **Clarification**: These are OTP application configuration values stored in the VM's memory, unrelated to the operating system's environment.

## Source Reference

Chapter 20: "The Count of Applications," section "The Application File"; original definition in Chapter 19, "The Application Resource File"; runtime override in Chapter 21, "Packaging the Release."

## Verification Notes

- Definition: Direct quotes from both chapters.
- Key Properties: Synthesised from the `env` tuple description and the `erlcount` usage.
- Confidence: HIGH — explicitly defined with worked usage.
