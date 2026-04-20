---
# === CORE IDENTIFICATION ===
concept: KV Backup
slug: kv-backup

# === CLASSIFICATION ===
category: kv
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Deno Documentation"
source_slug: deno
authors: "Deno Contributors"
chapter: "deploy/kv/backup.md"
chapter_number: null
pdf_page: null
section: "Backups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "KV backup and restore"
  - "continuous backup"
  - "KV S3 backup"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - deno-kv
extends: []
related:
  - kv-operations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I back up a Deno KV database on Deno Deploy?"
  - "What backup targets does Deno KV support?"
---

# Quick Definition
Deno KV databases on Deno Deploy can be continuously backed up to S3-compatible storage (Amazon S3 or Google Cloud Storage), enabling point-in-time recovery and live replication.

# Core Definition
KV databases hosted on Deno Deploy support continuous backup to S3-compatible storage buckets. This operates in addition to Deno Deploy's internal replication and backup mechanisms. The backup stream has very little lag from the live database, enabling point-in-time recovery.

Two S3-compatible targets are supported:
- **Amazon S3** -- Create an S3 bucket, configure an IAM policy with `PutObject` permission, create access keys, and enter credentials in the Deno Deploy dashboard under the project's KV tab.
- **Google Cloud Storage** -- Create a GCS bucket, configure a service account with `Storage Object Admin` access, create HMAC keys, and enter credentials in the Deploy dashboard.

Once configured, backup starts immediately and runs continuously. The backup data can be consumed using the `denokv` tool for operations like restoring data, running read-only replicas, or piping mutations into data pipelines (Kafka, BigQuery, ClickHouse).

# Prerequisites
- A Deno KV database running on Deno Deploy (deno-kv)
- An S3-compatible storage bucket (AWS S3 or GCS)

# Key Properties
1. **Continuous backup** -- Near-real-time streaming of mutations to S3-compatible storage
2. **Point-in-time recovery** -- Retrieve a consistent snapshot of data at any past point
3. **Two supported targets** -- Amazon S3 and Google Cloud Storage (via S3-compatible HMAC keys)
4. **Minimal configuration** -- Bucket name, access key, secret key, and region entered via Deno Deploy dashboard
5. **denokv tool** -- Backup data can be consumed using the `denokv` CLI tool for restore and replication
6. **Additive to internal backups** -- Deno Deploy already replicates data internally; S3 backup is an additional layer

# Construction / Recognition
- AWS S3 setup: Create bucket -> Create IAM policy with `s3:PutObject` on bucket -> Attach to IAM user -> Generate access keys -> Enter in Deploy dashboard
- GCS setup: Create bucket -> Create service account with `Storage Object Admin` -> Generate HMAC key -> Enter in Deploy dashboard
- Status visible in Deno Deploy dashboard under KV > Backup section

# Context & Application
Continuous backup is important for production applications requiring disaster recovery, compliance, or data pipeline integration. The backup stream can feed into analytical databases or streaming platforms, enabling real-time data analysis alongside the operational KV store. The point-in-time recovery capability provides a safety net for data corruption or accidental deletion.

# Examples
From deploy/kv/backup.md:
- AWS IAM policy for backup:
  ```json
  {
    "Version": "2012-10-17",
    "Statement": [{
      "Sid": "KVBackup",
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::<bucket-name>/*"
    }]
  }
  ```
- Use cases: consistent snapshots, read-only replicas, piping mutations to Kafka/BigQuery/ClickHouse

# Relationships
## Builds Upon
- deno-kv (backs up KV data from Deno Deploy)

## Enables
- Point-in-time recovery
- Read-only replicas outside Deno Deploy
- Data pipeline integration

## Related
- kv-operations

## Contrasts With
- Manual export/import (backup is continuous and automatic vs. one-time snapshots)

# Common Errors
1. Not granting sufficient S3 permissions -- the IAM policy must include `s3:PutObject` on the specific bucket
2. Using incorrect region for GCS HMAC keys -- the region must match the bucket's location

# Common Confusions
1. **Internal vs. S3 backup** -- Deno Deploy already performs internal replication; S3 backup is an additional user-controlled backup to your own storage
2. **denokv tool** -- The backup data format is consumed by the `denokv` CLI tool (github.com/denoland/denokv), not by standard S3 tools directly

# Source Reference
- deploy/kv/backup.md: Step-by-step instructions for configuring AWS S3 and GCS backup targets, IAM/service account setup, and use cases

# Verification Notes
- High confidence: Backup configuration is explicitly documented with step-by-step instructions for both cloud providers
