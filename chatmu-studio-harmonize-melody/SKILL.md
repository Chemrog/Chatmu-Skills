---
name: chatmu-studio-harmonize-melody
description: >
  Puts chords under a melody that already exists — a MIDI clip, a recorded or
  hummed vocal, a .mid file — in the user's Ableton Live set. Finds the key,
  picks the harmonic rhythm, chooses chords from the melody's structural notes
  with real function and cadences, offers a simple and a colourful version,
  voices them under the melody without clashes, writes them and verifies with
  the harmony map. Trigger phrases: "harmonize", "chords for this melody",
  "what chords go under", "reharmonize", "I hummed a melody", "armonizar",
  "acordes para esta melodía", "ponle acordes", "qué acordes van", "tarareé",
  "rearmonizar", "armonía para la voz".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Chords under an existing melody: key, harmonic rhythm, function, cadences, clash-free voicing"
version: "1.0"
tags: [studio, ableton, harmony, chords, harmonization, reharmonization, melody]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_tracks
  - local_ableton_get_notes
  - local_audio_to_midi
  - local_harmony_map
  - local_music_theory
  - local_ableton_edit_track
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_fire
---

# Chatmu Studio — Harmonize a melody

The melody is the user's. The chords must make **it** sound better, not compete with it.
A good harmonization does three things: it agrees with the melody's important notes, it moves
with a direction (tension → release), and it lands its cadences where the melody breathes.

Opposite task (melody over existing chords): `chatmu-studio-hook-melody` or
`chatmu-studio-melody-over-chords`. Clip basics: `chatmu-studio-compose-core`.

## When to use
The user has a melody (played, recorded, hummed, imported) and wants chords, or wants the
current chords replaced by better/richer ones.

## Workflow

### 1. Get the melody as notes
| Source | How |
|---|---|
| MIDI clip in Live | `local_ableton_tracks` → `local_ableton_get_notes` |
| Audio clip in Live (vocal, hum, instrument) | `local_audio_to_midi` with `track` + `clip` (or `arrangement_clip`); it is monophonic — perfect for a melody |
| Audio file on disk | `local_audio_to_midi` with `path` |
| The user wants to hum it now | record it first (`chatmu-studio-record`), then `local_audio_to_midi` |
| A .mid | read it with `local_harmony_map` `source: midi_file` (melody shows in `full`) |

After audio → MIDI: merge notes shorter than a 32nd into neighbours, fix obvious octave jumps
(one note an octave away from its neighbours), and **keep the user's timing**. Tell the user
what you cleaned. Ask them to confirm by firing the MIDI clip if the conversion looked rough.

### 2. Find the key and the phrases
- `local_music_theory` `action: detect_key` with the pitches (repeat long notes so duration
  weighs in). Check the answer against the melody: the last note and the longest notes are
  usually 1, 3 or 5. If the top two candidates are close (relative major/minor), choose by the
  final note and say it.
- Mark the phrases: where the melody rests (long note or silence ≥ 1 beat). Every phrase end is
  a cadence point.

### 3. Choose the harmonic rhythm
| Situation | Chords per bar |
|---|---|
| Default pop/rock/reggaetón/trap at normal tempo | 1 |
| Ballad, R&B, gospel, jazz, slow 6/8 | 2 (or one per beat at cadences) |
| Fast tempo (> 140 BPM) or club/ambient/trap loop | 1 every 2 bars, or a pedal |
| Approaching a cadence | speed up (2 per bar in the last bar) |

Change chords where the melody changes structural note, never in the middle of a held note.

### 4. Pick the chord for each span
For every span, list the **structural notes**: on beats 1 and 3, the longest, the accented,
the first and last of the phrase. Ignore passing and neighbour notes.

Each scale note belongs to three diatonic triads (as root, 3rd or 5th). Choose among those with
these priorities, in order:
1. **Cadences first.** Work backwards from each phrase end:
   - melody ends on 1 → authentic close: V–I (or IV–I for a softer, plagal close; ♭VII–I in
     rock/pop/minor-urban)
   - melody ends on 2, 5 or 7 → half close on V (the question)
   - want a surprise at a phrase end → V–vi (deceptive)
2. **Function flow** inside the phrase: tonic (I, vi, iii) → pre-dominant (IV, ii) → dominant
   (V, vii°) → tonic. Moving backwards (V → IV) is fine in pop/rock, but say it is a choice.
3. **The melody note as 3rd, 5th, 7th or 9th of the chord** sounds richer than as the root.
   Avoid having the melody double the bass at the octave on long notes.
4. **Bass motion**: roots by 4th/5th (strong), by step (smooth), or a stepwise bass line with
   inversions (I – V/7 – vi – IV is the classic descending line). Avoid the same root across a
   barline when the melody's structural note changes.
5. **Variety**: do not use the same chord for more than 2 consecutive spans unless it is a
   deliberate pedal.

In minor keys use V (major, from harmonic minor) for real dominant pull, v or ♭VII for a
modal, softer sound (trap, reggaetón, rock). In both, ♭VI and ♭III are the common colours.

### 5. Make two versions (three only if asked)
- **Version A — Clear**: diatonic triads, cadences as above. It must already sound right.
- **Version B — Colour for the genre** (pick tools that fit, explain each in a line):
  | Genre | Colours |
  |---|---|
  | Pop | sus2/sus4 at phrase starts, IV → iv (borrowed minor iv), ♭VII |
  | R&B / neo-soul | 7ths and 9ths, ii7–V7, IVmaj7 → iii7, chromatic approach chords |
  | Reggaetón / trap / urbano | minor loop i–♭VI–♭III–♭VII, pedal on i, fewer changes |
  | Rock | power chords, ♭VII and ♭VI, IV–I |
  | Jazz | ii–V into each target, tritone substitution, 9/11/13 extensions |
  | Ambient / cinematic | pedal tone, slow chords, add9 and maj7, ♭VI–♭VII–i |
  | Regional mexicano / ranchera | I–IV–V7 with secondary V7/IV and V7/V |
  Secondary dominants (V/x) work when the melody has the raised note (e.g. #4 → V/V) or the
  bar is a passing moment; never put one under a melody note it contradicts.

### 6. Voice the chords under the melody
- Get notes with `local_music_theory` `action: progression` (numerals, the key,
  `beatsPerChord` per span, `voiceLeading: true`, `bass: true` if the user wants a bass line);
  never compute MIDI by hand.
- Keep the chords' top voice **below the melody's lowest note in that span**, ideally a 3rd or
  more below; never cross the melody. Lower the voicing (or use `voicing: spread`) if needed.
- Clash check, every strong-beat melody note against the chord sounding under it:
  - a minor 2nd or ♭9 between the melody and a held chord tone → change the voicing (drop that
    chord tone) or change the chord
  - the melody on the chord's 4th over a major triad on a long note → use sus4 or another chord
  - an avoid note held on a strong beat → only if it resolves by step within the beat
- Chords in MIDI 48–72; below 52 only roots, 5ths and octaves (mud otherwise).

### 7. Write, verify, play
1. Create a MIDI track for the chords (`local_ableton_edit_track` `create_midi`, name it
   `Chords A`) with a neutral keys/pad sound; a separate one for `Chords B`.
2. `local_ableton_create_clip` in the same scene row as the melody, same length; write with
   `local_ableton_write_notes`.
3. Verify: `local_harmony_map` (source `daw`, that scene, `melodyTracks` = the melody track,
   `detail: full`). The chord it reads in each bar must be the one you meant; a mismatch means a
   wrong note — fix it before playing.
4. `local_ableton_fire` the scene/clips so the user hears melody + version A, then version B.

## Hard rules
- The melody wins: never change the user's melody to fit your chords without asking.
- Every chord has a numeral and a reason (function, cadence, colour). If you can't name the
  reason, use the simpler chord.
- Never write chords that cross above the melody.
- Never present more than two versions unless asked.
- If the user says a chord is wrong, they are right for their song: change it and continue.

## Tell the user (short)
A table per version: bar → structural melody notes → chord → function. Then one line:
`Version A (clear): I–vi–IV–V, closes on I in bar 8. Version B (R&B): Imaj9–vi9–IVmaj7–iii7 / ii7–V7sus–I.
On tracks "Chords A" and "Chords B" in scene 1 — fire each with the melody.`
