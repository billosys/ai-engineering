# Per-Extraction Helper-Script Plan Template

This is a non-executable Markdown planning record for a source-specific helper,
not a script or a claim that one ships with the skill. Use only when inspected
inputs justify automation under the current task. Follow the
[structure](../guides/08-structure-mapping-and-splitting.md),
[media](../guides/07-media-path-normalization.md) and
[validation](../guides/10-validation-and-reports.md) guides.

Historical extraction helpers illustrate assumptions that must remain local:
detecting chapters from repeated abstract headings, guessing author/title text,
truncating names into slugs, adding output headers, rewriting one image syntax,
or assuming a converter output directory and runtime. None is canonical
behavior. Verify each against this source; stop on unmatched or ambiguous
cases instead of emitting plausible filenames, boundaries or asset matches.

## Scope And Inputs

| Field | Value |
| --- | --- |
| Plan ID / manifest / author / date | <values> |
| Source / input and conversion snapshots / intended run | <IDs> |
| Why a helper is needed / requested uses | <observed repetitive work; indexing, reading, review, analysis, optional concept-cards> |
| Operating mode / execution actor | <human-assisted or agent-direct; who can inspect and run> |
| Preserved input paths / identity checks | <exact files and digests or explicit unknowns> |
| Output, report and scratch paths / resolution root | <distinct derived destinations; prior outputs preserved> |
| Tools / versions / invocation plan | <required dependencies and exact arguments; proposed, not executed> |
| Scope exclusions and stop conditions | <unsupported syntax, missing inputs, ambiguous boundary, collision, failed precondition> |

## Transformation Contract

| Concern | Rule to fill and supporting evidence |
| --- | --- |
| Section inventory and boundary rules | <accepted map IDs; exact matches and inspected context; front/back matter and unnumbered sections> |
| Complete containers | <fences, divs, tables, notes and definitions; larger unit or no split when uncertain> |
| Original metadata and generated headers | <preserved titles/labels; generated fields separate; line-offset consequences> |
| Output naming | <persistent ID-to-name map; duplicate, truncation and case collisions; no overwrite> |
| Media rewrite rules | <each original full resource and containing file to final file-relative target; alt/title/attributes retained; nested paths inspected> |
| References and dependencies | <cross-file links, fragments, footnotes, SVG, srcset and unsupported cases> |
| Manual decisions | <explicit source-scoped exceptions with evidence; no silent inferred repair> |

## Dry Run, Apply, And Regenerate

- Dry-run/report mode contract: <enumerated input coverage, proposed spans,
  filenames, old/new targets, unchanged items, unresolved cases and caveats;
  no derived or raw file mutation in dry run>.
- Review criteria before apply: <which observations establish every proposed
  change; report path and actor; unresolved changes withheld>.
- Apply/error behavior: <fresh destination, precondition recheck, bounded writes,
  partial-output labelling and failure report; originals never overwritten>.
- Idempotence/regeneration: <rebuild from preserved inputs; stable map reuse;
  already-normalized references unchanged; compare body bytes/inventories and
  mappings; no repeated prefixes, headers, asset copies or renamed identities>.
- Changed inputs/settings: <new snapshot/run, retained prior evidence, comparison
  and explanation; no promise of untested converter byte identity>.

## Validation And Results To Record

| Check | Planned scope / acceptance condition | Actual result and evidence after execution |
| --- | --- | --- |
| Input preservation / output coverage | <all inputs unchanged; every span accounted for; omissions justified> | <not run until observed> |
| Structure and names | <order, complete boundaries, metadata, no collisions/gaps/overlap> | <not run> |
| Media and dependencies | <resolve from every output; identity/appearance checked separately> | <not run> |
| Locators | <typed original/output mapping; bases and header effects verified> | <not run> |
| Fidelity | <specific risky text/table/code/math/image comparisons and sampling rationale> | <not run> |
| Regeneration and failure paths | <repeat-run comparison; ambiguous/missing input behavior and reports> | <not run> |

Caveat output: <[caveat record](./caveat-record.md) destination, stable IDs,
affected spans, blocked operations and re-entry checks>. Final reporting:
<manifest transformations, checks and per-use [readiness](./validation-readiness.md)>.
If execution is human-assisted, distinguish operator logs from direct checks;
unexecuted plans and unsaved reports remain explicitly unverified.
