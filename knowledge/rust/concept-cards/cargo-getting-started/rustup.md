---
# === CORE IDENTIFICATION ===
concept: Rustup
slug: rustup

# === CLASSIFICATION ===
category: tooling
subcategory: installers
tier: foundational

# === PROVENANCE ===
source: "Cargo Getting Started"
source_slug: cargo-getting-started
authors: "The Cargo Team"
chapter: "Installation"
chapter_number: 1
pdf_page: null
section: "Install Rust and Cargo"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - rustup-init
  - rustup-init.exe

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - rust-release-channels
  - cargo-build
  - cargo-run
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is rustup?"
  - "How does rustup relate to Cargo installation?"
  - "How do I install Rust and Cargo?"
  - "What do I need before I can use Cargo?"
---

# Quick Definition

Rustup is the official installer and version manager for Rust and Cargo. It provides the easiest way to install the Rust toolchain and manage release channels.

# Core Definition

Rustup is the recommended tool for installing the Rust programming language and its package manager, Cargo. The source describes it as "the easiest way to get Cargo" and states that "installing Rust using `rustup` will also install `cargo`" (Cargo Getting Started, Ch. 1: Installation). Rustup also enables switching between release channels (stable, beta, nightly) after initial installation.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. Installs both Rust and Cargo together in a single operation
2. Available on Linux, macOS (via shell script), and Windows (via `rustup-init.exe`)
3. Supports installing additional release channels (beta, nightly) after initial setup
4. Uses `curl https://sh.rustup.rs -sSf | sh` on Linux and macOS
5. The `rustup` command remains available after installation for managing channels

# Construction / Recognition

## To Install Rust and Cargo via Rustup:

### On Linux and macOS:
1. Run `curl https://sh.rustup.rs -sSf | sh`
2. Wait for the script to download and execute
3. Confirm installation succeeds when you see "Rust is installed now. Great!"

### On Windows:
1. Download and run `rustup-init.exe` from https://win.rustup.rs/
2. Follow the console prompts
3. Confirm success message appears

## To Install Additional Release Channels:
1. Use the `rustup` command after initial installation
2. Specify the desired channel (e.g., `beta` or `nightly`)

# Context & Application

Rustup is the first tool a new Rust developer encounters. It is the recommended entry point for setting up a Rust development environment, and it ensures that both the Rust compiler and Cargo are installed and properly configured. The alternative is building Cargo from source, which the documentation mentions but does not recommend for typical users.

# Examples

**Example 1** (Ch 1): Linux/macOS installation command:
```console
curl https://sh.rustup.rs -sSf | sh
```
Expected output on success: `Rust is installed now. Great!`

**Example 2** (Ch 1): After initial installation, using rustup to install additional channels:
```console
rustup install nightly
```

# Relationships

## Builds Upon
- None -- this is a foundational entry point

## Enables
- **rust-release-channels** -- rustup provides the mechanism to install and switch between channels
- **cargo-build** -- Cargo must be installed (via rustup) before building
- **cargo-run** -- Cargo must be installed (via rustup) before running
- **cargo-new** -- Cargo must be installed (via rustup) before creating packages

## Related
- **rust-release-channels** -- rustup manages channel installations

## Contrasts With
- None within this source

# Common Errors

- **Error**: Forgetting to source the environment after installation on Linux/macOS (shell PATH not updated).
  **Correction**: Start a new terminal session or source the appropriate profile file after installation.

- **Error**: Running the curl command without the `-sSf` flags.
  **Correction**: Use the exact command `curl https://sh.rustup.rs -sSf | sh` to ensure silent operation with failure reporting.

# Common Confusions

- **Confusion**: Believing you need to install Cargo separately from Rust.
  **Clarification**: Installing Rust via rustup automatically installs Cargo as well. They come bundled together.

- **Confusion**: Thinking rustup is only an installer and has no further use after installation.
  **Clarification**: Rustup remains useful for managing release channels (stable, beta, nightly) and updating the toolchain.

# Source Reference

Chapter 1: Installation, section "Install Rust and Cargo." No page numbers (online documentation source).

# Verification Notes

- Definition source: Directly from Ch 1 text -- "The easiest way to get Cargo is to install the current stable release of Rust by using rustup"
- Confidence rationale: HIGH -- the source explicitly names rustup and describes its purpose and usage clearly
- Uncertainties: None for the core definition; the source provides limited detail on advanced rustup features
- Cross-reference status: All slugs reference cards planned in this extraction set
