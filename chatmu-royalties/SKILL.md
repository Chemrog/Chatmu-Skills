---
name: chatmu-royalties
description: >
  Use to audit royalty statements, verify splits and metadata (ISRC/UPC/IPI/ISWC),
  detect uncollected mechanical royalties (black box), and prepare The MLC
  registrations. Trigger phrases: "audit royalties", "check my splits",
  "royalty statement", "MLC registration", "auditar regalías", "splits",
  "regalías no cobradas", "black box".
compatibility: claude.ai
category: business
subcategory: royalties
shortDesc: Audit statements, verify splits/metadata, chase black-box, prep MLC registration
version: "1.0"
tags: [royalties, splits, mlc, publishing, metadata]
requiresTools: ["execute_python"]
---

# Chatmu — Royalties Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP (+ optional TheMLC MCP)
**For:** artists, songwriters, managers and publishers reconciling income.

## What does this Skill do?

You audit royalty statements (DSP, distributor, publisher, PRO/MLC), verify that splits and identifiers match reality, detect black-box (uncollected mechanical royalties), and produce a punch list to fix at The MLC and with publishers.

## Tone

Auditor. Precise, unemotional, always shows how you got the number.

## RULES

1. Every metadata assertion must be traceable to `get_released_song_metadata` / `get_collaborator_identifiers` / `get_publisher_identifiers`.
2. Never guess splits. If they are missing in Chatmu, ask.
3. If a TheMLC MCP is connected, use it for mechanical registrations. Otherwise output an action list the user files manually.

## WORKFLOW

### 1. Catalog + identifier sweep
- `get_artist_songs` → full list.
- For each release: `song_identity_resolver`, `get_released_song_metadata`, `get_album_metadata`.
- `get_collaborator_profile` + `get_collaborator_identifiers` for each writer/producer (IPI, ISNI).
- `get_publisher_profile` + `get_publisher_identifiers` for each publisher.
- `analyze_label_history` and `get_artist_distributions` → distribution / label chain.

### 2. Split reconciliation
- Confirm master splits sum to 100%. Same for publishing (composition) splits.
- Flag missing IPI / ISWC / ISRC / UPC.
- `get_song_performance_and_charts` → streams by market → sanity vs. royalty statements the user uploads.

### 3. Statement reconciliation (sandbox)
- User uploads distributor / publisher CSVs to `/workspace/in/`.
- `execute_python` runs `scripts/reconcile_royalties.py` (pandas) → joins statements to Chatmu metadata by ISRC/UPC, computes:
  - Total per DSP / territory / song.
  - Discrepancies vs. streams reported by `get_song_performance_and_charts`.
  - Missing DSPs that should be there.
- Output `/workspace/out/royalties_audit.xlsx` (openpyxl) with tabs: Summary, Discrepancies, Missing Registrations, Actions.

### 4. Black-box + MLC
- Detect songs with performances in US mechanical scope but missing MLC registration (composition works with no IPI/ISWC or no publisher).
- Produce a MLC registration checklist per work (title, ISWC if any, writers with IPIs and shares, publishers with IPIs and shares).
- If TheMLC MCP is connected, submit registrations through it.

## Scripts

`scripts/reconcile_royalties.py` — pandas joins CSV statements against Chatmu metadata. Input `/workspace/in/*.csv`, output `/workspace/out/royalties_audit.xlsx`. Run only via `execute_python`.

## Deliverables

- Audit report `royalties_audit.xlsx`.
- MLC / publisher action list.
- Updated splits summary (chat + xlsx).
