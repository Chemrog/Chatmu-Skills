---
name: chatmu-studio-harmony
description: >
  Writes chords and chord progressions in the user's Ableton Live set with real
  function, cadences, genre colour, voicings and voice leading — and reharmonizes
  existing progressions. Covers major/minor/modal harmony, progressions by genre
  and mood, close/open/drop-2/shell/rootless voicings, chord rhythm per genre,
  secondary dominants, borrowed chords and substitutions. Trigger phrases:
  "chords", "chord progression", "harmony", "voicing", "inversions", "cadence",
  "reharmonize", "sad chords", "jazzy chords", "7ths", "pad", "piano chords",
  "acordes", "progresión", "armonía", "rearmonizar", "acordes tristes",
  "acordes jazzeros", "séptimas", "inversiones".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Chords with function, cadences, genre colour, voicings and voice leading; reharmonization"
version: "1.0"
tags: [studio, ableton, harmony, chords, voicing, cadence, reharmonization]
requiresTools:
  - local_music_theory
  - local_harmony_map
  - local_ableton_tracks
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_get_notes
  - local_ableton_fire
---

# Chatmu Studio — Harmony

A progression is a **direction**, not a list of chords: rest → movement → tension → release.
Pick the direction first (function), then the colour (genre), then the voicing (how it sits),
then the rhythm (how it is played). Merges the former `harmony-functional` and
`harmony-voicing` skills.

Related: chords under an existing melody → `chatmu-studio-harmonize-melody`; melody over
chords → `chatmu-studio-hook-melody` / `chatmu-studio-melody-over-chords`; clip basics and
the pitch map (MIDI 60 = C3 in Live) → `chatmu-studio-compose-core`.

## When to use
Writing a chord track, choosing what chord goes where, fixing a progression that "sounds
wrong" or "boring", making chords richer, or reharmonizing.

## Workflow
1. **Key, intent, genre, bars.** Read the set first (`local_harmony_map` if music exists).
   Ask only what is missing; if there is no key, propose one and say why (vocal range,
   instrument, genre habit).
2. **Choose the function path** (decision tree below).
3. **Add the genre colour** (progression table, colour tools).
4. **Get voiced notes** from `local_music_theory`:
   `action: progression` with `key` + `numerals` (or a `genre` preset: pop, sad, reggaeton,
   trap, lofi, rnb, deep_house, house, edm, cinematic, corridos, jazz, andalusian),
   `voicing` (close / drop2 / spread), `voiceLeading: true`, `beatsPerChord`, `bass: true`
   when a bass/808 track needs roots. `action: chords` does the same from chord symbols.
   Never compute MIDI by hand.
5. **Shape the rhythm** for the genre (section "Chord rhythm"), editing starts/durations.
6. **Write** with `local_ableton_create_clip` + `local_ableton_write_notes`; one note per voice;
   duration ≈ 0.9–1 × chord length; velocity 70–95, top voice slightly louder.
7. **Verify** with `local_harmony_map` (that scene): each bar must read as the chord you meant.
8. **Play** with `local_ableton_fire`. Offer one variation only (simpler or richer).

## 1. Diatonic chords
| Major | I | ii | iii | IV | V | vi | vii° |
|---|---|---|---|---|---|---|---|
| C major | C | Dm | Em | F | G | Am | B° |
| with 7ths | Cmaj7 | Dm7 | Em7 | Fmaj7 | G7 | Am7 | Bm7♭5 |

| Natural minor | i | ii° | ♭III | iv | v | ♭VI | ♭VII |
|---|---|---|---|---|---|---|---|
| A minor | Am | B° | C | Dm | Em | F | G |
| with 7ths | Am7 | Bm7♭5 | Cmaj7 | Dm7 | Em7 | Fmaj7 | G7 |

- **Harmonic minor** raises the 7th: **V (E/E7 in A minor)** and vii° — the real dominant
  that pulls home. Use it at phrase ends.
- **Dorian** (minor + major 6th): iv becomes **IV** (D/D7 in A Dorian) — lo-fi, funk, soul.
- **Mixolydian** (major + ♭7): ♭VII (B♭ in C) — rock, pop anthems.
- **Phrygian** (minor + ♭2): ♭II (B♭ in A) — trap, drill, flamenco, metal.
- In minor the **dominant is V (or v)**; ♭VII is the subtonic, not the dominant.

## 2. Functions and cadences
| Function | Chords | Role |
|---|---|---|
| Tonic | I (i) | rest |
| Tonic prolongation | vi, iii (♭III, ♭VI in minor) | share two notes with I; move away gently |
| Pre-dominant | IV, ii (iv, ii°) | prepares tension |
| Dominant | V, vii° | wants to resolve to I |

Normal flow: **T → (prolongation) → PD → D → T**. Accepted exceptions: IV→I (plagal),
V→vi (deceptive), V→IV (rock/pop "backwards" motion — a choice, say so).

| Cadence | Formula | Effect |
|---|---|---|
| Perfect authentic | V–I, roots in the bass, tonic on top | strong close (song end) |
| Imperfect authentic | V–I with inversion or 3rd/5th on top | soft close (phrase end) |
| Plagal | IV–I (iv–I for bittersweet) | "amen", gentle |
| Deceptive | V–vi | surprise, keeps going |
| Half | ends on V | question |
| Modal | ♭VII–I / ♭VI–♭VII–I | rock/pop/epic close without a leading tone |

### Decision tree
```
Need a close?          → V–I (PAC at the end; IAC inside)
Need a question?       → end on V (HC) or V–vi (DC)
Loop without a close?  → I–V–vi–IV or vi–IV–I–V
Minor urban loop?      → i–♭VI–♭III–♭VII
Darker / static?       → i–♭II, or a pedal on i with one moving chord
Jazzy loop?            → ii7–V7–Imaj7 (or iii–vi–ii–V)
Modern colour?         → add 9/11/13, omit the 5th
Modulate?              → pivot chord shared by both keys, or V/new key
Melody clashes?        → change the chord so the melody note is its 3rd/5th/7th/9th
```

## 3. Progressions by genre (C major / A minor)
| Genre / mood | Progression | Example | Harmonic rhythm |
|---|---|---|---|
| Pop, uplifting | I–V–vi–IV | C–G–Am–F | 1 / bar |
| Pop, emotional | vi–IV–I–V | Am–F–C–G | 1 / bar |
| Pop, lift into chorus | IV–V–vi / ii–IV–V | F–G–Am | 1 / bar, faster at the end |
| Rock | I–♭VII–IV / I–IV–V / i–♭VI–♭VII | C–B♭–F | 1 / bar |
| Reggaetón | i–♭VI–♭III–♭VII | Am–F–C–G | 1 / bar, 4-bar loop |
| Reggaetón, darker | i–iv–♭VII–♭III | Am–Dm–G–C | 1 / bar |
| Trap, dark | i–♭VI–iv–V | Am–F–Dm–E | 1–2 bars / chord |
| Trap, phrygian | i–♭II | Am–B♭ | 2 bars / chord |
| Lo-fi / neo-soul | ii7–V7–Imaj7 / Imaj7–vi7–ii7–V7 | Dm7–G7–Cmaj7 | 1 / bar |
| Lo-fi Dorian | i7–IV7 | Am7–D7 | 1–2 bars |
| Deep house | i7–iv7, or a one-chord i9 vamp | Am7–Dm7 | 2 bars |
| House | i7–♭VII–♭VImaj7–♭VII | Am7–G–Fmaj7–G | 1 / bar |
| R&B | IVmaj9–iii7–vi9 / ii9–V13–Imaj9 | Fmaj9–Em7–Am9 | 1 / bar |
| Cinematic / sad | i–♭VI–♭III–♭VII / ♭VI–♭VII–i | Am–F–C–G | 1–2 bars |
| Epic / tension | i–iv–♭VI–V | Am–Dm–F–E | 1 / bar |
| Andalusian (flamenco, Latin) | i–♭VII–♭VI–V | Am–G–F–E | 1 / bar |
| Regional mexicano | I–IV–V7, with V7/IV and V7/V | C–C7–F–D7–G7 | 1 / bar |
| Ambient | Imaj7–IVmaj7 (lydian), pedal + add9 | Cmaj7–Fmaj7 | 2–4 bars |

Transpose by moving every pitch the same number of semitones.

## 4. Colour tools (and when they work)
| Tool | Example (C major) | Use when |
|---|---|---|
| Borrowed iv | F → Fm → C | bittersweet return home (pop, ballads) |
| ♭VI, ♭VII from minor | A♭, B♭ | epic, rock, cinematic lift |
| Secondary dominant V/x | E7 → Am (V/vi), D7 → G (V/V) | push into a chord; the melody must allow the raised note |
| Sus2 / sus4 | Csus4 → C | openness at phrase starts; resolve the 4th to the 3rd |
| Add9 / maj7 / m9 | Cadd9, Fmaj7, Am9 | modern pop, R&B, ambient (omit the 5th) |
| Pedal tone | C in the bass under C–F/C–G/C | static, hypnotic, intros, trap, ambient |
| Line cliché | Am–Am(maj7)–Am7–Am6 | one inner voice moves by semitone; ballads, bossa |
| Tritone substitution | D♭7 for G7 | jazz, neo-soul; bass moves by semitone |
| Chromatic approach | B7 → C, D♭maj7 → C | R&B/gospel cadences |
| Relative swap | Am for C, Em for G | softer version of the same function |

Reharmonizing a progression: keep the melody notes, keep the cadence points, change what is
between — swap within the same function first (ii for IV, vi for I), then add secondary
dominants into strong targets, then substitutions. Present one reharm at a time.

## 5. Voicings
- **Close:** all tones within an octave (C E G).
- **Inversions:** 1st = 3rd lowest, 2nd = 5th lowest. Use them to keep the top voice smooth;
  the bass track still plays roots unless you want a bass line (I – V/7 – vi).
- **Open / spread:** root + 5th low, 3rd + 7th (+9) an octave up — pads, piano, cinematic.
- **Drop-2:** from a 4-note close voicing, drop the 2nd-highest note an octave.
  Cmaj7 close C60 E64 G67 B71 → drop-2 G55 C60 E64 B71. Warm keys/guitar.
- **Shell:** root + 3rd + 7th — clean under a busy melody.
- **Rootless (jazz keys):** 3–5–7–9 or 7–9–3–13 over a bass playing the root.
- **Power chord (rock):** root + 5th (+ octave); no 3rd.

Register: chord tones in MIDI **48–79**; below 52 only roots, 5ths, octaves. Don't double
the 3rd in 4 voices. The top voice is a melody: move it by step. Keep chords below the lead
melody and out of the vocal's 1–4 kHz space when possible (pads lower, fewer notes).

## 6. Voice leading (always)
1. Common tones stay in the same voice.
2. Other voices move to the nearest tone (step or semitone).
3. Dominant 7th resolves **down**; leading tone (raised 7̂) resolves **up**.
4. No parallel 5ths/octaves between the outer voices in exposed parts.
5. Guide tones in ii–V–I: 7th of ii → 3rd of V; 3rd of V → 7th of I.

Worked example — reggaetón Am–F–C–G, 1 bar each:
| Bar | Chord | Upper voices (MIDI) | Bass |
|---|---|---|---|
| 1 | Am | 57 A, 60 C, 64 E | 45 A |
| 2 | F | 57 A, 60 C, 65 F | 41 F |
| 3 | C | 55 G, 60 C, 64 E | 48 C |
| 4 | G | 55 G, 59 B, 62 D | 43 G |

Worked example — ii–V–I rootless (C major):
| Chord | Voices (MIDI) | Degrees | Bass |
|---|---|---|---|
| Dm9 | 53 F, 57 A, 60 C, 64 E | 3 5 7 9 | 38 D |
| G13 | 53 F, 57 A, 59 B, 64 E | 7 9 3 13 | 43 G |
| Cmaj9 | 52 E, 55 G, 59 B, 62 D | 3 5 7 9 | 36 C |

## 7. Chord rhythm by genre
| Genre | How the chords are played |
|---|---|
| Pop / R&B keys | sustained or 8th pulses; anticipate the next chord by an 8th/16th sometimes |
| Rock | 8th-note downstrokes (power chords), accents on 2 and 4 with the snare |
| Reggaetón | pads or plucks following the dembow: stabs on 0.75 and 1.5 of each half-bar |
| House | short off-beat stabs (0.5, 1.5, 2.5, 3.5) or a 3-3-2 pattern |
| Lo-fi | long, slightly late, velocity 60–85, chord tones rolled 10–30 ms apart |
| Trap | sustained pads/bells, often 2 chords; the melody carries the movement |
| Ambient | 2–4 bar chords, slow attack, overlapping releases |
| Regional mexicano | bass on 1, chord on the off-beats (oom-pah) or arpeggiated requinto |

## Hard rules
- Every chord has a numeral and a function. If you can't name it, don't write it.
- In major, the I chord with a 7th is **Imaj7** (I7 only in blues or as V/IV).
- Don't stack extensions on every chord; density is a genre decision.
- If the user corrects a chord, they are right for their song: update and continue.
- Function is objective; mood is a choice — never present taste as theory.

## Corrections carried from the upstream material
F major in C minor is **IV** (Dorian), not iv. B♭7/E♭7 over C are borrowed/chromatic, not
C Mixolydian. A♭ = A♭–C–E♭ (not C–E♭–G). In F minor the dominant is C/C7; E♭ is ♭VII.
Cmaj7–Em7–Am7–Dm7 starts on **Imaj7**, not I7.

## Credits & license
Voicing tables adapted and corrected from `chord-pro` and `midi-cleanup` in
glincker/ableton-skills — Copyright (c) 2026 Glincker, MIT License.

## Tell the user (short)
`A minor · 92 BPM · i–♭VI–♭III–♭VII (Am–F–C–G), 1 per bar, voice-led triads on "Chords", bass roots on "Bass". Variation offered: Am9–Fmaj7–C–G6 for an R&B colour.`
