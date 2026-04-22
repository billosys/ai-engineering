---
concept: Structured Logging and Observability
slug: logging-and-observability
category: guidelines
subcategory: null
tier: intermediate
source: "Pragmatic Rust"
source_slug: pragmatic-rust
authors: "Pragmatic Rust Contributors"
chapter: "01-universal"
chapter_number: 1
pdf_page: null
section: "M-LOG-STRUCTURED"
extraction_confidence: high
aliases:
  - "structured logging rust"
  - "message templates"
  - "tracing events"
  - "opentelemetry rust logging"
prerequisites:
  - pragmatic-rust-overview
extends: []
related:
  - naming-and-quality-guidelines
  - application-guidelines
contrasts_with: []
answers_questions:
  - "How should Rust applications implement logging?"
  - "What are message templates in Rust logging?"
  - "How do I name log events in Rust?"
  - "How should sensitive data be handled in logs?"
  - "What are OpenTelemetry semantic conventions for Rust logging?"
---

# Quick Definition

M-LOG-STRUCTURED (v0.1) requires that logging use structured events with named properties and message templates following the message templates specification. This avoids runtime string formatting allocations, enables filtering and grouping by event name and properties, and integrates with OpenTelemetry semantic conventions.

# Core Definition

**M-LOG-STRUCTURED** (v0.1): "Logging should use structured events with named properties and message templates following the message templates specification." The guideline addresses four key concerns: avoiding string formatting (which allocates at runtime), naming events with hierarchical dot-notation, following OpenTelemetry semantic conventions for standardization, and redacting sensitive data. (Ch. 1, Universal)

The guideline uses the `tracing` crate's `event!` macro for examples but notes these principles apply to any logging API that supports structured logging (e.g., `log`, `slog`, custom telemetry systems).

# Prerequisites

- **pragmatic-rust-overview** -- understanding the guideline maturity framework (this is a v0.1 guideline, meaning it is newer and may evolve)

# Key Properties

1. **Avoid string formatting**: Message templates defer formatting until viewing time, avoiding runtime allocations. Use `{{property}}` syntax in templates, not `format!()` or string interpolation
2. **Name events hierarchically**: Use dot-notation `<component>.<operation>.<state>` (e.g., `file.processing.success`, `file.open.success`) to enable grouping and filtering
3. **Use named properties**: All structured fields should have semantic names (e.g., `file.path`, `file.size`) rather than positional arguments
4. **Follow OpenTelemetry semantic conventions**: Use standard attribute names (HTTP: `http.request.method`, `http.response.status_code`; File: `file.path`, `file.size`; Database: `db.system.name`, `db.operation.name`; Errors: `error.type`, `error.message`)
5. **Redact sensitive data**: Never log plain sensitive data (email addresses, PII, session IDs, tokens). Use redaction functions or the `data_privacy` crate
6. **Include all named properties in the message template**: For easier inspection at viewing time, the message template should reference all named properties

# Construction / Recognition

## Implementing Structured Logging:
1. Choose a structured logging crate (`tracing` is the primary example)
2. For each log statement, assign a hierarchical event name using `name:` parameter
3. Define named properties for all relevant data fields
4. Write a message template using `{{property}}` syntax that references all named properties
5. Map common attributes to OpenTelemetry semantic conventions where applicable
6. Audit all log statements for sensitive data; apply redaction before logging

## Event Naming Convention:
- Pattern: `<component>.<operation>.<state>`
- Examples: `file.open.success`, `file.processing.success`, `file.write.success`, `file.operation.started`

## Common OTel Semantic Convention Attributes:
- HTTP: `http.request.method`, `http.response.status_code`, `url.scheme`, `url.path`, `server.address`
- File: `file.path`, `file.directory`, `file.name`, `file.extension`, `file.size`
- Database: `db.system.name`, `db.namespace`, `db.operation.name`, `db.query.text`
- Errors: `error.type`, `error.message`, `exception.type`, `exception.stacktrace`

# Context & Application

Structured logging is essential for production observability. Unstructured string-based logging makes it difficult to filter, aggregate, and alert on specific events. The structured approach enables log aggregation systems to parse fields, create dashboards, and trigger alerts based on specific properties rather than regex matching on free-text messages.

**Typical contexts:**
- Production application logging and monitoring
- Distributed tracing with OpenTelemetry integration
- Security auditing where sensitive data must be redacted
- Performance-sensitive hot paths where logging allocation overhead matters

# Examples

**Example 1** (Ch. 1, M-LOG-STRUCTURED -- Avoid String Formatting):
Bad: `tracing::info!("file opened: {}", path);` -- string formatting allocates at runtime.
Good: `event!(name: "file.open.success", Level::INFO, file.path = path.display(), "file opened: {{file.path}}");` -- defers formatting, uses named properties.

**Example 2** (Ch. 1, M-LOG-STRUCTURED -- Named Events):
Bad: `event!(Level::INFO, file.path = file_path, "file {{file.path}} processed succesfully");` -- unnamed event.
Good: `event!(name: "file.processing.success", Level::INFO, file.path = file_path, "file {{file.path}} processed succesfully");` -- named event enables grouping and filtering.

**Example 3** (Ch. 1, M-LOG-STRUCTURED -- Redaction):
Bad: `user.email = user.email` -- logs sensitive email directly.
Good: `user.email.redacted = redact_email(user.email)` -- redacts before logging. Consider the `data_privacy` crate for consistent redaction.

# Relationships

## Builds Upon
- **pragmatic-rust-overview** -- this is a universal guideline applicable to all Rust project types

## Enables
- Production observability pipelines with structured log aggregation
- OpenTelemetry-compatible tracing and monitoring

## Related
- **naming-and-quality-guidelines** -- M-DOCUMENTED-MAGIC shares the principle of explicit documentation; M-STATIC-VERIFICATION helps catch logging issues
- **application-guidelines** -- applications are the primary consumers of structured logging
- performance-guidelines (covered by another extraction agent) -- M-THROUGHPUT relates to avoiding unnecessary allocations in logging

## Contrasts With
- Unstructured `println!`-based debugging or `format!`-based log messages
- Positional format arguments without named properties

# Common Errors

- **Error**: Using `format!()` or string interpolation in log messages.
  **Correction**: Use message templates with `{{property}}` syntax. Formatting is deferred until viewing time, avoiding runtime allocations.

- **Error**: Creating log events without a `name:` parameter.
  **Correction**: Always provide a hierarchical event name (`name: "component.operation.state"`) to enable grouping and filtering across log entries.

- **Error**: Logging sensitive data (emails, tokens, file paths with PII) without redaction.
  **Correction**: Apply redaction functions before logging. Use the `data_privacy` crate for consistent handling. Test that sensitive values do not appear in log output.

# Common Confusions

- **Confusion**: Thinking `{{property}}` in message templates performs Rust format string interpolation.
  **Clarification**: The `{{property}}` syntax preserves literal text while escaping Rust's format syntax. Actual string formatting is deferred until logs are viewed, not when they are emitted.

- **Confusion**: Assuming this guideline only applies to the `tracing` crate.
  **Clarification**: The source explicitly notes these principles apply to any structured logging API, including `log`, `slog`, and custom telemetry systems. `tracing` is used for examples only.

# Source Reference

Chapter 1: Universal Guidelines, section M-LOG-STRUCTURED (v0.1, "To minimize the cost of logging and to improve filtering capabilities"). Includes subsections on avoiding string formatting, naming events, OpenTelemetry semantic conventions, and redacting sensitive data, with code examples for each. References the Message Templates Specification, OpenTelemetry Semantic Conventions, and the OWASP Logging Cheat Sheet.

# Verification Notes

- Definition: Direct quotation from the guideline opening
- Key Properties: Drawn from each subsection (Avoid String Formatting, Name Your Events, Follow OpenTelemetry Semantic Conventions, Redact Sensitive Data)
- Confidence: HIGH -- the guideline is detailed with multiple code examples and external references
- Uncertainties: This is a v0.1 guideline, meaning it may evolve; the OTel conventions referenced are a living standard
- Cross-reference status: All slugs are within this extraction set or reference Agent B's planned cards
