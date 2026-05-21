---
# === CORE IDENTIFICATION ===
concept: Sensitive Data Protection
slug: sensitive-data-protection

# === CLASSIFICATION ===
category: production-ops
subcategory: data-security
tier: advanced

# === PROVENANCE ===
source: "OTP Design Principles"
source_slug: otp-design-principles
authors: "Ericsson AB"
chapter: "Secure Coding Guidelines"
chapter_number: null
pdf_page: null
section: "Rules / Secure Coding Standard"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "MSC-004"
  - "protecting secrets in Erlang"
  - "sensitive process flag"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - erlang-threat-model
extends: []
related:
  - secure-error-handling
  - gen-server
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do you protect sensitive data from appearing in Erlang logs and crash dumps?"
  - "What is process_flag(sensitive, true) and when should it be used?"
  - "How do you wrap secrets to prevent leakage in stack traces?"
  - "What is the format_status/2 callback for?"
  - "What ETS options protect sensitive table contents?"
---

# Quick Definition

Erlang logs many things by default, making it easy for sensitive data to appear in log files, crash dumps, and introspection tools. Protection mechanisms include the `private` ETS option, `process_flag(sensitive, true)`, the `format_status/2` callback for gen* behaviours, and wrapping secrets in zero-arity funs.

# Core Definition

The Secure Coding Guidelines state under MSC-004 (priority: Medium): "As Erlang logs many things by default, it is common for application data to appear in log files and the like. This is not necessarily a problem but some environments are under regulatory or compliance requirements not to leak certain data to disk or similar in case an unauthorized person were to get ahold of them (CWE-532)." The document then describes multiple protection mechanisms available in Erlang/OTP for preventing data leakage.

# Prerequisites

- **Erlang Threat Model** -- understanding what data the system logs by default and the scope of introspection tools.

# Key Properties

1. **Private ETS tables** -- using the `private` option prevents table contents from being read by other processes.
2. **Sensitive process flag** -- `process_flag(sensitive, true)` disables nearly all introspection: message queue inspection, tracing, crash dump inclusion.
3. **format_status/2 callback** -- for `gen_server` and other gen* behaviours, this callback controls how process state is presented in introspection tools such as `observer`.
4. **Zero-arity fun wrapping** -- wrapping secrets in a `fun() -> Secret end` causes the fun to appear instead of the data in stack traces and introspection features.
5. **Fun wrapping caveats** -- the secret becomes at least as long-lived as the fun (increasing crash dump risk), and in distributed systems, calling the fun may crash due to code version differences.
6. **Fun environment extraction** -- as a workaround for distributed version issues, extract with `[Secret] = erlang:fun_info(Fun, env)` instead of calling the fun.
7. **Stack frame scrubbing** -- catch errors in sensitive code sections and walk through stack frames discarding arguments before re-raising.
8. **Limitations** -- neither fun wrapping nor stack scrubbing prevents data leakage through crash or core dumps.
9. **Related CWEs** -- CWE-209 (Generation of Error Message Containing Sensitive Information), CWE-532 (Insertion of Sensitive Information into Log File).

# Construction / Recognition

## ETS Table Protection:
```erlang
%% Create a private ETS table
ets:new(secrets_table, [private, named_table]).
```

## Process-Level Protection:
```erlang
%% Disable introspection for the current process
process_flag(sensitive, true).
```

## Gen_server State Protection:
```erlang
%% Implement format_status/2 to redact sensitive state
format_status(_Opt, [_PDict, State]) ->
    [{data, [{"State", redacted}]}].
```

## Secret Wrapping:
```erlang
%% Wrap a secret in a zero-arity fun
WrappedSecret = fun() -> "my-api-key" end.

%% Retrieve the secret when needed
Secret = WrappedSecret().

%% In distributed systems, extract from fun environment
[Secret] = erlang:fun_info(WrappedSecret, env).
```

# Context & Application

This concept is particularly relevant for systems under regulatory or compliance requirements (HIPAA, GDPR, PCI-DSS) where sensitive data must not leak to logs, crash dumps, or monitoring tools. Erlang's default behavior of extensive logging and crash reporting -- while excellent for debugging and fault tolerance -- conflicts with data protection requirements. The multiple protection mechanisms (ETS private option, sensitive flag, format_status callback, fun wrapping) address different vectors through which data can leak. The source notes this is connected to OWASP A09:2025 (Logging and Alerting Failures), emphasizing the tension between thorough logging for security monitoring and protecting sensitive information.

# Examples

**Example 1** (secure_coding.md, MSC-004): "Using process_flag(sensitive, true) for processes operating on sensitive data. This disables nearly all introspection for the process: other processes cannot inspect the message queue of this process, tracing is disabled, the process' data will not be included in a crash dump, and so on."

**Example 2** (secure_coding.md, MSC-004): "A common technique is to wrap secrets in a zero-arity fun() that is then called in order to retrieve the secret. When passed around, the fun() will appear instead of the data it retrieves when called."

**Example 3** (secure_coding.md, MSC-004): Fun wrapping caveat: "In a distributed system you may have differing versions of the code, and calling the fun() may crash because it's for a different version of its defining module. A workaround for that would be to extract the secret with [Secret] = erlang:fun_info(Fun, env) instead of calling the fun."

# Relationships

## Builds Upon
- **Erlang Threat Model** -- understanding what the system logs and exposes through introspection is prerequisite to protecting sensitive data

## Enables
- No concepts directly enabled.

## Related
- **Secure Error Handling** -- crash-based error handling generates logs that may contain sensitive data; format_status and sensitive flag mitigate this
- **gen-server** -- the format_status/2 callback is specific to gen* behaviours

## Contrasts With
- No direct contrasts in source.

# Common Errors

- **Error**: Storing secrets in plain process state without implementing `format_status/2`.
  **Correction**: Implement the `format_status/2` callback in gen_server and other gen* behaviour modules that handle sensitive data, redacting secrets before they reach observer or crash logs.

- **Error**: Assuming that wrapping secrets in a fun prevents all leakage.
  **Correction**: "Neither approach prevents the data from leaking out through a crash or core dump." Fun wrapping prevents leakage via stack traces and introspection, but not via memory dumps.

- **Error**: Calling a secret-wrapping fun in a distributed system where code versions may differ.
  **Correction**: Use `[Secret] = erlang:fun_info(Fun, env)` to extract the secret from the fun's environment instead of calling it, avoiding crashes due to code version mismatches.

# Common Confusions

- **Confusion**: Thinking `process_flag(sensitive, true)` only affects logging.
  **Clarification**: It disables "nearly all introspection for the process" -- message queue inspection by other processes, tracing, crash dump inclusion, and more. It is a comprehensive introspection disable, not just a log filter.

- **Confusion**: Believing that the fun wrapping technique requires the secret to be computed on demand.
  **Clarification**: The secret can be part of the function environment (captured as a closure). However, this means "the secret becomes at least as long-lived as the fun, increasing the risk of it showing up in a crash dump."

# Source Reference

OTP Design Principles, Secure Coding Guidelines, MSC-004 rule (secure_coding.md, lines 1220-1269).

# Verification Notes

- Definition source: Directly quoted from MSC-004 rule section.
- Confidence rationale: High -- detailed section with multiple specific techniques, caveats, and CWE references (CWE-209, CWE-532).
- Uncertainties: None.
- Cross-reference status: References CWE-209, CWE-532. Related to gen-server (format_status callback), secure-error-handling.
