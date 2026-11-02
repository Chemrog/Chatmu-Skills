---
name: chatmu-studio-hook-melody
description: >
  Writes melodies that people remember — hooks, chorus top-lines, synth leads,
  riffs and instrumental motifs — in the user's Ableton Live set, for any genre.
  Builds a short motif with a signature rhythm, repeats and varies it, plans one
  peak, leaves questions and answers, fits it to the chords, and self-checks
  against the habits that make AI melodies forgettable before writing a note.
  Trigger phrases: "melody", "hook", "catchy", "top line", "chorus melody",
  "lead", "riff", "motif", "make it stick", "melodía", "gancho", "pegajosa",
  "que se quede", "coro", "melodía del coro", "lead", "riff", "no engancha",
  "la melodía no dice nada", "suena a IA".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Hooks that stick: motif + signature rhythm, one peak, question/answer, anti-AI self-check"
version: "1.0"
tags: [studio, ableton, melody, hook, top-line, riff, songwriting]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_tracks
  - local_harmony_map
  - local_music_theory
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_get_notes
  - local_ableton_fire
  - local_sing
---

# Chatmu Studio — Hook melody

A hook is not "a nice sequence of notes". It is **one short idea, said three times, with
one surprise**. Listeners remember a rhythm and a shape long before they remember pitches.
This skill writes the idea first and the notes last.

Basics (clip flow, MIDI 60 = C3 in Live): `chatmu-studio-compose-core`.
Chords already exist and you only need a line over them: this skill still applies; it reads
the harmony itself in step 2.

## Why AI melodies don't stick (and what this skill does instead)

| Habit of a model writing note by note | Result | What you do |
|---|---|---|
| Picks the most probable next note every time (steps, chord tone on every beat) | Correct and forgettable: nothing to predict, nothing to be surprised by | Plan **one** deliberate surprise per phrase (a leap, a held tension, a rhythmic displacement) |
| Writes 8 bars of new material | No idea to hold on to | A **1–2 bar motif**, repeated and varied; ≥ 50% of the hook is repetition |
| Even 8ths, same length, velocity 100 | Sounds typed, not sung | A **signature rhythm**: syncopation, pickup, a rest, ≥ 2 note lengths, accents |
| Peak lands anywhere, or in every phrase | No arrival | **One** highest note per section, placed late, held, approached on purpose |
| Every phrase ends on the tonic | Nothing pulls forward | Phrase 1 ends **open** (2, 5 or 7), the last one closes |
| Always MIDI 60–72 | Wrong register for the voice/instrument | Register chosen from the role (table below) |
| Same melody shape in every genre | Generic | Genre cell from the table below |

## When to use
The user asks for a melody, hook, chorus line, lead, riff or motif; or says the melody is
boring, "doesn't say anything", "sounds like AI", "isn't catchy". Also as the melody step of
a full song.

## Ask only what is missing
Key and tempo (read them from the set first), genre/mood, which section (verse, pre, chorus,
drop), instrument or voice, and whether there are lyrics. Never ask more than two things at
once; propose defaults ("I'll write it for the chorus, on a pluck, 4 bars").

## Workflow

### 1. Read the set
`local_ableton_snapshot` → tempo, tracks, scenes. If chords or bass exist, run
`local_harmony_map` (source `daw`, `detail: compact`, the scene or locator of the section).
Keep the chord of every bar; strong-beat notes will be checked against it. If there are no
chords, the melody will imply them: decide the progression in your head first (numerals) and
say it.

Get the scale pitches in the register you need with `local_music_theory` `action: scale`
(never compute MIDI numbers by hand).

### 2. Pick the role and register
| Role | MIDI range (60 = C3 in Live) | Notes |
|---|---|---|
| Female / high vocal top-line | 55–79 | chorus sits in the top half |
| Male vocal top-line | 48–72 | chorus a 3rd–5th above the verse |
| Synth lead / pluck / bell hook | 67–91 | trap bells and plucks live high |
| Flute / ney / whistle | 72–96 | |
| Guitar / bass riff | 40–64 | rhythm first, few pitches |
| Pad melody / ambient | 60–84 | long notes, wide intervals |

Range of the whole hook: ≤ 12 semitones for an instrumental hook, ≤ 14 for a vocal chorus.

### 3. Write the rhythm cell first (1 bar, sometimes 2)
Clap it before giving it pitches. Requirements:
- At least **one syncopation** (a note starting off the beat and held across it) or an
  **anticipation** (the phrase starts on the "and" of 4 of the previous bar).
- At least **one rest** of an 8th or longer inside the cell (vocals need breath; hooks need
  air).
- At least **two different note lengths**; one longer note that will carry the strongest
  pitch.
- Starts on beat 1 at most half the time — pickups and "and"-starts are more memorable.

Genre cells (beats from the bar start, 1 beat = quarter note):
| Genre | Typical cell | Feel |
|---|---|---|
| Pop chorus | 0.5, 1, 1.5, 2.5(long) · rest · 3.75 pickup | syllabic, title on the long note |
| Dark trap hook | 0, 0.75, 1.5 · rest · 2.5, 2.83, 3.17 (8th-note triplet) | sparse, 2-bar loop |
| Reggaetón | 0.5, 1.25, 2, 2.75, 3.5 (against the 3-3-2) | ends anticipating beat 1 |
| Rock riff | 0, 0.5, 0.75, 1.5, 2(long), 3.5 | rhythmic, repeated exactly |
| House riff | 0.5, 1.5, 2.5, 3.5 (offbeats) + one 16th push | 1 bar, hypnotic |
| R&B | pickup 16ths into a long note, melismatic fills | behind the beat |
| Ambient | 0 (2–4 beats long), next note 2–4 beats later | no cell; the interval is the hook |
| Regional mexicano | 8th pickups, long notes on 1 and 3 | doubled a 3rd below (segunda voz) |

### 4. Give the cell pitches → the motif
- 3–5 distinct pitches. The motif's identity = **rhythm + contour**, so a later variation can
  change pitches and still be recognised.
- Include **one characteristic interval**: a leap of a 4th–6th, a repeated note followed by a
  step, or a scale colour the genre owns (♭2 in phrygian, ♭6 in minor, #4 in lydian, the
  augmented 2nd in harmonic minor).
- Long notes and strong beats take chord tones (1, 3, 5) or a deliberate colour (9, or 11 in
  minor) held on purpose. A non-chord note on a strong beat is allowed only as an
  appoggiatura that resolves **by step within one beat**.

### 5. Build the phrase (usually 4 bars) with a plan
Choose one form and say it:
- **A A A' B** — statement three times, the third slightly changed, then an answer. The most
  reliable hook form.
- **A B A B'** — call and answer; B' closes.
- **A A' (2 bars each)** — same rhythm, A' moves to the new chord and changes the ending.

Endings: first pass of the phrase ends **open** (on scale degree 2, 5 or 7, or on a chord tone
that is not the root), the repeat ends **closed** (1, or 3). Change the **ending** of a motif,
not its beginning — the beginning is what people recognise.

### 6. Place the peak
One highest note per section, in the second half (bar 3 of 4, or bar 6–7 of 8), longer than
the notes around it, on a strong syllable/beat. Approach it either by a leap up after lower
repeated notes, or by a step after a climb. Never repeat the peak note elsewhere in the
section.

### 7. Section contrast (when writing more than one section)
Verse: lower, narrower range, more notes, more speech rhythm. Pre-chorus: rising outline,
shorter phrases. Chorus: a 3rd–5th higher than the verse, longer notes, more repetition, the
title on the peak or on the long note. Drop/post-chorus hook: instrumental version of the
motif, even more repetitive.

### 8. Self-check before writing (all must pass; fix and re-check)
Count on your own note list:
1. Motif length 1–2 bars, and it appears ≥ 2 times in 4 bars (exact or varied).
2. ≥ 1 syncopation or anticipation every 2 bars.
3. ≥ 2 distinct durations; ≥ 1 rest of an 8th or longer per bar in vocal lines.
4. Steps 55–80% of intervals; at least one leap ≥ a 4th; no leap > a 6th unless it resolves
   by step in the opposite direction.
5. Exactly one peak per section.
6. Not every phrase ends on the tonic.
7. Strong-beat notes are chord tones, planned colours, or step-resolving appoggiaturas.
8. Range fits the role table.
9. Velocity has shape: strong/long notes 95–112, passing notes 70–88, ghosted pickups 55–70.
10. Could you describe the hook in one sentence ("a triplet stab that falls a 5th and answers
    itself")? If not, it has no identity: go back to step 3.

### 9. Write and play
1. Find or create a MIDI track with the right sound (`chatmu-studio-sound-design` for the
   sound). Use `local_ableton_tracks` for indexes.
2. `local_ableton_create_clip` (length = phrase length in beats, name e.g. `Hook A`).
3. `local_ableton_write_notes` with the notes; check with `local_ableton_get_notes` if a write
   timed out.
4. `local_ableton_fire` (action `clip`) — with the chords and drums playing if they exist.
5. Vocal line and the user wants to hear it sung: `local_sing` with the lyrics (or neutral
   syllables like "na-na") on that clip. Say it is a rough guide, not a final vocal.

### 10. Offer one alternative, on one axis
Write **one** alternative in the next empty slot of the same track, named `Hook B`, that
changes only one axis: same rhythm with a new contour, or same pitches with a new rhythm.
Let the user compare by firing each. Never dump five options.

## Feedback → what to change
| The user says | Change |
|---|---|
| "Not catchy" / "no engancha" | Shorter motif, more exact repetition, stronger rhythm cell |
| "Boring" / "plana" | Add the surprise: a leap to the peak, a held 9th, a displaced repeat |
| "Too weird" | More chord tones on strong beats, more steps, resolve tensions sooner |
| "Sounds like AI" | Run the self-check again; usually even rhythm and no motif |
| "Too busy" | Remove notes, keep the rhythm cell's skeleton; add rests |
| "Higher / more emotion" | Move the chorus up a 3rd, peak later and longer |

If the user hums or plays an idea: record it (`chatmu-studio-record`) or convert audio with
`chatmu-studio-harmonize-melody`'s intake step, and develop **their** motif with steps 5–8
instead of replacing it.

## Hard rules
- Never write a hook without being able to name its motif, its form (AAA'B…) and its peak.
- Never present more than two versions at once.
- Never change the user's melody silently; say what you changed and why.
- Do not quantize-and-flatten a melody the user played; keep their timing unless asked.
- Do not end every phrase on the tonic; do not put the peak in every phrase.
- `local_sing` is for guides only; never use it to talk to the user.

## Tell the user (short)
`Hook (chorus, 4 bars, A A A' B): a syncopated 3-note cell that climbs to the 5th; peak on bar 3
(the long G), first ending open on the 2nd, the repeat closes on the root. Written to "Lead",
clip "Hook A". Alternative "Hook B": same rhythm, falling contour.`
