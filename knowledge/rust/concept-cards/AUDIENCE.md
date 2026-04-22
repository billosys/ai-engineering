# Audience

Most concept cards in this skill map directly into a main guide — they back the day-to-day Rust-programming guidance that lives one level up. Two card sets are different: they target a specialist audience and are intentionally kept in the concept-cards area without promotion to a main guide.

## Specialist card sets

### `knowledge/rust/concept-cards/compiler-guide/`

- **Cards:** 26
- **Audience:** rustc contributors and rustdoc hackers — people working on HIR/MIR, the query system, name resolution, trait solving, the borrow checker, codegen backends, diagnostics, bootstrapping, or the feature lifecycle.
- **Why not promoted:** rustc internals are not day-to-day Rust programming. Inlining them into a main guide would bloat that guide for the 99% of readers who write Rust rather than hack on the compiler.

### `knowledge/rust/concept-cards/clippy/`

- **Cards:** 26 (of which the `[lint-development]` subcategory — roughly 14 cards covering lint passes, emission, registration, testing, `clippy_utils`, `ty::Ty`/`TyKind`, `TypeckResults`, macro handling, and trait checking — targets lint authors specifically).
- **Audience:** clippy lint developers writing or modifying lints, not users configuring clippy in their own projects. (Cards on configuration, lint levels, `cargo clippy`, and `clippy-driver` usage *are* user-facing and remain usable on their own.)
- **Why not promoted:** writing a clippy lint requires driving rustc's internal APIs. That is a specialist workflow, not something every Rust programmer needs.

## Still discoverable

These cards remain available for grep-style lookup from the concept-cards tree and are ready for anyone who wants to contribute to rustc or clippy — they just aren't surfaced through the main guides.

## Future home

If this skill ever grows into genuine support for compiler or lint development, the right move is to split that content into its own skill — e.g. `knowledge/rust-toolsmithing/` or `knowledge/rust-compiler-dev/` — rather than mixing specialist toolchain content with day-to-day Rust-programming guidance. The current arrangement is a holding pattern, not a long-term structure.
