# CC Proposed-Done Closing Report: Arc01 Slice01

Status: revised proposed-done by CC only. All ledger evidence is `attested`;
independent CDC reproduction is pending. Per operator instruction on 2026-09-12,
this close packet is intentionally uncommitted.

## Scope and outcome

Delivered the assigned historical/current inventory, preserved ignored
CompCogNeuro workbench evidence, field/capability crosswalk and Slice02 research
agenda. No schema was selected, no extraction was run, no source skill/version,
historical prompt, card corpus or other project was edited.

## Validation

See `artifacts/validation-evidence.md`. The key reproducible observations are:

- source `main` was `e763c661`; planning was `03c5b207` before work;
- Fennel/YAML::XS parsed 2,106 of 2,124 registered Markdown files;
- the legacy population is 2,054 cards (390 Complete Musician, 1,664 Erlang);
- three rich rerun cards have invalid YAML from colon-bearing unquoted titles;
- the two preserved workbench trees are byte-identical across 27 files.

Final rerun: the helper output was byte-identical to the checked-in raw
inventory; checksum comparison passed; `git -C .worktrees/planning diff --check`
passed; and the declared artifact text had no trailing whitespace. The source
checkout remained clean. The planning checkout contains only this slice's
uncommitted ledger/report/artifact changes.

## Ledger row walk

| Row | CC disposition | Evidence |
| --- | --- | --- |
| S1-1 | done, attested | `artifacts/input-register.md` |
| S1-2 | done, attested | `artifacts/baseline-snapshots/{source,copy}-sha256sums.txt` |
| S1-3 | done, attested | `artifacts/frontmatter-inventory.json`, helper, inventory report |
| S1-4 | done, attested | `artifacts/capability-crosswalk.md` |
| S1-5 | done, attested | crosswalk, planning brief and representative body observations |
| S1-6 | done, attested | `artifacts/research-agenda.md` |
| S1-7 | done, attested | validation report, this report and final diff/status checks |

## Artifact inventory

- `artifacts/input-register.md`
- `artifacts/metadata-inventory.md`
- `artifacts/capability-crosswalk.md`
- `artifacts/research-agenda.md`
- `artifacts/validation-evidence.md`
- `artifacts/inventory_frontmatter.rb` and `artifacts/frontmatter-inventory.json`
- `artifacts/baseline-snapshots/` with two path-mapped source trees and two
  SHA-256 manifests (27 files in each mapped tree)

## Findings and limits

F-01: current typed records make richer evidence/provenance representation
possible but the inspected output does not demonstrate an equivalent practical
projection for legacy traversal/CQ lookup. F-02: three rich baseline cards are
not YAML-parseable. F-03: legacy field absence, empty lists and nulls are all
observed and cannot be normalized into one state. F-04 revised: the cited local
CompCogNeuro source snapshot is currently present, clean and pinned as recorded
in `input-register.md`; direct source-support checking remains outside this slice.

## Iteration 01 corrections

R1: replaced the Ruby helper with `artifacts/inventory-frontmatter.fnl`, whose
Fennel reporting logic uses a documented local YAML::XS parser bridge. The Ruby
file is removed; fixtures cover null/empty/nested/malformed/non-mapping/
unterminated/missing-root behavior. R2: added `field-dispositions.json` with
169/169 top-level and 307 observed field paths. R3: corrected typed population
to 52 records/31 cards, Arc07 to ten cards/four supports, Erlang subset to 224,
and baseline count to 27 total. R4: added commands, versions and exact inputs.
R5: refreshed the source snapshot availability without claiming semantic review.

New artifacts: `inventory-frontmatter.fnl`, `inventory-fixtures/` and
`field-dispositions.json`; `inventory_frontmatter.rb` was removed. No files
were staged or committed.

## Bubble-up to Arc01

This slice delivered the arc's assigned inventory/research-question input.
Slice02's existing scope already covers every surfaced need: primary-source
research for classification, identity/locators, typed relations/provenance and
CQ requirements. The research agenda adds concrete fixtures for YAML parse
failures, graph traversal and lifecycle scope, but does not require a changed
slice order or a new Arc01 slice. Therefore no `arc-plan.md` change is proposed.

Scope-as-specified versus delivered: all five named reports, baseline copies,
ledger update and this proposed-done report are present. The optional small
helper and raw inventory are declared above. No listed item was deferred or
dropped. CDC verification, architecture, implementation and extraction are
explicitly outside this slice and remain open.

## Independent verification pending

CDC should rerun the helper and field-union counts, compare both baseline
manifests, inspect every crosswalk disposition against representative evidence,
check `git diff --check` and worktree hygiene, then write `cdc-verification.md`.
This report does not close the slice, arc or project.
