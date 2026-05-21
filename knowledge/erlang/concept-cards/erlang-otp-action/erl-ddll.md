---
# === CORE IDENTIFICATION ===
concept: erl_ddll Driver Loading
slug: erl-ddll

# === CLASSIFICATION ===
category: tooling
subcategory: interoperability
tier: advanced

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Integrating with foreign code using ports and NIFs"
chapter_number: 12
pdf_page: null
section: "12.3.4. The Erlang side of the driver"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "erl_ddll:load/2"
  - dynamic driver loading

# === TYPED RELATIONSHIPS ===
prerequisites:
  - linked-in-driver
  - open-port
extends: []
related:
  - priv-directory
  - driver-callbacks
contrasts_with:
  - nif-loading

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you load a linked-in driver from Erlang?"
  - "What does erl_ddll:load/2 do?"
  - "How does opening a port differ for a driver versus an external program?"
---

# Quick Definition

`erl_ddll:load/2` loads and links a linked-in driver's shared library into the Erlang VM, after which `open_port({spawn, DriverName}, ...)` opens a port to it.

# Core Definition

When using a linked-in driver, the Erlang side is responsible for ensuring the C library has been loaded and linked before opening the port. To load a shared library you call `erl_ddll:load(Path, Name)` (note: two `d`s), where `Path` is the path to the directory of the library file and `Name` is the filename without extension (`.so` or `.dll`). The filename must match the `driver_name` field of the `ErlDrvEntry` struct. If the call returns `ok`, you can proceed to open the port; the `open_port` command looks the same as for an external program, but the name given is no longer a file path — it is the string used to identify the loaded driver ("Erlang and OTP in Action," Ch. 12, Section 12.3.4).

# Prerequisites

- **Linked-in port driver** — `erl_ddll` loads the driver's shared library.
- **open_port BIF** — After loading, a port is opened to the driver.

# Key Properties

1. `erl_ddll:load(Path, Name)` loads and links a driver shared library into the VM.
2. `Path` is the directory containing the library; `Name` is the filename without `.so`/`.dll` extension.
3. The `Name` must match the `driver_name` in the driver's `ErlDrvEntry` struct.
4. The library file is normally placed in the application's `priv` directory.
5. After a successful `ok` result, `open_port({spawn, DriverName}, Options)` opens a port to the driver.
6. For a linked-in driver, the `exit_status` and `{packet, N}` options are not used.
7. The `{spawn, DriverName}` argument is the driver's identifying string, not a file path.

# Construction / Recognition

## To Construct/Create:
1. Determine the `priv` directory with `code:priv_dir(AppName)`.
2. Call `erl_ddll:load(PrivDir, "jp_driver")`; exit on anything other than `ok`.
3. Call `open_port({spawn, "jp_driver"}, [binary])` to open the port.

## To Identify/Recognize:
1. An `erl_ddll:load/2` call followed by `open_port({spawn, Name}, ...)` with the same name string.

# Context & Application

- **Typical contexts**: The Erlang side of a linked-in driver integration.
- **Common applications**: `jp_server` loads `jp_driver` from `priv` and opens a port to it.
- **Historical/stylistic notes**: The OTP application structure is unchanged from the port version; only the port-management parts of the `gen_server` change.

# Examples

**Example 1** (Section 12.3.4): `case erl_ddll:load(PrivDir, "jp_driver") of ok -> ok; Other -> exit(Other) end, open_port({spawn, "jp_driver"}, [binary])`.

# Relationships

## Builds Upon
- **Linked-in port driver** — `erl_ddll` is how the driver is brought into the VM.
- **open_port BIF** — Used after loading to open a port to the driver.

## Related
- **priv directory** — The driver library lives in `priv`.
- **erl_driver callback functions** — `driver_name` must match the `erl_ddll:load` name.

## Contrasts With
- **NIF library loading** — NIFs are loaded with `erlang:load_nif/2` and do not involve ports.

# Common Errors

- **Error**: Passing the filename with its `.so`/`.dll` extension to `erl_ddll:load/2`.
  **Correction**: Give the name without extension; it must match `driver_name`.

- **Error**: Using `exit_status` or `{packet, N}` when opening a port to a linked-in driver.
  **Correction**: Omit them — the `erl_driver` API already supplies sizes, and there is no external process exit status.

# Common Confusions

- **Confusion**: Thinking `{spawn, "jp_driver"}` names a file on disk.
  **Clarification**: For a linked-in driver it is the identifying string of the loaded driver, not a file path.

# Source Reference

Chapter 12: "Integrating with foreign code using ports and NIFs," Section 12.3.4 "The Erlang side of the driver."

# Verification Notes

- Definition source: Direct adaptation of Section 12.3.4.
- Confidence rationale: HIGH — the book shows the exact loading and port-opening code.
- Uncertainties: None.
- Cross-reference status: `linked-in-driver`, `open-port` owned by this agent.
- Re-extraction notes: Fresh extraction; no prior card existed.
