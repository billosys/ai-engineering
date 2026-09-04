# Skill Library

The skill library is the collection of Markdown skill packages and guide
material in [`knowledge/`](../knowledge/), plus the
[`collaboration-framework`](../knowledge/collaboration-framework/SKILL.md) entrypoint. Each installable skill has
a skill entrypoint file and package target; the detailed guide content stays
with the owning knowledge root.

Skill kind and topology are separate. Kind says what a skill is about:
domain/tooling, framework/operational, or method work. Topology says how a
skill composes: an atomic skill has one bounded load reason, while a
composite skill exists to select, sequence, route, govern, or compose multiple
loadable components.

## Current Installable Skills

| Skill package | Source entrypoint | Use when |
|---|---|---|
| `rust-guidelines.zip` | [`knowledge/rust/SKILL.md`](../knowledge/rust/SKILL.md) | Writing, reviewing, or refactoring Rust. |
| `go-guidelines.zip` | [`knowledge/go/SKILL.md`](../knowledge/go/SKILL.md) | Writing, reviewing, or refactoring Go. |
| `cpp-guidelines.zip` | [`knowledge/cpp/SKILL.md`](../knowledge/cpp/SKILL.md) | Working with modern C++ and C++ Core Guidelines material. |
| `javascript-deno-guidelines.zip` | [`knowledge/js/SKILL.md`](../knowledge/js/SKILL.md) | Writing JavaScript with Deno-first conventions. |
| `erlang-guidelines.zip` | [`knowledge/erlang/SKILL.md`](../knowledge/erlang/SKILL.md) | Writing Erlang/OTP systems. |
| `cobalt-guidelines.zip` | [`knowledge/cobalt/SKILL.md`](../knowledge/cobalt/SKILL.md) | Building or extending Cobalt static sites. |
| `visual-design-system.zip` | [`knowledge/design/SKILL.md`](../knowledge/design/SKILL.md) | Designing UI, layout, typography, and color systems. |
| `tailwindcss.zip` | [`knowledge/tailwindcss/SKILL.md`](../knowledge/tailwindcss/SKILL.md) | Styling with Tailwind CSS v4. |
| `deno-js-linter.zip` | [`knowledge/deno/SKILL-js-linter.md`](../knowledge/deno/SKILL-js-linter.md) | Applying Deno lint rules to JavaScript. |
| `biome-js-linter.zip` | [`knowledge/biome/SKILL-js-linter.md`](../knowledge/biome/SKILL-js-linter.md) | Applying Biome JavaScript lint rules. |
| `biome-linter.zip` | [`knowledge/biome/SKILL-web-linter.md`](../knowledge/biome/SKILL-web-linter.md) | Applying broader Biome web lint rules. |
| `collaboration-framework.zip` | [`knowledge/collaboration-framework/SKILL.md`](../knowledge/collaboration-framework/SKILL.md) | Running sustained planning, implementation, review, and verification work. |

## Choosing What To Load

Load the domain/tooling skill that matches the code or artifact you are
working on. For example, Rust code should load Rust guidance, Erlang/OTP work
should load Erlang guidance, and Tailwind styling should load Tailwind
guidance.

Load the collaboration framework when the work itself needs structure: project
planning, ledgered implementation, code audit, coverage hardening, subagent
delegation decisions, or contribution-ticket writing. It is a composite
framework/operational skill: the "how we work" layer and daily-driver
composer, not a substitute for language or tooling expertise.

When a task crosses boundaries, load the smallest set that covers the work.
For example, an Erlang implementation slice in a ledgered project would use
the collaboration framework plus Erlang guidance.

Rust is the public example of an atomic domain/tooling skill. The Rust domain
is broad, but the load reason "work in Rust" is coherent. That example does
not mean every domain/tooling skill is atomic.

## Package And Source Distinction

The source roots under `knowledge/` can contain more than a packaged skill
loads: source material, extraction metadata, concept cards, workbench notes,
and other provenance-bearing files. The generated skill zips contain the
package surface needed by a skill loader.

Use source paths when you are studying, maintaining, or auditing the repository.
Use generated zips when you are installing skills into a loader.
The generated `collaboration-framework.zip` still exposes package entrypoint
`collaboration-framework/SKILL.md`.

## Planned Method Material

This repository has planning evidence for method skills such as planned
`concept-card-method`. That material should not be treated as a live
installable skill until a later implementation project lands source and package
support.
