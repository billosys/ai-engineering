---
concept: Included Application
slug: included-application
category: applications-releases
subcategory: applications
tier: advanced
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "The Count of Applications"
chapter_number: 20
pdf_page: null
section: "Included Applications"
extraction_confidence: high
aliases:
  - included app
prerequisites:
  - otp-application
  - application-dependency
extends: []
related:
  - application-dependency
  - erlang-release
contrasts_with:
  - application-dependency
answers_questions:
  - "How does an OTP application relate to a release?"
  - "What is an OTP application?"
---

# Included Application

## Quick Definition

An included application is an application defined as part of another application, started by its parent rather than independently. The book recommends *against* using them.

## Core Definition

"The basic idea of an included application is that you define an application (in this case `ppool`) as an application that is part of another one (`erlcount` here)" (Ch. 20, "Included Applications"). Using one requires modifying both application files and adding *start phases* that follow a protocol described in the Erlang documentation.

## Prerequisites

- **OTP application** — Both the included and the including app are OTP applications.
- **Application dependency** — Included applications are an alternative to plain dependencies.

## Key Properties

1. The included application is started by its parent application, not on its own.
2. Setting one up requires changes to *both* application files and the addition of *start phases*.
3. It seriously limits code reuse: an included application can no longer be included in any other application on the VM.
4. If the parent application dies, the included application is taken down with it.
5. It is "more and more recommended *not* to use included applications."
6. Releases provide the same coordination "in a more generic manner."

## Construction / Recognition

## To Recognise When (Not) to Use Them

1. If you need one application started in lockstep with another → an included application is one option.
2. But prefer plain dependencies (`applications` tuple) and releases instead.
3. Avoid included applications when the inner application should be reusable by other applications.

## Context & Application

The book explains the downside concretely: `ppool` was carefully designed so "anyone can use it, get their own pool." Making it an included application of `erlcount` would mean "it can no longer be included in any other application on this VM. Also, if `erlcount` dies, then `ppool` will be taken down with it, ruining the work of any third-party application that wanted to use `ppool`." For these reasons "included applications are usually excluded from many Erlang programmers' toolbox."

## Examples

**Example 1** (Ch. 20): Making `ppool` an included application of `erlcount` is presented and then rejected, because it would prevent any other application from reusing `ppool`.

## Relationships

## Builds Upon

- **OTP application** — An included application is an OTP application embedded in another.

## Related

- **application-dependency** — The recommended alternative.
- **erlang-release** — Provides the same coordination more generically.

## Contrasts With

- **application-dependency** — A dependency stays a separate, reusable, independently-started application; an included application is bound to and started by its parent and cannot be reused elsewhere.

## Common Errors

- **Error**: Making a reusable library/service into an included application.
  **Correction**: Keep it a standalone application and depend on it; use a release to coordinate startup.

## Common Confusions

- **Confusion**: Thinking included applications are the standard way to compose applications.
  **Clarification**: They are largely discouraged; plain dependencies plus releases are the recommended approach.

## Source Reference

Chapter 20: "The Count of Applications," section "Included Applications."

## Verification Notes

- Definition: Direct quotes from "Included Applications."
- Key Properties: Adapted from the section's cost/benefit discussion.
- Confidence: HIGH — explicitly defined, including the recommendation against use.
