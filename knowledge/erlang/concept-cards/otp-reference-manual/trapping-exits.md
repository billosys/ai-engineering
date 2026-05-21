---
# === CORE IDENTIFICATION ===
concept: Trapping Exits
slug: trapping-exits

# === CLASSIFICATION ===
category: error-handling
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Erlang Reference Manual"
source_slug: otp-reference-manual
authors: "Ericsson AB"
chapter: "Processes"
chapter_number: null
pdf_page: null
section: "Error Handling"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - trap_exit
  - trapping exit signals
  - process_flag(trap_exit, true)

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-process
  - erlang-signals
  - process-links
  - exit-signals
extends: []
related:
  - process-termination
  - message-receiving
  - signal-irregularities
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can a process survive the termination of a linked process?"
  - "How does process_flag(trap_exit, true) change exit signal handling?"
  - "What message format do trapped exits produce?"
  - "Can all exit signals be trapped?"
---

# Quick Definition
Trapping exits is a process mode enabled by `process_flag(trap_exit, true)` that converts incoming exit signals into `{'EXIT', SenderID, Reason}` messages in the process's message queue, instead of causing the process to terminate. This is the mechanism that allows supervisors to detect and respond to child process failures.

# Core Definition
The Erlang Reference Manual describes in the "Receiving Exit Signals" section that the behavior when a process receives an exit signal depends on the "trap exit state of the receiver at the time when the exit signal is received" along with the exit reason, sender, and link flag.

When trapping exits and the exit signal's link flag is not set (explicit `exit_signal/2`), the signal is converted to a message "if the exit reason of the signal is not the atom `kill`." When the link flag is set and the link is active, the signal is converted to a message regardless of the exit reason -- "an exit reason of `kill` will _not_ terminate the process in this case and it will not be converted to `killed`."

"The converted message will be of the form `{'EXIT', SenderID, Reason}` where `Reason` equals the exit reason of the exit signal and `SenderID` is the identifier of the process or port that sent the exit signal." (Processes chapter, "Receiving Exit Signals" section).

# Prerequisites
- **erlang-process** -- Trapping exits is a per-process setting
- **erlang-signals** -- Understanding the signal mechanism is essential
- **process-links** -- Trapping exits is primarily used with linked processes
- **exit-signals** -- Must understand exit signals to understand what is being trapped

# Key Properties
1. Enabled by calling `process_flag(trap_exit, true)`
2. Converts exit signals into `{'EXIT', SenderID, Reason}` messages in the message queue
3. The process can then handle these messages with a `receive` expression
4. Exit signals with reason `normal` are also converted to messages when trapping (instead of being silently dropped)
5. Exit reason `kill` from `exit_signal/2` (link flag not set) cannot be trapped -- the process is unconditionally terminated with reason `killed`
6. Exit reason `kill` from a link (link flag set) can be trapped -- the reason is not converted to `killed`
7. If the link has been deactivated (via `unlink/1`), the exit signal is silently dropped regardless of trap_exit state
8. Disabled by calling `process_flag(trap_exit, false)` (the default)

# Construction / Recognition
## To Enable:
1. Call `process_flag(trap_exit, true)` in the process that should trap exits

## To Disable:
1. Call `process_flag(trap_exit, false)`

## To Handle Trapped Exits:
```erlang
process_flag(trap_exit, true),
receive
    {'EXIT', Pid, Reason} ->
        %% Handle the exit signal from Pid
        handle_exit(Pid, Reason)
end
```

## To Identify/Recognize:
1. A process is trapping exits if `process_info(Pid, trap_exit)` returns `{trap_exit, true}`
2. `{'EXIT', Pid, Reason}` messages in a process's mailbox indicate trapped exit signals

# Context & Application
Trapping exits is essential for implementing supervisors and any process that needs to manage the lifecycle of other processes. By trapping exits, a supervisor can detect when a child process fails, log the failure reason, and take corrective action (such as restarting the child) without itself being terminated.

**Typical contexts:**
- OTP supervisors trap exits from all child processes
- Any process managing a pool of workers
- Processes that need to perform cleanup when a linked peer terminates
- Implementing custom supervision strategies

**When NOT to use:**
- Regular worker processes should generally not trap exits -- they should fail fast and let their supervisor handle recovery
- Trapping exits inappropriately can mask bugs by silently converting crashes into messages that are never handled

# Examples
**Example 1** (Processes, "Receiving Exit Signals" section): The complete decision matrix for receiving exit signals:

Without trapping exits:
- Exit reason `normal` -- signal is silently dropped
- Exit reason other than `normal` (with active link or no link flag) -- process terminates with that reason
- Exit reason `kill` from `exit_signal/2` -- process terminates with reason `killed`

With trapping exits:
- Exit reason other than `kill` from `exit_signal/2` -- converted to `{'EXIT', Sender, Reason}` message
- Any exit reason from a link (link flag set, link active) -- converted to `{'EXIT', Sender, Reason}` message, including `kill`
- Exit reason `kill` from `exit_signal/2` (link flag not set) -- process unconditionally terminates with reason `killed` (cannot be trapped)

**Example 2** (Processes, "Receiving Exit Signals" section): The message format:
```erlang
{'EXIT', SenderID, Reason}
```
Where `SenderID` is the pid or port identifier of the process that sent the exit signal, and `Reason` is the exit reason.

# Relationships
## Builds Upon
- **erlang-process** -- Trap_exit is a per-process flag
- **erlang-signals** -- Changes how exit signals are handled upon reception
- **process-links** -- Trapping exits is most commonly used with linked processes
- **exit-signals** -- Trapping exits changes the action taken when exit signals are received

## Enables
Nothing directly -- trapping exits is a terminal capability used by supervisors and lifecycle managers.

## Related
- **process-termination** -- Trapping exits prevents termination from exit signals (except `kill` via `exit_signal/2`)
- **message-receiving** -- Trapped exits become messages that can be fetched with `receive`
- **signal-irregularities** -- The asymmetric behavior of exit reason `kill` based on the link flag is an irregularity

## Contrasts With
No direct contrast -- trapping exits is a mode, not an alternative to another mechanism.

# Common Errors
- **Error**: Trapping exits but never handling the `{'EXIT', ...}` messages
  **Correction**: If you trap exits, you must have `receive` clauses that match `{'EXIT', Pid, Reason}`. Otherwise, these messages accumulate in the mailbox, consuming memory and causing the process to become unresponsive to other messages (if using selective receive).

- **Error**: Assuming `exit_signal(Pid, kill)` can be trapped
  **Correction**: Exit reason `kill` from `exit_signal/2` (link flag not set) cannot be trapped. The process is unconditionally terminated with reason `killed`. This is by design, to provide an unblockable process termination mechanism.

# Common Confusions
- **Confusion**: Thinking `exit_signal(Pid, kill)` and a link-based exit with reason `kill` behave the same
  **Clarification**: They do not. `exit_signal(Pid, kill)` is unconditionally fatal and untrappable. But when a linked process terminates with exit reason `kill`, the resulting exit signal (with link flag set) can be trapped, and the reason is not converted to `killed`. This is explicitly noted as an irregularity in the reference manual.

- **Confusion**: Thinking `process_flag(trap_exit, true)` prevents all process deaths
  **Clarification**: It does not prevent termination from `exit_signal(Pid, kill)`, from calling `exit(Reason)` or `error(Reason)` within the process itself, or from runtime errors in the process's own code.

# Source Reference
Processes chapter, "Error Handling" section, specifically the "Receiving Exit Signals" subsection, with behavioral details from the "Irregularities" section.

# Verification Notes
- Definition source: Direct from source -- decision matrix reconstructed from explicit conditional statements
- Confidence rationale: High -- the reference manual provides a detailed and precise specification of all cases
- Uncertainties: None
- Cross-reference status: All referenced slugs correspond to existing or planned cards
