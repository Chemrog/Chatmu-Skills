---
name: chatmu-studio-genre-oriental-hiphop
description: >
  Produces hip hop, trap and drill with an Arabic / Middle-Eastern / oriental
  colour in the user's Ableton Live set: picks the scale (Hijaz / phrygian
  dominant, double harmonic, harmonic minor, phrygian) in 12-TET, sets a tonic
  pedal and the few chords that keep the colour, writes an ornamented flute,
  oud or string hook, layers a darbuka rhythm (maqsum, baladi, saidi) over the
  hip-hop drums and tunes the 808 to the scale. Trigger phrases: "Arabic beat",
  "oriental trap", "Middle Eastern hip hop", "Arabic drill", "sounds Arabic",
  "hijaz", "phrygian dominant", "darbuka", "beat árabe", "trap árabe",
  "hip hop oriental", "suena árabe", "color árabe", "beat oriental",
  "drill árabe", "escala árabe".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Hip hop / trap / drill with Arabic colour: Hijaz in 12-TET, tonic pedal, ornamented hook, darbuka layer"
version: "1.0"
tags: [studio, ableton, genre, hip-hop, trap, drill, arabic, oriental, hijaz, fusion]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_tracks
  - local_ableton_set_tempo
  - local_ableton_edit_track
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_fire
  - local_ableton_scene_name
  - local_music_theory
  - local_synth_find_preset
  - local_synth_set_preset
  - local_ableton_browser
  - local_ableton_load_device
  - local_harmony_map
---

# Chatmu Studio — Hip hop with Arabic / oriental colour

This is a **fusion**: the body is hip hop (drums, 808, space for the rapper), the colour is
Middle-Eastern (scale, ornaments, a darbuka layer, a flute/oud/string voice). The colour must
be specific enough to sound real and restrained enough to leave room for the vocal. Two
things kill it: a caricature ("snake charmer" runs everywhere) and Western chord changes that
erase the mode.

Related: `chatmu-studio-hook-melody` (the hook method — this skill gives it the scale and the
gestures), `chatmu-studio-drum-rack`, `chatmu-studio-sound-design`, `chatmu-studio-bass-lines`,
`chatmu-mixing-progressive`. Real maqam/raga with quarter tones and a drone, not fused with hip
hop: the planned world-scales skill (see MASTER_PLAN_SKILLS.md).

## 1. Brief (ask only what is missing; propose defaults)
| Decision | Options | Default |
|---|---|---|
| Base style | boom bap 85–95 BPM · trap 130–150 (half-time feel) · drill 140–145 · reggaetón-oriental 90–100 | trap 140 |
| Colour | Arabic/Levantine · Turkish · North African (raï) · Persian · Indian | Arabic |
| Mood | dark/menacing · epic · sensual/romantic · melancholic | dark |
| Lead voice | flute/ney · oud/saz (plucked) · strings · vocal chop · bell/pluck | flute |

## 2. Pick the scale (12-TET) — say which and why
Write the scale yourself from these intervals (semitones from the tonic) and check it with
`local_music_theory` `action: scale` when the tool knows the mode name (`harmonic minor`,
`phrygian`). Phrygian dominant on X has the same notes as the harmonic minor a 5th below
(D phrygian dominant = G harmonic minor), so you can ask the tool for that.

| Scale | Intervals | Sound | Use it for |
|---|---|---|---|
| **Hijaz / phrygian dominant** | 0 1 4 5 7 8 10 | the classic "Arabic" sound; augmented 2nd between ♭2 and 3 | dark trap, drill, epic |
| **Double harmonic (Hijaz Kar / Bhairav)** | 0 1 4 5 7 8 11 | two augmented 2nds; more exotic, very dramatic | intros, hooks, Indian colour |
| **Harmonic minor (Nahawand-like)** | 0 2 3 5 7 8 11 | minor with a pull to the tonic; sensual, melancholic | R&B-ish, romantic, raï |
| **Phrygian (Kurd)** | 0 1 3 5 7 8 10 | dark, no augmented 2nd; subtle | drill, menacing, minimal |

**Microtones:** Bayati, Rast, Saba and Sikah need quarter tones. The bridge writes 12-TET notes
only. Do not fake them silently: for this genre use the 12-TET scales above (that is what the
genre normally does) and, if the user asks for Bayati/Rast specifically, say that real
quarter tones need a microtonal instrument or a recorded player, and offer Kurd (closest
12-TET to Bayati) meanwhile.

Common tonics: D, E, C#, F# (they put the ♭2 and the flute in a sweet register). The 808 likes
tonics between C#1 and F#1 (MIDI 25–30).

## 3. Harmony: a pedal, not a progression
The colour lives in the **tonic and the ♭2**. Most bars sit on the tonic; chords are moments.
- **Pedal**: 808 and a low drone/pad on the tonic most of the time.
- **Moves that keep the mode** (Hijaz on D: D Eb F# G A Bb C):
  - I – ♭II – I (D – Eb – D): the signature tension; ♭II for 1–2 beats or one bar out of four
  - iv – I (Gm – D): sad pull home
  - ♭vii – I (Cm – D): darker approach
  - in harmonic minor: i – ♭VI – V – i (Gm – Eb – D – Gm), with V major (the 3rd of V is the
    leading tone)
- **Avoid**: I–V–vi–IV-style changes, ii–V jazz moves, major IV in Hijaz (it is minor iv).
- 4- or 8-bar loop. Change the colour by orchestration (add/remove layers), not by changing
  chords every bar.
- Write chord/drone notes with `local_music_theory` `action: chords` (chord symbols) or
  `progression`, keeping the voicing low and sparse (root + 5th + the 3rd an octave up).

## 4. The hook: gestures that make it sound right
Use `chatmu-studio-hook-melody` for the motif, the repetition and the peak. In this genre add:
- **The augmented 2nd** (♭2 ↔ 3) as the hook's characteristic interval, in both directions.
- **Hover around the tonic**: 1 – ♭2 – 1 – 7(below, if double harmonic) – 1, then leap to 5.
- **Descending Hijaz tetrachord** at phrase ends: 4 – 3 – ♭2 – 1 (G – F# – Eb – D).
- **Hold the ♭2 and resolve down** to 1 on the strong beat — the genre's "sigh".
- Upper tetrachord (5 ♭6 7/♭7 1') for the peak; ♭6 → 5 is the second sigh.
- **Ornaments written as MIDI** (velocity lower than the main note):
  - grace note: a 32nd (0.125 beat) one step above, right before the main note
  - mordent: main – upper – main as three 32nds, then hold the main note
  - turn: upper – main – lower – main as 16th-triplets into a long note
  - trill on a long note: alternate main/upper in 32nds for the first half of the note
  - slide: no pitch bend available — a fast chromatic 32nd run of 2–3 notes into the target
  One ornament per phrase on the long notes; never on every note.
- **Monophonic** lead; for width double it an octave up on a second voice at −10 dB, never in
  thirds (thirds turn it Western).
- Register: flute/ney MIDI 72–96, oud/saz 55–79, strings 60–84 (or the `register_midi` of the
  preset you load).
- Leave the rap pockets empty: the hook plays the intro/chorus; in the verse only a 1-bar
  answer every 4 bars, or a filtered pad.

## 5. Drums: hip-hop body + darbuka layer
1. Base pattern: `local_music_theory` `action: drum_pattern` with the base genre (`trap`,
   `boombap`; for drill write it — snares on beat 3 of the half-time bar + syncopated kicks,
   sliding 808). Write it to a Drum Rack track (`chatmu-studio-drum-rack`).
2. Darbuka layer on its own track (load a darbuka/doumbek kit from the browser —
   `local_ableton_browser`, search `darbuka`, `doumbek`, `tabla`, `percussion`; if none, use a
   low tom for **dum** and a rim/high conga for **tek**). One bar of 4/4, beats from the bar
   start, D = dum (low, velocity 100–115), T = tek (high, velocity 70–95):
   | Rhythm | Pattern | Feel |
   |---|---|---|
   | **Maqsum** | D 0 · T 0.5 · T 1.5 · D 2 · T 3 | the default, versatile |
   | **Baladi** | D 0 · D 0.5 · T 1.5 · D 2 · T 3 | heavier, earthy |
   | **Saidi** | D 0 · T 0.5 · D 1.5 · D 2 · T 3 | bouncy, festive |
   | **Malfuf** | D 0 · T 0.75 · T 1.5 (2/4 cycle, repeat at 2) | fast, driving |
   Add tek fills in 16ths (velocity 45–65) in the last half-bar of every 4 bars. In trap at
   140 BPM the darbuka plays the **half-time** grid (one pattern per 2 beats feels too busy;
   one per bar fits).
3. The darbuka's dum must not fight the kick: move the dum off the kick's hits, or drop the dum
   and keep only teks on top of the hip-hop kick.

## 6. Sounds
- `local_synth_find_preset` first with the user's words (e.g. `query: "flute dark"`,
  `"strings"`, `"pluck"`, `"808"`). The library has no "Arabic" genre: you will get the nearest
  match with `fallback: true` — say so, then load it with `local_synth_set_preset`.
- For oud, ney, saz, darbuka, check the user's library with `local_ableton_browser`; load with
  `local_ableton_load_device` (one approval per load). If nothing fits, use a plucked synth for
  oud and a breathy flute preset for ney, and tell the user a recorded player would sound more
  real.
- 808: tuned to the tonic; glide (portamento) up to the 5th or down to ♭2 for movement.

## 7. Arrangement (16-bar loop as the seed)
| Section | Bars | What plays |
|---|---|---|
| Intro | 4–8 | hook alone or with drone + darbuka, filtered |
| Verse | 16 | drums + 808 + drone; hook answers once every 4 bars |
| Chorus / hook | 8 | everything; hook full register; strings double |
| Bridge | 4–8 | drop drums, ♭II moment, ornamented solo line |
Name scenes with `local_ableton_scene_name` (`Intro`, `Verse`, `Hook`…). For the full song
structure use `chatmu-studio-arrangement`.

## 8. Mix notes
- Flute/strings get space from a reverb send (not an insert); short pre-delay keeps them in
  front of the reverb.
- The ♭II chord over a sustained tonic 808 is a deliberate clash: keep it short, or move the
  808 to ♭2 for that bar.
- Darbuka panned slightly off-centre, teks brighter than dums; the rap stays centre and on top
  (`chatmu-mixing-progressive`).

## Workflow with the tools
1. `local_ableton_snapshot` → what exists; `local_ableton_set_tempo` from the brief.
2. Tracks (`local_ableton_edit_track` `create_midi`): Drums, Darbuka, 808, Drone, Hook.
3. Drums → darbuka → 808 → drone (clips with `local_ableton_create_clip`, notes with
   `local_ableton_write_notes`), firing after each layer (`local_ableton_fire`) so the user
   hears the build and can stop you.
4. Hook last, over the groove. Verify the bars' harmony with `local_harmony_map` if chords were
   added.
5. Tell the user what you made and what you'd do next (arrangement, vocal, mix).

## Hard rules
- Say the scale, the tonic and that it is 12-TET.
- Never use Western functional changes that erase the mode (I–V–vi–IV, ii–V–I).
- Never ornament every note; one ornament per phrase on long notes.
- No thirds harmony on the lead; unison or octaves only.
- Do not fill the verse with the hook; the rapper needs the space.
- Respect the source culture: no caricature runs, no fake "Arabic" vocal samples; suggest a
  real player when the part is exposed.

## Tell the user (short)
`Trap with Arabic colour · 140 BPM · D Hijaz (phrygian dominant, 12-TET) · pedal on D, Eb for
one bar in four · maqsum darbuka over a trap kit · flute hook: 1–♭2–1 hover, leap to 5, falls
down the Hijaz tetrachord with a mordent on the long G. Tracks: Drums, Darbuka, 808, Drone, Hook.`
