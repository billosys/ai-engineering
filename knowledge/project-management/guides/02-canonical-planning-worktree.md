# Part II — The canonical planning worktree

In the absence of a project's own stated convention, planning artifacts live on
a dedicated Git worktree, not on the implementation branch and not under the
implementation branch's `docs/` tree. This is the canonical planning worktree.
It is the single source of truth for where planning artifacts live; the
[methodology](../../engineering-methods/guides/01-engineering-methodology.md) used to carry an abridged copy
and now points here.

The default planning substrate is:

1. **Find the repository's worktree convention.** Inspect the repository before
   creating anything. If it already has a worktree directory convention, reuse
   it. Prefer an existing in-repo `.worktrees/` directory when present; otherwise
   use the convention already visible from `git worktree list`.
2. **If no convention exists, use `$PROJECT_DIR/.worktrees`.** This keeps the
   planning tree close to the repository while leaving it off the implementation
   branch.
3. **Use a `planning` branch and worktree by default.** If a suitable planning
   branch/worktree already exists, use it. If not, create a `planning` branch
   and a worktree directory of the same name under the worktree root.
4. **The `planning` branch is orphaned.** It shares the repository's Git object
   database and remotes, but it starts with no inherited implementation files.
   Its sole purpose is to house project plans, arc plans, per-scale ledgers,
   prompts, close reports, independent verification, and default homes for durable
   slice-produced artifacts. The default branch is used to identify the
   repository and remote context, not to seed the planning files.

When a planning branch/worktree does not already exist, the safe creation
recipe is:

```sh
WORKTREE_ROOT="${PROJECT_DIR}/.worktrees" # or the repo's existing convention
git -C "$PROJECT_DIR" worktree add --detach --no-checkout "$WORKTREE_ROOT/planning"
git -C "$WORKTREE_ROOT/planning" switch --orphan planning
```

The resulting default Two-Contributor Workflow shape is:

```
$PROJECT_DIR/.worktrees/planning/
  project01-<slug>/
    project-plan.md              ← the project's plan-of-record (the arc roadmap)
    ledger.md                    ← project-level DoD / composition ledger
    closing-report.md            ← project-level close + gate review, written at project close
    arcNN-<slug>/
      arc-plan.md                ← the arc's plan-of-record (the slice breakdown)
      ledger.md                  ← arc-level slice-close / composition ledger
      closing-report.md          ← arc-level close + bubble-up, written at arc close
      sliceNN-<slug>/
        slice-plan.md            ← plan-of-record for this slice
        ledger.md                ← grep-verifiable acceptance criteria (the steps)
        cc-prompt.md             ← initial CC assignment; preserved once issued
        cc-prompt-iterationNN.md ← follow-up assignment, only when needed
        artifacts/               ← supporting outputs: research, findings, logs, etc.
        closing-report.md        ← per-row walk + bubble-up, written at slice close
        cdc-verification.md      ← independent re-run + check, written at slice close
```

Three tiers of plan-of-record, one per scale: **`project-plan.md`** for the
project, **`arc-plan.md`** for each arc, and **`slice-plan.md`** for each
slice. Three tiers of ledger, one per scale: **`ledger.md`** beside each
project plan, arc plan, and slice plan. Three tiers of closing-report close the
same scales when they finish: project, arc, and slice. The per-slice
verification record is the independent re-run that gates a slice closed.
In the Three-Contributor Workflow, use `crc-verification.md` at slice level
and both `crc-verification.md` and `cdc-verification.md` beside each arc and
project plan at closure. The records have distinct responsibilities below.
When a slice produces durable artifacts, its default artifact home is
`sliceNN-<slug>/artifacts/`, unless the operator records an override. Their full
roles are defined in [`Planning, top-down`](./03-planning-top-down.md),
[`Closing slices`](./04-closing-slices.md), and
[`Closing arcs`](./05-closing-arcs.md); their on-disk shape is fixed here.

Each scale is also **verified by a ledger** — the recomposition discipline in
[`Row Closure`](../../work-verification/guides/03-row-closure.md). The ledger rows
for a scale live in that scale's own `ledger.md`: project rows in
`projectNN-<slug>/ledger.md`, arc rows in `arcNN-<slug>/ledger.md`, and slice
rows in `sliceNN-<slug>/ledger.md`. The plan-of-record names the capability,
roadmap, or slice scope; the ledger file carries the grep-verifiable rows that
prove the plan. Work verification owns the ledger mechanics at all three
scales; this file owns where the rows live.

### Naming rules

- **Projects use `projectNN-<slug>`**, matching the arc and slice convention.
  `project01-vault-split` is the shape; `docs/design-v0.1.0` is no longer the
  default. Version-looking directory names have repeatedly confused humans and
  LLMs into treating planning scope as release scope.
- **`NN` is two digits, zero-padded** (`project01`, `arc01`, `slice03`) — sorts
  cleanly, reads consistently, and survives projects that grow past nine arcs.
- **`<slug>` is short, kebab-case, and descriptive in isolation** —
  `project01-vault-split`, `arc01-discovery`, not `project01-thing`. Read aloud,
  the path should tell a reader what is in that directory without opening it.
- **Directory order is not dependency order.** Project metadata determines
  ordering and relationships: `depends-on`, `blocks`, `related`, current status,
  and any project-specific lineage fields. The numeric prefix is a stable,
  sortable local identifier, not the source of truth for dependency semantics.
- **When a body of work is one slice, not an arc**, skip the arc wrapper: the
  per-slice documents, and any slice `artifacts/` directory, live directly in
  one `sliceNN-<slug>/` directory under `projectNN-<slug>/`, with no
  `arc-plan.md` or arc-level
  `ledger.md` / `closing-report.md` above them. That collapse is not a third
  case to choose; it is what you discover when the sizing judgment comes back
  "one slice, not an arc." A project that is genuinely a single slice may keep a
  minimal `project-plan.md` and project-level `ledger.md`, but the moment a
  second arc is conceivable, write the full roadmap.

### Project metadata

Every `project-plan.md` begins with a short metadata block or equivalent header
section that makes relationships explicit. Minimum fields:

| Field | Meaning |
| --- | --- |
| `project` | Stable project id, matching `projectNN-<slug>`. |
| `status` | `planned`, `active`, `blocked`, `closed`, or project-specific status. |
| `depends-on` | Project ids or external prerequisites this project consumes. Empty is explicit. |
| `blocks` | Project ids or external outcomes blocked by this project. Empty is explicit. |
| `related` | Adjacent projects, tickets, repos, or evidence sources that are not hard dependencies. |

Use the same relationship vocabulary consistently across project plans. If a
project has a richer metadata schema, record it in the project instructions and
keep these meanings intact.

### The per-slice documents and artifact home

The five base Markdown documents under each `sliceNN-<slug>/` form an
**open set** (written when the slice is planned, before any code) and a
**close set** (written when the slice finishes). Follow-up prompts extend this
first-class document set when another assignment is issued:

| Path | Set | Role |
|----------|-----|------|
| `slice-plan.md` | open | Plan-of-record: goal, scope (in/out), verification approach, exit criteria. |
| `ledger.md` | open | The acceptance criteria as grep-verifiable rows — the steps. Format and discipline in [`Row Closure`](../../work-verification/guides/03-row-closure.md). |
| `cc-prompt.md` | open | Initial assignment to CC; preserve its contents once issued. |
| `cc-prompt-iterationNN.md` | iteration | A new assignment for each follow-up pass; a sibling of the initial prompt, never a supporting artifact. |
| `crc-escalationNN.md` | as needed | Preserved CRC-to-CDC decision report, relayed by the Operator. |
| `cdc-directiveNN.md` | as needed | Preserved CDC-to-CRC assignment or response to an escalation, relayed by the Operator. |
| `closing-report.md` | close | The per-row walk written at slice close, plus the **bubble-up to the arc** (see [`Closing slices`](./04-closing-slices.md)). |
| `cdc-verification.md` (two contributors) or `crc-verification.md` (three contributors) | close | The assigned reviewer's independent re-run that verifies the closing report against evidence, plus the **bubble-up check** (see [`Closing slices`](./04-closing-slices.md)). |
| `artifacts/` | as needed | Default home for supporting outputs such as research, findings, logs, and analysis. Excludes the first-class slice documents above. Create only when needed or when it clarifies the handoff. |

Opening the close-set documents at slice start, or leaving the open-set
documents unfinished when handing off to CC, are both spec-keeping failures.
Write the open set fully before CC starts; write the close set only once
there is something to close.

If the slice is expected to create durable artifacts, name the artifact home in
`slice-plan.md` and `cc-prompt.md`; the default is `artifacts/` inside the slice
directory. If no durable artifacts are expected, a short "Artifacts: none
expected" line is enough. If the operator wants those artifacts somewhere else,
record the override and rationale in the slice plan before work begins, and
carry the chosen path into the prompt and close evidence.

### Design handoff filenames and preservation

In the Three-Contributor Workflow, place `crc-escalationNN.md` and its matching
`cdc-directiveNN.md` beside the owning `slice-plan.md`. If the decision is owned
at arc or project scale, place the pair beside that scale's plan and link it
from affected child plans; do not create competing copies per child. These are
first-class handoff records, not supporting files under `artifacts/`.

For a new exchange, use a two-digit number above the highest used by either
prefix in that directory, starting at `01`. A response directive uses its
escalation's number. Pending escalations reserve that number: an initial or
proactive CDC assignment starts a new exchange, names the initiating
Operator/CDC decision, and does not consume a pending response slot. Create
packets only when issuing a real request, assignment, or response; never
pre-create an approval or verdict. Preserve every issued
packet's content and path. A correction or follow-up gets a new number and
links its predecessor; no mutable "latest" packet or silent overwrite.

Record the current exchange and status in the owning plan's **Design handoff
history**. These numbers identify correspondence, not extra implementation
iterations or permission to reset CC's iteration budget. For the required
contents and Operator relay, read
[Design escalation and return handoffs](./03-planning-top-down.md#design-escalation-and-return-handoffs).

### Verification records by workflow and scale

| Scale | Two-Contributor Workflow | Three-Contributor Workflow |
| --- | --- | --- |
| Slice | `cdc-verification.md`: CDC independently reviews CC's implementation. | `crc-verification.md`: CRC independently reviews CC's implementation. |
| Arc | CDC assembles `closing-report.md`; a fresh independent context or the Operator records the composition gate with attribution in that report or the project's existing gate record. | `crc-verification.md`: operational/composition evidence and readiness. `cdc-verification.md`: independent composition/design gate reviewing that evidence and the assembled close. |
| Project | CDC assembles `closing-report.md`; the Operator plus independent review records the DoD gate with attribution in that report or the project's existing gate record. | `crc-verification.md`: operational/system acceptance evidence and readiness. `cdc-verification.md`: independent DoD/design gate. Operator acceptance remains separately explicit. |

In the Operator-selected One-Contributor Workflow, ordinary non-ledgered tasks
use the completion report, not verification-role files or a newly invented
planning tree. Existing ledgered tasks keep their records: document self-checks
as attested in the closing report, with any required independent gate pending
until actually performed and attributed to its reviewer. Do not generate a CDC
or CRC verification record that presents the implementer's self-review as
independent. A recorded filename override cannot weaken the evidence contract.

Create records only when review occurs, not as pre-filled success artifacts.
The three-contributor arc/project records are complementary, not two approvals
of the same report. CRC's own assembly or demonstration remains doer-attested
until independently checked by CDC; pointers to accepted children do not prove
composition. Both records identify scope, source/plan state, author role/context,
checks, evidence strength, unresolved findings, and verdict. Closure requires
both records to address the same current candidate, dispositioned findings,
and the required independent and Operator gates, not merely both files existing.
Link them from the owning ledger and closing report. See
[independent verification](../../work-verification/guides/05-independent-verification.md).

### Verification filename compatibility

Existing `cdc-verification.md` files, historical links, and project conventions
remain valid. Workflow transitions do not rename or relabel historical evidence.
For new review after a transition, record the role-specific active path in the
plan and link the preceding record, its source state, and the scope superseded
by the new review. Do not leave two competing current slice verdicts or copy
old acceptance into a new role's file. Explicit project filename overrides
remain valid when recorded. Examples describing past work retain their names.

### Slice iteration filenames and preservation

The initial assignment is `cc-prompt.md`. Each follow-up assignment gets a
new file beside it: `cc-prompt-iteration01.md`, then
`cc-prompt-iteration02.md`, with a two-digit, increasing suffix. `01` means
the first refinement after the initial assignment. Create a file only when
there is a concrete assignment; do not pre-create empty iteration prompts.
Keep the slice's existing plan and ledger: an iteration is a pass inside the
same slice, not another directory or planning scale.

**Once a prompt is issued to CC, preserve its contents and path.** Drafts may
be edited before handoff. Corrections or changed instructions after handoff
belong in the next numbered prompt, even if CC has not started. Do not overwrite
or append new work to an issued prompt, recycle a used number, rename the
initial prompt, or turn `cc-prompt.md` into a mutable "latest" copy or symlink.
Git history alone does not make reuse safe: the handoff path must distinguish
the new assignment from the old one.

All CC assignments are first-class slice documents in the slice root. Do not
put iteration prompts in `artifacts/`, `prompts/`, an iteration subdirectory,
or a session directory. A different home for supporting artifacts does not
change prompt placement. Any operator-approved prompt naming/layout override
must be recorded explicitly in project instructions.

For an existing slice with noncanonical or reused prompt paths, preserve the
historical evidence and record the discrepancy and existing sequence in
`slice-plan.md`. Use the next unused canonical path for new work unless an
explicit project override applies. Do not silently relocate, renumber, or
reconstruct previously issued prompts. See
[Issuing and executing an iteration](./03-planning-top-down.md#issuing-and-executing-an-iteration)
for the current-assignment record and handoff requirements.

---
