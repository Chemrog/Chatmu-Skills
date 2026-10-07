---
name: chatmu-studio-humanize
description: >
  Use in Co-Producer to make MIDI in Ableton feel played instead of robotic:
  swing, micro-timing, velocity variation, accents, ghost notes, rolled chords,
  and when NOT to humanize. Works by rewriting note starts/velocities with
  write_notes. Trigger phrases: "humaniza", "humanizar", "humanize", "suena
  robótico", "muy cuadrado", "sounds robotic", "too stiff", "swing", "groove",
  "shuffle", "dale feel", "velocity", "más vivo", "cuantiza", "quantize".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Swing, timing and velocity humanization for Ableton MIDI, by genre"
version: "1.0"
tags: [studio, ableton, humanize, swing, groove, midi, co-producer]
requiresTools: ["local_ableton_get_notes", "local_ableton_write_notes", "local_ableton_status"]
---

# Chatmu Studio — Humanize
**Version:** 1.0
**Use with:** `chatmu-studio-compose-core`.

Live's Groove Pool is not reachable from the tools, so the feel is written into the
notes themselves: you read the clip, compute new `start` / `velocity` values and write
the clip back with `replace: true` + `expectClipName` (the user approves on screen).

## 1. Units

- `start` / `duration` are in **beats**. Convert milliseconds with
  **`beats = ms × BPM / 60000`** (tempo from `local_ableton_status`).
  At 90 BPM, 10 ms = 0.015 beat; at 128 BPM, 10 ms ≈ 0.021 beat.
- **Swing %** (MPC-style): 50 % = straight, 66.7 % = full triplet shuffle.
  - 16th swing: every EVEN 16th (steps 2, 4, 6 … = starts 0.25, 0.75, 1.25 …) moves
    later by **`(swing − 0.5) × 0.5` beats**. 58 % → +0.04 beat.
  - 8th swing: every off-beat 8th (starts 0.5, 1.5, 2.5 …) moves later by
    **`(swing − 0.5) × 1` beat**. 58 % → +0.08 beat.
  - Apply swing to the part that carries the subdivision (hats, shakers, keys), and
    the SAME amount to everything that should lock with it.

## 2. Amounts by genre

| Genre | Swing | Timing jitter | Velocity jitter | Notes |
|---|---|---|---|---|
| Lo-fi | 55–62 % | ±10–20 ms | ±10–20 | snare/chords may sit 5–20 ms late |
| Boom-bap | 54–60 % | ±5–15 ms | ±10–15 | |
| R&B / neo-soul | 55–62 % | ±5–15 ms | ±8–15 | |
| UK garage | 58–66 % | ±3–8 ms | ±8–12 | |
| Trap / drill | 50–54 % on hats | kick/808/clap 0–3 ms | hats ±10–20 | rolls stay tight |
| Reggaetón | 50 % (straight) | ±0–5 ms | ±5–10 | dembow must stay locked |
| Pop | 50–54 % | ±0–8 ms | ±5–10 | |
| House / deep house | 50–58 % on hats | kick 0 ms | ±5–10 | kick on grid |
| Techno | 50–52 % | kick 0 ms | ±3–8 | |

## 3. Rules

1. **Never move a four-on-the-floor kick** (house/techno/reggaetón) or the downbeat of
   bar 1. Keep `start ≥ 0` and inside the clip length.
2. **Accents over randomness:** hats louder on beats and "&", softer on "e"/"a"
   (e.g. 80 / 60). Then add small jitter on top.
3. Keep velocities in **1–127**. Notes the user set at 120+ or under 40 are intentional:
   keep them.
4. **Ghost notes:** snare at 25–45, max ~4 per bar, usually on "e"/"a" before a backbeat.
5. **Rolled chords (keys, lo-fi, R&B):** stagger chord tones 10–30 ms from bottom to top;
   pads/strings don't need it.
6. **Late feel:** lo-fi/neo-soul snares and chords can sit 5–20 ms late; never late the
   kick in a dance track.
7. **Don't exceed ±25 ms or ±25 velocity** — beyond that it sounds sloppy.
8. **Don't change pitches** while humanizing.
9. **Quantize, not destroy:** to tighten a recorded part, move each note 50–75 % of the
   way to the grid (keep feel) instead of 100 %, unless the user asks for full quantize.

## 4. Procedure

1. `local_ableton_get_notes` → keep the clip name for `expectClipName`.
2. Show a one-line plan: "16th swing 58 %, hats ±12 velocity, ±8 ms on snares, kick
   untouched. ¿Lo aplico?"
3. Compute the new notes (same pitches/durations; shorten a note if its new start would
   push its end past the next same-pitch note).
4. `local_ableton_write_notes` `{ trackIndex, clipIndex, notes, replace: true, expectClipName }`.
5. Play it and offer "more / less".

## Credits & license

Adapted and corrected from `midi-cleanup`, `groove-builder` and `tempo-coach` in
[glincker/ableton-skills](https://github.com/glincker/ableton-skills),
Copyright (c) 2026 Glincker, MIT License. Full text in
`LICENSE-glincker-ableton-skills.txt` in this folder.
