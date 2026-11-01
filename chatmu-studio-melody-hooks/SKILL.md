---
name: chatmu-studio-melody-hooks
description: >
  Writes memorable melodies, hooks, top-lines, riffs, arpeggios and
  counter-melodies in Ableton Live. Builds a structural outline, applies tone
  tendencies, contour, repetition-with-variation and lyric prosody. Trigger
  phrases: "melody", "hook", "top line", "riff", "arpeggio", "counter-melody",
  "chorus melody", "catchy", "memorable", "melody ideas".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Memorable melodies: outline, tension, contour, repetition, prosody"
version: "1.0"
tags: [studio, ableton, melody, hook, top-line, riff]
requiresTools:
  - local_music_theory
  - local_ableton_snapshot
  - local_ableton_get_notes
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_fire
---

# Chatmu Studio — Melody & hooks

**Card:** `music-kb/40_melody/hooks.md` (principles, types, decision tree, errors).
**Read first:** `chatmu-studio-compose-core` (clip flow, MIDI 60 = C3).
**Over existing chords:** `chatmu-studio-melody-over-chords` (build the harmonic map first).

## When to use
When the user wants a melody, hook, top-line, riff or arpeggio, or says the melody
"goes nowhere" (Spanish users may say "no dice nada"). If there are chords already, get the map first; never write blind.

## Workflow

1. **Context:** key, mode, tempo, genre, section, 2/4/8 bars. If chords exist, read them.
2. **Pick the type** from the card: coral, lead/top-line, hook instrumental, arpeggio,
   riff, counter-melody, melisma.
3. **Write the outline:** 4–6 structural tones on strong beats, long notes, accents,
   phrase start/end, highest/lowest note. The outline must go somewhere (up, down, arch).
4. **Choose the tension plan:** last note of each phrase stable (1/3/5) or unstable (2/7).
   Penultimate phrase leaves tension; final phrase resolves.
5. **Set the rhythm** from the genre. Keep the motif 1–2 bars.
6. **Repeat and vary:** A A' or A B. Change the ending, not the beginning.
7. **Embellish** between structural tones: neighbor, passing, changing tone, anticipation,
   leap. Keep steps as the default.
8. **Check prosody** if there is a lyric: stressed syllable on a strong beat, important
   words in opening/closing lines.
9. **Write** with `local_ableton_write_notes` (melody range MIDI 60–84), then
   `local_ableton_fire`.
10. **Hum test:** ask the user to sing it back after one listen. If they can't, rewrite
    the outline, not the ornaments.

## Hard rules
- No melody without an outline; if you cannot name the 4–6 structural tones, it is not done.
- One peak per section.
- Do not end every phrase on the tonic.
- Do not repeat the same contour in every phrase.
- No leap larger than a 6th without stepwise preparation or resolution.
- Strong-beat notes must belong to the chord of that bar (see melody-over-chords).
- Never hold an avoid note; use it as a passing tone.

## Output
Show the outline, the phrase plan (A A' / A B), and where it resolves. Then the MIDI.
Offer one variation: same rhythm/new pitches, or same pitches/new rhythm.
