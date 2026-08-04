# CCDP: Composite Cognition Dispatch Protocol — Specification v0.2

**Status:** Draft v0.2 — second review round incorporated. Not yet implementation-ready; see spec-quality next steps below. See the overall review assessment in `workbench/review-v0.2/` for outstanding items from the first review round, and the second-round revision notes below for current status.

**Full spec:** See the source files in this directory (`01-abstract.md` through `18-references.md`) and the assembler tool in `../tools/`.

## Table of Contents

1. **Abstract** — Problem, solution, novel contribution (provenance grades, escalation-as-routing, mandatory audit)
2. **Conventions** — RFC 2119/8174 language, JSON format, naming conventions, document vs. wire-protocol versioning
3. **Introduction** — Problem grounded in TC⁰ limits; why MCP, A2A, gRPC, FIPA-ACL are insufficient; what makes cognitive dispatch different (claims not data, provenance-grade insufficiency as routing, spec-recursion); design principles; scope
4. **Terminology** — Defined terms, including the Structural Validation vs Semantic Interpretation distinction
5. **Architecture Overview** — Star topology, component roles (Dispatcher, Services, Registry, Human Supervisor), service modes, supervision-tree mapping
6. **Protocol Layers** — Layered architecture: Transport, Routing/Audit, Epistemic (novel), Content (opaque)
7. **Message Format** — JSON-RPC 2.0 wire encoding, message types, full envelope structure with per-message-type field requirements, Content structure, size limits, extensibility
8. **Capability Registry** — Capability Record structure, well-known types, registry operations, schema versioning with Avro-inspired compatibility rules
9. **Routing** — Routing algorithm, escalation routing, retry policy, circuit breaker integration
10. **Provenance and Evidence Grades** — Grade taxonomy (OPAQUE→HUMAN_ATTESTED) with an explicit policy-order caveat, grade assignment rules, composition rules (weakest-link, cross-check, decomposition), composition trace, worked examples
11. **Audit Trail** — Mandatory audit as core protocol, record structure, per-message-type audit requirements, audit store failure behavior, W3C Trace Context, storage requirements
12. **Flow Control** — Cost budgets, capacity advertisements, deadline propagation, back-pressure, bullwhip warning
13. **Error Handling and Escalation** — Error taxonomy (protocol/service/epistemic), error codes, escalation reasons, escalation chain processing (with authorization/budget/isolation checks), health monitoring, circuit breakers
14. **Decomposition** — Decomposition as first-class service, plan structure (DAG via `depends_on`), typed result references, composition methods, fallback strategies, recursive decomposition with width/depth/total-node limits
15. **Security** — mTLS, bearer tokens (format-agnostic, with lifecycle guidance), message signing with JSON canonicalization, replay protection, isolation, credential handling
16. **Conformance** — Conforming Dispatcher requirements as stable-ID tables (`DISP-CORE-NNN`, `DISP-FULL-NNN`, `DISP-OPT-NNN`); Conforming Service and Registry requirements; Core vs Full conformance levels; conformance testing guidance
17. **Security Considerations** — Threat model, known attack vectors with mitigations and residual risks, NSA/CISA response table, honest limitations
18. **References** — Normative and informative references, organized by category

## Key Design Decisions

- **Coordinator Dispatcher / structural protocol:** The Dispatcher is a constrained protocol enforcement and execution coordinator — it performs structural operations (routing, schema validation, decomposition plan execution, typed-reference resolution) but never semantic interpretation of Content
- **Provenance grades as Spence signals:** Cost-to-fake increases monotonically up the grade ladder — though the ordering is a policy order for routing and conformance, not a universal epistemic hierarchy (Section 10.2)
- **HUMAN_ATTESTED as highest grade:** Spec-recursion terminates at human judgment
- **Escalation as routing, not error:** First-class message type with structured chain processing, including authorization/budget/isolation checks on escalation targets
- **Layered architecture with novel Epistemic Layer:** No TCP/IP analog — this is where cognitive dispatch differs from data routing
- **Security as a protocol-level requirement:** Security properties are protocol-level requirements; production enforcement depends on deployment infrastructure, key management, and operational practices beyond the protocol's scope. Mutual authentication and token scoping required at all levels; message signing required for Full conformance with high-grade provenance and cross-domain deployments

## Next Steps

- Project plan: arcs and slices for implementation (in regular High effort mode)
- Implementation language selection
- Reference implementation scope

**Spec-quality next steps (before implementation):**
- Machine-readable JSON Schemas for all message types (Section 7.8) — schema inventory defined, schemas not yet published
- Conformance test suite (Section 16.6) — verification checklist defined, formal suite not yet published
- Reference and link verification — completed for this draft (Section 18); a final pass is still recommended before publication
- Threat-model refinement (multi-component, registry poisoning)
- Versioning alignment review (document version, wire version, audit schema version, registry record version)
- Stable requirement IDs — Section 16 conversion to `DISP-CORE-NNN` / `DISP-FULL-NNN` / `DISP-OPT-NNN` (completed for the Dispatcher; Service and Registry requirement tables remain prose-only)

**Implementation blockers (before first conforming implementation):**
- Companion JSON Schemas (`schemas/` directory) — inventory in Section 7.8
- Conformance test suite — framework in Section 16.6
- Reference and link verification — final pass before publication
- Stable requirement IDs — Section 16 conversion to `DISP-CORE-NNN` / `DISP-FULL-NNN`
