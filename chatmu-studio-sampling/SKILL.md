---
name: chatmu-studio-sampling
description: >
  Turns an existing recording into a new beat in Ableton Live: choose what to
  sample, dig for a phrase, chop by attack, fit tempo with warp or re-pitch,
  flip the sample (pitch, reverse, reorder, filter, layer), program drums and
  document the source for clearance. Trigger phrases: "sample", "sampling",
  "chop", "flip", "loop", "boom bap", "lo-fi beat", "sample this record",
  "remake this beat", "sample clearance".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Dig, chop, flip and clear a sample into a new beat"
version: "1.0"
tags: [studio, ableton, sampling, chop, flip, hip-hop, lo-fi, boom-bap]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_create_audio_clip
  - local_ableton_devices
  - local_ableton_set_device_param
  - local_ableton_write_notes
  - local_ableton_fire
  - local_music_theory
---

# Chatmu Studio — Sampling

**Card:** `music-kb/60_sampling/chop-and-flip.md` (numbers, types, decision tree, errors).
**Related:** `chatmu-studio-drums-by-genre`, `chatmu-studio-humanize`, `chatmu-studio-spatial-panning`.

## When to use
When the user wants to build a beat from an existing recording, chop a loop, flip a sample,
or asks whether a sample is "too long" or "clearable".

## Workflow

1. **Listen and measure.** Read tempo and key; note whether the section has vocals.
2. **Choose the sample type** from the card: complete phrase, spare-part phrase, section
   piece, sound stab, sound tone.
3. **Capture** the section at a healthy level (no clipping). Keep the source file and note
   artist, title, timestamp.
4. **Chop** with `local_ableton_create_audio_clip`: exact start on the attack, 2–5 ms fades.
5. **Fit tempo**: warp (keep pitch) or re-pitch (change pitch). Say which and why.
6. **Flip** with devices/params: pitch, reverse, reorder, filter, layer. A flip must change
   the context, not just loop the original.
7. **Program drums** (`chatmu-studio-drums-by-genre`); leave space for the vocal.
8. **Humanize** only after the quantized groove works.
9. **Report** source, bars used, warp mode, flip and clearance status.

## Hard rules
- 1–4 bars is best practice; 5–8 needs substantial transformation; 17+ is not best practice.
- Never cut the attack off a chop.
- Always add 2–5 ms fades.
- Do not quantize everything: if the source swings, keep some of it.
- Do not stretch a sample so far that artifacts appear; re-pitch or choose another section.
- Best practices are craft standards, not legal clearance. Say so explicitly.
- Never claim a sample is cleared; only the user or their lawyer can confirm that.

## Output
A one-block summary: source, bars used, sample type, chop length, warp/re-pitch, flip,
drums, clearance status. Then the changes applied in Ableton.
