# Source Impact and Validation Plan

## Source Impact

Slice01 is read-only and made no source edits. Later Arc08 source-edit slices
should use explicit staging pathspecs and stay within their authorized files.

Support artifacts controlling this plan:

- `artifacts/operator-accepted-architecture.md`
- `artifacts/component-file-layout-plan.md`

## Likely Slice02 Source Edit Surfaces

Likely Slice02 source impact:

- `knowledge/project-management/guides/PROJECT-MANAGEMENT.md`: correct
  Expedited Mode wording so it is limited to explicit listed process changes.
- `knowledge/collaboration-framework/SKILL.md`: repair route text that mentions
  Expedited Mode so it does not imply shortcuts, skipped validation, weaker
  review, inferred source scope, timeline interpretation, or bypassed operator
  approval gates.
- `knowledge/project-management/guides/version-history.md`: move to
  `knowledge/project-management/version-history.md` and reconcile route links.
- `knowledge/project-management/SKILL.md`: update version-history route after
  the sibling history move.
- `Makefile`: update `CF_FILES` if version-history paths move.
- `assets/packaging/path-exceptions.tsv`: update only if a moved path affects a
  package-path exception.
- README/docs/AGENTS: repair any public or standing-instruction routes changed
  by the version-history move.
- release notes, including `workbench/release-notes/RELEASE-0.5.0.md`, if they
  mention old framework guide or version-history locations.

## Later Decomposition Source Impact

Likely Slice03 source impact:

- split
  `knowledge/collaboration-framework/guides/AI-CONSTITUTION-SUPPLEMENT.md`
  into the approved four collaboration-framework guide files;
- update `knowledge/collaboration-framework/SKILL.md`;
- add or update `knowledge/collaboration-framework/version-history.md`;
- update `Makefile` `CF_FILES`;
- repair README/docs/AGENTS/component links and package-path exceptions only
  when the move requires it.

Likely Slice04 source impact:

- split
  `knowledge/engineering-methods/guides/AI-ENGINEERING-METHODOLOGY.md`
  into the accepted six engineering-methods guide files;
- update `knowledge/engineering-methods/SKILL.md`;
- update framework route references;
- add or update `knowledge/engineering-methods/version-history.md`;
- update `Makefile` `CF_FILES`;
- repair README/docs/AGENTS/component links and package-path exceptions only
  when the move requires it.

Likely Slice05 source impact:

- normalize sibling `version-history.md` files for `work-verification`,
  `testing`, `code-auditing`, `agent-coordination`, and
  `contribution-style`;
- reconcile embedded `## Version History` sections or record explicit
  exceptions;
- repair package-local routes for guides/templates/history files.

Likely Slice06 source impact:

- final README/docs/AGENTS/SKILL/component route reconciliation;
- final package validation and generated package inspection;
- isolated install smoke;
- CCDP package disposition;
- release notes reconciliation.

## Package Surfaces

Package surfaces likely affected by later slices:

- `Makefile` `ALL_SKILL_FILES`, when component `SKILL.md` files or descriptions
  change.
- `Makefile` `CF_FILES`, when collaboration-framework bundled component
  guides, templates, or sibling `version-history.md` files move.
- `scripts/stage-skill-entrypoint`, when source/package path divergence changes
  for `knowledge/collaboration-framework/SKILL.md`.
- `assets/packaging/path-exceptions.tsv`, only for narrow moved-path
  exceptions or newly proven package-only false positives.

## Validation Commands

Later source-edit slices should run the relevant subset and Slice06 should run
the complete set:

- source status before edits;
- `git diff --check`;
- local README/docs/AGENTS/SKILL/component-guide Markdown link validation;
- `make check-skills`;
- `make collab-framework`;
- `make all`;
- `make check-package-paths`;
- generated `collaboration-framework.zip` package inspection;
- generated installable skill zip inspection;
- isolated install smoke with `INSTALL_DIR` under `/private/tmp`;
- `make ccdp-package`;
- `make check-ccdp-package`;
- final source status.

Shared-build Make targets should be run serially, not in parallel, because
they write through common `build/` and `target/skills` paths.
