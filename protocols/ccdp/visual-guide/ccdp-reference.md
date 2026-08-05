# CCDP Visual Guide — Reference Document

> This document provides all the copy, terminology, relationships, and
> compare/contrast material that needed to build an interactive
> visual guide to the Composite Cognition Dispatch Protocol (CCDP). Every
> claim here comes directly from the v0.2 specification.

---

## Section 1: Friendly Overview (for the landing/hero view)

### One-liner

CCDP is a protocol that routes cognitive work to the right tool for the job —
and stamps every answer with how much you should trust it.

### Elevator pitch (2–3 sentences)

When you ask an LLM a question, it does everything itself — drafts, reasons,
calculates, checks — and you get one answer with no way to tell which parts
are rock-solid and which are educated guesses. CCDP splits that work up: a
central Dispatcher reads the envelope (never the content), routes each piece
to a specialist — a theorem prover, a planner, a database, an LLM, a human
reviewer — and every answer comes back with a provenance grade saying exactly
how strong the evidence behind it is. If a piece can't meet the quality bar,
it escalates up the chain instead of quietly getting it wrong.

### The core insight (one sentence)

Cognitive outputs are claims with epistemic status, not just data — and a
protocol that carries that distinction lets you build reliable systems from
unreliable parts.

---

## Section 2: Conceptual Component Diagram

### Components (for the diagram)

**Human Supervisor** — sits at the top of the supervision tree. Provides
specification, value judgment, and the faculties no machine has yet. The
escalation chain terminates here. Provenance grade when a human signs off:
HUMAN_ATTESTED (the ceiling).

**Dispatcher** — the constrained coordinator at the center of the star. Reads
envelopes, never content. Routes requests, enforces schemas, logs audits,
monitors health, enforces deadlines, handles escalation. It is deliberately
*not* intelligent — it's a protocol enforcement engine, like a network switch
that reads headers and forwards packets.

**Capability Registry** — the source of truth for what Services exist, what
they can do (typed contracts with JSON Schemas for input/output), their cost
hints, health endpoints, provenance capabilities, and schema versions. The
Dispatcher consults it for every routing decision.

**Services** — the heterogeneous cognitive workforce behind the Dispatcher.
All expose the same typed interface; all are interchangeable from the
Dispatcher's perspective. Four implementation modes:

- **Mode 1: LLM alone** — language generation, summarization, translation.
  Typical grade: ASSERTED or HEURISTIC. The language organ — superb at
  understanding and generation, structurally unreliable at deduction or
  planning without external checks.
- **Mode 2: Deterministic engine** — theorem provers (Z3, Lean, Coq),
  planners, databases, calculators. Typical grade: COMPUTED or
  FORMALLY_VERIFIED. Correct by construction given correct input.
- **Mode 3: LLM + engine composite** — the architecturally significant
  pattern. An LLM translates natural language into formal input, an engine
  processes it, the LLM translates the output back. "LLM proposes, engine
  disposes." Typical grade: VALIDATED or FORMALLY_VERIFIED depending on
  translation confidence.
- **Mode 4: Human queue** — expert review behind the same typed interface.
  Slower, more expensive, highest trust. Typical grade: HUMAN_ATTESTED.

**Decomposition Service** — a special Mode 3 service with capability type
`org.ccdp.decomposition`. Receives complex requests, emits structured
Decomposition Plans (sub-requests, dependency DAGs, composition rules). The
Dispatcher executes the plan structurally — it never reasons about the
content.

### Topology

Star topology with the Dispatcher at center. All inter-service communication
goes through the Dispatcher. No direct service-to-service links. This avoids
O(N²) communication explosion and gives a single point of protocol
enforcement.

```
              Human Supervisor
                    |
                    | (escalation, oversight)
                    |
              +-----------+
              | DISPATCHER |
              +-----------+
             /   |   |   |  \
            /    |   |   |   \
          LLM  Z3  Planner Human  DB
         (M1) (M2)  (M3)  (M4)  (M2)
```

### Key relationships to show

- Requests flow IN to Dispatcher, get routed OUT to a Service.
- Responses flow back through Dispatcher to the requester.
- Every hop generates an audit record (mandatory).
- Escalations flow UP toward the Human Supervisor.
- The Registry is consulted for every routing decision.
- The Dispatcher reads envelopes (metadata), never content (payload).

---

## Section 3: Protocol Layer Stack

Four layers, bottom to top:

| Layer | Name | Analog | What it does |
|-------|------|--------|-------------|
| 1 | Transport | TCP/IP Transport + Link | HTTP, JSON-RPC 2.0, TLS, authentication (mTLS, bearer tokens) |
| 2 | Routing & Audit | Internet/Network | Capability-type routing, registry lookups, trace/span IDs, mandatory audit, deadline propagation, health monitoring |
| 3 | Epistemic | *No TCP/IP analog — CCDP's novel layer* | Provenance grades and evidence, escalation semantics, decomposition plans, cost and resource signals |
| 4 | Content | Application | Service-specific input/output, schema-governed by capability records, opaque to the Dispatcher |

**Key point for the visual:** Layer 3 (Epistemic) is what makes CCDP
different from every existing protocol. It's the layer that carries "how much
should you trust this answer" as a first-class protocol field. Color it
distinctly.

---

## Section 4: Provenance Grade Ladder (the showpiece)

Eight grades, weakest to strongest. Use a vertical ladder or stacked bar
visual. Color-code by category.

### Category: Unbacked claim (neutral/gray)

**Grade 0: OPAQUE** — basis unknown. No provenance information available. The
floor. Treat with maximum skepticism.

**Grade 1: ASSERTED** — the service stated it, no backing. Raw LLM output,
unvalidated opinion. Confidence without verification is assertion.

### Category: Machine-verified (green/teal)

**Grade 2: HEURISTIC** — an educated guess with some signal. Statistical
model output with confidence scores, classifiers with measured precision/recall.
Carries *quantified uncertainty*, unlike ASSERTED.

**Grade 3: COMPUTED** — output of a deterministic engine. Given the same
inputs, any correct implementation gives the same result. Database queries,
arithmetic, hashing. The computation isn't in question; only the inputs are.

**Grade 4: VALIDATED** — checked by a sound external validator. Code that
passes a test suite, a plan accepted by a validator, translation verified by
back-translation. The checker is independent of the producer.

**Grade 5: CROSS_CHECKED** — independent services agree on the result.
Multiple different methods, different implementations, no shared state. Full
independence required (not replicas). Agreement across independent processes
catches errors no single validation would.

**Grade 6: FORMALLY_VERIFIED** — proven correct against a stated spec.
Machine-checkable proof available (Lean, Coq, Z3). Carries a `scope` field
binding it to a specific specification. The spec-recursion caveat: "correct
relative to this spec" — whether the spec captures intent is a separate
question.

### Category: Human judgment (warm/salmon)

**Grade 7: HUMAN_ATTESTED** — a person reviewed and signed off. The ceiling.
Domain expert with verified identity. Highest grade because the
spec-recursion problem terminates at human judgment — someone must decide
whether the specification captures intent.

### Composition rules (for tooltips or a sub-view)

- **Sequential (weakest link):** Chain A→B→C: composed grade = min(A, B, C).
  The chain is only as strong as its weakest link.
- **Parallel (cross-check upgrade):** Independent services agree:
  composed grade can upgrade to CROSS_CHECKED if independence is confirmed.
- **Decomposition:** Considers three factors: decomposition plan grade,
  sub-result grades, composition step grade. Composed = min of all three.

### Signaling theory connection (for a callout)

Each grade costs more to fake than the one below it (Spence signaling theory).
An LLM can cheaply assert anything (ASSERTED), but producing a
machine-checkable proof (FORMALLY_VERIFIED) requires actual computation that
can't be faked without doing the work.

---

## Section 5: Example Deployment Architecture

### Scenario: "Enterprise AI Platform"

A company deploys CCDP to handle mixed cognitive workloads — legal analysis,
code generation, data retrieval, planning.

**Components:**

- **Dispatcher** — central routing engine, no cognitive capability
- **Registry** — PostgreSQL-backed capability store
- **Human Supervisor** — the compliance team, reachable via a review queue

**Services:**

| Service | Mode | Capability Types | Typical Grade | Cost |
|---------|------|-----------------|---------------|------|
| Claude (LLM) | Mode 1 | `org.ccdp.language.generation`, `org.ccdp.language.translation` | ASSERTED | $0.01–0.50/req |
| Z3 Prover | Mode 2 | `org.ccdp.deduction` | FORMALLY_VERIFIED | $0.001/req |
| OptaPlanner | Mode 2 | `org.ccdp.planning` | COMPUTED | $0.01/req |
| Code Verifier (LLM + test runner) | Mode 3 | `org.ccdp.code.verification` | VALIDATED | $0.10/req |
| Legal Review Queue | Mode 4 | `org.ccdp.legal.compliance` | HUMAN_ATTESTED | $50/req, 2 days |
| Decomposition Service (LLM + validator) | Mode 3 | `org.ccdp.decomposition` | VALIDATED | $0.05/req |
| PostgreSQL | Mode 2 | `org.ccdp.data.retrieval` | COMPUTED | $0.0001/req |

**Request flow example:** "Generate a legally compliant privacy policy for
our new product."

1. Request arrives at Dispatcher with `capability_type: org.ccdp.decomposition`.
2. Decomposition Service splits it: (a) retrieve relevant regulations from DB,
   (b) generate draft policy text from LLM, (c) verify legal compliance via
   Legal Review Queue.
3. Dispatcher routes sub-request (a) to PostgreSQL → grade: COMPUTED.
4. Dispatcher routes sub-request (b) to Claude → grade: ASSERTED (depends on
   result of (a)).
5. Dispatcher routes sub-request (c) to Legal Review Queue → grade:
   HUMAN_ATTESTED.
6. Composed result: min(VALIDATED [decomp], COMPUTED, ASSERTED, HUMAN_ATTESTED)
   = ASSERTED.
7. But the legal compliance *check* is separately tracked at HUMAN_ATTESTED —
   the consumer can inspect the composition trace to see which parts to trust.

---

## Section 6: Compare/Contrast Views

### Instructions for CD

Each view shows the same request handled two ways: "Plain LLM" on the left,
"Through CCDP" on the right. The left side shows what happens when you just
ask an LLM. The right side shows what CCDP adds. Use a consistent layout:
a shared request at the top, two columns below, and a takeaway line at the
bottom.

### Intro text (before the first compare/contrast view)

> The following views trace through CCDP's big ideas in the order they appear
> in the specification. Each one shows the same request sent two ways — to a
> plain LLM on the left, and through a CCDP system on the right. The
> difference isn't that the LLM is bad. It's that the LLM alone can't tell
> you *which parts of its answer you can trust* — and CCDP can.

---

### View 1: The Core Problem — Claims vs Data (§3 Introduction)

**Request:** "Is this contract clause enforceable under California law?"

**Plain LLM:**
- Reads the clause, generates a confident legal analysis.
- Sounds authoritative. Cites cases. May hallucinate citations.
- No way to distinguish "I looked this up" from "I pattern-matched from
  training data."
- grade: ASSERTED
- *You get an answer that reads like a lawyer wrote it. But a lawyer didn't.*

**Through CCDP:**
- Envelope: `capability_type = org.ccdp.legal.analysis`,
  `min_policy_grade = VALIDATED`.
- Dispatcher routes to a Mode 3 service: LLM drafts analysis, legal database
  cross-references the cited cases, validator checks citations exist.
- Response carries grade: VALIDATED, with evidence entries listing each
  verified citation.
- If the analysis can't meet VALIDATED, it escalates to a human lawyer
  instead of guessing.
- *You get an answer with a receipt — and if it can't back up its claims, it
  says so.*

**Takeaway:** Cognitive outputs are claims, not data. CCDP makes the evidence
strength a first-class protocol field so you can tell the difference.

---

### View 2: Routing — Who Decides Where Work Goes (§9 Routing)

**Request:** "Translate this contract from English to Japanese, then verify
the translation preserves legal meaning."

**Plain LLM:**
- Does everything itself. Translates, then self-reviews.
- No independent check — it's grading its own homework.
- If it's bad at legal Japanese, you won't know until a human reads it.
- *The same brain that made the mistake is the one checking for mistakes.*

**Through CCDP:**
- Dispatcher reads the envelope: `capability_type = org.ccdp.language.translation`.
- Queries the Registry: 3 translation services registered, filters by health
  (1 unhealthy), deadline (1 too slow), provenance (picks the one with
  `max_grade: CROSS_CHECKED`).
- Routes to best candidate. Translation comes back. Dispatcher routes
  verification to an independent back-translation service.
- 7-step routing algorithm: explicit destination → capability lookup →
  health filter → deadline filter → provenance filter → cost-aware ranking →
  selection and logging.
- *Every routing decision is logged. The Dispatcher never reads the Japanese —
  it reads the envelope.*

**Takeaway:** Routing by typed envelope metadata, not by content
understanding. The Dispatcher is a network switch for cognitive work.

---

### View 3: Provenance Grades — The Trust Ladder (§10 Provenance)

**Request:** "Give me a valid 2-week on-call rota for 4 engineers: nobody on
two weekends running, Ana can't take Mondays, every shift needs a senior,
max 3 shifts each."

**Plain LLM:**
- Reads the prompt, generates a rota that looks right.
- States it satisfies every rule.
- No independent check — it's grading its own homework.
- grade: ASSERTED
- *Plausible, but may quietly break a constraint — and it sounds just as
  confident either way. You can't tell without checking by hand.*

**Through CCDP:**
- Envelope: `capability_type = org.ccdp.planning`,
  `min_policy_grade = FORMALLY_VERIFIED`.
- Dispatcher routes to a constraint solver — never reads the rota itself.
- Solver returns a rota that provably meets every rule, or UNSAT if none
  exists.
- Can't finish in the deadline? It escalates to a human instead of guessing.
- grade: FORMALLY_VERIFIED
- *Either a rota you can trust, or an honest "no valid rota exists" / handed
  to a person. Never confident-but-wrong.*

**Takeaway:** The same answer, but one tells you how much to trust it. That's
the difference between ASSERTED and FORMALLY_VERIFIED.

---

### View 4: Escalation — What Happens When It Can't (§13 Error Handling)

**Request:** "Verify this cryptographic implementation is constant-time."

**Plain LLM:**
- Reads the code. Generates a confident analysis: "Yes, this implementation
  appears to be constant-time."
- Doesn't actually run timing analysis. Can't — it's a language model.
- If it's wrong, the vulnerability ships.
- *The most dangerous kind of wrong: confident and plausible.*

**Through CCDP:**
- Request: `min_policy_grade = FORMALLY_VERIFIED`,
  `required_methods = ["formal_verification"]`.
- Dispatcher routes to a timing-analysis service.
- Service runs, finds it can't produce FORMALLY_VERIFIED (the code is too
  complex for its analysis window).
- Returns ESCALATION with reason `PROVENANCE_BELOW_REQUIREMENT`, achieved
  grade: VALIDATED, partial result attached.
- Dispatcher walks the escalation chain → routes to a human security
  reviewer.
- *Instead of a confident wrong answer, you get an honest "I couldn't fully
  verify this" plus the partial work, routed to someone who can finish it.*

**Takeaway:** Escalation is a first-class protocol operation, not an error.
"I can't meet the quality bar" is the right answer when the alternative is
silently getting it wrong.

---

### View 5: Decomposition — Breaking Complex Work Apart (§14 Decomposition)

**Request:** "Build the on-call rota, then write the announcement email."

**Plain LLM:**
- Does both tasks in one pass.
- The rota might have constraint violations. The email will confidently
  describe whatever rota was generated.
- No separation between the rules-puzzle part and the writing part.
- *If the rota is wrong, the announcement is wrong too — and both sound
  equally confident.*

**Through CCDP:**
- Decomposition Service splits the request into two typed sub-requests:
  (a) `org.ccdp.planning` — build the rota (→ constraint solver, grade:
  FORMALLY_VERIFIED); (b) `org.ccdp.language.generation` — write the email
  (→ LLM, grade: ASSERTED). Sub-request (b) depends on (a).
- Dispatcher holds the email sub-request until the solver returns.
- Solver returns a provably valid rota. Dispatcher feeds the verified rota
  into the LLM's email prompt.
- Composed result: the rota half is bulletproof, the email half is flavor.
  Overall grade: ASSERTED (weakest link). But the composition trace shows
  which half is which.
- *You know precisely which part to trust and which to just enjoy.*

**Takeaway:** Decomposition routes each piece to the right tool. The
composition trace preserves per-piece trust — you don't lose the solver's
guarantee just because an LLM wrote the email.

---

### View 6: Audit Trail — What Got Logged (§11 Audit Trail)

**Request:** "Summarize the patient's medical history for the consulting
physician."

**Plain LLM:**
- Generates a summary. Hopefully it's accurate.
- No structured record of what data sources were consulted, what was
  included, what was omitted.
- If something goes wrong, reconstruct from chat logs — if they exist.
- *Three months later: "Why did the summary omit the allergy?" Nobody knows.*

**Through CCDP:**
- Every message through the Dispatcher generates a structured audit record:
  timestamp, trace_id, span_id, message type, routing decision (which
  service, why, what alternatives were considered), validation status,
  provenance summary, timing.
- The audit trail is mandatory — it's a core protocol requirement, not an
  extension.
- Full W3C Trace Context propagation: trace_id links the entire request
  tree, span_id links each hop.
- Three months later: pull the trace_id. See every routing decision, every
  service consulted, every provenance grade, every escalation. The audit
  record tells you exactly what happened.
- *Mandatory structured audit means you can always reconstruct what happened
  and why.*

**Takeaway:** Audit is not a best practice — it's a protocol requirement.
Every hop, every decision, every grade, logged in a structured,
query-friendly format.

---

### View 7: Capability Registry — Typed Contracts (§8 Capability Registry)

**Request:** "I need to add a new theorem-proving service to my system."

**Plain LLM (tool-use ecosystem):**
- Write a natural-language tool description: "This tool proves theorems."
- The LLM reads the description and decides when to invoke it.
- No schema versioning. No compatibility checking. If the tool's API changes,
  things break silently.
- *Tool descriptions are free text meant for LLM consumption. The protocol
  intelligence lives in the consumer, not the envelope.*

**Through CCDP:**
- Register a Capability Record: service_id, capability_type
  (`org.ccdp.deduction`), input JSON Schema, output JSON Schema, cost hints
  (p50/p95/p99 latency, monetary cost), provenance capabilities (max_grade:
  FORMALLY_VERIFIED, supported_evidence_methods: ["formal_verification"]),
  health-check endpoint, schema version with Avro-style compatibility rules.
- The Registry enforces backward/forward compatibility on schema evolution.
- The Dispatcher routes by typed metadata, not by reading descriptions.
- *Typed contracts with versioned schemas. The service can evolve without
  breaking consumers — the Registry enforces it.*

**Takeaway:** Typed contracts in a registry with schema versioning, not
free-text descriptions interpreted by an LLM.

---

### View 8: Flow Control — Resource Signals (§12 Flow Control)

**Request:** "Analyze this dataset, but don't spend more than $5 and finish
within 10 minutes."

**Plain LLM:**
- No native cost signals. You might hit a token limit, or the API might
  time out. No way to express "I want an answer, but not at any price."
- If you hit the ceiling, you get an error, not a graceful degradation.
- *Cost and deadline are infrastructure concerns, not protocol features.*

**Through CCDP:**
- Request carries `cost_budget: {max_monetary_cost: "5.00", monetary_unit:
  "USD"}` and `deadline` with 10 minutes remaining.
- Dispatcher filters services by estimated latency (p95) and cost hints.
  Routes to the best candidate that can plausibly finish in budget.
- Service monitors consumption during execution. If it's about to exceed
  the budget, it returns an ESCALATION with reason `BUDGET_EXCEEDED`,
  reporting resources consumed so far and an estimate of what's needed.
- Every response reports actual resource consumption: tokens consumed,
  compute seconds, monetary cost. Audit data enables increasingly accurate
  cost estimation over time.
- *Cost budgets and deadlines are protocol-level fields, not afterthoughts.
  The Dispatcher makes resource-rational routing decisions.*

**Takeaway:** TCP has congestion signals. A cognitive dispatch protocol needs
cognitive-resource signals. CCDP has them.

---

### View 9: Security — Protocol vs Discipline (§15 Security)

**Request:** "Ensure that only authorized users can invoke the legal analysis
service."

**Plain LLM (tool-use ecosystem):**
- Security depends on implementation discipline: each tool author implements
  their own auth, each host manages its own token validation.
- Tool naming collisions exploitable from public registries.
- No mandated mutual authentication between components.
- *Security by convention — it works until it doesn't.*

**Through CCDP:**
- mTLS between Dispatcher and every Service (mutual authentication at the
  transport layer — no impersonation).
- Bearer tokens with capability-type scoping: a token authorized for
  `org.ccdp.language.generation` is rejected for `org.ccdp.deduction`.
- Ed25519 or HMAC-SHA256 envelope signing for high-grade provenance and
  cross-domain deployments.
- Replay protection: a request with the same `request_id` and different
  payload is rejected (error `-32011`).
- Every security decision is logged in the audit trail.
- *Security by protocol guarantee, not by implementation discipline.*

**Takeaway:** A cognitive dispatch protocol with security as a protocol
guarantee, not an implementation choice.

---

### View 10: Service Modes — Progressive Automation (§5 Architecture)

**Concept:** "How do I bring a new cognitive capability online?"

**Plain LLM:**
- Train a bigger model. Hope it handles the new task.
- Or add a tool and hope the LLM knows when to use it.
- No structured path from "a human does this" to "a machine does this."
- *Scaling means bigger models, not more capable systems.*

**Through CCDP:**
- Start with Mode 4: a human does the task behind a typed interface (same
  envelope, same schema, same provenance — just slower and more expensive).
- When tooling matures, swap in Mode 3: LLM + deterministic engine. The
  Dispatcher doesn't change. The Registry schemas don't change. Other
  services' integrations don't change.
- Later, swap in Mode 2: deterministic engine alone. Same interface, higher
  provenance grade, lower cost.
- The Dispatcher never gets smarter; the Services behind it get more capable.
- Provenance grades make the swap transparent: consumers see the grade change
  from HUMAN_ATTESTED to FORMALLY_VERIFIED and can calibrate trust
  accordingly.
- *Progressive automation: start with humans everywhere, replace one service
  at a time. The protocol is the stable spine.*

**Takeaway:** Modes are interchangeable without changing the Dispatcher. The
path from "a human does this" to "a machine does this" is a service swap, not
a protocol rewrite.

---

## Section 7: The Supervision Tree Connection

CCDP maps to the classic OTP supervision-tree model:

- **Human Supervisor** = top supervisor. Holds the spec and value judgment.
  Owns the restart policy.
- **Dispatcher** = intermediate supervisor. Routes to workers, monitors
  health, reroutes around failures, escalates when no worker can handle it.
- **Services** = worker processes. Supervised, typed protocol on the wire.
  They crash loudly (structured errors, escalations) rather than silently
  emitting corrupt output.
- **"Let it crash"** = the failure discipline. A service that fails crashes
  loudly, the failure is named, logged, and routed to the escalation chain.
  The output is *not* forwarded.

Key insight from Armstrong (2003): you build reliable systems from unreliable
components not by making the components correct, but by strong isolation,
message-passing-only interaction, supervision, and restart from a known-good
state.

---

## Section 8: Why Existing Protocols Aren't Enough (for a "Why CCDP?" view)

| Protocol | What it gets right | What it lacks for cognitive dispatch |
|----------|-------------------|-------------------------------------|
| **MCP** | Connects LLMs to tools. Huge ecosystem. July 2026 stateless pivot adds routing headers. | Designed for smart consumers, not dumb dispatchers. No mandatory audit. No cost signals. No epistemic dimension — treats all outputs as data. Security by implementation discipline. |
| **A2A** | Agent Cards for discovery. Task lifecycle. Opacity principle. | Assumes both sides are agents. CCDP's dispatcher is deliberately not an agent — it's a constrained coordinator. Peer-to-peer topology doesn't match CCDP's star. |
| **gRPC** | Typed contracts (protobuf). Streaming. Interceptor chains. | Implementation complexity works against the constrained-coordinator principle. Schema version management is a chronic operational wound. No epistemic layer. |
| **FIPA-ACL** | Typed communicative acts — exactly the right concept. | Never escaped the lab. No verifiable identity, no governance, no runtime tooling. CCDP inherits the insight, designs against the failure modes. |

---

## Section 9: Quick Reference — Key Numbers

- **8** provenance grades (OPAQUE through HUMAN_ATTESTED)
- **7** message types (REQUEST, RESPONSE, ESCALATION, NOTIFICATION,
  HEALTH_REQUEST, HEALTH_RESPONSE, DECOMPOSITION_RESULT)
- **7** steps in the routing algorithm
- **4** protocol layers (Transport, Routing/Audit, Epistemic, Content)
- **4** service modes (LLM, deterministic, composite, human)
- **14** CCDP-specific error codes (plus 5 standard JSON-RPC codes)
- **3** escalation reasons shown in the spec (PROVENANCE_BELOW_REQUIREMENT,
  CAPABILITY_EXCEEDED, DEADLINE_INSUFFICIENT, plus BUDGET_EXCEEDED and
  INTERNAL_DEGRADATION)
- **Star topology** — N links, not N(N-1)/2

---

## Section 10: Glossary of Terms for Copy Accuracy

Use these exact terms in the visual:

- **Dispatcher** (not "router", not "orchestrator", not "agent")
- **Constrained coordinator** (not "AI coordinator", not "smart router")
- **Provenance grade** (not "trust score", not "confidence level")
- **Escalation** (not "error", not "failure") — it's a first-class protocol
  operation
- **Envelope** (not "header") — the structured metadata the Dispatcher reads
- **Content** (not "payload" in formal contexts, though payload is fine
  casually)
- **Capability type** (not "tool type") — uses reverse-domain notation like
  `org.ccdp.deduction`
- **Service** (not "agent", not "tool") — any component that implements a
  capability
- **Evidence entry** (not "proof") — one piece of evidence supporting a grade
- **Composition trace** (not "audit log") — documents how a composed grade
  was derived
