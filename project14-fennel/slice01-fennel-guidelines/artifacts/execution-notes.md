# Execution notes — Project14 / Slice01

## Intake and contract readback

Read the initial project plan, slice plan and both ledgers in full before dependent
implementation. The preserved initial cc-prompt was read in full; the Operator's
subsequent single-contributor instruction supersedes its workflow gate. The current
project/slice plan records that transition and the required fresh-context audit.

The source import must retain the selected original bytes and pertinent history,
not merely copy the latest docs. The new skill must teach Lua semantics explicitly,
route to focused guides and work inside a generated package. Runtime examples,
history fidelity and package-path checks prove different properties. Upstream
style licensing cannot be silently changed to the root repository's MIT notice.
The Operator authorized autonomous completion and a fresh audit with corrections;
self-checks remain attributed to the primary context rather than mislabeled CDC QA.

Template/reference reads: Rust entrypoint selection/workflow/integration conventions
and core-idiom pattern examples; Makefile pack_skill, inventories, aggregate,
install and validation routes; README and docs/skill-library table. Framework
loads included project-management's wayfinder/layout/confirmation/top-down and
closure guides; work-verification ledger and row closure; skill-creator; testing
and validation gates; agent-coordination; and evidence/severity audit guides.

Source reads were bounded by guide claims: values, style, macros and rationale;
setup embedding/AOT; tutorial binding/table/error/vararg/module/gotcha sections;
reference syntax, functions, destructuring, case/match/guards, set, with-open,
pick-values, loops, operators, comprehensions, calls, include and macro/compiler
sections; API options/compile/searcher/view/docstring bodies; Lua primer types,
iteration/io/tables/loading and Clojure comparison runtime/tables/iteration. The
primary's section reads are not a claim to have read every supplemental page or
all history semantically. The fresh audit independently reports its own coverage.
History checks queried every retained rewritten commit and selected path; those
are full-population data checks, not semantic reading of every commit.

## Significant intermediate failures and corrections

- The initial network clone in the sandbox failed DNS resolution. The authorized
  escalated clone succeeded; the actual full upstream objects were used thereafter.
- The historical-path preflight initially rejected api.md because --follow found
  README.md. Retaining README preserved that lineage and also kept the language
  overview. The project/slice plans record the clarification.
- First example pass: 69/112 passed, 43 failed due to surplus closing delimiters
  in draft examples. These were repaired and the project-owned examples formatted.
  The original JSON/log are retained; subsequent passes reached 112/112. The
  eight intended compile-negative cases now check their specific diagnostics.
- The first package gate rejected the history heading because its recognizer
  requires `## Version ...`; corrected the heading without changing version policy.
- The skill-creator validator initially lacked PyYAML under system python3;
  rerunning with the repository's .venv/bin/python succeeded. No installation
  or dependency changes were needed.

## Check coverage

- History: 749 rewritten commits, 679 selected-path non-merge change commits,
  7,493 historical blobs and 14 exact current source files. Original identities,
  timestamps and messages compared; imported graph is reachable through the
  second parent of c6a089ba. Rewritten cryptographic signatures are not retained.
- Examples: 112 blocks = 56 GOOD + 56 BAD. Eight deliberately invalid examples
  must produce the intended compile diagnostic. The other 104 compile and execute
  under both Fennel and emitted Lua; expected/undesirable behaviors use assertions.
  Formatter checks cover the 103 ordinary executable blocks; ST-01 BAD intentionally
  demonstrates ugly layout, and the eight compile-negative blocks are separate.
- Integration: 9 checks cover a real module/macro consumer, embedded Lua host,
  bundled AOT with globals checking, execution with package.path/package.cpath
  empty in a clean directory, strict rejection versus bare-AOT emission of an
  unknown global, actual library relocation and a relocated bundled artifact.
- Package: exact 14 shipped files equal their source bytes, 56 unique rule IDs,
  resolving local guide links, 25 source skill/25 generated package version
  checks, and zero hard failures in the full catalog path gate. The dedicated
  Fennel path check has zero warnings or exceptions. Other catalog warnings are
  reported by the normal repository gate and are outside this slice's changes.

Limit: these executions use Fennel 1.6.1, fnlfmt 0.3.2 and PUC Lua 5.5. They do not
establish compatibility on Lua 5.1/5.2/5.3/5.4 or LuaJIT or an embedded production
host. The guide makes those target-specific checks explicit. No comparative
performance or universal correctness claim is made.

## Final record hygiene

The planning-tree whitespace gate flagged a terminal blank line in the rendered
initial example log. Its trailing blank lines were normalized to one newline;
all diagnostic text and the full initial JSON results remain preserved. The source
whitespace gate was already clean. The corrected planning diff is checked again
before its final record commit.
