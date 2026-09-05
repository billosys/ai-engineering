# Findings And Severity

Use this guide when writing code-audit reports, classifying findings, or
checking whether an audit result is actionable. It is independently loadable and
preserves the diagnosis-only finding contract from the original audit guide.

For audit setup and source mapping, load
[`01-audit-scope-and-map.md`](./01-audit-scope-and-map.md). For scale coverage,
load [`03-scale-aware-auditing.md`](./03-scale-aware-auditing.md). For
modernization synthesis, load
[`04-modernization-synthesis.md`](./04-modernization-synthesis.md).

## Per-Language Report Structure

Each audited language gets one Markdown report with this structure:

1. **Executive summary** - 3 to 5 sentences. Name what is solid, the dominant
   cluster of issues, and any missing or undiscoverable architecture context.
2. **Audit map for this language** - packages, crates, modules, targets,
   binaries, entrypoints, test trees, generated/vendored exclusions, and
   cross-language boundaries reviewed. Mark inferred boundaries explicitly.
3. **Scale coverage** - a short paragraph or checklist covering line/function,
   file/module, logical unit, package/crate/target, app/service/executable,
   whole codebase, and workspace/monorepo where present.
4. **Findings** - grouped by category, highest severity first.
5. **Coherence observations** - patterns that are not single defects but affect
   maintainability at scale.
6. **Cross-cutting findings**, when present.
7. **Things I looked for and did not find** - at least five clean checks.

## Finding Categories

Use these categories where they apply. Do not invent categories just to make a
report look fuller.

- Correctness / soundness
- Architecture and coherence
- API design and invariants
- Error handling
- Concurrency and runtime safety
- Testing
- Performance
- Idioms and style
- Modernization

## Finding Shape

Every finding uses this shape:

- **ID** - stable within the report, such as `RUST-001`, `CPP-004`, or
  `JS-002`. Use the same ID in the index, cross-references, and modernization
  synthesis.
- **Severity** - one of Blocker, High, Medium, Low.
- **Location** - `path/to/file.ext:LINE`, or `:LINE-LINE` for a range. Every
  finding cites at least one specific file and line. For scale findings, cite a
  boundary-defining file or documented contract plus representative file:line
  evidence.
- **Scale** - line/function, file/module, logical unit, package/crate/target,
  app/service/executable, whole codebase, or workspace/monorepo.
- **What's wrong** - one or two sentences.
- **Why it's wrong** - the actual failure mode, not a restatement.
- **Fix** - concrete, applied at the cited location. Include a code snippet
  only when the fix is non-obvious.

## Severity Classes

Severity is a commitment, not a hedge.

- **Blocker:** ships a bug, unsoundness, data loss, security exposure, or
  unrecoverable user-facing failure.
- **High:** correctness risk under realistic operating conditions.
- **Medium:** will bite future maintainers or meaningfully degrade quality,
  reliability, observability, or evolvability.
- **Low:** local style, minor idiom drift, wording, or small maintainability
  improvement without a concrete failure mode.

If two severity levels both seem plausible, write the reasoning in one line and
pick one. Do not use Medium as a place to hide uncertainty.

## Coherence Observations

Coherence is auditable. "These files feel inconsistent" is not a finding. Name
the inconsistent idiom, cite representative lines from each side, explain the
operational or maintenance failure mode, and assign severity if it matters.

Examples of coherence issues:

- Mismatched naming systems.
- Duplicated concepts.
- Inconsistent layering.
- Multiple competing abstractions.
- Divergent testing styles.
- Different error, logging, configuration, serialization, or dependency
  direction models in neighboring code.

Promote any observation with a concrete failure mode to a severity-graded
finding.

## Cross-Cutting Findings

When a bug's root cause is in one language but its effect lands in another
language, file the finding in the report for the language where the root cause
lives. Leave a one-line cross-reference in the other report or reports that
points back to the root-cause finding.

Cross-cutting examples include FFI boundaries, IPC protocols, shared schemas,
generated clients, command contracts, and serialized data formats.

## Negative Findings

Every per-language report includes at least five checks that came back clean.
This prevents filler findings and makes real negative evidence visible.

Good negative findings name the concrete check:

- "Searched for `.unwrap()` in public Rust library paths; no caller-reachable
  instances found."
- "Checked all CLI exit paths for stderr/status consistency; no divergence
  found."

Bad negative findings are generic:

- "No major problems found."
- "Tests look good."
