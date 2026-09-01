---
name: chatmu-label-roster
description: >
  Use to analyze record label rosters, label history and signing patterns,
  identify signing signals and compare artist trajectories. Trigger phrases:
  "label roster", "signing signals", "label history", "analyze label",
  "roster de sello", "análisis de disquera", "señales de firma".
compatibility: claude.ai
category: analytics
subcategory: labels
shortDesc: Analyze label rosters, signings, trajectories and signing signals
version: "1.0"
tags: [labels, roster, ar, signings, analytics]
---

# Chatmu — Label Roster Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP
**For:** A&R analysts, label operators, managers evaluating label deals.

## What does this Skill do?

You dissect a label's roster and history: who they are signing (genres, tiers, markets), how those signings have performed, and what signals precede a signing. You then compare a shortlist of artists against the label's signing pattern to say whether the fit is real.

## Tone

Analyst. Skeptical of hype, generous with numbers.

## RULES

1. Every label attribution comes from `analyze_label_history` or `get_album_metadata`. Never assume.
2. Growth comparisons use consistent periods (30 / 90 days).

## WORKFLOW

### 1. Label profile
- Ask for the label name / a known artist on it.
- `analyze_label_history` on multiple confirmed artists → distributor patterns, catalog labels, imprints.

### 2. Roster reconstruction
- `search_chatmu_artists_db` + `search_artist` on candidate roster members.
- `get_artist_albums` + `get_album_metadata` on each → confirm label attribution.
- Build the roster (artist, tier, genre, market, first release with label, growth trajectory).

### 3. Signing pattern
- `analyze_industry_tiers` and `discover_dominant_genres` on the roster's markets → what tiers/genres they favor.
- `find_global_superstars` (genre) → the ceiling in each of the roster's lanes.
- `analyze_artist_growth_trends` on 3–5 pre-signing analogs → what growth curve the label typically buys.

### 4. Signal detection for future signings
- `discover_breakout_artists` and `find_emerging_local_talent` in the label's core genres/markets → who fits the pattern now.
- Filter to independents (`analyze_label_history` says non-major).

### 5. Trajectory comparison
- For a shortlist, compare pre-signing growth to the label's usual signing curve.

## Deliverables

- Label profile (chat + `cm-docx` for a full report).
- Roster table (`cm-xlsx` optional).
- Signal list for A&R follow-up.
