---
# === CORE IDENTIFICATION ===
concept: Library Application
slug: library-application

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
section: "How Applications Run"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "library app"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
extends:
  - otp-application
related:
  - application-resource-file
contrasts_with:
  - otp-application

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an OTP application?"
  - "How do I structure an OTP application?"
---

# Quick Definition

A library application is an OTP application that contains library modules but starts no supervisor or processes of its own; its exported functions are invoked by processes running in other applications.

# Core Definition

There are two types of applications: normal applications and library applications. Library applications contain library modules but do not start a supervisor or processes themselves; the function calls they export are invoked by workers or supervisors running in a different application (Cesarini & Vinoski, p. 205). A typical example is `stdlib`, which contains the OTP standard libraries such as `supervisor`, `gen_event`, `gen_server`, and `gen_fsm`. An application becomes a library application by omitting the `mod` property from its resource file — no supervision tree is then created at startup (pp. 205, 215).

# Prerequisites

- **OTP application** — A library application is one kind of OTP application.

# Key Properties

1. Contains library modules only — no supervisor, no processes.
2. Its exported functions are called by processes in other applications.
3. Created by omitting the `mod` property from the `.app` resource file.
4. Has the standard application directory structure and resource file.
5. The standard `stdlib` application is a library application.

# Construction / Recognition

## To Construct/Create:
1. Build the application with the standard directory structure.
2. Write the `.app` resource file but omit the `mod` property.

## To Identify/Recognize:
1. The `.app` file has no `mod` property.
2. Starting the application creates no supervision tree.

# Context & Application

- **Typical contexts**: Shared utility code packaged for reuse — e.g. `stdlib`.
- **Common applications**: Bundling reusable modules without a process model.
- **Historical/stylistic notes**: The book recommends placing code that must start several identical supervision trees in a standalone library application, to avoid namespace clashes (p. 222).

# Examples

**Example 1** (p. 205): `stdlib` — the library application containing the OTP standard library modules.

**Example 2** (p. 215): The book notes that omitting `mod` results in the application being treated as a library application, started by a supervisor or worker in another application.

## Worked Example

The book gives no full library-application `.app` listing; the defining feature is the absence of `mod`. A library application's resource file looks like:

```erlang
{application, mylib,
 [{description, "Shared utilities"},
  {vsn, "1.0"},
  {modules, [util_a, util_b]},
  {registered, []},
  {applications, [kernel, stdlib]}]}.   %% no mod key -> library application
```

# Relationships

## Builds Upon
- **OTP application** — A library application is a kind of OTP application.

## Enables
- *(none)*

## Related
- **Application resource file** — Omitting the `mod` property is what makes an application a library application.

## Contrasts With
- **OTP application** — A normal application starts a top-level supervisor and supervision tree; a library application starts nothing.

# Common Errors

- **Error**: Including a `mod` property in a library application's `.app` file.
  **Correction**: Omit `mod`; with it, the application would try to start a (nonexistent) supervision tree.

# Common Confusions

- **Confusion**: Thinking a library application is not a "real" OTP application.
  **Clarification**: It is a full OTP application with the standard structure and resource file — it simply starts no processes.

# Source Reference

Chapter 8: Applications, "How Applications Run" and "Application Resource Files" (the `mod` property), pages 205, 215, 222.

# Verification Notes

- Definition source: Direct adaptation from p. 205.
- Confidence rationale: HIGH — explicitly defined and contrasted with normal applications, with `stdlib` as a named example.
- Uncertainties: None.
- Cross-reference status: Verified against planned card slugs for this source.
- Re-extraction notes: Fresh extraction — no pre-existing card for this source.
</content>
