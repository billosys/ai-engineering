# Package and Install Inspection Report

Source commit: `b9aaaf4302fb50631bb915cb64d1272a6fd3c405`

## Package Inspection

Generated package roots and top-level installable skill entrypoints:

| Zip | Root | Entrypoint |
| --- | --- | --- |
| `biome-js-linter.zip` | `biome-js-linter/` | `biome-js-linter/SKILL-js-linter.md` |
| `biome-linter.zip` | `biome-linter/` | `biome-linter/SKILL-web-linter.md` |
| `cobalt-guidelines.zip` | `cobalt-guidelines/` | `cobalt-guidelines/SKILL.md` |
| `collaboration-framework.zip` | `collaboration-framework/` | `collaboration-framework/SKILL.md` |
| `cpp-guidelines.zip` | `cpp-guidelines/` | `cpp-guidelines/SKILL.md` |
| `deno-js-linter.zip` | `deno-js-linter/` | `deno-js-linter/SKILL-js-linter.md` |
| `erlang-guidelines.zip` | `erlang-guidelines/` | `erlang-guidelines/SKILL.md` |
| `go-guidelines.zip` | `go-guidelines/` | `go-guidelines/SKILL.md` |
| `javascript-deno-guidelines.zip` | `javascript-deno-guidelines/` | `javascript-deno-guidelines/SKILL.md` |
| `rust-guidelines.zip` | `rust-guidelines/` | `rust-guidelines/SKILL.md` |
| `tailwindcss.zip` | `tailwindcss/` | `tailwindcss/SKILL.md` |
| `visual-design-system.zip` | `visual-design-system/` | `visual-design-system/SKILL.md` |

`ccdp.zip` was also generated for CCDP protocol distribution validation, but
it has no `SKILL*.md` entrypoint and is not an installable skill package.

## collaboration-framework.zip

`collaboration-framework.zip` inspection confirmed:

- `collaboration-framework/SKILL.md` is present.
- Component SKILL.md files are present for `agent-coordination`,
  `code-auditing`, `contribution-style`, `engineering-methods`,
  `project-management`, `testing`, and `work-verification`.
- Long component material is under `guides/`.
- Preserved templates remain under `templates/`.
- No legacy `knowledge/<component>/docs/` or `docs/pm` package entries are
  present.

The archive inspection reported `legacy_docs_count 0`, `guide_count 17`, and
template files:

- `collaboration-framework/knowledge/work-verification/templates/LEDGER-DISCIPLINE.md`
- `collaboration-framework/knowledge/contribution-style/templates/CONTRIBUTION-TICKET.md`

## Isolated Install Smoke

The isolated install smoke used:

```sh
make INSTALL_DIR=/private/tmp/ai-engineering-slice04-install-smoke-20260904 install
```

It installed these skill roots with `SKILL*.md` entrypoints:

- `biome-js-linter/SKILL-js-linter.md`
- `biome-linter/SKILL-web-linter.md`
- `cobalt-guidelines/SKILL.md`
- `collaboration-framework/SKILL.md`
- `cpp-guidelines/SKILL.md`
- `deno-js-linter/SKILL-js-linter.md`
- `erlang-guidelines/SKILL.md`
- `go-guidelines/SKILL.md`
- `javascript-deno-guidelines/SKILL.md`
- `rust-guidelines/SKILL.md`
- `tailwindcss/SKILL.md`
- `visual-design-system/SKILL.md`

The isolated install directory had no ccdp root: `ccdp exists: False`.

Generated packages live under `target/skills`; generated package staging lives
under `build/`. Both are ignored generated-output paths and were not committed.
