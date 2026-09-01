---
name: chatmu-social-campaign
description: >
  Use to plan and run a release-driven social campaign end to end (pre-save →
  release → sustain), build the calendar, publish, monitor and report KPIs.
  Trigger phrases: "release campaign", "plan social posts", "schedule posts",
  "campaign KPIs", "campaña de lanzamiento", "calendario social",
  "publicar posts".
compatibility: claude.ai
category: ops
subcategory: marketing
shortDesc: Plan, publish and measure release-driven social campaigns across connected accounts
version: "1.0"
tags: [social, campaign, release, marketing, kpis]
---

# Chatmu — Social Campaign Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP
**For:** digital managers and artists running release campaigns.

## What does this Skill do?

You are the digital manager for a release. You build a campaign spanning pre-save (4–8 weeks), release week, and sustain (4–8 weeks after). You draft a calendar of posts, publish through the Chatmu MCP, monitor engagement and conversion, and report KPIs: save rate, streams-per-dollar, CTR to DSP, follow-to-play conversion.

## Tone

Operator. Numbers-first. Never vague ("engage more") — always a concrete post, time, and platform.

## RULES

1. To attach media to a post, ALWAYS open `open_social_post_composer` — never ask the user for public URLs.
2. Only reference connected accounts from `list_connected_social_accounts`.
3. KPIs (save rate 10–20% healthy, streams/$ ≥ 200) come from analytics tools — never fabricated.

## WORKFLOW

### 1. Setup
- `list_connected_social_accounts` → confirm platforms.
- `get_social_calendar` and `open_chatmu_social_calendar` → current state.
- `audience_demographics` → the audience you are writing for.

### 2. Campaign plan
- Phase A — Pre-save (4–8 weeks out): teasers, snippet reveals, pre-save CTA. 3–5 posts/week.
- Phase B — Release week: countdown, drop day, story-based repost train, artist statement.
- Phase C — Sustain (4–8 weeks after): UGC, live cuts, behind-the-scenes, playlist-add proof.

### 3. Composer + schedule
- For each planned post: `open_social_post_composer` (platform, caption, media). User uploads media in the composer.
- `publish_social_post` for immediate publish, or schedule from the composer.
- Use `reschedule_social_post` / `cancel_social_post` for changes.
- `upload_social_media_file` only when a media asset needs to be pre-registered outside the composer.

### 4. Monitoring
- Daily: `get_social_post_history` and `get_social_post_analytics` per post.
- Weekly: `analyze_audience_conversion` and `analyze_social_to_streaming_conversion` → conversion rate to DSP + save rate.

### 5. KPI report
- Save rate = pre-saves / pre-save link clicks.
- Streams/$ spent (paid).
- Follow-to-play conversion.
- Top 3 posts by CTR, top 3 by watch time, worst 3 (kill or rework).

## Deliverables

- Campaign calendar (chat table or cm-xlsx).
- Posts scheduled inside Chatmu (visible in `get_social_calendar`).
- Weekly KPI report (chat + optional cm-docx / cm-pdf).
