---
name: chatmu-studio-breakbeats
description: >
  Programs breakbeats in Ableton Live using the 13 elements of funk drumming:
  ghost notes, kick doubles, open hi-hats, syncopated snare accents, rolls,
  hi-hat subdivision, triplets and 3-over-2 polyrhythm. For boom bap, lo-fi,
  hip-hop, DnB and dubstep. Trigger phrases: "breakbeat", "boom bap drums",
  "funk drums", "ghost notes", "break", "drum break", "hip-hop drums",
  "dnb drums", "jungle", "half-time", "make the drums groove".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Breakbeats built from the 13 elements of funk drumming"
version: "1.0"
tags: [studio, ableton, rhythm, breakbeat, drums, hip-hop, funk, boom-bap]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_fire
  - local_ableton_set_tempo
---

# Chatmu Studio — Breakbeats

**Card:** `music-kb/50_rhythm/breakbeats.md` (13 elements, tempos, build order, errors).
**Related:** `chatmu-studio-drums-by-genre`, `chatmu-studio-humanize`, `chatmu-studio-sampling`.

## When to use
When the user wants boom bap, lo-fi, hip-hop, funk, DnB, jungle or dubstep drums, or says
the drums "don't groove".

## Workflow

1. **Set tempo and feel.** Boom bap 80–95, DnB/jungle 160–180, dubstep ~140 half-time.
2. **Program the framework:** kick on 1 and 3, snare on 2 and 4, steady 8th or 16th hats.
3. **Add element 8** (steady 16th hi-hat) so the kick and snare lock.
4. **Add elements one at a time**, in this order: 4 (kick doubles), 1 (ghost snares),
   6 (syncopated accents), 5 (open hats sparingly), 9 (hat variation).
5. **Set velocities:** ghost notes 20–40, main snare 90–110, hats lower than snare.
6. **Add 11 or 13 only for a fill or a special bar.**
7. **Play it** with `local_ableton_fire`; if it does not make you nod, remove an element.
8. **Humanize only after** the quantized groove works.

## Hard rules
- One element per pass; never add three at once.
- Do not overuse the open hi-hat: it turns the break into disco.
- Do not quantize ghost notes so hard that the pocket disappears.
- Keep a steady hi-hat layer; it is the floor of the groove.
- Element 11 (triplets) and 13 (3-over-2) are spice, not the main pattern.
- Match the tempo to the genre before programming.

## Output
State tempo, feel, elements used and velocities. Then the MIDI written and a one-line
listening instruction. If it still does not groove, remove the last element added.
