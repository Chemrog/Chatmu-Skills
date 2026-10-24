---
name: chatmu-studio-sound-design
description: >
  Use in Co-Producer (Chatmu Desktop) when the user asks for a SOUND by type or
  character, without a reference recording: "hazme un pluck", "un pad cálido",
  "un supersaw para el drop", "un 808 con punch", "un bajo que gruña", "un
  growl de dubstep", "sonido de house", "algo tipo trance", "make me a pluck /
  pad / supersaw / 808 / growl / reese / lead". Builds it in Chatmu Synth from
  tested recipes (measured renders, not guesses), plays a test note and
  verifies it by ear with Chatmu Ears. For tweaks of an existing sound use
  chatmu-studio-synth; to clone a recording, the clone tools.
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Design classic synth sounds in Chatmu Synth (pluck, pad, supersaw, 808, growl) from measured recipes"
version: "1.0"
tags: [studio, synth, sound-design, diseño-sonoro, pluck, pad, supersaw, "808", growl, chatmu-synth, co-producer]
requiresTools: ["local_synth_status", "local_synth_set_preset", "local_synth_set_params", "local_synth_modulate", "local_synth_unmodulate", "local_synth_get_preset", "local_synth_note", "local_synth_character", "local_ears_listen", "local_ears_ensure_plugin"]
---

# Chatmu Studio — Sound design (classic synth sounds)
**Version:** 1.0
**Requires:** Chatmu Desktop bridge + Chatmu Synth open on a MIDI track. Ears for verification.
**Related:** chatmu-studio-synth (tool details, tweaks), chatmu-studio-genre-templates (which sound fits which genre), chatmu-studio-listen-troubleshooting.

## What does this Skill do?

It turns "quiero un pluck / pad / supersaw / 808 / growl" into a finished, playable
Chatmu Synth patch in one pass. Each recipe was rendered with Chatmu Synth's engine and
measured (envelope, brightness over time, stereo width, sub weight, pitch punch, wobble
rate) until it showed the traits that define the sound. Values here are **engine units**,
exactly what `local_synth_set_params` takes. Don't improvise numbers: start from the
recipe, then shape it to taste with the character knobs.

Answer in the user's language. Say what you built in producer words ("pluck corto con
filtro que se cierra, delay en corchea con puntillo"), not parameter dumps.

## HARD RULES

1. **Start from a clean patch.** A recipe only sets what it needs. Leftovers from the previous sound (an LFO on the cutoff, reverb, osc 2) will ruin it. Use path A or B below, never apply a recipe on top of another sound.
2. **Save the user's current sound first** if it is not a factory preset: `local_synth_get_preset { save_to }`.
3. **Engine units.** `local_synth_set_params` values are engine values (the recipe numbers). Option parameters take the option index (shown in parentheses).
4. **Verify before saying it's done.** Play a test note (`local_synth_note`) and, if the user is listening or Ears is available, listen to it. Never describe how it sounds if you didn't hear it: say "no lo he escuchado" instead.
5. **One sound per track.** If the track's Chatmu Synth already has a sound the user likes, ask before replacing it (or create a new MIDI track).

## Path A — factory preset (preferred when available)

The factory presets ship as `.vital` files: `Chatmu Pluck`, `Chatmu Warm Pad`, `Chatmu Supersaw`, `Chatmu 808`, `Chatmu Growl` (folder `~/Music/Chatmu Synth/User/Presets/` or the app's factory folder). They have the exact wavetables (true sine for the 808, square layers for pad and growl).

`local_synth_set_preset { file: "<folder>/Chatmu 808.vital" }`. An ungranted folder raises an approval; tell the user what it is for.

If the file is not there, use path B. It needs no files and sounds almost the same (verified).

## Path B — build from the init sound with the tools

1. **Reset** with `local_synth_set_params`:
   - `osc_2_on 0, osc_3_on 0, filter_1_on 0, filter_2_on 0, sample_on 0`
   - `chorus_on 0, delay_on 0, reverb_on 0, distortion_on 0, compressor_on 0, eq_on 0, flanger_on 0, phaser_on 0, filter_fx_on 0`
   - `osc_1_distortion_type 0, osc_1_unison_voices 1, legato 0, polyphony 8`

   Then remove every active modulation (`local_synth_get_preset` lists them → `local_synth_unmodulate`). Osc 1 keeps the init saw, which is what the recipes expect.
2. **Apply the recipe** below: one `local_synth_set_params` with the `set` list, then one `local_synth_modulate` per modulation.
3. **Test note** in the sound's register (pluck/supersaw C4–C5 = notes 60–72, pad a chord around C4, 808 C1–A1 = notes 24–33, growl F1 = 29).
4. **Listen** (rule 4) and compare with the "Should sound like" line.

## Recipes (engine units; option index in parentheses)

### Pluck — "pluck", "house pluck", "arp", "marimba sintética"
Should sound like: short, bright click that darkens fast; no sustain; echoes.
- `osc_1_on 1, osc_1_level 1, osc_1_unison_voices 3, osc_1_unison_detune 1.61, osc_1_unison_blend 0.7, osc_1_stereo_spread 0.7`
- `filter_1_on 1, filter_1_model 0 (Analog), filter_1_style 1 (24dB), filter_1_cutoff 48, filter_1_resonance 0.25, filter_1_keytrack 0.6`
- `env_1_attack 0, env_1_decay 0.861, env_1_sustain 0, env_1_release 0.707`
- `env_2_attack 0, env_2_decay 0.685, env_2_sustain 0, env_2_release 0.669`
- `polyphony 8, velocity_track 0.5, volume 6400`
- `reverb_on 1, reverb_dry_wet 0.16, reverb_decay_time 0.263`
- `delay_on 1, delay_sync 2 (Tempo Dotted), delay_tempo 9 (1/8), delay_dry_wet 0.14, delay_feedback 0.3, delay_style 2 (Ping Pong)`
- Mods: `env_2 → filter_1_cutoff 0.45`, `velocity → filter_1_cutoff 0.15`
- Measured: falls ~24 dB within 300 ms; brightness 1.3 kHz → 0.3 kHz in 300 ms.
- Variations: longer tail → `env_1_decay` up to ~1.0 (0.95 s); more "pluck" → `filter_1_cutoff` 40–44; marimba → `osc_1_unison_voices 1`, delay off.

### Warm pad — "pad", "colchón", "atmósfera", "fondo"
Should sound like: swells in (~1 s), sustains, wide, softly breathing.
- `osc_1_on 1, osc_1_level 0.671, osc_1_unison_voices 7, osc_1_unison_detune 3, osc_1_unison_blend 0.8, osc_1_stereo_spread 1`
- `osc_2_on 1, osc_2_level 0.447, osc_2_transpose 12, osc_2_unison_voices 3, osc_2_unison_detune 2, osc_2_stereo_spread 1, osc_2_destination 0 (Filter 1)`
- `filter_1_on 1, filter_1_model 0 (Analog), filter_1_style 0 (12dB), filter_1_cutoff 76, filter_1_resonance 0.15, filter_1_keytrack 0.3`
- `env_1_attack 0.974, env_1_decay 1, env_1_sustain 1, env_1_release 1.125`
- `lfo_1_sync 0 (Seconds), lfo_1_frequency -2.474`
- `polyphony 12`
- `chorus_on 1, chorus_dry_wet 0.35`
- `reverb_on 1, reverb_dry_wet 0.35, reverb_decay_time 1.807`
- Mod: `lfo_1 → filter_1_cutoff 0.08`
- Measured: attack ~0.9 s, holds within 4 dB, side/mid −1 to −2 dB (very wide).
- Variations: darker/lo-fi → `filter_1_cutoff` 66–70; brighter → 82–86; slower swell → `env_1_attack` 1.1.

### Supersaw — "supersaw", "trance lead", "EDM chords", "drop", "acordes grandes"
Should sound like: huge, wide wall of detuned saws; instant attack; for leads and chord stabs.
- `osc_1_on 1, osc_1_level 0.632, osc_1_unison_voices 16, osc_1_unison_detune 5.5, osc_1_unison_blend 0.85, osc_1_stereo_spread 1`
- `osc_2_on 1, osc_2_level 0.469, osc_2_transpose -12, osc_2_unison_voices 4, osc_2_unison_detune 2.49, osc_2_stereo_spread 0.6`
- `env_1_attack 0.252, env_1_decay 1, env_1_sustain 1, env_1_release 0.74`
- `polyphony 8`
- `distortion_on 1, distortion_type 0 (Soft Clip), distortion_drive 6, distortion_mix 0.6`
- `eq_on 1, eq_low_mode 1 (High Pass), eq_low_cutoff 40`
- `reverb_on 1, reverb_dry_wet 0.22, reverb_decay_time 1.138`
- `delay_on 1, delay_sync 1 (Tempo), delay_tempo 9 (1/8), delay_dry_wet 0.12, delay_style 2 (Ping Pong), delay_feedback 0.35`
- No modulations.
- Measured: side/mid −1 dB (widest of the set), attack < 10 ms.
- For a drop: pair with chatmu-studio-sidechain when it exists (pumping on the kick).

### 808 — "808", "bajo de trap", "sub", "bajo con punch"
Should sound like: deep sine bass with a "boom" pitch drop at the hit, long tail, a bit of grit so it reads on phones.
- `osc_1_on 1, osc_1_level 0.922, osc_1_unison_voices 1, osc_1_stereo_spread 0`
- `env_1_attack 0, env_1_decay 1.218, env_1_sustain 0, env_1_release 0.622`
- `env_2_attack 0, env_2_decay 0.514, env_2_sustain 0`
- `polyphony 1, legato 0, portamento_time -4.059`
- `distortion_on 1, distortion_type 0 (Soft Clip), distortion_drive 9, distortion_mix 0.55`
- `eq_on 1, eq_high_mode 1 (Low Pass), eq_high_cutoff 110`
- Path B only (makes the init saw a near-sine): `filter_1_on 1, filter_1_model 0, filter_1_style 1 (24dB), filter_1_cutoff 65, filter_1_keytrack 1, filter_1_resonance 0`
- Mods: `env_2 → osc_1_transpose 0.12` (punch), `env_2 → filter_1_cutoff 0.09` (keeps the punch through the filter)
- Measured: 99 % of the energy below 100 Hz. Pitch drop 8.8 semitones (factory) / 7.7 (path B) over the first ~70 ms, the same as reference 808s (6.6–8.8).
- Variations: more punch → transpose mod 0.15; cleaner → `distortion_mix` 0.3; longer → `env_1_decay` 1.3; glide between notes → overlap the MIDI notes (portamento is on).
- Mono: write 808 notes one at a time (no chords).

### Growl — "growl", "dubstep", "riddim", "wobble", "bajo que habla"
Should sound like: aggressive mid bass that "talks" (wow-wow) in time with the song.
- `osc_1_on 1, osc_1_level 0.866, osc_1_distortion_type 5 (Squeeze), osc_1_distortion_amount 0.6, osc_1_unison_voices 1`
- `osc_2_on 1, osc_2_level 0.5, osc_2_transpose 12, osc_2_destination 0 (Filter 1)`
- `filter_1_on 1, filter_1_model 5 (Formant), filter_1_formant_x 0.3, filter_1_formant_y 0.5, filter_1_formant_resonance 0.8, filter_1_mix 0.85`
- `env_1_attack 0.266, env_1_decay 1, env_1_sustain 1, env_1_release 0.589`
- `lfo_1_sync 1 (Tempo), lfo_1_tempo 9 (1/8)`
- `polyphony 1, legato 1`
- `distortion_on 1, distortion_type 3 (Sine Fold), distortion_drive 8, distortion_mix 0.5`
- `compressor_on 1`
- `eq_on 1, eq_low_mode 1 (High Pass), eq_low_cutoff 30`
- Mods: `lfo_1 → filter_1_formant_x 0.8`, `lfo_1 → osc_1_distortion_amount 0.3`
- Measured: vowel movement at 1/8 of the tempo (4 Hz at 120 BPM).
- Keep osc 1 at 1 unison voice: with 2+ voices the detune beating (~1 Hz) hides the wobble.
- Variations:
  - Faster talk → `lfo_1_tempo` 10 (1/16); half-time → 8 (1/4).
  - Riddim (choppier) → set the LFO shape to square in the plugin (no tool for LFO shapes yet; tell the user).
  - Add a sub under it with a separate 808/sine track.

## After building

- Offer the obvious next step in one line: "¿Te escribo un patrón para probarlo?" (chatmu-studio-compose-core / bass-lines / drums-by-genre).
- Small changes go through `local_synth_character` (brightness, attack, body, air, vibrato, space, wear, volume; −1..1, start with ±0.3).
- If the user likes it: `local_synth_get_preset { save_to: "~/Music/Chatmu Synth/User/Presets/<name>.vital" }` so it shows in the plugin's browser.

## Verification (rule 4)

With the track playing (or a test note looped in a clip), `local_ears_listen` 8 s and check:

| Sound | Must hear |
|---|---|
| Pluck | short notes, clear gaps between them, echoes |
| Pad | slow fade-in, continuous, wide |
| Supersaw | very wide, dense, no attack delay |
| 808 | strong low end (most of the energy under 100 Hz), "boom" at each hit |
| Growl | regular wow-wow in time with the song |

If something's off (e.g. the pad sounds narrow), re-read the patch with `local_synth_get_preset` and compare with the recipe: usually a leftover from the previous sound (rule 1).

## Don'ts

- Don't apply a recipe on top of another sound without the reset.
- Don't invent parameter values or ranges; use the recipe, then the character knobs.
- Don't put chords on the 808 or the growl (mono patches).
- Don't claim it sounds right without listening; don't promise wavetable changes (no tool for them yet; path A covers it).
