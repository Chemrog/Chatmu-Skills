---
name: chatmu-studio-synth
description: >
  Use in Co-Producer (Chatmu Desktop) whenever the user works with Chatmu Synth,
  Chatmu's own synth plugin (VST3): shape its sound ("más brillante", "menos
  reverb", "más aire", "ataque más suave", "más vibrato", "más sucio"), set
  exact parameters, add or remove modulations, play a test note, load or save a
  preset, or find the audio they dropped on the plugin (cloning a recording:
  chatmu-studio-clone-sound). Covers installing it and finding the open
  instance. Trigger phrases: "Chatmu Synth", "el sinte", "el
  synth", "el sintetizador", "hazlo más brillante", "ábrele el filtro", "quítale
  reverb", "más aire", "toca una nota", "carga este preset", "guarda el preset",
  "solté un audio en el sinte", "make the synth brighter", "synth preset".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Drive Chatmu Synth: character knobs, exact parameters, modulations, test notes and presets"
version: "1.1"
tags: ["studio", "synth", "sinte", "chatmu-synth", "sound-design", "preset", "co-producer"]
requiresTools: ["local_synth_status", "local_synth_character", "local_synth_list_params", "local_synth_set_params", "local_synth_get_preset", "local_synth_set_preset", "local_synth_modulate", "local_synth_unmodulate", "local_synth_note", "local_synth_dropped_audio", "local_synth_clone", "local_repair"]
---

# Chatmu Studio — Chatmu Synth
**Version:** 1.1
**Requires:** Chatmu Desktop bridge + Chatmu Synth (VST3) loaded on a track in the user's DAW. Beta: Apple silicon Macs only.
**Related:** chatmu-studio-clone-sound (clone a recording, audio → MIDI), chatmu-studio-sound-design (new sounds: factory library, recipes), chatmu-studio-listen-troubleshooting (hearing the result), chatmu-studio-compose-core (writing MIDI for it).

## What does this Skill do?

Chatmu Synth is Chatmu's own synthesizer. Every open instance (one per track
that has the plugin) talks to the bridge, so you can read and change its whole
sound. This skill is how to change it the way a producer would: small, audible,
reversible steps, checked by ear.

Answer in the user's language (usually Spanish). Short messages.

## HARD RULES

1. **Always call it "Chatmu Synth".** Never name the project it was derived from, and never send the user to third-party synth sites or presets.
2. **Character knobs first.** The 8 knobs are in BOTH the Simple and the Advanced view of the plugin. For any broad request ("brighter", "less reverb", "more air") use `local_synth_character`. It moves relative offsets over the preset's own values: 0 = the preset as it was, so it never destroys a cloned or designed sound. Use `local_synth_set_params` only for a precise, named change.
3. **Never guess a parameter name.** Call `local_synth_list_params` with a filter (`filter_1`, `env_1`, `osc_1`, `reverb`, `lfo_1`…) before `local_synth_set_params` or `local_synth_modulate`.
4. **Small steps.** Knobs go from -1 to 1: move 0.2–0.4, check, then adjust. Never jump to ±1 on the first try.
5. **`local_synth_set_preset` replaces the whole sound.** Before it, offer to save the current one (`local_synth_get_preset` with `save_to`). Never load a preset the user didn't ask for.
6. **Cloning a recording = `chatmu-studio-clone-sound`** (`local_synth_clone`; the Clone button / drop zone is in both the Simple and the Advanced view). "Pásalo a MIDI" = `local_audio_to_midi` (same skill). Never say cloning doesn't exist.
7. **A guide vocal / a synth that sings the melody is NOT a tool in this version.** A prototype exists; say it's in development, don't promise a date and don't try to fake it.
8. **Never invent where a setting lives** in the DAW or the plugin. If it isn't in this skill, say you're not sure.

## Phase 0 — Find the synth (read only)

`local_synth_status` →

| Result | What to do |
|---|---|
| `instances` has one reachable | Use it (no `port` needed). |
| Several | Pick by `preset_name` / host; if it's ambiguous, ask which track. Pass its `port` on every call. |
| None, `installed.installed: true` | Ask the user to load **Chatmu Synth** on a MIDI track (Live: browser → Plug-Ins → VST3 → Chatmu Synth). If Live doesn't list it: Settings → Plug-Ins → Rescan. |
| None, not installed | Offer `local_repair` with `install_synth` (the user approves on screen), then the rescan above. If it says unavailable, this Mac isn't supported by the beta (Apple silicon only). |
| `reachable: false` | The plugin window may be busy or the DAW froze; ask the user to check the track, then retry once. |

## Phase 1 — Change the sound

### Broad requests → `local_synth_character`

| The user says | Knob | First step |
|---|---|---|
| más brillante / más presencia / ábrelo | `brightness` | +0.3 |
| más oscuro / más opaco / quítale agudos | `brightness` | -0.3 |
| ataque más suave / que entre lento | `attack` | +0.3 |
| más pegada / que ataque rápido | `attack` | -0.3 |
| más cuerpo / más grave | `body` | +0.3 |
| más aire / más soplido / más respiración | `air` | +0.3 |
| más vibrato / que vibre | `vibrato` | +0.3 |
| más espacio / más reverb | `space` | +0.3 |
| más seco / menos reverb | `space` | -0.3 |
| más sucio / más saturado / con más grano | `wear` | +0.3 |
| más fuerte / más bajo | `volume` | ±0.2 |

Call it with only the knobs you move (`{"brightness": 0.3}`); the reply has the applied values. Read them without `values` before moving them again, so you add to where they are.

### Precise requests → `local_synth_set_params`

1. `local_synth_list_params { filter }` → current value, range, units.
2. `local_synth_set_params { values }` in those units (clamped to the range). The DAW sees each change, so the user can undo it there.

### Modulations

- `local_synth_get_preset` lists the active ones (`modulations`).
- `local_synth_modulate { source, destination, amount }` connects or updates one (amount -1..1, start around ±0.1–0.3). Examples: vibrato = `lfo_1` → `osc_1_tune`; brighter when played harder = `velocity` → `filter_1_cutoff`.
- `local_synth_unmodulate { source, destination }` removes one.

## Phase 2 — Check it

- `local_synth_note { note, velocity, duration_ms }` plays a note straight into the plugin so the user hears the change without writing MIDI. Use a note in the instrument's range (bass ~36–48, lead ~60–76).
- To measure instead of guess: play the part (or the note) while listening with Chatmu Ears (chatmu-studio-listen-troubleshooting).
- Then ask "¿así o más?" and repeat in smaller steps.

## Presets

- **Read**: `local_synth_get_preset` gives a summary (name, comments, wavetables, modulations, the settings that differ from the defaults). If the comments carry `"final_score": NN`, the plugin shows it as "Similarity NN%".
- **Save**: `local_synth_get_preset { save_to: "~/Music/Chatmu Synth/User/Presets/<Name>.vital" }`. That folder is the plugin's own preset browser, so it appears there. Writing outside an authorized folder asks the user.
- **Load**: `local_synth_set_preset { file }` (or `{ preset }` with the JSON). It replaces the whole sound: rule 5.

## Dropped audio

When the user says "el audio que solté" / "este sonido" after dropping a file on the plugin (drop zone or Clone button, Simple or Advanced view), `local_synth_dropped_audio` gives its path. "Clónalo" → `chatmu-studio-clone-sound` (`local_synth_clone` without `path` uses this file).
