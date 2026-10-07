---
name: chatmu-studio-bass-lines
description: >
  Use in Co-Producer to write basslines and 808s in Ableton Live that follow
  the chords and lock with the kick: root/octave/fifth patterns, approach notes,
  808 glides, off-beat house bass, reggaetón tresillo bass. Trigger phrases:
  "bajo", "línea de bajo", "bassline", "bass line", "808", "sub", "slide 808",
  "glide", "bajo de reggaetón", "bajo de house", "el bajo choca con el bombo",
  "bass clashes with kick".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Basslines and 808s that follow the chords and lock with the kick"
version: "1.0"
tags: [studio, ableton, bass, bajo, 808, co-producer]
requiresTools: ["local_ableton_get_notes", "local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_device_params", "local_ableton_set_device_param"]
---

# Chatmu Studio — Bass Lines
**Version:** 1.0
**Use with:** `chatmu-studio-compose-core` (pitch map: MIDI 60 = C3 in Live),
`chatmu-studio-harmony-voicing`, `chatmu-studio-drums-by-genre`.

## 1. Before writing

1. Read the chords (`local_ableton_get_notes` on the chord clip) → the root of each chord
   and when it changes.
2. Read the kick (drum clip, pitch 36) → kick positions in beats.
3. Bass is **monophonic**: one note at a time. Overlap notes only on purpose (glides).
4. Range: bass **28–55**, 808/sub **24–43**. Pick the octave so the key's root sits around
   MIDI 33–45 (A0–A1 in Live naming for A = 33/45).

## 2. Core rules

1. Land the **chord root on the downbeat** where the chord changes.
2. Between changes, use **root, octave, 5th**; the 3rd/7th sparingly (on weak beats).
3. **Approach notes:** in the last 8th/16th before a chord change, step into the new root
   from a scale step or a semitone above/below.
4. **Lock with the kick** in hip-hop/trap/pop/R&B (bass starts with kick hits). In house,
   do the opposite: bass on the off-beats between kicks.
5. **Leave space** for the kick transient: when bass and kick start together, the kick
   should win (sidechain or shorter bass attack); offer sidechain only if the user wants it.

## 3. Patterns by genre (start / duration in beats, per bar)

| Genre | Pattern |
|---|---|
| Reggaetón | tresillo every 2 beats: starts 0, 0.75, 1.5, 2, 2.75, 3.5 (durations 0.75, 0.75, 0.5); root, octave on the 2nd hit optional |
| House / deep house | off-beat: starts 0.5, 1.5, 2.5, 3.5, duration 0.25–0.4; root or root+octave; deep house adds 7th/9th passing notes |
| Trap / drill 808 | one long note per kick, each lasting until the next kick; mostly the root; glides to the octave, 5th or ♭7 |
| Lo-fi / R&B | root on 1 (long), passing/approach notes on beats 3–4, slides; follow chord tones |
| Pop | 8th-note root pulses (starts 0, 0.5 … 3.5, duration 0.45) or root on 1 + syncopation on 2.5 |
| Drum & bass | long sub notes (1–2 bars) or Reese riff on the root/♭3/5th |

## 4. 808 glide (portamento)

A glide needs **two things**: overlapping notes in MIDI (the next note starts before the
previous ends, e.g. previous `start 2, duration 1.25`, next `start 3`) **and** a mono
instrument with glide/portamento turned on. Check the instrument's parameters with
`local_ableton_device_params` and set them with `local_ableton_set_device_param` only
after telling the user which parameter you will change. Parameter names differ per
device — read them, don't guess. If the device has no glide, say so and offer a
different 808 (`local_ableton_load_device`).

## 5. Example — reggaetón bass for Am–F–C–G (1 bar per chord)

Roots: A = 45, F = 41, C = 48, G = 43. Bar 1 (A), relative to the clip start:

```json
[{"pitch":45,"start":0,"duration":0.7,"velocity":110},
 {"pitch":45,"start":0.75,"duration":0.7,"velocity":100},
 {"pitch":45,"start":1.5,"duration":0.45,"velocity":95},
 {"pitch":45,"start":2,"duration":0.7,"velocity":110},
 {"pitch":45,"start":2.75,"duration":0.7,"velocity":100},
 {"pitch":43,"start":3.5,"duration":0.45,"velocity":95}]
```

The last note (43 = G) is an **approach note**: it steps down a whole tone into the next
root F (41) on beat 1 of bar 2. Any scale step or semitone next to the new root works.
Bars 2–4: same rhythm, add 4 beats per bar, on 41, 48, 43.

## Don'ts

- Don't write chords in the bass track.
- Don't put the bass in the same register as the chords' lowest voice.
- Don't let 808 notes overlap unless you want a glide.
- Don't put a busy bass under a busy kick: one of them leads.
