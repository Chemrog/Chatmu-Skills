---
name: chatmu-studio-counter-melody
description: >
  Writes a second line that supports the lead without fighting it, in the user's
  Ableton Live set: counter-melodies, harmony voices in 3rds and 6ths,
  call-and-response fills, brass and string answers, contrary and oblique motion.
  Stays out of the lead's register and rhythm, fills its gaps, and checks every
  vertical interval against the chords before writing.
  Trigger phrases: "counter melody", "second voice", "harmony line", "answer the
  vocal", "fills", "call and response", "brass answer", "string line",
  "contramelodía", "segunda voz", "armonía en terceras", "que conteste a la voz",
  "relleno", "pregunta y respuesta", "respuesta de metales", "línea de cuerdas".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Second voices, 3rds/6ths harmonies and call-and-response fills that stay out of the lead's way"
version: "1.0"
tags: [studio, ableton, counter-melody, harmony, arrangement, brass, strings]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_tracks
  - local_ableton_get_notes
  - local_harmony_map
  - local_music_theory
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_fire
  - local_sound_find_preset
---

# Chatmu Studio — Counter-melody & second voices

A second line has one job: **make the lead sound better**. It wins by being *different* —
moving when the lead holds, resting when the lead talks, going down when the lead goes
up, living in another register. The AI tell is a second line that is just the lead
transposed, playing the same rhythm, at the same volume: it doubles the clutter instead of
adding depth.

Basics: `chatmu-studio-compose-core` (clip flow, MIDI 60 = C3). The lead itself:
`chatmu-studio-hook-melody`. Chord-tone harmonization of a melody into full chords:
`chatmu-studio-harmonize-melody`. Pan/width of the second line:
`chatmu-studio-spatial-panning`.

## When to use
User asks for a counter-melody, harmony voice, fills between vocal lines, a brass/string
answer, or says the arrangement feels empty between phrases; or the arrangement step of a
song needs a secondary line for the chorus or last chorus.

## Ask only what is missing
Read key, tempo and the lead clip from the set. Ask at most: which type (table below) and
which instrument. Default if unsure: verse = call-and-response fill, chorus = harmony in
3rds/6ths or a sustained counter-line.

## Pick the type
| Type | When | How it relates to the lead |
|---|---|---|
| **Parallel harmony (3rds/6ths)** | Chorus vocals, hook doubles, mariachi violins, norteño 2nds, R&B stacks | Same rhythm, diatonic 3rd above or 6th below |
| **Call-and-response fill** | Verses, gaps between vocal lines, funk/salsa/brass, gospel | Plays only in the lead's rests |
| **Sustained counter-line** | Pads/strings under a busy lead, last chorus lift | Long notes (1–2 bars) moving by step, oblique to the lead |
| **Active counter-melody** | Instrumental sections, cinematic, intros, post-chorus | Independent rhythm and contour, contrary motion |
| **Riff/ostinato** | EDM, reggaeton, rock under a vocal | Repeating 1–2 bar figure in another register |

## Step 1 — Map the lead
`local_ableton_get_notes` on the lead clip. Record:
- **Range** (lowest/highest MIDI note) and the average register.
- **Rests** ≥ 1/4 note: these are the windows for fills (beat positions).
- **Held notes** ≥ 1 beat: windows where the second line can move.
- **Peak** note and its position: the counter-line must not compete there.
`local_harmony_map` → chords per bar (chord tones are your safe landing notes).

## Step 2 — Register: stay out of the way
- Separation ≥ a 3rd at every point; never cross the lead.
- Prefer **below** the lead for support (6ths below, strings an octave lower), **above**
  only for a descant/shimmer in the last chorus (octave-ish above, quieter, thinner sound).
- Typical windows (lead vocal around 55–72):
  - Under-voice / cello or horn line: 48–62.
  - Fills between lines: same range as the lead is fine, because they don't overlap in time.
  - Descant (strings, flute, bell, synth pluck): 72–88, velocity 15–25 lower than the lead.
- Keep clear of the bass (usually below 48) and the kick/snare body; nothing busy below
  about C2 (48) except the bass.

## Step 3 — Motion rules (contrary > oblique > similar > parallel)
- **Contrary**: lead up, counter down. Strongest independence. Use at phrase climaxes.
- **Oblique**: one holds, the other moves. The default for sustained counter-lines.
- **Similar** (same direction, different intervals) is fine; **parallel 5ths and octaves**
  between lead and counter are not — they fuse into one voice (unless you deliberately
  double the lead in octaves for power: rock riffs, EDM leads).
- Parallel 3rds/6ths: correct only for the *harmony voice* type, and always **diatonic**
  (alternate major/minor 3rds by scale degree). Use `local_music_theory` scale to compute
  the 3rd above/6th below each lead note; if the result clashes with the current chord
  (a 2nd/9th against a chord tone on a strong beat), move it to the nearest chord tone.
- On strong beats the vertical interval should be consonant (3, 6, 8, 5 as a passing
  sonority); dissonances (2nds, 4ths, 7ths) only on weak beats or prepared/resolved by step.

## Step 4 — Rhythm: complement, don't copy
- Fill type: start **after** the lead's last note (≥ 1/16 gap), end before its next
  pickup (≥ 1/8 gap). Fill length ½–1½ bars. Not every gap: 2 of every 4 gaps.
- Counter-line: when the lead runs in 16ths, the counter holds half/whole notes; when
  the lead holds, the counter can move in 8ths.
- Harmony voice: identical onsets to the lead (copy start/duration), velocity −10 to −15,
  and enter on the chorus or the title line only — not the whole song.
- Answers in salsa/funk/regional brass: tight, short (1/16–1/8 notes, staccato
  duration 0.15–0.25 beats), syncopated, accented on the "and" of 2 or 4.

## Step 5 — Density across the song
- Verse 1: none or one fill per 4 bars. Verse 2: fills every 2 bars. Chorus: harmony or
  sustained line. Last chorus: add the descant. Bridge: drop it to give contrast.
- Only one secondary line active at a time in front; a second one goes to the back plane
  (quieter, darker, more reverb — see `chatmu-mix-effects`).

## Instruments (query words)
`local_sound_find_preset` with genre + instrument: Strings (Warm) for sustained lines,
Brass (Bright/Short) for answers, Flute or Bell for descants, Guitar (Short) for fills,
Vocal for "oh/ah" pads, Keys for soft countermelodies. If it returns `fallback: true`,
use the Live browser: Strings/Brass ensembles, or a filtered saw for synth genres.
Velocity: harmony voice 70–90, fills 75–100 (accents up), descant 60–80.

## Genre idioms (short)
- **Mariachi / ranchera**: violins in parallel 3rds/6ths, trumpets answer the vocal in
  the gaps; armonía de la segunda voz usually a 3rd below.
- **Norteño / corridos**: accordion fills in every vocal gap (16th runs, ends on a chord
  tone), bajo sexto holds; second voice in 3rds in choruses.
- **Salsa / son**: brass mambo answers, 2–4 bar call-and-response with the coro; locked
  to the clave (see `chatmu-studio-afro-cuban-rhythms`).
- **Pop / R&B**: stacked 3rds on the chorus title, "ooh" pads oblique under verses.
- **EDM / house**: counter-riff an octave below or above the lead, different rhythm cell;
  pluck answers in the breakdown.
- **Cinematic**: strings in contrary motion to the theme, horns on long notes.
- **Gospel / soul**: call-and-response between lead and choir.

## What ruins it
- Counter-line in the same register and rhythm as the lead → mud and fighting.
- Parallel octaves/5ths by accident → sounds like a doubled lead, not a second voice.
- Fills in every single gap → busy, nowhere to breathe.
- Chromatic 3rds (always major) → out of key.
- Second line louder or brighter than the lead.
- Harmony voice for the entire song → no lift left for the chorus.

## Tool workflow
1. `local_ableton_snapshot` → key, tempo; `local_ableton_tracks` → lead track/clip.
2. `local_ableton_get_notes` on the lead → range, rests, holds, peak (step 1).
3. `local_harmony_map` → chord per bar; `local_music_theory` scale → diatonic notes.
4. Plan the line on paper (type, register, motion), tell the user in one sentence.
5. `local_sound_find_preset` → sound; create a track/clip with `local_ableton_create_clip`
   matching the lead's length.
6. `local_ableton_write_notes` (pitch/start/duration in beats/velocity). Loop with
   `local_ableton_fire` together with the lead so the user hears both.
7. Check: no crossings, no parallel 5ths/8ves, consonance on strong beats.

## Hard rules
- Never in the same register AND rhythm as the lead.
- Diatonic 3rds/6ths only; check each against the chord.
- Contrary or oblique motion at the lead's peak.
- Fills only inside the lead's rests, with gaps on both sides.
- Second line 10–15 velocity (or ~3–6 dB) under the lead.
- Write a new clip; never overwrite the lead.

## Tell the user (example)
"Your vocal rests on beats 3–4 of every second bar, so I wrote a trumpet answer just in
those gaps, short and on the off-beats, ending on the chord's 3rd. In the chorus I added
a second voice a diatonic 3rd below your line, only on the title phrase. Want the answer
on strings instead, or more of them?"
