---
name: chatmu-studio-sound-profile-produce
description: >
  Use in Co-Producer (Chatmu Desktop) when the artist asks for a track or
  several sketches (bocetos) IN THEIR OWN SOUND, with their own material: their
  template, their samples and packs, their effect chains and plug-ins, inside
  the tempo/key ranges and master targets of their sound profile
  (Sound/SOUND.md + Sound/profile.json). Delivers open, editable Ableton Live
  sets that the artist curates and finishes; batch mode for many sketches
  ("make 10 sketches tonight"). Trigger phrases: "haz un track con mi sonido",
  "hazme un boceto de Palmasur", "bocetos con mi sonido", "haz 10 bocetos",
  "con mi material", "make a track in my sound", "make 10 sketches", "sketches",
  "batch", "sound profile", "SOUND.md".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Sketches in the artist's own sound: their template, samples and chains, checked against the profile"
version: "1.0"
tags: ["studio", "ableton", "sound-profile", "perfil-de-sonido", "sketches", "bocetos", "batch", "co-producer"]
requiresTools: ["local_read_file", "local_copy_file", "local_ableton_open_set", "local_ableton_snapshot", "local_ableton_set_tempo", "local_ableton_edit_track", "local_ableton_create_audio_clip", "local_ableton_clip", "local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_browser", "local_ableton_load_device", "local_ableton_mixer", "local_ableton_arrangement", "local_ableton_export", "local_ears_analyze_file", "local_music_theory"]
---

# Chatmu Studio — Produce with the sound profile
**Version:** 1.0
**Requires:** a sound profile in the artist folder (`chatmu-studio-sound-profile-build`), Ableton Live with the AbletonMCP Remote Script and «Permitir control», Chatmu Ears for the check.
**Related:** `chatmu-studio-sound-profile-edit`, `chatmu-studio-compose-core`, `chatmu-studio-harmony-voicing`, `chatmu-studio-drums-by-genre`, `chatmu-studio-humanize`, `chatmu-studio-export`, `chatmu-studio-reference`.

## What it is (how to say it)

"Tu asistente que sabe cómo suena tu proyecto y trabaja con tu material." The sketch is
built in the artist's DAW from what is already theirs: their template, their loops and
one-shots, their chains and plug-ins, the progressions they use. The result is an open Live
set; the artist decides what stays, changes it and finishes it. Never say the result "is
not AI"; never present a sketch as a finished song.

## HARD RULES

1. **Read the profile first.** `local_read_file` on `<artist folder>/Sound/SOUND.md`, then
   `Sound/profile.json`. **SOUND.md wins** over profile.json when they disagree (the artist
   edited it). Its "Don't" list is absolute.
2. **Their material only.** Samples from the paths in the profile (`samples.top`,
   `localAssets.sampleFolders`, the template's own clips) — never download or invent sources.
   If a needed sound isn't in their material, say so and ask.
3. **Never touch the originals.** Each sketch is a NEW set: copy the template with
   `local_copy_file` to `<artist folder>/Sketches/<YYYY-MM-DD> <name>/<name>.als` and open the
   copy. Never save over `Sound/local/template.als` or any of their projects.
4. **Inside the ranges.** BPM inside `tempo.bpm` p10–p90 (or the range SOUND.md states), a
   key from `keys.sets`, time signature from `timeSignatures`, structure from `structure`.
5. **Missing plug-in** (the chain names a third-party plug-in that this Mac doesn't have):
   say which one and propose the native Live equivalent (e.g. a compressor plug-in → Glue
   Compressor/Compressor; tape/lo-fi → Saturator + Redux/Vinyl Distortion; EQ → EQ Eight).
6. Loading devices and creating tracks ask on screen (except under «Recomendado»): group
   the loads (`local_ableton_load_devices`) so the artist isn't asked ten times.

## Phase 1 — Plan the sketch (say it in 2–3 lines before building)

From the profile: BPM, key, meter, the roles to use (`trackTemplate.roles` with share ≥ 0.5,
in their usual order and colors), the samples per role (`samples.roleTopSamples`, combos the
artist already uses in `samples.combos` / `packCombos`), the chain per role (`chains[role]`),
a progression from `midi.progressions` (if the artist works with MIDI), the master chain
and loudness target (`masters.integratedLufs` median, `truePeakDbtp`).

## Phase 2 — Build in Live

1. Copy and open the template: `local_copy_file { source: localAssets.template, destination:
   <sketch folder>/<name>.als }` → `local_ableton_open_set { path, expectName }`. Wait for Live
   to load, then `local_ableton_snapshot`. No template → start from the current set after the
   artist saves it, and create the tracks of the template (`local_ableton_edit_track`).
2. Tempo: `local_ableton_set_tempo`.
3. Loops/one-shots: `local_ableton_create_audio_clip` with `sampleKey/setKey/sampleBpm/setBpm`
   (key/BPM from the sample's name in the profile) → then `local_ableton_clip` to warp
   (beats for drums, complex for melodic) and transpose by the shortest way.
4. MIDI parts: `local_ableton_create_clip` + `local_ableton_write_notes` with a progression
   from the profile (voicings: `chatmu-studio-harmony-voicing`; feel: `midi.swing16` and
   `chatmu-studio-humanize`).
5. Chains: the template already has them; extra devices with `local_ableton_browser` +
   `local_ableton_load_device(s)`; plug-in presets the artist saved load by name.
6. Arrangement: sections and lengths from `structure` (`chatmu-studio-arrangement`), with
   `local_ableton_arrangement`.

## Phase 3 — Check against the profile

1. Render a section: `local_ableton_export { action: "start", bit_depth 32, folder: <sketch folder> }`
   (`chatmu-studio-export`).
2. `local_ears_analyze_file` on the render, compare with `masters`: integrated LUFS and true
   peak vs the medians, `spectralCurve` per band, `stereoWidthPercent`. A sketch without the
   master chain will be quieter: compare the band balance, not only the level.
3. Fix only what is clearly off (a band ±3 dB from the curve, width far from the range) with
   `local_ableton_mixer` / the EQ already in the chain. Report: "dentro de tu rango" or what is
   off and what you changed.

## Phase 4 — Deliver

Leave the set open and saved (ask the artist to press Cmd+S if Live shows unsaved changes).
Tell them: the sketch folder, BPM/key, which of their samples and chains you used, how it
measured against their masters, and that it is a starting point to curate. Add a line to the
sketch folder's `CHATMU.md` (`local_write_file`): date, BPM/key, samples used.

## Batch mode ("haz 10 bocetos", overnight)

- Confirm the count and that Live will be busy the whole time (it is the artist's DAW).
- One sketch at a time, each in its own folder `Sketches/<date> <name> NN/`; vary key, tempo
  (inside the range), sample combo and progression so they are not ten copies.
- After each: render + check (Phase 3) + one line in `Sketches/BATCH.md` (name, BPM, key,
  samples, LUFS vs target). Stop and report if something fails twice in a row.
- At the end: the list for the artist to curate ("escucha y quédate con los que te gusten").
  Opening sets switches Live's current set: the batch runs only when the artist says Live is
  free. A scheduler that starts it by itself does not exist yet: the artist keeps Chatmu
  Desktop open and starts it.

## Learning from approvals (not automatic yet)

When the artist keeps or discards a sketch and says why ("me gusta la trompeta con ese
delay", "nunca uses ese bombo"), add it to SOUND.md's Rules with
`chatmu-studio-sound-profile-edit`. Nothing is learned silently.
