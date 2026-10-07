---
name: chatmu-studio-harmony-voicing
description: >
  Use in Co-Producer to write chords and chord progressions in Ableton Live
  with correct Roman numerals, voicings and voice leading, by genre and mood
  (pop, reggaetón, trap, lo-fi, deep house, R&B, cinematic). Trigger phrases:
  "acordes", "progresión de acordes", "chords", "chord progression", "armonía",
  "harmony", "voicing", "inversiones", "acordes tristes", "sad chords", "acordes
  de lo-fi", "jazzy chords", "séptimas", "7ths", "pad", "piano chords".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Chord progressions by genre with correct numerals, voicings and voice leading"
version: "1.0"
tags: [studio, ableton, harmony, chords, acordes, voicing, co-producer]
requiresTools: ["local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_get_notes"]
---

# Chatmu Studio — Harmony & Voicing
**Version:** 1.0
**Use with:** `chatmu-studio-compose-core` (clip flow + pitch map; MIDI 60 = C3 in Live).

## 1. Diatonic chords

| Major key | I | ii | iii | IV | V | vi | vii° |
|---|---|---|---|---|---|---|---|
| C major | C | Dm | Em | F | G | Am | B° |
| with 7ths | Cmaj7 | Dm7 | Em7 | Fmaj7 | G7 | Am7 | Bm7♭5 |

| Natural minor | i | ii° | ♭III | iv | v | ♭VI | ♭VII |
|---|---|---|---|---|---|---|---|
| A minor | Am | B° | C | Dm | Em | F | G |
| with 7ths | Am7 | Bm7♭5 | Cmaj7 | Dm7 | Em7 | Fmaj7 | G7 |

- **Harmonic minor** raises the 7th: the v becomes **V (E / E7 in A minor)** — the real
  dominant that pulls back to i. Use it at phrase ends.
- **Dorian** (minor with major 6th) turns iv into **IV (D / D7 in A Dorian)**.
- In a minor key the **dominant is V (or v)**, built on the 5th degree. ♭VII is the
  *subtonic*, not the dominant.

## 2. Progressions by genre (examples in C major / A minor)

| Genre / mood | Progression | Example | Harmonic rhythm |
|---|---|---|---|
| Pop, uplifting | I–V–vi–IV | C–G–Am–F | 1 chord / bar |
| Pop, emotional | vi–IV–I–V | Am–F–C–G | 1 / bar |
| Reggaetón | i–♭VI–♭III–♭VII | Am–F–C–G | 1 / bar, 4-bar loop |
| Reggaetón (darker) | i–iv–♭VII–♭III | Am–Dm–G–C | 1 / bar |
| Trap, dark | i–♭VI–iv–V | Am–F–Dm–E | 1–2 bars / chord |
| Trap, phrygian | i–♭II | Am–B♭ | 2 bars / chord |
| Lo-fi / neo-soul | ii7–V7–Imaj7 | Dm7–G7–Cmaj7 | 1 / bar (I lasts 2) |
| Lo-fi | Imaj7–vi7–ii7–V7 | Cmaj7–Am7–Dm7–G7 | 1 / bar |
| Lo-fi minor / Dorian | i7–IV7 | Am7–D7 | 1–2 bars / chord |
| Deep house | i7–iv7 (or a one-chord i9 vamp) | Am7–Dm7 | 2 bars / chord |
| Deep house | i7–♭VII–♭VImaj7–♭VII | Am7–G–Fmaj7–G | 1 / bar |
| R&B | IVmaj9–iii7–vi9 | Fmaj9–Em7–Am9 | 1 / bar |
| R&B | ii9–V13–Imaj9 | Dm9–G13–Cmaj9 | 1 / bar |
| Cinematic / sad | i–♭VI–♭III–♭VII | Am–F–C–G | 1–2 bars |
| Tension / epic | i–iv–♭VI–V | Am–Dm–F–E | 1 / bar |

Transpose by moving every MIDI pitch by the same number of semitones.

## 3. Voicings

- **Close:** all chord tones within an octave (C E G).
- **Inversions:** 1st = 3rd in the bass voice (E G C), 2nd = 5th lowest (G C E). Use them
  to keep the top voice smooth, not to change the bass — the bass track plays roots.
- **Open / spread:** root + 5th low, 3rd + 7th (+9th) an octave up. Good for pads, piano.
- **Drop-2:** take a 4-note close voicing and drop the 2nd-highest note one octave.
  Cmaj7 close = C60 E64 G67 B71; the 2nd from the top is G67 → drop-2 = G55 C60 E64 B71.
  Warm for keys/guitar.
- **Shell:** root + 3rd + 7th. Clean under a busy melody.
- **Rootless (jazzy keys):** 3–5–7–9 or 7–9–3–13 with the bass playing the root.

Register rules (MIDI): keep chord tones between **48 and 79**; below ~52 use only roots,
5ths and octaves (thirds there sound muddy). Do not double the 3rd in a 4-voice chord.
The top voice is a melody — move it by step.

## 4. Voice leading (always)

1. Keep **common tones** in the same voice.
2. Move every other voice to the **nearest** tone of the next chord (step or stay).
3. Avoid parallel 5ths/octaves between the top voice and the bass in exposed parts.
4. Resolve tendency tones: 7th of a dominant chord steps **down**; the leading tone
   (raised 7th) steps **up** to the root.

### Worked example A — reggaetón Am–F–C–G (voice-led triads, 1 bar each)

| Bar | Chord | Upper voices (MIDI) | Bass (MIDI) |
|---|---|---|---|
| 1 | Am | 57 A, 60 C, 64 E | 45 A |
| 2 | F | 57 A, 60 C, 65 F | 41 F |
| 3 | C | 55 G, 60 C, 64 E | 48 C |
| 4 | G | 55 G, 59 B, 62 D | 43 G |

Each change moves at most two voices by 1–2 semitones.

### Worked example B — ii–V–I with rootless 4-voice voicings (C major)

| Chord | Voices (MIDI) | Degrees | Bass |
|---|---|---|---|
| Dm9 | 53 F, 57 A, 60 C, 64 E | 3 5 7 9 | 38 D |
| G13 | 53 F, 57 A, 59 B, 64 E | 7 9 3 13 | 43 G |
| Cmaj9 | 52 E, 55 G, 59 B, 62 D | 3 5 7 9 | 36 C |

Notes for `local_ableton_write_notes`: one note object per voice, same `start`,
`duration` ≈ 0.9–1 × the chord length (slightly short avoids smearing), velocity 70–95,
top voice a bit louder than the inner voices.

## 5. Rhythm of chords per genre

- **Pop / R&B keys:** sustained or 8th-note pulses; anticipate the next chord by an
  8th or 16th sometimes.
- **Reggaetón:** sustained pads or plucks following the dembow (stabs on the "a" of 1
  and the "&" of 2 — see drums skill).
- **House:** short stabs on off-beats (the "&") or a syncopated 3-3-2 pattern.
- **Lo-fi:** long chords, slightly late, low velocity (60–85), roll the chord tones
  10–30 ms apart (see humanize).
- **Trap:** sustained pads/bells, often only 2 chords; the melody carries the movement.

## Corrections vs. the upstream material

The source skills had theory mistakes that this version fixes:
- "Cm – F – Cm – G7 (i-iv-i-V)": F major in C minor is **IV** (Dorian), not iv.
- "Cmaj7 – Fmaj7 – B♭7 – E♭7 (mixolydian feel)": B♭7/E♭7 are borrowed/chromatic
  chords, not C Mixolydian (which would give B♭maj and Gm7, not E♭7).
- F-minor example voiced the A♭ chord as C–E♭–G (that is C minor); A♭ = A♭–C–E♭.
- Called E♭ "dominant" in F minor; it is ♭VII (subtonic). The dominant is C / C7.
- "Cmaj7–Em7–Am7–Dm7 (I7-…)": the I chord is **Imaj7**, not I7 (a dominant 7th).

## Credits & license

Adapted and corrected from `chord-pro` and `midi-cleanup` in
[glincker/ableton-skills](https://github.com/glincker/ableton-skills),
Copyright (c) 2026 Glincker, MIT License. Full text in
`LICENSE-glincker-ableton-skills.txt` in this folder.
