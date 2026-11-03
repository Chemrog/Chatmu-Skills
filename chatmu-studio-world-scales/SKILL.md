---
name: chatmu-studio-world-scales
description: >
  Writes music in Arabic maqam and Hindustani raga the way the traditions work —
  tonic drone, characteristic phrases (sayr, pakad), ascent/descent rules,
  emphasized notes, ornaments, rhythmic cycles — in the user's Ableton Live set,
  and handles quarter tones honestly (12-TET compromise, a detuned second voice,
  or Live's tuning systems). Also pentatonic and other modal colours. For urban
  fusion with an Arabic colour use chatmu-studio-genre-oriental-hiphop.
  Trigger phrases: "maqam", "raga", "Arabic scale", "Indian scale", "quarter
  tones", "microtonal", "Bayati", "Rast", "Hijaz", "Yaman", "Bhairav",
  "Bhairavi", "tanpura", "drone", "escala árabe", "escala india", "cuartos de
  tono", "microtonal", "raga", "maqam", "suena indio", "suena árabe".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Maqam and raga done right: drone, sayr/pakad, ascent/descent, ornaments, honest quarter-tone handling"
version: "2.0"
tags: [studio, ableton, scales, maqam, raga, microtonal, world, drone]
requiresTools:
  - local_music_theory
  - local_ableton_tracks
  - local_ableton_edit_track
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_fire
  - local_synth_find_preset
  - local_synth_set_preset
  - local_synth_list_params
  - local_synth_set_params
  - local_synth_modulate
---

# Chatmu Studio — World scales (maqam and raga)

A maqam or a raga is not a scale. It is a scale **plus a way of moving**: which notes lead,
which ones you rest on, which phrases identify it, which direction notes are approached from,
how they are ornamented. Running the notes up and down sounds like a textbook; following the
characteristic phrases sounds like the music. This skill writes the phrases.

Rewrite of the earlier DeepSeek version: the old rules forbade 12-TET and Western chords
outright. Here: **in a traditional context** keep the drone and no chord changes; **in an urban
fusion** use `chatmu-studio-genre-oriental-hiphop`, where 12-TET Hijaz over a pedal is the
genre's normal practice.

## 1. Quarter tones — decide and say it
`local_ableton_write_notes` writes 12-TET notes only (no pitch bend). Pick one route and tell
the user which:
| Route | How | When |
|---|---|---|
| **A. 12-TET compromise** | Use maqamat without quarter tones (Hijaz, Nahawand, Kurd, Ajam, Nikriz) or the closest 12-TET version | sketches, fusion, no time for setup |
| **B. Detuned second voice** | Two instances of the same Chatmu Synth preset: voice 1 normal; voice 2 detuned −50 cents (find the oscillator tune/fine parameter with `local_synth_list_params`, set it with `local_synth_set_params`). Put every half-flat note (E½♭, B½♭…) on voice 2 at the 12-TET pitch a semitone **above** the target, so −50 cents lands on it. | real Rast/Bayati/Sikah/Saba melodies, monophonic lines |
| **C. Live's tuning system** | The user loads a maqam tuning file (.scl/.ascl) into Live 12's Tuning (Set-wide); then MIDI notes map to the tuned pitches | exact intonation, the user can do one setup step |
Never approximate a quarter-tone maqam silently. Ragas need no quarter tones in practice
(12-TET is acceptable; the *andolan* oscillation is what matters — see ornaments).

## 2. The drone (always, in traditional mode)
- **Tanpura (raga):** Sa + Pa (or Sa + Ma when the raga omits Pa, e.g. Malkauns; Sa + Ni for
  Marwa-type ragas). Pluck cycle per 4 beats: Pa (low), Sa (high), Sa (high), Sa (low) on
  beats 0, 1, 2, 3, each held ~3.5 beats, velocity 60–80 with ±8 variation. Register: low Sa
  MIDI 48–52.
- **Maqam:** sustained tonic (+ 5th) on strings/pad, or an oud/qanun tonic pulse; quieter than
  the melody (−10 to −14 dB).
- No chord changes over the drone. Harmony is the drone + the melody.

## 3. Maqam
### Common maqamat (tonic D unless noted; ½♭ = half-flat)
| Maqam | Notes | Lower jins → upper jins | Character | 12-TET option |
|---|---|---|---|---|
| Rast (C) | C D E½♭ F G A B½♭ C | Rast on C → Rast on G | stately, "mother" maqam | none faithful — route B/C |
| Bayati | D E½♭ F G A B♭ C D | Bayati on D → Nahawand on G | warm, common, folk | Kurd (E♭) as stand-in, say so |
| Hijaz | D E♭ F♯ G A B♭ C D | Hijaz on D → Nahawand/Rast on G | intense, augmented 2nd | exact (0 1 4 5 7 8 10) |
| Nahawand (C) | C D E♭ F G A♭ B C | Nahawand on C → Hijaz/Kurd on G | lyrical, minor-like | exact |
| Kurd | D E♭ F G A B♭ C D | Kurd on D → Nahawand on G | dark, phrygian | exact |
| Sikah (E½♭) | E½♭ F G A B½♭ C D | Sikah → Rast | very characteristic neutral tonic | route B/C only |
| Saba | D E½♭ F G♭ A B♭ C | Saba (diminished 4th) | grief, unstable | route B/C |
| Ajam (C) | C D E F G A B C | Ajam → Ajam | bright, major | exact |

### Sayr — how a maqam moves
1. Open around the tonic and the first jins (notes 1–4): small steps, returning to 1.
2. Rise to the **ghammaz** (the note where the upper jins starts, usually the 4th or 5th) and
   rest there — this is the first arrival.
3. Explore the upper jins, reach the octave or above for the climax.
4. Descend through the upper jins back to the ghammaz, then down the lower jins to rest on
   the tonic. The final phrase ends on the tonic, approached from above.
Write phrases of 2–4 bars, each ending on a resting note (tonic or ghammaz). Long notes go on
resting notes; passing notes are short.

### Rhythm (iqa')
Darbuka/riq cycles in beats (D = dum low, T = tek high): Maqsum D 0, T 0.5, T 1.5, D 2, T 3 ·
Baladi D 0, D 0.5, T 1.5, D 2, T 3 · Saidi D 0, T 0.5, D 1.5, D 2, T 3 · Wahda (slow, 4 beats)
D 0, T 2. Taqsim
(improvised intro) is unmetered: no drums, free rhythm.

## 4. Raga
### Reference ragas (Sa = tonic; r/g/d/n = komal (flat), M# = tivra Ma)
| Raga | Notes | Aroha (ascent) / avaroha (descent) | Vadi / samvadi | Pakad (identifying phrase) | Time / mood |
|---|---|---|---|---|---|
| Yaman | S R G M# P D N | N R G M# D N S' / S' N D P M# G R S | G / N | N R G R S, P M# G R S | evening, serene |
| Bhairav | S r G M P d N | S r G M P d N S' / S' N d P M G r S | d / r | G M d d P, G M r r S (r and d with slow andolan) | dawn, devotional |
| Bhairavi | S r g M P d n | S r g M P d n S' / reverse | M / S | g M d P, g M r S | morning or concert close, longing |
| Bhupali | S R G P D | S R G P D S' / S' D P G R S | G / D | G R S D(low) S R G | evening, joyful |
| Malkauns | S g M d n | S g M d n S' / S' n d M g S | M / S | M g M d n d M, g S | late night, deep |
| Kafi | S R g M P D n | S R g M P D n S' / reverse | P / S | R g R S, n D P | flexible, folk, spring |
| Darbari Kanada | S R g M P d n | S R g M P d n S' / S' d n P M P g M R S | R / P | g (andolan) M R S, d (andolan) n P | late night, grave, slow |
| Desh | S R G M P D n N | S R M P N S' / S' n D P M G R G S | R / P | R M P N S', R n D P | monsoon, romantic |
| Miyan ki Todi | S r g M# P d N | S r g M# d N S' / S' N d P M# g r S | d / g | d M# g r, g r S | morning, intense |

Rules that make a raga recognisable:
- Follow aroha going up and avaroha coming down (Desh uses N up and n down; Yaman tends to
  skip S and P in the ascent).
- Rest and linger on the **vadi**; answer it with the **samvadi**.
- Use the **pakad** as the hook: it is the raga's signature phrase, repeat it at section ends.
- Unfold slowly: start in the lower/middle octave around Sa, reach the upper Sa only later.

### Tala (rhythmic cycle)
Teentaal 16 beats (4+4+4+4): sam (strongest) on beat 1, khali (the "empty" wave) on beat 9 —
resolve phrases onto the sam. Rupak 7 (3+2+2), sam on 1 (a khali beat). Keharwa 8 (4+4) for
light/folk. Alap (opening) has no tala: slow, free, drone only.

## 5. Ornaments written in MIDI
| Ornament | Tradition | How to write it |
|---|---|---|
| Kan / grace | raga, maqam | a 32nd (0.125 beat) neighbour note just before the main note, velocity −20 |
| Meend / slide | raga | no pitch bend: enable glide/portamento on the synth and overlap the two notes by a 32nd; or a quick 2–3 note chromatic run into the target |
| Andolan | raga (Bhairav r/d, Darbari g/d) | slow oscillation: `local_synth_modulate` an LFO (~3–5 Hz, small amount) to the oscillator tune on that voice, or alternate the note with its lower neighbour in 8th-triplets very softly |
| Gamak | raga | fast oscillation between two notes: alternating 16ths/32nds, accent on the main note |
| Murki | raga | quick turn: upper–main–lower–main as 32nds |
| Trill / mordent | maqam | main–upper alternations in 32nds on the first half of a long note |
| Qafla (cadence) | maqam | descending phrase to the tonic with a grace note before the last note |
One or two ornaments per phrase, on structural notes — never on every note.

## 6. Instruments and sounds
Search first with `local_synth_find_preset` (flute for bansuri/ney, strings for sarangi/violin,
guitar/pluck for oud/sitar/santoor); the factory has no dedicated Indian/Arabic genre, so the
result is a nearest match — say it. Load with `local_synth_set_preset`. Keep the melody
**monophonic**; octave doubling only.
Registers: bansuri/ney MIDI 60–86 · sitar/oud 50–77 · sarangi/violin 55–84 · tanpura 40–55.

## 7. Workflow
1. Tradition, raga/maqam, tonic, tempo or "free" (alap/taqsim). Ask only what is missing;
   propose a raga/maqam by mood and time if the user only gives a feeling.
2. Quarter-tone route (§1) — state it.
3. Tracks (`local_ableton_edit_track` `create_midi`): Drone, Melody (+ Melody ½♭ for route B),
   Percussion if metered.
4. Drone first (`local_ableton_create_clip` 4–8 bars, `local_ableton_write_notes`), fire it.
5. Melody: an opening phrase around Sa/tonic, then the pakad/sayr arrival, written with
   ornaments; fire with the drone. Use `local_music_theory` `action: scale` only to list 12-TET
   pitches in a register; the movement rules above decide the order.
6. Rhythm cycle if metered; phrases land on sam / the cycle's first beat.
7. Tell the user what to listen for (the vadi, the pakad, the ascent rule) and suggest comparing
   with a recording of the same raga/maqam by a traditional player.

## Hard rules
- State the tradition, the tonic, the quarter-tone route and the drone.
- No chord progressions under a traditional raga/maqam; drone only.
- Never run the scale straight up and down as the melody.
- Respect ascent/descent rules and the vadi/resting notes.
- Ornaments on structural notes only.
- Treat the music with respect: no caricature, no claims of authenticity a sketch doesn't have;
  for exposed parts recommend a real player.

## Tell the user (short)
`Raga Yaman · Sa = D · evening mood · 12-TET (fine for raga) · tanpura Sa–Pa · bansuri-like flute.
Opening around Ni–Re–Ga, lingers on Ga (vadi), pakad "N R G R S" closes each phrase, teentaal at
70 BPM landing on sam.`
