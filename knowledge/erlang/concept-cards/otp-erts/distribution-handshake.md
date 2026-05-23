---
# === CORE IDENTIFICATION ===
concept: Distribution Handshake
slug: distribution-handshake

# === CLASSIFICATION ===
category: distribution
subcategory: protocol
tier: advanced

# === PROVENANCE ===
source: "ERTS User's Guide"
source_slug: otp-erts
authors: "Ericsson AB"
chapter: "Distribution Protocol"
chapter_number: null
pdf_page: null
section: "Distribution Handshake"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "dist handshake"
  - "node handshake"
  - "connection handshake"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distribution-protocol
  - epmd-protocol
extends:
  - distribution-protocol
related:
  - distribution-connection
  - alternative-distribution-carrier
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do Erlang nodes authenticate during connection setup?"
  - "What is the distribution handshake?"
  - "How does cookie-based authentication work in Erlang distribution?"
---

# Quick Definition

The distribution handshake is the multi-step challenge/response procedure by which two Erlang nodes exchange names, negotiate capabilities, and authenticate each other using shared cookies and MD5 digests. It was introduced in OTP R6, amended in OTP 23 (version 6), and became the only supported version from OTP 25.

# Core Definition

The ERTS documentation describes a handshake procedure between an initiator node `A` and an acceptor node `B`:

1. **connect/accept**: `A` opens a TCP connection to `B`.
2. **send_name/receive_name**: `A` sends its node name, capability flags, and creation. The new format (tag `'N'`) sends 64-bit flags, 32-bit creation, and the node name. The old format (tag `'n'`) is only used by OTP 23/24 nodes not using EPMD.
3. **recv_status/send_status**: `B` sends a status code: `ok`, `ok_simultaneous`, `nok`, `not_allowed`, `alive`, or `named:` (for dynamic node names).
4. **recv_challenge/send_challenge**: `B` sends its name, flags, creation, and a 32-bit random challenge (tag `'N'`).
5. **send_complement/recv_complement** (optional): If `A` used the old name format, it sends complementary flags and creation (tag `'c'`).
6. **send_challenge_reply/recv_challenge_reply**: `A` sends its own 32-bit challenge plus an MD5 digest of `B`'s challenge concatenated with the shared cookie (tag `'r'`).
7. **recv_challenge_ack/send_challenge_ack**: `B` verifies `A`'s digest, then sends back its own MD5 digest of `A`'s challenge (tag `'a'`).
8. **check**: `A` verifies `B`'s digest. If correct, the connection is up.

The cookies are never sent in cleartext. The digest is 16 bytes of MD5 of the cookie text concatenated with the challenge as text. All messages in the handshake use 2-byte packet headers (`{packet, 2}`), switching to 4-byte headers after the handshake completes.

# Prerequisites

- **distribution-protocol** -- The handshake is phase 2 of the distribution protocol
- **epmd-protocol** -- EPMD provides the port number needed to initiate the TCP connection

# Key Properties

1. Uses MD5 digests for cookie verification -- cookies are never sent in cleartext
2. Challenges are random 32-bit integers
3. Handshake messages use 2-byte packet headers; post-handshake switches to 4 bytes
4. Capability flags are exchanged early to negotiate features for the connection
5. Supports simultaneous connect detection (`ok_simultaneous`, `nok` status codes)
6. Supports dynamic node names via `DFLAG_NAME_ME` and `named:` status
7. The `DFLAG_HANDSHAKE_23` flag is mandatory from OTP 25
8. An `out_cookie` for node B must match B's `in_cookie` for the local node
9. The protocol is not safe against takeover attacks -- a tradeoff between security and performance

# Construction / Recognition

## To Construct/Create:
1. Implement the handshake in a distribution module using `dist_util:handshake_we_started/1` (initiator) or `dist_util:handshake_other_started/1` (acceptor)
2. Populate a `#hs_data{}` record with callbacks (`f_send`, `f_recv`, `f_address`, etc.) and pass it to the `dist_util` functions
3. The `dist_util` module handles the actual handshake logic

## To Identify/Recognize:
1. Messages tagged with `'N'`, `'n'`, `'s'`, `'c'`, `'r'`, or `'a'` on a distribution connection
2. Uses 2-byte packet headers (unlike the 4-byte headers of connected-node traffic)

# Context & Application

The handshake is the security gate of Erlang distribution. Although not resistant to sophisticated attacks, it prevents accidental cross-cluster connections and provides basic authentication. Understanding the handshake is essential for implementing alternative distribution carriers, debugging connection failures, and understanding why distribution over TLS is recommended for production systems.

# Examples

**Example 1** (Distribution Handshake, semigraphic view): The handshake flow between initiator A and acceptor B:
```
A (initiator)                                    B (acceptor)
TCP connect ---------------------------------->  TCP accept
send_name ----------------------------------->   recv_name
  <------------------------------------------- send_status
recv_status
                        (ChB)                    ChB = gen_challenge()
  <------------------------------------------- send_challenge
recv_challenge
ChA = gen_challenge(),
OCA = out_cookie(B),
DiA = gen_digest(ChB, OCA)
                        (ChA, DiA)
send_challenge_reply ----------------------->    recv_challenge_reply
                                                 ICB = in_cookie(A),
                                                 check: DiA == gen_digest(ChB, ICB)?
                        (DiB)
  <------------------------------------------- send_challenge_ack
recv_challenge_ack                               DONE
ICA = in_cookie(B),
check: DiB == gen_digest(ChA, ICA)?
DONE
```

**Example 2** (Distribution Handshake, new send_name): The version 6 name message format:
```
| 'N' | Flags(8) | Creation(4) | Nlen(2) | Name(Nlen) |
```

# Relationships

## Builds Upon
- **distribution-protocol** -- The handshake is the second phase of the distribution protocol
- **epmd-protocol** -- EPMD provides the port number for the initial TCP connection

## Related
- **distribution-connection** -- Successful handshake leads to the connected phase
- **alternative-distribution-carrier** -- Custom carriers must implement or delegate the handshake

## Contrasts With
None

# Common Errors

- **Error**: Assuming the cookie is sent over the wire
  **Correction**: Only MD5 digests of the cookie concatenated with the challenge are exchanged. The cookie itself is never transmitted.

- **Error**: Using 4-byte packet headers during the handshake
  **Correction**: The handshake uses 2-byte packet headers (`{packet, 2}`). The switch to 4-byte headers happens only after the handshake completes.

# Common Confusions

- **Confusion**: Thinking the handshake provides strong security
  **Clarification**: The documentation explicitly notes it is "vulnerable against takeover attacks" and is "a tradeoff between fair safety and performance." Use distribution over TLS for production security.

- **Confusion**: Confusing `out_cookie` and `in_cookie`
  **Clarification**: `A`'s `out_cookie` for `B` must match `B`'s `in_cookie` for `A`, and vice versa. They need not be the same in both directions, though by default Erlang uses a single shared cookie.

# Source Reference

"Distribution Protocol" chapter, section "Distribution Handshake", including subsections "General", "Definitions", "The Handshake in Detail", "Semigraphic View", and "Distribution Flags".

# Verification Notes

- Definition source: Direct from source text including the semigraphic view
- Confidence rationale: HIGH -- explicitly defined with step-by-step protocol and wire formats
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
