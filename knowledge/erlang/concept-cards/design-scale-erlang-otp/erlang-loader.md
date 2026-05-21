---
# === CORE IDENTIFICATION ===
concept: Erlang Loader
slug: erlang-loader

# === CLASSIFICATION ===
category: applications-releases
subcategory: code-loading
tier: advanced

# === PROVENANCE ===
source: "Designing for Scalability with Erlang/OTP"
source_slug: design-scale-erlang-otp
authors: Francesco Cesarini & Steve Vinoski
chapter: "System Principles and Release Handling"
chapter_number: 10
pdf_page: 282
section: "The Erlang loader"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - erl_prim_loader
  - boot server
  - erl_boot_server

# === TYPED RELATIONSHIPS ===
prerequisites:
  - code-loading-and-code-paths
  - system-boot-process
extends: []
related:
  - boot-file
  - arguments-and-flags
  - init-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Erlang loader and how can a node boot over the network?"
  - "How does the system boot process work?"
---

# Quick Definition

The Erlang loader (`erl_prim_loader`) is the module that fetches and loads modules during startup. Its method is chosen by the `-loader` flag: `efile` reads from the local filesystem, `inet` loads from a remote boot server.

# Core Definition

The `-loader` argument specifies how `erl_prim_loader` fetches the modules (Cesarini & Vinoski, p. 300-302, pdf p. 282). The default loader, `efile`, retrieves the modules from the local filesystem. To load from a boot server on another machine, the `inet` loader is specified. When using `inet`, you must include the name of the remote node where the boot server is running via `-id name`, and the IP address of that machine via `-hosts address`. The boot server is started on the remote node with `erl_boot_server:start/1`.

# Prerequisites

- **Code loading and code paths** — The loader is part of how modules are located and loaded.
- **System boot process** — The loader operates during the boot process to load modules.

# Key Properties

1. `erl_prim_loader` is a preloaded module that fetches and loads modules.
2. The loading method is set by the `-loader` flag.
3. `efile` (default) — retrieves modules from the local filesystem.
4. `inet` — loads modules from a remote boot server over the network.
5. With `inet`, `-id name` names the remote boot-server node and `-hosts address` gives its IP.
6. The boot server is started with `erl_boot_server:start([IpAddress])`.
7. Useful for embedded devices with little or no disk space.

# Construction / Recognition

## To Boot Over the Network:
1. Generate the boot file with the `local` option so local beam files are found: `systools:make_script("basestation", [local])`.
2. Start the boot server node: `erl_boot_server:start([{127,0,0,1}])`.
3. Start the client node with `-loader inet -id <server> -hosts <ip> -boot <name>`.

## To Recognize It:
1. The `-loader inet` flag in a start command.
2. A node running `erl_boot_server`.

# Context & Application

- **Typical contexts**: Booting a release on embedded devices with little or no disk space.
- **Common applications**: Loading modules from a database or another node across the network rather than from a local file.
- **Historical/stylistic notes**: The book's example uses the local host (`127.0.0.1`), but the technique works across two different hosts on a network.

# Examples

**Example 1** (p. 300): Generating a boot file for network loading with the critical `local` option:

```erlang
1> systools:make_script("basestation", [local]).
ok
```

**Example 2** (p. 301): Starting the boot server, then the client node:

```erlang
(foo@127.0.0.1)1> erl_boot_server:start([{127,0,0,1}]).
{ok,<0.42.0>}
```

```
$ erl -name bar@127.0.0.1 -id foo -hosts 127.0.0.1 \
  -loader inet -setcookie cookie -boot basestation
```

# Relationships

## Builds Upon
- **Code loading and code paths** — The loader implements module fetching.
- **System boot process** — The loader runs during boot to load modules.

## Related
- **Boot file** — The boot file's `primLoad` actions use `erl_prim_loader:get_file/1`.
- **Arguments and flags** — `-loader`, `-id`, and `-hosts` configure the loader.
- **Init module** — `init` interprets the boot file and works with the loader.

# Common Errors

- **Error**: Generating the boot file without the `local` option for network loading.
  **Correction**: The `local` option adds the local path to the boot server's load path so `make_script` succeeds without installing beam files into `lib`.

- **Error**: Omitting `-id` or `-hosts` when using `-loader inet`.
  **Correction**: Both are required — `-id` names the boot-server node, `-hosts` gives its IP address.

# Common Confusions

- **Confusion**: Thinking the loader can only read from the local filesystem.
  **Clarification**: The default `efile` loader reads locally, but the `inet` loader can fetch modules from a remote boot server.

- **Confusion**: Believing network loading requires two physical hosts to demonstrate.
  **Clarification**: It can be demonstrated on the local host (`127.0.0.1`), though it genuinely works across the network.

# Source Reference

Chapter 10: System Principles and Release Handling, section "The Erlang loader," pages 300-302 (pdf p. 282). See also the `erl_boot_server`, `erl_prim_loader`, and `init` reference manual pages.

# Verification Notes

- Definition source: Direct adaptation of pp. 300-302.
- Confidence rationale: HIGH — the source explicitly describes the loader, the `-loader` flag, and the boot server.
- Uncertainties: None.
- Cross-reference status: Verified against planned cards.
- Re-extraction notes: Fresh extraction; no pre-existing card.
