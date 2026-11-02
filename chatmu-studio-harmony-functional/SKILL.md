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

**Reference:** the tables and decision tree are at the end of this skill.
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

## Reference


### What it solves
Given a key and an intention (stable, tense, jazzy, epic, sad), choose the right
progression and connect it with good voice leading. This is the base for `20_genres`.

### Numbers

### Diatonic triads
| Major | I | ii | iii | IV | V | vi | vii° |
|---|---|---|---|---|---|---|---|
| Quality | M | m | m | M | M | m | dim |
| With 7th | maj7 | m7 | m7 | maj7 | 7 | m7 | m7♭5 |

| Natural minor | i | ii° | ♭III | iv | v | ♭VI | ♭VII |
|---|---|---|---|---|---|---|---|
| Quality | m | dim | M | m | m | M | M |
| With 7th | m7 | m7♭5 | maj7 | m7 | m7 | maj7 | 7 |

Harmonic minor: **V** (major, with 7th) and **vii°** appear; this is the cadential form.
Melodic minor: major IV and vi°; mostly used on an ascending line.

### Functions (Hutchinson ch. 9.4)
| Function | Chords | What it does |
|---|---|---|
| Tonic | I | rest, asks for nothing |
| Tonic prolongation | vi, iii | share 2 notes with I; move toward pre-dominant |
| Pre-dominant | IV, ii | prepares the dominant |
| Dominant | V, vii° | contains 7̂ and 2̂; wants to resolve to I |

Normal flow: **Tonic → (prolongation) → Pre-dominant → Dominant → Tonic**.
Exceptions: IV→I (plagal) and V→vi (deceptive).

### Cadences
| Type | Formula | Effect |
|---|---|---|
| Authentic (AC) | V–I | close |
| Perfect (PAC) | V–I, both root position, tonic in top voice | strong close |
| Imperfect (IAC) | V–I with inversion or 3rd/5th on top | soft close |
| Plagal (PC) | IV–I | "amen", soft close |
| Deceptive (DC) | V–vi | surprise, no close |
| Half (HC) | phrase ends on V | question, suspension |

### Voice leading (hard rules)
1. Common tones stay in the same voice.
2. Other voices move to the nearest tone (step or semitone).
3. The 7th of a dominant chord resolves **down** by step.
4. The leading tone (raised 7̂) resolves **up** to the tonic.
5. No parallel 5ths or octaves between outer voices.
6. Do not double the 3rd in a 4-voice chord.
7. Chord range: MIDI **48–79**; below 52 use only roots, 5ths and octaves.
8. The top voice is a melody: move it by step, not by odd leaps.

### Jazz (Levine ch. 2–3)
- **ii–V–I** is the basic unit: Dm7–G7–Cmaj7.
- **Guide tones** = 3rd and 7th. In ii–V–I: the 7th of ii falls to the 3rd of V;
  the 3rd of V falls to the 7th of I.
- **Chord-scale**: each chord uses its scale (Dm7 = D Dorian; G7 = G Mixolydian;
  Cmaj7 = C Ionian).
- **Avoid note** = a note to handle with care, not a banned note. On maj7, the 4th
  (F over Cmaj7); on a dominant, the 4th too. Use it as a passing tone or resolve it
  to the 3rd; never hold it.

### Principles
1. A progression is a **direction**, not a list of chords.
2. The cadence defines where the phrase ends; without a cadence there is no close.
3. The bass rules: the inversion changes what sounds good on top.
4. Fewer chords, better voice leading. Four well-connected chords beat eight badly connected.
5. The 3rd and 7th state the quality; the 5th may be omitted.
6. Tension accumulates toward the dominant and releases on the tonic.

### Decision tree

```
Need a close?              → V–I (PAC at the end; IAC internally)
Need a question?           → end on V (HC) or V–vi (DC)
Loop without a close?      → I–V–vi–IV or vi–IV–I–V
Minor urban loop?          → i–♭VI–♭III–♭VII
Jazzy loop?                → ii7–V7–Imaj7 (or iii–vi–ii–V)
Want a "modern" sound?     → add 9th/11th/13th and omit the 5th
Need a modulation?         → pivot chord shared by both keys
Melody clashes?            → move the melody to the 3rd/5th of that bar's chord
```

### Progressions by genre (starting point)
| Genre | Typical loop | Harmonic rhythm |
|---|---|---|
| Pop | I–V–vi–IV / vi–IV–I–V | 1 chord/bar |
| Reggaetón | i–♭VI–♭III–♭VII | 1/bar, 4-bar loop |
| Trap | i–♭VI–iv–V / i–♭II | 1–2 bars/chord |
| Lo-fi / neo-soul | ii7–V7–Imaj7 / Imaj7–vi7–ii7–V7 | 1/bar |
| House | i7–iv7 / i7–♭VII–♭VImaj7–♭VII | 2 bars/chord |
| R&B | IVmaj9–iii7–vi9 / ii9–V13–Imaj9 | 1/bar |
| Jazz | ii–V–I, rhythm changes | 1–2/bar |
| Cinematic | i–♭VI–♭III–♭VII / i–iv–♭VI–V | 1–2 bars |

### Common errors
- Calling ♭VII the "dominant" in minor: the dominant is V (or v); ♭VII is the subtonic.
- Using I7 in major: it is **Imaj7**; I7 only in blues or as a secondary dominant.
- Calling Dm "iv" in C minor: in natural minor it is iv (Dm); major IV is Dorian.
- Doubling the 3rd while leaving the root undoubled.
- Moving every voice by leap at each change.
- Holding an avoid note on a strong beat.

### How it is validated
- **Ears**: not applicable to harmony directly; validate by ear.
- **Ableton**: write MIDI, play with `local_ableton_fire`, listen.
- **Contrast**: same melody over two voicings; the one that does not clash wins.
- **Theory**: every chord must have a degree and a function; if you cannot name it, revise.

### Checklist
- [ ] Does every chord have a degree and a function?
- [ ] Is there a cadence where it should close?
- [ ] Do voices move by step and keep common tones?
- [ ] Does the dominant 7th fall and the leading tone rise?
- [ ] Does the bass match the written inversion?
- [ ] Does the melody land on the 3rd/5th on strong beats?
