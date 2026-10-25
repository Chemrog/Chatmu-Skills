---
name: chatmu-studio-sound-design
description: >
  Use in Co-Producer (Chatmu Desktop) to design a sound from scratch in Chatmu
  Synth with proven recipes: trompeta / brass, supersaw, growl bass, pluck,
  pad, talking bass with formants, sub bass, lead. Each recipe: which sections
  to touch (oscillators, unison, filter, envelopes, LFO, effects), starting
  values found by reading the real parameters, a test with a short MIDI clip,
  an Ears check that it sounds as intended, and saving it as the user's preset.
  Trigger phrases: "diseña un sonido", "hazme un supersaw", "hazme un pluck",
  "un pad", "un growl", "bajo que hable", "talking bass", "formantes", "suena
  como trompeta", "hazme una trompeta en el sinte", "un lead", "un sub",
  "sound design", "make a supersaw", "make a pluck", "make a pad", "growl
  bass", "Chatmu Synth", "sinte", "synth".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Chatmu Synth recipes: brass, supersaw, growl, pluck, pad, talking bass; tested with Ears, saved as preset"
version: "1.0"
tags: ["studio", "synth", "sinte", "chatmu-synth", "sound-design", "diseño-sonoro", "preset", "supersaw", "co-producer"]
requiresTools: ["local_synth_status", "local_synth_list_params", "local_synth_set_params", "local_synth_character", "local_synth_modulate", "local_synth_unmodulate", "local_synth_get_preset", "local_synth_set_preset", "local_synth_note", "local_ableton_snapshot", "local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_fire", "local_ableton_status", "local_ears_listen", "local_ears_render"]
---

# Chatmu Studio — Sound design recipes (Chatmu Synth)
**Version:** 1.0
**Requires:** Chatmu Desktop bridge + Chatmu Synth (VST3) on a MIDI track in Live + Chatmu Ears. Beta: Apple silicon only.
**Related:** `chatmu-studio-synth` (tool rules, presets), `chatmu-studio-clone-sound` (a sound FROM a recording — usually closer for real instruments), `chatmu-studio-sidechain`.

## What does this Skill do?

Builds a named sound type from a clean starting point, in small audible steps, checks it with
Ears, and saves it in the user's preset browser so it can be reused.

Answer in the user's language (usually Spanish). Short messages; "¿así o más?" after each step.

## HARD RULES

1. **Always "Chatmu Synth".** Never name the project it was derived from.
2. **Never guess a parameter name or unit.** Before setting anything:
   `local_synth_list_params { filter }` with the section ("osc_1", "filter_1", "env_1",
   "env_2", "lfo_1", "unison", "distortion", "chorus", "reverb", "delay", "portamento",
   "voice"). Use the names, ranges, units and options it returns. The recipes below give
   targets in musical terms; translate them with what the read shows.
3. **Save first, then design.** If the current patch matters, `local_synth_get_preset
   { save_to: "~/Music/Chatmu Synth/User/Presets/<old name> backup.vital" }`.
4. **Small steps, test after each section** (rule 4 of `chatmu-studio-synth`). Character
   knobs (`local_synth_character`) are for the final taste tweaks.
5. **Real instruments (trumpet, violin, voice): offer the clone first.** A clone from a
   recording (`chatmu-studio-clone-sound`) usually beats a recipe; the recipe is for when
   there is no recording or the user wants a "synth" version.
6. **Guide vocal / singing synth:** a prototype exists but it is **not a tool in this
   version**. Don't promise it or try to fake it with formants; say it's in development.

## Test setup (once)

1. `local_synth_status` → the instance (`port` if several).
2. A short test clip on the synth's track: `local_ableton_create_clip` (1–2 bars) +
   `local_ableton_write_notes` with a pattern that fits the sound (one long note for pads,
   8th-note line for plucks/leads, low notes for bass), then `local_ableton_fire` it.
   Quick alternative for a single hit: `local_synth_note { note, velocity, duration_ms }`.

## Recipes

Targets are where to START; adjust by ear.

### Brass / "trompeta"
- Osc 1: saw (bright, rich in harmonics). Unison off or 2 voices, tiny detune.
- Filter 1: low-pass, cutoff mid-low; **envelope → cutoff** (attack ~40–80 ms, short decay,
  sustain mid) so each note "opens" like a blown attack; velocity → cutoff (+).
- Amp env (env_1): attack 20–60 ms, sustain high, release 100–200 ms.
- Pitch: a small upward scoop at the start (short envelope → osc tune, a few cents).
- Vibrato: lfo_1 → osc tune, ~5–6 Hz, small amount (or the character knob `vibrato`).
- Mono / legato with a short glide for lines. A touch of noise for breath (`air`).
- Ears: most energy in high_mid/presence (800 Hz–5 kHz), not much air.

### Supersaw
- Osc 1 (and 2): saw, unison 7–9 voices, detune ~30–50 % of the range, stereo spread wide.
- Filter: low-pass fairly open, low resonance. Amp env: fast attack, sustain full, release
  200–400 ms. Chorus light, reverb medium.
- Play chords; high-pass the lows in the mix if it fights the bass.
- Ears: wide stereo (high width, correlation lower but positive), dense mid → brilliance.

### Growl bass
- Osc 1: a harmonically rich wavetable; lfo_1 synced (1/8 or 1/16) → wavetable position
  and/or filter cutoff. Filter: band-pass / comb / formant style if the read lists it.
- Distortion on (drive high), then a low-pass after it if harsh. Mono.
- Keep a clean sub (osc 2 or a separate sub track) under ~100 Hz.
- Ears: strong high_mid/presence movement; low end steady (mono).

### Pluck
- Osc: saw or square, unison 2–4 small detune. Amp env: attack 0, decay 150–400 ms,
  sustain 0, release short. Filter env (env_2 → cutoff): fast decay, a bit shorter than the
  amp. Velocity → cutoff. Delay 1/8 dotted for space.
- Ears: high crest factor, short decays visible in the waveform.

### Pad
- Osc 1+2: saw/triangle or soft wavetable, unison 4–6 small detune. Amp env: attack
  300 ms–1.5 s, release 1–3 s. Filter: low-pass mid, slow LFO (0.1–0.3 Hz) on cutoff or
  wavetable position. Chorus + long reverb (`space`).
- Ears: low crest, wide, little transient energy; keep low_mid in check.

### Talking bass (formants)
- Osc: saw/square, mono, glide short. Filter: **formant** model if `list_params` shows one;
  modulate its vowel/formant parameter with an LFO synced to 1/8 or with an envelope per
  note ("ua-ua"). Light distortion before or after.
- Ears: moving peaks in mid/high_mid; render `spectrogram` to see the vowels move.

### Sub bass
- Osc: sine (or triangle softened by a low-pass), mono, no unison, no reverb. Amp env:
  attack 0–5 ms, release short.
- Ears: almost all energy in sub/low; nothing above ~200 Hz.

## Ears verification

With the test clip playing (Live playing): solo the synth track, `local_ears_listen
{ seconds: 6–8 }`, read spectrum bands, stereo and dynamics, and check the recipe's "Ears"
line. Optional picture: `local_ears_render { captureId, view: "spectrum_curve" }` (or
`"spectrogram"` for movement). For a single `local_synth_note` with Live stopped, listen with
`allow_stopped: true`. Report in words + 1–2 numbers. If you can't listen, say **"no
verificado"** — never describe how it sounds from the parameters alone.

## Save it

When the user likes it: `local_synth_get_preset { save_to:
"~/Music/Chatmu Synth/User/Presets/<Name>.vital" }` (it appears in the plugin's preset
browser). Pick a new name; never overwrite. Tell them the name.

## Don'ts

- Don't set parameters you didn't read first.
- Don't jump to extreme values; don't stack effects "just because".
- Don't claim a sound is done without listening (or say "no verificado").
