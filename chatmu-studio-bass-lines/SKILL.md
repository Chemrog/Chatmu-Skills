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
version: "1.1"
tags: ["studio", "ableton", "bass", "bajo", "808", "co-producer"]
requiresTools: ["local_ableton_get_notes", "local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_device_params", "local_ableton_set_device_param"]
---

# Chatmu Studio — Bass Lines
**Version:** 1.1
**Use with:** `chatmu-studio-compose-core` (pitch map: MIDI 60 = C3 in Live),
`chatmu-studio-harmony`, `chatmu-studio-drums-by-genre`.

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
| Rock | 8th-note root pulses locked to the kick (starts 0, 0.5 … 3.5, duration 0.4), approach note on 3.5 into the next chord; follows the guitar riff's rhythm when there is one; MIDI 28–48 |
| Funk / disco | octave jumps on 16ths (root 0, octave 0.5, root 0.75 …), ghost notes velocity 40–55, rests are part of the groove |
| R&B / neo-soul | sub-bass root on 1 held ~1.5 beats, chromatic approach on 3.75 into the next root; sometimes the 3rd or 7th of the chord on beat 3; behind the beat by 10–20 ms |
| Techno | 16th-note rolling bass on the root (off the kick: steps 2–4, 6–8…), or one sustained sub note per bar; few pitch changes |
| UK garage | swung syncopated bass (starts 0, 0.75, 1.75, 2.5), short notes, octave stabs |
| Regional mexicano (banda / norteño) | tuba / tololoche "oom-pah": root on 1 and 5th on 3 (or 2 and 4 in 2/4 polka feel: root on 0, 5th on 1), walking runs between chords on the last beat; corridos tumbados: 808-style long root under the requinto |
| Cumbia | root on 1, 5th on 2.5 / root on 3 (quarter + 8th pattern), very steady; bass follows the güira/guacharaca |
| Salsa | tumbao: anticipated root on the "and" of 2 (1.5) tied over, 5th on 4 (3); beat 1 is usually silent |
| Bachata | syncopated arpeggio: root 0, 5th 0.5, octave 1.5, 5th 2 …, slides into chord changes |
| Afrobeats | syncopated, sparse: root 0, then 1.75 and 2.5 or 3.25; leaves space for the percussion; amapiano: log drum (pitched percussive bass) on 16th-note syncopations with pitch drops |
| Ambient | drone on the root for 2–8 bars or no bass at all; swell in with slow attack (≥ 300 ms) |
| Cinematic | low strings/brass on roots and 5ths in whole notes; ostinato in 8ths for tension |
| Jazz | walking bass: one note per beat, chord tone on 1, scale/chromatic approach on 4 into the next chord's root; MIDI 28–55 |

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
