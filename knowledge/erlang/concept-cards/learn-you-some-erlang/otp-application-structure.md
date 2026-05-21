---
concept: OTP Application Structure
slug: otp-application-structure
category: applications-releases
subcategory: applications
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building Applications the OTP Way"
chapter_number: 19
pdf_page: null
section: "My Other Car Is a Pool"
extraction_confidence: high
aliases:
  - application directory layout
  - application directory structure
  - "ebin/src/include/priv layout"
prerequisites:
  - otp-application
extends: []
related:
  - app-file
  - rebar-build-tool
contrasts_with: []
answers_questions:
  - "How do I structure an OTP application?"
  - "What is an OTP application?"
---

# OTP Application Structure

## Quick Definition

An OTP application uses a standard directory layout — `ebin/`, `include/`, `priv/`, `src/` (plus optional `test/`, `doc/`) — so the VM and tools know where to find compiled code, headers, source, and assets.

## Core Definition

The book prescribes copying application files "into a neat directory structure" with `ebin/`, `include/`, `priv/`, `src/` (and `test/`). "The four basic directories to have are `ebin/`, `include/`, `priv/`, and `src/`. These are common to pretty much every OTP application, although only `ebin/` and `priv/` will be exported when real OTP systems are deployed" (Ch. 19, "My Other Car Is a Pool").

## Prerequisites

- **OTP application** — The structure is the layout of an OTP application.

## Key Properties

1. **`ebin/`** — Holds compiled `.beam` files and the application resource (`.app`) file.
2. **`include/`** — Holds public Erlang header (`.hrl`) files.
3. **`priv/`** — Holds executables, other programs, and application-specific assets.
4. **`src/`** — Holds Erlang source files (and private `.hrl` files).
5. **`test/`** — Holds test files; common but not distributed as part of the app.
6. **`doc/`** — Created when EDoc documentation is generated.
7. Only `ebin/` and `priv/` are exported when a real OTP system is deployed.

## Construction / Recognition

## To Lay Out an Application

1. Create `ebin/`, `include/`, `priv/`, `src/`.
2. Put source modules in `src/`; compile them into `ebin/`.
3. Put the `.app` file in `ebin/` (or `.app.src` in `src/` if a build tool generates it).
4. Put public headers in `include/`, assets in `priv/`.
5. Add `test/` for tests, `doc/` for generated docs as needed.

## Context & Application

The book converts the `ppool` application into this layout, moving the demo-only `ppool_nagger.erl` into `test/` since "it is not much more than a demo case and will have nothing to do with our application." An `Emakefile` at the app's base directory tells the compiler to read from `src/` and `test/` and write `.beam` files to `ebin/`. Modern projects use rebar3, which assumes this layout.

## Examples

**Example 1** (Ch. 19): `ppool` laid out as `ebin/`, `include/`, `priv/`, `src/` (the five `ppool_*.erl` modules), and `test/`.

**Example 2** (Ch. 20): `erlcount` uses the same layout, with five `erlcount_*` modules in `src/` and `erlcount.app` in `ebin/`.

## Relationships

## Builds Upon

- **OTP application** — The structure organises an application.

## Related

- **app-file** — Lives in `ebin/` (or as `.app.src` in `src/`).
- **rebar-build-tool** — Understands and assumes this structure.

## Common Errors

- **Error**: Placing the `.app` file outside `ebin/` without a build tool to copy it.
  **Correction**: Either put it directly in `ebin/`, or keep `myapp.app.src` in `src/` and let the build tool copy/generate it.

## Common Confusions

- **Confusion**: Thinking all four directories are shipped on deployment.
  **Clarification**: Only `ebin/` and `priv/` are exported in a deployed OTP system; `src/`, `include/`, and `test/` are development artifacts.

## Source Reference

Chapter 19: "Building Applications the OTP Way," section "My Other Car Is a Pool"; also "Converting the Pool" (the `Emakefile`).

## Verification Notes

- Definition: Direct quotes from "My Other Car Is a Pool."
- Key Properties: Each directory's purpose copied from the source.
- Confidence: HIGH — explicitly described.
