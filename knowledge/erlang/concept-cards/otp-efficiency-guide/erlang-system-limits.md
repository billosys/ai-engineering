---
concept: Erlang System Limits
slug: erlang-system-limits
category: system-configuration
subcategory: runtime-limits
tier: foundational
source: "Erlang Efficiency Guide"
source_slug: otp-efficiency-guide
authors: "Ericsson/OTP Team"
chapter: "System Limits"
chapter_number: null
pdf_page: null
section: null
extraction_confidence: high
aliases:
  - "BEAM VM limits"
  - "Erlang runtime limits"
  - "OTP system limits"
prerequisites: []
extends: []
related:
  - erlang-data-type-memory-sizes
  - atom-creation-safety
contrasts_with: []
answers_questions:
  - "What are the default limits for processes, atoms, and ports in Erlang?"
  - "How can Erlang system limits be configured?"
  - "What is the maximum number of atoms in Erlang?"
  - "How many simultaneous processes can an Erlang node support?"
---

# Quick Definition

The Erlang runtime has practical limits on processes (default 1,048,576), atoms (default 1,048,576), open ports (default 16,384), tuple elements (16,777,215), atom name length (255), and function arguments (255). Most limits are configurable via command-line flags.

# Core Definition

The Erlang language specification puts no limits on the number of processes, length of atoms, and so on. However, for performance and memory saving reasons, there will always be limits in a practical implementation of the Erlang language and execution environment (Ericsson/OTP Team, "System Limits").

The key limits are configurable at VM startup using command-line flags, while others are fixed by the implementation.

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

**Configurable limits:**

1. **Processes**: default 1,048,576 simultaneously alive; configurable with `+P` flag
2. **Atoms**: default 1,048,576; configurable with `+t` flag
3. **Open ports**: default 16,384; configurable with `+Q` flag

**Fixed limits:**

4. **Characters in an atom name**: 255
5. **Elements in a tuple**: 16,777,215 (24-bit unsigned integer)
6. **Number of function arguments**: 255
7. **Number of fun arguments**: 255 minus one for each environment variable
8. **Binary size (32-bit)**: 536,870,911 bytes
9. **Binary size (64-bit)**: 2,305,843,009,213,693,951 bytes
10. **Node name length**: 255 (stored as an atom)

**Practically unlimited:**

11. **Unique local process identifiers**: 2^60 - 1 (64-bit) or 2^28 - 1 (32-bit)
12. **Unique local port identifiers**: 2^60 - 1 (64-bit) or 2^28 - 1 (32-bit)
13. **Unique references per scheduler**: 2^64 - 1 per set; at 1 per nanosecond, reuse after 584+ years
14. **Unique integers**: similar to unique references, practically inexhaustible
15. **Timer resolution**: millisecond on most systems

**Other limits:**

16. **Known nodes**: limited by the maximum number of atoms available for node names
17. **Connected nodes**: limited by max known nodes, max ports, or max sockets
18. **Open files and sockets**: limited by max ports and OS-specific settings
19. **Total allocated data**: full 32-bit or 64-bit address space, subject to OS limits

# Construction / Recognition

## Checking Current Limits

1. Process limit: check `+P` flag at startup or use `erlang:system_info(process_limit)`
2. Atom count: use `erlang:system_info(atom_count)` and `erlang:system_info(atom_limit)`
3. Port limit: check `+Q` flag at startup
4. Word size: `erlang:system_info(wordsize)`

## Configuring Limits at Startup

1. Increase process limit: `erl +P 2097152` (doubles the default)
2. Increase atom limit: `erl +t 2097152`
3. Increase port limit: `erl +Q 65536`

# Context & Application

System limits are relevant when:

- Designing systems with massive concurrency (may need to raise process limit)
- Building systems that handle external input (atom limit is a DoS vector; see atom-creation-safety)
- Working with large binaries (binary size limits differ between 32-bit and 64-bit)
- Managing many network connections (port limit constrains concurrent connections)
- Operating in distributed Erlang clusters (known node limit tied to atom limit)

**Key design considerations:**
- The default 1M process limit is sufficient for most applications but may need raising for extreme concurrency
- The atom limit of 1M is a hard security boundary -- atoms from untrusted input can crash the VM
- The 16K default port limit may be too low for high-connection-count servers
- Binary size limits on 32-bit (512 MB) can be a practical constraint for data processing
- From OTP 27, all binary-creating operations enforce the same size limit (previously only bit syntax did)

# Examples

**Startup configuration** (derived from source: "System Limits"):

```shell
# Raise process limit to 4 million
erl +P 4194304

# Raise atom limit to 2 million
erl +t 2097152

# Raise port limit to 65536
erl +Q 65536

# Combined
erl +P 4194304 +t 2097152 +Q 65536
```

**Querying limits at runtime:**

```erlang
%% Check process limit
erlang:system_info(process_limit).
%% => 1048576

%% Check current atom count
erlang:system_info(atom_count).
%% => (varies)

%% Check word size to determine architecture
erlang:system_info(wordsize).
%% => 8 (64-bit) or 4 (32-bit)
```

# Relationships

## Related

- **erlang-data-type-memory-sizes** -- Memory sizes interact with system limits (e.g., process base cost * max processes = potential memory)
- **atom-creation-safety** -- The atom limit (1,048,576 default) directly constrains safe atom creation practices

# Common Errors

- **Error**: Not raising the process limit for applications that spawn millions of processes
  **Correction**: Use `+P` flag at startup: `erl +P 4194304`

- **Error**: Not raising the port limit for high-connection-count servers
  **Correction**: Use `+Q` flag at startup and also check OS-level file descriptor limits

- **Error**: Assuming 32-bit and 64-bit systems have the same binary size limits
  **Correction**: 32-bit limit is ~512 MB; 64-bit limit is ~2 EB. Choose 64-bit for large binary processing.

# Common Confusions

- **Confusion**: Believing the Erlang language specification imposes these limits
  **Clarification**: The language specification puts no limits; these are practical implementation constraints of the BEAM VM

- **Confusion**: Thinking the process limit is the number of processes that can ever be created
  **Clarification**: The `+P` limit is for simultaneously alive processes. The unique PID limit (2^60 - 1 on 64-bit) is the total number of unique identifiers.

- **Confusion**: Assuming the default limits cannot be changed
  **Clarification**: The three major limits (processes, atoms, ports) are all configurable via command-line flags at VM startup

# Source Reference

"System Limits" chapter. Comprehensive listing of all practical limits in the Erlang runtime, including default values, configuration flags, and architecture-dependent variations. The source notes the OTP 27 change for binary size enforcement.

# Verification Notes

- All limit values: Directly from source
- Configuration flags (+P, +t, +Q): Explicitly named in source
- Unique identifier limits: Exact values from source (2^60 - 1, 2^28 - 1, etc.)
- 584-year reuse calculation: Explicitly stated in source
- OTP 27 binary limit change: Explicitly noted in source
- Confidence: HIGH -- comprehensive reference table from official OTP documentation
