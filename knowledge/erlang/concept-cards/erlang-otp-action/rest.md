---
# === CORE IDENTIFICATION ===
concept: REST (Representational State Transfer)
slug: rest

# === CLASSIFICATION ===
category: api-design
subcategory: web-interfaces
tier: intermediate

# === PROVENANCE ===
source: "Erlang and OTP in Action"
source_slug: erlang-otp-action
authors: "Martin Logan, Eric Merritt, Richard Carlsson"
chapter: "Adding an HTTP interface to the cache"
chapter_number: 11
pdf_page: null
section: "11.2.3. Getting REST"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Representational state transfer"
  - RESTful interface

# === TYPED RELATIONSHIPS ===
prerequisites:
  - http-protocol
extends: []
related:
  - gen-web-server
  - restful-cache-interface
contrasts_with:
  - simple-text-protocol

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is REST?"
  - "What are the main principles of REST?"
  - "Why must a RESTful server be stateless between requests?"
---

# Quick Definition

REST (representational state transfer) is an architectural style in which clients use a standardized interface (HTTP) to manipulate representations of resources identified by global URIs, with no per-client state kept on the server between requests.

# Core Definition

REST stands for *representational state transfer*. It is a concept described as an after-the-fact summary of some of the central ideas in HTTP. The main principles of REST are that clients use a standardized interface (HTTP) for working with *representations* (documents) of resources kept on servers, referenced by global identifiers (URIs). A client never gets the actual resource — it gets a representation, possibly available in several formats. Each request transfers the client from one state to the next. Crucially, between requests the server should never keep implicit state about a client: either the client holds the necessary information, or it is stored explicitly on the server as a resource with its own address ("Erlang and OTP in Action," Ch. 11, Section 11.2.3).

# Prerequisites

- **HTTP protocol basics** — REST summarizes and builds on HTTP's verbs and resource model.

# Key Properties

1. A standardized uniform interface — HTTP verbs like `GET`, `PUT`, `POST`, `DELETE`.
2. Resources are identified by global identifiers (URIs).
3. Clients work with *representations* of resources, not the resources themselves.
4. Each request moves the client from one state to the next.
5. Statelessness: the server keeps no implicit per-client state between requests.
6. HTTP verbs map naturally onto database CRUD operations (create, read, update, delete).

# Construction / Recognition

## To Construct/Create:
1. Model the domain as resources, each addressed by a URI.
2. Define what each HTTP verb means as an operation on those resources.
3. Ensure no client state is retained on the server between requests.

## To Identify/Recognize:
1. An HTTP interface that uses standard verbs on URI-identified resources and keeps no implicit client session state.

# Context & Application

- **Typical contexts**: Designing language-neutral web service interfaces.
- **Common applications**: The chapter's RESTful cache interface — `GET`/`PUT`/`DELETE` on `/key` URLs.
- **Historical/stylistic notes**: Statelessness is the principle that prevents you from "slapping an HTTP interface onto any old service and calling it RESTful."

# Examples

**Example 1** (Section 11.2.3): A representation could be offered in multiple formats — e.g., the same image as JPEG, PNG, or TIFF.

**Example 2** (Section 11.2.3): For the cache, `DELETE /key` calls `simple_cache:delete(Key)`, `GET /key` calls `simple_cache:lookup(Key)`, and `PUT /key` calls `simple_cache:insert(Key, Body)` — only basic HTTP operations on URL-identified resources, with no client state retained.

# Relationships

## Builds Upon
- **HTTP protocol basics** — REST is an after-the-fact summary of central HTTP ideas.

## Enables
- **RESTful cache interface** — The chapter's concrete RESTful HTTP interface implements REST principles.

## Related
- **gen_web_server** — The behaviour used to build the RESTful interface.

## Contrasts With
- **Simple text-based protocol** — A bespoke protocol; REST uses the standardized HTTP interface and a stateless resource model.

# Common Errors

- **Error**: Keeping per-client session state on the server between requests.
  **Correction**: Make the server stateless — the client carries the state, or it is stored explicitly as an addressable resource.

# Common Confusions

- **Confusion**: Believing any HTTP interface is automatically RESTful.
  **Clarification**: RESTfulness requires the statelessness principle and a resource/representation model, not merely the use of HTTP.

# Source Reference

Chapter 11: "Adding an HTTP interface to the cache," Section 11.2.3 "Getting REST." See sidebar "Representational state transfer."

# Verification Notes

- Definition source: Direct adaptation of Section 11.2.3 and its sidebar.
- Confidence rationale: HIGH — the book explicitly defines REST and enumerates its principles.
- Uncertainties: None.
- Cross-reference status: Verified against planned slugs.
- Re-extraction notes: Fresh extraction; no prior card existed.
