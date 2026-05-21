---
concept: Project Structure (App vs Release Layout)
slug: project-structure
category: applications-releases
subcategory: project-layout
tier: foundational
source: "Stuff Goes Bad: Erlang in Anger"
source_slug: erlang-in-anger
authors: "Fred Hébert"
chapter: "Building Open Source Erlang Software"
chapter_number: 2
pdf_page: null
section: "Project Structure"
extraction_confidence: high
aliases:
  - "Directory layout"
prerequisites:
  - otp-application
  - otp-release
extends: []
related:
  - rebar3
  - relx-release-assembly
contrasts_with: []
answers_questions:
  - "What are the main differences between the directory structure of an app and a release?"
  - "How do I build a release with rebar3?"
---

# Quick Definition

OTP applications and OTP releases use different directory layouts: an application keeps a single top-level app in `src/`, while a release nests multiple applications under an `apps/` (or `lib/`) directory.

# Core Definition

From Chapter 2, section "Project Structure": "The structures of OTP applications and of OTP releases are different. An OTP application can be expected to have one top-level supervisor (if any) and possibly a bunch of dependencies that sit below it. An OTP release will usually be composed of multiple OTP applications."

An OTP application layout (with `rebar3`):

```text
_build/
doc/
src/
test/
LICENSE.txt
README.md
rebar.config
rebar.lock
```

An OTP release layout nests applications one level deeper:

```text
_build/
apps/
  - myapp1/
     - src/
  - myapp2/
     - src/
doc/
LICENSE.txt
README.md
rebar.config
rebar.lock
```

# Prerequisites

- `otp-application` — one of the two layout types.
- `otp-release` — the other layout type.

# Key Properties

1. Application layout: a single app, with code directly under `src/`.
2. Release layout: multiple apps nested under `apps/` (or `lib/`), each with its own `src/`.
3. Both layouts share `_build/` and `rebar.lock`, which `rebar3` generates automatically.
4. `_build/` holds all build artifacts, including project-local copies of dependencies.
5. The release layout "lends itself to generating releases where multiple OTP applications under your control [live] under a single code repository."

# Construction / Recognition

To recognize: a `src/` directory at the project root means an application; an `apps/` or `lib/` directory containing multiple sub-applications means a release. To build a release from the nested layout, add a `relx` tuple to `rebar.config` and run `rebar3 release`.

# Context & Application

Choosing the layout follows from what you are building: a reusable application uses the flat layout; a deployable product composed of several of your own applications uses the nested release layout.

# Examples

From Chapter 2, section "Project Structure": the flat app layout and the nested `apps/myapp1`, `apps/myapp2` release layout are both shown verbatim, with the note that the nested form supports "multiple OTP applications under your control under a single code repository."

# Relationships

## Builds Upon
- `otp-application`, `otp-release` — the two things being laid out.

## Enables
- `relx-release-assembly` — the nested layout feeds `relx`.

## Related
- `rebar3` — the tool that generates `_build/` and `rebar.lock`.

## Contrasts With
Nothing directly — the app layout contrasts with the release layout.

# Common Errors

- Shipping the `_build/` directory with public source code — Chapter 2 says to distribute *without* it.

# Common Confusions

- `apps/` and `lib/` are interchangeable names for the nested-applications directory; using one over the other does not change behaviour.
- An umbrella application is still a single application even though it may look release-like; the defining trait is whether multiple distinct applications are nested.

# Source Reference

Chapter 2: Building Open Source Erlang Software, Section "Project Structure". (No PDF pages — this source has none.)

# Verification Notes

- Definition source: quoted from Chapter 2, section "Project Structure."
- Confidence rationale: high — both layouts shown verbatim.
- Uncertainties: none.
- Cross-reference status: Verified
