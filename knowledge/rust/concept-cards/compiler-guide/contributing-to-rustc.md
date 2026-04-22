---
# === CORE IDENTIFICATION ===
concept: Contributing to the Rust Compiler
slug: contributing-to-rustc

# === CLASSIFICATION ===
category: compiler-development
subcategory: contribution-workflow
tier: foundational

# === PROVENANCE ===
source: "Rust Compiler Dev Guide"
source_slug: compiler-guide
authors: "The Rust Compiler Team"
chapter: "Contribution Procedures"
chapter_number: 4
pdf_page: null
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "contributing to rustc"
  - "rustc PR workflow"
  - "compiler team procedures"
  - "r+ review"
  - "@bors merge"
  - "@rustbot"
  - "RFC process"
  - "feature stabilization"
  - "MCP (Major Change Proposal)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - compiler-guide-overview
  - building-rustc
extends: []
related:
  - compiler-testing
  - compiler-debugging
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the workflow for submitting a PR to rustc?"
  - "How does the review process work (r?, @bors r+)?"
  - "What is the RFC process and when is it needed?"
  - "How do new features get stabilized?"
  - "What is a Major Change Proposal (MCP)?"
  - "How is the compiler team organized?"
  - "What is @rustbot and how do I use it?"
  - "How do I use Git effectively for rustc contributions?"
  - "What are the expectations around performance for PRs?"
  - "How do I write documentation for the compiler?"
---

# Quick Definition

Contributing to rustc follows a "fork and pull" model where PRs are filed against the `main` branch, automatically assigned a reviewer by `@rustbot`, tested by CI, approved via `@bors r+`, and merged through a serialized merge queue. The process encompasses bug fixes (straightforward PRs), new features (requiring feature gates and often RFCs), and major changes (requiring MCPs). The compiler team (`t-compiler`) communicates via Zulip, holds weekly triage meetings, and uses a reviewer rotation system for PR assignments. The Rust project follows a strict no-merge-commit policy, requiring rebasing instead.

# Core Definition

## PR Lifecycle

1. **File a PR** against `main` branch (run `./x test tidy --bless` first)
2. **Automatic reviewer assignment** by `@rustbot` (or request specific reviewer with `r? @username`)
3. **CI runs** PR-level checks (~40 minutes: tidy, lints, basic tests)
4. **Review cycle** -- reviewer may request changes (PR gets `S-waiting-on-author`); when done, use `@rustbot ready` to signal review readiness
5. **Approval** via `@bors r+` (or `@bors r+ rollup` for trivial changes)
6. **Merge queue** -- bors runs full test suite on the merge commit (~2 hours)
7. **Merge to main** or failure notification

## Types of Changes

- **Bug fixes / refactoring**: Standard PR process; no special procedures. WIP and Draft PRs are acceptable.
- **New features**: Require feature gates (`#![feature(my_feature)]`), typically preceded by an RFC. Features go through nightly, potentially iterate, then stabilize.
- **Major changes**: Require a Major Change Proposal (MCP), a "relatively lightweight mechanism for getting feedback on large changes to the compiler."
- **Breaking changes**: Have a dedicated procedure involving edition boundaries and compatibility considerations.

## The RFC Process

For substantial new features, the lifecycle is: Pre-RFC (informal discussion on internals.rust-lang.org) -> RFC (formal proposal at rust-lang/rfcs) -> Implementation (behind feature gate) -> Iteration -> Stabilization. An RFC enters Final Comment Period (FCP) with one of three dispositions: merge, close, or postpone. After merge, a tracking issue is created in rust-lang/rust.

## Stabilization

Requires a stabilization report including: brief description of behavior, deviations from RFC, affected editions, and links to tests demonstrating key aspects. A PR removes the feature gate, enabling the feature by default.

## Team Organization

The compiler team (`t-compiler`) holds weekly triage meetings on Zulip (Thursdays at 10am Boston time), covering: announcements, MCP/FCP status, working group check-ins, beta/stable nominations, P-critical/P-high bug review, `S-waiting-on-t-compiler` issues, and performance triage.

Team membership is offered after significant sustained contributions and carries review obligations. Contributors first receive `r+` rights (ability to approve PRs via bors), then may join the reviewer rotation.

# Prerequisites

- Familiarity with Git (rebase workflows specifically)
- Understanding of the build system (see building-rustc)
- A fork of `rust-lang/rust`
- Understanding of the test infrastructure (see compiler-testing)

# Key Properties

1. **No merge commits allowed**: Rust uses a "rebase workflow"; use `git config merge.ff only` to enforce locally. "Merge commits in PRs are not accepted."
2. **@rustbot enables non-member actions**: Claiming issues (`@rustbot claim`), relabeling (`@rustbot label +S-waiting-on-review -S-waiting-on-author`), and shortcuts (`@rustbot ready`)
3. **r? assigns specific reviewers**: Add `r? @username` to PR description or comments; use `r? rust-lang/groupname` for team-based assignment
4. **Performance tracking is systematic**: PRs can trigger perf runs; results appear on perf.rust-lang.org showing comparison against `main`
5. **CI is encouraged for testing**: "You should never have to worry about wasting computational resources each time you push a change." Running full `./x test` locally is not recommended.
6. **Revert policy exists**: PRs causing miscompilations or significant regressions may be reverted. For complex reverts, the problematic code can be disabled for specific inputs instead.
7. **Closing keywords in PR description, not commits**: Use "closes #123" in PR description, not commit messages, to avoid spamming the issue during rebases. Exception: do not use closing keywords for backport PRs.
8. **Update branches only when needed**: "Avoid updating an already-green PR under review unless necessary." Rebase only for merge conflicts, broken upstream CI, or reviewer request.
9. **`git range-diff` for reviewing rebased changes**: `git range-diff main @{upstream} HEAD` shows a "diff of diffs" comparing old and new versions of a branch
10. **Git submodules are pinned dependencies**: The `rust-lang/rust` repo uses submodules for llvm-project, cargo, stdarch, backtrace, etc. Run `git submodule update` when submodules show as modified.

# Construction / Recognition

## Standard Contribution Workflow:

```bash
git checkout main
git pull upstream main --ff-only
git checkout -b issue-12345-fix
# make changes, test them
git add src/changed/file.rs          # avoid git add .
git commit
git push --set-upstream origin issue-12345-fix
# open PR on GitHub
```

## After Review Feedback:

```bash
git checkout issue-12345-fix
# make changes
git add specific-files
git commit
git push
```

## Requesting Review:

In PR description or comment:
```
r? @reviewer-name
```
Or for team-based assignment:
```
r? rust-lang/diagnostics
```

## Using @rustbot:

```
@rustbot claim              # assign issue to yourself
@rustbot release-assignment # unassign yourself
@rustbot ready              # mark PR as ready for review
@rustbot label -S-waiting-on-author +S-waiting-on-review
```

## Writing a Stabilization Report:

Include:
- Brief description of the behavior and any deviations from the RFC
- Which edition(s) are affected and how
- Links to a few tests showing the interesting aspects

Then submit a PR removing the feature gate.

# Context & Application

- **First-time contributors**: Bug fixes and diagnostic improvements follow the standard PR process
- **Feature implementers**: New language/compiler features need feature gates, often an RFC, and eventually stabilization
- **Reviewers**: Guidelines emphasize politeness, r+ only when confident, and awareness of reviewer rotation load
- **Documentation contributors**: Contributions to the rustc-dev-guide are welcome at the separate `rustc-dev-guide` repo
- **Process designers**: MCPs and RFCs shape compiler direction through community consensus

# Examples

**Example 1**: A typical contribution walkthrough -- the guide walks through the `?` Kleene operator for macros as a complete example:
1. Pre-RFC discussion on internals.rust-lang.org
2. Formal RFC at rust-lang/rfcs
3. Implementation behind `#![feature(macro_at_most_once_rep)]`
4. Multiple iterations refining the feature
5. Stabilization with an FCP and stabilization report
6. Feature gate removal, release notes entry

**Example 2**: Triggering a performance benchmark:
```
@bors try @rust-timer queue
```
This creates a try build and queues it for benchmarking on perf.rust-lang.org.

**Example 3**: Squashing commits via bors:
```
@bors squash msg="Improve diagnostics for missing lifetime parameter"
```

**Example 4**: Checking for rebase accuracy with `git range-diff`:
```bash
git range-diff main @{u} HEAD
```
Shows a "diff of diffs" -- a `-` or `+` on the left indicates change between old and new branch; markers on the right show committed changes.

**Example 5**: Handling submodule accidents after rebase:
```bash
git log --stat -n1 src/tools/cargo    # find the accidental commit
git checkout <commit>~ src/tools/cargo  # revert to previous submodule state
git commit --fixup <commit>           # create fixup commit
git rebase --autosquash -i upstream/main  # squash into original
```

# Relationships

## Builds Upon
- **compiler-guide-overview** -- understanding where to ask questions and find work
- **building-rustc** -- knowing how to build and test changes

## Enables
- All compiler contributions flow through these procedures

## Related
- **compiler-testing** -- every PR needs appropriate tests
- **compiler-debugging** -- investigating bugs before fixing them

## Contrasts With
- None within this source

# Common Errors

- **Error**: Creating merge commits when updating a branch.
  **Correction**: Use `git pull --rebase` or `git rebase upstream/main`. Set `git config pull.ff only` or `git config merge.ff only` to prevent accidental merges.

- **Error**: Using `git add .` which can stage submodule changes.
  **Correction**: "Avoid `git add .`, as it makes it too easy to unintentionally commit changes that should not be committed, such as submodule updates."

- **Error**: Following git's advice to `git pull` when `git push` is rejected.
  **Correction**: "The advice this gives is incorrect!" because of the no-merge policy. Use `git push --force-with-lease` instead.

- **Error**: Opening a PR without running tidy.
  **Correction**: "CI will automatically fail your build if it doesn't pass `tidy`." Run `./x test tidy --bless` before every PR.

# Common Confusions

- **Confusion**: All new features need an RFC.
  **Clarification**: "If you are not proposing a new feature or substantial change to Rust or the ecosystem, you don't need to follow the RFC process." Bug fixes, refactoring, and internal improvements can go directly to implementation.

- **Confusion**: @bors r+ means the reviewer merges the PR.
  **Clarification**: "PRs are never merged by hand." `@bors r+` queues the PR for automated testing and merge through the bors queue.

- **Confusion**: Getting `S-waiting-on-author` means the PR has problems.
  **Clarification**: It often just means the reviewer left comments or requested minor changes. Use `@rustbot ready` after addressing feedback.

- **Confusion**: Reviewer rotation means all reviewers are equally expert.
  **Clarification**: "Not all `t-compiler` members are experts on all parts of `rustc`; it's a pretty large project." If assigned a PR outside your expertise, use `r? @so-and-so` to reassign.

- **Confusion**: Contributing to rustc-dev-guide is separate from compiler work.
  **Clarification**: Contributions to the guide are made at the separate `rustc-dev-guide` repo. The guide recommends semantic line breaks and contextualized information with dates.

# Source Reference

Chapter 4 (1736 lines) covering: Contribution Procedures (bug reports, bug fixes, new features, MCPs, performance, PRs, CI, bors, opening PRs, reverting PRs), Writing Documentation, Issue Triage, About the Compiler Team (discussion, reviewers, meetings, membership, r+ rights, reviewer rotation), Using Git (standard workflow, troubleshooting, rebasing, submodules, range-diff, no-merge policy, tips for reviewers), Mastering @rustbot (issue claiming, relabeling), and Walkthrough of a Typical Contribution (the `?` macro feature end-to-end).

# Verification Notes

- Definition source: Direct content from Chapter 4 contribution documentation
- Key Properties: All items supported by source text with specific commands and procedures
- Confidence rationale: HIGH -- procedural documentation with concrete workflows and examples
- Uncertainties: Bot names, Zulip channel names, and meeting schedules may evolve
- Cross-reference status: Related slugs reference other cards in this compiler-guide extraction set
