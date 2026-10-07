---
name: chatmu-studio-compose-core
description: >
  Use in Co-Producer whenever you write MIDI into Ableton Live: a melody,
  chords, a bassline, an arpeggio or a drum pattern. Covers the composing flow
  (create_clip + write_notes), the pitch map (MIDI 60 = C3 in Live), ranges
  per instrument and melody-writing rules. Trigger phrases: "hazme una
  melodía", "melodía", "melody", "escribe acordes", "acordes", "chords",
  "componer", "compose", "haz un loop", "make a beat", "progresión", "MIDI",
  "notas", "write notes", "arpegio", "arpeggio", "Ableton".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Compose MIDI in Ableton: clip flow, pitch map, ranges, melody rules"
version: "1.0"
tags: [studio, ableton, compose, melody, melodía, midi, co-producer]
requiresTools: ["local_ableton_snapshot", "local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_get_notes", "local_ableton_fire"]
---

# Chatmu Studio — Compose Core
**Version:** 1.0
**Requires:** Chatmu Desktop (Co-Producer) bridge + Ableton Live (AbletonMCP control surface).
**Load with:** `chatmu-studio-harmony-voicing` (chords), `chatmu-studio-drums-by-genre`
(drums), `chatmu-studio-bass-lines`, `chatmu-studio-humanize`, `chatmu-studio-genre-templates`.

## The flow (do it in this order)

1. **Brief.** Genre, tempo, key/scale, mood, length. If two or more are missing ask ONE
   short question; otherwise use the genre defaults in `chatmu-studio-genre-templates`.
2. **Read the set:** `local_ableton_snapshot` (add `includeNotes: true` only if you need
   to match existing parts — it can be large). Note the tempo, MIDI tracks and their
   instruments, empty clip slots, and existing clips you must not clash with.
3. **Tempo:** only change it with the user's OK (`local_ableton_set_tempo`) — it shifts
   everything already in the set.
4. **Write in this order:** harmony (chords) → bass → drums → melody → humanize → listen.
5. **Create the clip:** `local_ableton_create_clip` `{ trackIndex, clipIndex, lengthBeats, name }`.
   The slot must be EMPTY (it refuses occupied slots). `lengthBeats` in 4/4 = bars × 4.
   Name clips clearly: "Chords A", "Bass A", "Drums A", "Lead A".
6. **Write notes:** `local_ableton_write_notes` `{ trackIndex, clipIndex, notes: [{ pitch, start, duration, velocity }] }`.
   - `start` and `duration` are in **beats** from the clip start (1 beat = quarter note,
     0.5 = eighth, 0.25 = sixteenth, 1/3 ≈ 0.3333 = eighth-note triplet).
   - Notes are ADDED by default. To rewrite a clip use `replace: true` AND
     `expectClipName` (the clip's current name, `""` if unnamed). The user approves on screen.
   - If a write times out, call `local_ableton_get_notes` before retrying — the notes may
     already be there.
7. **Check:** `local_ableton_get_notes` and compare with what you meant to write.
8. **Play & listen:** `local_ableton_fire` `{ action: "clip" }` (or the scene), then follow
   `chatmu-studio-listen-troubleshooting`. Offer 1–2 concrete changes, not ten.

Write at most 8 bars per idea; let the user react before writing more.

## Pitch map (critical)

Ableton labels **MIDI 60 as C3** (not C4). Formula: `MIDI = 12 × (LiveOctave + 2) + pitchClass`
with C=0, C#=1, D=2, D#=3, E=4, F=5, F#=6, G=7, G#=8, A=9, A#=10, B=11.

| Live name | MIDI | | Live name | MIDI |
|---|---|---|---|---|
| C0 | 24 | | C3 | 60 |
| C1 | 36 | | C4 | 72 |
| C2 | 48 | | C5 | 84 |

Always reason in MIDI numbers. When you quote a note name to the user, say which
convention ("C3 in Ableton, middle C").

**Working ranges (MIDI):**

| Part | Range | Notes |
|---|---|---|
| Sub / 808 | 24–43 | fundamentals; one note at a time |
| Bass (synth/electric) | 28–55 | roots, fifths, octaves |
| Chords / keys / pads | 48–79 | no 3rds or 7ths below ~52 (mud) |
| Lead / melody / vocal-like | 60–84 | sing-able span ~ an octave and a half |
| Drum Rack | 36–51 | see `chatmu-studio-drums-by-genre` |

Before writing a part, check the neighbouring parts' ranges (`get_notes`) so the
melody does not sit on top of the chords' top voice and the bass does not double the
kick's fundamental for every note.

## Scales (semitone steps from the root)

| Scale | Intervals | Typical use |
|---|---|---|
| Major (Ionian) | 0 2 4 5 7 9 11 | pop, uplifting |
| Natural minor (Aeolian) | 0 2 3 5 7 8 10 | reggaetón, trap, pop, EDM |
| Harmonic minor | 0 2 3 5 7 8 11 | trap/drill melodies, Latin, "dark" leads (raised 7th → major V) |
| Dorian | 0 2 3 5 7 9 10 | deep house, lo-fi, neo-soul (minor with a major 6th) |
| Phrygian | 0 1 3 5 7 8 10 | dark trap, flamenco colour (♭2) |
| Mixolydian | 0 2 4 5 7 9 10 | funk, rock, house vamps (major with ♭7) |
| Minor pentatonic | 0 3 5 7 10 | hooks, bass, guitar-like riffs |
| Major pentatonic | 0 2 4 7 9 | pop hooks, R&B runs |

Every melody/bass note must belong to the chosen scale unless it is a deliberate
passing/chromatic note on a weak beat, resolved by step on the next note.

## Melody rules

1. **Motif first.** Write a 1–2 bar motif, then repeat it with variation
   (question → answer): same rhythm with a different ending, or same contour shifted.
   A 4-bar phrase is usually A A' or A B; 8 bars: A A' A B'.
2. **Strong beats get chord tones.** On beats 1 and 3 (and long notes) use the root,
   3rd or 5th of the chord under it (7th/9th allowed in jazzy genres). Non-chord tones go
   on weak positions and resolve by step.
3. **Mostly steps, few leaps.** After a leap larger than a 4th, move back by step in the
   opposite direction.
4. **One peak per phrase.** The highest note appears once, ideally in the 2nd half.
5. **Leave space.** Rests are part of the melody; don't fill every 16th. Leave room for a
   vocal if the track will have one.
6. **Rhythm follows the genre:** syncopated 16ths in reggaetón/R&B, sparse long notes in
   lo-fi, short repeated stabs/plucks in house, triplet flows in trap.
7. **End phrases on stable tones** (root or 3rd) at the end of 4 or 8 bars.

## Don'ts

- Don't write every note at velocity 100 on the exact grid — see `chatmu-studio-humanize`.
- Don't stack root-position triads in the same octave as the bass.
- Don't overwrite a user's clip without `replace` + `expectClipName` + saying so.
- Don't change tempo/key of the whole set without asking.

## Credits & license

Parts of this workflow are adapted and corrected from
[glincker/ableton-skills](https://github.com/glincker/ableton-skills) (`producer-mode`, `chord-pro`),
Copyright (c) 2026 Glincker, MIT License. The full license text is in
`LICENSE-glincker-ableton-skills.txt` in this folder.
