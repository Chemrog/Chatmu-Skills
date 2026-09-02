---
name: chatmu-pr-presskit
description: >
  Use to build a press kit / EPK (bio, one-sheet, photo, music), pitch press,
  radio and podcasts, and follow up. Trigger phrases: "press kit", "EPK",
  "pitch to press", "media outreach", "kit de prensa", "campaña de prensa",
  "pitch a medios".
compatibility: claude.ai
category: ops
subcategory: pr
shortDesc: Build press kit and EPK, pitch press and podcasts, follow up
version: "1.0"
tags: [pr, press, epk, publicity, podcasts]
requiresTools: ["execute_python"]
---

# Chatmu — PR & Press Kit Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP
**For:** artists, managers and independent PRs building a press push.

## What does this Skill do?

You build the press kit (bio short + long, one-sheet, high-res photo slots, key tracks, quotes, socials, contact) and run press outreach: journalists, blogs, podcasts, radio interview slots. Every asset is grounded in real MCP data so numbers are current.

## Tone

Editorial. Story-first. Numbers as evidence, not fireworks.

## RULES

1. Every stat in the EPK comes from `artist_current_stats` / `get_song_performance_and_charts` at the moment of generation. Never stale.
2. Bios use `RAG_artist_context` for artist voice; no hallucinated bio facts.
3. Journalist / podcast contacts must be logged via `networking_create_contact` before outreach.

## WORKFLOW

### 1. Data pull
- `artist_details` → structural profile.
- `artist_current_stats` (period: 30) → live metrics.
- `get_artist_briefing` → high-level narrative points.
- `RAG_artist_context` → voice/story hooks.
- `get_artist_songs`, `get_artist_albums` → catalog.

### 2. Draft EPK
Draft in-chat first (bio 60w / 150w / 300w, one-sheet bullets, highlight tracks, quotes, socials, booking + press contact).

### 3. Generate the deliverables (sandbox)
- Bundle draft as JSON → `execute_python` runs `scripts/epk_docx.py` (python-docx) to produce `/workspace/out/EPK_<slug>.docx`.
- Then `execute_python` runs `scripts/epk_pdf.py` (reportlab) for `/workspace/out/EPK_<slug>.pdf`.

### 4. Media outreach
- `search_verified_curators` (role = journalist / blogger / podcast host, genre, market).
- `extract_contacts_from_web` on outlet mastheads / podcast about-pages.
- `networking_create_contact` → CRM.
- `networking_create_pitch` per outlet with a tailored hook (why this outlet, why now).
- `networking_send_email` or `networking_manage_campaigns` to deliver — one contact per outlet.
- `networking_read_inbox` to catch replies and follow-ups.

### 5. Follow-up loop
- 7 days: soft follow-up on no-replies.
- 14 days: close-out / thank-you for confirmed pieces. Log coverage in the CRM.

## Scripts

`scripts/epk_docx.py` — python-docx generator. Input JSON at `/workspace/in/epk.json`, output `.docx` at `/workspace/out/`.
`scripts/epk_pdf.py` — reportlab generator, same convention.

Executed only via `execute_python` in the sandbox. Never run locally.

## Web research (tool-agnostic)

Use web search for discovery and context, not for numbers:
- Finding who to contact (production companies, supervisors, curators, journalists, sponsors, venues), industry news, briefs, trends, and market context.
- Prefer whatever web-search tool is connected (`web_search`, Tavily, Bright Data, etc.); use `extract_contacts_from_web` for contact discovery.
- Metrics (streams, listeners, followers, growth, royalties) ALWAYS come from the Chatmu MCP — never from the web.
- If no web tool is available, proceed with MCP data and ask the user for context.

## Email delivery (tool-agnostic)

Outreach is delivered with whatever email the user has connected:
1. Chatmu networking tools when available: `networking_create_pitch` (log) + `networking_send_email` / `networking_manage_campaigns`.
2. Any other email MCP the user has connected (Gmail, Outlook, etc.).
3. Always prepare a ready-to-paste draft per outlet as a fallback.
Ask the user which channel they prefer before mass-sending.

## Deliverables

- EPK `.docx` + `.pdf` (downloadable).
- Press pitch campaign in `networking_manage_campaigns`.
- Coverage log in CRM.
