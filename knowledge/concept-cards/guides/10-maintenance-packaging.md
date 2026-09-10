# Maintenance And Package Boundaries

Use this guide to maintain the method's source core and to hand off support
and integration work without overstating what exists. The
[guide map](../SKILL.md#guide-map) exposes all ten live core guides. Their
presence supplies instructions; it does not establish that a workflow has been
run against a corpus or that an installable package has been delivered.

## Source Core Ownership

After Arc03, `concept-cards` owns the entrypoint and guidance for load scope,
operator workflow, extraction, re-extraction, provenance, preservation,
evidence lifecycle, relationships/CQs, reconciliation, validation/verification,
memory admission and maintenance boundaries. The sibling
[version history](../version-history.md) records significant source changes.

Keep raw PDF/EPUB/HTML extraction and converted-source preparation routed to
`document-extraction`. Consume its manifest, locator/media mappings, readiness
and caveats as upstream provenance, then assess support for each assertion.
Do not copy conversion procedures into this method or reinterpret preparation
readiness as semantic verification. Domain expertise remains responsible for
domain correctness; project, release and installation workflows remain with
their applicable owners.

## Remaining Delivery Ownership

| Owner | Remaining deliverables and acceptance boundary |
| --- | --- |
| Arc04 | Sibling templates, representative examples, and reference/review material are live source support. The references preserve construct distinctions and result provenance, including incomplete and conflicting cases. Source presence does not prove package contents or installability. |
| Arc05 | Package targets, Makefile integration, generated zips, docs, README/discoverability, install behavior and package validation. These are not yet implemented for this skill. Source-file presence, a Markdown link check or another skill's package success does not establish this skill's packaged contents or installability. |

Current sibling support lives in `templates/`, `examples/`, and `references/`.
The current helper macros copy `guides/`, `templates/`, and `examples/`, but
not `references/`. Arc05 must add and validate package support for this sibling
directory before claiming generated-zip contents or installability. Do not create
placeholder assets or links to absent files to imply completion.

## Promise Boundary

The source core is not an executable validator. It instructs an actor how to
record structural and semantic checks; a described check is not an implemented
program or a performed check. A future schema would describe structure and
would not, by itself, prove semantic support or enforce memory admission.

This skill does not implement runtime services, a graph or ontology database,
GraphRAG, CCDP services or memory runtime automation. It does not supply live
corpus processing, retrieval indexes or automatic reconciliation. Edge records
represent relations; CQ records represent requirements and scoped observations;
admission records permit bounded reliance. None creates the corresponding
runtime, data store or consumer behavior.

Keep evidence claims at their real scope: source guidance authored, record
written, check performed, independent verification reproduced, package built,
installation inspected and runtime action observed are different achievements.
Report missing evidence rather than deriving one from another.

## Maintain The Core Coherently

Before editing, identify the owning concern and its callers in the entrypoint,
[load contract](./01-load-contract.md) and
[operator workflow](./02-operator-workflow.md). Read affected downstream guides
so route changes do not silently alter their semantics. Preserve these
distinctions in both prose and future records:

- Card identity and concept boundary; claims; source locators, spans and support.
- Relationship identity, endpoint validity and semantic warrant; CQ coverage,
  answerability and retrieval observations.
- Extraction confidence and evidence grade; validation result, verification
  result/state, reconciliation result/state, preservation and memory admission.
- Actor/run provenance, input/output revisions, actual review scope,
  same-context checks, independent review and operator-reported evidence.

Keep prior values and result applicability recoverable when meanings or routes
change. Record significant changes in the sibling history and maintain the
owning entrypoint's version metadata; avoid duplicate skill-version prose and
guide-local histories. Apply the repository's maintenance instructions in its
own governance files rather than copying that contract into user procedures.

Review links against files that actually exist, and inspect active availability
statements for stale promises. Historical history entries can retain the
availability that was true at the time. Future support assets should refer to
the owning procedure instead of creating a competing method definition.

## Human-Assisted And Agent-Direct Maintenance

In human-assisted work, identify the supplied source revision and the files or
package observations that the operator reports. Return proposed edits or a
handoff packet if direct inspection/writing is unavailable; do not describe
unseen installed contents as checked.

In agent-direct work, inspect accessible source and callers, make only
authorized changes and record the exact revised paths and actual checks.
Reopen written artifacts. Keep source validation, independent review and
package/install observations distinct, including when no package work was
requested. This guide does not initiate a project, release or installation.

## Handoff To Arc04 And Arc05

For Arc04, identify the current core revision, construct/attachment requirements,
live guide routes, representative success and incomplete/conflict cases,
provisional record vocabulary and unresolved format decisions. Existing
templates, examples, and references preserve uncertainty, scoped results and
provenance. Arc05 package support must preserve this material without turning
its prose options into a finalized machine schema.

For Arc05, identify the eventual complete source/support inventory, intended
package boundaries, cross-skill preparation route and remaining packaging,
docs/discoverability and install requirements. Require evidence from that
skill's actual generated zip contents, local/package links and inspected
installation before reporting those capabilities. Existing aggregate checks
may build unrelated packages; their success does not imply this skill ships.

For either handoff, report source/input/output revisions and paths, implemented
guidance, validation actually performed, remaining deliverables, missing evidence
and the bounded next work. Preserve source-only status until the responsible
delivery work demonstrates more. The core being ready for review does not
close an arc or project without its own ledger composition and verification.
