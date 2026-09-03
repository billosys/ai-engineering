# deferred re-entry notes

## Scope

Slice03 implemented only authorized README, focused-doc, and top-level
`SKILL.md` public wording. It did not edit package-facing metadata, source
layout, generated packages, CCDP source, templates, or knowledge entrypoint
metadata.

## Deferred Package-Facing Work

Deferred package-facing surfaces:

- `Makefile`
- package target names
- `INSTALL_ZIPS`
- `ALL_SKILL_FILES`
- `CF_FILES`
- generated zip contents as committed release artifacts
- package root names
- `package-path-exceptions.tsv`

No package-facing source edit was required to implement the accepted public
wording. If later public wording requires frontmatter category alignment,
package root renames, target help text changes, or exception changes, reopen
Arc05 or Arc06 with explicit source/package authorization.

## Deferred Metadata Work

`knowledge/*/SKILL*.md` frontmatter names, descriptions, and categories were
not edited. Metadata category alignment remains deferred because Slice02 did
not authorize package metadata changes.

## Deferred CCDP Work

CCDP remains a protocol distribution and protocol package. Slice03 did not
edit `protocols/ccdp/**` and did not repackage CCDP as an installable skill.

During an intermediate edit to `docs/protocols.md`, `make ccdp-package`
reported:

```text
ERROR: protocols/ccdp/composite-cognition-dispatch-protocol.md is stale
Run 'make -C protocols/ccdp ccdp-rfc' and commit the generated refresh.
```

Refreshing the assembled CCDP spec would edit `protocols/ccdp/**`, which is
outside Slice03 authorization. The final source commit leaves `docs/protocols.md`
unchanged, so this is recorded as deferred CCDP re-entry evidence rather than
a Slice03 source repair.

## Deferred Template Work

`templates/GUIDE.md` was not edited. Public docs now describe it as support
material / support template, but the template itself remains outside this
slice.

## Deferred Knowledge Entrypoint Work

Knowledge entrypoint metadata was not edited. `concept-card-method` remains a
planned method skill until source, skill entrypoint, package behavior, and
validation evidence exist.

## Re-Entry Conditions

Re-enter vocabulary work if:

- package-facing metadata changes public category wording;
- package roots or target names change;
- generated zip contents change a public load reason;
- CCDP gains an installable assistant-skill entrypoint or `make install`
  starts installing CCDP;
- `concept-card-method` lands as live source or package material;
- Biome stops being a multi-entrypoint knowledge root;
- `collaboration-framework` stops being the top-level daily-driver composer.
