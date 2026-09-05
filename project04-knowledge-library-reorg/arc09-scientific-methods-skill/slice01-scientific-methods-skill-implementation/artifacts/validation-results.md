# Validation Results

## Source Validation

- `git diff --check`: pass.
- `git diff --cached --check`: pass.
- `make check-skills`: pass.
- Focused local Markdown link validation: 12 files checked, 188 local links
  checked, 0 missing.

## Package Validation

- `make scientific-methods`: pass.
- `make check-package-paths`: pass.
- Package-path baseline:
  - 13 zips scanned.
  - 222 packaged Markdown files scanned.
  - 0 hard failures.
  - 376 warnings.
  - 3 explicit exceptions.
  - 656 skipped external URLs.

## Scientific-Methods Zip Inspection

`target/skills/scientific-methods.zip` contains 17 entries, including:

- `scientific-methods/SKILL.md`
- `scientific-methods/version-history.md`
- `scientific-methods/guides/`
- `scientific-methods/guides/01-inquiry-framing.md`
- `scientific-methods/guides/02-experiment-design.md`
- `scientific-methods/guides/03-controls-and-confounds.md`
- `scientific-methods/guides/04-operational-measures.md`
- `scientific-methods/guides/05-protocol-and-prompt-design.md`
- `scientific-methods/guides/06-evidence-capture.md`
- `scientific-methods/guides/07-comparison-and-regression-testing.md`
- `scientific-methods/guides/08-analysis-and-threats-to-validity.md`
- `scientific-methods/guides/09-anti-patterns.md`
- `scientific-methods/templates/`
- `scientific-methods/templates/ab-comparison-prompt.md`
- `scientific-methods/templates/experiment-protocol.md`
- `scientific-methods/templates/evaluation-rubric.md`

## Install Smoke

Command shape:

```sh
tmpdir=$(mktemp -d /private/tmp/ai-engineering-scientific-methods-install.XXXXXX)
make install INSTALL_DIR="$tmpdir"
find "$tmpdir" -maxdepth 2 -name 'SKILL*.md' | sort
test ! -e "$tmpdir/ccdp"
```

Result:

- Install directory:
  `/private/tmp/ai-engineering-scientific-methods-install.wo7iuJ`
- 13 `SKILL*.md` entrypoints installed.
- Installed entrypoints included `scientific-methods/SKILL.md`.
- No `ccdp` install root existed.

## Final Source Status

Source checkout was clean after source commit
`a2122abbe75b42f87e550c87ba1150b51d7abb38`.
