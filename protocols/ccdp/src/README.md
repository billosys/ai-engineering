# CCDP: Composite Cognition Dispatch Protocol — Specification v0.1

**Status:** Draft Specification, August 2026
**Full spec:** 18 sections in `ccdp-spec/` directory on device at:
`/Users/oubiwann/Dropbox/Duncan's Research/LLMs/AI Progress Since the 1990s/ccdp-spec/`

## Table of Contents

1. **Abstract** — Problem, solution, novel contribution (provenance grades, escalation-as-routing, mandatory audit)
2. **Conventions** — RFC 2119/8174 language, JSON format, naming conventions
3. **Introduction** — Problem grounded in TC⁰ limits; why MCP, A2A, gRPC, FIPA-ACL are insufficient; what makes cognitive dispatch different (claims not data, confidence insufficiency as routing, spec-recursion); 8 design principles; scope
4. **Terminology** — 24 defined terms
5. **Architecture Overview** — Star topology, component roles (Dispatcher, Services, Registry, Human Supervisor), 4 service modes, supervision-tree mapping
6. **Protocol Layers** — 4-layer architecture: Transport, Routing/Audit, Epistemic (novel), Content (opaque)
7. **Message Format** — JSON-RPC 2.0 wire encoding, 7 message types, full envelope structure with all fields, Content structure, size limits, extensibility
8. **Capability Registry** — Capability Record structure, well-known types, 5 registry operations, schema versioning with Avro-inspired compatibility rules
9. **Routing** — 7-step algorithm, escalation routing, retry policy, circuit breaker integration
10. **Provenance and Evidence Grades** — 8-grade taxonomy (OPAQUE→HUMAN_ATTESTED), grade assignment rules, composition rules (weakest-link, cross-check, decomposition), composition trace
11. **Audit Trail** — Mandatory audit as core protocol, record structure, W3C Trace Context, storage requirements
12. **Flow Control** — Cost budgets, capacity advertisements, deadline propagation, back-pressure, bullwhip warning
13. **Error Handling and Escalation** — Error taxonomy (protocol/service/epistemic), 13 error codes, 9 escalation reasons, escalation chain processing, health monitoring, circuit breakers
14. **Decomposition** — Decomposition as first-class service, plan structure (DAG), result references, composition methods, fallback strategies, recursive decomposition
15. **Security** — mTLS, bearer tokens with scoped capabilities, message signing, replay protection, isolation, credential handling
16. **Conformance** — Conforming Dispatcher (33 requirements), Service (24), Registry (14); Core vs Full conformance levels
17. **Security Considerations** — Threat model, 8 attack vectors with mitigations and residual risks, NSA/CISA response table, honest limitations
18. **References** — 9 normative, 30+ informative (organized by category)

## Key Design Decisions

- **Dumb dispatcher / smart protocol:** Dispatcher reads envelopes, never content
- **Provenance grades as Spence signals:** Cost-to-fake increases monotonically up the grade ladder
- **HUMAN_ATTESTED as highest grade:** Spec-recursion terminates at human judgment
- **Escalation as routing, not error:** First-class message type with structured chain processing
- **4-layer architecture with novel Epistemic Layer:** No TCP/IP analog — this is where cognitive dispatch differs from data routing
- **Security by default:** Every requirement is a protocol guarantee, not an implementation recommendation

## Next Steps

- Project plan: arcs and slices for implementation (in regular High effort mode)
- Implementation language selection
- Reference implementation scope

