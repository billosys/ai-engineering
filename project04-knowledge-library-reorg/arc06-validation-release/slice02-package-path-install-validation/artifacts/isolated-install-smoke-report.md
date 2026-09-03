# isolated install smoke report

## Scope

Slice02 ran the install smoke test against a temporary INSTALL_DIR under
`/private/tmp`, not the operator's default `~/.agents/skills`.

temporary INSTALL_DIR:

```text
/private/tmp/ai-engineering-install.83lU0N
```

## Command

```sh
tmp="$(mktemp -d /private/tmp/ai-engineering-install.XXXXXX)"
printf 'INSTALL_DIR=%s\n' "$tmp"
make install INSTALL_DIR="$tmp"
printf 'installed entrypoints:\n'
find "$tmp" -maxdepth 2 -name 'SKILL*.md' -print | sort
for path in \
  "$tmp/collaboration-framework/SKILL.md" \
  "$tmp/rust-guidelines/SKILL.md" \
  "$tmp/go-guidelines/SKILL.md" \
  "$tmp/cpp-guidelines/SKILL.md" \
  "$tmp/javascript-deno-guidelines/SKILL.md" \
  "$tmp/erlang-guidelines/SKILL.md" \
  "$tmp/cobalt-guidelines/SKILL.md" \
  "$tmp/visual-design-system/SKILL.md" \
  "$tmp/tailwindcss/SKILL.md" \
  "$tmp/deno-js-linter/SKILL-js-linter.md" \
  "$tmp/biome-js-linter/SKILL-js-linter.md" \
  "$tmp/biome-linter/SKILL-web-linter.md"; do
  test -f "$path" || { printf 'missing %s\n' "$path"; exit 1; }
done
if [ -e "$tmp/ccdp" ]; then
  printf 'unexpected ccdp install root: %s\n' "$tmp/ccdp"
  exit 1
fi
printf 'install smoke: pass\n'
```

## Installed Skill Root and Entrypoint Inspection

Installed entrypoints:

```text
/private/tmp/ai-engineering-install.83lU0N/biome-js-linter/SKILL-js-linter.md
/private/tmp/ai-engineering-install.83lU0N/biome-linter/SKILL-web-linter.md
/private/tmp/ai-engineering-install.83lU0N/cobalt-guidelines/SKILL.md
/private/tmp/ai-engineering-install.83lU0N/collaboration-framework/SKILL.md
/private/tmp/ai-engineering-install.83lU0N/cpp-guidelines/SKILL.md
/private/tmp/ai-engineering-install.83lU0N/deno-js-linter/SKILL-js-linter.md
/private/tmp/ai-engineering-install.83lU0N/erlang-guidelines/SKILL.md
/private/tmp/ai-engineering-install.83lU0N/go-guidelines/SKILL.md
/private/tmp/ai-engineering-install.83lU0N/javascript-deno-guidelines/SKILL.md
/private/tmp/ai-engineering-install.83lU0N/rust-guidelines/SKILL.md
/private/tmp/ai-engineering-install.83lU0N/tailwindcss/SKILL.md
/private/tmp/ai-engineering-install.83lU0N/visual-design-system/SKILL.md
```

Installed skill root checks:

| installed skill root | expected entrypoint | disposition |
| --- | --- | --- |
| `collaboration-framework/` | `SKILL.md` | pass |
| `rust-guidelines/` | `SKILL.md` | pass |
| `go-guidelines/` | `SKILL.md` | pass |
| `cpp-guidelines/` | `SKILL.md` | pass |
| `javascript-deno-guidelines/` | `SKILL.md` | pass |
| `erlang-guidelines/` | `SKILL.md` | pass |
| `cobalt-guidelines/` | `SKILL.md` | pass |
| `visual-design-system/` | `SKILL.md` | pass |
| `tailwindcss/` | `SKILL.md` | pass |
| `deno-js-linter/` | `SKILL-js-linter.md` | pass |
| `biome-js-linter/` | `SKILL-js-linter.md` | pass |
| `biome-linter/` | `SKILL-web-linter.md` | pass |

## Pass/Fail Result

Result: pass.

`make install INSTALL_DIR=/private/tmp/ai-engineering-install.83lU0N` exited 0,
all expected installable skill roots and `SKILL*.md` entrypoints were present,
and no `ccdp/` root was installed.
