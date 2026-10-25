---
name: chatmu-studio-drop-buildup
description: >
  Use in Co-Producer (Chatmu Desktop + Ableton Live) to build an electronic
  build-up and drop: 8 or 16 bars of tension (snare roll that accelerates,
  riser, white-noise sweep, filter that opens, pitch going up), removing kick
  and bass before the drop, a moment of silence, an impact on bar 1, and real
  energy contrast — written as MIDI and placed in the Arrangement with OK, and
  checked with Chatmu Ears (energy and low end before vs after the drop).
  Trigger phrases: "hazme un drop", "el drop no pega", "build-up", "buildup",
  "subida antes del drop", "que suba la tensión", "redoble antes del drop",
  "snare roll", "riser", "ruido blanco", "white noise", "que explote el
  coro", "impacto", "drop", "EDM", "house", "techno", "make a drop", "build
  up to the drop", "Arrangement", "Ableton".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Electronic build-up and drop: snare roll, riser, filter, cut before the drop, impact, verified with Ears"
version: "1.0"
tags: ["studio", "ableton", "drop", "build-up", "buildup", "riser", "edm", "house", "co-producer"]
requiresTools: ["local_ableton_snapshot", "local_ableton_arrangement", "local_ableton_edit_track", "local_ableton_load_devices", "local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_fire", "local_ableton_transport", "local_ableton_status", "local_ableton_undo", "local_synth_list_params", "local_synth_set_params", "local_ears_listen", "local_ears_render"]
---

# Chatmu Studio — Build-up & drop
**Version:** 1.0
**Requires:** Chatmu Desktop bridge + Ableton Live + Chatmu Ears.
**Uses:** `chatmu-studio-genre-templates` (lengths/tempos), `chatmu-studio-drums-by-genre` (patterns), `chatmu-studio-automation` (filter/volume moves), `chatmu-studio-arrangement` (where it sits), `chatmu-studio-sidechain` (the drop's pump), `chatmu-studio-sound-design` (riser/noise sounds).

## What does this Skill do?

A drop only hits if what comes before it takes energy away and builds tension. This skill
designs the last 8–16 bars before the drop and the first bar of it, writes what can be
written, and measures the contrast.

Answer in the user's language (usually Spanish). Show the plan as a bar-by-bar table.

## HARD RULES

1. **Contrast > loudness.** The drop must have more low end and density than the end of the
   build — not just be louder. The last 1–2 bars of the build lose kick and bass.
2. **New material on NEW tracks** ("Build Snare", "Riser", "Impact"), never inside the
   user's clips. Placing a Session clip in the Arrangement replaces that range on that track
   (`duplicate_from_session`, approval) — use those new tracks.
3. **Bars:** build = bars before the drop's bar 1 (e.g. drop at bar 65 → 16-bar build = 49–64).
4. Arrangement edits the tools can't do (cut the kick clip, split): tell the user exactly
   where (Cmd+E at bar X on track Y), or put the cut in the new material instead.
5. Plan → OK → write → Ears check → keep or `local_ableton_undo`.

## Phase 0 — Read

`local_ableton_snapshot` (+ `local_ableton_arrangement get_clips` on kick/bass/main
synths): tempo, genre, where the drop is (locator or ask), what plays in the build now.

## Phase 1 — The plan (8 or 16 bars)

| Compases (16-bar build) | Batería | Música | FX |
|---|---|---|---|
| 1–8 | kick on, snare on quarters | filter starts closing / music thins | noise riser starts low |
| 9–12 | snare in 8ths, kick may drop | filter opening, pitch riser starts | riser rising |
| 13–14 | snare in 16ths | bass out | riser + reverb growing |
| 15 | snare 32nds / triplets, velocity rising | kick and bass OUT | peak |
| 16 (last beat) | stop — 1 beat of silence or a vocal/FX tail | | reverse cymbal into the drop |
| Drop bar 1 | kick + bass + full chords | everything in | impact (crash + sub boom) |

8-bar build: compress the same arc (quarters 1–4, 8ths 5–6, 16ths 7, 32nds/stop 8).
Genre: house/techno builds are subtler (filter + percussion, rarely a full stop); EDM/future
bass go big (full roll, silence, impact); trap drops often use a vocal tag + 808 hit.

## Phase 2 — Write it

1. Tracks: `local_ableton_edit_track { action: "create_midi" }` (approval each) and rename.
   Load sounds in ONE `local_ableton_load_devices` call (a drum kit — not a bare
   "Drum Rack", see `chatmu-studio-drum-rack`; a Chatmu Synth for the riser if the user
   has it).
2. **Snare roll:** a 16-bar Session clip (`local_ableton_create_clip`) with notes from the
   table — quarters → 8ths → 16ths → 32nds, velocity ramping ~60 → 120
   (`local_ableton_write_notes`; pitch per kit, MIDI 38/40 = snare on GM-style kits; check
   the kit's pads).
3. **Riser:** on a Chatmu Synth track, one long note (or a slow upward line) for the build's
   length; noise + rising filter/pitch with `local_synth_list_params` → `local_synth_set_params`
   (or a riser sample the user has). Movement: `chatmu-studio-automation`.
4. **Impact:** a crash + low hit on bar 1 of the drop (one-bar clip).
5. Audition in Session first (`local_ableton_fire`), then with OK place each clip:
   `local_ableton_arrangement { action: "duplicate_from_session", trackIndex, clipIndex,
   beats }`.
6. Kick/bass out in the last bars: rule 4.

## Ears verification

Play from 4 bars before the end of the build through 4 bars of the drop
(`local_ableton_transport { action: "play", fromBeat }`), `local_ears_listen` for that length
(one call), then `local_ears_render { captureId, view: "loudness" }` and `"spectrogram"`.
Pass if: the low end (sub/low bands) is nearly gone in the last build bar and returns on the
drop, and the drop is ≥ 2–3 LU above the build's last bars (electronic: often more).
Report the numbers. If not, adjust one thing and re-measure; if you couldn't listen, say
**"no verificado"**.

## Don'ts

- Don't make the build louder than the drop.
- Don't write into the user's existing clips.
- Don't leave the drop without low end "for contrast" — the contrast is the build.
