---
# === CORE IDENTIFICATION ===
concept: Application priv Directory
slug: priv-directory

# === CLASSIFICATION ===
category: applications-releases
subcategory: application-structure
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Integrating with foreign code using ports and NIFs"
chapter_number: 12
pdf_page: null
section: "12.2.1. The Erlang side of the port"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - priv dir
  - "code:priv_dir/1"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - otp-application
extends: []
related:
  - open-port
  - linked-in-driver
  - nif
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the priv directory of an application?"
  - "How do you locate an application's priv directory?"
  - "Why might code:priv_dir/1 fail during shell testing?"
---

# Quick Definition

The `priv` directory is an application's location for non-Erlang resources — such as external port programs and shared libraries — found at runtime via `code:priv_dir(AppName)`.

# Core Definition

The normal location for external programs that are part of your application is the `priv` directory (or a subdirectory thereof). You can always get the path of the `priv` directory of any application by calling `code:priv_dir/1` with the application name. This function searches the code path for the given application name: if the path contains a directory `.../foo/ebin`, then `code:priv_dir(foo)` returns the corresponding `.../foo/priv` directory ("Erlang and OTP in Action," Ch. 12, Section 12.2.1, Note and sidebar "The application directory and the code path").

# Prerequisites

- **OTP application** — `priv` is a standard directory within an application.

# Key Properties

1. The standard location for an application's non-Erlang resources (external programs, shared libraries, data files).
2. Located via `code:priv_dir(AppName)`, which searches the code path.
3. `code:priv_dir(foo)` returns `.../foo/priv` when the code path contains `.../foo/ebin`.
4. By default a release package includes the `priv` directory (alongside `ebin`) for each application.
5. External port programs and `.so`/`.dll` driver and NIF libraries are placed here (or a subdirectory).

# Construction / Recognition

## To Construct/Create:
1. Create a `priv` directory beside the application's `ebin` and `src` directories.
2. Place external executables, shared libraries, and data files in it.
3. At runtime, locate them with `filename:join([code:priv_dir(AppName), "file"])`.

## To Identify/Recognize:
1. A directory named `priv` within an application's directory tree.

# Context & Application

- **Typical contexts**: Bundling compiled C programs or shared libraries with an Erlang application.
- **Common applications**: The `jp_prog` external program, `jp_driver.so` linked-in driver, and `jp_nifs.so` NIF library all live in `priv`.
- **Historical/stylistic notes**: When testing from the shell with `erl -pa ./ebin`, the system has no clue about the application name, so `code:priv_dir/1` fails — start with `erl -pa ../foo/ebin` instead.

# Examples

**Example 1** (Section 12.2.1): The Erlang side gets `code:priv_dir(?APPNAME)` and joins it with `"jp_prog"` to find the external program.

**Example 2** (Section 12.2.1 sidebar): `erl -pa ./ebin` makes `priv_dir(foo)` fail to locate application `foo`; `erl -pa ../foo/ebin` works.

# Relationships

## Builds Upon
- **OTP application** — `priv` is part of the application directory structure.

## Related
- **open_port BIF** — External port programs in `priv` are launched with `open_port`.
- **Linked-in driver** — Driver `.so`/`.dll` files are placed in `priv`.
- **NIF** — NIF shared libraries are placed in `priv`.

# Common Errors

- **Error**: Starting Erlang with `erl -pa ./ebin` and expecting `code:priv_dir/1` to work.
  **Correction**: Use `erl -pa ../AppName/ebin` so the system can derive the application name.

# Common Confusions

- **Confusion**: Thinking `priv` holds compiled Erlang `.beam` files.
  **Clarification**: `.beam` files live in `ebin`; `priv` holds non-Erlang resources such as external programs and libraries.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Section 12.2.1 — the Note and the sidebar "The application directory and the code path."

# Verification Notes

- Definition source: Direct adaptation of the Note and sidebar in Section 12.2.1.
- Confidence rationale: HIGH — the book explicitly explains the `priv` directory and `code:priv_dir/1`.
- Uncertainties: None.
- Cross-reference status: `otp-application` owned by Agent 2.
- Re-extraction notes: Fresh extraction; no prior card existed.
