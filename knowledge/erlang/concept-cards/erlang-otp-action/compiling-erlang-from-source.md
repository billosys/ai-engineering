---
# === CORE IDENTIFICATION ===
concept: Compiling Erlang from Source
slug: compiling-erlang-from-source

# === CLASSIFICATION ===
category: tooling
subcategory: installation
tier: foundational

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Appendix A"
chapter_number: null
pdf_page: null
section: "A.2.1. Compiling from source"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "building Erlang from source"
  - "configure make make install"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you compile and install Erlang from source?"
  - "What libraries are needed to build Erlang?"
  - "How do you install Erlang to a non-default location?"
---

# Quick Definition

Compiling Erlang from source is the standard configure/make/make-install build on UNIX-like systems, and is the surest way to get the latest version.

# Core Definition

On UNIX-like systems, building and installing Erlang from source is the best way to ensure you have the latest version. You download the latest source package from the Erlang site, unpack it, `cd` into the directory, and run the `./configure` script — optionally with a `--prefix=...` flag to install somewhere other than the default `/usr/local/lib/erlang`. You then run `make` and `make install` (the install step usually needs root privileges, e.g. `sudo make install`, when installing to the default location). Afterward, `erl` starts Erlang and `erlc` runs the compiler; for a non-standard location, the install's `bin` subdirectory must be on `PATH`. To compile, certain libraries and tools must already be present (Appendix A, Section A.2.1).

# Prerequisites

This is a foundational installation procedure with no conceptual prerequisites within this source.

# Key Properties

1. The build is the standard `./configure`, `make`, `make install` sequence.
2. Building from source ensures the latest Erlang version, unlike some package managers.
3. The default install location is `/usr/local/lib/erlang`; `--prefix=...` overrides it.
4. `make install` to the default location usually needs root privileges (`sudo`).
5. A working GCC environment and Ncurses development libraries are required to compile.
6. Missing OpenSSL, ODBC, or Java only produce configure warnings — some applications simply will not be built.
7. After installing to a non-standard path, its `bin` subdirectory must be added to `PATH`.

# Construction / Recognition

## To Construct/Create:
1. Download the latest source package from `www.erlang.org/download.html`.
2. Untar the package and `cd` into the directory.
3. Run `./configure` (add `--prefix=/your/path` for a custom location).
4. Run `make`.
5. Run `make install` (use `sudo make install` for the default location).
6. Verify with `erl` and `erlc`; add the `bin` directory to `PATH` if non-standard.

# Context & Application

- **Typical contexts**: Installing Erlang on macOS, Linux, or other UNIX-like systems.
- **Common applications**: Getting a current Erlang/OTP release for development.
- **Historical/stylistic notes**: Package managers (Ubuntu's synaptic, Homebrew on macOS) are alternatives but may lag the latest release.

# Examples

**Example 1** (Section A.2.1): `./configure --prefix=/home/jdoe/lib` configures an install into a user directory.

**Example 2** (Section A.2.2): Missing OpenSSL, ODBC, or Java development libraries cause configure warnings; re-running `./configure`, `make`, `make install` after installing them enables those applications.

# Relationships

This procedure stands largely on its own within the source; no typed concept relationships apply.

# Common Errors

- **Error**: Running `make install` to the default location without root privileges.
  **Correction**: Use `sudo make install` when installing to `/usr/local/lib/erlang`.

- **Error**: Installing to a custom prefix and then finding `erl` is not found.
  **Correction**: Add the install's `bin` subdirectory to the `PATH` environment variable.

# Common Confusions

- **Confusion**: Assuming a package-manager install always gives the latest Erlang.
  **Clarification**: Package managers may lag; building from source guarantees the current release.

# Source Reference

Appendix A: Installing Erlang, Sections A.2.1 "Compiling from source" and A.2.2 "Resolving configuration problems."

# Verification Notes

- Definition source: Direct adaptation of Sections A.2.1-A.2.2.
- Confidence rationale: HIGH — the procedure is explicitly described.
- Uncertainties: None.
- Cross-reference status: No cross-references; standalone procedure.
- Re-extraction notes: Fresh extraction; no prior card. Windows install and package-manager paths were judged too procedural/thin to warrant separate cards.
</content>
