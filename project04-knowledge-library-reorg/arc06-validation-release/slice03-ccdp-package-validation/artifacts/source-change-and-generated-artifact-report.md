# source-change and generated-artifact report

## Source Change

Source commit:

```text
94569ec681bf35dced8c024f1a8bf698e98f57c9
```

Changed source path:

- `protocols/ccdp/composite-cognition-dispatch-protocol.md`

Diff scope:

```text
protocols/ccdp/composite-cognition-dispatch-protocol.md | 2 +-
1 file changed, 1 insertion(+), 1 deletion(-)
```

No-op source surfaces:

- source `Makefile`: no-op.
- `scripts/check-ccdp-package`: no-op.
- `protocols/ccdp/src/**`: no-op.
- `protocols/ccdp/json/**`: no-op.
- `protocols/ccdp/templates/**`: no-op.
- `protocols/ccdp/visual-guide/**`: no-op.
- `protocols/ccdp/tools/ccdp-assembler/**`: no-op.

## Generated Artifact Handling

Generated artifact policy: `ccdp.zip`, installable skill zips, and `build/`
outputs are not committed unless a separate release process explicitly asks.

Tracked zip check:

```sh
git ls-files '*.zip' build
```

Result: no tracked zips or build outputs.

Ignored artifact check:

```sh
git status --short --ignored --untracked-files=all -- '*.zip' build
```

Result includes ignored generated outputs:

```text
!! biome-js-linter.zip
!! biome-linter.zip
!! ccdp.zip
!! cobalt-guidelines.zip
!! collaboration-framework.zip
!! cpp-guidelines.zip
!! deno-js-linter.zip
!! erlang-guidelines.zip
!! go-guidelines.zip
!! javascript-deno-guidelines.zip
!! rust-guidelines.zip
!! tailwindcss.zip
!! visual-design-system.zip
```

## Final Source Status

Final source status after the source commit and validation:

```sh
git status --short --untracked-files=all
```

Result: clean output.
