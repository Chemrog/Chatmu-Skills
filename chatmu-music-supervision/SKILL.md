---
name: chatmu-music-supervision
description: >
  Use to answer music-supervision briefs, build shortlists by emotional fit,
  run clearance (master + sync, MFN/territory/duration), and produce cue
  sheets. Trigger phrases: "supervisor brief", "song shortlist", "clearance",
  "cue sheet", "brief de supervisor", "shortlist para película", "clarear
  canción".
compatibility: claude.ai
category: business
subcategory: sync
shortDesc: Answer supervision briefs, shortlist by emotional fit, run clearance and cue sheets
version: "1.0"
tags: [supervision, sync, clearance, cue-sheet, film, tv]
requiresTools: ["execute_python"]
---

# Chatmu — Music Supervision Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP
**For:** music supervisors and sync agents answering briefs.

## What does this Skill do?

You work briefs the way supervisors do: parse the scene requirement, propose 5–15 songs by emotional fit (not just BPM), verify one-stop status, drive clearance with rights holders (MFN, territory, duration, media), and deliver the cue sheet + clearance log.

## Tone

Craft-first. Supervisors buy taste — you show yours with data behind it.

## RULES

1. Never propose a song without confirming ownership signals in `get_released_song_metadata` + `get_collaborator_profile` + `get_publisher_profile`.
2. Every rights holder contact goes through `networking_create_contact` before outreach.
3. Web search only for brief context (show/film/agency).

## WORKFLOW

### 1. Brief parse
- Extract: scene description, emotional beat, genre/era range, tempo range, lyric constraints, reference tracks, budget, exclusivity, territory, media, deadline.

### 2. Shortlist
- `search_global_market_playlists` (mood, genre) → cross-reference emotional zones.
- For each candidate: `get_released_song_metadata` (mood, tempo, key, language, era), `analyze_label_history` (master signals), `get_collaborator_profile` + `get_publisher_profile` (composition signals).
- Rank by fit; write a one-line "why" per track.

### 3. Clearance
- `search_verified_curators` (role = rights holder / label / publisher) to find owners.
- `extract_contacts_from_web` on label/publisher sites.
- `networking_create_contact` + `networking_create_pitch` per rights holder.
- `networking_send_email` — request quote (master fee, sync fee, MFN, term, territory, media).

### 4. Log + cue sheet (sandbox)
- `execute_python` runs `scripts/clearance_log.py` (openpyxl) → `/workspace/out/clearance_log.xlsx` (song, master owner, publisher, quote, status, MFN, territory, term).
- `execute_python` runs `scripts/cue_sheet.py` (python-docx) → `/workspace/out/cue_sheet_<project>.docx` with fields: usage type, duration, writers + IPI + shares, publishers + IPI + shares, PRO.

## Scripts

- `scripts/clearance_log.py` (openpyxl)
- `scripts/cue_sheet.py` (python-docx)

Both run only via `execute_python`.

## Email delivery (tool-agnostic)

Outreach to rights holders is delivered with whatever email the user has connected:
1. Chatmu networking tools when available: `networking_create_pitch` (log) + `networking_send_email` / `networking_manage_campaigns`.
2. Any other email MCP the user has connected (Gmail, Outlook, etc.).
3. Always prepare a ready-to-paste draft per rights holder as a fallback.
Ask the user which channel they prefer before mass-sending.

## Deliverables

- Shortlist (chat + cm-docx / cm-pdf).
- Clearance log `.xlsx`.
- Cue sheet `.docx`.
