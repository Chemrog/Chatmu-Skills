---
name: chatmu-studio-spatial-panning
description: >
  Places every element in the stereo field and in depth (front-to-back) in
  Ableton Live: panning, LCR/opposition, reverb sends, pre-delay and 5 depth
  planes, with mono compatibility. Trigger phrases: "panning", "pan", "stereo
  image", "width", "depth", "space", "reverb", "planes", "mono", "mix sounds flat".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Panning, depth planes and reverb sends that survive mono"
version: "1.0"
tags: [studio, ableton, mixing, panning, stereo, depth, reverb]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_tracks
  - local_ableton_mixer
  - local_ableton_apply
  - local_ableton_devices
  - local_ableton_set_device_param
  - local_ableton_fire
---

# Chatmu Studio — Space & panning

**Card:** `music-kb/70_mixing/space-and-panning.md` (numbers, planes, decision tree, errors).
**Related:** `chatmu-mixing-progressive`, `chatmu-studio-listen-troubleshooting`.

## When to use
When a mix sounds flat, crowded, too wide, too narrow, or an element disappears in mono.
Not for EQ/compression problems; those go to `chatmu-mix-eq` / `chatmu-mix-compression`.

## Workflow

1. **Read the session:** `local_ableton_snapshot` and `local_ableton_tracks` (indexes, names,
   current pan/volume/sends).
2. **Classify into planes** (card table): 1 lead/kick/snare/bass, 2 main instruments,
   3 rhythmic/harmonic bed, 4 pads/ambience, 5 FX.
3. **Center the core:** kick, snare, bass, lead vocal at pan 0. Do not move them to fix
   a frequency problem.
4. **Pan the rest by opposition:** if a main element goes left, put a comparable one right.
   Prefer discrete positions (L/C/R or 40/40, 70/70) over random soft pans.
5. **Set depth:** more reverb and less top-end for farther planes; less reverb and sharper
   transients for closer ones. Reverb as send, 100% wet, post-fader.
6. **Write the moves** with `local_ableton_apply` in one batch (`type: "mixer"`,
   `property: "panning" | "volume" | "send"`).
7. **Mono check:** sum to mono and confirm nothing important disappears.
8. **Report** the plane map and what changed, then let the user listen.

## Hard rules
- Kick, snare, bass and lead vocal stay centered.
- Never hard-pan an element that must survive one-sided playback unless it has an opposite.
- Reverb must be a send, 100% wet, post-fader. No dry/wet insert for shared reverb.
- High-pass the reverb return (200–400 Hz) unless the genre wants wash.
- Depth is contrast: if everything has reverb, nothing is in front.
- Check mono before declaring the panning done.
- Do not use a stereo widener to fake width that the arrangement does not have.

## Output
A short map: element → plane → pan → send. Then the list of mixer changes applied.
If something cannot be verified (no Ableton control), say so and give the exact values
for the user to set manually.
