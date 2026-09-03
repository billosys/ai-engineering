# source edit impact map

## Boundary

source-files-edited: false

This Slice01 artifact maps possible future source edits. It does not authorize
those edits. no source edit was made in Slice01, and no source commit was
created.

authorization boundary: later slices must explicitly authorize any
README.md, docs/, SKILL.md, package-facing, Makefile, package-list,
package-path-exception, generated zip, concept-card-method, or CCDP wording
change.

## Possible README.md Impacts

Potential later edit surface:

- top-level definition of AI Engineering as skills, guides, methods,
  templates, and protocol material
- "programming and tooling skill packages" wording
- collaboration-framework wording
- support material wording
- CCDP separate packaging wording
- Current Boundaries language about skill-category and topology

Risk: README.md is the first public route, so accepted vocabulary must be short
and not overclaim planned method surfaces.

## Possible docs/ Impacts

Potential later edit surfaces:

- `docs/skill-library.md`: package table, choosing what to load, package/source
  distinction, planned method material
- `docs/collaboration-framework.md`: composer, narrow components, daily-driver
  language, provisional category language
- `docs/knowledge-library-anatomy.md`: source roots, package roots, Biome/Deno
  exceptions, CCDP boundary
- `docs/protocols.md`: protocol distribution versus skill package language
- `docs/repository-overview.md`: top-level surfaces and boundary language
- `docs/contributing.md`: category/topology wording, new skill surface
  requirements, protocol package warning
- `docs/building-and-installing.md`: installable skill package and CCDP command
  language
- `docs/ORIGINS.md`: historical prose should remain provenance-oriented; edit
  only if vocabulary creates confusion in current links or route labels

## Possible SKILL.md Impacts

Potential later edit surface:

- top-level collaboration-framework description
- "Does NOT load domain skills under ./knowledge/ -- loaded separately"
- route table labels and component descriptions
- frontmatter metadata category `meta-skills`
- version history if wording changes affect behavior or public route contract

Risk: SKILL.md is both public entrypoint and package input; changes require
`make check-skills`, package-path validation, and collaboration-framework
package validation.

## Possible Package-Facing Impacts

package-facing surfaces:

- Makefile `INSTALL_ZIPS`, `ALL_SKILL_FILES`, `CF_FILES`, help text, and
  package target descriptions
- frontmatter names/descriptions in knowledge/.*/SKILL*.md
- metadata category values in SKILL.md and knowledge/.*/SKILL*.md
- package-path-exceptions.tsv only if wording or links create new package-path
  behavior
- generated zips only through Make targets, not direct edits

Risk: public vocabulary may be reflected in package metadata descriptions but
should not force package-root renames unless Slice02 explicitly accepts that
scope.

## Protocol and Support Impacts

CCDP:

- `docs/protocols.md` and `protocols/ccdp/README.md` already use protocol
  distribution/package language
- later edits should preserve separate `make ccdp-package` and
  `make check-ccdp-package` behavior

Templates:

- `templates/GUIDE.md` is currently cross-cutting support material
- owner-local templates under knowledge/ should remain tied to their owning
  surface unless a later slice changes that policy

## No Unauthorized Source Surfaces

No Slice01 edits were made to README.md, docs/, SKILL.md, knowledge/,
Makefile, package-path-exceptions.tsv, generated zips, protocols/ccdp/, or
templates/GUIDE.md.

Later slices must carry explicit authorization before editing any of those
surfaces.
