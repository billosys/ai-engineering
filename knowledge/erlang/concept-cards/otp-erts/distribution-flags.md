---
# === CORE IDENTIFICATION ===
concept: Distribution Flags
slug: distribution-flags

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
section: "Distribution Flags"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "capability flags"
  - "DFLAG"
  - "dflags"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - distribution-handshake
extends:
  - distribution-handshake
related:
  - distribution-connection
  - distribution-header
  - distribution-module
  - external-term-format
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are distribution flags in Erlang?"
  - "How do nodes negotiate capabilities during the distribution handshake?"
  - "Which distribution flags are mandatory?"
---

# Quick Definition

Distribution flags (also called capability flags or DFLAGs) are bit flags exchanged during the distribution handshake to negotiate which features and encoding formats will be used on a connection. The intersection of both nodes' flags defines the connection's capabilities. Many flags are mandatory; if a mandatory flag is missing, the connection is refused.

# Core Definition

The ERTS documentation states: "Early in the distribution handshake the two participating nodes exchange capability flags. This is done in order to determine how the communication between the two nodes should be performed. The intersection of the capabilities presented by the two nodes defines the capabilities that will be used."

Distribution flags are sent as part of the `send_name` and `send_challenge` messages. In the new (version 6) format, flags are 64-bit big-endian integers. Key flag categories include:

**Mandatory flags** (connection refused if not present):
- `DFLAG_EXTENDED_REFERENCES` (16#4), `DFLAG_FUN_TAGS` (16#10), `DFLAG_NEW_FUN_TAGS` (16#80)
- `DFLAG_EXTENDED_PIDS_PORTS` (16#100), `DFLAG_EXPORT_PTR_TAG` (16#200)
- `DFLAG_BIT_BINARIES` (16#400), `DFLAG_NEW_FLOATS` (16#800)
- `DFLAG_UTF8_ATOMS` (16#10000), `DFLAG_MAP_TAG` (16#20000)
- `DFLAG_BIG_CREATION` (16#40000), `DFLAG_HANDSHAKE_23` (16#1000000)
- `DFLAG_UNLINK_ID` (16#2000000, mandatory from OTP 26)
- `DFLAG_V4_NC` (1 bsl 34, mandatory from OTP 26)

**Optional feature flags:**
- `DFLAG_DIST_HDR_ATOM_CACHE` (16#2000) -- atom cache in distribution header
- `DFLAG_FRAGMENTS` (16#800000) -- fragmented distribution messages
- `DFLAG_SEND_SENDER` (16#80000) -- `SEND_SENDER` control messages
- `DFLAG_EXIT_PAYLOAD` (16#400000) -- `PAYLOAD_*` control messages
- `DFLAG_SPAWN` (1 bsl 32) -- distributed spawn support
- `DFLAG_NAME_ME` (1 bsl 33) -- dynamic node name request
- `DFLAG_ALIAS` (1 bsl 35) -- process alias support (deprecated, replaced by `DFLAG_ALTACT_SIG`)
- `DFLAG_ALTACT_SIG` (1 bsl 37) -- alternate action signals (OTP 28)
- `DFLAG_NATIVE_RECORDS` (1 bsl 38) -- native record terms (OTP 29)

Distribution modules can configure flags via the `#hs_data{}` record fields: `add_flags`, `reject_flags`, and `require_flags`.

# Prerequisites

- **distribution-handshake** -- Flags are exchanged during the handshake

# Key Properties

1. Exchanged as part of `send_name` and `send_challenge` messages
2. 64-bit flags in the new (version 6) protocol format
3. The intersection of both nodes' flags determines connection capabilities
4. Missing mandatory flags cause connection refusal
5. `reject_flags` in `#hs_data{}` can disable features (e.g., atom cache, fragmentation)
6. `require_flags` can mandate specific features on a per-connection basis
7. `dist_util:strict_order_flags/0` returns flags for features requiring strict data ordering
8. Rejecting strict-order flags relaxes ordering to per-sender/receiver pair ordering

# Construction / Recognition

## To Construct/Create:
1. Flags are automatically set by the runtime system during handshake
2. Custom distribution modules can add, reject, or require specific flags via `#hs_data{}`
3. Use `reject_flags` to disable atom cache (`DFLAG_DIST_HDR_ATOM_CACHE`) or fragmentation (`DFLAG_FRAGMENTS`)
4. Use `require_flags` to mandate specific capabilities

## To Identify/Recognize:
1. The `Flags` field in `send_name` and `send_challenge` messages
2. `DFLAG_*` macros defined in the ERTS distribution protocol documentation

# Context & Application

Distribution flags are the capability negotiation mechanism that allows Erlang's distribution protocol to evolve while maintaining backward compatibility. New features are added as optional flags that become mandatory after a transition period (typically 2-3 OTP versions). Understanding flags is important when implementing alternative carriers (to know which features to support), debugging connection failures (missing mandatory flags), or tuning distribution performance (e.g., disabling atom cache for simpler carriers).

# Examples

**Example 1** (Distribution Flags): Rejecting strict-order features for a carrier that only guarantees per-sender/receiver ordering:
```erlang
#hs_data{
    reject_flags = dist_util:strict_order_flags()
    %% This disables DFLAG_DIST_HDR_ATOM_CACHE and DFLAG_FRAGMENTS
}
```

**Example 2** (Distribution Flags): Requiring spawn support on a connection:
```erlang
#hs_data{
    require_flags = ?DFLAG_SPAWN
    %% Connection aborts if remote node doesn't support SPAWN_REQUEST
}
```

# Relationships

## Builds Upon
- **distribution-handshake** -- Flags are the capability negotiation embedded in the handshake

## Related
- **distribution-connection** -- The negotiated flags determine which control messages are used
- **distribution-header** -- The `DFLAG_DIST_HDR_ATOM_CACHE` and `DFLAG_FRAGMENTS` flags control header features
- **distribution-module** -- Custom modules configure flags via `#hs_data{}`
- **external-term-format** -- Many flags control which encoding tags are accepted

## Contrasts With
None

# Common Errors

- **Error**: Not setting mandatory flags in a custom distribution implementation
  **Correction**: Mandatory flags are typically set automatically by the runtime. If implementing at a lower level, ensure all mandatory flags for the target OTP version are present.

- **Error**: Rejecting flags without understanding the consequences
  **Correction**: Rejecting `DFLAG_DIST_HDR_ATOM_CACHE` disables atom caching (may reduce performance). Rejecting `DFLAG_FRAGMENTS` prevents message interleaving. Both are returned by `dist_util:strict_order_flags/0`.

# Common Confusions

- **Confusion**: Thinking `DFLAG_NAME_ME` is a capability
  **Clarification**: `DFLAG_NAME_ME` is "not a capability but rather used as a request from the connecting node to receive its node name from the accepting node." It enables dynamic node names.

- **Confusion**: Thinking `DFLAG_ALIAS` and `DFLAG_ALTACT_SIG` are independent
  **Clarification**: `DFLAG_ALIAS` is deprecated (scheduled for removal in OTP 30) and has been replaced by `DFLAG_ALTACT_SIG`, which handles alias, priority, and exit signals.

# Source Reference

"Distribution Protocol" chapter, section "Distribution Flags", listing all defined capability flags and their semantics.

# Verification Notes

- Definition source: Direct from source text with complete flag catalog
- Confidence rationale: HIGH -- explicitly defined with per-flag documentation
- Uncertainties: None
- Cross-reference status: Verified against planned slugs
