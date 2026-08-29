# Entrypoint Target Resolution

Generated after the staging transform and `make check-package-paths`.

## Staged Zip Entrypoints

`unzip -p rust-guidelines.zip rust-guidelines/SKILL.md | rg -n "guides/14-cli-tools/README.md|guides/15-cargo/01-cargo-basics.md|guides/15-cargo/04-cargo-publishing.md|guides/15-cargo/07-lints-and-formatters.md"`

```text
113:| **CLI application** | `guides/14-cli-tools/README.md`, then section-specific |
114:| **Cargo package / dependencies / workspaces** | `guides/15-cargo/01-cargo-basics.md` |
117:| **Publishing to crates.io / SemVer** | `guides/15-cargo/04-cargo-publishing.md` |
120:| **Clippy and rustfmt policy** | `guides/15-cargo/07-lints-and-formatters.md` |
196:1. **Load `guides/14-cli-tools/README.md`** for the map, then load the section that matches what you're doing.
545:1. Load: `guides/14-cli-tools/README.md` for the map; then `guides/14-cli-tools/01-project-setup.md`, `guides/14-cli-tools/02-argument-parsing.md`, `guides/14-cli-tools/04-output-and-ux.md`, `guides/14-cli-tools/08-advanced-topics.md`.
567:1. Load: `guides/15-cargo/04-cargo-publishing.md`, `13-documentation.md`, `02-api-design.md`.
581:- **Clippy lints** are referenced as `clippy::lint_name`. The same lint is referenced in `guides/15-cargo/07-lints-and-formatters.md` as an enforceable rule.
604:| Build a CLI with `clap` | `guides/14-cli-tools/README.md` -> section-specific |
605:| Manage dependencies / features / workspaces | `guides/15-cargo/01-cargo-basics.md`, `guides/15-cargo/02-cargo-build-system.md`, `guides/15-cargo/08-manifest-and-workspace-advanced.md` |
606:| Publish to crates.io | `guides/15-cargo/04-cargo-publishing.md` |
```

`unzip -p javascript-deno-guidelines.zip javascript-deno-guidelines/SKILL.md | rg -n "guides/09-anti-patterns.md|guides/12-deno/12-02-testing.md|guides/13-biome/13-01-setup.md|knowledge/js/guides/"`

```text
42:| **Any JS code** | `guides/09-anti-patterns.md` (always load first) |
44:| **Implementing a new feature** | `guides/01-core-idioms.md`, `guides/06-functions-closures.md`, `guides/09-anti-patterns.md` |
47:| **Refactoring** | `guides/09-anti-patterns.md`, `guides/01-core-idioms.md`, `guides/04-values-references.md` |
48:| **Code review / quality audit** | `guides/09-anti-patterns.md`, `guides/01-core-idioms.md`, `guides/08-performance.md` |
49:| **Writing or improving tests** | `guides/12-deno/12-02-testing.md`, `guides/03-error-handling.md` |
50:| **Debugging failing tests** | `guides/12-deno/12-02-testing.md`, `guides/03-error-handling.md`, `guides/07-async-concurrency.md` |
61:| **Biome lint/format** | `guides/13-biome/13-01-setup.md`, `guides/13-biome/13-02-lint-rules.md`, `guides/13-biome/13-03-formatting.md` |
69:1. **Load anti-patterns first**: Read `guides/09-anti-patterns.md` - know what to avoid before writing a line
94:1. **Load testing guide**: `guides/12-deno/12-02-testing.md`
```

No `knowledge/js/guides/` matches were emitted by that staged zip entrypoint
check.

## Zip File Presence

`unzip -l rust-guidelines.zip | rg "rust-guidelines/guides/(14-cli-tools/README.md|15-cargo/01-cargo-basics.md|15-cargo/04-cargo-publishing.md|15-cargo/07-lints-and-formatters.md)"`

```text
    16566  08-29-2026 15:12   rust-guidelines/guides/14-cli-tools/README.md
    14369  08-29-2026 15:12   rust-guidelines/guides/15-cargo/07-lints-and-formatters.md
    21810  08-29-2026 15:12   rust-guidelines/guides/15-cargo/04-cargo-publishing.md
    24263  08-29-2026 15:12   rust-guidelines/guides/15-cargo/01-cargo-basics.md
```

`unzip -l javascript-deno-guidelines.zip | rg "javascript-deno-guidelines/guides/(09-anti-patterns.md|12-deno/12-02-testing.md|13-biome/13-01-setup.md)"`

```text
    32286  08-29-2026 15:12   javascript-deno-guidelines/guides/12-deno/12-02-testing.md
    23709  08-29-2026 15:12   javascript-deno-guidelines/guides/13-biome/13-01-setup.md
    45517  08-29-2026 15:12   javascript-deno-guidelines/guides/09-anti-patterns.md
```

## Source Checkout Preservation

`rg -n "14-cli-tools/README.md|15-cargo/01-cargo-basics.md|knowledge/js/guides/09-anti-patterns.md|12-deno/12-02-testing.md" knowledge/rust/SKILL.md knowledge/js/SKILL.md`

```text
knowledge/js/SKILL.md:42:| **Any JS code** | `knowledge/js/guides/09-anti-patterns.md` (always load first) |
knowledge/js/SKILL.md:94:1. **Load testing guide**: `12-deno/12-02-testing.md`
knowledge/rust/SKILL.md:113:| **CLI application** | `14-cli-tools/README.md`, then section-specific |
knowledge/rust/SKILL.md:114:| **Cargo package / dependencies / workspaces** | `15-cargo/01-cargo-basics.md` |
```

`test -e` source target checks passed for:

- `knowledge/rust/guides/14-cli-tools/README.md`
- `knowledge/rust/guides/15-cargo/01-cargo-basics.md`
- `knowledge/js/guides/09-anti-patterns.md`
- `knowledge/js/guides/12-deno/12-02-testing.md`
- `knowledge/js/guides/13-biome/13-01-setup.md`
