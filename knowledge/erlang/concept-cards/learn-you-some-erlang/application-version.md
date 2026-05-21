---
concept: Application Version (vsn)
slug: application-version
category: applications-releases
subcategory: applications
tier: foundational
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "Building Applications the OTP Way"
chapter_number: 19
pdf_page: null
section: "The Application Resource File"
extraction_confidence: high
aliases:
  - "vsn"
  - application version
  - "vsn tuple"
prerequisites:
  - app-file
extends: []
related:
  - app-file
  - release-resource-file
contrasts_with: []
answers_questions:
  - "How do I structure an OTP application?"
---

# Application Version (vsn)

## Quick Definition

The `vsn` field of an application's `.app` file is its version string, used to identify the application — especially by upgrade, downgrade, and release tooling.

## Core Definition

"`{vsn, "1.2.3"}` — This is the version of your application. This string can take any format you want. It's usually a good idea to stick to a scheme of the form *Major.Minor.Patch* ... When you start using tools to help with upgrades and downgrades, this string is used to identify your application's version" (Ch. 19, "The Application Resource File").

## Prerequisites

- **App file** — `vsn` is a field of the `.app` file.

## Key Properties

1. Declared as `{vsn, String}` in the application resource file.
2. The string can take any format, but `Major.Minor.Patch` is recommended.
3. It identifies the application to upgrade/downgrade tooling.
4. Release resource files reference each application's version.
5. It is distinct from the *release* version, which is independent.

## Construction / Recognition

## To Set an Application Version

1. Add `{vsn, "1.0.0"}` to the `.app` file's properties.
2. Follow a `Major.Minor.Patch` scheme for consistency.
3. Bump it when releasing changes so tooling can distinguish versions.

## Context & Application

Both `ppool.app` and `erlcount.app` declare `{vsn, "1.0.0"}`. The release resource file in Chapter 21 lists each application with its version — `{ppool, "1.0.0", permanent}` — and the version numbers can be read at runtime via `application:which_applications()`. Being explicit about versions lets a system "mix and match different libraries from different Erlang versions."

## Examples

**Example 1** (Ch. 19): `ppool.app` declares `{vsn, "1.0.0"}`.

**Example 2** (Ch. 21): `application:which_applications()` reports `{stdlib, "ERTS  CXC 138 10", "1.18.1"}` — the version string in use.

## Relationships

## Builds Upon

- **App file** — `vsn` lives in the `.app` file.

## Related

- **release-resource-file** — Lists each application with its version.

## Common Errors

- **Error**: Never bumping `vsn` across releases.
  **Correction**: Increment it on each release so upgrade/downgrade tooling can distinguish versions.

## Common Confusions

- **Confusion**: Thinking the application version must match the release version.
  **Clarification**: They are independent — a release has its own version, separate from each constituent application's `vsn`.

## Source Reference

Chapter 19: "Building Applications the OTP Way," section "The Application Resource File"; runtime versions in Chapter 21, "Releases with systools."

## Verification Notes

- Definition: Direct quote from "The Application Resource File."
- Key Properties: Adapted from the `vsn` description.
- Confidence: HIGH — explicitly defined.
