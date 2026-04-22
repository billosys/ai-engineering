---
# === CORE IDENTIFICATION ===
concept: Rust Compiler Development Practices
slug: rustc-compiler-dev-practices

# === CLASSIFICATION ===
category: compiler-internals
subcategory: development-process
tier: intermediate

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Development Practices, Notification Groups"
chapter_number: 6-7
pdf_page: null
section: "Coding Conventions, Breaking Changes, External Repos, Fuzzing, Editions, Notification Groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rustc coding conventions"
  - "compiler coding style"
  - "breaking change procedure"
  - "crater runs"
  - "future compatibility lints"
  - "notification groups"
  - "edition support in rustc"
  - "subtree dependencies"
  - "compiler fuzzing"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - rustc-feature-lifecycle
  - rustc-compiler-overview
  - rustc-compiler-bootstrapping
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What coding conventions does the Rust compiler follow?"
  - "How do I format code in the rustc repository?"
  - "What is the procedure for making breaking changes in rustc?"
  - "What is a crater run and when should I do one?"
  - "What are future-compatibility lints and how do I create one?"
  - "How do external dependencies (subtrees and submodules) work in rust-lang/rust?"
  - "What are notification groups and how do I join one?"
  - "How does edition support work inside the compiler?"
  - "What is edition hygiene in rustc?"
  - "How do I handle edition-specific linting?"
  - "What are the guidelines for fuzzing the Rust compiler?"
  - "How do I structure a PR for the Rust compiler?"
---

# Quick Definition

Rustc development follows specific conventions covering code formatting (via `./x fmt`, not `cargo fmt`), PR structure (isolated refactorings, many small commits, no merge commits), naming conventions (`cx` for context, `tcx` for typing context, `krate` instead of `crate`), and a rigorous procedure for breaking changes that requires crater runs, tracking issues, and future-compatibility warning periods before errors. The project uses notification groups for platform-specific triage, manages external dependencies through subtrees and submodules, and has detailed procedures for edition support including migration lints and edition hygiene through span-based edition checking.

# Core Definition

The compiler codebase enforces specific practices to maintain quality across its large contributor base.

**Formatting** uses a pinned rustfmt version via `./x fmt` rather than standard `cargo fmt`. Lines should be at most 100 characters (80 preferred). Tabs are not used; 4-space indents are standard. C++ code (for LLVM interfacing) is formatted with `./x test tidy --extra-checks cpp:fmt --bless`, and Python code with `./x test tidy --extra-checks py:fmt --bless`.

**Breaking changes** follow a strict procedure based on RFC 1589. The permitted categories are: soundness fixes, compiler bugs (where behavior doesn't match RFCs), and underspecified semantics. The procedure requires: (1) a crater run to assess impact, (2) a dedicated tracking issue, (3) future-compatibility lint warnings before errors (except when fewer than 10 crates are affected), and (4) stabilization of the change (converting warnings to errors) after at least one release cycle.

**External dependencies** in `rust-lang/rust` use three mechanisms: crates.io dependencies for ecosystem-useful libraries, subtrees (git or josh) for tools that depend on compiler internals (clippy, miri, rust-analyzer, rustfmt, etc.), and git submodules for independent tools (cargo). Subtree synchronization uses the `rustc-josh-sync` tool for josh-based subtrees.

**Edition support** in the compiler uses span-based edition checking (`span.edition().at_least_rust_2021()`) rather than global session checks to properly handle macro hygiene across crate boundaries. Migration lints use `FutureIncompatibilityReason::EditionError` or `EditionSemanticsChange` and are auto-grouped into `rust-20xx-compatibility` lint groups. New keywords can be introduced across edition boundaries using `Symbol::is_used_keyword_conditional`.

**Notification groups** are platform-focused teams (Apple, ARM, RISC-V, WASM, Windows, etc.) that receive GitHub pings via `@rustbot ping <group>` when issues matching their criteria are found. They handle isolated, middle-priority bugs and are easy to join by PR to the team repository.

# Prerequisites

Familiarity with the Rust language, git workflows, and basic compiler concepts. Understanding of the Rust edition system is helpful for edition-related material.

# Key Properties

1. **`./x fmt` over `cargo fmt`**: The repository uses a pinned rustfmt version with custom config; standard `cargo fmt` is not recommended
2. **Exhaustive matches preferred**: Using `_` in match arms is discouraged because new enum variants may not be handled correctly
3. **`// TODO` vs `// FIXME`**: TODO comments are caught by tidy and prevent landing; FIXME is for permanent notes in the codebase
4. **No merge commits**: Only bors may create merge commits; contributors must rebase with `git rebase --interactive`
5. **PR structure**: Isolate pure refactorings, prefer more commits, format each commit, individual commits don't need to build
6. **Naming conventions**: `cx` = context suffix, `tcx` = typing context, `'tcx` = arena lifetime, `krate` = crate (since `crate` is a keyword)
7. **Crater runs**: Required before breaking changes; if fewer than 10 total affected crates, can go directly to errors
8. **Future-compatibility lints**: Declared with `@future_incompatible` in `declare_lint!`, referencing a tracking issue
9. **Edition hygiene**: Use `span.edition()` not `sess.edition()` to ensure macros from other crates respect their originating edition
10. **Migration lints**: Must produce `MachineApplicable` suggestions that compile in both old and new editions
11. **Josh subtrees**: Preferred over git subtrees for scaling; synchronized via `rustc-josh-sync pull` and `push` commands
12. **Licensing**: Dual MIT/Apache-2.0; reviewers must watch for GPL or patented code in contributions

# Construction / Recognition

## To Create a Future-Compatibility Lint:

```rust
// 1. Define the lint in compiler/rustc_lint/src/builtin.rs
declare_lint! {
    pub YOUR_LINT_HERE,
    Warn,
    "illegal use of foo bar baz"
    @future_incompatible = FutureIncompatibleInfo {
        reason: fcw!(FutureReleaseError #1234) // tracking issue
    },
}

// 2. Add a lint pass and emit the lint:
cx.emit_span_lint(YOUR_LINT_HERE, pat.span, MyDiagnostic { ... });
```

## To Add an Edition Migration Lint:

```rust
declare_lint! {
    pub KEYWORD_IDENTS,
    Allow,
    "detects edition keywords being used as an identifier",
    @future_incompatible = FutureIncompatibleInfo {
        reason: fcw!(EditionError 2018 "slug-of-edition-guide-page")
    };
}
```

## To Join a Notification Group:

Open a PR adding your GitHub username to the appropriate file in the `rust-lang/team` repository. If not already a Rust team member, also run `cargo run add-person $your_user_name`.

# Context & Application

- **New contributors**: Must follow formatting conventions, PR structure guidelines, and understand the tidy checks
- **Breaking change authors**: Must perform crater runs, create tracking issues, and implement future-compatibility lints before hard errors
- **Platform specialists**: Can join notification groups (Apple, ARM, RISC-V, WASM, Windows, LoongArch, GPU, Rust for Linux) to help triage platform-specific issues
- **Edition implementors**: Must understand edition hygiene, migration lints, and how to gate features on editions
- **Fuzzer operators**: Should follow guidelines on corpus building, ICE reporting, and minimization using tools like treereduce-rust

# Examples

**Example 1**: Naming conventions in compiler code:
```rust
// tcx is the typing context, 'tcx is the arena lifetime
fn example<'tcx>(tcx: TyCtxt<'tcx>, krate: CrateNum) {
    // cx suffix for other contexts
    let lcx = LoweringContext::new(tcx);
}
```

**Example 2**: Breaking change procedure -- if a change affects fewer than 10 crates on crates.io, you can skip the warning period:
> "If fewer than 10 **total** affected projects are found (**not** root errors), we can move straight to an error."

**Example 3**: Edition-specific lint that changes default level:
```rust
declare_lint! {
    pub SOME_LINT_NAME,
    Allow,
    "my lint description",
    @edition Edition2024 => Warn;
}
```

**Example 4**: Fuzzing tip -- use `--emit=mir` to avoid LLVM code generation, and `-Zmir-opt-level=4` to enable additional MIR optimization passes for finding bugs.

# Relationships

## Builds Upon
- None within this extraction set

## Enables
- **rustc-feature-lifecycle** -- the breaking change procedure feeds into the feature stabilization process
- **rustc-compiler-overview** -- understanding conventions helps when navigating compiler source code

## Related
- **rustc-feature-lifecycle** -- stabilization and feature gating are closely tied to development practices
- **rustc-compiler-bootstrapping** -- `./x` commands and stage-based builds are central to development workflow

## Contrasts With
- None within this source

# Common Errors

- **Error**: Using `cargo fmt` to format compiler code.
  **Correction**: Use `./x fmt` which invokes the pinned rustfmt version with the project's custom configuration. Standard `cargo fmt` may produce different formatting.

- **Error**: Submitting a PR with merge commits.
  **Correction**: "We do not allow merge commits into our history, other than those by bors." Use `git rebase --interactive rust-lang/main` instead.

- **Error**: Checking global session edition instead of span edition for edition-sensitive behavior.
  **Correction**: "You should normally use the edition from the token span instead of looking at the global Session edition" -- use `span.edition().at_least_rust_2021()` instead of `sess.at_least_rust_2021()`.

# Common Confusions

- **Confusion**: Future-compatibility warnings and deprecation warnings are the same thing.
  **Clarification**: Future-compatibility warnings are a special category of lint that signals an upcoming breaking change (soundness fix or bug fix). Deprecation warnings signal that an API is being phased out in favor of a newer one. They have different lifecycle and governance processes.

- **Confusion**: Subtrees and submodules work the same way in the rustc repository.
  **Clarification**: Subtrees (clippy, miri, rustfmt, rust-analyzer) are copied into the repo as regular files and can be modified in-tree. Submodules (cargo) are external git references. Subtrees are for tools that depend on compiler internals; submodules are for independent tools.

- **Confusion**: Migration lints must be `Warn` by default.
  **Clarification**: Most migration lints are `Allow` by default. They only appear during `cargo fix --edition` when cargo passes `--force-warn rust-20xx-compatibility`. Using `Warn` is reserved for cases where it's "important for everyone to be aware of the change."

# Source Reference

Chapter 6: Development Practices (1315 lines) covering coding conventions, formatting, breaking change procedures, external dependencies (subtrees and submodules), fuzzing guidelines, licensing, and edition support in the compiler. Chapter 7: Notification Groups (417 lines) covering platform-specific notification groups, their purpose, membership, and tagging procedures.

# Verification Notes

- Definition source: Direct text from coding conventions, breaking change procedure, and edition support sections
- Key Properties: All items directly supported by source text with specific commands, code patterns, and procedures
- Confidence rationale: HIGH -- canonical procedural documentation with specific, verifiable instructions
- Uncertainties: Specific file paths and tool versions may change as the compiler evolves
- Cross-reference status: Related slugs reference other cards in this compiler-guide extraction set
