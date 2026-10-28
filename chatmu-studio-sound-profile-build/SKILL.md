---
name: chatmu-studio-sound-profile-build
description: >
  Use in Co-Producer (Chatmu Desktop) when the artist wants Chatmu to LEARN HOW
  THEIR PROJECT SOUNDS from their own material: a folder of Ableton Live
  projects (.als) and their finished masters. Builds the sound profile
  (perfil de sonido) in the artist's workspace folder: Sound/SOUND.md (the
  artist's editable rules) + Sound/profile.json (BPM and key ranges, track
  template, effect chains per track and on the master, third-party plug-ins
  and where they are used, most used samples and packs, progressions, master
  loudness / tone / stereo width from Chatmu Ears) and a local template.als.
  Trigger phrases: "crea mi perfil de sonido", "aprende mi sonido", "analiza
  mis proyectos", "analiza mi disco", "cómo suena mi proyecto", "mi sonido",
  "create my sound profile", "learn my sound", "sound profile", "SOUND.md",
  "analyze my Ableton projects", "update my sound profile".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Learn the artist's sound from their Live sets and masters into Sound/SOUND.md + profile.json"
version: "1.0"
tags: ["studio", "ableton", "sound-profile", "perfil-de-sonido", "co-producer", "mastering", "samples", "plugins"]
requiresTools: ["local_sound_profile_build", "local_als_parse", "local_list_access", "local_list_dir", "local_search_files", "local_read_file", "local_ears_analyze_file"]
---

# Chatmu Studio — Build the sound profile
**Version:** 1.0
**Requires:** Chatmu Desktop bridge (Co-Producer). Masters need Chatmu Ears installed and set up. Nothing needs Ableton Live open.
**Related:** `chatmu-studio-sound-profile-edit` (the artist corrects SOUND.md), `chatmu-studio-sound-profile-produce` (sketches with the profile).

## What it is (how to say it)

"Tu asistente que sabe cómo suena tu proyecto y trabaja con tu material." Chatmu reads the
artist's own sets and masters on their Mac and writes down what it finds: tempos, keys,
the tracks they always set up, the chains and plug-ins they use and where, the samples and
packs they reach for, how their masters measure. The artist owns all of it and edits it.

Never say the result "is not AI" or "stops being AI", and never promise that Chatmu makes
music by itself: it organizes and measures the artist's material and works in their DAW
with it.

## HARD RULES

1. **Read-only on the artist's projects.** The tool only reads `.als` files; the template is
   a COPY. Never edit, move or "clean" the originals.
2. **Only `Sound/` is written**, in the artist's linked workspace folder (or `output_folder`).
   An existing `Sound/SOUND.md` is the artist's text: it is never overwritten (the new draft
   goes to `SOUND.draft.md`, then use `chatmu-studio-sound-profile-edit` to merge).
3. **Heavy assets stay on the Mac.** `Sound/local/` (template.als …) is never uploaded. Only
   the text files (`SOUND.md`, `profile.json`) describe the project elsewhere.
4. **Report what the data says, not more.** Ears measures loudness, spectrum and stereo of
   the masters; it does not measure their tempo or key (those come from the sets). Don't
   invent a "lo-fi character" number: it is not measured yet.
5. One build at a time. Hundreds of sets take minutes: say so once and report progress.

## Phase 0 — Where things are

1. The artist folder: the hidden `[proyecto local]` block names it ("Carpeta del artista").
   No linked folder → ask the user to link it with the folder chip in the chat (or pass
   `output_folder`).
2. Ask which folders hold their Live projects (an external drive is fine) and which audio
   files are finished masters (e.g. the last record). `local_list_access` shows what is
   granted; `local_search_files` (`**/*.als`) helps find projects. Ungranted folders: the app
   asks the user once when the build starts — tell them to accept.
3. More sets = a better profile. 10+ sets and 3+ masters is the minimum worth doing; a whole
   library (hundreds) is fine.

## Phase 1 — Build

`local_sound_profile_build { sets: [folders or .als], masters?: [files or a folder], artist?,
workspace_id?, output_folder?, max_sets?, export_template?, analyze_masters? }`

- Backups (`Backup/`), `Samples/` and hidden folders are skipped; up to `max_sets` (600).
- If the result has `status: "running"` + `job_id`, call again with `{ job_id }` until done.
  One short progress line to the user ("Llevo 120 de 340 proyectos"), not one per call.
- `sets.unreadable` lists sets that could not be read (corrupt, not a Live set): mention the
  count, not each file.
- `masters.failed` with an Ears code → see `chatmu-studio-listen-troubleshooting`; the profile
  is still written without the master targets.

To look at one set in detail (which plug-ins on which track, the samples of a clip, the
notes): `local_als_parse { path, detail: "summary" | "full" }`. It reflects the last save.

## Phase 2 — Show the result (short, in the user's language)

From `summary`: BPM range and the usual keys, the usual track roles, the 3–5 plug-ins they
use most and on which tracks, the master chain, the master loudness (LUFS), the main packs.
Then: "Escribí tu SOUND.md: ¿lo revisamos juntos?" → `local_read_file` on `files.soundMd`
and go through it section by section with `chatmu-studio-sound-profile-edit`. The artist
fills **Identity** and **Rules**: those matter more than any number.

If `files.existingSoundMd` is present, the artist already had a SOUND.md: compare it with
`SOUND.draft.md` and propose only the changes (new plug-ins, a tempo range that moved).

## What `profile.json` holds (for other skills)

`tempo.bpm` (p10/median/p90), `keys.sets`, `timeSignatures`, `structure`, `trackTemplate.roles`
(role, share of sets, usual count, order, color, names), `chains[role]` (chains, effects,
instruments), `returns`, `master`, `plugins[]` (name, vendor, format, sets, roles),
`samples` (top, packs, combos), `midi` (progressions, swing16, grooves), `masters`
(integratedLufs, truePeakDbtp, loudnessRangeLu, stereoWidthPercent, stereoCorrelation,
spectralCentroidHz, spectralTiltDbPerOct, spectralCurve), `localAssets` (template path).

Outside the studio the profile also helps describe the project: bios, playlist pitches,
genre/mood in distribution, video briefs, similar artists. Use SOUND.md's words for that.

## Errors

| Message | Do |
|---|---|
| no linked local folder | ask the user to link the artist folder (folder chip) or pass `output_folder` |
| denied / timed out approval | the user said no or didn't answer: ask before retrying |
| No .als found | check the folder with `local_list_dir`; projects may be one level deeper or on an unplugged drive |
| A build is already running | wait for that `job_id` |
| `ears_tenant_required` / Ears errors on masters | the profile is written without master targets; fix Ears and run again with only `masters` + the same `sets` |
