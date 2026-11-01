---
name: chatmu-studio-harmony-functional
description: >
  Writes chord progressions with correct function, numerals, voicings and voice
  leading in Ableton Live. Covers major/minor diatonic harmony, cadences,
  tonic/pre-dominant/dominant flow, inversions and jazz ii-V-I. Trigger phrases:
  "chords", "chord progression", "harmony", "cadence", "reharmonize", "voicing",
  "inversion", "dominant", "subdominant", "tonic", "minor", "major", "jazzy chords".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Functional harmony: pick the progression, then voice-lead it"
version: "2.0"
tags: [studio, ableton, harmony, chords, cadence, voicing]
requiresTools:
  - local_music_theory
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_get_notes
  - local_ableton_fire
---

# Chatmu Studio — Functional harmony

**Card:** `music-kb/10_harmony/functional-harmony.md` (numbers, functions, cadences, errors).
**Base:** `chatmu-studio-compose-core` (clip flow; MIDI 60 = C3 in Live).

## When to use
Before writing any chord track, or when the user asks what chord goes where, why a
progression sounds wrong, or how to reharmonize. If the task is melody over existing
chords, use `chatmu-studio-melody-over-chords` instead.

## Workflow

1. **Get the key and the intent.** Ask only if missing: key, mode, mood, genre, how many bars.
2. **Choose the function path**, not the chords:
   - close → V–I (PAC final, IAC internal)
   - question → end on V (HC) or V–vi (DC)
   - loop → I–V–vi–IV or vi–IV–I–V
   - minor urban → i–♭VI–♭III–♭VII
   - jazz → ii7–V7–Imaj7
3. **Pick the voicing.** Prefer 3rd/5th in the top voice; keep chords in MIDI 48–79;
   below 52 only roots, 5ths and octaves.
4. **Voice-lead every change**: common tones stay, other voices move by step,
   dominant 7th resolves down, leading tone resolves up, no parallel 5ths/8ves.
5. **Write it** with `local_ableton_write_notes`: one note object per voice, same start,
   duration ≈ 0.9–1× the chord length, velocity 70–95.
6. **Play it** with `local_ableton_fire` and let the user hear. Offer one variation only.

## Hard rules
- Every chord must have a Roman numeral and a function. If you cannot name it, do not write it.
- In minor, the dominant is V (or v). ♭VII is the subtonic, not the dominant.
- In major, the I chord with a 7th is Imaj7, never I7 (except blues/secondary dominant).
- Do not double the 3rd in a 4-voice chord.
- Never hold an avoid note on a strong beat; use it as a passing tone or resolve it.
- If the user corrects a chord, they are right: update the map and continue.

## Output to the user
One line with key, mode, tempo and the progression in numerals and letters:
`B minor · 88 BPM · i–♭VI–♭III–♭VII (Bm–G–D–A)`.
Then the MIDI you wrote and one optional variation.

## Do not
- Do not invent a key if the user did not give one; propose one and say why.
- Do not stack 7 extensions on every chord; density is a genre decision.
- Do not present theory as taste: the function is objective, the mood is a choice.
