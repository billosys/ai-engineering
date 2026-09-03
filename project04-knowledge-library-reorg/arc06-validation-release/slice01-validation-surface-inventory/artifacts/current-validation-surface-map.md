# current validation surface map

## Scope

This validation surface map covers Project04's final Arc06 gates after
Arc01 through Arc05 closed.

- source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`
- planning checkout:
  `/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning`
- source commit inspected: `9b948da`
- planning commit inspected before Slice01 edits: `66d855c`
- source files edited in this slice: none
- generated artifact policy: generated skill zips, `ccdp.zip`, and `build/`
  are validation outputs only and are not committed by Slice01.

## Current Checkout Surfaces

| Surface | Command | Current disposition |
| --- | --- | --- |
| source checkout cleanliness | `git status --short --untracked-files=all` | pass; clean output |
| planning checkout cleanliness | `git status --short --untracked-files=all` | pass before Slice01 edits; clean output |
| source whitespace | `git diff --check` | pass; clean output |
| planning whitespace | `git diff --check` | pass before Slice01 edits; clean output |

## README/docs/SKILL.md Surfaces

README, `docs/`, and top-level `SKILL.md` now carry the final public route map
for Project04:

- `README.md` points to the focused `docs/` guide set, `knowledge/`,
  `protocols/`, `templates/`, Make targets, installable skill packages, and
  CCDP package targets.
- `docs/*.md` provides end-user explanation for repository overview, skill
  library, collaboration framework, knowledge-library anatomy, building and
  installing, protocols, contribution guidance, and origins.
- `SKILL.md` remains the top-level `collaboration-framework` composite
  framework/operational skill entrypoint, with route links into `knowledge/`.

Local link validation command:

```sh
python3 - <<'PY'
from pathlib import Path
import re, urllib.parse
root=Path('/Users/oubiwann/lab/billosys/ai-engineering')
files=[root/'README.md', root/'SKILL.md']+sorted((root/'docs').glob('*.md'))
link_re=re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
missing=[]; checked=0; skipped=0
for path in files:
    text=path.read_text()
    for i,line in enumerate(text.splitlines(),1):
        for m in link_re.finditer(line):
            target=m.group(1).strip()
            if not target or target.startswith(('http://','https://','mailto:','#')):
                skipped+=1; continue
            target=target.split()[0]
            target=target.split('#',1)[0]
            if not target:
                skipped+=1; continue
            decoded=urllib.parse.unquote(target)
            resolved=(path.parent/decoded).resolve()
            checked+=1
            if not resolved.exists():
                missing.append((path.relative_to(root),i,target,resolved))
print(f'files checked: {len(files)}')
print(f'links checked: {checked}')
print(f'skipped external/anchors: {skipped}')
print(f'missing: {len(missing)}')
for item in missing:
    print(item)
raise SystemExit(1 if missing else 0)
PY
```

Current result: files checked: 10; links checked: 104; skipped external/anchors:
1; missing: 0.

Route scan command:

```sh
rg -n "\[[^\]]+\]\([^\)]+\)|https?://|docs/|knowledge/|protocols/|templates/|Makefile|package" README.md docs SKILL.md
```

Current result: pass; output shows expected route references for `docs/`,
`knowledge/`, `protocols/`, `templates/`, Make targets, package surfaces, and
CCDP package commands.

## Make Target Surfaces

| Make target | Purpose | Current disposition |
| --- | --- | --- |
| `make help` | List package, validation, install, and CCDP targets | pass |
| `make check-skills` | Validate every packaged `SKILL.md` description length | pass |
| `make check-package-paths` | Build all installable skill zips and validate package-context Markdown paths | pass with warning-only package-path findings; hard failures: 0 |
| `make all` | Build every installable skill zip plus `collaboration-framework.zip` | pass |
| `make install INSTALL_DIR=<isolated-dir>` | Install built skills into an isolated temp directory | planned for Slice02 smoke validation |
| `make ccdp-package` | Build the standalone CCDP protocol package | fail now; stale assembled spec |
| `make check-ccdp-package` | Validate `ccdp.zip` zipped and unzipped | fail now at `ccdp-package` prerequisite; stale assembled spec |

## Package Output Surfaces

`make all` generated these ignored installable skill package outputs:

| Package output | Package root | Entry count | Entrypoint observed |
| --- | --- | ---: | --- |
| `rust-guidelines.zip` | `rust-guidelines/` | 41 | `rust-guidelines/SKILL.md` |
| `go-guidelines.zip` | `go-guidelines/` | 15 | `go-guidelines/SKILL.md` |
| `cpp-guidelines.zip` | `cpp-guidelines/` | 18 | `cpp-guidelines/SKILL.md` |
| `javascript-deno-guidelines.zip` | `javascript-deno-guidelines/` | 24 | `javascript-deno-guidelines/SKILL.md` |
| `erlang-guidelines.zip` | `erlang-guidelines/` | 20 | `erlang-guidelines/SKILL.md` |
| `cobalt-guidelines.zip` | `cobalt-guidelines/` | 4 | `cobalt-guidelines/SKILL.md` |
| `visual-design-system.zip` | `visual-design-system/` | 9 | `visual-design-system/SKILL.md` |
| `tailwindcss.zip` | `tailwindcss/` | 4 | `tailwindcss/SKILL.md` |
| `deno-js-linter.zip` | `deno-js-linter/` | 6 | `deno-js-linter/SKILL-js-linter.md` |
| `biome-js-linter.zip` | `biome-js-linter/` | 20 | `biome-js-linter/SKILL-js-linter.md` |
| `biome-linter.zip` | `biome-linter/` | 20 | `biome-linter/SKILL-web-linter.md` |
| `collaboration-framework.zip` | `collaboration-framework/` | 40 | `collaboration-framework/SKILL.md` |

`ccdp.zip` exists as an ignored prior/generated artifact in the source checkout,
but `make ccdp-package` does not currently refresh it because the assembled
protocol freshness check fails first.

## Install Smoke Surface

Slice02 should run install smoke validation with an isolated install directory,
not the operator's default `~/.agents/skills`:

```sh
tmp="$(mktemp -d /private/tmp/ai-engineering-install.XXXXXX)"
make install INSTALL_DIR="$tmp"
find "$tmp" -maxdepth 2 -name 'SKILL*.md' -print | sort
test -f "$tmp/collaboration-framework/SKILL.md"
test -f "$tmp/rust-guidelines/SKILL.md"
test -f "$tmp/go-guidelines/SKILL.md"
test -f "$tmp/cpp-guidelines/SKILL.md"
test -f "$tmp/javascript-deno-guidelines/SKILL.md"
test -f "$tmp/erlang-guidelines/SKILL.md"
test -f "$tmp/cobalt-guidelines/SKILL.md"
test -f "$tmp/visual-design-system/SKILL.md"
test -f "$tmp/tailwindcss/SKILL.md"
test -f "$tmp/deno-js-linter/SKILL-js-linter.md"
test -f "$tmp/biome-js-linter/SKILL-js-linter.md"
test -f "$tmp/biome-linter/SKILL-web-linter.md"
test ! -e "$tmp/ccdp"
```

Expected outcome: installable skills appear under the isolated directory, and
CCDP is absent because CCDP is a protocol package, not an installable skill.

## Operator Acceptance Surface

Arc06 final acceptance should reconcile:

- README starts users in focused docs and routes them to `knowledge/` for
  source substrate.
- `docs/` remains explanatory documentation, not duplicated source payload.
- `knowledge/` remains the material substrate for installable skills.
- generated installable skill packages build and install from the final layout.
- CCDP remains a separate protocol distribution and either passes package
  freshness after repair or has an explicit accepted final disposition.
