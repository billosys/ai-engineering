# 18. References

## 18.1. Normative References

These references are essential to the implementation of this specification.

**[RFC 2119]** Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels," BCP 14, RFC 2119, March 1997. https://www.rfc-editor.org/rfc/rfc2119

**[RFC 8174]** Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words," BCP 14, RFC 8174, May 2017. https://www.rfc-editor.org/rfc/rfc8174

**[RFC 8259]** Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format," STD 90, RFC 8259, December 2017. https://www.rfc-editor.org/rfc/rfc8259

**[RFC 9562]** Davis, K., Peabody, B., and P. Leach, "Universally Unique IDentifiers (UUIDs)," RFC 9562, May 2024. https://www.rfc-editor.org/rfc/rfc9562

**[RFC 9126]** Lodderstedt, T., Campbell, B., Sakimura, N., Tonge, D., and F. Skokan, "OAuth 2.0 Pushed Authorization Requests," RFC 9126, September 2021. https://www.rfc-editor.org/rfc/rfc9126

**[RFC 6901]** Bryan, P., Ed., Zyp, K., and M. Nottingham, Ed., "JavaScript Object Notation (JSON) Pointer," RFC 6901, April 2013. https://www.rfc-editor.org/rfc/rfc6901

**[RFC 7519]** Jones, M., Bradley, J., and N. Sakimura, "JSON Web Token (JWT)," RFC 7519, May 2015. https://www.rfc-editor.org/rfc/rfc7519

**[RFC 7636]** Sakimura, N., Bradley, J., and N. Agarwal, "Proof Key for Code Exchange by OAuth Public Clients," RFC 7636, September 2015. https://www.rfc-editor.org/rfc/rfc7636

**[RFC 7662]** Richer, J., Ed., "OAuth 2.0 Token Introspection," RFC 7662, October 2015. https://www.rfc-editor.org/rfc/rfc7662

**[RFC 7800]** Jones, M., Bradley, J., and H. Tschofenig, "Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs)," RFC 7800, April 2016. https://www.rfc-editor.org/rfc/rfc7800

**[RFC 8785]** Rundgren, A., Jordan, B., and S. Erdtman, "JSON Canonicalization Scheme (JCS)," RFC 8785, June 2020. https://www.rfc-editor.org/rfc/rfc8785

(Note: RFC 8785 is Informational, not Standards Track. CCDP takes a normative dependency on this Informational RFC for message-signing canonicalization. If a Standards Track canonicalization scheme becomes available, future CCDP versions may adopt it.)

**[RFC 9207]** Meyer zu Selhausen, K. and D. Fett, "OAuth 2.0 Authorization Server Issuer Identification," RFC 9207, March 2022. https://www.rfc-editor.org/rfc/rfc9207

**[JSON-RPC]** JSON-RPC Working Group, "JSON-RPC 2.0 Specification," 2010. https://www.jsonrpc.org/specification

**[JSON-SCHEMA-2020-12]** Wright, A., Andrews, H., Hutton, B., and G. Dennis, "JSON Schema: A Media Type for Describing JSON Documents," draft-bhutton-json-schema-01, June 2022. https://json-schema.org/draft/2020-12/json-schema-core

**[W3C-TC]** W3C, "Trace Context," W3C Recommendation, February 2020. https://www.w3.org/TR/trace-context/ <!-- VERIFY: w3.org returns HTTP 403 to automated requests as of 2026-08-04; likely bot/WAF blocking (W3C TR pages are stable, long-lived URLs) — a human should confirm in-browser. -->

**[SemVer]** Preston-Werner, T., "Semantic Versioning 2.0.0." https://semver.org/

## 18.2. Informative References — Protocol Design Foundations

### TCP/IP and the End-to-End Principle

**[Saltzer-Reed-Clark 1984]** Saltzer, J.H., Reed, D.P., and D.D. Clark, "End-to-End Arguments in System Design," *ACM Transactions on Computer Systems*, 2(4):277–288, 1984. https://web.mit.edu/saltzer/www/publications/endtoend/endtoend.pdf

The foundational paper for CCDP's principle that the Dispatcher verifies protocol correctness while content correctness is the Service's responsibility.

**[E2E-Four-Decades]** "The End-to-End Argument, Four Decades Later," HackerNoon. https://hackernoon.com/the-end-to-end-argument-four-decades-later

### RPC and Schema Evolution

**[Kleppmann 2012]** Kleppmann, M., "Schema evolution in Avro, Protocol Buffers and Thrift," 2012. https://martin.kleppmann.com/2012/12/05/schema-evolution-in-avro-protocol-buffers-thrift.html

The basis for CCDP's schema versioning and compatibility rules in the Capability Registry.

**[Connect-gRPC]** Buf, "Connect: A Better gRPC." https://buf.build/blog/connect-a-better-grpc

Demonstrated that typed contracts and code generation are achievable without the full gRPC operational overhead. CCDP's HTTP-native approach is informed by Connect's design.

### Existing Protocols (Critical Analysis)

**[MCP-2026-07-28]** Model Context Protocol, "Release Candidate: The next generation of MCP," July 2026. https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/ (Blog post published May 21, 2026, announcing the July 28, 2026 release candidate.) (accessed 2026-08-03)

**[NSA-CISA-2024]** National Security Agency / Cybersecurity and Infrastructure Security Agency, "Deploying AI Systems Securely: Best Practices for Deploying Secure and Resilient AI Systems," April 2024. https://media.defense.gov/2024/Apr/15/2003439257/-1/-1/0/CSI-DEPLOYING-AI-SYSTEMS-SECURELY.PDF <!-- VERIFY: media.defense.gov returns HTTP 403 to automated requests as of 2026-08-04; likely bot/WAF blocking rather than a dead link (the URL path and filename are consistent with the known April 2024 NSA/CISA publication), but a human should confirm in-browser before external publication. -->

The general AI-deployment security findings that drove CCDP's "security by default" principle. See also [MCP-2026-07-28] for MCP-specific security posture findings.

**[MCP-Faults-2026]** "Real Faults in MCP Software: A Comprehensive Taxonomy," arXiv:2603.05637, 2026. https://arxiv.org/html/2603.05637v1

Analysis of 407 MCP-specific issues from 385 repositories documenting the consequences of loose protocol contracts.

**[A2A]** Linux Foundation / Google, "Agent2Agent (A2A) Protocol Specification," 2025. https://a2a-protocol.org/latest/specification (accessed 2026-08-04; the specification has moved from its original google.github.io/A2A/ location) — For background: Galileo AI, "Google Agent2Agent A2A Protocol Guide." https://galileo.ai/blog/google-agent2agent-a2a-protocol-guide (accessed 2026-08-03)

**[Zylos-Interop]** Zylos Research, "Agent Interoperability Protocols 2026." https://zylos.ai/research/2026-03-26-agent-interoperability-protocols-mcp-a2a-acp-convergence/ (accessed 2026-08-03)

**[Zylos-A2A]** Zylos Research, "Agent-to-Agent Communication Protocols." https://zylos.ai/research/2026-02-15-agent-to-agent-communication-protocols/ (accessed 2026-08-03)

**[FIPA-ACL]** SmythOS, "FIPA Agent Communication Language." https://smythos.com/developers/agent-development/fipa-agent-communication-language/ — See also: SmythOS, "Agent Communication Languages Comparison." https://smythos.com/developers/agent-development/agent-communication-languages-and-protocols-comparison/

**[arXiv-Agent-Comms]** "AI Agent Communication from an Internet Architecture Perspective," arXiv:2509.02317. https://arxiv.org/html/2509.02317

The most substantive academic survey of the agent communication landscape. CCDP drew from its FIPA-ACL historical analysis and two-layer standardization strategy while addressing a different problem space (supervised specialists under a dumb router, not autonomous peers at internet scale).

**[Mitra-Stack]** Mitra, S., "The Agent Protocol Stack: MCP + A2A + A2UI as TCP/IP Moment," 2026. https://subhadipmitra.com/blog/2026/agent-protocol-stack/ (accessed 2026-08-03)

**[DEV-Standards]** "The State of Agentic AI Standards in 2026," DEV Community. https://dev.to/alexmercedcoder/the-state-of-agentic-ai-standards-in-2026-mcp-a2a-webmcp-osi-and-the-protocol-stack-taking-3o2l (accessed 2026-08-03)

## 18.3. Informative References — Theoretical Foundations

### Market Economics and Quality Under Asymmetry

**[Akerlof 1970]** Akerlof, G.A., "The Market for Lemons: Quality Uncertainty and the Market Mechanism," *Quarterly Journal of Economics*, 84(3):488–500, 1970.

The lemons-market model for why cognitive output without quality signals degrades. Grounds the case for provenance grades as quality-discriminating signals.

**[Spence 1973]** Spence, M., "Job Market Signaling," *Quarterly Journal of Economics*, 87(3):355–374, 1973.

Signaling theory: a quality signal works only if it is expensive to fake. Grounds the provenance grade taxonomy — each grade represents increasing cost-to-fake.

**[Goodhart 1975]** Goodhart, C.A.E., "Monetary Relationships," 1975. Reformulated by Strathern, M., "'Improving Ratings': Audit in the British University System," *European Review*, 5(3):305–321, 1997.

"When a measure becomes a target, it ceases to be a good measure." Grounds the specification-recursion caveat for FORMALLY_VERIFIED grades and the rate-limiting-as-security design for verification services.

**[Howard 1966]** Howard, R.A., "Information Value Theory," *IEEE Transactions on Systems Science and Cybernetics*, 2(1):22–26, 1966.

Value of information as decision-relative. Grounds the resource-rational routing decisions and cost-budget design.

### Fault-Tolerant Composition

**[Armstrong 2003]** Armstrong, J., "Making reliable distributed systems in the presence of software errors," PhD thesis, KTH Royal Institute of Technology, 2003. https://erlang.org/download/armstrong_thesis_2003.pdf

The supervision-tree architecture. Build reliable systems from unreliable components through strong isolation, message-passing-only interaction, supervision, and "let it crash." Grounds CCDP's overall architectural model.

**[Hewitt-1973]** Hewitt, C., Bishop, P., and R. Steiger, "A Universal Modular ACTOR Formalism for Artificial Intelligence," IJCAI 1973.

The actor model: isolated actors interacting only by asynchronous messages. Grounds the "typed protocols on the wires" between Dispatcher and Services.

**[Simon 1962]** Simon, H.A., "The Architecture of Complexity," *Proceedings of the American Philosophical Society*, 106(6):467–482, 1962.

Near-decomposability: complex systems that survive are hierarchic with strong intra-module and weak inter-module interactions. Grounds the modular Service architecture and the decomposition model.

### Cognitive Architecture and Limits

**[Merrill-Sabharwal 2023]** Merrill, W. and Sabharwal, A., "The Parallelism Tradeoff: Limitations of Log-Precision Transformers," *TACL*, 2023. arXiv:2207.00729.

The TC⁰ result: transformers in a single pass cannot compute inherently sequential functions. Grounds the structural case for external cognitive organs.

**[Huang-2024]** Huang, J., et al., "Large Language Models Cannot Self-Correct Reasoning Yet," ICLR 2024. arXiv:2310.01798.

Self-correction without external feedback is unreliable. Grounds the requirement for external verification services and the escalation-over-silent-failure principle.

**[PlanBench]** Valmeekam, K., Kambhampati, S., et al., "On the Planning Abilities of Large Language Models," NeurIPS 2023. — Updated: Valmeekam, K., Stechly, K., and S. Kambhampati, arXiv:2409.13373, 2024.

LLMs do not plan reliably; they pattern-match and hallucinate plans for unsolvable problems. Grounds the Decomposition Service design — decomposition is a cognitive act performed by a dedicated service, not by the Dispatcher.

**[LLM-Modulo]** Kambhampati, S., et al., "LLMs Cannot Plan, But Can Help Planning in LLM-Modulo Frameworks," ICML 2024, PMLR v235:22895.

The constructive pattern for external planning organs: LLM as idea generator inside a generate-test loop with sound external verifiers. Grounds the Mode 3 (LLM + service composite) architecture.

**[ARC-AGI-2]** Chollet, F., et al., "ARC-AGI-2," arXiv:2505.11831, 2025.

Broad abstraction remains unsolved: ARC-AGI-2 scores ~3% for frontier models vs ~66% for humans. Grounds the HUMAN_ATTESTED grade as the highest grade and the human supervisor's irreducible role.

### Neurosymbolic Integration

**[PAL]** Gao, L., et al., "PAL: Program-aided Language Models," arXiv:2211.10435, 2022.

Offloading computation to a deterministic engine reliably beats chain-of-thought. Grounds the Mode 2 and Mode 3 service architectures.

**[Vericoding]** Bursuc, R., et al., "Vericoding," arXiv:2509.22908, 2025.

LLMs game weak specifications into vacuous proofs (~9%). Grounds the specification-recursion caveat on FORMALLY_VERIFIED grades and the `scope` requirement.

**[FunSearch]** Romera-Paredes, B., et al., "Mathematical discoveries from program search with large language models," *Nature*, 625:468, 2023.

LLM-in-a-loop discovery produces verifiable novel value, but only with a fast, sound, hard-to-game evaluator. Grounds the verification service architecture and Goodhart-aware rate limiting.

### Operations Research

**[Bullwhip]** Lee, H.L., Padmanabhan, V., and S. Whang, "The Bullwhip Effect in Supply Chains," *Management Science*, 43(4):546–558, 1997.

Variance amplification across serial stages. Referenced in Section 12.7 as a warning about error amplification in serial cognitive operations.

**[Little-1961]** Little, J.D.C., "A Proof for the Queuing Formula: L = λW," *Operations Research*, 9(3):383–387, 1961.

Distribution-free queueing invariant relating occupancy, throughput, and latency. Informs the capacity advertisement and load-aware routing design.

## 18.4. Informative References — Additional Sources

The references in this section are secondary or journalistic sources used for context and historical framing. Protocol-level claims in this specification are grounded in the primary references (Sections 18.1–18.3). Secondary sources provide useful context but are not evidence for protocol design decisions.

**[MCP-Roadmap]** Model Context Protocol, "The 2026 MCP Roadmap." https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/ (accessed 2026-08-03)

**[Scalifi-Flaws]** Scalifi AI, "Six Fatal Flaws of MCP," 2025. https://www.scalifiai.com/blog/model-context-protocol-flaws-2025 (accessed 2026-08-03)

**[Sivaro-MCP]** Sivaro, "Is MCP Outdated? A 2026 Reality Check." https://sivaro.in/articles/is-model-context-protocol-outdated-a-2026-reality-check/ (accessed 2026-08-03)

**[A2A-Adoption]** Glukhov, "A2A Protocol 2026 Adoption and Reality." https://www.glukhov.org/ai-systems/comparisons/a2a-protocol-2026-adoption/ (accessed 2026-08-03)

**[AlphaProof]** DeepMind, "AlphaProof," *Nature*, 651:607, 2025. https://www.nature.com/articles/s41586-025-09833-y

**[DreamCoder]** Ellis, K., et al., "DreamCoder: Bootstrapping Inductive Program Synthesis with Wake-Sleep Library Learning," PLDI 2021. https://dl.acm.org/doi/10.1145/3453483.3454080 <!-- VERIFY: dl.acm.org returns HTTP 403 to automated requests as of 2026-08-04; likely publisher bot-blocking, not a dead link — a human should confirm in-browser. -->

**[Dehaene-GW]** Dehaene, S., Kerszberg, M., and J.P. Changeux, "A neuronal model of a global workspace in effortful cognitive tasks," *PNAS*, 95(24):14529, 1998. https://www.pnas.org/doi/10.1073/pnas.95.24.14529

**[ACT-R]** Anderson, J.R., et al., "An integrated theory of the mind," *Psychological Review*, 111(4):1036, 2004.

**[Wagner-Altenberg]** Wagner, G.P. and Altenberg, L., "Complex Adaptations and the Evolution of Evolvability," *Evolution*, 50(3):967–976, 1996. https://academic.oup.com/evolut/article/50/3/967/6870900 <!-- VERIFY: academic.oup.com returns HTTP 403 to automated requests as of 2026-08-04; likely publisher bot-blocking, not a dead link — a human should confirm in-browser. -->

**[Bullmore-Sporns]** Bullmore, E. and Sporns, O., "The economy of brain network organization," *Nature Reviews Neuroscience*, 13(5):336–349, 2012. https://www.nature.com/articles/nrn3214

**[Lieder-Griffiths]** Lieder, F. and Griffiths, T.L., "Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources," *Behavioral and Brain Sciences*, 43:e1, 2020.

<!-- Link verification pass completed 2026-08-04. All URLs in this section were checked for resolution. Four URLs (academic.oup.com, dl.acm.org, media.defense.gov, w3.org) returned HTTP 403 to automated requests, consistent with publisher/vendor bot-blocking rather than dead links; each is flagged inline above with a VERIFY comment for human confirmation in-browser. All other URLs, including all arXiv IDs, resolved successfully (HTTP 200). -->
