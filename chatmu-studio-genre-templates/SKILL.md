---
name: chatmu-studio-genre-templates
description: >
  Use in Co-Producer to start a track in Ableton Live in a specific genre:
  tempo, key/scale, chord progression, drums, bass, Live stock instruments and
  effects, and song structure in bars. Genres: lo-fi, deep house, reggaetón,
  trap, pop, R&B. Trigger phrases: "hazme un reggaetón", "beat de reggaetón",
  "reggaeton", "lo-fi", "lofi", "deep house", "house", "trap", "pop", "R&B",
  "rnb", "empezar una canción", "start a track", "plantilla", "template",
  "estructura de la canción", "song structure", "qué BPM", "what tempo".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Genre starting points for Ableton: BPM, keys, chords, drums, sounds, structure"
version: "1.0"
tags: [studio, ableton, genre, reggaeton, trap, lofi, house, pop, rnb, co-producer]
requiresTools: ["local_ableton_snapshot", "local_ableton_set_tempo", "local_ableton_edit_track", "local_ableton_browser", "local_ableton_load_device", "local_ableton_arrangement"]
---

# Chatmu Studio — Genre Templates
**Version:** 1.0
**Use with:** `chatmu-studio-compose-core`, `chatmu-studio-harmony-voicing`,
`chatmu-studio-drums-by-genre`, `chatmu-studio-bass-lines`, `chatmu-studio-humanize`.

## How to use a template

1. Confirm genre + any user constraints (tempo, key, reference song). The user's choices
   always beat the template.
2. `local_ableton_snapshot` → reuse existing tracks; don't rebuild what exists.
3. Set tempo only with OK (`local_ableton_set_tempo`).
4. Tracks: `local_ableton_edit_track` `create_midi` (approval) — name them (`rename`).
   Load sounds with `local_ableton_load_device` (approval). **Look the device up first**
   with `local_ableton_browser` (paths `instruments`, `drums`, `audio_effects`): if a
   device isn't in the user's Live edition (some are Suite-only), pick another.
5. Two return tracks by default: reverb and delay (`load_device` `target: "return"`).
6. Write a 4–8 bar loop in Session (one scene), let the user react, then extend to the
   structure (`chatmu-studio-session-vs-arrangement` to place it on the timeline and
   `create_locator` for sections).

Bars are 4/4. Beats = bars × 4. **Seconds per bar = 240 / BPM** (90 BPM → 2.67 s, so 2 minutes ≈ 45 bars;
128 BPM → 1.875 s, so 3 minutes ≈ 96 bars).

---

## Lo-fi hip-hop
- **Tempo:** 70–90 BPM (default 82). Backbeat (snare on 2 & 4), swung 55–62 %.
- **Keys/scales:** major with 7ths/9ths, or minor/Dorian (Am7–D7).
- **Chords:** ii7–V7–Imaj7, Imaj7–vi7–ii7–V7; 1 chord per bar; rolled, slightly late.
- **Drums:** lo-fi pattern (drums skill), soft kick, dusty snare, swung hats.
- **Bass:** round, root on 1 + passing notes; low velocity.
- **Sounds:** electric piano (Electric, or a Rhodes-like Simpler/Operator preset), soft pad
  (Wavetable/Drift), vinyl texture.
- **FX:** Vinyl Distortion or Redux (light), Auto Filter low-pass on the master group of
  music, Saturator, Reverb; Glue Compressor on drums.
- **Structure (~2–3 min):** Intro 4–8 · A 16 · B 16 · A 16 · Outro 8.

## Deep house
- **Tempo:** 118–124 BPM (default 122). Four-on-the-floor, off-beat open hats, light swing.
- **Keys/scales:** minor, Dorian, minor 7th/9th chords.
- **Chords:** i7–iv7 (2 bars each), i9 one-chord vamp, i7–♭VII–♭VImaj7–♭VII; short stabs on
  the "&" or long pads.
- **Bass:** off-beat (starts 0.5, 1.5, 2.5, 3.5) or rolling 8ths, root + octave + 7th.
- **Sounds:** organ/stab chords (Operator/Wavetable), warm pad, sub bass.
- **FX:** Auto Filter sweeps, Echo/Delay on stabs, Reverb return, sidechain feel on pads.
- **Structure (DJ-friendly, phrases of 8/16):** Intro 16–32 · Groove 16 · Main 32 ·
  Breakdown 16 · Main 32 · Outro 16–32.

## Reggaetón
- **Tempo:** 88–100 BPM (default 94). Dembow, straight (no swing).
- **Keys/scales:** natural minor (most common); harmonic minor for hooks with a V.
- **Chords:** i–♭VI–♭III–♭VII (Am–F–C–G) or i–iv–♭VII–♭III; 1 chord per bar, 4-bar loop.
- **Drums:** dembow — kick every beat, snare on steps 4 7 12 15; layered rim/clap;
  extra percussion (timbal, shaker) straight 16ths.
- **Bass:** tresillo (starts 0, 0.75, 1.5 each half bar) on the root; 808 or sub.
- **Sounds:** plucked synth or piano for chords (Wavetable/Operator/Drift), pad, perc kit.
- **FX:** short Reverb on snare, Delay throws on vocal/lead, Saturator on 808.
- **Structure (~3 min):** Intro 4–8 · Verse 16 · Pre 4–8 · Chorus 8–16 · Verse 16 ·
  Chorus · Bridge 8 · Chorus · Outro 4–8.

## Trap
- **Tempo:** 130–150 BPM (default 140), **half-time** (clap on beat 3).
- **Keys/scales:** natural minor, harmonic minor (V chord, raised 7th), phrygian (♭II).
- **Chords:** i–♭VI, i–♭VI–iv–V, i–♭II; 1–2 bars per chord; dark pads, bells, plucks.
- **Drums:** trap pattern (drums skill): sparse kick, clap step 9, 8th hats + 1/32 and
  1/16-triplet rolls, occasional open hat.
- **Bass:** 808 following the kick, long notes, glides (bass skill).
- **Sounds:** bell/pluck lead (Operator/Wavetable), dark pad, 808 (Simpler with an 808
  sample or Operator sine with pitch envelope).
- **FX:** Saturator on 808, Reverb/Delay on the lead, Glue on drums.
- **Structure:** Intro 4–8 · Hook 16 · Verse 16 · Hook 16 · Verse 16 · Hook 16 · Outro 4–8
  (bars at the set tempo).

## Pop
- **Tempo:** 100–125 BPM (ballads 60–80).
- **Keys/scales:** major (I–V–vi–IV) or minor (vi–IV–I–V in the relative major).
- **Chords:** I–V–vi–IV, vi–IV–I–V, I–vi–IV–V; 1 chord per bar.
- **Drums:** pop pattern (kick 1 9 11, snare 5 13, 8th hats); build-ups with snare rolls.
- **Bass:** 8th-note roots or syncopated; follow the kick.
- **Sounds:** piano, synth pad, pluck, guitar-like (Simpler), claps.
- **FX:** Reverb/Delay returns, Compressor, Auto Filter risers.
- **Structure (~3 min):** Intro 4–8 · Verse 8–16 · Pre 4–8 · Chorus 8 · Verse 8–16 ·
  Pre 4–8 · Chorus 8 · Bridge 8 · Chorus 8–16 · Outro 4.

## R&B (contemporary)
- **Tempo:** 60–80 BPM (or 120–160 set as double time).
- **Keys/scales:** major with 9ths/13ths, minor 9ths, Dorian; pentatonic runs in melodies.
- **Chords:** ii9–V13–Imaj9, IVmaj9–iii7–vi9; 1 chord per bar; anticipations.
- **Drums:** R&B pattern (kick 1 8 11, snare/snaps 5 13), swung 16th hats, triplet runs.
- **Bass:** sub or electric-style with slides; chord tones and approach notes.
- **Sounds:** electric piano, warm pad, soft lead; finger snaps.
- **FX:** Chorus-Ensemble on keys, Reverb (plate-like), Echo; gentle Compressor.
- **Structure:** Intro 4 · Verse 8–16 · Pre 4 · Hook 8 · Verse 8–16 · Hook 8 · Bridge 8 ·
  Hook 8–16 · Outro 4.

---

## Corrections vs. the upstream material

- "Lo-fi: kick on 1, snare/clap on 3" and "lo-fi house at 95 BPM, snare on 3" → lo-fi
  hip-hop is a backbeat (2 & 4); lo-fi house is house tempo (≈115–125) with four-on-the-floor.
- "Trap at 140 is half-time: drums hit on every other beat" → half-time means the
  backbeat snare moves from beats 2 & 4 to beat 3; hats keep moving at 8ths/16ths.
- "2:00 = ~50 bars at 90 BPM" → 2:00 at 90 BPM is 45 bars (240 / 90 = 2.67 s per bar).
- Tempo ranges were checked and reggaetón/R&B templates were added.

## Credits & license

Tempo tables and setup flow adapted and corrected from `producer-mode`, `tempo-coach` and
`arrangement-coach` in [glincker/ableton-skills](https://github.com/glincker/ableton-skills),
Copyright (c) 2026 Glincker, MIT License. Full text in
`LICENSE-glincker-ableton-skills.txt` in this folder.
