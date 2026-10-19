## Purpose

Improve the operational reliability of Autonomous Mode while strengthening both ledger discipline and the usefulness of its records for research months or years later.

A recent multi-slice pilot delivered independently reviewed candidates and passing composed CI. Direct contributor handoffs and small commits worked well. The run also accumulated avoidable planner errors, validation plumbing repairs, shared-worktree interference and manual status reconciliation. The Operator reported similar feedback from another session: use a short reliable preflight, keep evidence in one authoritative place, and default to one implementer plus one independent reviewer.

These are observations motivating a proposal, not a controlled demonstration that Autonomous Mode is faster or cheaper. The second session has not been independently audited here. Implementation of the proposals below remains subject to normal planning, review and Operator authority.

## Non-negotiable constraints

**Ledger discipline must retain its full effectiveness. Long-term record quality must improve.** This is not a request to minimize evidence, shorten required reading, remove records or relax verification.

- Preserve every acceptance row, its meaning, origin, verification route, disposition, evidence strength and actual verifier; retain slice, arc and project composition gates.
- Preserve independent verification, explicit deferrals/no-ops, unresolved findings, iteration limits, bubble-up, closing records, retrospectives and Operator gates.
- Preserve original inputs, issued prompts/iterations, relevant instructions, revisions, environments, commands, outputs, failed attempts, decisions and independent observations. Matching outputs do not make two observations interchangeable.
- Keep original observations attributable and unchanged. New interpretations and corrected summaries must identify what they supersede without rewriting earlier evidence into success.
- Support future reconstruction, challenge and reanalysis after conversation context, local worktrees or CI artifacts are unavailable. Expiring hosted logs cannot be the sole copy of required evidence.
- Respect confidentiality, permissions and secret-handling rules. Preserve authorized evidence durably; disclose necessary redactions, missing inputs and resulting limits rather than manufacturing completeness.

Existing foundations already cover much of this: [Autonomous Mode](https://github.com/billosys/ai-engineering/blob/f2b1137a3f3d77b0d34d789c2233b48f4dcb15ff/knowledge/engineering-methods/guides/01-engineering-methodology.md#L326-L450), [ledger discipline](https://github.com/billosys/ai-engineering/blob/f2b1137a3f3d77b0d34d789c2233b48f4dcb15ff/knowledge/work-verification/guides/01-ledger-discipline.md), and [evidence during correction review](https://github.com/billosys/ai-engineering/blob/f2b1137a3f3d77b0d34d789c2233b48f4dcb15ff/knowledge/work-verification/guides/05-independent-verification.md#L79-L105). The improvement is to make those contracts easier to execute reliably, with better provenance and fewer conflicting current accounts.

## Observations motivating the changes

The reviewed pilot included:

- Planner assumptions that later needed repair: an unavailable image tag, a deprecated API rejected by repository lint, a guessed dependency-change population, and overbroad graph wording.
- Real validation failures caused by path quoting, an incorrect executable path, Bash syntax under `sh`, and successful commands that selected zero tests.
- Installation/generation mutating a tree during package loading or scanning; one command without an explicit Make target invoked the default build.
- Independent review successfully distinguishing installed package bytes from audit metadata and exposing finding identities previously hidden behind category counts.
- Strong raw evidence preservation accompanied by repeated manual summaries that required later corrections or explicit supersession.
- A CI publication job reporting success before the manual deployment gate. Automatic pipeline effects need to be included when establishing action authority; a successful job status alone is not a complete audit of its external effects.
- The same configured model and reasoning setting across contributor contexts. There is no measured basis here for a model-routing or cost-efficiency conclusion.

These observations include coordinator/author mistakes. They should not be attributed solely to implementers or model capability.

## Proposed improvements

### 1. A short, verifiable run contract and preflight

Use an entrypoint into the existing canonical plan, rather than requiring another competing planning tree. Before dependent work, establish:

- Explicit worktree, branch, revision and relevant clean/dirty state; identify preexisting changes and protected paths.
- Authorized scope and endpoint, current assignment/ledger, applicable instruction sources and revisions, allowed mutations and mandatory gates.
- Actual implementer, independent reviewer, workspace ownership, decision rights, unresolved approvals and next-action owner.
- Explicit Operator-confirmed model assignments and expenditure boundaries for those roles, under the mandatory model-selection gate below.
- Separate authority for commits, pushes/PRs, merge, publication and deployment. Inspect automatic CI effects before triggering them.

Short means compact presentation with complete backing evidence. Required domain reading, source inspection and contract readback remain in force. Revalidate changed facts after handoff, rebase or context recovery; retain earlier observations and record the delta. Static facts can be referenced when their continued applicability is established.

### 2. Default to one implementer and one independent reviewer

Make the Two-Contributor arrangement the operational default inside Autonomous Mode for substantive work. CDC may coordinate and review another context's implementation. If CDC implements or repairs substantive work, a separate context owns the affected independent verdict.

Add another contributor for a named risk, a bounded investigation, a safely separable workstream or a separation-of-authorship requirement. Record its scope, ownership, return contract and exit condition. Availability of spare contexts is not itself a reason to add them.

Preserve authorized adaptation, Three-Contributor arrangements and the existing limited One-Contributor exception. Reassignments retain findings, evidence and iteration counts. Different model names do not establish independent verification.

### 3. Mandatory Operator selection of models by role

Autonomous Mode must explicitly prompt the Operator for the model assignments before dispatching Autonomous role work. Treat the answer as a required execution gate because it affects expenditure. General authorization to use Autonomous Mode, a recorded default, a parent model or the runtime's inherited configuration is not an answer to that prompt.

The prompt should enumerate the roles actually planned for the run: coordination/planning, implementation and independent review, plus investigation or integration when separately assigned. Obtain an explicit role-to-model mapping, including provider/deployment and reasoning/effort settings where selectable. Proposed defaults may make the decision easier, but require explicit confirmation. The Operator may deliberately choose the same model for every role. Keep the framework model/provider-agnostic; available runtime capabilities constrain executable choices without silently selecting a substitute.

Also ask about the applicable expenditure boundary: a spend limit, an approval threshold or an explicitly chosen absence of a cap, with authorized concurrency where relevant. State which controls the runtime can actually enforce. Use current, sourced estimates only when available; distinguish estimates from measured charges, and mark unknown pricing/usage as unknown. Do not promise a hard spending cap when the execution environment cannot enforce one.

Record the response, its scope and the approved role/provider/model/settings mapping in the canonical run record before dispatch. Validate requested choices against available controls; record requested configuration and reported execution identity separately. If the selection cannot be honored or cost-relevant settings cannot be established, pause the affected role and ask rather than silently inherit, substitute or proceed with an unresolved assignment.

Carry this approval through its explicitly authorized scope. Model/provider substitutions, reasoning changes, concurrency increases or expenditure beyond that scope require renewed approval unless the Operator already authorized a precise bounded selection/escalation policy. CDC's adaptive staffing authority does not confer unrestricted spending authority. Preserve every mapping revision and the actual settings observed for each contributor so subsequent research can relate outcomes to expenditure and model allocation.

### 4. Establish the real execution substrate early

Preflight the consequential prerequisites before prescribing implementation: exact published package/image availability, repository lint/API constraints, actual shell, runtime selection, configuration paths and required real services.

Use repository-native commands with explicit targets and space-safe paths. Record selected-test identities/populations; distinguish a genuine pass from zero selected tests, loading failure, timeout or a blocked command. Exercise the actual caller boundary and final consumer where that boundary matters, including credible negative cases through the real tools.

Build the actual assembled image early when it is a delivery gate. Preserve no-mock discipline. Existing controls should establish the required property where adequate; a new harness or general validator needs its own justified scope, review and maintenance decision.

### 5. Give mutable worktrees explicit ownership

Assign one mutation owner per worktree. Serialize installations, generation, source changes and any loader/scanner that depends on a stable tree. Read-only operations are compatible only when concurrent mutations cannot invalidate their inputs. Use separate worktrees for genuinely independent mutable work.

Record ownership handoffs and source state before dependent checks. Name the integration/index owner. Inspect actual deltas before staging; preserve others' changes and outputs of unknown ownership. Preview explicit Make targets before introspection/build commands with possible side effects, and establish output ownership before cleanup.

### 6. One authoritative evidence home per batch, with full ledger traceability

A batch is a grouping/index for observations, not a replacement for project/arc/slice units or ledgers. Use the existing canonical artifact homes or an explicitly approved override. Slice decisions, review records and higher-scale ledgers should link to exact evidence entries rather than transcribe competing copies of their facts.

Retain complete original observations once in an authorized durable store, with stable references. Each entry should identify, where applicable:

- Claim/ledger row, assignment, author/context, role and independent-review relationship.
- Input/source revision and relevant working-tree state, instruction/skill revisions and actual read/query scope.
- Provider and requested model/settings, reported execution identity where available, inheritance/overrides and relevant tool versions; explicitly mark unavailable fields.
- Exact command and environment prerequisites, timestamps/timezone, exit status, stdout/stderr and selected-test/scan population.
- Input/output hashes and their derivation, including query/script versions and source locations for generated counts or projections.
- Findings, decisions, corrections, re-entry conditions, approvals and links to original and superseding observations.

Generate mechanical facts from actual execution; retain the derivation. Structured projections and compressed lossless archives are useful only when the original observations remain recoverable and independently inspectable. Checksums establish integrity, not correctness or verification independence.

Preserve separate runs even when their outputs match. Keep one clearly identified current interpretation, with a dated/revisioned history. Avoid introducing per-file ceremony or blanket collection of unrelated data; capture what supports verification and future research, and disclose limits. Fewer files or tokens alone is not evidence of improvement.

### 7. Derive acceptance populations and expose semantic distinctions

Use complete relevant inventories and real dependency/tool resolution before binding an assignment to guessed counts or version lists. Record how the population was selected, including hidden tracked files, build tags/platforms and test dependencies where relevant. Distinguish selected coverage from full coverage.

Keep separate claims for declared requirements, dormant upstream metadata, selected/imported packages, scanner categories, installed bytes, hosted CI and integrated/deployed state. A passing weaker claim cannot discharge a stronger ledger row.

When evidence reveals that the plan or acceptance criterion is wrong, preserve it, explain the discrepancy and obtain the required amendment. Never adjust evidence selection, quietly broaden scope or weaken criteria to make an existing result pass.

### 8. Make review, evidence retention and integration explicit

Preserve all independent review and higher-scale composition obligations. Reuse earlier reproduced evidence only under the existing correction-review contract: original claim/state/method/result remain identifiable, relevant inputs and conditions remain applicable, no finding undermines the proof, and no gate requires fresh execution. Record the applicability judgment separately from newly executed checks. Live-state checks need fresh observations when required.

Consolidate related reviewer feedback before issuing the next durable iteration when practical, while surfacing consequential new defects immediately. Separate preexisting defects, new discoveries, planner errors, implementation regressions and verification-method failures. A passing rerun alone does not establish the cause of an earlier failure.

For stacked delivery, record exact parent boundaries, reviewed heads, old/new ranges and applicable checks in the run's current view. Refresh review/CI for changed candidates as required. Candidate acceptance, publication, main integration, operational acceptance and external warning closure remain distinct states. Follow the target repository's authorized integration policy.

### 9. Evaluate the changes against quality and research usefulness

Start with guidance/templates and existing tools, then a bounded Operator-approved real trial. Proposed observations:

- Complete ledger coverage, explicit dispositions, independent reproduction and higher-scale composition; any weakened or lost guarantee is a failure.
- A fresh reader can reconstruct an actual failed attempt, its repair, the final accepted candidate and the reasons for decisions using retained authorized records without relying on chat memory or expired hosted logs.
- Every current summary claim reaches attributable evidence; distinct runs and original identities remain distinguishable.
- Record actual operator interruptions, coordination failures, correction causes, repeated checks and time/usage by role when available. Distinguish necessary validation, justified new scope and avoidable rework.
- Record confidentiality constraints and reconstruction limits; assess current record access/portability rather than claiming that a short trial proves multi-year durability.

If comparing workflows or model allocations, predeclare the comparison, hold scope/quality gates constant where feasible and report confounds. Do not infer causal performance or cost gains from these sessions, invent missing usage data, or reduce research records to improve a metric. Revisit recommendations at the next relevant close and retain, revise or retire them explicitly.

## Suggested ownership and implementation sequence

This is one improvement initiative with independently reviewable component changes, rather than a request for one broad patch:

| Concern | Owning component / existing pattern |
| --- | --- |
| Run authority, mandatory role/model approval, expenditure boundaries, staffing default and transitions | [engineering-methods](https://github.com/billosys/ai-engineering/blob/f2b1137a3f3d77b0d34d789c2233b48f4dcb15ff/knowledge/engineering-methods/guides/01-engineering-methodology.md#L326-L450), [agent-coordination](https://github.com/billosys/ai-engineering/blob/f2b1137a3f3d77b0d34d789c2233b48f4dcb15ff/knowledge/agent-coordination/guides/01-when-to-delegate.md#L13-L29) |
| Preflight, assignment readiness and workspace ownership | engineering-methods prompt-authoring; agent-coordination contributor packets |
| Evidence homes, durable handoffs and current status | project-management; existing ledger/verification filenames and approved artifact-home overrides |
| Row traceability, independent review and retained evidence | work-verification; existing evidence-strength and correction-review contracts |
| Real commands, selected-test populations and final consumers | testing; native validation and release gates |
| Retrospective follow-through and evaluation | [methodology-stewardship](https://github.com/billosys/ai-engineering/blob/f2b1137a3f3d77b0d34d789c2233b48f4dcb15ff/knowledge/methodology-stewardship/guides/01-retrospectives-and-follow-through.md#L116-L149), scientific-methods; laboratory-recordkeeping where archival organization is needed |

First agree the strengthened invariants and component boundaries; then make narrow guidance/template changes, validate source/package routes under repository policy, and evaluate a real bounded run. Preserve historical projects and issued records. Any adoption/migration needs an explicit mapping and provenance; avoid retroactive rewrites or a parallel acceptance system.

## Acceptance criteria for this improvement

- [ ] Ledger discipline, independent verification, composition, closure and Operator gates are explicitly preserved in all affected guidance.
- [ ] A complete, usable preflight/authority contract and two-contributor default exist, with bounded staffing exceptions and CI side effects addressed.
- [ ] Autonomous dispatch is blocked until the Operator explicitly answers the role/model/settings and expenditure prompt; inherited/default choices cannot silently satisfy it, unavailable choices pause affected work, and out-of-scope changes require approval.
- [ ] Workspace ownership and stable-input sequencing cover installations, generation, loaders/scanners, staging and cleanup.
- [ ] The evidence model preserves original failed/successful attempts, independent observations, provenance and future research utility; no batch summary replaces required ledger or review records.
- [ ] Mechanical counts/hashes are derived reproducibly; unavailable runtime/model/usage fields and proof limitations are explicit.
- [ ] Retained versus newly executed evidence and candidate versus integrated/external states are unambiguous.
- [ ] Existing canonical layouts, issued prompts and historical records remain intact; affected component routes, packages and skill metadata/history pass repository-required checks.
- [ ] A bounded real evaluation documents reconstruction quality, ledger coverage, operational effects and limitations, with independent review of substantive changes and recorded Operator decisions.

The preferred result is stronger execution and better research records. Specific template or tool choices can remain proportionate to the work; this issue does not authorize weaker evidence, automated acceptance or a scope expansion in an active run.

