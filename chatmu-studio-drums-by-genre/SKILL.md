---
name: chatmu-studio-drums-by-genre
description: >
  Use in Co-Producer to write drum patterns (batería, beat, groove) into an
  Ableton Drum Rack by genre: reggaetón/dembow, trap, drill, lo-fi, boom-bap,
  house, deep house, tech house, techno, drum & bass, UK garage, pop, R&B.
  Correct 16-step grids, Drum Rack note map, velocities and swing. Trigger
  phrases: "batería", "hazme un beat", "drums", "drum pattern", "groove",
  "dembow", "reggaetón", "beat de trap", "hi-hats", "hats", "rolls", "bombo",
  "caja", "kick", "snare", "clap", "four on the floor", "half-time".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Genre-correct drum patterns for Ableton Drum Rack (dembow, trap, house, lo-fi…)"
version: "1.0"
tags: [studio, ableton, drums, batería, reggaeton, trap, house, co-producer]
requiresTools: ["local_ableton_snapshot", "local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_load_device"]
---

# Chatmu Studio — Drums by Genre
**Version:** 1.0
**Use with:** `chatmu-studio-compose-core` (clip flow), `chatmu-studio-humanize` (feel).

## 1. Setup

1. `local_ableton_snapshot` → find the drum track (a MIDI track with a **Drum Rack**). If
   there is none, offer to create a MIDI track (`local_ableton_edit_track` `create_midi`,
   approval) and load a kit (`local_ableton_load_device` with a kit name found via
   `local_ableton_browser` path `drums`). Never claim a kit is loaded without checking.
2. Create the clip: `local_ableton_create_clip` (1–2 bars = 4–8 beats; up to 8 bars).
3. Write with `local_ableton_write_notes`; one call per clip with all the hits.

## 2. Drum Rack note map (General-MIDI layout used by Live's kits)

| Pad | MIDI | Live name | | Pad | MIDI | Live name |
|---|---|---|---|---|---|---|
| Kick | 36 | C1 | | Closed hat | 42 | F#1 |
| Rim / side stick | 37 | C#1 | | Pedal hat | 44 | G#1 |
| Snare | 38 | D1 | | Open hat | 46 | A#1 |
| Clap | 39 | D#1 | | Crash | 49 | C#2 |
| Low tom | 41/43 | F1/G1 | | Ride | 51 | D#2 |

Kits differ (some put percussion or 808 on other pads). If a pad sounds wrong, ask
the user or listen, and adjust the pitch numbers — don't insist on the table.

## 3. Grid → beats

A 4/4 bar has 16 sixteenth-steps. **Step n starts at beat `(n − 1) × 0.25`.**

| Step | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 |
|---|---|---|---|---|---|---|---|---|
| Count | 1 | 1& | 2 | 2& | 3 | 3& | 4 | 4& |
| Beat | 0 | 0.5 | 1 | 1.5 | 2 | 2.5 | 3 | 3.5 |

Even steps are the "e"/"a" 16ths (step 4 = "1a" = beat 0.75, step 8 = "2a" = 1.75).
For bar 2 add 4 beats. Drum hit `duration`: 0.25 (one-shots ignore length; keep it short).

**Backbeat vs half-time** (the classic mistake):
- **Backbeat:** snare/clap on beats **2 and 4** = steps **5 and 13**. Lo-fi, boom-bap, pop,
  R&B, house, DnB all use it.
- **Half-time:** snare/clap only on beat **3** = step **9**. Trap and drill at 130–150 BPM
  use it, which makes them *feel* like 65–75 BPM. Snare on 2 and 4 is **not** half-time.

## 4. Patterns (1 bar, X = hit; steps 1–16)

```
REGGAETÓN / DEMBOW — 88–100 BPM (most hits 90–96), straight (no swing)
Kick   X . . . X . . . X . . . X . . .   steps 1 5 9 13 (every beat)
Snare  . . . X . . X . . . . X . . X .   steps 4 7 12 15 (the dembow: "1a", "2&", "3a", "4&")
Hat    X . X . X . X . X . X . X . X .   8ths (or 16ths, low velocity)
```
Layer a rim (37) or clap (39) with the snare for the classic timbale/"tumba" colour.

```
TRAP — 130–150 BPM, HALF-TIME
Kick   X . . . . . . . . . X . . . . .   steps 1 11 (vary per bar; 808 follows the kick)
Clap   . . . . . . . . X . . . . . . .   step 9 only (beat 3)
Hat    X . X . X . X . X . X . X . X .   8ths, add rolls: 1/32 (0.125 beat) or
                                           1/16-triplets (1/6 ≈ 0.1667 beat) into beat 3 or 4
OpHat  occasional on step 15
```

```
UK DRILL — 138–145 BPM, HALF-TIME
Same skeleton as trap (snare/clap on step 9), with skippy triplet hats, a displaced
extra snare in the 2nd bar, and sliding 808s (see chatmu-studio-bass-lines).
```

```
LO-FI HIP-HOP — 70–90 BPM, BACKBEAT, swung
Kick   X . . . . . . . . . X . . . . .   steps 1 11 (+ step 8 for variation)
Snare  . . . . X . . . . . . . X . . .   steps 5 13 (beats 2 & 4 — backbeat, NOT half-time)
Hat    X . X . X . X . X . X . X . X .   8ths, swing 55–62 %, velocities 55–85
```

```
BOOM-BAP — 85–95 BPM, backbeat, swung
Kick   X . . . . . . X . . X . . . . .   steps 1 8 11
Snare  . . . . X . . . . . . . X . . .   steps 5 13
Hat    X . X . X . X . X . X . X . X .   8ths or 16ths, swing 54–60 %
```

```
HOUSE / DEEP HOUSE — 118–126 BPM (deep 118–124)
Kick   X . . . X . . . X . . . X . . .   four on the floor
Clap   . . . . X . . . . . . . X . . .   beats 2 & 4
OpHat  . . X . . . X . . . X . . . X .   OFF-BEAT "&": steps 3 7 11 15
CHat   16ths at low velocity (optional), swing 52–58 % (deep house more)
```

```
TECH HOUSE / TECHNO — 124–128 / 128–140 BPM
Kick four on the floor; clap or snare on 2 & 4 (techno often only a ride/hat on the
off-beats); 16th closed hats with accents on the off-beats; syncopated percussion.
Kick stays on the grid.
```

```
DRUM & BASS — 170–176 BPM, two-step (full-time backbeat)
Kick   X . . . . . . . . . X . . . . .   steps 1 11
Snare  . . . . X . . . . . . . X . . .   steps 5 13 (beats 2 & 4 at 174 — NOT half-time)
Hat    8ths or 16ths; ghost snares at velocity 25–45 on steps 8 / 15
Half-time DnB variant: snare only on step 9.
```

```
UK GARAGE (2-step) — 130–136 BPM, heavily swung
Kick   X . . . . . . . . . X . . . . .   steps 1 11 (no four-on-the-floor)
Snare  . . . . X . . . . . . . X . . .   steps 5 13
Hat    off-beats + 16th shuffle, swing 58–66 %
```

```
POP — 100–125 BPM
Kick   X . . . . . . . X . X . . . . .   steps 1 9 11
Snare  . . . . X . . . . . . . X . . .   steps 5 13
Hat    8ths
```

```
R&B — 60–80 BPM (if the set is at double tempo, read snare on step 9)
Kick   X . . . . . . X . . X . . . . .   steps 1 8 11
Snare  . . . . X . . . . . . . X . . .   steps 5 13 (snaps/rim layered)
Hat    16ths, swing 55–62 %, occasional 1/32 or triplet runs
```

## 5. Velocities

| Part | Velocity |
|---|---|
| Kick | 100–120 |
| Snare / clap | 95–115 |
| Ghost snare | 25–45 |
| Hats on beats / "&" | 70–90 |
| Hats on "e"/"a" | 50–70 |
| Open hat | 75–95 |

Then apply `chatmu-studio-humanize` (swing, timing, velocity) — except four-on-the-floor kicks.

## 6. Example call — 1 bar of dembow

```json
{ "trackIndex": 0, "clipIndex": 0, "notes": [
  {"pitch":36,"start":0,"duration":0.25,"velocity":112},
  {"pitch":36,"start":1,"duration":0.25,"velocity":108},
  {"pitch":36,"start":2,"duration":0.25,"velocity":112},
  {"pitch":36,"start":3,"duration":0.25,"velocity":108},
  {"pitch":38,"start":0.75,"duration":0.25,"velocity":100},
  {"pitch":38,"start":1.5,"duration":0.25,"velocity":104},
  {"pitch":38,"start":2.75,"duration":0.25,"velocity":100},
  {"pitch":38,"start":3.5,"duration":0.25,"velocity":104},
  {"pitch":42,"start":0,"duration":0.25,"velocity":80},
  {"pitch":42,"start":0.5,"duration":0.25,"velocity":65},
  {"pitch":42,"start":1,"duration":0.25,"velocity":80},
  {"pitch":42,"start":1.5,"duration":0.25,"velocity":65},
  {"pitch":42,"start":2,"duration":0.25,"velocity":80},
  {"pitch":42,"start":2.5,"duration":0.25,"velocity":65},
  {"pitch":42,"start":3,"duration":0.25,"velocity":80},
  {"pitch":42,"start":3.5,"duration":0.25,"velocity":65}
]}
```

## 7. Fills and variation

- 2-bar phrases: bar 2 = bar 1 with one change (extra kick, hat roll, open hat).
- Fill in the last 1–2 beats of bar 4 or 8 (snare 16ths rising in velocity, tom run,
  hat roll). Ghost notes: max ~4 per bar.

## Corrections vs. the upstream material

- Lo-fi "snare on 5 & 13 for half-time feel" → steps 5 & 13 are the **backbeat**
  (beats 2 & 4); half-time is step 9.
- Trap snare on steps 5 & 13 → trap is half-time: **step 9**.
- House open hat on steps 2/6/10/14 → the off-beat open hat is on the "&": **3/7/11/15**.
- DnB "snare on 2 & 4 (half-time feel)" → that is the normal two-step backbeat at 174.
- Lo-fi summary "kick on 1+3" while the grid had steps 1 and 7 → grids and text now match.

## Credits & license

Adapted and corrected from `groove-builder` in
[glincker/ableton-skills](https://github.com/glincker/ableton-skills),
Copyright (c) 2026 Glincker, MIT License. Full text in
`LICENSE-glincker-ableton-skills.txt` in this folder.
