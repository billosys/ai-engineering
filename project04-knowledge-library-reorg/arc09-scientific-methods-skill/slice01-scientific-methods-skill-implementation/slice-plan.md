# Slice 01: Scientific Methods Skill Implementation

## Goal

Create and package the `scientific-methods` method skill, document it for
users, and add collaboration-framework wayfinding so controlled inquiries,
A/B trials, regression comparisons, protocol design, evaluation rubrics, and
threats-to-validity analysis can route to it.

## Execution Mode

CDC-direct by operator override. No separate CC handoff/iteration is required.
The canonical `cc-prompt.md` is retained as a replayable implementation prompt
and scope record.

## In Scope

- Add `knowledge/scientific-methods/SKILL.md`.
- Add `knowledge/scientific-methods/version-history.md`.
- Add focused guides under `knowledge/scientific-methods/guides/`.
- Add reusable templates under `knowledge/scientific-methods/templates/`.
- Add `make scientific-methods` and include `scientific-methods.zip` in
  installable skill lists.
- Update README and user docs for discoverability.
- Update collaboration-framework wayfinding to load scientific-methods
  separately when the conversation becomes a controlled inquiry.
- Update release notes for the new skill and package baseline.
- Validate source, package, zip, and install behavior.

## Out Of Scope

- Adding scientific-methods to `collaboration-framework.zip`.
- Treating scientific-methods as a framework component.
- Changing Arc08 closure state.
- Implementing concept-card-method.
- Adding executable experiment runners or persistent data stores.

## Verification Approach

Run:

- `git diff --check`
- `git diff --cached --check`
- `make check-skills`
- focused local Markdown link validation
- `make scientific-methods`
- `make check-package-paths`
- `unzip -l target/skills/scientific-methods.zip`
- isolated `make install INSTALL_DIR=...` smoke

## Exit Criteria

The slice exits when the source commit exists, all validation commands pass,
the scientific-methods package includes its entrypoint, guides, templates, and
version history, README/docs/collaboration-framework wayfinding exists, and
the planning record discloses the same-context CDC verification limitation.
