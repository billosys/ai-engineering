# CDC-Direct Prompt: Arc09 Slice01 Scientific Methods Skill Implementation

Operator override: this slice was executed directly by CDC rather than handed
to a separate CC session. This file is retained as the canonical scope record
and replayable implementation prompt.

Implement the `scientific-methods` method skill in the source checkout at
`/Users/oubiwann/lab/billosys/ai-engineering`.

Create:

- `knowledge/scientific-methods/SKILL.md`
- `knowledge/scientific-methods/version-history.md`
- focused guides under `knowledge/scientific-methods/guides/`
- reusable templates under `knowledge/scientific-methods/templates/`

Wire:

- `Makefile` target `scientific-methods`
- `scientific-methods.zip` in installable skill package lists
- top-level `README.md`
- `docs/skill-library.md`
- `docs/building-and-installing.md`
- `docs/collaboration-framework.md`
- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`
- `workbench/release-notes/RELEASE-0.5.0.md`

Constraints:

- Keep scientific-methods independent and installable.
- Do not bundle scientific-methods into `collaboration-framework.zip`.
- Add only light collaboration-framework wayfinding that tells a loaded
  collaboration-framework session when to load scientific-methods separately.
- Keep the method practical: experimental discipline for working sessions, not
  academic ceremony.

Validate:

- `git diff --check`
- `git diff --cached --check`
- `make check-skills`
- focused local Markdown link validation
- `make scientific-methods`
- `make check-package-paths`
- `unzip -l target/skills/scientific-methods.zip`
- isolated `make install INSTALL_DIR=...` smoke with no `ccdp` install root

Report source commit, exact source files changed, validation results, package
baseline, install-smoke result, and any limitations.
