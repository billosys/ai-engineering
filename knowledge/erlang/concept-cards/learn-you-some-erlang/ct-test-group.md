---
concept: Common Test Test Group
slug: ct-test-group
category: testing
subcategory: common-test
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Common Test for Uncommon Tests"
chapter_number: 28
pdf_page: null
section: "Test Groups"
extraction_confidence: high
aliases:
  - "test group"
prerequisites:
  - common-test
  - ct-test-suite
  - ct-test-case
related:
  - ct-configuration
contrasts_with: []
answers_questions:
  - "What is a Common Test test group?"
  - "How do I run Common Test cases in parallel or random order?"
---

# Common Test Test Group

## Quick Definition

A Common Test test group hierarchically regroups test cases (and other groups) so they can share setup/teardown and run in parallel, in random order, or repeatedly.

## Core Definition

Common Test test groups allow you to regroup tests hierarchically, including groups nested within other groups. A group has its own initialization and termination functions (`init_per_group/2`, `end_per_group/2`) that wrap its member tests or subgroups, letting you define a common environment for a set of related tests. Groups are declared by a `groups/0` function returning a list of `{GroupName, GroupProperties, GroupMembers}` tuples, and are invoked by placing `{group, GroupName}` in the suite's `all/0` (Chapter 28, "Test Groups").

## Prerequisites

- **Common Test** — Groups are a Common Test organizational feature
- **CT test suite** — Groups are declared in a suite via `groups/0`
- **CT test case** — Groups exist to organize and parameterize test cases

## Key Properties

1. Declared by `groups/0` returning `[{GroupName, GroupProperties, GroupMembers}]`
2. Members may be test case atoms, `{group, Name}` references, or inline group definitions
3. Group setup/teardown is `init_per_group/2` and `end_per_group/2`; these run in a process *distinct* from the test cases
4. Group properties control execution: empty list (sequential), `shuffle` (random order, seed logged), `parallel` (separate processes), `sequence` (stop subsequent tests on failure)
5. Repetition properties: `{repeat, Times}`, `{repeat_until_any_fail, N}`, `{repeat_until_all_fail, N}`, `{repeat_until_any_succeed, N}`, `{repeat_until_all_succeed, N}`; `N`/`Times` may be `forever`
6. Properties can be combined, e.g. `[parallel, {repeat, 9}]`
7. Used via `{group, Name}` entries in `all/0`

## Construction / Recognition

## To Define and Use a Test Group

1. Define `groups() -> [{my_group, [Properties], [member_cases]}].`
2. Export and define `init_per_group/2` and `end_per_group/2` (required for `parallel`, or it is silently ignored)
3. Reference the group in `all/0` as `{group, my_group}`

## Context & Application

Groups solve the problem of many test cases needing similar but not identical setup, and enable parallel or randomized execution that EUnit cannot easily provide. The chapter's `meeting_SUITE` uses a `clients` group with `[parallel, {repeat, 10}]` to provoke a race condition, nested inside a `session` group whose `init_per_group` starts the shared `meeting` process. Because group init runs in a separate process, actors linked to it must be unlinked, and ETS tables need an heir.

## Examples

**Example** (Chapter 28, "The Meeting Room"): `groups() -> [{session, [], [{group, clients}, all_same_owner]}, {clients, [parallel, {repeat, 10}], [carla, mark, dog]}].` with `all() -> [{group, session}].`

## Relationships

## Builds Upon

- **CT test suite** — Groups are declared and invoked from within a suite

## Related

- **CT test case** — The cases a group organizes and parameterizes
- **CT configuration** — `init_per_group/2` receives and may extend the `Config` proplist

## Common Errors

- **Error**: Using the `parallel` property without exporting `init_per_group`/`end_per_group`
  **Correction**: Common Test silently ignores `parallel` if those functions are not exported; export them

- **Error**: Starting linked actors or ETS tables in `init_per_group` without precautions
  **Correction**: Group init runs in a separate process; unlink actors and give ETS tables an heir so they survive

## Common Confusions

- **Confusion**: Assuming `sequence` means tests run in declared order
  **Clarification**: `sequence` means that if a test in the group fails, the remaining tests are skipped — it can be combined with `shuffle`

## Source Reference

Chapter 28: Common Test for Uncommon Tests, section "Test Groups" (subsections "Defining Test Groups," "Test Group Properties," "The Meeting Room").

## Verification Notes

- Definition: Direct adaptation from "Test Groups"
- Key Properties: All explicit in the chapter, including the full property list
- Confidence: HIGH — explicitly defined with extensive examples
- Cross-references: verified against planned cards in this extraction
