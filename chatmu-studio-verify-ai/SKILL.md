---
name: chatmu-studio-verify-ai
description: >
  Use in Co-Producer (Chatmu Desktop) when the user wants to MEASURE how much a
  song's audio reads as AI-generated with Chatmu's AI music detector, before
  and/or after remaking it (stems, Chatmu Synth, re-recording), and understand
  what the number means. Uploads the audio to the user's own Chatmu account
  only after they agree, runs the detector, and explains that it measures the
  AUDIO, not who composed the song. Trigger phrases: "¿esto suena a IA?",
  "mide el % de IA", "pásalo por el detector de IA", "verificar IA",
  "detector de IA antes y después", "¿cuánto IA tiene?", "is this AI",
  "AI detector", "check AI percentage".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Measure a song's AI-detector score before/after a remake and explain what it does and doesn't mean"
version: "1.0"
tags: ["studio", "ai-detector", "detector", "verificar-ia", "ia", "remake", "co-producer"]
requiresTools: ["local_upload_to_chatmu", "local_ableton_export", "local_search_files", "local_list_dir"]
---

# Chatmu Studio — Verify AI (detector before / after)
**Version:** 1.0
**Requires:** Chatmu Desktop signed in (upload) + the Chatmu MCP (cloud detector:
`open_chatmu_ai_music_detector`, `detect_ai_music_song`).
**Related:** `chatmu-studio-remake-song`, `chatmu-studio-separate-stems`.

## What does this Skill do?

Runs Chatmu's AI music detector on the user's audio (the original, and optionally the remade
version) and explains the result honestly.

Answer in the user's language (usually Spanish). Short.

## HARD RULES (positioning — non-negotiable)

1. **The detector measures the AUDIO, not the authorship.** It estimates whether the sound has
   the traits of AI-generated audio. It says nothing about who wrote the melody, chords or
   lyrics.
2. **Never promise or claim that a result "stops being AI", "is no longer AI", "is human now"
   or "can be distributed as human".** If a song started as an AI sketch, its composition still
   came from the AI after a remake; a lower score after resynthesis means the *sound* changed,
   not the origin. Distributors' and platforms' AI-disclosure rules still apply — tell the user
   to follow them.
3. **Never frame this as beating or fooling detectors.** The point of a remake is control and
   editability; the measurement is information, not a goal.
4. **Chatmu does not generate music.**
5. **Audio leaves the Mac only with an explicit yes**: "Para medirlo tengo que subir el audio a
   tu cuenta de Chatmu (queda privado en tu almacenamiento). ¿Lo subo?"

## Phase 1 — The audio

- A file the user has → its path (`local_search_files` / `local_list_dir` if needed).
- "After" of a remake → export the remade set first: `local_ableton_export` (WAV), with the
  same section as the "before" when possible (same length, same part of the song) so the two
  numbers are comparable.
- Already in their Chatmu catalog → `detect_ai_music_song { song_id }` directly (no upload).

## Phase 2 — Upload (after the yes) and detect

1. `local_upload_to_chatmu { path, purpose: "asset" }` → `publicUrl` (bytes go from the bridge
   to the user's own storage, never through the chat). `needs_login` → ask them to sign in to
   Chatmu Desktop.
2. `open_chatmu_ai_music_detector { audio_url: publicUrl, file_name }` → the detector's result.
3. Before/after: run it on both, one at a time, and keep both numbers.

## Phase 3 — Explain (short)

- The number: Chatmu's detector treats **above ~50% as "likely AI audio"** and below as "likely
  human-made audio". It is a probability from a model, with errors both ways; near 50% means
  "unclear".
- Before vs after: "El detector ve el audio rehecho con síntesis como menos parecido a audio de
  IA (98% → 12%). Eso habla del sonido, no de quién compuso la canción."
- Always close with rule 1 in one sentence. If the user asks whether they can now release it as
  100% human or skip an AI disclosure: no — the composition's origin hasn't changed; point to the
  distributor's AI policy.

## Maintainer note

The ~50% threshold comes from the issue (chatmu-desktop #2) and must be confirmed with Chema
against the detector's current calibration before this skill ships; update Phase 3 if it changes.

## Don'ts

- Don't upload without the yes. Don't run the detector in a loop "until it goes down".
- Don't suggest tweaks whose purpose is lowering the score.
