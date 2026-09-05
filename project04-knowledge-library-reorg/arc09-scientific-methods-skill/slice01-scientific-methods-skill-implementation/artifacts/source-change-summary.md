# Source Change Summary

## Source Commit

`a2122abbe75b42f87e550c87ba1150b51d7abb38`

Commit message: `Add scientific-methods skill`

## New Skill Surface

Added `knowledge/scientific-methods/` as a live method skill:

- `SKILL.md` - entrypoint and guide router.
- `version-history.md` - sibling component history.
- `guides/01-inquiry-framing.md`
- `guides/02-experiment-design.md`
- `guides/03-controls-and-confounds.md`
- `guides/04-operational-measures.md`
- `guides/05-protocol-and-prompt-design.md`
- `guides/06-evidence-capture.md`
- `guides/07-comparison-and-regression-testing.md`
- `guides/08-analysis-and-threats-to-validity.md`
- `guides/09-anti-patterns.md`
- `templates/experiment-protocol.md`
- `templates/ab-comparison-prompt.md`
- `templates/evaluation-rubric.md`

## Package Wiring

`Makefile` now includes:

- `scientific-methods.zip` in `SKILL_ZIP_NAMES`;
- `knowledge/scientific-methods/SKILL.md` in `ALL_SKILL_FILES`;
- phony target `scientific-methods`;
- `make scientific-methods` package target;
- `scientific-methods` in `make skills`, `make all`, and `make install`.

The target packages `SKILL.md`, `version-history.md`, `guides/`, and
`templates/`.

## Public Documentation

Updated:

- `README.md`
- `docs/skill-library.md`
- `docs/building-and-installing.md`
- `docs/collaboration-framework.md`
- `workbench/release-notes/RELEASE-0.5.0.md`

The public docs name `scientific-methods` as a live method skill for practical
inquiry, controlled comparison, experiment planning, evaluation rubrics,
evidence capture, regression analysis, and threats-to-validity analysis.

## Collaboration-Framework Wayfinding

Updated:

- `knowledge/collaboration-framework/SKILL.md`
- `knowledge/collaboration-framework/guides/04-component-route-table.md`
- `knowledge/collaboration-framework/version-history.md`

The collaboration-framework route is deliberately light: it recognizes
controlled inquiry, A/B prompt or framework trials, regression investigations,
operational measures, experiment protocols, evaluation rubrics, evidence
capture, and threats-to-validity analysis as signals to load
`scientific-methods` separately when available.

`scientific-methods` is not bundled into `collaboration-framework.zip`.
