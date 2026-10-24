---
name: chatmu-studio-melody-hooks
description: >
  Use in Co-Producer whenever you write a MELODY, lead, topline idea, riff or
  hook in Ableton (MIDI), or the user says the melody is boring / not catchy.
  A method to write hooks that stick: rhythm cell first, 3-5 pitches, one
  signature leap, A A A' B phrasing, several candidates scored with a
  checklist, two of them played for the user to choose. Genre rhythm banks for
  trap, reggaetón, lo-fi, pop, R&B, house, corridos. Trigger phrases: "hazme
  una melodía", "un hook", "un gancho", "melodía pegajosa", "más pegajosa",
  "la melodía no engancha", "riff", "topline", "lead", "make a catchy melody",
  "hook", "earworm".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Write catchy hook melodies: rhythm cell first, few pitches, A A A' B, scored candidates"
version: "1.0"
tags: [studio, ableton, melody, melodía, hook, gancho, topline, riff, compose, co-producer]
requiresTools: ["local_ableton_snapshot", "local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_get_notes", "local_ableton_fire"]
---

# Chatmu Studio — Melody hooks
**Version:** 1.0
**Requires:** Chatmu Desktop bridge + Ableton Live.
**Related:** chatmu-studio-compose-core (clip flow, pitch map, scales: read it first), chatmu-studio-genre-templates (tempo, key, chords), chatmu-studio-humanize, chatmu-studio-sound-design (the sound for the lead).

## Why this skill exists

"Correct" melodies (chord tones on strong beats, stepwise motion, one peak) don't sound
wrong, but they don't stick. Hooks stick because of **rhythm, repetition and a signature
move**. This skill replaces "write a nice melody" with a procedure you can check. Follow it
every time; don't write the first melody that comes to mind.

## The method (do it in order)

### 1. Rhythm first
Pick ONE rhythm cell (1 bar, 4/4) from the genre bank below. Positions are in **beats**
from the bar start (0.25 = a 16th), as `start+duration`. The cell is the hook's identity:
it repeats almost unchanged for the whole phrase.

### 2. Few pitches
Build a **pool of 3-5 notes**: the root, 3rd and 5th of the first chord in the lead
register (MIDI 72-88 for leads, see the pitch map), the root an octave up, plus **one
color tone** from the scale (2nd, 4th, 6th or 7th). The hook only uses this pool (bar 3 and
4 may borrow the tones of their chords).

### 3. Motif = cell + pool, with ONE signature leap
- Assign a pool note to each onset of the cell.
- Include exactly **one leap of a 4th to a 6th** (5-9 semitones). This is the "move" people remember. Mostly steps (0-4 semitones) elsewhere.
- **At most 2 equal notes in a row.** The line must change direction at least once in the bar.
- Strong onsets (beat 1, 2, 3, 4 on the grid) use chord tones; off-beats can use the color tone.

### 4. Phrase = A A A' B (4 bars; repeat for 8)
- **A**: the motif over chord 1.
- **A**: the SAME motif again, identical. Repetition is the point; don't "improve" it.
- **A'**: same rhythm, same contour; move only the strong-onset notes to the nearest tone of the chord under bar 3.
- **B (answer)**: the first half of the cell, then ONE long note (≥ 2 beats) on the root or 3rd of the last chord. Fewer notes = it sounds like an ending.
- 8 bars: A A A' B + A A A' B'. B' ends on the key's root.

### 5. Candidates and score
Write **3 candidates** (different cells or different leaps). Score each with this checklist
(1 point each, keep the best two):

| # | Check | Pass |
|---|---|---|
| 1 | Bars 1 and 2 identical | yes |
| 2 | Distinct pitches in the 4 bars | 3–6 |
| 3 | Range (highest − lowest) | ≤ 10 semitones |
| 4 | Signature leaps (≥ 5 semitones) | 2–6 in 4 bars |
| 5 | Chord tones on strong onsets | ≥ 75 % |
| 6 | Off-beat onsets (syncopation) | in the genre band (table below) |
| 7 | Last note | root or 3rd of the last chord |
| 8 | No 3 equal notes in a row; direction changes every bar | yes |
| 9 | At least one rest (≥ an 8th) per bar | yes |

### 6. Let the user choose
Write the best two in **separate clips** on the lead track ("Hook A", "Hook B"), same scene
rows as the chords/drums, fire them one after the other and ask: "¿A o B?". Then iterate
with these levers instead of rewriting from scratch:

| The user says | Change |
|---|---|
| "más pegajosa" | fewer pitches (3-4), repeat the cell exactly, longer last note |
| "más energía" | bar 3 an octave up, or denser cell (add 16ths); keep the leap |
| "más triste / oscura" | harmonic minor (raised 7th on the V chord), descending contour in B |
| "más alegre" | major pentatonic pool, ascending leap at the start |
| "muy repetitiva" | change only bar 4 (B) and bar 8 (B'), never A |
| "muy aguda / muy grave" | move the whole pool ± an octave (keep it above the chords' top voice) |

## Rhythm banks (beats: start+duration; one bar)

| Genre (BPM) | Cells | Off-beat band |
|---|---|---|
| Trap (130-150, half-time feel) | `0+0.5, 0.75+0.25, 1.5+0.5, 2+0.25, 2.5+0.5, 3+0.75` · `0+0.25, 0.5+0.25, 0.75+0.5, 1.5+0.25, 2+0.75, 3+0.5, 3.5+0.25` · `0+0.75, 1+0.25, 1.5+0.25, 1.75+0.5, 2.5+1` | 35–70 % |
| Reggaetón (88-98) | `0+0.5, 0.75+0.5, 1.5+0.5, 2+0.25, 2.75+0.5, 3.5+0.5` · `0+0.25, 0.75+0.25, 1.5+0.5, 2.5+0.25, 2.75+0.5, 3.5+0.25` · `0.25+0.25, 0.75+0.5, 1.5+0.25, 2+0.5, 2.75+0.25, 3.25+0.5` | 45–85 % (3-3-2 feel) |
| Lo-fi (70-90) | `0+0.75, 1+0.25, 1.5+1, 3+0.5` · `0.5+0.5, 1+0.5, 1.75+1.25, 3.5+0.5` · `0+0.5, 0.75+0.25, 1+1, 2.5+0.25, 2.75+0.75` | 25–60 % (lay it 10-20 ms late, see humanize) |
| Pop (100-125) | `0+0.25, 0.5+0.25, 1+0.5, 1.75+0.25, 2+0.75, 3+0.5` · `0+0.5, 0.5+0.5, 1+0.25, 1.5+0.5, 2.5+0.25, 3+0.75` · `0.25+0.25, 0.5+0.25, 1+0.5, 2+0.25, 2.5+0.25, 2.75+0.75` | 25–60 % |
| R&B (65-95) | lo-fi cells + 16th pickups into beat 1 (`3.75+0.25`) | 35–70 % |
| House (120-128) | `0.5+0.25, 1.5+0.25, 2.5+0.25, 3.5+0.25` (off-beat stabs) · `0+0.25, 0.75+0.25, 1.5+0.25, 2.25+0.25, 3+0.5` | 50–90 % |
| Corridos / regional (requinto lines) | triplet runs `0, 0.333, 0.667` into a long note; `0+0.5, 0.5+0.25, 0.75+0.25, 1+1` | 20–50 % |

## Worked examples (scored 96-100; MIDI note numbers; start+duration in beats)

**Trap — 140 BPM, A minor (harmonic), Am F Dm E**
- Bar 1-2 (A, A): `84 0+0.5, 81 0.75+0.25, 88 1.5+0.5, 84 2+0.25, 88 2.5+0.5, 84 3+0.75`
- Bar 3 (A'): `86 0+0.5, 81 0.75+0.25, 88 1.5+0.5, 86 2+0.25, 88 2.5+0.5, 86 3+0.75`
- Bar 4 (B): `83 0+0.5, 81 0.75+0.25, 88 1.5+2.25`
- Signature: the jump A→E (81→88); the B (83) over E is the harmonic-minor "dark" note.

**Reggaetón — 92 BPM, A minor, Am G F G**
- Bars 1-3: `84 0+0.25, 88 0.75+0.25, 88 1.5+0.5, 89 2.5+0.25, 84 2.75+0.5, 81 3.5+0.25`
- Bar 4: `83 0+0.25, 88 0.75+0.25, 91 1.5+2.25`

**Lo-fi — 82 BPM, D dorian, Dm7 G7 Cmaj7 Am7**
- Bars 1-2: `77 0+0.5, 81 0.75+0.25, 74 1+1, 74 2.5+0.25, 77 2.75+0.75`
- Bar 3: `76 0+0.5, 81 0.75+0.25, 72 1+1, 74 2.5+0.25, 77 2.75+0.75`
- Bar 4: `76 0+0.5, 81 0.75+0.25, 81 1+2.75`

**Pop — 112 BPM, C major, C G Am F**
- Bars 1-2: `76 0+0.5, 79 0.5+0.5, 79 1+0.25, 72 1.5+0.5, 76 2.5+0.25, 79 3+0.75`
- Bar 3: `76 0+0.5, 79 0.5+0.5, 81 1+0.25, 72 1.5+0.5, 76 2.5+0.25, 81 3+0.75`
- Bar 4: `77 0+0.5, 79 0.5+0.5, 77 1+0.25, 77 1.5+2.25`

Use them as models, not as the answer. Transpose to the song's key and write new ones
with the same method.

## Writing it in Live

`local_ableton_write_notes { trackIndex, clipIndex, notes: [{ pitch, start, duration, velocity }] }`,
`start` = (bar − 1) × 4 + the cell position. Velocity: strong onsets 100-110, off-beats 85-95,
the long ending note 95. Then `chatmu-studio-humanize` (small timing/velocity spread; lo-fi a bit late).

The sound matters as much as the notes: put the hook on a clear lead (chatmu-studio-sound-design:
pluck for trap/reggaetón/lo-fi, supersaw or bright pluck for pop/EDM), an octave above the
chords' top voice, and leave space if there will be a vocal (or put the hook between vocal phrases).

## Don'ts

- Don't write melodies that use the whole scale; 3-5 pitches.
- Don't vary bar 2; repetition is what makes it a hook.
- Don't fill every 16th; at least one rest per bar.
- Don't deliver a single option: two candidates, user picks.
- Don't describe the hook as catchy without having played it (`local_ableton_fire`) and listened.
