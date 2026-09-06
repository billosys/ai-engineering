# Arc 08 Closing Report: Framework Guide Decomposition and Version History Normalization

Status: closed.

## Capability

Arc08 split the accepted collaboration-framework, engineering-methods, and
framework component monolith/pre-split guide surfaces into focused
selective-load guide files; normalized framework component version histories as
sibling `version-history.md` files beside component `SKILL.md` files;
reconciled the project-management guide/example layout; corrected Expedited
Mode wording; and verified source, package, install, CCDP, and release-note
behavior after the decomposition.

Composition verdict: delivered.

## Slice Walk

| Slice | Outcome | Evidence |
| --- | --- | --- |
| Slice01: Split Map, Version-History Contract, and Expedited Wording | Delivered | `slice01-split-map-version-history-confirmation/cdc-verification.md` verified the operator-confirmation packet, source-impact map, monolith/history inventory, and Expedited Mode wording target before source edits. |
| Slice02: Project-Management Process Wording and Version-History Baseline | Delivered | `slice02-project-management-process-history/cdc-verification.md` verified corrected Expedited Mode wording, project-management sibling history placement, and top-level `AGENTS.md` version-history practice documentation. |
| Slice03: Collaboration-Framework Posture Guide Split | Delivered | `slice03-collaboration-framework-posture-split/cdc-verification.md` verified the four numbered posture guides, old supplement disposition, route repair, and package validation. |
| Slice04: Engineering-Methods Guide Split | Delivered | `slice04-engineering-methods-guide-split/cdc-verification.md` verified the six numbered engineering-methods guides, old methodology disposition, route repair, and package validation. |
| Slice05: Component Version-History Normalization | Delivered | `slice05-component-version-history-normalization/cdc-verification.md` verified sibling histories for work-verification, testing, code-auditing, agent-coordination, and contribution-style, plus embedded-history disposition. |
| Slice06: Project-Management Example Layout Reconciliation | Delivered | `slice06-project-management-example-layout-reconciliation/cdc-verification.md` verified the accepted `examples/01-worked-example-odm.md` layout and package route repair. |
| Slice07: Work-Verification Guide Split | Delivered | `slice07-work-verification-guide-split/cdc-verification.md` verified the five numbered work-verification guides and retained ledger template support asset. |
| Slice08: Testing Guide Split | Delivered | `slice08-testing-guide-split/cdc-verification.md` verified the three testing guides and old `CODE-COVERAGE.md` disposition. |
| Slice09: Code-Auditing Guide Split | Delivered | `slice09-code-auditing-guide-split/cdc-verification.md` verified the five audit guides and diagnosis-only contract preservation. |
| Slice10: Agent-Coordination Guide Split | Delivered | `slice10-agent-coordination-guide-split/cdc-verification.md` verified the four delegation/context/result/anti-pattern guides and old `SUBAGENT-DELEGATION-POLICY.md` disposition. |
| Slice11: Contribution-Style Guide Split | Delivered | `slice11-contribution-style-guide-split/cdc-verification.md` verified the contribution-style/workflow split and retained ticket template. |
| Slice12: Final Validation, Install, Link, and Release Reconciliation | Delivered | `slice12-final-validation-release-reconciliation/cdc-verification.md` verified final route, package, install, CCDP, and release-note reconciliation, including the operator-review project-management README rename and CDC's final CCDP freshness repair. |

## Composition Check

Arc08's slices compose into the promised capability:

- Framework posture now loads through focused numbered guides:
  `01-posture-and-ethics.md`, `02-structural-pulls.md`,
  `03-collaborative-rights.md`, and `04-component-route-table.md`.
- Engineering methods now loads through six focused guides for methodology,
  knowledge substrate, process rigour, operational routing, boundary analysis,
  and source/package/release gates.
- Project-management now uses `guides/README.md` as the guide-set wayfinder,
  keeps eight numbered guides, and keeps the worked example under
  `examples/01-worked-example-odm.md`.
- Work-verification, testing, code-auditing, agent-coordination, and
  contribution-style all have component `SKILL.md` wayfinders plus focused
  numbered guides for selective loading.
- Reusable support assets remain templates where appropriate:
  `work-verification/templates/LEDGER-DISCIPLINE.md` and
  `contribution-style/templates/CONTRIBUTION-TICKET.md`.
- Each framework component root keeps component history in a sibling
  `version-history.md`; no guide/template/example-local component history file
  remains.
- Expedited Mode wording now names only the explicit commit/close/advance
  behaviors and explicitly rejects shortcuts, skipped validation, weaker
  evidence/review, inferred source scope, scope reduction/change, timeline
  interpretation, and operator-gate override.
- Old monolith and pre-split filenames are no longer live load targets or
  package routes. Remaining mentions are historical, provenance, disposition,
  or package-local template text.
- `collaboration-framework.zip` exposes the current focused guide layout and
  no old monolith/pre-split filename in its archive listing.
- Final package validation passes on the current project baseline: 13
  installable skill zips, 222 packaged Markdown files, 0 package-path hard
  failures, 376 warnings, 3 explicit exceptions, and 656 skipped external URLs.
- Current isolated install smoke installs 13 `SKILL*.md` entrypoints and no
  `ccdp` install root.
- CCDP remains a protocol package. `make ccdp-package` and
  `make check-ccdp-package` pass after the CDC date-only assembled-spec refresh
  in source commit `b18d049333799141f4d2e2328b1cd6ba444a437b`.

No Arc08 scope item is known to have been silently dropped.

## Accumulated Arc-Plan Change Log

Arc08 received fourteen tracked arc-plan updates:

- v1.1 closed Slice01 and corrected the A-1 operator-confirmation wording.
- v1.2 recorded operator approval and clarified version-history and Expedited
  Mode wording.
- v1.3 through v1.5 closed Slices02-04 and opened component-history
  normalization.
- v1.6 integrated the operator-approved remaining component guide splits into
  Arc08.
- v1.7 through v1.13 closed Slices05-11 and opened the next focused split or
  final reconciliation slice.
- v1.14 closed Slice12, recorded the final CCDP freshness repair, and closed
  Arc08.

## Bubble-Up to Project04

Arc08 delivers project ledger row P-9. The framework guide surface now supports
selective loading without losing the composed collaboration-framework entrypoint
or the operational meaning of the original monoliths.

Project04 should close by reproducing project row P-7 against the current
README/docs/knowledge/protocol/package layout and marking P-9 done. The final
project close should also record Arc09's accepted scientific-methods expansion
and Arc10's evidence archive as later operator-approved additions that do not
invalidate Arc08 closure.
