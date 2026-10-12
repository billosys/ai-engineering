# Slice01 — Baseline and Migration Inventory

## Goal, state and assignment

Produce the replayable baseline and migration map on which later source review,
CHCD design and copying will depend. This is **evidence-only work** with the
source checkout read-only. It contributes to A01-01, A01-04 and A01-05 in the
[arc ledger](../ledger.md); it does not complete those composition rows.

Status: **open, ready for CC via Operator relay**. Current assignment:
[cc-prompt.md](cc-prompt.md), initial pass. Sofie is CDC; the separate receiving
context is CC. Its identity will be recorded on execution. The Operator's
2026-10-09 request opened this arc/slice; it did not authorize protocol edits
or publication. The [slice ledger](ledger.md) defines the exit criteria.

## Baseline and observed source

Source root: `/Users/oubiwann/lab/billosys/ai-engineering`.
Pinned source revision: `dffa504e851b03b8e4746f1941068e4cc850b612`.
At authoring the source HEAD matched this pin; the only source status entry was
untracked `knowledge/lfe/`, outside scope. Planning HEAD was
`0e0c1d0a6b9f451a9328036b0af035e5405cafa8`; Project12's plans were untracked
working files, so this planning commit does not identify their content.
Record actual plan hashes and source/planning status at execution intake.

Author reconnaissance found 103 tracked `protocols/ccdp/` files; the assembled
document SHA-256 is
`aab693d14819dcb0f85fa2fc064c80083491d0684771f8f2ad77d42d3d0da254`.
These are cross-checks, not manufactured expected outputs. Source drift needs
an explicit disposition, not a silently repinned baseline.

The protocol Makefile defaults to document version 0.2; section 7.3.1 requires
wire `ccdp_version: "1.0"` independently. `json/MANIFEST.md` describes extracted
examples and derived instances, not normative JSON Schemas. The main Makefile
packages a selected subtree, whereas the historical archive covers every
tracked predecessor file. `.github/workflows/pages.yml` publishes `site/`.
The guide HTML embeds a JSON-string template; decoding that template reveals
an extra sentence in the published introduction. Preserve both byte identities
and report the decoded difference; do not choose a winner in this slice.

## Scope and outputs

Inventory the complete tracked predecessor tree at the pin. Search the entire
pinned source repository for CCDP names and CCDP-bearing paths, then classify
external integration surfaces. Include the Pages workflow even though its
contents need not say CCDP. Cover build/package/checker paths, root and docs
navigation, site pages, source and assembled text, JSON examples/notes,
namespaces/envelope fields, guide reference/template content, and historical
mentions. Include unknowns with an owner rather than treating every hit as a
rename target. Record ignored/untracked content under the predecessor separately
as excluded candidates; do not hash large generated caches or inspect unrelated
untracked directories.

Allowed durable outputs, all under this slice's `artifacts/`:

- `baseline-files.jsonl`: per-file identity manifest for the predecessor plus
  discovered external integration files and the Pages workflow.
- `migration-inventory.jsonl`: classified observations and source witnesses.
- `baseline-report.md`: coverage totals, preservation/copy-boundary proposal,
  build/publication map, guide comparison, inherited-gap index and open questions.
- `execution-notes.md`: intake/readback, exact commands, exits, replayable
  inspection snippets, denominators, validation results and start/end status.

CC may update only this slice's ledger evidence/status notes and assignment
disposition, and create its `closing-report.md` when reporting proposed-done.
Do not change criteria, parent plans/ledgers, the issued prompt, source files,
or other projects. Do not create `protocols/chcdp/`, future slice directories,
generated releases, new reusable validators or independent verification records.
No commits or pushes are requested for this assignment; leave the scoped work
for review. Proposed scope changes return to CDC through the Operator.

## Method and verification

The prompt's **Inspection recipe and record shapes** is the binding execution
contract. Use Git-object reads at the pin to distinguish tracked historical
content from working-tree bytes. Reconcile manifest path sets, modes, object
identities, lengths and SHA-256 values against a fresh enumeration. Detect dirty
tracked inputs and source drift; never silently replace preserved evidence.

Use case-insensitive tracked content and path search to establish coverage,
then inspect the contexts needed to classify each distinct surface. Per-file
hit counts and bounded witnesses avoid copying huge encoded guide lines into
the report. Decode template JSON without executing its JavaScript to compare
human-readable content. Reading coverage must distinguish structured census
queries from semantic prose reads.

Each inventory row references manifest paths and pinned line/range or decoded
template locators. Reconcile the whole search population to rows or explicit
exclusions. Preserve the different populations: archive versus package versus
published site. Inventory inherited blockers and `json/FINDINGS.md` identities;
their historical assertions remain unverified until the later review slices.

No source assembly or package build is required: this slice changes neither
protocol nor packaging. `make help` and inspected target definitions establish
routes only. Direct Git/hash/set checks establish preservation and coverage;
they do not verify scientific claims, package behavior or runtime compatibility.
Use the checks in S01-01 through S01-07; no new validation framework is needed.

## Exit and handoff

Return the exact assignment identity, actual source/planning state, all output
paths, per-row evidence with honest strength, failed/blocked/unrun checks and
open questions. The closing report must compare promised versus delivered
scope and bubble findings up to Arc01. CC's completion is proposed-done until
CDC reviews and reproduces it in `cdc-verification.md`. Do not open Slice02.

## Author readiness

CDC completed source reconnaissance and packet review on 2026-10-09. The
read-only method, explicit data shapes, file boundaries and set/hash oracles
resolve execution choices; evidence-dependent conclusions remain open. The
prompt manifest limits prose intake to governing contracts, source entrypoints
and relevant witness sections rather than falsely requiring semantic review of
the entire specification. External research and protocol design are deferred
to their named slices, not dropped. Domain code changes are out of scope.

Applied guidance: project-management `03-planning-top-down.md` (complete open
set and assignment history); engineering-methods `07-implementation-prompt-authoring.md`
(investigation method, record shapes, complete intake and author readiness);
work-verification `01-ledger-discipline.md` (reproducible rows and independent
acceptance); testing `03-validation-gates.md`, Proportionate Proof (direct
Git/hash/context checks rather than a new verification product).

## Assignment history

| Assignment | Date | Predecessor | Reason | Disposition |
|---|---|---|---|---|
| `cc-prompt.md` | 2026-10-09 | None | Initial baseline and migration inventory | Active; prepared for Operator relay; execution not reported |

## Version History

- 1.0 (2026-10-09): Opened the evidence-only baseline/migration slice with a
  pinned source, complete open set, explicit artifact shapes and replay checks.
