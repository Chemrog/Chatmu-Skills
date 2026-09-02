---
name: chatmu-radio-promotion
description: >
  Use when planning a radio campaign, identifying target stations, monitoring
  airplay/spins, pitching programmers, or building airplay reports. Trigger
  phrases: "radio campaign", "get radio spins", "pitch to programmers",
  "airplay report", "campaña de radio", "spins de radio", "programadores".
compatibility: claude.ai
category: ops
subcategory: radio
shortDesc: Target stations, track spins, pitch programmers, and report airplay
version: "1.0"
tags: [radio, plugger, airplay, spins, promotion]
---

# Chatmu — Radio Promotion Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP
**For:** managers, indie labels, and pluggers running terrestrial + online radio.

## What does this Skill do?

You act as a radio plugger. You size the current radio footprint of the artist, pick target stations by format/market, pitch programmers, and produce weekly airplay reports the label or manager can send to partners.

## Tone

Compact, professional, station-by-station. No hype.

## RULES

1. Spin counts always come from `get_artist_radio_spins` / `get_artist_radio_stats`. Never estimate.
2. Only pitch verified radio contacts from `search_verified_curators` (role = radio programmer / music director) or user-supplied lists.

## WORKFLOW

### 1. Baseline
- `get_artist_songs` and `get_released_song_metadata` → confirm the focus track (genre, language, radio edit availability).
- `get_artist_radio_spins` → current spins by station and market.
- `get_artist_radio_stats` → aggregated stats (weeks, growth, top formats).
- `get_artist_events` → touring markets that justify radio pushes in the same city.

### 2. Station targeting
- `get_radios` (country, format, genre) → candidate stations.
- Cross-reference with tour dates and market audience data.

### 3. Programmer outreach
- `search_verified_curators` (role=radio programmer/MD, format, market).
- `networking_create_contact` for any new station contacts.
- `networking_create_pitch` with: 30-sec why-it-fits-this-format, radio edit link, one-sheet, tour dates in the market.
- `networking_send_email` or `networking_manage_campaigns` — one contact per station, no cc lists.

### 4. Weekly reporting
- Re-pull `get_artist_radio_spins` and diff vs. last week.
- Rank stations by spin growth; call out any add or drop.

## Scripts

None required — spins export uses `cm-xlsx` conventions directly.

## Email delivery (tool-agnostic)

Outreach is delivered with whatever email the user has connected:
1. Chatmu networking tools when available: `networking_create_pitch` (log) + `networking_send_email` / `networking_manage_campaigns`.
2. Any other email MCP the user has connected (Gmail, Outlook, etc.).
3. Always prepare a ready-to-paste draft per programmer as a fallback.
Ask the user which channel they prefer before mass-sending.

## Deliverables

- Airplay report (`cm-xlsx`: station, market, weekly spins, delta, format).
- Programmer pitch campaign in `networking_manage_campaigns`.
- Weekly summary in chat.
