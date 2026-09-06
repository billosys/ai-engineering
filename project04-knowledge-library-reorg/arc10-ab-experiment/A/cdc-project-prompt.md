# Framework Effectiveness Trial: Lykn to Tiny C++ Transpiler

You are participating in an A/B evaluation of an AI engineering collaboration
framework. Your job is to use the framework at the exact path provided below
to plan and guide a small real software project deeply enough to evaluate
project planning, implementation support, and later code-audit behavior.

## Framework Under Test

Run label: `framework-0.4.1`

Framework root:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1`

Framework entrypoint:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/SKILL.md`

Experiment workspace:

`/Users/oubiwann/lab/billosys/ai-engineering/.worktrees/0.4.1/workbench/lykn-cpp-transpiler-trial`

Important constraints:

- You MUST use the collaboration framework from the exact entrypoint above.
- You MUST NOT use the installed `collaboration-framework` skill or any other
  copy of the collaboration framework.
- If the framework entrypoint routes you to supporting files, load those
  supporting files from the same framework root/version only.
- Do not inspect or borrow from the other framework version being tested.
- Do not silently substitute newer, older, installed, cached, or remembered
  framework instructions.
- You may use the Rust and C++ domain skills at the explicit paths below,
  because those are part of the project domain rather than the collaboration
  framework under test:
  - Rust: `/Users/oubiwann/.codex/skills/rust-guidelines/SKILL.md`
  - C++: `/Users/oubiwann/.codex/skills/cpp-guidelines/SKILL.md`
- You may inspect the Lykn language guides at:
  - `/Users/oubiwann/lab/lykn/lang/docs/guides/`

## Scientific Controls

This is a comparison run. Do not optimize for looking good; optimize for
faithful execution under the framework version you were assigned.

At the start of your response, record:

- the run label,
- the framework entrypoint you loaded,
- the framework files you read,
- any domain/reference files you read,
- any assumptions you made.

Do not infer extra process rules from other framework versions, prior
conversations, installed skills, or memory. If the assigned framework lacks a
process detail, make the smallest reasonable local decision and record it as an
assumption.

Keep the project small. A good trial produces enough real planning,
implementation, validation, and audit surface to compare framework behavior; it
does not try to become a serious compiler project.

## Project

Build a Rust implementation of a compiler/transpiler from a tiny
Lykn-inspired syntax to a deliberately tiny, safe subset of C++.

The implementation language is Rust.

The output language is C++17, but only the tiny subset listed below. The subset
should be deliberately scoped so the project can produce real code, tests, and
auditable design decisions without becoming a full compiler.

Use the Lykn guides to understand how Lykn is currently used as syntax for
JavaScript. Then design the minimum Lykn-to-C++ mapping needed for this trial.

Use the C++ guidelines to design the generated C++ subset conservatively. Favor
simple, modern, RAII-compatible C++ with clear initialization, predictable
control flow, and standard-library-first output.

Use the Rust guidelines to design and implement the transpiler as idiomatic
Rust. The Rust implementation should be testable, reasonably modular, and
suitable for a later code audit.

## Scope Limit for This Trial

Target a tiny implementation with this maximum scope:

- Input: a small Lykn-inspired source file containing integer `let` bindings
  and `print` statements.
- Expressions: integer literals, identifiers, `+`, `-`, `*`, `/`, and
  parentheses.
- Output: one C++17 source file with `#include <iostream>` and `int main()`.
- Generated C++: local `int` variables, expression statements,
  `std::cout << ... << "\\n";`, and `return 0;`.
- Errors: clear diagnostics for unsupported syntax, unknown identifiers if
  feasible, and malformed expressions.
- Interface: either a small CLI or a library API plus thin CLI, whichever the
  assigned framework leads you to choose.

Explicitly out of scope:

- Full Lykn compatibility.
- JavaScript semantics.
- C++ classes, templates, headers, pointers, references, ownership modelling,
  exceptions, build-system generation, optimization, formatting beyond
  deterministic readable output, and multi-file C++ output.
- Type inference beyond treating all values as `int`.
- Functions, conditionals, loops, strings, arrays, objects, imports, modules,
  macros, comments, or source maps unless the framework gives a strong reason
  to include one and records it as a deliberate scope change.

A good result should produce perhaps a few hundred lines of Rust across
parser/AST/codegen/tests, not a multi-week compiler project.

## Expected Project Depth

The complete trial project should be small enough to finish in a handful of
slices. Prefer 3 arcs if that fits the assigned framework, and do not exceed 4
arcs or 8 total slices without recording a specific reason.

The trial should eventually include:

- a parser for the tiny accepted subset,
- a small AST,
- deterministic C++ code generation,
- structured errors,
- fixtures for valid and invalid programs,
- Rust unit or integration tests,
- one or two generated C++ examples,
- enough implementation surface for a later code-audit pass.

Do not try to implement everything in the first slice. The first slice should
be useful, bounded, and capable of producing evidence.

## Your Role

Hold the role of CDC.

For this first turn, do not implement the transpiler yourself. Your job is to
create the planning packet and the first CC prompt.

Please produce:

1. A project plan with all projected arcs laid out in order.
2. Detailed planning for Arc 01 only.
3. A first slice plan for Arc 01 Slice 01.
4. A CC prompt for Arc 01 Slice 01 that I can pass directly to CC.
5. A short evaluation note explaining what evidence this slice should produce
   for later comparison between framework versions.

If you create files, place them under the experiment workspace named above. Do
not edit the framework source files themselves unless the operator explicitly
asks you to.

## Planning Expectations

Use the assigned framework's project-management and SDLC practices as
faithfully as possible.

The plan should make clear:

- project goal,
- non-goals,
- target C++ subset,
- likely Rust crate/tool shape,
- expected validation gates,
- how Lykn reference material will be used,
- how Rust and C++ guidelines will be used,
- what artifacts CC should create,
- what evidence CDC should later verify,
- when the project should become ready for an audit pass.

## Later Audit Pass

This project is not only testing implementation. After enough implementation
slices have landed, we will ask you to use the same assigned framework version
to perform a code audit.

Therefore, during planning, make sure the project will eventually produce
auditable surfaces such as:

- parser and AST code,
- code generation code,
- error types,
- CLI or library API boundaries,
- fixtures and tests,
- generated C++ examples.

Do not perform the audit yet. Just plan toward making a fair audit possible.
Prefer shallow-but-real implementation depth over broad language coverage; the
audit should evaluate actual Rust design and generated-C++ choices, not the
ambition of the language roadmap.

## Output Format

Please organize your response with these sections:

1. `Run Setup`
2. `Framework Files Loaded`
3. `Reference Files Loaded`
4. `Project Plan`
5. `Arc 01 Plan`
6. `Arc 01 Slice 01 Plan`
7. `CC Prompt: Arc 01 Slice 01`
8. `Evaluation Notes`

The CC prompt should be self-contained and should include exact instructions
for what CC should read, create, modify, validate, and report.

End by stating whether you believe Arc 01 Slice 01 is ready to hand to CC.
