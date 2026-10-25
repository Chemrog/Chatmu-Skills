---
name: chatmu-studio-drum-rack
description: >
  Use in Co-Producer (Chatmu Desktop + Ableton Live) to BUILD and tune a Drum
  Rack kit (not to write patterns): load a real kit (never an empty rack),
  read and edit pads and their chains, layer kicks, set choke groups so the
  open hi-hat is cut by the closed one, tune the kick to the song's key, level
  and pan pads, and check the kit with Chatmu Ears. Patterns are in
  chatmu-studio-drums-by-genre. Trigger phrases: "arma el kit", "arma un drum
  rack", "drum rack", "kit de batería", "cambia el kick", "capas de kick",
  "layer al kick", "afina el kick", "que el kick esté en tono", "choke",
  "grupo de corte", "hi-hat abierto y cerrado", "el rack está vacío", "pads",
  "build a drum kit", "tune the kick", "choke group", "batería", "drums",
  "Ableton".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Build and tune a Drum Rack kit: real kit, pads, kick layers, choke groups, kick in key, checked with Ears"
version: "1.0"
tags: ["studio", "ableton", "drum-rack", "drums", "batería", "kit", "kick", "choke", "co-producer"]
requiresTools: ["local_ableton_snapshot", "local_ableton_browser", "local_ableton_load_device", "local_ableton_load_devices", "local_ableton_edit_track", "local_ableton_rack", "local_ableton_lom", "local_ableton_device_params", "local_ableton_set_device_param", "local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_fire", "local_ableton_undo", "local_ears_listen", "local_ears_render", "local_music_theory", "local_ableton_get_notes"]
---

# Chatmu Studio — Drum Rack (build and tune the kit)
**Version:** 1.0
**Requires:** Chatmu Desktop bridge + Ableton Live 12 (AbletonMCP patched Remote Script 1.10.0-chatmu for pads via the LOM) + Chatmu Ears.
**Patterns:** `chatmu-studio-drums-by-genre` (pad map MIDI 36 = kick, 38 = snare, 42 = closed hat, 46 = open hat…). **Bass vs kick:** `chatmu-studio-bass-lines`, `chatmu-studio-sidechain`.

## What does this Skill do?

Gets a playable, tuned kit on a track — every pad that the pattern uses has a sound, hats
choke correctly, the kick sits in the key — and proves it with a test loop.

Answer in the user's language (usually Spanish). Short.

## HARD RULES

1. **Never leave an empty rack.** "Drum Rack" by name is the bare device (0 chains); the
   load tools report it as an error. Load a **kit preset** (browser path `drums`, e.g. a
   "… Kit" item) and, after any load, check that pads have chains.
2. **Read pads before writing:** `local_ableton_rack { action: "inspect" }` (chains, their
   devices, parameter names) and `local_ableton_lom describe` on `... devices N drum_pads
   <note>` / `... drum_pads <note> chains 0` for pad-specific properties. Use what the read
   shows; Live versions differ.
3. **Pads are addressed by MIDI note:** `drum_pads 36` = C1 (kick), `drum_pads 38` = D1
   (snare), `42` closed hat, `46` open hat.
4. **Loading a sample or device into ONE specific pad is not available yet** (untested in the
   tools). Options: pick a kit that already has the sound, copy a pad onto another with
   `local_ableton_lom call` `copy_pad` (destructive: overwrites the target pad; approval +
   `expectName`), or ask the user to drag the sample onto the pad (say which pad by note
   name).
5. **Never say a pad property "is not exposed"** without `describe` first.

## Phase 0 — Find or load the kit

1. `local_ableton_snapshot` → a MIDI track with a Drum Rack? Its device index.
2. None: create a MIDI track (`local_ableton_edit_track create_midi`, approval), browse
   `local_ableton_browser { path: "drums" }`, load a kit by its exact name (one approval).
3. `local_ableton_rack { action: "inspect", trackIndex, deviceIndex }` → which pads have
   chains, what's on them (Simpler/Sampler + effects). Map them to roles.

## Phase 1 — Build the kit pad by pad

| Role | Pad (note) | Check |
|---|---|---|
| Kick | 36 C1 | punch + low end; one kick, or layers (below) |
| Snare / clap | 38 D1 / 39 D#1 | body + crack |
| Closed / open hat | 42 F#1 / 46 A#1 | same family; choke (below) |
| Perc, toms, crash | 37, 41–51 | as the genre needs |

For each pad you change: read its chain's devices (`local_ableton_device_params` with
`devicePath: "live_set tracks N devices D drum_pads 36 chains 0 devices 0"`), then set in
real units (`local_ableton_set_device_param` with the same `devicePath`, `display`): volume
("-3 dB"), pan, transpose ("-2 st"), decay/release (ms).

### Kick layers
A layered kick = a short click/top kick + a body/sub kick. In a Drum Rack, a pad can hold
several chains (the pad's chain list): `describe` the pad; if the kit has an Instrument Rack
on the kick pad, its chains are the layers. Set each layer's level/filter: high-pass the
top layer (~150–300 Hz), low-pass the sub layer (~150 Hz). Check phase by ear (if the
low end gets thinner when both play, shift the body layer a few ms or flip it if the read
shows a phase parameter).

### Choke groups (open/closed hat)
`describe` `drum_pads 46 chains 0`: if it has a `choke_group` property, set the open hat
and the closed hat (pad 42 chains 0) to the same group (e.g. 1) with `local_ableton_lom set`.
Result: the closed hat cuts the open one, like a real hi-hat.

### Tune the kick to the key
1. Song key: from the user, or `local_music_theory { action: "detect_key" }` on the notes of
   a bass/chord clip read with `local_ableton_get_notes`.
2. Kick fundamental: solo the drum track, play a bar with only the kick (test clip with
   note 36), `local_ears_listen { seconds: 4 }` → the lowest strong peak in the spectrum
   (`local_ears_render { view: "spectrum_curve" }` helps), e.g. 52 Hz ≈ G#1.
3. Semitones to the nearest root or fifth of the key below ~60 Hz; set the kick sampler's
   transpose in `display` ("+2 st"). Re-listen: the peak should land on the note.
4. 808-style kicks with long tails: tune to the root; they play bass.

## Phase 2 — Test loop

A 1–2 bar Session clip with the genre's pattern (`chatmu-studio-drums-by-genre`), fire it.

## Ears verification

Kit playing (test loop), drum track soloed: `local_ears_listen { seconds: 8 }`. Check:
kick energy in sub/low, no pad far louder than the rest (peaks), hats not harsh
(brilliance/air), the open hat stops when the closed hits (waveform:
`local_ears_render { view: "waveform" }`), the kick's fundamental on the target note. Report
2–3 findings with numbers. If you couldn't listen, say **"no verificado"**.

## Don'ts

- Don't leave a rack with 0 chains or pads the pattern needs but are empty.
- Don't overwrite a pad with `copy_pad` without saying which one and getting OK.
- Don't duplicate the pattern skills: link `chatmu-studio-drums-by-genre`.
