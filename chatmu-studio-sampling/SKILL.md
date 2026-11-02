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
  - local_ableton_clip
  - local_stems_separate
  - local_ableton_devices
  - local_ableton_set_device_param
  - local_ableton_write_notes
  - local_ableton_fire
  - local_music_theory
---

# Chatmu Studio — Sampling

**Reference:** the tables and decision tree are at the end of this skill.
**Related:** `chatmu-studio-drums-by-genre`, `chatmu-studio-humanize`, `chatmu-studio-spatial-panning`.

## When to use
When the user wants to build a beat from an existing recording, chop a loop, flip a sample,
or asks whether a sample is "too long" or "clearable".

## Workflow

1. **Listen and measure.** Read tempo and key; note whether the section has vocals.
2. **Choose the sample type** (Reference): complete phrase, spare-part phrase, section
   piece, sound stab, sound tone.
3. **Capture** the section at a healthy level (no clipping). Keep the source file and note
   artist, title, timestamp.
4. **Chop**: bring the audio into Live with `local_ableton_create_audio_clip` (it places a file as a clip; it does not cut), split the source first with `local_stems_separate` if you need one stem, then set each chop's start/end with `local_ableton_clip` (`startMarker`/`endMarker`, `loopStart`/`loopEnd`): exact start on the attack, 2–5 ms fades. Warp mode and pitch also go through `local_ableton_clip` (`warpMode`, `pitchCoarse`).
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

## Reference


### What it solves
Turn an existing recording into a new beat: what to sample, how much, how to chop it,
how to fit tempo, how to transform it, and what the legal line is.

### Numbers

### How much to sample (BeatTips best practices)
| Bars used | Status |
|---|---|
| 1–4 consecutive bars | best practice |
| 5–8 bars | OK with substantial transformation or new context |
| 9–16 bars | possible only with significant transformation |
| 17+ bars | not best practice |
| single hits/stabs | de minimis by default |

Less is better. Transformation matters more than length. These are craft standards,
**not** legal permission.

### Sample types
| Type | What it is | Use |
|---|---|---|
| Complete phrase | 1+ bar with beginning/middle/end | ready-made loop |
| Spare-part phrase | part of a complete phrase | more original, harder to identify |
| Section piece | short, uneven fragment | needs support; trains chopping |
| Sound stab | single hit (kick, snare, horn) | layering, replacement |
| Sound tone | sustained multi-instrument fragment | texture, stabs |

### Chop and timing
| Parameter | Starting value |
|---|---|
| Phrase chop | 1/8–1/2 beat |
| Stutter chop | 1/16 beat |
| Fade in/out | 2–5 ms (avoid clicks, keep attack) |
| Swing (MPC) | 54–62% as a starting point |
| Dilla feel | not one value: some hits late 10–30 ms, some early |
| Boom bap tempo | 80–95 BPM |
| Lo-fi tempo | 70–90 BPM |
| Trap tempo | 130–150 BPM |

Warp vs re-pitch:
- **Warp** keeps pitch, changes time (Ableton: Beats / Tones / Texture).
- **Re-pitch** changes both (turntable-style); use for chipmunk or slow-down.

### Principles
1. **Dig first.** A great sample is a 1–2 bar phrase with open space, no vocals, and an
   interesting timbre. Intros often hide ready-made loops.
2. **Listen full, not only spot.** Spot-listening finds obvious loops; full listening finds
   the spare parts that make a beat original.
3. **Chop by attack, not by grid.** If the transient is late or clipped, the whole groove
   drags.
4. **Flip = change the context**, not just loop it: pitch, reverse, reorder, filter, layer,
   or change the drum frame.
5. **One primary sample is enough.** Classic beats are often one sample plus drums.
6. **Do not over-quantize.** If the source swings, keep some of it; otherwise the beat
   loses its pocket.
7. **Document the source** (artist, title, timestamp) before release. Clearance is a
   business step, not a mixing step.

### Decision tree
```
Source has vocals?        → filter, chop around them, or use the instrumental
Loop too fast/slow?       → warp (keep pitch) or re-pitch (change pitch)
Want boom bap?            → 1–2 bar loop, 1/8–1/4 chops, swing 54–60, low-pass
Want lo-fi?               → pitch down 1–3 semitones, low-pass, wow/flutter, noise
Want trap?                → 1/16 chops, pitch up, layer 808
Want Dilla feel?          → don't quantize all; nudge snares late 10–30 ms
Sample too recognizable?  → chop smaller, reorder, layer, change key/tempo
No clear loop?            → use stabs/section pieces; build from hits
```

### Workflow
1. **Dig**: pick the section; note BPM, key and whether it has vocals.
2. **Capture** at healthy level, no clipping; keep the source file.
3. **Chop**: exact start on the attack, end after the tail; 2–5 ms fades.
4. **Fit tempo**: warp if the pitch is right; re-pitch if the pitch should change.
5. **Flip**: pitch, reverse, reorder, filter, layer, or replay.
6. **Sequence**: drums first, then the chop; leave space for the vocal.
7. **Humanize**: only after the groove works quantized.
8. **Document**: source, timestamp, clearance status.

### Common errors
- Cutting the attack off: the chop loses punch.
- No fades: clicks and pops.
- Quantizing everything: no pocket.
- Stretching too far: warp artifacts.
- Sampling 17+ bars and calling it original.
- Sampling the "heart" of a famous song without transformation.
- Auto-chop without a musical idea: 32 slices, no groove.
- Forgetting the source: impossible to clear later.

### How it is validated
- **Ears `listen_spectrum`**: confirm the low-pass and the chop's tone.
- **Ears `listen_dynamics`**: the transient must survive the chop.
- **Ableton**: check warp markers; A/B against the original loop.
- **Mono check**: the chop must survive mono.
- **Legal**: best practices ≠ permission; clearance is separate.

### Checklist
- [ ] Is the sample 1–4 bars (or transformed if longer)?
- [ ] Does the chop start exactly on the attack?
- [ ] Are there 2–5 ms fades?
- [ ] Did you choose warp or re-pitch on purpose?
- [ ] Is the flip a real change of context?
- [ ] Does the groove keep its pocket?
- [ ] Is the source documented?
- [ ] Do you know the clearance status before release?
