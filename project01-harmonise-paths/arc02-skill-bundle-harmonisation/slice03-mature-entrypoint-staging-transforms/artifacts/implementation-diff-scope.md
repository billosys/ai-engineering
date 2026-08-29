# Implementation Diff Scope

Implementation checkout status after edits:

```text
 M Makefile
 M package-path-exceptions.tsv
?? scripts/stage-skill-entrypoint
```

Implementation scope:

- `Makefile`: routes per-domain skill entrypoint staging through
  `scripts/stage-skill-entrypoint` before copying `guides/`.
- `scripts/stage-skill-entrypoint`: new constrained helper. It applies
  package-only path rewrites for `knowledge/rust/SKILL.md` and
  `knowledge/js/SKILL.md`; all other skill entrypoints are copied unchanged.
- `package-path-exceptions.tsv`: retired six resolved transitional entrypoint
  rows: four Rust `SKILL.md` rows and two JavaScript/Deno `SKILL.md` rows.

Out-of-scope files were not edited:

- no mature guide prose files;
- no collaboration-framework bundle files;
- no CCDP package files;
- no package layout expansion or image additions.

Planning worktree note: `AGENTS.md` and `CLAUDE.md` were already staged, and
`project02-collab-breakout/` was unrelated untracked work. This slice did not
modify those paths.
