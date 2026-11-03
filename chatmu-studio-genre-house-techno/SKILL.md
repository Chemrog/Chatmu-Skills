---
name: chatmu-studio-genre-house-techno
description: >
  Produces four-on-the-floor club music in the user's Ableton Live set: house,
  deep house, tech house, techno, melodic techno (and trance as a neighbour):
  right BPM, kick / clap / hat grid, offbeat bass, stabs or one-chord vamps,
  sidechain pump values, DJ-friendly 8/16/32-bar arrangement, subtle builds
  and drops, and club mix targets. Trigger phrases: "house", "deep house",
  "tech house", "techno", "melodic techno", "trance", "four on the floor",
  "club track", "club beat", "rave", "hazme un house", "beat de techno",
  "algo para la pista", "tech house para DJ", "música de club", "cuatro por
  cuatro", "techno melódico", "deep house relajado".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "House, deep/tech house, techno, melodic techno: 4/4 grids, offbeat bass, pump, DJ-friendly arrangement"
version: "1.0"
tags: [studio, ableton, genre, house, deep-house, tech-house, techno, melodic-techno, trance, club]
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
  - local_ableton_browser
  - local_ableton_load_device
  - local_ableton_device_routing
  - local_ableton_set_device_param
  - local_ears_track_levels
  - local_ears_listen
---

# Chatmu Studio — House & techno

Four-on-the-floor is a **family, not a genre**: house, tech house, techno and trance share the
kick and differ in tempo, hats, bass and structure. The music is made for DJs and bodies:
the groove must work with no melody, energy is managed by what enters and leaves every
8/16/32 bars, and repetition is a feature — but repetition with micro-variation, or it sounds
like a loop from a machine. Tempo first: the same pattern at the wrong BPM is a different
genre.

Related: `chatmu-studio-drum-rack`, `chatmu-studio-sidechain` (routing + Ears proof),
`chatmu-studio-bass-lines`, `chatmu-studio-synth`, `chatmu-studio-arrangement`,
`chatmu-studio-humanize`, `chatmu-mixing-progressive`. Breakbeat genres: `chatmu-studio-genre-dnb-garage`.

## 1. Brief (ask only what is missing; propose defaults)
| Style | BPM (default) | Feel | Signature |
|---|---|---|---|
| **House** | 118–128 (124) | light swing | offbeat open hat, piano/organ chords |
| **Deep house** | 118–124 (122) | swing 54–58% | minor 7/9 chords, warm stabs, rolling bass |
| **Tech house** | 124–128 (126) | groovy, percussive | short bass riff, vocal one-shots, dry |
| **Techno** | 128–140 (132; hard 140–150) | straight, hypnotic | rumble/rolling bass, 16th hats, no song form |
| **Melodic techno** | 120–126 (124) | straight, dark-emotive | minor arps, big pad, long builds |
| **Trance** | 134–140 (138) | straight | offbeat bass/hat, 32-bar build & reprise |
Also ask: key/mood (default minor: A, F, G or D minor), vocal yes/no, DJ edit (long intro/outro) or radio edit.

## 2. Groove grid (1 bar, 16 steps; step 1 = beat 0, step 5 = beat 1)
Drum Rack: 36 kick, 39 clap, 38 snare, 37 rim, 42 closed hat, 46 open hat, 70 shaker.
| Element | House / deep | Tech house | Techno | Trance |
|---|---|---|---|---|
| Kick (36) | 1 5 9 13, vel 110–120 | same | same | same |
| Clap/snare | 5 13 (vel 95–110) | 5 13 + clap layer | 5 13 sparse, or none | 5 13 |
| Open hat (46) | **3 7 11 15**, vel 85–100 | 3 7 11 15 short | often omitted / ride | 3 7 11 15 |
| Closed hat (42) | 16ths vel 45–75 | 16ths, accents on 3 7 11 15 | 16ths vel 60–95 | 16ths soft |
| Shaker (70) | 16ths vel 35–60, swung | 16ths | — | — |
| Perc | conga/rim on 4, 8, 14 | rim 4 7 12 / tom fills | ride on offbeats, 3/16 perc | — |
- Beats: kick 0,1,2,3; clap 1,3; open hat 0.5,1.5,2.5,3.5.
- The **offbeat open hat is the house signature**: remove it and it stops being house. In
  techno it often goes, replaced by a ride or 16th hats — that keeps it hypnotic.
- Swing: house/deep 54–58% on hats/shaker only; **the kick stays on the grid** in every style.
- Base pattern: `local_music_theory` `action: drum_pattern` `genre: house` or `techno`, then
  edit to the table. Velocity on 16th hats: accent pattern high-low-mid-low (e.g. 75 45 60 45).
- Micro-variation: every 4th bar change one hat or add a perc hit; every 8th bar a clap
  flam or open-hat choke; every 16 bars a 1-beat fill (tom/perc), never a snare roll.
- One polyrhythm at a time (e.g. a 3/16 perc loop over 4/4). Stacking 3:2 and 4:3 confuses.

## 3. Harmony
- **Deep house**: minor 7/9/11 chords. i7–iv7 (2 bars each), one-chord i9 vamp,
  i7–♭VII–♭VImaj7–♭VII. Preset `deep_house` from `local_music_theory` `action: progression`.
  Voicing: rootless or root + 7 + 3 + 9 around MIDI 55–72 (C3 = 60), no low root (the bass has it).
- **House**: piano/organ 7ths, Dorian or major; i–IV (Dorian), vi–IV–I–V style allowed in
  vocal house; preset `house`.
- **Tech house**: one chord or none — a stab on 1–2 notes, harmony implied by the bass.
- **Techno**: no progression. One note/drone or a 1–2 chord vamp over 16–32 bars; change
  energy, not chords. Changing chords every bar kills the hypnosis.
- **Melodic techno**: minor (Aeolian/Phrygian), i–♭VI–♭III–♭VII or i–♭VI over 4–8 bars per
  chord; preset `edm` slowed down. Avoid major-key cheese and V7.
- **Trance**: minor, i–♭VI–♭III–♭VII, 2 bars per chord, preset `edm`; breakdown may lift to
  the relative major.
- Avoid in all: ii–V–I jazz motion (except jazzy deep house stabs), dense voicings below MIDI 48.

## 4. Hooks: riffs, stabs and vocals
Building on `chatmu-studio-hook-melody`, the club hook is **rhythmic first**:
- **Stab hook** (house/deep): a chord stab on the offbeats or a syncopated pattern
  (steps 3, 6, 11 or 4, 7, 12, 15), duration 0.25–0.5 beat, vel 85–105. Repeat for 8+ bars;
  vary by filter, not notes.
- **Riff hook** (tech house/techno): 1–2 bars, 2–4 pitches within a 5th, 16th-based, the same
  rhythm repeated, one note changing every 4 bars. Call (bar 1) / answer (bar 2).
- **Arp hook** (melodic techno/trance): 16th arp over the chord tones, 1–2 octaves,
  `local_music_theory` gives chord pitches; the hook is the filter/resonance movement.
- **Vocal hook**: one short phrase (2–6 words) or a chopped one-shot every 2–4 bars; use
  `chatmu-studio-vocal-chops`.
- Register: stabs MIDI 55–76, leads/arps 64–88. Velocity varies ±8 to feel played.

## 5. Bass
- Lives **in the kick's holes**: the bass follows the gaps, not the kick. Sidechain if it fights.
- **House / deep**: offbeat (starts 0.5, 1.5, 2.5, 3.5), 0.25–0.5 beat long, root + octave +
  7th, or rolling 8ths; MIDI 31–48 (G1–C3).
- **Tech house**: short syncopated riff — e.g. starts 0.5, 0.75, 1.5, 2.25, 2.5, 3.5, durations
  0.125–0.25, vel 90–120, one or two pitches plus an octave jump.
- **Techno**: rolling 16ths off the kick (steps 2 3 4, 6 7 8…) or a "rumble" (the kick sent to a
  long reverb, low-passed at 150–200 Hz, sidechained hard to the kick).
- **Trance**: rolling offbeat 16ths (steps 2 3 4 per beat) on the root, the "galloping" bass.
- Sub fundamental 40–70 Hz; the kick owns 50–60 Hz punch, bass sits around it (tune kick to key).

## 6. Sounds
- `local_synth_find_preset` with genre words: `"house bass"`, `"deep house keys"`,
  `"techno synth dark"`, `"bass short"`, `"strings"`, `"vocal"`, `"bell"`. If the genre isn't
  in the factory you get `fallback: true` — say so. Characters: Warm for deep house keys/pads,
  Dark for techno, Short for stabs and bass. Load with `local_synth_set_preset`.
- Browser (`local_ableton_browser` → `local_ableton_load_device`): kits `909`, `808`, `house`,
  `techno`; one-shots `clap`, `ride`, `organ`, `stab`, `chord`; devices `Auto Filter`, `Echo`,
  `Reverb`, `Saturator`, `Compressor`, `Glue Compressor`. Classic palette: 909 kick/clap/hats,
  M1-style organ/piano for house, Rhodes/Wurli for deep, distorted hats and rumble for techno.
- FX: Auto Filter sweeps on stabs/pads, Echo/Delay on stabs (3/16 or 1/8 dotted), one reverb
  return, Saturator on bass for midrange audibility on small speakers.

## 7. Sidechain values (route with `local_ableton_device_routing`, see `chatmu-studio-sidechain`)
One beat = 60000 / BPM ms (124 BPM → 484 ms). Release so the level returns just before the next kick.
| Style / target | Ratio | Attack | Release | GR on hits |
|---|---|---|---|---|
| House / deep (pads, chords) | 4:1 – inf:1 | 0.1–1 ms | 30–45% of a beat | 4–8 dB |
| Big pump as effect (EDM-leaning) | inf:1 | 0.1 ms | ~50% of a beat (≈1/8) | 8–15 dB |
| Techno (bass, rumble) | 4:1 – 10:1 | 0.1–1 ms | 80–150 ms | 2–5 dB (rumble more) |
Ghost kick: a muted kick track (fader −inf) playing every beat as trigger through breakdowns
(tap Post FX). Prove the pump with `local_ears_listen` A/B (ON vs OFF): dips on every beat.

## 8. Arrangement (DJ-friendly phrases of 8/16/32 bars)
Seconds per bar = 240 / BPM (124 → 1.94 s; 6 min ≈ 186 bars).
| Section | Deep / house | Techno | Melodic techno / trance |
|---|---|---|---|
| Intro (DJ) | 16–32: kick + hats, bass at 17 | 32: kick, hats, perc | 16–32 |
| Groove / main | 16 + 32 | 64 linear, add/remove 1 layer per 16 | 32 |
| Breakdown | 16: no kick, chords/vocal | 16–32: texture, filter | 32: pad + arp, emotional |
| Build | 8–16 | 8 (filter + perc) | 16: roll, riser |
| Drop / main 2 | 32 | 64 | 32, reprise of the hook |
| Outro (DJ) | 16–32: strip to drums | 32 | 16–32 |
- **Build** (last 8–16 bars before a drop): filter closing/opening, percussion density up,
  noise riser; house/techno builds are subtle — rarely a full stop; trance/EDM go bigger
  (snare 4ths → 8ths → 16ths → 32nds, vel 60 → 120). The last 1–2 bars lose kick and bass.
- **Drop bar 1**: kick + bass + full chords together, impact (crash + sub boom) optional.
  Contrast > loudness: the drop has more low end and density, ≥ 2–3 LU above the build end.
- Techno: structure is energy management, not song form. Keep 1 element entering or leaving
  every 16 bars. Name scenes with `local_ableton_scene_name` (`Intro`, `Groove`, `Break`, `Build`, `Drop`, `Outro`).

## 9. Mix targets
- Kick is the loudest element (reference 0 dB); bass −2 to −4; clap −4; hats −10 to −14;
  stabs/pads −8 (ducked); vocal −3 to −5.
- Low end: everything but kick and bass high-passed at 120–200 Hz. Kick and bass mono below
  120 Hz. Kick punch 50–60 Hz, click 2–5 kHz; bass 40–70 Hz sub + 100–300 Hz body (cut 250 Hz on pads).
- Space: drums mostly dry; short room on clap (0.8–1.2 s); long reverb only on breakdown
  pads/vocals; delay throws at phrase ends.
- Loudness: club master **−9 to −6 LUFS** integrated (techno −7 to −6, deep house −10 to
  −8), true peak ≤ −1 dBTP, kick transient preserved (no smashed limiter).
- Check with `local_ears_track_levels` (kick vs bass masking) and `local_ears_listen` (drop
  denser/louder than build). Dance test: it must work with drums + bass only.

## What ruins it
- Wrong BPM for the style; swung kick; snare rolls in deep house/techno.
- Removing the offbeat open hat in house; adding it to hypnotic techno.
- Bass on top of the kick instead of in its holes; no sidechain on full pads.
- Chords changing every bar in techno; pop song form in a DJ tool.
- Every element playing every 16th; no build/drop contrast; build louder than the drop.
- 8 bars copied 24 times with zero variation — the machine-loop tell.

## Workflow with the tools
**Start with `local_studio_genre_starter` (`genre: house` or `techno`) when you have it.** In one approval it
adds Drums, Bass and Chords at the end of the set with this genre's real groove, bass rhythm and
progression, voiced with Chatmu Synth's presets of the genre. Pass the user's `bpm` / `key`.
Don't rewrite its drum grid: build on top of it (perc layer, riff/hook, arrangement, variations)
with the steps below from the riff/perc step on. If the tool is missing (older Desktop), follow
the steps below from the start.

1. `local_ableton_snapshot`; `local_ableton_set_tempo` from §1.
2. Tracks (`local_ableton_edit_track` `create_midi`): Drums, Bass, Chords/Stab, Lead/Arp, Perc.
3. Drums (§2) → fire (`local_ableton_fire`) → bass (§5) → fire → chords/stab (§3–4) → fire.
   Clips via `local_ableton_create_clip`, notes via `local_ableton_write_notes`, humanize hats
   and stabs (`local_music_theory` `action: humanize`), kick untouched.
4. Sidechain pads/bass to the kick (§7) and verify by listening.
5. Arrange in 8/16/32-bar scenes (§8), then `local_ears_track_levels` + `local_ears_listen`.

## Hard rules
- One style at a time; BPM inside its range; kick on 1 5 9 13 on the grid.
- House keeps the offbeat open hat (steps 3 7 11 15).
- Bass in the kick's gaps; sidechain or EQ when they fight.
- Phrases in multiples of 8 bars; something changes every 8–16 bars.
- Drop beats build in low end and density; last build bars lose kick + bass.
- Say style, BPM, key, grid, bass placement and structure.

## Tell the user (short)
`Deep house · 122 BPM · A minor · Am9 → Dm9 (2 bars each) · 909 kick 1-5-9-13, clap 5/13,
open hat on the &, shaker swung 56% · offbeat bass A1/A2/G2 · warm keys stab on steps 4/7/12
sidechained (inf:1, 0.5 ms, 180 ms, ~6 dB) · DJ intro 32 bars. Next: breakdown with vocal chop?`
