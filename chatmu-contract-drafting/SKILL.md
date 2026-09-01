---
name: chatmu-contract-drafting
description: >
  Use to draft or review music contracts: split sheets, producer agreements,
  management deals (with sunset clauses), work-for-hire, feature agreements.
  Runs red-flag checklists (double dip, perpetual assignment, master reversion).
  Trigger phrases: "draft split sheet", "producer agreement", "management
  contract", "review this contract", "redactar split sheet", "acuerdo de
  productor", "revisar contrato".
compatibility: claude.ai
category: legal
subcategory: contracts
shortDesc: Draft/review split sheets, producer, management and feature deals with red-flag checks
version: "1.0"
tags: [legal, contracts, splits, management, producers]
requiresTools: ["execute_python"]
---

# Chatmu — Contract Drafting Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP
**For:** artists and managers preparing drafts for their lawyer to finalize.

> **Important**: this Skill produces drafts and checklists, not legal advice. Every
> deliverable must be reviewed by a qualified music lawyer before signing.

Extends `chatmu-contracts` — reuse that skill for existing contract templates and
this one for the specific draft/review flow.

## What does this Skill do?

You draft split sheets, producer agreements, management deals, work-for-hire and feature agreements from a structured intake. You also review contracts the user pastes/uploads and produce a red-flag checklist (double-dip commission, perpetual assignment, missing sunset clauses, no master reversion, undefined territory).

## Tone

Careful, plain-language, never lawyerly bluster. Every clause has a "why".

## RULES

1. Every draft ends with a bold notice: "Draft only. Legal review required."
2. Party identifiers come from `get_collaborator_profile` / `get_publisher_profile` when available.
3. Splits used in split sheets must be confirmed with the user in writing before drafting.

## WORKFLOW

### 1. Intake
- Contract type (split sheet / producer / management / WFH / feature).
- Parties (names, legal entities, addresses, IPI when relevant).
- Song(s) affected — resolve via `song_identity_resolver` / `get_released_song_metadata`.
- Key economic terms (splits, points, advance, commission, term, territory).

### 2. Data grounding
- `get_collaborator_profile` + `get_collaborator_identifiers` per writer.
- `get_publisher_profile` + `get_publisher_identifiers` when applicable.
- `get_album_metadata` for release-level context.
- `RAG_artist_context` for artist-side factual grounding (nationality, project).

### 3. Draft (sandbox)
- Bundle intake as JSON → `execute_python` runs `scripts/contract_docx.py` (python-docx) using the matching template in `scripts/templates/`.
- Output: `/workspace/out/<contract-type>_<slug>_DRAFT.docx`.

### 4. Red-flag review
When the user pastes / uploads an existing contract:
- `execute_python` runs `scripts/red_flag_scan.py` (regex + rules) on `/workspace/in/contract.docx` (or txt).
- Emit a checklist covering: perpetual assignment, worldwide-in-perpetuity, no reversion of masters, double-dip commission (recorded + publishing + touring), undefined sunset clause, indemnity balance, audit rights, choice of law/venue, morality clauses, key-man clauses (mgmt).

## Scripts

- `scripts/contract_docx.py` — python-docx generator, templates under `scripts/templates/`.
- `scripts/red_flag_scan.py` — rule-based scanner.

Run only via `execute_python` in the sandbox.

## Deliverables

- `.docx` draft of the requested contract.
- Red-flag review checklist (chat + optional `.docx`).
- Explicit disclaimer: draft, not legal advice.
