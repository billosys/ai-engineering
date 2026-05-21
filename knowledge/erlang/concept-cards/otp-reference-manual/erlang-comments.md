---
# === CORE IDENTIFICATION ===
concept: Comments
slug: erlang-comments

# === CLASSIFICATION ===
category: core-idioms
subcategory: module-structure
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Modules"
chapter_number: null
pdf_page: null
section: "Comments"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "Erlang comment"
  - "percent comment"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - erlang-module
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I write comments in Erlang?"
  - "What is the comment syntax in Erlang?"
  - "What do the different levels of % mean in Erlang?"
---

# Quick Definition
Comments in Erlang begin with the `%` character and continue to the end of the line. They can be placed anywhere except within strings and quoted atoms, and have no effect on execution.

# Core Definition
The Erlang Reference Manual states: "Comments can be placed anywhere in a module except within strings and quoted atoms. A comment begins with the character `%`, and continues up to but not including the next end of line. A comment has no effect, being essentially equivalent to white space." (Modules, "Comments" section).

# Prerequisites
This is a foundational concept with no prerequisites.

# Key Properties
1. Comments begin with `%` and extend to the end of the line
2. Cannot appear within strings or quoted atoms
3. Treated as whitespace -- no effect on program behavior
4. Erlang has no multi-line comment syntax (no block comments)
5. By convention, three levels of commenting are used:
   - `%%%` -- Module-level comments (describing the module as a whole)
   - `%%` -- Comments for the following code block or function clause
   - `%` -- Inline comments at the end of a line of code

# Construction / Recognition
## To Construct/Create:
1. Module-level: `%%% @doc This module implements ...`
2. Function/block-level: `%% Calculate the factorial`
3. Inline: `N * fact(N-1),   % recursive case`

## To Identify/Recognize:
1. Any text on a line following a `%` character (outside strings and quoted atoms)

# Context & Application
Comments are essential for code documentation. The conventional three-level system (`%%%`, `%%`, `%`) is widely followed in the Erlang community and recognized by documentation tools like EDoc. The `-doc` attribute (introduced in newer OTP versions) provides a more structured alternative for function and module documentation.

# Examples
**Example 1** (Module Syntax section):
```erlang
-module(m).          % module attribute
-export([fact/1]).   % module attribute

fact(N) when N>0 ->  % beginning of function declaration
    N * fact(N-1);   %  |
fact(0) ->           %  |
    1.               % end of function declaration
```

# Relationships
## Builds Upon
This is a foundational concept with no prerequisites.

## Enables
None directly.

## Related
- **erlang-module** -- Comments appear within modules

## Contrasts With
None.

# Common Errors
- **Error**: Trying to use `/* */` style block comments
  **Correction**: Erlang only supports `%` line comments; use multiple `%` lines for multi-line comments

- **Error**: Placing a `%` inside a string and expecting it to start a comment
  **Correction**: `%` inside strings is a literal character, not a comment delimiter

# Common Confusions
- **Confusion**: Thinking the number of `%` characters has syntactic meaning
  **Clarification**: To the compiler, `%`, `%%`, and `%%%` are identical -- everything after the first `%` is a comment. The convention of using different counts is purely for human readability and tool support.

# Source Reference
"Modules" chapter, "Comments" section.

# Verification Notes
- Definition source: Direct quote from source
- Confidence rationale: High -- explicit definition in source
- Uncertainties: The three-level convention (%%%, %%, %) is community practice, not explicitly described in this section of the reference manual
- Cross-reference status: All slugs correspond to planned or existing cards
