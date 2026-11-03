---
name: chatmu-studio-genre-dnb-garage
description: >
  Produces breakbeat-based UK bass music in the user's Ableton Live set: drum &
  bass (liquid, rollers, neuro), jungle, UK garage / 2-step and dubstep basics:
  right tempo, two-step and half-time grids, ghost snares and chopped breaks,
  swung garage shuffle, sub and reese bass, 8/16-bar switch-ups and club mix
  targets. Trigger phrases: "drum and bass", "dnb", "d&b", "jungle", "liquid
  dnb", "neurofunk", "UK garage", "2-step", "two step", "speed garage",
  "dubstep", "breakbeat", "amen break", "hazme un drum and bass", "beat de
  dnb", "garage inglés", "algo tipo jungle", "dubstep con wobble", "breaks".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "DnB, jungle, UK garage/2-step, dubstep: two-step & half-time grids, ghost snares, sub/reese, switch-ups"
version: "1.0"
tags: [studio, ableton, genre, drum-and-bass, dnb, jungle, uk-garage, 2-step, dubstep, breakbeat]
requiresTools:
  - local_studio_genre_starter
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
  - local_synth_modulate
  - local_ableton_browser
  - local_ableton_load_device
  - local_ears_track_levels
  - local_ears_listen
---

# Chatmu Studio — Drum & bass, jungle, UK garage, dubstep

These genres share a UK sound-system lineage: **broken drums over a heavy sub**, the snare
not on a four-on-the-floor kick. They are NOT fast house. DnB is two-step at 170–176: snare on
2 and 4, kick syncopated, ghost snares carrying the roll. Dubstep is half-time at 140: snare
on 3. Garage is 2-step at 130–136 with heavy swing. Tempo first: DnB at 140 is not DnB, and a
dubstep snare on 2 and 4 is not dubstep.

Related: `chatmu-studio-breakbeats` (the 13-element break method), `chatmu-studio-drum-rack`,
`chatmu-studio-sampling` (chopping breaks), `chatmu-studio-bass-lines`,
`chatmu-studio-sound-design` (reese, wobble), `chatmu-studio-sidechain`, `chatmu-studio-humanize`,
`chatmu-mixing-progressive`. Four-on-the-floor: `chatmu-studio-genre-house-techno`.

## 1. Brief (ask only what is missing; propose defaults)
| Style | BPM (default) | Feel | Signature |
|---|---|---|---|
| **Liquid DnB** | 172–176 (174) | two-step, smooth | Rhodes/pads, soulful vocal, round sub |
| **Rollers / dancefloor DnB** | 172–176 (174) | two-step, driving | rolling reese, minimal hook |
| **Neurofunk** | 172–176 (174) | tight, aggressive | modulated reese, precise edits |
| **Jungle** | 160–170 (165) | chopped breaks, ragga | amen edits, deep sine sub, dub FX |
| **UK garage / 2-step** | 130–136 (132) | swing 58–66% | skippy kick, chopped R&B vocals, organ/bass stabs |
| **Dubstep** | 138–142 (140) | half-time | snare on 3, sub + wobble, space |
Range for DnB overall: 165–185 (172/174 most common). Also ask: key/mood (default F minor or
A minor), vocal or instrumental, liquid vs dark.

## 2. Groove grids (1 bar, 16 steps; step 1 = beat 0, step 5 = beat 1, step 9 = beat 2)
Drum Rack: 36 kick, 38 snare, 37 rim, 39 clap, 42 closed hat, 46 open hat, 70 shaker.
```
DRUM & BASS — two-step, 174 BPM (full-time backbeat, NOT half-time)
Kick   X . . . . . . . . . X . . . . .   steps 1 11  (beats 0, 2.5)
Snare  . . . . X . . . . . . . X . . .   steps 5 13  (beats 1, 3) vel 100–115
Ghost  . . . . . . . X . . . . . . X .   steps 8 15  vel 25–45 (more on 4, 12, 16 for rollers)
Hat    8ths or 16ths vel 50–80, shaker/ride 16ths vel 30–55
```
- Variations: kick on 1 and 11 + extra on 7 or 8 in bar 2 of each 2-bar phrase; ghost snares
  move bar to bar. Ghost snares matter more than the main snare: they are the roll.
- Half-time DnB variant (intro/halftime switch): snare only on step 9.
- `local_music_theory` `action: drum_pattern` `genre: dnb` for a base, then edit to the grid.
```
JUNGLE — 160–170 BPM, chopped break
Break slices on a Drum Rack / Simpler: kick (K), snare (S), hat/ride (H) per 16th.
Amen-style bar: K . K . S . . S . S K . S . . S  (rearrange every 2–4 bars)
Ghosts vel 20–40, main snare 90–110; reverse/pitched snare at bar 4 or 8; sine sub on top.
```
```
UK GARAGE / 2-STEP — 132 BPM, swing 58–66% on all 16ths
Kick   X . . . . . . . . . X . . . . .   steps 1 11 (no four-on-the-floor; skips into 3)
Snare  . . . . X . . . . . . . X . . .   steps 5 13 (clap/rim layer)
Hat    off-beats (3 7 11 15) + 16th shuffle vel 40–80, shaker swung
Extra kick on step 14 or 16 every other bar = the "skip". Speed garage: 4/4 kick instead.
```
```
DUBSTEP — 140 BPM, half-time
Kick   X . . . . . . . . . . . . . . .   step 1 (+ syncopated extras on 11 or 15)
Snare  . . . . . . . . X . . . . . . .   step 9 (beat 2 = "3" of the half-time bar) vel 110–120
Hat    sparse 8ths vel 50–70, 16th/triplet details at phrase ends
```
Swing: DnB/jungle straight to 52%; garage 58–66%; dubstep straight with triplet hat details.

## 3. Building a break (from `chatmu-studio-breakbeats`)
Framework (kick 1/3, snare 2/4 at the genre's grid) → steady 16th hat (element 8) → kick
doubles (4) → ghost snares on the "e"/"a" (1) → snare accents off 2/4 (6) → open hat sparingly
(5, too much = disco) → hat mix of 8ths/16ths/rests (9) → triplets (11) or 3-over-2 (13) only
for fills. One element per pass; fire after each (`local_ableton_fire`); remove the last one
if it stops nodding. Ghosts 20–40, main snare 90–110, hats below the snare. Humanize ghosts
±5–15 ms after the grid works; never hard-quantize them. Layer a programmed kick/snare under a
chopped break for weight (unison, element 12).

## 4. Harmony
- Liquid: minor 7/9 chords, Dorian, i9–♭VImaj7–♭VII–iv7 over 2 bars each, or ii–V-ish soul
  moves (allowed here); preset `rnb` or `jazz` slowed. Voicings MIDI 55–76.
- Rollers/neuro/dubstep: one root for 8–16 bars, harmony implied by bass; Phrygian ♭2 for
  menace (i–♭II), or i–♭VI. Pads optional.
- Jungle: dub minor, 1–2 chords, stabs or pads drenched in delay.
- Garage: minor 7/9 organ or piano stabs, i7–iv7 or ♭VImaj7–♭VII–i; preset `rnb`.
- Avoid: bright major pop progressions in dark styles, chords below MIDI 48, changing chords
  every bar under a moving reese.

## 5. Hooks
Building on `chatmu-studio-hook-melody`:
- DnB hook = **a bass riff or a vocal phrase**, 2 bars, call/answer; melodic lead is rare in
  rollers. Liquid: a 4–8 note vocal/keys motif, long notes over the fast drums (the half-speed
  melody against 174 BPM drums is the genre's emotion).
- Garage: chopped vocal hook, syncopated one-shots on steps 4, 7, 11, 14, pitched to the chord
  (`chatmu-studio-vocal-chops`); organ-bass stab riffs.
- Dubstep: the drop hook is the bass phrase — 1–2 bars of wobble rhythm (8th/16th/triplet rate
  changes) answered by silence; the "melody" is in the build/intro.
- Jungle: ragga vocal stabs or dub sirens, rare and treated with delay.

## 6. Bass
- **Sub** (all styles): sine/triangle 30–60 Hz fundamental, MIDI 24–40 (C0–E1 in Live's naming), mono.
  DnB sub notes long (1–4 beats), entering on the kick or just after; leave the snare hit clear.
- **Reese** (DnB/neuro): two detuned saws (±10–20 cents) low-passed, slow movement; split
  into sub (below 100–120 Hz, mono) and mids (120 Hz–4 kHz, distorted, can be wide).
  `local_synth_modulate`: LFO 0.1–0.5 Hz on cutoff or detune.
- **Wobble** (dubstep): LFO on filter cutoff synced 1/4, 1/8, 1/8T, 1/16 — change rate every
  half-bar to write the rhythm; sub layer underneath untouched.
- **Garage**: short organ/sub bass in the kick's gaps (starts 0.75, 1.5, 2.75, 3.5), 0.25–0.5
  beat, octave jumps, swung with the drums.
- **Jungle**: deep sine sub following the root, long slides faked as 2–3 32nd chromatic notes
  (no pitch bend); glide via the synth's portamento if available.
- Sidechain sub to kick lightly (4:1–10:1, 0.1 ms attack, 50–100 ms release, 2–5 dB) only if
  they overlap; better: don't overlap them.

## 7. Sounds
- `local_synth_find_preset`: `"bass dark"`, `"reese"`, `"bass short"`, `"keys warm"`,
  `"strings"`, `"vocal"`, `"synth dark"`, `"808"` for garage/dubstep subs. Genres missing from
  the factory return `fallback: true` — say so. Load with `local_synth_set_preset`.
- Browser (`local_ableton_browser` → `local_ableton_load_device`): `break`, `amen`, `think`,
  `jungle`, `breakbeat`, `garage`, `dnb kit`, `ride`, `organ`, `vocal`; devices `Simpler` (slice
  the break), `Drum Buss`, `Saturator`, `Auto Filter`, `Echo`, `Reverb`.
- Snare: bright, 200 Hz body + 3–5 kHz crack; DnB snare is the loudest drum.

## 8. Arrangement (8/16-bar phrases; seconds per bar = 240 / BPM, 174 → 1.38 s)
| Section | DnB / jungle | Garage | Dubstep |
|---|---|---|---|
| Intro (DJ) | 16–32: drums light, pads, filtered | 16: drums + stabs | 16: atmos, half-time perc |
| Build | 8–16: snare roll / riser, filter | 8 | 8: rising, vocal tag |
| Drop 1 | 32: full drums + bass | Verse/groove 16 | 16 |
| Breakdown | 16–32: no drums, melody/vocal | 8 | 8–16 |
| Drop 2 | 32: **switch-up** (new bass, new break edit) | Hook 16 | 16: new wobble pattern |
| Outro (DJ) | 16–32 | 16 | 8–16 |
- Switch-ups every 8 bars: change a ghost pattern, swap the break chop, mute drums for 1 beat,
  bass variation at bar 8 and 16. A pre-drop 1-beat silence then impact on drop bar 1.
- Drops: contrast is the build losing kick + sub in the last 1–2 bars; the drop returns all low end.
- Name scenes with `local_ableton_scene_name` (`Intro`, `Build`, `Drop`, `Break`, `Drop 2`, `Outro`).

## 9. Mix targets
- Relative (snare = 0): kick −1 to −2, sub −1 to −3 (felt more than heard), reese mids −4,
  hats/ride −10 to −14, pads −10, vocal −2 to −4. Dubstep: sub and snare equal anchors.
- Low end: sub owns 30–80 Hz mono; kick punch 60–100 Hz (DnB kicks are short, no long tail);
  high-pass everything else at 100–150 Hz. Breaks high-passed ~ 80–120 Hz when a programmed kick
  carries the low end.
- Space: drums dry-ish with a short room; pads/vocals in a long reverb + dub delay (jungle).
- Loudness: DnB/dubstep club masters **−7 to −5 LUFS**, garage −9 to −7, liquid −9 to −7;
  true peak ≤ −1 dBTP. Keep snare transient.
- Check `local_ears_track_levels` (sub vs kick, reese vs snare masking) and `local_ears_listen`
  (drop denser than build, ghosts clearly lower than main hits).

## What ruins it
- Wrong tempo (DnB at 140, garage at 124 straight); dubstep snare on 2 and 4.
- DnB with a four-on-the-floor kick; garage with no swing.
- No ghost snares, or ghosts quantized flat at velocity 100.
- Overused open hats (disco), triplets or 3-over-2 every bar.
- Sub and kick on top of each other; wide sub; reese mids masking the snare.
- 2 bars looped for 3 minutes with no switch-ups.

## Workflow with the tools
**Start with `local_studio_genre_starter` (`genre: dnb`) when you have it.** In one approval it
adds Drums, Bass and Chords at the end of the set with this genre's real groove, bass rhythm and
progression, voiced with Chatmu Synth's presets of the genre. Pass the user's `bpm` / `key`.
Don't rewrite its drum grid: build on top of it (perc layer, riff/hook, arrangement, variations)
with the steps below from the riff/perc step on. If the tool is missing (older Desktop), follow
the steps below from the start.

1. `local_ableton_snapshot`; `local_ableton_set_tempo` (§1).
2. Tracks (`local_ableton_edit_track` `create_midi`): Drums (or Break + Drums), Sub, Bass
   mids/Reese, Keys/Pad, Vox/FX.
3. Drums by the §3 build order, firing after each element; humanize ghosts.
4. Sub, then reese/wobble mids; fire. Chords/hook last.
5. Arrange 8/16-bar scenes with switch-ups; `local_ears_track_levels` + `local_ears_listen`.

## Hard rules
- Tempo inside the style's range before programming anything.
- DnB = two-step (snare 5/13 + ghosts), dubstep = snare on 9 (half-time), garage = swung 2-step.
- Ghost snares 20–40 velocity; main snare 90–110.
- Sub mono below ~100 Hz; kick and sub don't overlap.
- One polyrhythm at a time; triplets/3-over-2 only as fills.
- Say style, BPM, grid, bass type and structure.

## Tell the user (short)
`Liquid DnB · 174 BPM · F minor · Fm9 → D♭maj7 → E♭ → B♭m7 (2 bars each) · kick 1/11, snare
5/13, ghosts on 8/15 at vel 35, ride 16ths · sine sub F0/D♭1 long notes + warm Rhodes ·
16-bar intro, drop at 17, switch-up at 49. Next: vocal chop hook or a reese for drop 2?`
