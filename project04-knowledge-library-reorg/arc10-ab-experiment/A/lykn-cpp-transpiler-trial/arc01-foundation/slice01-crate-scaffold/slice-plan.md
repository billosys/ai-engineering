# Arc 01 Slice 01: Crate Scaffold

## Goal

Create the first usable implementation slice for the trial: a Rust crate with a thin CLI, a testable library API, a documented trial syntax choice, structured errors, support for `(print 42)`, and deterministic generated C++ output.

## In Scope

- Create the Rust package under the experiment workspace.
- Add a syntax note documenting the trial language's relationship to Lykn.
- Implement `transpile(source: &str) -> Result<String, TranspileError>`.
- Support exactly one accepted source shape: `(print <integer-literal>)`.
- Generate one C++17 source string with `#include <iostream>`, `int main()`, `std::cout << 42 << "\n";`, and `return 0;`.
- Add a thin CLI that reads an input file and writes generated C++ to stdout.
- Add unit and CLI integration tests for success and one unsupported/invalid input diagnostic.
- Add one generated C++ example file for the literal print case.

## Out of Scope

- `let` bindings.
- Identifiers.
- Arithmetic expressions beyond an integer literal.
- Multiple statements.
- Full Lykn compatibility.
- C++ compile/run gates unless CC records them as extra evidence.
- Code audit.

## Verification Approach

CDC should later verify this slice by inspecting the actual files and rerunning the ledger commands in `ledger.md`. CC's closing report is proposed-done until CDC reproduces the evidence.

## Exit Criteria

Every row in `ledger.md` reaches a final status with evidence. The close report must include a row-by-row ledger walk and a Bubble-up to the arc section.
