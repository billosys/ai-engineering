# Framework Warning Classification

Baseline source: `baseline-collaboration-framework-warnings.txt`

Post-change source: `post-collaboration-framework-warnings.txt`

## Baseline Counts

Rows excluding header: 56

| Classification | Count | Slice 02 disposition |
| --- | ---: | --- |
| `bundled-reference` | 4 | Fixed by source edits and retired from transitional exceptions. |
| `repo-only/provenance` | 45 | Preserved as warnings; these are canonical planning examples, source-root instruction-file names, workbench placeholders, source skill placeholders, or glob examples. |
| `source-clone-reference` | 5 | Preserved as warnings; these name source-clone material that is intentionally not bundled in the collaboration-framework package. |
| `example-project path` | 2 | Preserved as warnings; these are illustrative user/home paths, not package artifacts. |

## Fixed Package-Internal Rows

These rows pointed at files that are bundled in `collaboration-framework.zip`
but used source-root or wrong-context spellings from documents below `docs/`.
They now use relative paths that resolve in both source and package contexts:

| Document | Old target | New target |
| --- | --- | --- |
| `docs/pm/06-confirmation-protocol.md` | `docs/PROJECT-MANAGEMENT.md` | `../PROJECT-MANAGEMENT.md` |
| `docs/pm/version-history.md` | `docs/PROJECT-MANAGEMENT.md` | `../PROJECT-MANAGEMENT.md` |
| `docs/AI-ENGINEERING-METHODOLOGY.md` | `SKILL.md` | `../SKILL.md` |

The `docs/pm/06-confirmation-protocol.md` target occurred twice.

## Preserved Warning Rationale

Remaining framework warnings are intentionally not hidden in
`package-path-exceptions.tsv` during this slice. They stay visible for Arc 02
warning-policy tightening:

- `repo-only/provenance`: canonical planning path examples such as
  `sliceNN-<slug>/artifacts/`, source-root instruction filenames such as
  `CLAUDE.md` and `AGENTS.md`, source substrate placeholders such as
  `knowledge/<slug>/`, and historical workbench examples are not bundled
  reader dependencies.
- `source-clone-reference`: `README.md`, `./knowledge/`,
  `knowledge/rust/guides/11-anti-patterns.md`, and
  `./dev/concept-cards/...` are useful source-clone context, not required
  collaboration-framework package files.
- `example-project path`: `~/.claude/CLAUDE.md` is an illustrative user-local
  path, not a package artifact.

No broad allowlist was added. The existing explicit exceptions for
`knowledge/<slug>/SKILL*.md` and `knowledge/<domain>/SKILL.md` remain because
they pre-date this slice and carry source/provenance reasons.
