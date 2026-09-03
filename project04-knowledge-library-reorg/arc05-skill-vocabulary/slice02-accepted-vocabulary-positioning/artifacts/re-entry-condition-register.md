# re-entry condition register

## Purpose

This re-entry condition register records future evidence that should reopen
Arc05 vocabulary decisions. Re-entry is tied to concrete repository facts, not
taste or preference drift.

## Entrypoint Evidence

Reopen vocabulary if:

- a current skill entrypoint changes load reason
- a new `SKILL.md` or `SKILL-*.md` entrypoint is added
- top-level `SKILL.md` stops acting as the collaboration-framework composer
- a current atomic example becomes a router over independently loadable units
- a component gains standalone entrypoint behavior that public docs must name

Affected decisions: skill kind, atomic, composite, public examples,
framework/operational language, method skill language, and SKILL.md wording.

## Package Root Evidence

Reopen vocabulary if:

- generated package root behavior changes
- source root and package root are made equivalent by policy
- package root names are renamed
- Biome's source root is split into separate roots
- a multi-entrypoint source root is added or removed

Affected decisions: package root caveats, Biome positioning, source-root /
package-root equivalence avoid-list, and package-facing wording.

## Makefile Target Evidence

Reopen vocabulary if:

- Makefile target names or help text change the public build/install contract
- `INSTALL_ZIPS`, `ALL_SKILL_FILES`, or `CF_FILES` changes package membership
- `make install` starts installing a surface previously described as separate
- CCDP targets merge into installable skill targets

Affected decisions: skill package, protocol package, protocol distribution,
support material, package-facing language, and validation requirements.

## Package-Path Exception Evidence

Reopen vocabulary if:

- `package-path-exceptions.tsv` gains or removes exceptions tied to public
  wording
- package-path validation warnings become hard failures
- an accepted exception hides a public category or topology claim

Affected decisions: source/provenance, support template, package-local route
language, and generated zip acceptance.

## Generated Zip Evidence

Reopen vocabulary if:

- generated zip contents differ from accepted public package descriptions
- a package includes or excludes material that changes the load reason
- `collaboration-framework.zip` no longer contains a composed route table and
  specialist component material
- `ccdp.zip` begins behaving like an installable assistant skill package

Affected decisions: atomic/composite examples, collaboration-framework
positioning, CCDP positioning, package root wording, and package validation.

## CCDP Evidence

Reopen vocabulary if:

- CCDP gains an accepted installable assistant-skill entrypoint
- `make install` installs CCDP
- CCDP package validation no longer uses separate CCDP targets
- docs route CCDP into `knowledge/` as a skill source without a protocol
  package decision

Affected decisions: CCDP, protocol distribution, protocol package, "CCDP is a
skill" avoid-list, and docs/protocols wording.

## Biome Evidence

Reopen vocabulary if:

- `knowledge/biome/` stops being a multi-entrypoint root
- one Biome package absorbs the other
- package names change from `biome-js-linter.zip` or `biome-linter.zip`
- public docs need to explain Biome as more than a current package/source-root
  edge case

Affected decisions: Biome edge-case positioning, multi-entrypoint wording,
package root language, atomic package entries, and composite source root
language.

## Docs Route and README Evidence

Reopen vocabulary if:

- README.md or docs/ route users through a different top-level taxonomy
- docs/ stops being explanatory and starts duplicating knowledge substrate
- knowledge/ stops being the material source for skill content
- SKILL.md links or docs routes change the collaboration-framework component
  map
- public docs introduce bridge/integration layer or application/task bundle as
  primary end-user categories

Affected decisions: docs route, README language, SKILL.md wording, public
versus maintainer-facing vocabulary, and Arc05 examples.

## Planned Surface Evidence

Reopen vocabulary when `concept-card-method` lands in source or package form.
The evidence must include current source path, entrypoint, package behavior,
validation command results, and whether its load reason is atomic method or
composite method/framework behavior.

Until that evidence exists, concept-card-method remains planned method skill
language only.
