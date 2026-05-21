---
# === CORE IDENTIFICATION ===
concept: File Inclusion
slug: file-inclusion

# === CLASSIFICATION ===
category: core-idioms
subcategory: preprocessor
tier: foundational

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Preprocessor"
chapter_number: null
pdf_page: null
section: "File Inclusion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "-include"
  - "-include_lib"
  - "include directive"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-module
  - preprocessor-directives
extends: []
related:
  - macro-definition
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I include a header file in Erlang?"
  - "What is the difference between -include and -include_lib?"
  - "Where does the compiler search for include files?"
---

# Quick Definition
The `-include(File)` and `-include_lib(File)` directives insert the contents of a file at the directive's position during compilation. `-include` uses file paths; `-include_lib` uses OTP application-relative paths.

# Core Definition
The Erlang Reference Manual states: "A file can be included as follows: `-include(File).` `-include_lib(File).`" where "`File`, a string, is to point out a file. The contents of this file are included as is, at the position of the directive." The manual notes: "Include files are typically used for record and macro definitions that are shared by several modules. It is recommended to use the file name extension `.hrl` for include files." (Preprocessor, "File Inclusion" section).

For `-include`, the file is searched in: (1) the current working directory, (2) the directory where the module is being compiled, (3) the directories given by the `include` option.

For `-include_lib`, "the first path component (possibly after variable substitution) is assumed to be the name of an application." The code server uses `code:lib_dir/1` to find the application directory.

# Prerequisites
- **erlang-module** -- Include directives appear within modules
- **preprocessor-directives** -- Includes are preprocessor directives

# Key Properties
1. `-include(File)` -- searches relative paths in current dir, compile dir, and include paths
2. `-include_lib(File)` -- first path component is treated as an OTP application name
3. File contents are included as-is at the directive's position
4. Convention: include files use the `.hrl` extension
5. `File` can start with `$VAR` for environment variable substitution
6. If a path is absolute (possibly after variable substitution), it is used directly

# Construction / Recognition
## To Construct/Create:
1. For local includes: `-include("my_records.hrl").`
2. For includes with paths: `-include("incdir/my_records.hrl").`
3. For OTP application includes: `-include_lib("kernel/include/file.hrl").`
4. With environment variable: `-include("$PROJ_ROOT/my_records.hrl").`

## To Identify/Recognize:
1. The `-include("...")` or `-include_lib("...")` directives
2. File arguments are strings, not atoms

# Context & Application
File inclusion is essential for sharing record definitions, macro definitions, and type specifications across modules. Since Erlang records are a compile-time construct and must be defined identically in every module that uses them, header files (`.hrl`) are the standard mechanism for this sharing. `-include_lib` is preferred for OTP application dependencies because it resolves to the correct application version at compile time.

# Examples
**Example 1** (File Inclusion section):
```erlang
-include("my_records.hrl").
-include("incdir/my_records.hrl").
-include("/home/user/proj/my_records.hrl").
-include("$PROJ_ROOT/my_records.hrl").
```

**Example 2** (File Inclusion section, using include_lib):
```erlang
-include_lib("kernel/include/file.hrl").
```
The code server uses `code:lib_dir(kernel)` to find the directory of the current (latest) version of Kernel, and then the subdirectory `include` is searched for the file `file.hrl`.

# Relationships
## Builds Upon
- **preprocessor-directives** -- Include is a preprocessor directive

## Enables
- Sharing record, macro, and type definitions across modules

## Related
- **macro-definition** -- Macros are commonly defined in include files

## Contrasts With
None. Note that `-include` and `-include_lib` differ in path resolution, not in the inclusion mechanism.

# Common Errors
- **Error**: Using `-include_lib` with a relative path that is not an application name
  **Correction**: The first path component of `-include_lib` must be an OTP application name (e.g., `kernel`, `stdlib`)

- **Error**: Forgetting to add the include directory to the compiler's search path
  **Correction**: Use the `-I` flag with `erlc` or the `{i, Dir}` option with `compile:file/2`

# Common Confusions
- **Confusion**: Thinking `-include` and `-include_lib` are interchangeable
  **Clarification**: `-include` searches for files using file system paths. `-include_lib` resolves the first path component as an OTP application name using `code:lib_dir/1`. Use `-include_lib` when including headers from OTP applications.

# Source Reference
"Preprocessor" chapter, "File Inclusion" section.

# Verification Notes
- Definition source: Direct quotes from source
- Confidence rationale: High -- explicit definition with search path details and examples
- Uncertainties: None
- Cross-reference status: All slugs correspond to planned or existing cards
