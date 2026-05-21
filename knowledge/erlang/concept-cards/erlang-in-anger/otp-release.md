---
concept: OTP Release
slug: otp-release
category: applications-releases
subcategory: code-base-types
tier: intermediate
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "How to Dive into a Code Base"
chapter_number: 1
pdf_page: null
section: "OTP Releases"
extraction_confidence: high
aliases:
  - "Release"
prerequisites:
  - otp-application
extends: []
related:
  - relx-release-assembly
  - project-structure
  - application-start-types
contrasts_with:
  - otp-application
answers_questions:
  - "What is an OTP release?"
  - "When should you use a release?"
  - "How do I dive into an unfamiliar code base?"
---

# Quick Definition

An OTP release is a set of OTP applications packaged in a production-ready manner so that the system boots and shuts down without manual `application:start/2` calls.

# Core Definition

From Chapter 1, section "OTP Releases": "A release is a set of OTP applications packaged in a production-ready manner so it boots and shuts down without needing to manually call `application:start/2` for any app. Compiled releases may contain their own copy of the Erlang virtual machine with more or less libraries than the default distribution, and can be ready to run standalone."

From Chapter 2: "If what you're building is a product that stands on its own and should be deployed by users as-is (or with a little configuration), what you should be building is an OTP release."

# Prerequisites

- `otp-application` — a release is a collection of OTP applications; you must understand applications first.

# Key Properties

1. Bundles multiple OTP applications so they boot in the correct order without manual `application:start/2` calls.
2. May include its own copy of the Erlang VM and can be run standalone.
3. Identified by a `relx.config` file or a `relx` tuple inside `rebar.config`, which lists the top-level applications in the release and packaging options.
4. Other systems may instead use configuration files for `systools` or `reltool`.
5. The discovery process used for individual OTP applications generally applies to releases too.
6. The right thing to build when shipping a deployable product, as opposed to a reusable piece of code.

# Construction / Recognition

To recognize one: look for `relx.config`, a `relx` tuple in `rebar.config`, or `systools`/`reltool` config files. To navigate it: the config lists the top-level applications; explore each as an individual OTP application. The `observer` application reveals individual supervision trees at runtime.

# Context & Application

Releases are the production deployment unit. They are assembled by `relx` (used by both `rebar3` and `erlang.mk`). Many teams that need a release build it as a single umbrella OTP application instead.

# Examples

From Chapter 1, section "OTP Releases": releases are recognized via "a file named `relx.config` or a `relx` tuple in a `rebar.config` file, which will state which top-level applications are part of the release and some options regarding their packaging." Chapter 2 gives a `relx` tuple producing a `demo` release from applications `myapp1, myapp2, ..., recon`.

# Relationships

## Builds Upon
- `otp-application` — a release packages applications.

## Enables
- `relx-release-assembly` — `relx` is the tool that assembles releases.

## Related
- `project-structure` — releases use a nested `apps/` or `lib/` layout.
- `application-start-types` — per-application start strategies are configured for a release.

## Contrasts With
- `otp-application` — an application is reusable code; a release is a deployable product packaging many applications.

# Common Errors

- Building an umbrella OTP application when a proper release is needed, or vice versa — the book's rule: reusable code = application, deployable product = release.

# Common Confusions

- A release is not just a tarball of one application; it is a coordinated bundle of applications with boot ordering, optionally including the VM.

# Source Reference

Chapter 1: How to Dive into a Code Base, Section "OTP Releases" (and Chapter 2). (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 1, section "OTP Releases."
- Confidence rationale: high — explicitly defined.
- Uncertainties: none.
- Cross-reference status: Verified
