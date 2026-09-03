# Moved Layout Composition Map

Date: 2026-09-02
Slice: Arc03 Slice06 implementation reconciliation
Source checkout: `/Users/oubiwann/lab/billosys/ai-engineering`

## Composition Verdict

The moved layout composition is coherent for Arc03 close. The final source
layout contains the accepted knowledge roots, preserves explicit exceptions,
and keeps CCDP under `protocols/ccdp` as a separate protocol distribution.

## Source History

- Slice03 source move: `99cebae1e98004164e4ea6735c4a68bc60c233da`
- Slice03 CDC compatibility repair: `27cc25581a16f56b87603f535b10481cf9178d79`
- Slice04 source ownership moves: `873a5502acef9c087cefd78d468cf6d123a27341`
- Slice05 CCDP freshness repair: `9b6d5d83d9c8debd977609aa1118004e89e2c895`
- Slice06 source commit: no source commit created

## Accepted Knowledge Roots Present

The source checkout contains the accepted Arc03 roots:

- `knowledge/collaboration-framework`
- `knowledge/engineering-methods`
- `knowledge/project-management`
- `knowledge/work-verification`
- `knowledge/testing`
- `knowledge/code-auditing`
- `knowledge/agent-coordination`
- `knowledge/contribution-style`

These roots compose with the pre-existing domain/tooling knowledge roots under
`knowledge/`, including Rust, Go, C++, JavaScript/Deno, Erlang, Cobalt, design,
Tailwind CSS, Deno linter, and Biome surfaces.

## Preserved Exceptions

The accepted exceptions remain in place:

- `docs/ORIGINS.md` remains under `docs/` as repository provenance/origin
  documentation.
- `templates/GUIDE.md` remains top-level as the cross-cutting template guide
  exception.
- `protocols/ccdp` remains under `protocols/` and is not folded into the
  installable skill library.
- Biome remains a multi-entrypoint package source under `knowledge/biome`.

## Recomposition Against Arc03 Capability

Arc03 promised to execute accepted file moves and link updates while preserving
history, minimizing prose changes, and keeping package/build validation green.

The final source layout satisfies the move portion of that capability:

- Collaboration-framework source payload moved from old `docs/` and
  `templates/` surfaces into `knowledge/collaboration-framework` in Slice03.
- Specialist component and method ownership moved into owner roots in Slice04.
- Package/list and link behavior was reconciled in Slice05.
- Slice06 found no additional source movement or source repair requirement.

No moved source path required a new broad package-path exception during
implementation reconciliation.
