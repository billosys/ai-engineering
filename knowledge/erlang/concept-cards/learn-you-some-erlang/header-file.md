---
concept: Header File
slug: header-file
category: data-types
subcategory: code-organization
tier: intermediate
source: "Learn You Some Erlang for Great Good!"
source_slug: learn-you-some-erlang
authors: "Fred Hébert"
chapter: "A Short Visit to Common Data Structures"
chapter_number: 9
pdf_page: null
section: "Sharing Records"
extraction_confidence: high
aliases:
  - ".hrl file"
  - "hrl file"
  - "include file"
prerequisites:
  - record
extends: []
related:
  - record
contrasts_with: []
answers_questions:
  - "What is an Erlang header file?"
  - "How do I share record definitions across modules?"
---

# Header File

## Quick Definition

An Erlang header file (`.hrl`) is a snippet of code — typically record and macro definitions — that is textually inserted into a module by the `-include` directive, as if written there directly.

## Core Definition

Because records are useful and code duplication is annoying, "Erlang programmers frequently share records across modules with the help of header files. Erlang *header files* are similar to their C counterparts. A header file is nothing but a snippet of code that gets added to the module as if it were written there in the first place." A `.hrl` file is created with content such as a `-record` definition and is pulled into a module with `-include("records.hrl").`. The chapter warns, however, that while a project-wide `.hrl` of shared records is common in open-source software, the author "strongly recommends" keeping record definitions local to one module and exposing accessor functions — this prevents name clashes and code-upgrade problems and improves maintainability (Hébert, ch. 9, "Sharing Records").

## Prerequisites

- **Record** — Header files most often carry record definitions to be shared

## Key Properties

1. A header file has the `.hrl` extension
2. It is a code snippet inserted into a module as if written inline
3. Pulled in with the `-include("file.hrl").` directive
4. Commonly holds record and macro definitions to share across modules
5. Public `.hrl` files often live in an `include/` directory; private ones in `src/`
6. The author recommends keeping records local rather than sharing them via project-wide headers

## Construction / Recognition

## To Use a Header File

1. Create a file with a `.hrl` extension containing definitions (e.g. `-record(included, {...}).`)
2. In a module, add `-include("records.hrl").`
3. Use the included definitions as if they were declared in the module
4. Place shared headers in `include/`, private ones alongside `src/`

## Examples

> **Header content** (ch. 9): `records.hrl` containing `-record(included, {some_field, some_default = "yeah!", unimaginative_name}).`
>
> **Inclusion** (ch. 9): `-include("records.hrl").` then `included() -> #included{some_field="Some value"}.`

## Relationships

## Related

- **Record** — Header files are most commonly used to share record definitions

## Common Errors

- **Error**: Putting every project record in one shared `.hrl` and editing it freely
  **Correction**: The author recommends local record definitions plus accessor functions to avoid clashes and upgrade problems

## Common Confusions

- **Confusion**: Thinking `-include` links modules at runtime
  **Clarification**: `-include` is purely textual inclusion at compile time, like a C `#include`

## Source Reference

Chapter 9, "A Short Visit to Common Data Structures," section "Records," subsection "Sharing Records."

## Verification Notes

- Definition and `-include`: directly from ch. 9
- Confidence: HIGH — explicitly described with an example
