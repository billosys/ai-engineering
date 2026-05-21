---
# === CORE IDENTIFICATION ===
concept: Closing a Port
slug: closing-a-port

# === CLASSIFICATION ===
category: processes-concurrency
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Ports and Port Drivers"
chapter_number: null
pdf_page: null
section: "Port BIFs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - port_close
  - port closing

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-port
  - port-owner
extends: []
related:
  - opening-a-port
  - port-message-protocol
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you close a port in Erlang?"
  - "What happens when a port is closed?"
  - "What happens to a port when its owner terminates?"
  - "Does the external program stop when the port is closed?"
---

# Quick Definition
A port can be closed by sending it a `{Pid, close}` message or by calling `port_close(Port)`. The port replies with `{Port, closed}` after all buffers are flushed. The external program is expected to terminate when the port closes. A port also closes automatically if its owner process terminates.

# Core Definition
The Erlang Reference Manual describes two ways to close a port. Via message: "`{Pid, close}` -- Closes the port. Unless the port is already closed, the port replies with `{Port, closed}` when all buffers have been flushed and the port really closes." Via BIF: "`port_close(Port)` -- Closes the port." Additionally, "If the port owner terminates, so does the port (and the external program, if it is written correctly)." The external program "is to terminate when the port is closed." (Ports and Port Drivers chapter, "Ports" and "Port BIFs" sections).

# Prerequisites
- **erlang-port** -- Must have a port to close
- **port-owner** -- Only the port owner can close via the message protocol

# Key Properties
1. Two mechanisms: message `{Pid, close}` or BIF `port_close(Port)`
2. The port replies with `{Port, closed}` after flushing all buffers
3. The reply is only sent if the port is not already closed
4. The external program should terminate when the port closes (it should detect EOF on stdin)
5. If the port owner terminates, the port closes automatically
6. The external program should be written to handle port closure gracefully
7. An `{'EXIT', Port, Reason}` message is sent to the owner if the port terminates unexpectedly

# Construction / Recognition
## To Close:
1. Send `Port ! {self(), close}` and wait for `{Port, closed}`
2. Or call `port_close(Port)`
3. Or let the port owner terminate (automatic closure)

## To Identify:
1. A `{Port, closed}` message indicates successful closure
2. An `{'EXIT', Port, Reason}` message indicates unexpected port termination

# Context & Application
Proper port closure ensures that the external program shuts down cleanly and that system resources (file descriptors, OS processes) are released. The automatic closure when the owner terminates provides cleanup in failure scenarios, aligning with Erlang's "let it crash" philosophy.

**Typical contexts:**
- Graceful shutdown of external programs
- Cleanup in gen_server terminate callbacks
- Automatic cleanup when a supervisor terminates a port-owning worker

# Examples
**Example 1** (Ports and Port Drivers, "Port BIFs" section): Closing via message:
```erlang
Port ! {self(), close},
receive
    {Port, closed} -> ok
end
```

**Example 2** (Ports and Port Drivers, "Port BIFs" section): Closing via BIF:
```erlang
port_close(Port)
```

**Example 3** (Ports and Port Drivers, "Ports" section): Automatic closure: "If the port owner terminates, so does the port (and the external program, if it is written correctly)."

# Relationships
## Builds Upon
- **erlang-port** -- Closing is part of the port lifecycle
- **port-owner** -- Owner termination triggers automatic port closure

## Enables
Nothing -- closing is the terminal operation.

## Related
- **opening-a-port** -- Counterpart operation: open creates, close destroys
- **port-message-protocol** -- Close message is part of the protocol

## Contrasts With
No direct contrasts.

# Common Errors
- **Error**: Not handling the case where the external program does not terminate after port closure
  **Correction**: The external program should detect EOF on stdin and exit. If it does not, the OS process may linger. Consider using `os:cmd/1` or OS-level signals for cleanup.

- **Error**: Closing a port from a process that is not the port owner via the message protocol
  **Correction**: Use `port_close(Port)` BIF which can be called from any process, or transfer ownership first.

# Common Confusions
- **Confusion**: Thinking `port_close/1` blocks until the external program terminates
  **Clarification**: `port_close/1` closes the port (shuts down the communication channel). The external program is expected to notice and terminate, but Erlang does not wait for the external program to exit.

# Source Reference
Ports and Port Drivers chapter, "Ports" and "Port BIFs" sections.

# Verification Notes
- Definition source: Direct from source
- Confidence rationale: High -- explicit description of closure behavior
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to planned cards
