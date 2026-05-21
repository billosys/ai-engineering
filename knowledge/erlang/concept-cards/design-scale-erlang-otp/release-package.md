---
# === CORE IDENTIFICATION ===
concept: Release Package
slug: release-package

# === CLASSIFICATION ===
category: applications-releases
subcategory: system-principles
tier: intermediate

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "System Principles and Release Handling"
chapter_number: 10
pdf_page: 282
section: "Creating a Release Package"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - release tar file
  - deployment package
  - target tar file

# === TYPED RELATIONSHIPS ===
prerequisites:
  - release
  - boot-file
extends: []
related:
  - release-directory-structure
  - target-system
  - systools
  - start-scripts-and-configuration
  - rebar3
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a release package?"
  - "How do I package, start, and configure a release?"
---

# Quick Definition

A release package is the deployable artifact built from a release — most simply a tar file — containing the `lib`, `releases`, and optionally `erts` directories. It is created with `systools:make_tar/2` and unpacked into the target environment.

# Core Definition

The release package is the deployment artifact created in the final step of building a release: a deployment package specific to the target environment — a tar file, a Debian or Solaris package, a container, or any other deployable instance (Cesarini & Vinoski, p. 273, 283-285, pdf p. 282). The book builds it as a gzipped tar file using `systools:make_tar/2`, which generates `ReleaseName.tar.gz` containing the `lib` directory (all application versions from the `.rel` file), the `releases` directory, and — if the `{erts, Dir}` directive is given — the `erts` directory with the runtime binaries.

# Prerequisites

- **Release** — The package is built from a release; the release concept comes first.
- **Boot file** — The boot file must exist before `make_tar/2` can package it.

# Key Properties

1. Most commonly a gzipped tar file (`ReleaseName.tar.gz`); can also be a deb/pkg/rpm or container.
2. Created by `systools:make_tar(Name, OptionsList)`.
3. Contains the `lib` and `releases` directories; includes `erts` only when `{erts, Dir}` is passed.
4. The `sys.config` file is included in `releases/Vsn` if it sits alongside the `.rel` file.
5. `OptionsList` accepts all `make_script` options plus `{erts, Dir}`, `{dirs, IncDirList}`, `{outdir, Dir}`, `{variables,...}`, and `{var_tar, VarTar}`.
6. After untarring, target-specific scripts, config files, and environment variables are fixed up — manually or by an automated build process.
7. There is no "one size fits all" package format or build/install boundary.

# Construction / Recognition

## To Create a Release Package:
1. Place the `.rel` file, boot files, and `sys.config` in a working directory.
2. Call `systools:make_tar(Name, OptionsList)`, optionally passing `{erts, Dir}` to include the runtime.
3. Untar the resulting `ReleaseName.tar.gz` in the target directory.
4. Fix up start scripts, config files, and target-specific environment variables.

## To Recognize It:
1. Look for a `ReleaseName.tar.gz` (or OS-specific package).
2. Untarring it reveals `lib`, `releases`, and optionally `erts`.

# Context & Application

- **Typical contexts**: Producing a deployable artifact at the end of a build.
- **Common applications**: Deploying the same tar file to thousands of independent installations, or to multiple node instances on one host.
- **Historical/stylistic notes**: Configuration scripts can be proprietary and bundled, or managed by third-party tools such as Chef, Puppet, or Capistrano.

# Examples

**Example 1** (p. 284): Building and unpacking the package:

```erlang
1> systools:make_tar("basestation",
     [{erts, "/usr/local/lib/erlang/"},
      {path, ["bsc/ebin"]}, {outdir, "ernie"}]).
ok
```

```
$ cd ernie
$ tar xf basestation.tar.gz
$ ls
basestation.tar.gz  lib  erts-7.2  releases
```

**Example 2** (p. 285): The `{dirs, IncDirList}` option copies extra directories — e.g. `[tests, src, examples]` — into the application subdirectories, in addition to the defaults `priv` and `ebin`.

# Relationships

## Builds Upon
- **Release** — The package is the deployable form of a release.
- **Boot file** — Bundled into the package.

## Related
- **Release directory structure** — The package, once unpacked, follows this layout.
- **Target system** — The package is installed to create a running target system.
- **systools** — `make_tar/2` builds the package.
- **Start scripts and configuration** — Configured after the package is unpacked.
- **Rebar3** — Automates package creation via `rebar3 tar`.

# Common Errors

- **Error**: Omitting `sys.config` from the package and from the installation.
  **Correction**: `sys.config` is optional at packaging time but mandatory at install time; if omitted from the package, add it during installation or the system will not start.

- **Error**: Including `erts` binaries built for the wrong OS/hardware.
  **Correction**: Make sure the runtime binaries are compiled and tested on the target platform before passing `{erts, Dir}`.

# Common Confusions

- **Confusion**: Thinking the package must always be a tar file.
  **Clarification**: A tar file is the simplest form; the package can equally be a deb, pkg, rpm, or container.

- **Confusion**: Believing the package always contains the runtime.
  **Clarification**: `erts` is included only when `{erts, Dir}` is passed; otherwise the target relies on a pre-installed runtime.

# Source Reference

Chapter 10: System Principles and Release Handling, section "Creating a Release Package," pages 283-286 (pdf p. 282). See the `systools:make_tar/2` option list on pp. 285-286.

# Verification Notes

- Definition source: Direct adaptation of pp. 273 and 283-286.
- Confidence rationale: HIGH — the source explicitly walks through creating the package and the `make_tar/2` options.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
