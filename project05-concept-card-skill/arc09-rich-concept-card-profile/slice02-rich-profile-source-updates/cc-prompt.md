# CC Prompt: Project05 Arc09 Slice02

You are working in Expedited Mode on Project05:

```text
project05-concept-card-skill
arc09-rich-concept-card-profile
slice02-rich-profile-source-updates
```

## Read First

Read these planning files before editing source:

- `project05-concept-card-skill/project-plan.md`
- `project05-concept-card-skill/ledger.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/arc-plan.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/ledger.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice01-v32-richness-gap-and-design/cdc-verification.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice01-v32-richness-gap-and-design/artifacts/rich-profile-gap-analysis.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice01-v32-richness-gap-and-design/artifacts/rich-profile-design.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice01-v32-richness-gap-and-design/artifacts/implementation-scope.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice01-v32-richness-gap-and-design/artifacts/validation-regression-plan.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice02-rich-profile-source-updates/slice-plan.md`
- `project05-concept-card-skill/arc09-rich-concept-card-profile/slice02-rich-profile-source-updates/ledger.md`

## Goal

Update the live `knowledge/concept-cards` source so real-corpus extraction
defaults to a rich readable card body while preserving the v4 control layer.
Carry forward the good v3.2 sections, but do not restore v3.2's overloaded
confidence/verification semantics or cleanup weaknesses.

## Expected Source Scope

Start from Slice01 `implementation-scope.md`. Expected source surfaces are:

- `knowledge/concept-cards/SKILL.md`
- `knowledge/concept-cards/guides/01-load-contract.md`
- `knowledge/concept-cards/guides/02-operator-workflow.md`
- `knowledge/concept-cards/guides/03-extraction.md`
- `knowledge/concept-cards/guides/04-re-extraction-preservation.md`
- `knowledge/concept-cards/guides/05-evidence-lifecycle.md`
- `knowledge/concept-cards/guides/06-graph-cq.md`
- `knowledge/concept-cards/guides/08-validation-verification.md`
- `knowledge/concept-cards/templates/concept-card.md`
- relevant files under `knowledge/concept-cards/examples/`
- `knowledge/concept-cards/references/structural-validation-candidates.md`
- `knowledge/concept-cards/references/semantic-audit-boundaries.md`
- `knowledge/concept-cards/references/operator-review-gates.md`
- `knowledge/concept-cards/version-history.md`

Read the current `metadata.version` in `knowledge/concept-cards/SKILL.md`
before editing. Assess the correct semver bump under the repository skill
version contract. Do not duplicate skill-version numbers outside `SKILL.md`
metadata and the sibling `version-history.md`.

## Required Source Behavior

The rich concept-card body should include:

- concept boundary;
- quick definition and core definition;
- prerequisites and key properties;
- construction / recognition;
- context and application;
- examples;
- relationships and CQs;
- common errors and common confusions;
- source reference and support map;
- extraction notes and review boundaries.

Every section should be present in the template. If selected source material
does not support a section, the card should say `not applicable`, `not
established in the selected source`, or `unresolved`, with a reason. Generic
filler is not compliance.

Keep these separate from the rich prose body:

- stable identity/revision;
- source and prepared-source provenance;
- claim and source-support records;
- evidence grade and extraction confidence;
- validation and verification states/results;
- reconciliation and preservation records;
- operator review gates;
- memory-admission decisions.

Rich prose can explain or link these controls, but it must not replace or
claim them.

## Required Artifacts

Write these files under:

```text
project05-concept-card-skill/arc09-rich-concept-card-profile/slice02-rich-profile-source-updates/artifacts/
```

- `source-update-summary.md`
- `validation-evidence.md`

The summary should list changed source files, state how the rich profile was
implemented, and identify any intentionally untouched surfaces. The validation
artifact should record commands, results, caveats, and any accepted warnings.

## Boundaries

Do not edit `document-extraction` unless you find a direct blocker and record
the evidence before touching it. Do not regenerate Arc07 cards, process the
full book, perform operator acceptance, independently semantically verify
cards, reconcile/admit memory, build graph/RAG/MCP/runtime infrastructure, or
claim retrieval quality.

Slice03 owns regression proof. Slice04 owns final package inspection and
Arc10 closure inputs.

## Verification

Run the strongest applicable checks, including:

- focused inspection of changed Markdown links and anchors;
- `make check-skills`;
- `make check-skill-versions`;
- `make check-package-paths` if Markdown paths or package contents changed;
- `git diff --check`;
- source and planning `git status --short --untracked-files=all`.

If package contents changed but a full package build is expensive, record the
reason and leave fresh package inspection to Slice04. If any gate fails, fix
and rerun it or record a concrete blocker with re-entry conditions.

## Closing

Update the Slice02 ledger rows, write `closing-report.md`, and commit with
explicit pathspecs so unrelated work is not included. Leave the slice as CC
proposed-done for CDC verification.
