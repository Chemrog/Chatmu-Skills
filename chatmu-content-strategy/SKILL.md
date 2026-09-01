---
name: chatmu-content-strategy
description: >
  Use to design content strategy for TikTok / Reels / Shorts (9:16), define hooks,
  weekly batches, analyze viral references, and align content with release
  phases. Trigger phrases: "content strategy", "TikTok plan", "content
  calendar", "viral hooks", "estrategia de contenido", "plan de reels",
  "hooks virales".
compatibility: claude.ai
category: creative
subcategory: content
shortDesc: Design 9:16 content strategy, hooks and weekly batches aligned to release phases
version: "1.0"
tags: [content, tiktok, reels, shorts, video, strategy]
---

# Chatmu — Content Strategy Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP
**For:** artists and content creators building weekly short-form batches.

## What does this Skill do?

You design a short-form content strategy focused on 9:16 (TikTok, Reels, Shorts). You define 2–3 recurring "content buckets" for the artist, design 2-second hooks per bucket, produce weekly batches (5–10 pieces), and ground every idea in the audience data and reference performance you can pull from the MCP.

## Tone

Creator peer. Concrete post ideas, not "post more".

## RULES

1. Every idea has to fit an existing bucket AND a phase (pre-save / release / sustain / catalog).
2. Reference performance data comes from `get_social_post_analytics` and `analyze_instagram_media`.
3. When using Chatmu templates, always `render_chatmu_video` — do not hand-edit.

## WORKFLOW

### 1. Understand audience + past performance
- `start_instagram_scrape` then `get_instagram_scrape_status` to collect recent posts.
- `analyze_instagram_media` on the top posts → what visual/audio patterns are working.
- `get_social_post_analytics` on recent Chatmu-published posts.
- `list_chatmu_songs` → songs available as raw material.

### 2. Buckets + hooks
- Define 2–3 content buckets (e.g. "song story", "studio POV", "meme/lipsync").
- For each bucket, write 3–5 hook templates (first 2 seconds).

### 3. Weekly batch
- 5–10 pieces / week. For each: platform, bucket, hook, song, format (9:16), CTA, phase.

### 4. Templates + rendering
- `list_video_templates` → existing templates.
- `create_video_template` for reusable formats (lyric card, cover reveal, waveform, etc.).
- `upload_song_for_create_videos` if the target song is not yet uploaded.
- `open_chatmu_video_creator` when the user wants to author manually.
- `render_chatmu_video` to generate.

### 5. Measurement loop
- After the batch runs, `get_social_post_analytics` and update the calendar. Kill dead buckets after 2 weeks.

## Deliverables

- Monthly content calendar (chat table or cm-xlsx).
- Brief per piece (hook, format, song, CTA).
- Rendered videos via `render_chatmu_video`.
