# From Slice to Implementation Prompt

Read this guide **before authoring or reviewing an initial CC implementation
prompt or a corrective iteration**. It operationalizes SDLC step 5: the author
turns an approved slice into an actionable code, investigation or evidence
assignment.
Use the [authoring template](../templates/cc-implementation-prompt.md) as a
starting shape, adapting its sections to the work.

Engineering-methods owns this design-to-execution contract. Project-management
owns slice selection, sizing, artifact homes, preserved assignments and handoff
history. Testing owns verification technique; work-verification owns evidence
strength and independent acceptance. Domain skills supply the engineering
knowledge that the prompt author must apply. None of those layers replaces
the author doing the engineering work below.

## Author responsibility and decision authority

Follow the selected contributor workflow in
[Engineering Methodology](./01-engineering-methodology.md#roles-and-shared-invariants).
CDC prepares first slices and, with two contributors, subsequent assignments.
CRC prepares subsequent slices and corrective iterations within the approved
design when three contributors are explicitly enabled. **The author performs
the source investigation, guideline application, implementation reasoning and
test design before handing the work to CC.** Asking CC to load a skill does not
discharge that obligation.

CRC's duty to detail the implementation is substantive engineering work. It
does not make CRC a second architecture authority: unresolved architecture,
scope or acceptance changes return to CDC and the Operator before affected work
is issued. CDC resolves those decisions with the Operator. Do not turn an
unresolved design question into an implementation instruction.

CC retains implementation skill and the duty to challenge a mistaken design.
It may choose local mechanics inside the stated contract, discover mismatches,
and propose improvements. It must not silently select public API behavior,
failure semantics, lifecycle, compatibility or acceptance policy left open by
the author. Label each consequential decision:

- **Binding:** approved behavior or constraint, with rationale and authority.
- **Recommended:** a worked implementation approach; alternatives may preserve
  the same contract within stated bounds and must be explained on return.
- **Local discretion:** choices such as private helper names that have no
  contract, ownership, ordering, performance-budget or scope consequences.
- **Unresolved:** owner, decision needed and affected work held. Resolve before
  issuing dependent implementation, or explicitly assign bounded investigation
  whose output is a decision packet rather than production code.

For explicitly selected one-contributor work, apply the engineering reasoning
proportionately in the existing task record; do not manufacture a CC handoff.

## 1. Investigate the actual implementation baseline

Before drafting the recipe, inspect the approved project, arc and slice inputs,
the current implementation and its tests. Record the source checkout, revision
and relevant dirty changes; resolve whether it matches the planned baseline.
For every significant change, identify:

- actual files and symbols to modify, existing behavior, callers and consumers;
- existing types, helpers, dependencies and conventions to reuse;
- integration points, initialization and teardown paths, feature/platform
  boundaries, generated surfaces and compatibility obligations;
- observed gaps versus assumptions that still need verification.

Cite paths and symbols, with revision-qualified line references when useful.
Verify version-sensitive API names against the pinned dependency source or
authoritative documentation. Do not write plausible signatures from memory
and leave CC to discover whether they exist. If an API cannot be checked,
label the uncertainty and specify who resolves it before dependent work.
CC rechecks source drift; that recheck supplements the author's reconnaissance.

## 2. Apply the relevant domain guides yourself

Select installed or repository-local domain skills from the work's languages
and concerns. Load the entrypoint and the actual relevant chapters before
settling the design. Rust API/ownership/error work, Erlang/OTP process and
supervision work, Go context/concurrency work and JavaScript/Deno module work
need different guidance. Do not load every domain or silently apply a skill's
default runtime, dependency, edition or toolchain over the project's contract.

Make the application visible in the prompt or a precisely linked design
section. For each consequential guideline, record:

| Source | Applied decision | Why it fits here | Implementation and proof |
| --- | --- | --- | --- |
| Exact skill/chapter/section or verified pattern ID and strength | Chosen API, behavior, interpretation boundary or inspection method | Project constraint and tradeoff; any justified exception | Target symbol plus observable check |

This is a record of engineering decisions, not a catalogue of every rule read.
Verify pattern IDs against their chapter text; summaries can drift. Retain
MUST/SHOULD/CONSIDER distinctions. Explain why a contextual recommendation fits
this task instead of promoting it to a universal rule. If guidance conflicts
with an approved design, resolve the conflict rather than concealing it with
a citation. Do not cite a rule you did not read or claim tests prove a design
property they do not exercise.

Domain skills remain separately installed dependencies. The issued assignment
must give the executing context resolvable skill/guide paths or supply the
needed scoped material; a path that exists only on the author's machine is
not a usable handoff. If a required guide is unavailable, disclose that gap
and obtain a supported substitute before claiming guideline-grounded readiness.

## 3. Resolve the engineering design

For the current slice, specify the behavior sufficiently that CC need not
redesign it. Address each applicable concern and give a short reason when an
apparently relevant concern does not apply:

- **Types and API:** signatures, visibility, data shapes, trait/interface
  changes, invariants, ownership and borrowing, compatibility and callers.
- **Control and data flow:** operation ordering, state transitions, mutation
  boundaries, exactly-once/idempotence rules, serialization and determinism.
- **Failure behavior:** error types/variants and propagation, no-mutation
  guarantees, partial success, rollback boundaries and legitimate panic paths.
- **Resources and concurrency:** owners, lifetime, cancellation, synchronization,
  capacity/backpressure and shutdown when applicable.
- **Integration and evolution:** registration, feature combinations, existing
  behavior retained, migrations, documentation and downstream consequences.
- **Performance:** the actual budgets or complexity constraints the task needs;
  avoid both speculative optimization and unexamined hot-path allocation.

Explain the important choices and rejected alternatives. “Use best practices,”
“handle errors appropriately,” and “ensure thread safety” leave the decision
to CC; name the actual policy and how it is achieved.

Check interactions between rules, not only each rule in isolation. For a
multi-step operation that can stop, fail, cancel or change mode partway through,
specify when the transition takes effect, what completes, what state/time or
resources advance, and what the caller receives. Reconcile the prose, sketch
and tests. If both an API and shared state can trigger a transition, define
their relationship; a guard checked only at entry may not enforce later changes.

Separate immutable inputs, explicitly authorized replacements and derived
values that must be recomputed. A request to repin an input can change its hash,
range or manifest entry; do not also require every old value to remain unchanged.
Name the exceptions and retain prior evidence at its historical revision.
Neither an exception nor a refresh authorizes unrelated input changes.

## 4. Provide a concrete implementation recipe

Write ordered, file-and-symbol-level steps. Each substantive step connects:
existing code → intended change → rationale → observable result. Include the
construction and wiring sites, not only the attractive new type or algorithm.

Supply exact signatures and representative code or pseudocode where the
important decision is in the shape: a borrow boundary, state machine,
supervision tree, channel lifecycle, algorithm or error conversion. A routine
mechanical change can use precise prose instead. Label sketches as sketches,
state which properties are binding, and state whether any example was actually
compiled or exercised. Do not present a sketch as tested drop-in code.

Give CC a coherent recommended implementation, not a menu of consequential
choices to select after starting. It is useful to mention rejected approaches
and the evidence that would justify reopening them. Proposed alternatives that
change a binding contract must be reviewed before implementation, not merely
disclosed after the fact in a completion report.

Keep the detail proportionate to the slice's risk and novelty. A list of
allowlisted files is not a file-level implementation plan. A complete ledger
is not an algorithm. A long prompt full of commit commands is not necessarily
better specified than a short one with an exact, bounded design attachment.

### Investigation and semantic evidence assignments

For research, metadata or ontology work, supply the inspection method rather
than prescribing conclusions the evidence has not established. Name the input
population, exact field paths/constructs, context and witnesses to inspect,
comparisons, evidence representation, and decision owner for unresolved policy.
Distinguish documented rules, observed values, author inference and unresolved
questions in the result. Similar names at different paths need separate
interpretation; repeated values do not establish a vocabulary or requiredness.

Predeclared counts and expectations can test a pinned baseline, but CC must
derive observations from the actual input and report discrepancies. Specify
how insufficient or contradictory evidence is recorded and what it blocks;
do not make a desired semantic answer the condition for passing the assignment.
Structural replay establishes only its checked properties, not semantic warrant.

## 5. Design the tests and their oracles

Map each acceptance criterion to a concrete setup, action and expected
observable result. State exact values, errors, sequences or invariants where
the contract determines them. Include meaningful positive, negative, boundary,
regression and feature/platform cases as applicable. Identify the plausible
incorrect implementation each important test would reject.

Walk each multi-step test through the actual APIs: which object still exists,
which calls are visible from the test location, and how state is observed after
each action. A consuming conversion cannot be followed by reuse of its former
owner. Name integration versus inline/unit test homes where access differs,
and retain the applicable feature matrix for both. Do not add a public accessor
or move an action earlier merely to rescue an infeasible test and weaken its
oracle; the author must supply a viable route within the approved contract.

Ask whether the old or specifically rejected implementation could pass the
proposed test. Choose inputs that force competing behaviors to disagree: if
ordering changes from numeric IDs to names, use opposing ID/name orders and
assert the exact winner. Stable results across two runs alone may prove neither
ordering policy. Observe intermediate stages when claiming phase order or
partial-failure behavior; final totals can hide both. For a validator, run
negative inputs through the same predicate as valid inputs. This does not
require exhaustive mutation testing or compiling every illustrative sketch.

Use public or real integration paths where the promise concerns integration.
A hook counter cannot alone prove that installed systems execute; a snapshot
after failure cannot prove rollback unless it covers the state at risk; passing
a wrapper command cannot prove an underlying failed command succeeded.

Reuse appropriate existing fixtures and test helpers. Do not inflate coverage
with tests that restate private implementation or compare a result against
another call to the same algorithm. The author derives expected results from
the behavior contract, not from what CC later happens to implement.

Name the repository-native validation commands, working directories, feature
matrix, prerequisites and known baseline failures. Distinguish behavior tests
from static, package and evidence checks. Keep unavailable or failing required
checks explicit; do not let an implementation prompt waive acceptance gates.
Inspect what reused validators actually cover: target revision, current
assignment, rows and properties. A passing predecessor-specific checker is
inherited evidence, not validation of the new slice. State gaps and the check
or owner that resolves them; preserve historical evidence and gate authority.
Use the testing component when defining detailed validation technique.

## 6. Assemble a usable assignment

The prompt itself must carry the outcome, scope, consequential decisions,
implementation sequence, test expectations, stop conditions and return contract.
Detailed supporting material may live in the existing slice plan or artifact
home, but the prompt must identify **exact files and sections**, why CC needs
them, their applicable revision and what governs if they disagree. Referenced
material must contain the claimed detail. Broad “read the plans” lists do not
substitute for synthesis.

Provide a compact implementation spine in the prompt even when the full recipe
is linked. Keep current-slice instructions distinct from future designs in a
shared document. Preserve one authoritative definition of each decision;
summaries must agree with it. Conflicting sources block affected work until
the author reconciles them; CC must not choose whichever is easiest.

Follow project-management for assignment identity, baseline, permitted paths,
artifact names, commit rules, preserved history, Operator relay and reviewer
return. State whether output is implementation, investigation or evidence only.
For evidence-only work, specify the inspection method and evidence oracle;
do not demand irrelevant API sketches or authorize opportunistic code repair.

### Required reading and CC intake

Splitting an assignment across files creates a reading obligation as well as a
linking obligation. The author must put a **required-reading manifest in the
issued prompt**, not only in another document that CC might never open. Include
reading order, exact path and source state, scope, why it matters, and when it
must be loaded. Use these categories:

- **Required-full:** read the entire document, including tables, code blocks,
  appendices and footnotes. The active prompt, slice plan and slice ledger are
  required-full. Include active directives and slice-specific binding design
  documents this way unless the author explicitly bounds a shared document.
- **Required-section:** read the complete named sections and their necessary
  definitions/dependencies. The author chooses exact boundaries and explains
  why they cover the current assignment. This suits large parent plans, shared
  designs and domain chapters; CC may not silently convert required-full into
  a section skim. A bare filename in a required-reading list means required-full.
- **Required-data:** for a structured dataset, name its pinned identity,
  population/projection, exact queries or specified query behavior, and required
  outputs. CC executes the queries and inspects their complete results, retaining
  commands, exits, denominators, exclusions and errors in the allowed evidence
  home. Recover truncated results or use lossless partitions of the required
  projection. This permits computation over a large input without dumping it
  all into context; it does not permit sampling to stand in for a whole-set
  check. Separately name full/section reads for witnesses whose meaning requires
  body context. Query coverage is not a claim of full-document semantic reading.
- **Conditional:** name the concrete trigger and exact material to load before
  the affected step. Record whether the trigger applies. Do not use this label
  to defer universally applicable scope, safety or acceptance constraints.
- **Reference-only:** optional background/provenance, not required execution
  instructions. If implementation depends on it, it belongs above.

Required-data applies to structured inspection, not as a substitute for reading
the prompt, plans, directives, guides or required witness prose. These labels
never reduce reading required by governing instructions. Enumerate known
normative dependencies; do not leave CC to chase an unbounded chain of
links or infer that every historical reference is an active instruction. A newly
encountered binding dependency must be loaded and recorded before affected work.
Keep current authority distinct from superseded prompts and historical examples.
The author applies the same complete-loading standard to their own required
inputs before declaring readiness.

**Budget the actual packet.** Account for source inspection, required reading,
implementation and recovery headroom when sizing the slice. If the packet cannot
fit coherently, the author must bound shared-document sections without losing
obligations or use the established re-slicing process. Do not respond by asking
CC to skim, silently drop requirements, or replace normative text with a summary.

**CC preflight, before dependent implementation:**

1. Confirm the active assignment and source state, then load the manifest's
   required text into the executing context and perform the declared required-data
   queries with visible results. File existence, byte counts,
   hashes, grep hits, headings, summaries and another agent's reading do not
   establish that this context received the full required content.
2. Use bounded reads sized so the tool returns their complete contents. When
   output is truncated or elided, recover the omitted portions using contiguous
   chunks with explicit ranges until the required extent is covered. Check the
   end of the file or section; do not equate command exit zero with full output.
   Shell redirection into a log is not loading that log into model context.
3. Record each required item, source state, loaded extent and any missing or
   truncated portions. Cite tool-output identifiers or visible read ranges where
   the environment exposes them; do not invent receipts. A tracked revision
   identifies committed content; qualify dirty or untracked inputs separately.
   Call text reads complete only after loading all required content; record
   data-query coverage and inspected results separately from document reads.
   Record conditional items as triggered/loaded or not applicable with a reason.
4. Write a brief **contract readback** in your own words: connect the slice's
   consequential obligations to source sections or ledger rows, intended changes or
   inspections and observable checks. Cover scope/exclusions, API and data contracts,
   failure/lifecycle rules, and acceptance gates as applicable. Explain the
   easily missed constraint that would invalidate an otherwise plausible
   implementation. Surface disagreements or uncertainty instead of reciting
   headings, copying the prompt, or saying “all files read.” This is a concise
   account of the contract and its consequences, not a transcript of reasoning.
5. Repair gaps or contradictions before affected edits. Unavailable required
   material blocks dependent work; report the exact item and owner needed.
   Once preflight is complete and coherent, proceed under existing authority;
   this is not a new permission request or a return-only assignment.

The prompt author names the intake record's home in an already allowed evidence
file or execution log; carry its reference into the closing report. Do not
invent another planning tree or require a separate artifact merely for receipts.
Keep the record concise: do not paste every source file into it. In a resumed
or compacted context, revalidate assignment/source state and reload required
contracts no longer reliably available before dependent work resumes. A previous
context's “read” claim or a compaction summary is not the original authority.

**Review evidence at the right strength.** The assigned reviewer checks intake
coverage and the readback against the actual sources, then checks implementation
and behavioral evidence against that contract. A readback that misses a binding
constraint is a defect to investigate even if the file list is complete.
Reading receipts are CC attestation; tool traces can establish which content
was delivered, not attention, comprehension or retention. Hashes establish
identity, not reading. Neither a receipt nor a fluent readback independently
proves understanding, and neither can replace code review and meaningful tests.
Do not add secret marker words or arbitrary recall quizzes as a quality gate.

## 7. Review readiness before issuing

The author performs this check before handing the prompt to the Operator. Record
a concise result in the existing slice plan or assignment record, with pointers
to the relevant sections; do not add a new approval role or ceremonial artifact.

1. **Source-grounded:** the recipe fits the inspected source and dependency
   baseline; assumptions are named, and critical ones are resolved.
2. **Design-complete:** consequential decisions and interacting state transitions
   are resolved within authority, including partial-work results. CC's remaining
   discretion is bounded; evidence-dependent conclusions remain open to findings.
3. **Guideline-applied:** relevant guides changed or supported concrete
   decisions with valid citations, rationale and checks.
4. **Executable:** files, symbols, integration order and representative shapes
   make a viable path visible. Test sequences respect ownership, access and
   observation points; investigation steps fit the available evidence.
5. **Falsifiable:** setups and observations distinguish the intended behavior
   from the old or rejected implementation. Test and validator coverage matches
   the claims; required gates and evidence remain intact.
6. **Coherent and portable:** prompt, plan, design and ledger agree; referenced
   material is accessible; current scope is separated from future work. The
   prompt carries a bounded required-reading manifest, intake/readback instructions
   and an allowed evidence home; the reading/query budget leaves implementation
   headroom. Preservation requirements allow exactly the authorized replacements
   and consequent identity updates, without contradictory immutable-value claims.

Ask: **Could two competent implementers follow this packet yet choose different
observable behavior, incompatible public APIs, or different failure/lifecycle
policies?** If yes, the author still owes a decision. Different private helpers
that preserve the same contract are fine. Ask also: **Did I merely repeat the
acceptance criteria, or did I supply the engineering route that meets them?**

Do not issue dependent implementation while a material gap remains. Resolve it,
escalate it, or issue an explicitly bounded investigation. Do not silently shrink
the slice. Context pressure and Expedited Mode do not lower this readiness bar.
There is no minimum byte count: detail is judged by resolved decisions and
usable guidance, not length or template-section count.

## Corrective iterations

Keep the same standard at smaller scope. Identify each unresolved row and
reproduced defect, its cause if known, the prescribed repair, affected contracts
and regression tests, and what accepted work must remain intact. If the cause
is unknown, assign bounded diagnosis with a stop condition. “Fix the review”
is insufficient. Carry forward binding constraints with precise references and
state authorized changes explicitly. Never rewrite an already issued prompt;
use project-management's preserved iteration and assignment-history rules.

## Worked fragment: registration without repeated side effects

Illustrative Rust assignment fragment, not a complete prompt or compiled code.
Assume the approved design has a rack-local installation map, a registration
hook, and a legacy chaining API. This example shows the level of author work;
it does not prescribe these APIs for unrelated projects.

**Binding decision:** add a fallible installation API with a named collision
error; retain the existing convenience API with a documented programmer-error
panic. The author has checked Rust error-handling guidance on library error
types and fallible/panicking counterparts, and justified the convenience path
for compatibility. The final assignment records the actual chapter references.

**Recommended implementation:** store kind-to-type identity privately on each
rack; initialize it in the constructor. Reuse existing registry/accessor wiring.
Inspect the installation map before obtaining mutable access to registries.
Return immediately for the same type and return the typed error for a different
type under the same kind. End temporary world/resource borrows before invoking
the hook with the application. Record success after the hook returns.

```text
try_install(type):
    kind, identity = declared kind, process-local type identity
    existing = installed[kind]
    if existing == identity: return this rack unchanged
    if existing is present: return KindConflict(kind) without mutation
    register existing metadata, spawner, setters and getters
    end world/resource borrows
    invoke the hook once with the approved schedule
    record installed[kind] = identity
    return this rack
```

**Boundary:** the no-mutation guarantee applies to detected kind conflicts.
An arbitrary user hook panic has no promised rollback. Type identity is not
persisted, used as a random seed, or used to order externally visible events.

**Test oracle:** a fixture loads two instances with output increments 2 and 3.
After one direct run of the approved schedule their totals are exactly 2 and 3;
running the unrelated schedule leaves both unchanged. Reinstall after changing
instance parameters, then run the approved schedule again: parameters persist
and each instance advances once. A different type with the same kind returns
the exact collision variant; the original spawner, accessors and behavior still
work. A second rack independently registers once. These checks reject duplicate
systems, registration on spawn, wrong scheduling, state reset and partial
replacement. Record the precise fixture APIs and feature matrix in the full
assignment after inspecting the actual repository. If accessing the application
consumes the rack wrapper, one option is an allowed inline/unit test that
retains the wrapper for the stateful reinstall sequence, alongside integration
tests for public loading/execution. Do not imply that the consumed wrapper can be reused.
