---
name: chatmu-studio-separate-stems
description: >
  Use in Co-Producer (Chatmu Desktop) when the user only wants the STEMS of a
  song they already have (separar stems, sacar las pistas, separar la voz,
  quitar la voz, acapella, instrumental, separar batería y bajo), locally on
  their Mac, without MIDI or rebuilding the song in Ableton. Splits any audio
  file (Descargas, Escritorio, a bounce) into drums, bass, vocals, guitar,
  piano and other with Demucs, writes one WAV per stem in a new folder, and
  can drop them into Live as audio tracks. Trigger phrases: "sácale los stems",
  "sepárame los stems", "separa la voz", "quítale la voz", "quiero el
  instrumental", "quiero la acapella", "separa la batería", "stems de esta
  canción", "split stems", "separate stems", "isolate the vocals".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Split a song into stems (drums, bass, vocals, guitar, piano, other) locally with Demucs"
version: "1.0"
tags: ["studio", "stems", "separar", "separation", "demucs", "vocals", "acapella", "instrumental", "co-producer"]
requiresTools: ["local_stems_separate", "local_repair", "local_doctor", "local_list_dir", "local_search_files", "local_ableton_edit_track", "local_ableton_create_audio_clip", "local_ableton_clip", "local_ableton_set_tempo", "local_ableton_tracks"]
---

# Chatmu Studio — Separate stems
**Version:** 1.0
**Requires:** Chatmu Desktop bridge on an Apple silicon Mac; the stem separation add-on (installed once with `local_repair`).
**Related:** `chatmu-studio-remake-song` (stems → MIDI + Chatmu Synth → Ableton set), `chatmu-studio-clone-sound`, `chatmu-studio-verify-ai`.

## What does this Skill do?

"Sácale los stems" → one WAV per instrument in a new folder, on the user's Mac. Nothing is
uploaded. Optionally places them in Live as audio tracks at the song's tempo.

Answer in the user's language (usually Spanish). Short messages; one progress line.

## HARD RULES

1. **Chatmu doesn't generate music.** It only processes audio the user already has.
2. **Never overwrite.** The tool always writes a new folder `<song> (stems)`.
3. **Say the limits up front, once:** separation isn't perfect (some bleed between stems);
   synths, strings, brass, flute, etc. all land in **other**; two instruments in the same
   range and timbre (e.g. violin and viola) don't separate well.
4. **Don't touch the Live set without asking** ("¿Los pongo en Live como pistas de audio?").

## Phase 1 — Find the file

The user names it or attaches it. If not, `local_search_files` / `local_list_dir` in
Descargas / Música. Formats: WAV, AIFF, FLAC, MP3, M4A, OGG, CAF.

## Phase 2 — Separate

`local_stems_separate { path, model? }`
- `htdemucs_6s` (default): drums, bass, other, vocals, guitar, piano.
- `htdemucs`: drums, bass, other, vocals — a bit cleaner when the user only wants
  voice/instrumental, drums or bass.
- Time: about a third to half of the song's length on the Mac's GPU (3-min song ≈ 1–1.5 min);
  the first use of `htdemucs` downloads its model (~80 MB).
- `status: "running"` + `job_id` → call again with `{ job_id }` until done. Say once: "Estoy
  separando los stems (≈1 min)". To stop: `{ job_id, cancel: true }`.

| Error code | Do |
|---|---|
| `stems_not_installed` | "Para separar stems en tu Mac necesito instalar un complemento (unos 500 MB, una sola vez, 1–2 min). ¿Lo instalo?" → yes → `local_repair { action: "install_stems" }` (the app asks for one click) → retry. |
| `stems_unavailable` | Intel Mac or old app: local separation isn't available; say so plainly. |
| `stems_busy` | another separation is running: wait for its `job_id`. |
| `model_download_failed` | connection problem on the first use of a model: retry later. |
| `out_of_memory` | retry with `model: "htdemucs"`, close heavy apps. |
| anything else | `local_doctor`, then report what it says. |

## Phase 3 — Report (short)

- The folder (`out_dir`) and each stem. Skip the ones with `silent: true` (listed in
  `empty_stems`, e.g. vocals of an instrumental): "no tiene voz".
- "Voz + instrumental": the instrumental is every non-vocal stem together; offer to place them
  in Live (they add up to the mix) rather than inventing a mixdown.
- Tempo: `tempo.bpm` (estimate). If `confidence` < 0.5, say it's approximate and offer the
  `half` / `double` alternative when the genre suggests it.

## Phase 4 — (Optional, after asking) Into Live

1. `local_ableton_set_tempo { bpm: tempo.bpm }` (only if the user agrees to change the set's tempo).
2. Per non-silent stem: `local_ableton_edit_track { action: "create_audio" }` → read the new index
   with `local_ableton_tracks` → `local_ableton_edit_track { action: "rename", index, name }` →
   `local_ableton_create_audio_clip { trackIndex, clipIndex: 0, path }`.
3. Keep them in sync: `local_ableton_clip` set `warping=false` on every stem clip (they are
   already at the song's speed; warping with guessed markers would drift them apart).

## Don'ts

- Don't promise studio-quality multitracks. Don't upload the song anywhere for separation.
- Don't say the stems "remove" authorship or AI traces — they are the same audio, split.
