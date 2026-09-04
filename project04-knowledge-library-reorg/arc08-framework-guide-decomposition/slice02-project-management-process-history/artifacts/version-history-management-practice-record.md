# Version-History Management Practice Record

Source commit: `d3d1f5a` (`Clarify expedited mode and move PM history`)

## Decision

The framework component version-history management practice is documented in
the top-level source `AGENTS.md`.

This follows the operator clarification in
`../slice01-split-map-version-history-confirmation/artifacts/operator-confirmation-packet.md`:
the durable next-session-visible home should be top-level `AGENTS.md` unless
Slice02 found a clearly better source home.

## Rationale

No better source home was found for this practice. The rule controls future
source-edit sessions across multiple framework component roots, so it belongs
in the repository standing instructions rather than in one component guide.

## Recorded Practice

Top-level `AGENTS.md` now documents:

- each framework component root keeps its component version in `SKILL.md`;
- each framework component root keeps its component change log in a sibling
  `version-history.md`;
- changes to that component's `SKILL.md`, `guides/`, `templates/`, or
  `examples/` are recorded in the sibling version-history file;
- component histories should not live under `guides/` merely because a guide
  was edited.

This establishes the pattern used by the project-management move in Slice02
and expected by the later Arc08 version-history normalization slices.

