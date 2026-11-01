---
name: chatmu-studio-club-grooves
description: >
  Builds club grooves in Ableton Live for house, techno, trance, drum & bass,
  dubstep and chill-out: correct tempo, kick/snare/hat grid, bass placement and
  8/16/32-bar structure. Trigger phrases: "house groove", "techno", "trance",
  "drum and bass", "dnb", "jungle", "dubstep", "chill-out", "four on the floor",
  "club beat", "edm drums".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Club grooves: tempo, drum grid, bass and structure by genre"
version: "1.0"
tags: [studio, ableton, genres, house, techno, trance, dnb, dubstep, groove]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_fire
  - local_ableton_set_tempo
---

# Chatmu Studio — Club grooves

**Card:** `music-kb/20_genres/electronic-genres.md` (BPM, grids, structure, errors).
**Related:** `chatmu-studio-drums-by-genre`, `chatmu-studio-sidechain`, `chatmu-studio-drop-buildup`.

## When to use
When the user asks for house, techno, trance, drum & bass, jungle, dubstep or chill-out,
or says a club track "doesn't feel like the genre".

## Workflow

1. **Set the genre and tempo** from the card.
2. **Program the grid:**
   - House/techno/trance: kick on 1, 2, 3, 4; clap on 2 and 4.
   - House: open hat on the offbeats (3, 7, 11, 15 in 16ths), closed hat on all 16.
   - DnB: 2-step, snare on 2 and 4 plus ghost snares; kick syncopated.
   - Dubstep: half-time, kick on 1, snare on 3.
3. **Place the bass in the holes** left by the kick; sidechain if it fights.
4. **Add structure** in 8/16/32-bar blocks: intro, build, drop, breakdown.
5. **Play it** with `local_ableton_fire`; A/B against a reference at the same BPM.
6. **Only then** add texture and automation.

## Hard rules
- One genre at a time: do not mix DnB tempo with a house kick.
- Dubstep snare goes on 3, not 2 and 4.
- DnB is 2-step: ghost snares matter more than the main snare.
- Keep the offbeat open hat in house; it is the signature.
- One polyrhythm at a time.
- Leave room for the kick in the bass.
- Do not change chords every bar in techno; manage energy, not song form.

## Output
State genre, BPM, grid (kick/snare/hat), bass placement and structure. Then the MIDI
written and one reference to compare against.
