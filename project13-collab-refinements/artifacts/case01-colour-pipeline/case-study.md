# Case01 — Repeated correction of nonlinear colour-pipeline evidence

## Question, boundary and result

Why did Project10 Arc02/Slice02 need repeated corrections, and what might reduce
avoidable rework without weakening its acceptance standard?

This retrospective covers the initial assignment and Iterations01–03, their
committed returns and CDC reviews. The cutoff is planning review `9a30f480`.
Four CC returns had been reviewed; the slice was still open, with four of nine
criteria accepted. Three corrections had completed and Iteration04 was issued.
This is a right-censored observation: **four returns is not time to closure**.
Later/in-flight work is excluded. The source pin is `dffa504e` throughout.

Main interpretation: preparation was much more concrete for the mathematics
than for the semantic review. Repeated execution failures, incremental reviewer
checks and growing record-maintenance work compounded that imbalance. These
are plausible contributing mechanisms, not experimentally isolated causes.
The study author is also the CDC whose decisions are being examined.

## Preserved evidence and reproduction

The [manifest](evidence-manifest.json) gives each copy's original repository path,
full revision, Git blob, SHA-256, bytes and line count. Fifty byte-identical files
are under `evidence/`: each stage's issued prompt/plan, seven returned outputs,
and subsequent cumulative CDC review, plus relevant source/method/plan context.
[Baseline measures](baseline-measures.json) contain the observations below.
The [capture self-check](capture-check.md) records integrity checks and a minimal
archive replay command.

Copies are research data, never live assignments. Their embedded relative links
retain original bytes and may not resolve in this archival layout; use the
manifest's original revision/path to follow them. Study-authored links point to
actual copies. Do not repair historical links or replay embedded code merely by
opening this archive. Git bytes, not the concurrently edited working tree, were
used. Current CC work and unrelated files were neither copied nor changed.

To reproduce a copy, obtain `git show REVISION:REPOSITORY_PATH` from the shared
repository, compare its bytes with `copy_path` under this directory, and verify
SHA-256/byte/line counts against the manifest. Original paths may contain spaces;
use subprocess argument arrays or proper shell quoting. Report identities and
command failures honestly. Copy comparison is a new integrity check; it is not
a fresh replay of the historical mathematical or semantic review.

## Observed sequence

| Return | Prompt words | JSONL rows / assessed rows | Notes bytes | CDC accepted criteria |
|---|---:|---:|---:|---:|
| Initial | 1,411 | 18 / 18 | 12,366 | 2/9 |
| Iteration01 | 2,064 | 60 / 42 | 32,985 | 3/9 |
| Iteration02 | 2,011 | 70 / 49 | 61,951 | 3/9 |
| Iteration03 | 1,892 | 71 / 50 | 475,086 | 4/9 |

Counts have different meanings: later JSONL populations include lineage envelopes,
boundaries and a duplicate link. Eighteen broad initial records are not fifty
comparable atomic assessments. Criteria have unequal difficulty; 4/9 is not a
percentage of project completion. Words count whitespace-delimited tokens, not
model tokens. Total effort and exact omitted-claim counts were not reconstructed.

### Initial assignment and return

The [initial plan](evidence/initial/slice-plan.md), especially Binding model and
scope distinctions and Case protocol and discriminating oracles, supplies actual
coefficient generations, input spaces, transfer branches, fixed cases, numerical
tolerances and author-reproduced witnesses. Its Results section instead adapts
an inherited generic five-dimension record shape, without a complete local
worked record demonstrating all distinctions together.

The [initial return](evidence/initial/closing-report.md) reports the core numerical
results and 18 claim records. The [initial CDC review](evidence/initial/cdc-verification.md),
F01–F05, establishes correct numerical results but missing intermediate tables
and recoverable code. All 18 dimension objects were identical across records;
correctness said supported-with-scope even for the matrix-collapse assertion
contradicted by the proof. Missing clauses, editor instructions in place of
replacement text, and incomplete read/replay receipts also remained.

### Iteration01

The [prompt](evidence/iteration01/cc-prompt-iteration01.md), F01–F04, names omissions,
contrasts the false whole-conversion matrix claim with a true nonlinear claim,
requires exact original propositions and recoverable evidence, and forbids C&B
retention. It requires actual replacement sentences and checks of printed stages.
The [return](evidence/iteration01/closing-report.md), Iteration01 section, describes
42 assessments and six controls. The [review](evidence/iteration01/cdc-verification.md),
Iteration01 F01–F05, accepts all stage values but finds substituted propositions,
a nonexistent method path, residual C&B text, editor commands, and incomplete
checker field coverage. Explicit instructions were therefore missed; prompt
vagueness alone cannot explain this return.

### Iteration02

The [prompt](evidence/iteration02/cc-prompt-iteration02.md), F01, explicitly names
line 97's exact-inverse qualifier. F02 again distinguishes original assertions
from corrections and introduces potentially misleading musical comparison
framing. F03 requires every printed original and staged field to be checked.
The [return](evidence/iteration02/closing-report.md) reports 70 records and broad
replay coverage. The [review](evidence/iteration02/cdc-verification.md), Iteration02
F01–F05, finds the named qualifier still absent, nine reasons assessing replacement
conditions, ten split consistency reasons without real comparisons, and ignored
RGB intermediate fields. Handoff verdict labels also disagree with claim results.

### Iteration03

The [prompt](evidence/iteration03/cc-prompt-iteration03.md) gives still more explicit
clause, evidence and RGB-stage repairs. The [return](evidence/iteration03/closing-report.md)
reports 50 assessed records and 128 RGB vector comparisons. The
[review](evidence/iteration03/cdc-verification.md), Iteration03 residual F01–F04,
accepts the repaired numerical coverage but finds repeated generic consistency
reasons, an invalid comparison between distinct musical analogies, confusion
between historical verification and this slice's new check, and five broken
fragments introduced as purported repairs. Its CDC clarification explicitly
withdraws the earlier review's implication about the musical passages.

## Findings and causal hypotheses

### C01 — Uneven author preparation

**Observation:** The numerical recipe had concrete cases and contrary controls;
core values were correct in the first return. Semantic results initially reused
identical verdict objects. See initial plan and review above, and the
[inherited method](evidence/context/review-procedure.md).

**Hypothesis:** A source-grounded worked assessment would have exposed the most
important interpretation errors before bulk record production. A generic shape
and principles did not sufficiently demonstrate their interaction. This is a
failure to apply the existing [prompt-authoring guidance](evidence/context/source/knowledge/engineering-methods/guides/07-implementation-prompt-authoring.md),
Investigation and semantic evidence assignments, rather than proof that another
framework layer is required. Mathematics and semantic judgment also differ in
intrinsic difficulty, so their outcomes do not isolate prompt quality alone.

### C02 — Unstable assertion inventory and incomplete context

**Observation:** The initial foundations range ended at 455; its paragraph ends
at 456. Inspect the [source copy](evidence/context/source/knowledge/design/guides/foundations-of-design.md),
lines 451–456. Later omissions include the explicitly assigned line-97 qualifier.
Clause splitting contributed to population growth; growth itself is not a defect.

**Hypothesis:** Inventorying complete propositions and qualifiers before assigning
verdicts would reduce late discovery and unnecessary remapping. CDC missed an
initial context boundary; CC later missed an expressly named requirement.

### C03 — Repeated failure types received broader correction lists

**Observation:** Iterations01–03 repeatedly require assessment of the original
proposition and actual consistency witnesses. Corrected wording is nevertheless
used to justify originals; splitting a record is treated as consistency evidence.
Iteration03's CARD-003-LINEARITY cites only its own subject for consistency.

**Hypothesis:** The repair process addressed examples without first demonstrating
that the underlying interpretation method had changed. After recurrence, a small
end-to-end repair pilot would be more informative than another wholesale pass.
This does not excuse ignoring explicit requirements.

### C04 — Verification coverage was discovered incrementally

**Observation:** Correct tables coexisted with checkers that ignored fields or
accepted corrupted values. Iteration01 review identifies XYZ/polar gaps;
Iteration02 review identifies RGB intermediate gaps; Iteration03 resolves those.
Historical PASS claims exceeded the properties actually checked.

**Hypothesis:** A case/field-to-predicate inventory and discriminating mutations
per field family would expose omissions together. Mechanical existence/hash checks
cannot establish semantic applicability. CDC also should have audited checker
coverage comprehensively earlier, rather than finding gaps in successive passes.

### C05 — Reviewer framing introduced rework

**Observation:** Iteration02 F02 suggests foundations 438–444 versus 451–456 as
analogous/conflicting context. The passages concern different propositions:
temperament/uniformity versus harmony/frequency ratios. Iteration03 review
withdraws the implication that differing strength labels establish conflict.

**Hypothesis:** Insufficiently checked reviewer examples can propagate a mistaken
answer as an apparent requirement. State comparison targets and uncertainty;
permit supported disagreement. CDC owns this contributing error.

### C06 — Evidence administration grew and sometimes tightened

**Observation:** Notes grew from 12,366 to 475,086 bytes; Iteration03 embeds the
full 70-record predecessor projection. Multiple historical checker blocks and
receipts remain. Iteration01 allows recoverable revision **or blob identity**;
later reviews require extra explicit revision/receipt metadata. Five previously
correct links were changed to incorrect fragments in Iteration03.

**Hypothesis:** Repeated transcription and accumulated historical payload increase
maintenance opportunities and distract from current reasoning. Attention overload
is not directly measured and cannot be asserted as a cause. Some receipt demands
were explicit and missed; some administrative rework arose from CDC tightening.
Prefer concise current records and pinned history, preserving all required reads,
failed attempts and prior evidence without needless inline duplication.

## Alternative explanations and limits

- Missing originals limit fidelity conclusions, but did not prevent this bounded
  mathematics/evidence assignment; acquiring them would not fix these failures.
- The task blends proof, semantic judgment, replacement prose, and evidence tooling.
  Difficulty and task composition can explain some difference from future slices.
- The same CDC authored prompts and diagnosed their weaknesses. Attribution is
  vulnerable to hindsight and self-serving interpretation; include reviewer errors.
- Model/version/settings, complete context exposure, token use and total human/agent
  effort were not established. Do not infer them from signatures or elapsed-time
  summaries. Installed guidance and repeated learning are further confounds.
- Reviews themselves are evidence to challenge, not infallible ground truth.
  No new mathematical replay or full independent semantic audit was done for this study.
- No exact omitted-claim count, atomic defect count, or causal percentage is claimed.
  F01–F05 are bundled findings, not five interchangeable bugs. The endpoint remains open.

## Proposed intervention and decision

Use a few source-grounded worked examples; inventory complete assertions before
verdicts; separate original, judgment and correction; map required observations
to actual checks; inspect all review categories together; change approach when
a failure type recurs; and keep one compact current record with pinned history.

These measures form a **bundle hypothesis**. The [prospective protocol](../experiment01-methodology-pilot/protocol.md)
will test whether the bundle is useful on real upcoming work, record costs and
regressions, and avoid attributing any benefit to an individual component. One
substantive return plus one correction is an aspiration, not a pass threshold,
permission to close early, or demonstrated counterfactual for this case.
