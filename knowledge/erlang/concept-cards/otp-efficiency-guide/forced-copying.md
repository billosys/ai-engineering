---
concept: Forced Copying
slug: forced-copying
category: memory-management
subcategory: binary-memory-layout
tier: advanced
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "Constructing and Matching Binaries"
chapter_number: null
pdf_page: null
section: "Circumstances That Force Copying"
extraction_confidence: high
aliases:
  - "forced binary copying"
  - "binary copy triggers"
  - "circumstances that force copying"
prerequisites:
  - binary-append-optimization
  - refc-binary
extends: []
related:
  - compiler-binary-optimization
  - binary-construction-efficiency
  - match-context
contrasts_with: []
answers_questions:
  - "What circumstances force a binary to be copied during append?"
---

# Quick Definition

Certain operations on a binary mark it so that any future append operation will be forced to copy the binary data into a new allocation. These include sending the binary as a message, inserting it into an ETS table, matching on it, and appending to a non-latest version of the binary.

# Core Definition

The binary append optimization requires that there is a single ProcBin and a single reference to the ProcBin for the binary. The reason is that the binary object can be moved (reallocated) during an append operation, and when that happens, the pointer in the ProcBin must be updated. If there would be more than one ProcBin pointing to the binary object, it would not be possible to find and update all of them. Therefore, certain operations on a binary mark it so that any future append operation will be forced to copy the binary. In most cases, the binary object will be shrunk at the same time to reclaim the extra space allocated for growing (Ericsson/OTP Team, "Constructing and Matching Binaries," section "Circumstances That Force Copying").

# Prerequisites

- **binary-append-optimization** -- Understanding the append optimization is essential to understanding what "forced copying" defeats
- **refc-binary** -- The ProcBin/binary-object structure and the single-reference requirement must be understood

# Key Properties

1. The append optimization requires a single ProcBin with a single reference
2. The binary object may be moved (reallocated) during append, so only one ProcBin can point to it
3. Operations that create additional references or pointers force future appends to copy
4. When copying is forced, the binary object is typically shrunk to reclaim unused space
5. Only the binary returned from the latest append operation supports further cheap appends
6. Appending to a previous version forces copying to preserve referential transparency

# Construction / Recognition

## Operations That Force Copying

1. **Sending as a message**: `PortOrPid ! Bin1` -- the binary is shrunk; next append copies
2. **Inserting into ETS**: The binary is shared with the ETS table
3. **Passing to `erlang:port_command/2`**: The binary data is shared with the port
4. **Passing to `enif_inspect_binary` in a NIF**: Creates an external reference to the data
5. **Matching on the binary**: Creates a match context with a direct pointer to the data; binary is shrunk
6. **Appending to a non-latest version**: Only the latest append result is growable; older versions force a copy
7. **Garbage collection shrinking**: If a process keeps binaries, GC can eventually shrink them; future appends reallocate

# Context & Application

Forced copying is the safety mechanism that ensures the binary append optimization does not violate Erlang's immutability guarantees. Every forced-copy scenario corresponds to a situation where the binary data could be observed by multiple parties (processes, ETS tables, ports, NIFs), making in-place mutation unsafe.

**Typical contexts where forced copying matters:**
- Logging or broadcasting binary data mid-construction (sending as a message)
- Caching intermediate binary results in ETS
- Protocol implementations that match received data and then append to it
- Any pattern where a binary is both shared and grown

**Performance implication:** When forced copying occurs, the next append must allocate a new binary and copy all existing data. For large binaries being built incrementally, an unexpected forced copy can cause a significant performance hit.

# Examples

**Sending forces copying** (source: "Circumstances That Force Copying" section):

```erlang
Bin1 = <<Bin0,...>>,
PortOrPid ! Bin1,
Bin = <<Bin1,...>>  %% Bin1 will be COPIED
```

After sending `Bin1`, it is marked and shrunk. The next append must copy.

**Matching forces copying** (source: same section):

```erlang
Bin1 = <<Bin0,...>>,
<<X,Y,Z,T/binary>> = Bin1,
Bin = <<Bin1,...>>  %% Bin1 will be COPIED
```

Matching creates a match context with a direct pointer to the binary data. The binary is shrunk and future appends must copy. The source notes: "The reason is that a match context contains a direct pointer to the binary data."

**Branching forces copying** (source: "Constructing Binaries" section):

```erlang
Bin1 = <<Bin0/binary,1,2,3>>,
Bin3 = <<Bin2/binary,7,8,9>>,    %% Bin2 was derived from Bin1
Bin4 = <<Bin1/binary,17>>,       %% Bin1 COPIED to protect Bin3
```

Only the latest append result (`Bin3`) supports cheap appends. Appending to `Bin1` forces a copy.

# Relationships

## Related

- **compiler-binary-optimization** -- The compiler optimization avoids code paths that trigger forced copying
- **binary-construction-efficiency** -- Understanding forced copying is essential for writing efficient binary construction
- **match-context** -- Matching creates a match context with a direct pointer, which triggers forced copying

# Common Errors

- **Error**: Sending an intermediate binary as a message and then continuing to append to it
  **Correction**: If you must send the binary mid-construction, be aware that the next append will copy. Consider delaying the send until construction is complete.

- **Error**: Matching on a binary and then appending to the same variable
  **Correction**: The match shrinks the binary and forces copying on the next append. Restructure code to avoid matching and appending on the same binary.

# Common Confusions

- **Confusion**: Thinking forced copying means the optimization is broken or buggy
  **Clarification**: Forced copying is a correctness mechanism. It ensures that shared or observed binary data is never mutated in place. The optimization works correctly; it just cannot be applied when safety requires immutability.

- **Confusion**: Believing that only message sends trigger forced copying
  **Clarification**: Multiple operations trigger it: message sends, ETS inserts, port commands, NIF inspection, binary matching, and GC shrinking. Any operation that creates a second reference or pointer to the binary data.

# Source Reference

"Constructing and Matching Binaries," section "Circumstances That Force Copying." The source explains the single-ProcBin requirement, lists the triggering operations (message send, ETS, port_command, enif_inspect_binary, matching), and provides code examples for the message-send and matching cases.

# Verification Notes

- Definition: Directly from source -- "certain operations on a binary mark it so that any future append operation will be forced to copy the binary"
- Single-ProcBin requirement: Explicitly stated with rationale (binary object can be moved during reallocation)
- Shrinking behavior: Explicitly stated -- "the binary object will be shrunk at the same time to reclaim the extra space"
- All triggering operations listed in source: message send, ETS insert, port_command, enif_inspect_binary, matching
- GC shrinking: Stated in final paragraph of the section
- Code examples: Both taken directly from source
- Confidence: HIGH -- explicit section with detailed rationale and examples in official OTP documentation
