# CC Prompt: Slice 04 Arc01 Synthesis for Directory Contract

You are CC for Project04 Arc01 Slice04,
`slice04-arc01-synthesis`, in the ai-engineering planning worktree.

## Before You Start

If the Slice04 opening packet is staged when you begin, commit exactly those
staged files before doing the slice work. Do not stage or commit unrelated
files. Use the repository commit trailers:

```text
Co-authored-by: Codex <noreply@openai.com>
Co-authored-by: Billo AI <ai-engineering@billo.systems>
```

Read, in order:

1. `project04-knowledge-library-reorg/project-plan.md`
2. `project04-knowledge-library-reorg/ledger.md`
3. `project04-knowledge-library-reorg/arc01-material-inventory/arc-plan.md`
4. `project04-knowledge-library-reorg/arc01-material-inventory/ledger.md`
5. `project04-knowledge-library-reorg/arc01-material-inventory/slice04-arc01-synthesis/slice-plan.md`
6. `project04-knowledge-library-reorg/arc01-material-inventory/slice04-arc01-synthesis/ledger.md`
7. The verified Slice01, Slice02, and Slice03 `cdc-verification.md` files.

Then read the Slice01, Slice02, and Slice03 artifacts referenced by the
Slice04 plan and ledger.

## Objective

Synthesize Arc01's verified evidence into an Arc02-ready packet. Your output
should tell CDC and the operator what Arc02 can now decide, what it must
preserve, what remains unresolved, and what validation gates later
implementation arcs must satisfy.

This is a planning-only synthesis slice. Do not edit the source checkout.

## Required Outputs

Create these artifacts under
`arc01-material-inventory/slice04-arc01-synthesis/artifacts/`:

- `arc02-readiness-packet.md`
- `directory-contract-requirements.md`
- `arc01-synthesis-decision-register.md`

Update only:

- `arc01-material-inventory/slice04-arc01-synthesis/ledger.md`
- `arc01-material-inventory/slice04-arc01-synthesis/closing-report.md`
- the three required artifacts above

Do not update parent arc or project files; CDC will do that after independent
verification.

## Required Content

Your synthesis must:

- consume verified Slice01, Slice02, and Slice03 evidence rather than relying
  on memory or summary;
- distinguish current source-backed facts, Project02 accepted facts, Project02
  implementation-plan hypotheses, Project03 planned method-skill facts,
  unresolved Arc02 decisions, risks, validation obligations, and re-entry
  conditions;
- preserve the operator's `docs/` versus `knowledge/` distinction:
  `docs/` should document the repository's materials, while `knowledge/`
  should hold the raw and derived knowledge-library substrate where the
  accepted directory contract says it belongs;
- preserve the accepted Project02 fact that `collaboration-framework` remains
  the daily-driver composite composer over specialist components;
- preserve Project03's `concept-card-method` as planned method-skill input,
  not live source;
- preserve CCDP as a separate protocol/package surface unless a later protocol
  package decision reopens that policy;
- keep skill kind and topology independent: do not equate domain/tooling with
  atomic or framework/operational with composite;
- preserve the external ontology rubric as tested input, not final public
  taxonomy;
- prepare Arc01 composition evidence for formal arc close without claiming that
  Arc01 is closed.

## Verification

Run every Verify command in `ledger.md` from
`arc01-material-inventory/slice04-arc01-synthesis/`.

Also run:

```sh
git -C /Users/oubiwann/lab/billosys/ai-engineering status --short
git -C /Users/oubiwann/lab/billosys/ai-engineering/.worktrees/planning diff --check
```

Expected source checkout result: no output.

## Close

When finished:

1. Update the Slice04 ledger with `attested` evidence for every done row.
2. Write `closing-report.md` with a per-row ledger walk, artifact inventory,
   verification run, bubble-up to Arc01, silent-drop diff, and What Worked
   section.
3. Leave Slice04 as `proposed-done` pending CDC verification.

Do not create `cdc-verification.md`; CDC owns that file.
