---
name: code-review
description: |
  Review proposed changes and pull/merge requests across functions, modules,
  libraries, and system effects, using applicable language guidance and real
  evidence. Use for change-focused assessment and GitHub inline comments;
  use code-auditing for repository-wide audits.
license: MIT
metadata:
  version: "1.0.0"
  hermes:
    tags: [ai-engineering, code-review, pull-requests, systems-analysis, verification]
    category: meta-skills
---

# Code Review

Review whether a proposed change is correct, fits its surrounding system, and
can be operated safely. Follow consequences beyond the diff; keep findings
specific to the change and its affected contracts.

## Start Here

- Load `collaboration-framework` when available and not already active. Reuse
  its posture, evidence discipline, and applicable workflow; do not reread
  loaded material or create planning artifacts solely to perform a PR review.
- Detect the languages and tools in the change and its affected boundaries.
  Load the supported domain skills and relevant guides before judging their
  idioms or anti-patterns. The framework supplies method, not language expertise.
  An unavailable language skill is a disclosed knowledge gap, not a reason to
  skip that language: inspect the source and consult authoritative references.
- Read [Review Method](./guides/01-review-method.md) for scope, analysis at all
  scales, verification, and writing the assessment.
- For GitHub, also read [GitHub Reviews And Inline Comments](./guides/02-github-reviews.md)
  before preparing or publishing a review.

## Working Contract

Pin the reviewed revisions, read every changed file and the relevant surrounding
contracts, and test consequential hypotheses against actual code or substrate.
Distinguish a regression, a newly exposed pre-existing weakness, an intentional
tradeoff, and an unrelated existing defect. No finding quota: a well-supported
approval can be the correct result.

Review is diagnosis-only unless the user also requests fixes. Preserve the
user's checkout and credentials. Use real unit tests, idempotent integration
checks, source inspection, and dry-runs of real recipes. Do not create or rely
on mocks, fake CLIs/services, or substitute implementations as verification
evidence. State what could not be verified and why.

Use short, visually separated review sections and narrowly anchored inline
comments. Explain a concrete trigger, consequence, evidence, and correction;
label non-blocking suggestions and open questions. Publish only within the
user's authorization, then verify what was actually submitted. A request for
review does not itself authorize merging, deploying, or messaging other people.

## Composition

Use `code-auditing` for deeper diagnosis when the requested scope warrants it.
Its [scale guide](../code-auditing/guides/03-scale-aware-auditing.md) and
[finding discipline](../code-auditing/guides/02-findings-and-severity.md) inform
this skill; its whole-repository inventory, report set, and modernization
deliverables are not automatic requirements of a change review.
Load `testing` for consequential verification design and `contribution-style`
when drafting a separate upstream issue. Respect the active framework's
delegation boundaries; the reviewer retains the final correctness judgment.

This framework/operational component ships standalone and inside the
collaboration-framework bundle. Its change record is [version-history.md](./version-history.md).
