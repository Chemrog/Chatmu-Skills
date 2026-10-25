---
name: chatmu-studio-melody-over-chords
description: >
  Use in Co-Producer BEFORE writing a melody, lead, counter-melody, bassline,
  arpeggio or harmony part over music that already exists in Ableton Live
  (chords, a loop, a sample converted to MIDI). Builds a harmonic map — which
  chord sounds in each bar, with which exact notes (voicing, inversion), its
  Roman numeral and the local key, including key changes — and then writes
  the part bar by bar against that map. Trigger phrases: "hazme una melodía",
  "melodía para estos acordes", "melodía de los primeros 4 compases", "otra
  variación", "contramelodía", "armonía", "segunda voz", "qué acordes son",
  "en qué tono está", "qué tonalidad", "analiza los acordes", "cambia de
  tono", "modulación", "bajo que siga los acordes", "melody over chords",
  "what chords", "what key", "chord progression", "acordes".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Map the chord of every bar (notes, inversion, local key) and write melodies against it"
version: "1.0"
tags: [studio, ableton, melody, melodía, harmony, armonía, acordes, chords, key, tonalidad, co-producer]
requiresTools: ["local_ableton_snapshot", "local_ableton_get_notes", "local_music_theory", "local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_fire"]
---

# Chatmu Studio — Melody over chords
**Version:** 1.0
**Requires:** Chatmu Desktop (Co-Producer) bridge + Ableton Live.
**Read first:** `chatmu-studio-compose-core` (clip flow, pitch map: MIDI 60 = C3 in Live, ranges).
**Related:** `chatmu-studio-harmony-voicing` (chord vocabulary), `chatmu-studio-bass-lines`,
`chatmu-studio-song-structure` (which section you are writing for), `chatmu-studio-humanize`.

## Why this skill exists

"The song is in B minor" is not enough to write a melody. A B-minor loop may be
Bm – G – D – A, and a note that is perfect over Bm (D) clashes when held over A. Songs
also change key (C → F# → C minor). Weak melodies come from writing against **one key for
the whole song**. Good ones come from knowing **which chord sounds in each bar and which
notes are already being played**, and landing on those on purpose.

So: **map first, then write.** Never write a melody over existing music without the map.

## 1. Build the harmonic map

### 1a. Gather the notes
1. `local_ableton_snapshot` → tempo, time signature (`song.sig`), tracks, clips and scenes.
   Beats per bar = `numerator × 4 / denominator`.
2. Pick the **harmonic tracks** of the section you will write for: chords, keys, pads, bass,
   arps, guitars. Leave drums out. Treat an existing melody separately (step 1e).
3. Read each one: `local_ableton_get_notes` `{ trackIndex, clipIndex }` (Session clips).
   Several clips at once: `local_ableton_snapshot` with `includeNotes: true` (can be large).
4. The music is **audio only** (a Splice loop, a sample, a bounce)? There is no tool for this
   yet. Ask the user to right-click the audio clip in Live → **Convert Harmony to New MIDI
   Track** (and **Convert Bass to New MIDI Track** for the bass), then read that MIDI. Tell
   them it is an approximation and confirm the result by ear.

### 1b. Slice into bars
For bar N (starting at 1), keep the notes that **sound** during
`[(N − 1) × beatsPerBar, N × beatsPerBar)` — including notes that started earlier and are
still held. Weight each pitch by how long it sounds inside the bar. If the pitch set
clearly changes mid-bar (typically on beat 3), split the bar into two halves.

### 1c. Name the chord of each slice
1. **Bass note** = the lowest pitch sounding (from the bass track if there is one).
2. Take the **pitch classes** (pitch mod 12), ignoring very short notes (< ¼ beat) on weak
   positions: they are passing tones, not harmony.
3. Try each pitch class as the root and compute the intervals of the others above it. Pick
   the chord type below that **covers the most sounding weight with the fewest missing
   tones**. On a tie, prefer the bass note as the root, then the simpler chord.

| Type | Intervals | Symbol |
|---|---|---|
| Major | 0 4 7 | C |
| Minor | 0 3 7 | Cm |
| Diminished | 0 3 6 | C° |
| Augmented | 0 4 8 | C+ |
| Sus2 / Sus4 | 0 2 7 / 0 5 7 | Csus2 / Csus4 |
| Power (no 3rd) | 0 7 | C5 |
| Dominant 7 | 0 4 7 10 | C7 |
| Major 7 | 0 4 7 11 | Cmaj7 |
| Minor 7 | 0 3 7 10 | Cm7 |
| Half-diminished | 0 3 6 10 | Cm7♭5 |
| Diminished 7 | 0 3 6 9 | C°7 |
| 6 / minor 6 | 0 4 7 9 / 0 3 7 9 | C6 / Cm6 |
| add9 / minor 9 / major 9 | 0 4 7 2 / 0 3 7 10 2 / 0 4 7 11 2 | Cadd9 / Cm9 / Cmaj9 |

   A missing 5th is normal (still the same chord). Missing 3rd → sus or power chord.
4. **Inversion** from the bass: bass = root → root position; bass = 3rd → 1st inversion
   (`G/B`); bass = 5th → 2nd inversion (`G/D`); bass = 7th → 3rd inversion; bass outside the
   chord → slash chord (`C/D`) or pedal.
5. **Voicing** = the actual notes, low to high, with their Live names (`B1 · F#2 B2 D3`).
   This is what decides whether a melody note clashes with the top voice.

### 1d. Keys and key changes
1. Global key: `local_music_theory` `{ action: "detect_key", notes }` with all harmonic notes.
2. **Local key**: run `detect_key` again on windows of 4–8 bars (one per section). If a window
   gives a different key with clear confidence, that is a **modulation**; mark where it starts.
   A single borrowed chord (♭VI or iv in a major key, V in natural minor) is NOT a key
   change: keep the key and mark the chord as borrowed.
3. Write each chord's **Roman numeral relative to its local key** (i, ♭VI, V/V…).

### 1e. What is already being sung or played on top
If there is a melody, vocal-like line or top-line synth, read it too and note per bar its
range and its notes on the strong beats. Your new part must avoid them (or answer them).

### 1f. Write the map down and show it
One line per bar (or half bar), compact:

```
Si menor · 88 BPM · 4/4
c.1  Bm     i    raíz    B1 · F#2 B2 D3      (melodía actual: —)
c.2  G/B    ♭VI  1ª inv  B1 · G2 B2 D3
c.3  D      ♭III raíz    D2 · D3 F#3 A3
c.4  A      ♭VII raíz    A1 · E3 A3 C#4
c.9  → modula a Mi menor (pivote: G = ♭VI en Si menor = ♭III en Mi menor)
```

Show the user the short version ("Son 4 compases: Bm – G/B – D – A, en Si menor") and keep
the full map in your context for writing. If the user corrects a chord, they are right:
update the map.

## 2. Write against the map

Work on the bars the user asked for ("los primeros 4 compases" = bars 1–4; "el coro" =
the section's bars from `chatmu-studio-song-structure`). For each bar, from its map line:

1. **Chord tones** = the chord's notes in the melody range (MIDI 60–84 for leads). **Guide
   tones** = the 3rd and the 7th: they say the most about the chord.
2. **Strong beats (1 and 3, and any note ≥ 1 beat long) land on chord tones** of THAT bar's
   chord. Prefer the 3rd or 5th over the root for colour; the root for endings.
3. **Weak positions** may use other notes of the local key (passing and neighbour tones),
   resolving by step to a chord tone.
4. **Avoid notes** — never on a strong beat or held:
   - a semitone above a chord tone that is sounding (♭9 over the root, the 4th over a major
     3rd: F over C major);
   - the major 7th over a dominant-7 chord, the minor 3rd over a major chord;
   - the note the top voice of the chords is holding, in the same octave (double it an octave
     above or below, or pick another tone).
5. **Connect the bars.** At each chord change, the first note of the new bar goes to the
   nearest chord tone of the new chord: a **common tone** (same note, held across the bar
   line) or a **step** (1–2 semitones). Approach it from a step above or below on the last
   offbeat of the previous bar. That movement is what makes a melody "follow the chords".
6. **Key changes:** from the modulation bar on, use the new local key's scale. In the bar
   before, aim the melody at a note common to both keys (the pivot).
7. **Shape** (from `chatmu-studio-compose-core`): a 1–2 bar motif, repeated and varied
   (A A' or A B), one peak per phrase, rests, end the phrase on the root or 3rd of the last
   chord. When the motif repeats over a different chord, keep its rhythm and contour and
   move only the strong-beat notes to the new chord's tones.
8. **Rhythm** follows the genre (`chatmu-studio-genre-templates`); the harmony only decides
   the pitches.

### Bass lines
Same map, other rules: the bass plays the **bass note of the map** (the inversion matters:
G/B means B in the bass, not G) on beat 1 of each chord; move between chords by step or
with the 5th/octave; approach the next root from a semitone or a step on the last offbeat.
Details per genre in `chatmu-studio-bass-lines`.

### Second voice / harmony
A 3rd or a 6th above or below the melody, adjusted note by note so that it **stays in the
chord of each bar** (the interval changes size between major and minor 3rds; that is
correct).

## 3. Check before you write, and after

Before `local_ableton_write_notes`, go through your notes bar by bar and confirm: every
strong-beat note is a chord tone of that bar, no avoid note is held, and the range does not
sit on top of the chords' top voice. Fix, then write (`chatmu-studio-compose-core` for the
clip flow).

After writing: `local_ableton_get_notes` to confirm, `local_ableton_fire` to play it with the
chords, and let the user listen. Offer **one** variation at a time:
- **Same rhythm, new pitches** (another contour over the same chord tones), or
- **Same pitches, new rhythm** (the genre's other rhythm cell), or
- **Answer phrase**: keep bars 1–2, rewrite 3–4 to end on the tonic.

## Don'ts

- Don't write over existing music without building the map first.
- Don't treat a song as one key if the map shows a modulation; don't call one borrowed chord a key change.
- Don't put a passing tone on beat 1 or hold it.
- Don't ignore the inversion: the bass note changes what sounds good on top.
- Don't present the map as certain when it came from audio converted to MIDI; say it is an estimate.
