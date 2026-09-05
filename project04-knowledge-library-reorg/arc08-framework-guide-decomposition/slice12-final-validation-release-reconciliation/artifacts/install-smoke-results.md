# Install Smoke Results

## Command

Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`

```sh
tmpdir=$(mktemp -d /private/tmp/ai-engineering-slice12-install-smoke.XXXXXX)
make install INSTALL_DIR="$tmpdir" > /private/tmp/slice12-install-smoke.out
find "$tmpdir" -maxdepth 2 -name 'SKILL*.md' | sort > /private/tmp/slice12-install-smoke-skill-files.out
find "$tmpdir" -maxdepth 1 -type d | sort > /private/tmp/slice12-install-smoke-roots.out
test ! -e "$tmpdir/ccdp"
```

Temporary install root:

- `/private/tmp/ai-engineering-slice12-install-smoke.eraUir`

## Installed Entrypoints

The smoke run installed 12 `SKILL*.md` entrypoints:

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

The root listing contained those 12 installed skill roots plus the temporary
install directory itself. There was no `ccdp` install root.

## Verdict

Pass. Isolated install behavior produces the expected 12 installable skill
roots and confirms CCDP is not installed as a skill root.
