---
name: chatmu-studio-clone-sound
description: >
  Use in Co-Producer (Chatmu Desktop) when the user wants to CLONE the sound of
  a recording into Chatmu Synth, or turn a recording into MIDI in Ableton Live:
  an audio in Descargas, attached in the chat, dropped on the plugin (Simple or
  Advanced view) or a clip already in Live. Runs the Chatmu Ears timbre clone
  (automatic recipe: plucked/pulsada for guitar, bass, harp, piano; sustained/
  sostenida for trumpet, voice, violin, flute, leads), loads and saves the
  preset in the user's library, writes the phrase as MIDI, explains the
  similarity score, then fine-tunes with the character knobs. Trigger phrases:
  "clona este sonido", "clónalo", "clona la trompeta", "clona la guitarra",
  "quiero este sonido en el sinte", "haz un preset con este audio", "solté un
  audio en el sinte", "el audio que solté", "pásalo a MIDI", "convierte el
  audio a MIDI", "sácame las notas", "audio a MIDI", "clone this sound",
  "clone this recording", "audio to MIDI", "Chatmu Synth", "sinte", "synth".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Clone a recording into Chatmu Synth (plucked/sustained recipe) and turn audio into MIDI in Live"
version: "1.0"
tags: ["studio", "synth", "sinte", "chatmu-synth", "clone", "clonar", "audio-to-midi", "sound-design", "co-producer"]
requiresTools: ["local_synth_status", "local_synth_dropped_audio", "local_synth_clone", "local_audio_to_midi", "local_synth_character", "local_synth_get_preset", "local_synth_set_preset", "local_synth_note", "local_ableton_snapshot", "local_ableton_arrangement", "local_ableton_lom", "local_ears_analyze_file", "local_ears_listen", "local_list_access", "local_repair"]
---

# Chatmu Studio — Clone a sound (Chatmu Synth) + audio → MIDI
**Version:** 1.0
**Requires:** Chatmu Desktop bridge + Chatmu Ears (with timbre clone) + Chatmu Synth (VST3) on a MIDI track. Beta: Apple silicon Macs only.
**Related:** `chatmu-studio-remake-song` (a whole song: stems → one clone + MIDI per instrument → Live set), `chatmu-studio-separate-stems` (isolate one instrument first when it's inside a full mix), `chatmu-studio-synth` (knobs, presets, parameters), `chatmu-studio-sound-design` (any sound by instrument, genre or character: factory library, recipes), `chatmu-studio-listen-troubleshooting`.

## What does this Skill do?

"Clona este sonido" → a Chatmu Synth preset that sounds like the recording (pure
synthesis, no samples), loaded in the plugin, saved in its preset browser, with the phrase
written as MIDI so the user hears it right away. "Pásalo a MIDI" → the notes of a recording
in a new MIDI clip in Live.

Answer in the user's language (usually Spanish). Short messages; one progress line, not one
per poll.

## HARD RULES

1. **Always "Chatmu Synth".** Never name the project it was derived from.
2. **Monophonic sources clone best** (one note at a time: trumpet, voice, violin, flute, a
   bass line, a guitar melody). With chords/strums the plucked recipe models the HIT
   (attack, decay, brightness, pick) — not the chords. Say it before starting if the audio
   is chordal.
3. **The score is objective, not taste.** Explain it as in Phase 3; never say "suena
   idéntico".
4. **Nothing is overwritten.** The clone saves new presets (`<Name>.vital` and
   `<Name> (play).vital`) in `~/Music/Chatmu Synth/User/Presets`; a taken name gets " 2".
   But loading a clone REPLACES the sound in the open instance: if the current sound
   matters, save it first (`local_synth_get_preset { save_to }`, see `chatmu-studio-synth`).
5. **Live's API can't write pitch bend or CC1.** The MIDI written in Live has the notes
   only. The expression (bends, vibrato, dynamics) is in `expression.mid` next to the
   renders: the user drags it into a clip if they want the "performance" version. Don't
   promise that the agent will put it there.
6. **Never invent a cause.** Errors come with a code; use the table in Phase 5.
7. One clone at a time; don't start a second while one is running.

---

## Phase 0 — Find the audio and the synth (read only)

| Where the audio is | What to pass |
|---|---|
| Dropped on the plugin (Simple or Advanced view, drop zone or Clone button) | nothing: `local_synth_clone` uses it. Check with `local_synth_dropped_audio` (`exists: true`). |
| A file (Descargas, Escritorio, chat attachment) | `path` (wav, aiff, flac, mp3, m4a; mp3/m4a are converted locally). Ungranted folder → the app asks once: "acepta el permiso para leer esa carpeta". |
| An audio clip in Live | clone: read its file path with `local_ableton_lom { action: "get", path: "live_set tracks N clip_slots M clip", props: ["file_path"] }` (Session) and pass it as `path`. MIDI: `local_audio_to_midi` takes `track` + `clip` / `arrangement_clip` directly. |

Then `local_synth_status`: one reachable instance → use it; several → ask which track (pass
`port`); none → ask the user to load **Chatmu Synth** on a MIDI track (installation: see
`chatmu-studio-synth`, Phase 0).

## Phase 1 — Choose the recipe (automatic, explain it)

Ears decides the recipe from the audio; `instrument_hint` names the preset, sets the pitch
range (bass, cello, voice, flute, violin) and can force the recipe for a known instrument.

| Recipe | Typical sources | What it models | What comes out |
|---|---|---|---|
| **Plucked / pulsada** | guitar, bass (picked), harp, piano, pluck synths | the hit: attack, decay to silence, brightness that fades, pick noise | a playable pluck; does not follow the melody of chords |
| **Sustained / sostenida** | trumpet, sax, voice, violin, flute, leads, pads | the timbre per pitch zone, soft/loud layers, the attack | a "(play)" preset where velocity = brightness/level and mod wheel = vibrato, plus a "performance" preset that matches the original phrase with its expression MIDI |

Pass `instrument_hint` in English ("trumpet", "guitar", "voice", "bass", "flute", "violin",
"cello", "sax"). If the user doesn't say what it is, ask once ("¿qué instrumento es?") or
leave it out.

## Phase 2 — Clone

`local_synth_clone { path?, instrument_hint, name?, port? }` (defaults: 60 iterations, loads
the "(play)" preset, writes the phrase as MIDI on the synth's track).
- Takes ~30–90 s. If the result has `status: "running"` + `job_id`, call again with
  `{ job_id }` only (no path) until it's done. Tell the user once: "Estoy clonando (≈1 min)".
- Several tracks have Chatmu Synth → pass `track` (the result says which ones).
- `load: "performance"` only if the user wants the original phrase reproduced (then they
  also need `expression.mid`, rule 5).
- `iterations` higher (e.g. 150) = slower and sometimes closer; offer it only if the first
  score is low and the user wants to wait.

## Phase 3 — Explain the result (short)

| Field | Say |
|---|---|
| `recipe` (+ `measures`) | "Lo traté como **sostenido** (la nota se mantiene después del ataque)" / "como **pulsado** (el sonido cae después del golpe)". |
| `score.start → score.final` | "Parecido espectral: 38 → 64 / 100". **50–70 is a good clone**; > 70 very close; < 45: say it's a rough approximation and why (chords, noise, reverb, very short audio). |
| `score.play_final` | the playable preset's score (usually a bit lower: it must work for every note) |
| `preset_name`, `play_preset_name` | saved in `~/Music/Chatmu Synth/User/Presets` — visible in the plugin's preset browser |
| `loaded` | which one is playing now; if `loaded: false`, it is saved: the user loads it from the browser |
| `midi` | the clip written on the synth's track; `expression_left_out` → rule 5 with its `file` path; `skipped` → say why |
| `notes`, `zones` | how many notes Ears found; pitch zones it learned (sustained) |

## Phase 4 — Fine-tune by ear

1. Play it: fire the MIDI clip it wrote (or `local_synth_note` in the instrument's range).
2. Ask "¿qué le falta?" and map it with `local_synth_character` (knobs in both the Simple and
   Advanced views): brillo, ataque, cuerpo, aire, vibrato, espacio, desgaste, volumen.
   Steps 0.2–0.3. Knobs are offsets over the clone (0 = the clone), so they never destroy it.
3. To keep a tweak: save it under a new name with `local_synth_get_preset { save_to:
   "~/Music/Chatmu Synth/User/Presets/<Name> v2.vital" }` (never over the clone).

## Audio → MIDI (`local_audio_to_midi`)

- Source: `path`, or `track` + `clip` (Session) / `arrangement_clip` (index from
  `local_ableton_arrangement get_clips`).
- Target: `target_track` (an existing MIDI track) or a NEW MIDI track (on-screen approval).
- `quantize`: "1/16" default; "off" for rubato; "1/8t" / "1/16t" for triplet feel.
- Monophonic detection: melodies, basslines, solo lines come out right. Chords/strums →
  **approximate** (the strongest line) or `rhythm` mode (one C3 per attack, to re-voice).
  The result says which: tell the user plainly.
- Timing follows the Set's tempo from the start of the file; a warped/trimmed clip may not
  line up exactly: say so if it's a clip from Live.
- Natural pairing: "clónalo y pásalo a MIDI" = `local_synth_clone` (already writes MIDI on
  the synth track). Use `local_audio_to_midi` for a different instrument or a separate track.

## Phase 5 — Errors

| Code / message | Meaning | Do |
|---|---|---|
| `ears_outdated` | the installed Chatmu Ears has no timbre clone | tell the user Chatmu Ears needs updating (not their fault); offer `local_repair { action: "install_ears" }` (installs the Ears bundled with the app, on-screen approval); if it still says outdated, Chatmu Desktop itself needs updating |
| `no_steady_notes` | sustained recipe found no clear notes (chords, noise) | try `instrument_hint` "guitar" (plucked) or a monophonic passage |
| no synth instance | Chatmu Synth isn't open | ask to load it on a MIDI track |
| "Several tracks have Chatmu Synth" | MIDI target ambiguous | pass `track` |
| path not granted | folder permission | the app asks; tell the user to accept |
| job still running | not an error | call again with `job_id` |

## Ears verification

The clone's `score` is already an Ears measurement of the render against the original. After
knob tweaks, verify by listening: play the clip (Live playing) → `local_ears_listen
{ seconds: 6–8 }` with only the synth track soloed, and compare its band balance with
`local_ears_analyze_file { path: <original>, tool: "spectrum" }` (both are loudness-normalized
by Ears). Report the closest/farthest bands. If you can't listen (nothing playing, Ears
unavailable), say **"no verificado"** and rely only on the score.

## Don'ts

- Don't promise an identical copy, or chords from a chord recording.
- Don't overwrite a preset; don't load a clone over a sound the user didn't save.
- Don't say the agent can write pitch bend / CC1 into Live.
- Don't name the synth's origin project.
