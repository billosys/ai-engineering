# navigation route validation evidence

## README Start Here

README.md retains a compact Start Here route set:

- docs/repository-overview.md
- docs/skill-library.md
- docs/collaboration-framework.md
- docs/knowledge-library-anatomy.md
- docs/building-and-installing.md
- docs/protocols.md
- docs/contributing.md

These focused docs form the expected end-user navigation set from Slice03.

## Focused Docs Cross-Links

The focused docs cross-link the current repository surfaces without restoring
old docs/dev or docs/design paths:

- repository overview points to docs/, knowledge/, protocols/, templates/, and
  packaging surfaces
- skill library points to knowledge/*/SKILL*.md entries and source component
  folders
- collaboration framework points to ../SKILL.md and framework component files
  under ../knowledge/
- knowledge library anatomy explains docs/ versus knowledge/ and package input
  boundaries
- building and installing points to ../Makefile and generated package outputs
- protocols points to ../protocols/ccdp/ and its assembled/spec/source paths
- contributing points to templates/GUIDE.md and repository checks
- Origins records historical provenance through repaired ../knowledge/ routes

## Docs Versus Knowledge Routing

docs/ is the user-facing documentation layer. knowledge/ is the source
substrate for skill bodies, guides, framework components, concept-card
materials, and package inputs. README.md and the focused docs preserve that
distinction: overview and guide pages live under docs/, while implementation
substrate links target knowledge/ directly.

## Origins

docs/ORIGINS.md current route status: historical Origins references are
retained as provenance, but paths now resolve through ../knowledge/... rather
than obsolete docs/dev or docs/design destinations.

## Route Scan Evidence

Commands run in the source checkout:

```sh
rg -n "\[[^\]]+\]\([^\)]+\)|https?://|docs/|knowledge/|protocols/|templates/|Makefile|package" README.md docs
rg -n "docs/dev|docs/design|CODE-AUDIT|AI-ENGINEERING|PROJECT-MANAGEMENT|SUBAGENT|LEDGER-DISCIPLINE|CONTRIBUTION-TICKET|templates/" README.md docs
find docs -maxdepth 2 -type f | sort
rg -n "^#{1,4} " README.md docs
```

Findings:

- broad route scan showed current README.md and docs/ routes to docs/,
  knowledge/, protocols/, templates/, Makefile, and package references
- stale route scan showed no docs/dev or docs/design hits
- remaining uppercase framework/template hits are current knowledge/ routes or
  literal validation-command text
- docs file inventory contains the seven focused docs plus docs/ORIGINS.md
- heading scan showed bounded H1/H2 structures with no navigation rewrite need
