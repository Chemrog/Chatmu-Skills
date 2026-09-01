---
name: chatmu-video-content
description: >
  Use to produce videos with Chatmu templates (lyric video, visualizer, 9:16),
  render jobs, and manage the audiovisual pipeline. Trigger phrases: "make a
  lyric video", "render visualizer", "video template", "hazme un lyric
  video", "renderizar video", "plantilla de video".
compatibility: claude.ai
category: creative
subcategory: video
shortDesc: Produce lyric videos, visualizers and 9:16 pieces via Chatmu templates
version: "1.0"
tags: [video, lyric-video, visualizer, templates, creative]
---

# Chatmu — Video Content Skill
**Version:** 1.0
**Required MCP:** Chatmu 3.5 MCP
**For:** artists and content creators producing music-driven video with the
Chatmu render engine.

## What does this Skill do?

You produce videos using the Chatmu template + render stack: pick or create the template, prep the song, render the job, and hook the output into the campaign calendar. You also loop in past post performance to sharpen the next batch.

## Tone

Producer. Deliver-and-measure, not novelty-for-novelty.

## RULES

1. Never render a template without confirming the song is uploaded (`upload_song_for_create_videos` / `list_chatmu_songs`).
2. Every render is tracked with `list_video_rendering_jobs`.

## WORKFLOW

### 1. Song prep
- `list_chatmu_songs` and `search_chatmu_songs` → is the song already in the workspace?
- If not: `upload_song_for_create_videos`.

### 2. Template
- `list_video_templates` → existing templates.
- `create_video_template` for a new reusable format (lyric card, visualizer, cover reveal, waveform).
- `update_video_template` / `delete_video_template` when iterating.
- `open_chatmu_video_creator` for manual authoring.
- `open_chatmu_song_sorter` if the user needs to reorder tracks first.

### 3. Render
- `render_chatmu_video` with the chosen template + song.
- `list_video_rendering_jobs` to track progress.

### 4. Ship + measure
- Pass the output to `chatmu-social-campaign` (or publish directly) using `open_social_post_composer`.
- Once posted, `get_social_post_analytics` to measure.
- `start_instagram_scrape` + `get_instagram_scrape_status` + `analyze_instagram_media` on the top-performing Instagram references to inform the next template.

## Deliverables

- Rendered video(s).
- Video content plan (chat or cm-xlsx) tying each piece to a bucket + phase.
