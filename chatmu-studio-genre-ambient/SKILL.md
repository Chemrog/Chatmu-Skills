---
name: chatmu-studio-genre-ambient
description: >
  Produces ambient, calm / chill, lo-fi chill backgrounds and meditation music
  in the user's Ableton Live set: static or slow-moving harmony, long evolving
  pads and drones, textures instead of beats, no hard transients, long
  reverbs, and movement that comes from automation and slow modulation rather
  than from new notes. Trigger phrases: "ambient", "ambient track", "calm
  music", "chill background", "meditation music", "relaxing", "drone",
  "soundscape", "sleep music", "study background", "música ambiental",
  "música relajante", "música para meditar", "fondo tranquilo", "algo calmado",
  "paisaje sonoro", "música para dormir", "ambient chill".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Ambient / calm / meditation: static harmony, evolving pads, no hard transients, movement by automation"
version: "1.0"
tags: [studio, ableton, genre, ambient, chill, meditation, drone, soundscape, calm, texture]
requiresTools:
  - local_synth_status
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
  - local_ableton_set_device_param
  - local_ears_track_levels
  - local_ears_listen
---

# Chatmu Studio — Ambient, calm and meditation

Ambient is the genre where **time is the instrument**. Nothing announces itself: notes fade in,
overlap and leave; the listener should be able to ignore it or dive into it. The harmony
barely moves, the sound moves a lot — filter, reverb size, density and stereo width drift
over minutes. Three things kill it: hard transients (a click, a sharp pluck, a snare), chord
changes on a pop clock (every bar), and a static loop with nothing evolving (that sounds like
a preset demo, i.e. "AI-made").

Related: `chatmu-studio-harmony` (voicings), `chatmu-studio-sound-design` and
`chatmu-studio-synth` (pads/drones), `chatmu-studio-spatial-panning`, `chatmu-mix-effects`
(reverb/delay), `chatmu-studio-humanize`, `chatmu-studio-arrangement`. Lo-fi hip hop with
drums in front: `chatmu-studio-genre-hiphop` (planned); this skill covers the beatless or
nearly beatless end.

## 1. Brief (ask only what is missing; propose defaults)
| Decision | Options | Default |
|---|---|---|
| Use | listening · study/work background · meditation/sleep · video bed | background |
| Pulse | none (free) · implied (slow pulse 60–80) · soft beat (lo-fi chill 70–85) | implied 70 |
| Mood | warm/hopeful · melancholic · dark/vast · neutral/floating | warm |
| Length | 2–4 min (video) · 6–10 min (listening) · 20+ min (sleep, loopable) | 4 min |
| Palette | synth pads · piano + texture · strings/choir · field recordings · guitar drones | pads + piano |

Meditation/sleep: no pulse, no melody hooks, no surprises, slow everything (see §9).

## 2. Tempo and time
- Ambient still needs a BPM so clips line up: **60–80 BPM** (70 default). Free-time pieces:
  set 60 and write in whole bars; the grid is only for placement.
- Think in **long durations**: pad notes 4–16 bars (16–64 beats), drones the whole section.
  Melody notes ≥ 1 beat, often 2–6 beats.
- Lo-fi chill backgrounds: 70–85 BPM, swing 55–60% on hats, everything softened (§5).
- Chill-out (downtempo, 80–126 BPM): sparse kick or kick on 1 and 3, soft clap/snare on 2 and 4,
  soft hats, long simple bass (root, 1–2 bars per note); same no-transient rules apply.
- Phrase lengths: 8, 16 or 32 bars, and **overlap** sections by 2–4 bars instead of cutting.

## 3. Harmony: static, modal, slow
- **Pedal / drone** on the tonic (or tonic + 5th) under most of the piece. Root C2–G2 (MIDI
  36–43); never below MIDI 33 — sub energy makes it tiring and eats headroom.
- **Harmonic rhythm**: one chord every 4–8 bars (at 70 BPM that is 14–27 s). Meditation: one
  chord per 16 bars or a single chord for the whole piece.
- Modes that float: **Lydian** (bright, #4), **Dorian** (warm minor, natural 6), **Mixolydian**,
  **Aeolian**; major/minor **pentatonic** for melodies that cannot clash.
- Moves that stay calm (in C): I – IV/I (C – F over C), Imaj7 – IVmaj7 (Cmaj7 – Fmaj7),
  i – ♭VI (Am – F), I – II in Lydian (C – D over C), i9 – iv9 (Dorian), sus2 ↔ add9 swaps.
  Change one or two voices at a time (common-tone voice leading); the rest hold.
- Colour tones: add9, maj7, 6/9, sus2, sus4, 11 on minor. Open voicings: root + 5th low,
  3rd/7th/9th spread over 1.5–2 octaves above (C2 G2 | E3 B3 D4).
- **Avoid**: V7 → I cadences, ii–V–I, dominant 7ths, diminished passing chords, four chords
  in four bars, close-voiced triads in the low register (mud below 250 Hz).
- `local_music_theory` `action: scale` for the mode; `action: chords` with symbols
  (`Cmaj9`, `Fmaj7/C`, `Dsus2`) to get pitches, then spread the voicing by octaves yourself.
  Presets `cinematic` or `lofi` from `action: progression` are a start — slow them to 4–8 bars
  per chord and drop any V7.

## 4. Melody: fragments, not hooks
Ambient does not use the `chatmu-studio-hook-melody` hook (short, repeated, punchy). Instead:
- **Motif of 2–4 notes**, pentatonic or the mode's stable tones, played rarely: once every 4–8
  bars, with long silences (≥ 50% of the time silent).
- Slow intervals: steps and 4ths/5ths; avoid fast runs and repeated-note rhythms.
- **Phase it**: repeat the motif in a clip whose length is not a multiple of the pad clip (e.g.
  motif clip 7 bars, pad 8 bars, texture 5 bars). The combination keeps changing for 280 bars.
- Piano/keys: velocity 35–70, notes 2–6 beats, sustain via long durations; register MIDI
  60–84. A low octave answer (MIDI 48–60) every 16 bars adds depth.
- Bell/glass: MIDI 72–96, velocity 30–55, max one note per bar.
- Humanize every played part: start ±10–30 ms, velocity ±8 (`local_music_theory`
  `action: humanize`). Grid-perfect piano reads as machine.

## 5. Rhythm (only if the brief has a pulse)
- **Beatless default**: pulse comes from a slow arpeggio or a delay echo, not from drums.
  Soft arp: 8th notes at velocity 30–50, filtered (cutoff 1–3 kHz), synced delay 3/16.
- **Lo-fi chill background** (70–85 BPM): kick on 1 and the "and" of 2 (beats 0, 1.5) at
  velocity 70–85, soft rim/snare on beats 1 and 3 at 55–70, closed hat 8ths at 35–55 with
  swing 55–60%, shaker (70) 16ths at 25–40. `local_music_theory` `action: drum_pattern`
  `genre: lofi` then lower all velocities 15–20 and low-pass the drum bus at 6–9 kHz.
- No claps, no crash cymbals, no snare rolls, no risers with hard impacts.
- Percussion substitutes: brushed textures, rain, vinyl crackle, soft shakers, a heartbeat-
  like low tom at velocity 40 every 2 beats for meditation.

## 6. Sounds and texture
**Chatmu Sound first (house rule).** Every bass and melodic part (bass/808, keys, pads, plucks,
leads, brass, strings…) gets **Chatmu Sound with a factory preset of this genre**, not Live's
stock instruments (Operator, Grand Piano, Electric…), which sound like generic MIDI:
1. `local_synth_find_preset` with `genre: "Ambient"`, the `instrument` and a `character`. If it
   returns `fallback: true`, say it's the closest genre.
2. Load the plugin on the track: searching the browser by name does NOT find plugins, so use
   `local_ableton_browser` `path: "plugins"` (then its VST3 folder) to get Chatmu Sound's `uri`,
   and `local_ableton_load_device` with that `uri`.
3. Right after loading, `local_synth_set_preset { file }` (it goes to the newest instance), then
   `local_synth_status`: that track's instance must show the `preset_name`. An empty
   `preset_name` means no preset is loaded yet — never tweak or write on top of that.
Load every synth track first, then write notes. Live's instruments only when the library has
nothing for that part (say so). **Drums are not Chatmu Sound** (no noise source, no percussion
presets): use a Live Drum Rack / kit or samples; a Chatmu Sound 808 can sit under it as the low end.

Build 4–6 layers that each occupy a different band and move at a different speed:
| Layer | Range | Role | Movement |
|---|---|---|---|
| Drone/sub pad | 40–200 Hz | floor | filter drift 8–32 bars |
| Main pad | 200 Hz–4 kHz | harmony | cutoff + volume swells 4–8 bars |
| Keys / piano / guitar | 250 Hz–5 kHz | the human voice | sparse notes |
| Air / shimmer | 5–16 kHz | sparkle | slow tremolo / width |
| Texture / field recording | full, low level | place, noise bed | constant, −24 to −30 dB |

- `local_synth_find_preset` with words like `"pad warm"`, `"strings dark"`, `"keys warm"`,
  `"bell"`, `"vocal"`, `"synth dark"`. There is no "ambient" genre in the factory: expect
  `fallback: true`; pick Warm/Dark characters for pads, never Short. Load with
  `local_synth_set_preset`.
- Slow modulation with `local_synth_modulate`: LFO 0.02–0.1 Hz on cutoff (±15–25%), on pan
  (±20%) and on wavetable position; never faster than 0.25 Hz on a pad (it becomes a wobble).
- Attack ≥ 300 ms on pads (800–2000 ms typical), release 2–6 s. Keys: soften with a low-pass
  at 3–5 kHz and short attack ≥ 5 ms to remove the click.
- Browser (`local_ableton_browser`, then `local_ableton_load_device`): search `pad`, `drone`,
  `texture`, `ambience`, `field`, `rain`, `vinyl`, `piano`, `felt`, plus Ableton devices
  `Reverb`, `Hybrid Reverb`, `Echo`, `Auto Filter`, `Chorus-Ensemble`, `Grain Delay`.
- A short loop of a field recording (rain, room tone) at −28 dB glues layers and hides the
  digital silence between notes.

## 7. Movement = automation (the core of the genre)
Every 8–16 bars something must change, slowly. Pick 2–3 automations per section:
- Pad filter cutoff: 600 Hz → 2.5 kHz over 16 bars, back over 16.
- Reverb send: −18 dB → −8 dB across a section; reverb decay 4 s → 9 s in the climax.
- Volume swells: each pad chord fades in over 1–2 bars, out over 2–4.
- Stereo width of the air layer 60% → 120%.
- Delay feedback 30% → 55% for one passage, then back (never above 70%: runaway).
Use `local_ableton_set_device_param` for device values and clip envelopes; check what each
device exposes before writing. Cross-fade layers in and out (≥ 2 bars) instead of muting.

## 8. Arrangement (default 4 min at 70 BPM ≈ 70 bars)
| Section | Bars | What happens |
|---|---|---|
| Emerge | 1–8 | texture + drone fade in from silence (−inf to target over 4–8 bars) |
| Settle | 9–24 | main pad enters, first motif at bar 13, filter slowly opening |
| Bloom | 25–48 | keys/second pad, one chord change every 4–8 bars, reverb grows |
| Still | 49–60 | strip to drone + one voice; widest reverb, the most space |
| Dissolve | 61–70 | layers leave one by one, last note rings out 6–10 s, no hard stop |
Climax is about density and brightness, not loudness (+2–3 dB at most). Loops for 20+ min
pieces: make the last bar flow into the first (same chord, same layers). Name scenes with
`local_ableton_scene_name`.

## 9. Meditation / sleep variant
- No pulse, no drums, no melody above MIDI 84, no chord change faster than 16 bars.
- Tonic drone + one pad; optional bowl/bell every 8–16 bars at velocity 30–45.
- Even dynamics: total level change < 4 dB over the piece; nothing sudden.
- Don't promise health effects (no "432 Hz heals", no binaural claims); just calm music.

## 10. Mix targets
- Loudness: **−18 to −14 LUFS integrated** (streaming ambient −16; meditation −18 to −20);
  true peak ≤ −1 dBTP. No hard limiting: crest factor should stay high.
- Low end: high-pass everything except the drone at 100–150 Hz; drone low-passed ~ 200–400 Hz.
  Cut 200–400 Hz build-up on pads (−2 to −4 dB, wide).
- Harsh band: tame 2–5 kHz on pads and piano (−2 dB) — fatigue matters in long listening.
- Space: one long reverb send (decay 4–10 s, pre-delay 20–60 ms, low cut 200 Hz on the return)
  + one dotted-8th or 3/16 delay. Wet can be loud — 30–50% of perceived level is normal here.
- Relative levels (drone = reference 0): main pad −2, keys +1 (the most present), air −8,
  texture −12, soft arp −6.
- Check with `local_ears_track_levels` (masking between pads, keys must stay audible) and
  `local_ears_listen` (loudness, no clipping). The numbers are indicative; trust slow A/B.

## What ruins it
- Transients: pluck attacks, claps, crashes, keys with click, sudden mutes.
- Chord change every bar, V7–I cadences, busy bass lines.
- A 4-bar loop repeated with no automation — the #1 "AI-made" tell.
- Sub-bass heavy pads, mud at 250 Hz, bright fizz at 8 kHz all the time.
- Over-loud master (−9 LUFS) that kills the swell.
- Melody that is too catchy or too busy: it pulls attention and stops being ambient.

## Workflow with the tools
1. `local_ableton_snapshot`; `local_ableton_set_tempo` (70 default).
2. Tracks with `local_ableton_edit_track` `create_midi`: Drone, Pad, Keys, Air, Texture
   (+ Drums only if pulse). Keep them grouped mentally by band (§6).
3. Drone first (one note or root+5th, whole section), then pad chords (4–8 bars each, long
   attacks), firing with `local_ableton_fire` after each layer so the user hears it bloom.
4. Keys motif with silences, clip length offset from the pad (phasing), humanized.
5. Texture/field layer from the browser; reverb and delay sends.
6. Automation passes (§7): at least filter + reverb + one volume swell per section.
7. `local_ears_track_levels` then `local_ears_listen`; adjust; tell the user.

## Hard rules
- No hard transients; pad attack ≥ 300 ms; no claps or crashes.
- Harmonic rhythm ≥ 4 bars per chord (≥ 16 in meditation); no V7–I cadences.
- Something evolves every 8–16 bars via automation or modulation; never a static loop.
- Silence is part of the melody: ≥ 50% rests in the lead.
- Loudness −14 LUFS or quieter; keep dynamics.
- Say the mode, the tonic, the BPM and what evolves.

## Tell the user (short)
`Ambient · 70 BPM · D Lydian over a D drone · Dmaj9 → E/D every 8 bars · warm pad (fallback
preset, 1.5 s attack), felt-piano motif of 3 notes every 6 bars (7-bar clip, phases against
the 8-bar pad) · rain texture at −28 dB · filter opens over 16 bars, reverb 4→9 s in the
bloom · target −16 LUFS. Next: arrange to 4 min or add a soft arp?`
