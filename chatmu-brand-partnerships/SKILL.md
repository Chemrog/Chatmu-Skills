---
name: chatmu-brand-partnerships
description: >
  Use to pitch brand partnerships and sponsorships: define values/audience,
  build the deck, target brands and agencies, model activation KPIs. Trigger
  phrases: "brand deal", "sponsorship deck", "pitch to brands", "endorsement",
  "acuerdo de marca", "patrocinio", "deck de patrocinio".
compatibility: claude.ai
category: business
subcategory: branding
shortDesc: Build brand pitch deck, target sponsors, measure activation
version: "1.0"
tags: [brand, sponsorship, partnerships, deck, marketing]
requiresTools: ["execute_python"]
---

# Chatmu — Brand Partnerships Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP
**For:** managers and artists pitching brand deals / tour sponsorships.

## What does this Skill do?

You define the artist as a brand asset (values, audience, aesthetic, moments), build the pitch deck grounded in real data, target the right brands and agencies, and outline the activation and how it will be measured (reach, engagement, sell-through).

## Tone

Executive. Deck-ready. Every claim is a number.

## RULES

1. Every audience number in the deck comes from `audience_demographics` / `artist_current_stats`.
2. Never invent brand affinities — use `audience_demographics` interests only.
3. Every target logged as a `networking_create_contact` before outreach.

## WORKFLOW

### 1. Artist-as-brand profile
- `RAG_artist_context` for narrative + values.
- `artist_current_stats` (period: 30 and 90) → active reach.
- `audience_demographics` (includeInterests: yes) → interests / brand affinity signals.
- `artist_top_geographic_data` → where the audience is.
- `analyze_instagram_media` on top 5 posts → aesthetic.

### 2. Moments + touring context
- `get_artist_events` → upcoming activations.

### 3. Target list
- Match audience interests to candidate brand categories.
- `extract_contacts_from_web` on brand marketing pages / creative agencies.
- `networking_create_contact` per contact.

### 4. Deck (sandbox)
- Bundle profile + moments + assets as JSON → `execute_python` runs `scripts/brand_deck_pptx.py` (python-pptx) → `/workspace/out/brand_deck_<slug>.pptx`.
- Sections: cover, artist story, audience by numbers, geographic reach, cultural moments, activation menu (content, IG takeover, event branding, product feature, tour sponsorship), KPIs, contact.

### 5. Outreach
- `networking_create_pitch` per target with the deck.
- `networking_send_email` / `networking_manage_campaigns`.

### 6. Activation measurement (post-deal)
- `get_social_post_analytics` on sponsored posts.
- `analyze_audience_conversion` and `analyze_social_to_streaming_conversion` for lift attribution.

## Scripts

`scripts/brand_deck_pptx.py` — python-pptx deck generator. Input `/workspace/in/deck.json`, output `/workspace/out/brand_deck_<slug>.pptx`. Run via `execute_python` only.

## Email delivery (tool-agnostic)

Outreach is delivered with whatever email the user has connected:
1. Chatmu networking tools when available: `networking_create_pitch` (log) + `networking_send_email` / `networking_manage_campaigns`.
2. Any other email MCP the user has connected (Gmail, Outlook, etc.).
3. Always prepare a ready-to-paste draft per target as a fallback.
Ask the user which channel they prefer before mass-sending.

## Deliverables

- Brand deck `.pptx`.
- Target list (chat or cm-xlsx) with contacts.
- Post-activation KPI report.
