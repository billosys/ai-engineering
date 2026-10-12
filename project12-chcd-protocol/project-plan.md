---
project: project12-chcd-protocol
status: active
depends-on: []
blocks: []
related: []
---

# CHCD Protocol — Rename and Model Generalization

## Purpose and authority

Evolve the Composite Cognition Dispatch Protocol (CCDP) into the **Composable
Heterogeneous Cognition Dispatch Protocol**, normally written **CHCD Protocol**
and pronounced **Check-Dee Protocol**. Support services using one or more
models of arbitrary architecture and modality, alone or composed with other
computational services, through explicit capability and data contracts.

The Operator requested this planning session and historical-copy migration on
2026-10-09, then accepted 0.3 with continued support for legacy CCDP names and
deprecation notices announcing removal in 0.4. Planning lives on branch
`planning`, in `.worktrees/planning/project12-chcd-protocol/`, as recorded in
[local instructions](AGENTS.md). This document is the initial design brief and
arc roadmap; [the ledger](ledger.md) records project acceptance criteria.
Detailed design follows the source/evidence inventory in Arc01.

Current status: active; [Arc01](arc01-baseline-and-evidence/arc-plan.md) and
[Slice01](arc01-baseline-and-evidence/slice01-baseline-and-migration-inventory/slice-plan.md)
are open at the Operator's request. The initial evidence-only CC assignment is
prepared for Operator relay; execution has not been reported. No source
implementation is authorized. The project is a specification and publication migration, not
a reference implementation project or a claim of production readiness.

## Confirmed direction

- Full title: Composable Heterogeneous Cognition Dispatch Protocol.
- Normal prose: CHCD Protocol; pronunciation: Check-Dee Protocol.
- Compact path segment: `chcdp`, including `protocols/chcdp/` and the published
  successor under `site/protocols/chcdp/`. Keep deployment base-path handling
  explicit; do not assume the project site is hosted at the domain root.
- Preserve `protocols/ccdp/` as historical source; copy the current 0.2 contents
  to seed the successor rather than moving or rewriting the predecessor.
- Revise and verify both the specification's sources/references and the visual
  guide. Add HTML meta redirects for the corresponding published CCDP pages.
- Release the generalized successor as Draft 0.3. Continue supporting legacy
  CCDP protocol names in 0.3 with deprecation notices; remove that support in
  0.4. Preserve historical artifacts and migration redirects beyond removal.

## Baseline and preservation contract

The inspected source checkout HEAD was
`dffa504e851b03b8e4746f1941068e4cc850b612`. There were 103 tracked files under
`protocols/ccdp/`; `src/README.md` identifies the baseline as Draft v0.2 with
review iterations through v0.2m incorporated, and explicitly says it is not
implementation-ready. The assembled specification's SHA-256 was
`aab693d14819dcb0f85fa2fc064c80083491d0684771f8f2ad77d42d3d0da254`.
These are intake observations, not a substitute for the full Arc01 manifest.

Pin the exact baseline revision and record the tracked file inventory and
content hashes before copying. Establish byte equivalence at the copy boundary
before successor edits, retaining evidence of that state. Do not accidentally
copy ignored build outputs or workbench material with an unrestricted directory
copy. Inventory any additional material and explicitly disposition it.

Do not edit the frozen predecessor to add archive banners or successor names.
Explain lineage in the successor and repository navigation. Keep original
history and references intact; revised successor citations must not overwrite
the historical record. Verify the full predecessor tree remains unchanged at
project closure. Decide the retention/build policy for historical packaging
and assembler tooling during Arc01; do not silently delete either.

Published HTML is separate from that archive. The Pages workflow uploads
`site/`; current landing and guide pages are
`site/protocols/ccdp/index.html` and
`site/protocols/ccdp/visual-guide/index.html`. The source and published guide
copies are not byte-identical at intake (two changed lines); reconcile the
reason before choosing an authoritative authoring/publishing route.

## Generalization design brief

Preserve these earlier design notes throughout the project:

1. **Keep cognitive service as the umbrella.** Models, provers, planners,
   databases and human services remain distinct implementations behind typed
   interfaces. Use learned model where the current text unnecessarily assumes
   an LLM; retain LLM terminology where the claim or example is actually
   specific to language models.
2. **Generalize service modes deliberately.** Revisit Mode 1 as a learned-model
   service and Mode 3 as a composite service. Cover one model, multiple models
   of the same type, heterogeneous models, and combinations with other engines.
   Resolve overlapping classifications explicitly; service mode does not by
   itself determine provenance grade.
3. **Make non-text contracts concrete.** Cover typed inputs and outputs,
   multimodal data, latent representations and referenced artifacts where
   justified. Representation identity, schema compatibility and adapters must
   be explicit; arbitrary model type does not imply arbitrary representations
   are interchangeable or that every backend needs built-in protocol support.
4. **Specify composition boundaries.** Distinguish a service's internal model
   pipeline from protocol-visible decomposition. Exercise sequential, parallel
   and ensemble compositions; make aggregation, partial failure, cancellation,
   retries, idempotency and result equivalence explicit where affected.
5. **Preserve evidence discipline.** Separate model/inference identity,
   repeatability, prediction correctness and evidence for the semantic claim.
   Deterministic inference does not automatically make a prediction COMPUTED
   or verified. Multiple models agreeing does not establish independent
   corroboration; shared weights, training and dependencies matter. Preserve
   composition traces and the distinction between policy ordering and a
   universal epistemic hierarchy.
6. **Generalize resource accounting.** Review token-only assumptions alongside
   existing cost, capacity and deadline contracts. Define units, estimation and
   unknown values where new dimensions are needed, without mandating irrelevant
   accounting fields for every service.
7. **Keep the Dispatcher structural.** Models may implement semantic services;
   their use must not make the Dispatcher a hidden reasoning agent. Preserve
   opaque Content, structural validation, audit, escalation and human authority.
8. **Scope scientific claims to evidence.** Transformer complexity results,
   autoregressive-language limitations and self-correction findings must not
   become claims about all models through terminology substitution. JEPA, Jev
   and Laya are Operator-supplied research leads; verify exact referents,
   architecture and supported claims before admitting examples.

## Compatibility and deprecation contract

The Operator's 0.3/0.4 decision applies to protocol name compatibility, not just
the document title. Arc01 must inventory legacy names across capability types,
schema references, envelope fields (including `ccdp_version`), metadata,
examples, audit records, tooling, packages and published links. Classify which
are protocol aliases, external navigation, implementation names or immutable
historical identifiers; do not assume all have the same migration behavior.

For protocol aliases, the 0.3 design must:

- Specify canonical CHCD spellings and an explicit mapping for supported legacy
  CCDP names, including `org.ccdp.*`; distinguish defined names from extensions
  and unrecognized identifiers.
- Accept supported legacy names without forcing an immediate client migration,
  while marking them deprecated and identifying 0.4 as the removal release.
- Define accepted input, emitted output and any negotiation/echo behavior;
  resolve messages containing both spellings, conflicting values and mixed
  legacy/new references without ambiguous precedence.
- Ensure alias handling does not bypass capability authorization or schema
  validation, break signatures, change replay/idempotency identity, or falsify
  audit provenance. Specify where normalization occurs and what is retained.
- Define discoverable documentation and operational deprecation notices without
  inventing ad hoc envelope fields or making formerly valid requests fail.
- Keep document release numbering separate from wire, registry and audit schema
  versions. State exactly which version boundary activates removal.

0.4 removes support for the legacy protocol aliases. This project must deliver
the migration guidance and explicit removal contract; implementing a later
0.4 release is outside the current 0.3 scope. Existing archived records retain
their original identifiers. Redirects and historical documentation are not
runtime alias support and are not scheduled for deletion by this decision.

## Evidence, guide and publishing work

Inventory normative and informative references and the claims they support;
retain a complete denominator, verification date, exact source/version and
accessible evidence. Prefer primary sources. A reachable URL alone does not
verify a claim. Record unavailable or blocked sources and resolve, replace or
narrow unsupported successor claims before publication. Recheck comparative
claims about other protocols against their actual versioned specifications.

Carry forward and disposition the baseline's unfinished schemas, conformance
suite, Service/Registry requirement IDs, reference checks and five deferred
design questions. Do not silently expand the project into a full implementation
or claim those blockers are solved by the rename. Any work required to support
new normative claims must be included before those claims are accepted.

Update visual-guide narratives, diagrams, examples, counts, identifiers and
comparisons against the accepted specification. Maintain an explicit mapping
from guide claims to supporting sections/sources. Check rendered behavior,
navigation, accessibility and deployment resource loading, not just text matches.

Publish successor destinations before or atomically with HTML meta redirects
from both the old landing page and old guide. Include canonical and visible
fallback links. Verify directory and explicit `index.html` forms, supported
query/fragment behavior, deployment base paths and absence of redirect loops.
Do not assume meta refresh preserves every bookmark or equate it with an HTTP
301. Preserve meaningful deep-link destinations where possible and document
any unavoidable changes. Update repository and site navigation and keep an
accessible link to the historical specification. Live publication remains a
separate Operator gate.

## Initial arc roadmap

| Arc | Outcome | Dependencies |
|---|---|---|
| arc01-baseline-and-evidence | Pinned archive/copy manifest; claim/source and migration inventories; inherited-gap dispositions; accepted design and evaluation contract | Current baseline and Operator decisions |
| arc02-generalized-protocol-design | Model/service/composition contracts, evidence semantics and precise 0.3 compatibility/0.4 removal rules | Arc01 evidence and scope |
| arc03-successor-specification-and-tooling | Verified baseline copy, revised source/assembly/examples, build and package routes, deprecation implementation appropriate to delivered artifacts | Accepted Arc02 design; Arc01 preservation contract |
| arc04-visual-guide-and-web-migration | Spec-aligned guide, synchronized publication route, updated navigation and tested HTML redirects | Arc03 accepted content and identifiers |
| arc05-integrated-verification | Cross-artifact agreement, unchanged archive, compatibility evidence, independent review and release-readiness disposition | Arc01–04 accepted results |

Arc01 and its first slice now have complete open sets; later slices and arcs
remain roadmap entries. Agree concrete evaluation cases before authoring the artifacts they will judge. The roadmap
does not defer source accuracy, compatibility or guide design until final review.

## Evaluation and definition of done

The [project ledger](ledger.md) is the acceptance authority for delivered work.
At minimum, use bounded examples for a language model, a non-language model,
same-type and heterogeneous multi-model composition, a composite involving a
non-model engine, and an existing non-model/human service. Demonstrate typed
contract failures and evidence limits as well as successful routes. These cases
exercise protocol expressiveness, not universal empirical model capability.

Compatibility verification must cover legacy-only, new-only and mixed names;
conflicts, unknown names and authorization failures; signature/replay/audit
effects; and observable deprecation notices. Distinguish runnable schema or
tooling tests from specification walkthroughs. Do not claim runtime conformance
without an implementation capable of demonstrating it.

Use Make-backed assembly and package gates and browser checks appropriate to
the resulting implementation. Name exact commands and supported environments
in the relevant slice contracts. Confirm generated-document freshness,
standalone package behavior, guide/source agreement, redirects and predecessor
hash preservation. Retain failed, blocked and unrun checks with dispositions.

## Workflow, open decisions and acceptance

Default Two-Contributor Workflow. Sofie in this chat handles CDC planning with
the Operator; CC is unassigned. No Three-Contributor Workflow or Expedited Mode
is inferred. Implementation begins only through complete slice open sets and
Operator handoff. Independent verification belongs in `cdc-verification.md`
under the canonical per-scale contract; no self-acceptance or bootstrap closure.

Resolve canonical successor namespace and field spellings, alias conflict and
output behavior, notice channels, version negotiation, inherited blocker scope,
guide authoring authority and historical packaging policy before dependent
assignments. The 0.3 support and 0.4 removal schedule is settled, not an open
decision. Revisit the baseline pin if the source changes before intake.

Project closure requires accepted children, composed evidence against every
ledger row, finding dispositions, independent review and the Operator gate.
Publication is separately authorized; a push to `main` can trigger the existing
Pages workflow and must be treated accordingly. No release or runtime-readiness
claim follows merely from completing this planning bootstrap.

## Version History

- 1.1 (2026-10-09): Opened Arc01 and Slice01 at the Operator's request. Bounded
  the first assignment to the preservation baseline and migration inventory;
  retained claim/source verification and design decisions in later slices.
- 1.0 (2026-10-09): Established the CHCD Protocol planning project, historical
  CCDP preservation and copy contract, model-generalization notes, source and
  visual-guide review, web migration roadmap, and Operator-selected legacy-name
  support in 0.3 with deprecation and removal in 0.4.
