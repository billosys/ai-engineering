---
name: cpp-guidelines
description: |
  Comprehensive C++ best practices, idioms, and anti-patterns grounded in the
  ISO C++ Core Guidelines by Bjarne Stroustrup, Herb Sutter, and contributors.
  Use when: writing new C++ code, refactoring existing C++ code, reviewing C++
  for correctness or style issues, designing APIs and ownership boundaries,
  applying RAII/resource management, choosing parameter and return conventions,
  working with classes/value types/templates/concepts, handling exceptions and
  noexcept, diagnosing lifetime/null/dangling-pointer hazards, using the
  standard library, modernizing C-style or legacy C++, wiring CMake/tooling, or
  triaging generated C++ for safety, concurrency, performance, and idiom drift.
license: MIT
metadata:
  hermes:
    tags: [cpp, cplusplus, core-guidelines, raii, templates, concurrency, cmake]
    category: systems-programming
---

# C++ Coding Guidelines Skill

## Overview

This skill exposes the C++ Core Guidelines as a source-preserved, topic-split
knowledge pack. The upstream repository is imported under
`knowledge/cpp/sources/md/cpp-core-guidelines/` with history preserved. The
LLM-facing guides in `knowledge/cpp/guides/` keep upstream guideline IDs and
anchors intact while splitting the large source document into task-oriented
chapters.

The default posture is modern C++ with RAII, static type safety, clear
ownership, scoped lifetimes, standard-library-first design, and gradual
adoption in legacy code. The project under inspection still wins: check its
C++ standard, build system, compiler, formatter, warning policy, sanitizer
policy, and existing idioms before applying these defaults mechanically.

## Notes for Codex

Load `11-anti-patterns.md` first on any C++ task. It is an index of negative
rules and generated-code traps; the detailed rationale and examples live in
the home topic guide for each rule.

Treat the imported C++ Core Guidelines source as authoritative. The generated
topic guides are easier to navigate, but when exact wording, licensing, or
edge-case rationale matters, inspect
`knowledge/cpp/sources/md/cpp-core-guidelines/CppCoreGuidelines.md`.

Strength and wording come from the C++ Core Guidelines. A guideline violation
may still be justified by ABI, embedded, real-time, no-exceptions, legacy, or
interoperability constraints. If a project must violate a rule, isolate the
violation behind a narrow interface and document the reason, following `I.30`.

For toolchain work, inspect the repository before prescribing tools:
`CMakeLists.txt`, `meson.build`, `BUILD.bazel`, `Makefile`, `.clang-format`,
`.clang-tidy`, compiler flags, CI files, package manager manifests, and test
layout. Prefer existing local gates over inventing a new policy.

## Document Locations

All guideline documents are in `knowledge/cpp/guides/`:

- `01-core-idioms.md` — Abstract, introduction, philosophy, type safety, immutability, naming/layout
- `02-api-design.md` — Interfaces, contracts, ownership at boundaries, globals, ABI, Pimpl
- `03-functions.md` — Function design, parameter passing, return values, lambdas, `constexpr`, `noexcept`
- `04-classes-and-value-types.md` — Classes, regular/value types, constructors/destructors, hierarchies, operators, unions, enums
- `05-resource-management.md` — RAII, ownership, raw pointers/references, allocation, smart pointers, GSL
- `06-error-handling.md` — Exceptions, `noexcept`, exception safety, error codes, failure contracts
- `07-templates-and-generics.md` — Templates, concepts, generic constraints, variadic templates, metaprogramming
- `08-concurrency.md` — Data races, locks, threads, tasks, condition variables, coroutines
- `09-performance.md` — Measurement, optimization discipline, allocation, locality, false sharing
- `10-expressions-and-statements.md` — Initialization, scope, casts, macros, arithmetic, pointers, control flow, constants
- `11-anti-patterns.md` — Cheap safety net: negative rules and recurring generated-code risks
- `12-project-structure-and-tooling.md` — Source files, headers, namespaces, profiles, enforcement, supporting tools
- `13-standard-library.md` — Standard-library guidance, containers, strings, IO streams, library selection
- `14-c-style-and-modernization.md` — C-style programming, C interop, legacy modernization, gradual adoption
- `15-reference-and-glossary.md` — Architectural notes, non-rules/myths, references, FAQ, discussion, glossary, proto-rules

Supporting material:

- `knowledge/cpp/sources/md/cpp-core-guidelines/` — subtree-preserved upstream source repository
- `knowledge/cpp/extraction-metadata/cpp-core-guidelines-analysis.md` — split analysis and rule counts
- `knowledge/cpp/tools/split_cpp_core_guidelines.py` — regeneration script for the guide layer

## Document Selection Guide

| Task | Load These Documents |
|------|---------------------|
| Any C++ code | `11-anti-patterns.md` first, then topic-specific |
| New code from scratch | `11-anti-patterns.md`, `01-core-idioms.md`, `05-resource-management.md` |
| API design | `02-api-design.md`, `03-functions.md`, `05-resource-management.md` |
| Ownership/lifetime/nullability | `05-resource-management.md`, `02-api-design.md`, `10-expressions-and-statements.md` |
| Function signatures | `03-functions.md`, `02-api-design.md` |
| Class/value type design | `04-classes-and-value-types.md`, `05-resource-management.md` |
| Constructors/destructors/rule of zero | `04-classes-and-value-types.md`, `06-error-handling.md` |
| Exceptions/error handling | `06-error-handling.md`, `03-functions.md` |
| Templates/concepts/generic APIs | `07-templates-and-generics.md`, `02-api-design.md` |
| Concurrency/coroutines | `08-concurrency.md`, `05-resource-management.md` |
| Performance work | `09-performance.md`, then the touched topic guide |
| Casts/macros/arithmetic/control flow | `10-expressions-and-statements.md`, `11-anti-patterns.md` |
| Headers/source layout/tooling | `12-project-structure-and-tooling.md` |
| Standard library usage | `13-standard-library.md`, `10-expressions-and-statements.md` |
| Legacy C/C++ modernization | `14-c-style-and-modernization.md`, `11-anti-patterns.md` |
| Code review/quality audit | `11-anti-patterns.md`, then each touched topic guide |

## Workflow

### For Writing New Code

1. Load `11-anti-patterns.md`, then `01-core-idioms.md`.
2. Inspect the project standard and tooling before choosing C++17/20/23 features.
3. Prefer RAII handles, standard library vocabulary types, `const` by default,
   narrow scopes, explicit ownership transfer, and strongly typed interfaces.
4. Load topic guides for functions, APIs, classes, templates, errors, or
   concurrency as needed.
5. Run the project’s formatter, compile, tests, static analysis, and sanitizers
   when available.

### For Refactoring or Modernizing

1. Load `11-anti-patterns.md` and `14-c-style-and-modernization.md`.
2. Change one rule family at a time: ownership, initialization, casts, macros,
   globals, hierarchy design, or error handling.
3. Preserve ABI and behavioral compatibility unless the user explicitly asks
   for a breaking cleanup.
4. Keep necessary legacy or unsafe constructs behind narrow interfaces and
   cite the relevant rule ID, especially `I.30`.

### For Code Review

1. Start with `11-anti-patterns.md`.
2. Map each finding to a rule ID when possible.
3. Prioritize correctness, lifetime, ownership, undefined behavior, exception
   safety, concurrency, and ABI risks over surface style.
4. Load the home guide for any rule before making a nuanced judgment.

## Critical Rules

- Prefer RAII and scoped objects; avoid naked `new`/`delete` and `malloc`/`free`.
- A raw pointer or reference is non-owning unless explicitly wrapped or named as ownership.
- Do not transfer ownership through raw `T*` or `T&`.
- Always initialize objects; keep scopes small and make values `const` when they should not change.
- Prefer return values over output parameters; use `T*` only when null is a meaningful option.
- Destructors, deallocation, `swap`, and exception copy/move operations must not fail.
- Avoid data races; use RAII lock guards and do not detach threads without a documented lifecycle reason.
- Avoid casts, macros for program text, naked unions, implicit conversions, and C-style arrays when safer vocabulary types exist.
