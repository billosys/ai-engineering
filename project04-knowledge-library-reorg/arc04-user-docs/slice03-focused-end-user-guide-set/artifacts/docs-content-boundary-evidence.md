# Docs Content Boundary Evidence

docs content boundary evidence for Arc04 Slice03.

Source commit: `bcfd986ca1a9078508bfb2628d574af69ddc1fe1`

## Boundary Checked

The expanded `docs/` pages explain repository materials for human readers.
They route to source surfaces such as `knowledge/`, `protocols/ccdp/`,
`templates/GUIDE.md`, `SKILL.md`, and `Makefile` instead of duplicating the
actual substrate.

The `knowledge/` substrate remains the owner of skill entrypoints, guides,
concept-card material, extraction metadata, sources, examples, owner-local
templates, tools, and workbench material.

## Not Duplicated

- The skill library page lists package names and source entrypoints, but does
  not copy domain/tooling guide content out of `knowledge/`.
- The collaboration framework page links to component documents under
  `knowledge/`, but does not copy the framework source documents into `docs/`.
- The knowledge anatomy page explains common root shapes, but does not move or
  duplicate sources, concept cards, or extraction metadata.
- The protocols page routes to CCDP entrypoints, but does not duplicate CCDP
  protocol chapters.
- The contributing page points to `templates/GUIDE.md` and validation
  commands, but does not create a new process substrate in `docs/`.

## Arc05 Boundary

Arc05 owns public vocabulary finalization. Slice03 wording remains
provisional: skill kind, atomic, composite, domain/tooling,
framework/operational, method, and protocol distribution are used only as
reader wayfinding and are not finalized here.
