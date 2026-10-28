---
name: chatmu-studio-remake-song
description: >
  Use in Co-Producer (Chatmu Desktop) when the user wants to REMAKE / REOPEN a
  song they already have as an editable Ableton Live project: any audio file
  (an old master with no sessions, a demo, a sketch) → stems → MIDI + Chatmu
  Synth presets that clone each instrument's timbre → a Live set with one
  track per instrument, the right tempo, and vocals as an audio guide. Also
  for remixes and live versions that need the parts separated. Trigger
  phrases: "rehaz esta canción", "rehacer canción", "pásala a multitrack",
  "ábreme esta canción en Ableton", "sácale los stems a MIDI", "tengo solo el
  máster de una canción vieja", "quiero editar esta canción", "conviértela en
  proyecto", "remake this song", "song to multitrack", "stems to MIDI".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Remake a song as an editable Live set: stems, MIDI + Chatmu Synth clones, tempo, vocals as audio"
version: "1.0"
tags: ["studio", "remake", "rehacer", "stems", "multitrack", "audio-to-midi", "chatmu-synth", "clone", "ableton", "co-producer"]
requiresTools: ["local_stems_separate", "local_synth_clone", "local_audio_to_midi", "local_synth_status", "local_ableton_set_tempo", "local_ableton_edit_track", "local_ableton_tracks", "local_ableton_load_device", "local_ableton_create_audio_clip", "local_ableton_clip", "local_ableton_mixer", "local_ableton_color", "local_ableton_group_tracks", "local_ableton_snapshot", "local_repair", "local_doctor"]
---

# Chatmu Studio — Remake a song (audio → stems → MIDI + Chatmu Synth → Live set)
**Version:** 1.0
**Requires:** Chatmu Desktop bridge on an Apple silicon Mac, Ableton Live with control enabled,
Chatmu Ears (timbre clone), Chatmu Synth (VST3), the stem separation add-on.
**Uses:** `chatmu-studio-separate-stems` (Phase 1), `chatmu-studio-clone-sound` (Phase 3 details),
`chatmu-studio-verify-ai` (optional before/after measurement).

## What does this Skill do?

"Rehaz esta canción" + a file → a Live set the musician can edit: the song's tempo, one track
per instrument (Chatmu Synth playing MIDI that follows the original, with a preset cloned from
that stem), drums and vocals as audio, everything grouped. The value is **control and
editability**: getting a song out of a closed MP3.

Answer in the user's language (usually Spanish). Short messages: one line per phase.

## HARD RULES

1. **Chatmu does NOT generate music.** It only processes audio the user already has. Never
   offer to compose or "fill in" parts.
2. **Positioning.** Never say or imply the result "stops being AI", "is no longer AI", "is now
   human" or "is now yours" for rights or distribution. If the song came from an AI tool, the
   composition still came from it; remaking it gives editability, not authorship. AI detector
   questions → `chatmu-studio-verify-ai`.
3. **Ask ONCE before touching the Live set**, with the plan (Phase 2). Without a yes, stop
   after the stems.
4. **Never overwrite**: stems go into a new folder; clones are saved as new presets; tracks are
   appended at the end of the set. Recommend an empty set ("abre un set nuevo en Live").
5. **Report honestly**: what is MIDI, what stayed audio, the per-stem similarity score, and
   what came out approximate. Never "suena idéntico".
6. **Vocals are never synthesized**: they stay as an audio guide; suggest re-recording.
7. One long job at a time (separation, then one clone after another).

---

## Phase 0 — Preflight (read only)

- The file: the user names/attaches it (WAV, AIFF, FLAC, MP3, M4A…).
- `local_ableton_snapshot` → Live reachable and control enabled; note the current track count.
- `local_synth_status` → Chatmu Synth installed? If not: `local_repair { action: "install_synth" }`
  (approval; Live must rescan plug-ins). Without it, the plan falls back to "MIDI only + stems
  as audio" (say so).
- If any tool fails: `local_doctor` → the repair it names.

## Phase 1 — Stems + tempo

`local_stems_separate { path }` (default `htdemucs_6s`). Resume with `{ job_id }` while
`running`. Not installed → offer `local_repair { action: "install_stems" }` (≈500 MB once).
Keep: each stem's `path`, `silent`, `rms_db`; and `tempo` (bpm, confidence, half, double).
Drop every `silent` stem from the plan.

## Phase 2 — Plan + the ONE confirmation

Default treatment per stem:

| Stem | Track | How |
|---|---|---|
| drums | audio | the stem as is (exact groove). Optional rhythm guide: `local_audio_to_midi { path, instrument_hint: "drums" }` → one note per hit, approximate (Ears doesn't tell kick/snare/hat apart). For a Drum Rack: in Live, right-click the clip → "Slice to New MIDI Track" (the user does it; there is no API). |
| bass | MIDI + Chatmu Synth | clone (`instrument_hint: "bass"`) → preset + MIDI |
| guitar, piano | MIDI + Chatmu Synth | clone (`"guitar"` / `"piano"`): the plucked recipe models the hit, the MIDI is the strongest line (approximate for chords) — keep the stem as a muted audio reference |
| other | MIDI + Chatmu Synth | clone with the user's word for what it is ("synth lead", "flute", "strings"…); mixed instruments clone poorly → keep the stem as audio too |
| vocals | audio | guide track, never synthesized |

Tempo: `tempo.bpm` → set it. If `confidence` < 0.5 or the genre suggests otherwise, ask
("¿la canción va a 86 o a 172?") using `half`/`double`.

Say it in 3–5 lines, e.g.: "Voy a poner el set a 97 BPM y crear: Batería (audio), Bajo (Chatmu
Synth + MIDI), Guitarra (Chatmu Synth + MIDI, aproximado: son acordes), Voz (audio guía), todo en
un grupo. Tarda ≈3–5 min. ¿Lo hago?" — and wait for yes.

## Phase 3 — Build the set (after yes)

Order matters: **tempo first** (MIDI positions are computed from seconds at the set's tempo).

1. `local_ableton_set_tempo { bpm }`.
2. **Audio tracks** (drums, vocals, and the reference copies): `local_ableton_edit_track
   { action: "create_audio" }` → `local_ableton_tracks` for the new index → rename (e.g.
   "Batería (stem)", "Voz (guía)") → `local_ableton_create_audio_clip { trackIndex, clipIndex: 0,
   path }` → `local_ableton_clip` set `warping=false` (they are already at the song's speed;
   unwarped, everything stays in sync). Reference copies: mute them with `local_ableton_mixer`.
3. **Synth tracks**, one stem at a time:
   1. `local_synth_status` → remember the open instances' ports.
   2. `local_ableton_edit_track { action: "create_midi" }`, rename it ("Bajo"), then
      `local_ableton_load_device { trackIndex, name: "Chatmu Synth" }`.
   3. `local_synth_status` again → the NEW port is this track's instance.
   4. `local_synth_clone { path: <stem>, instrument_hint, port, track, name: "<Song> <Part>" }`
      → loads the "(play)" preset, saves it in the user's library, writes the MIDI on that track.
      Resume with `{ job_id }` while `running`. Keep `score`, `recipe`, `model`, `midi`.
   5. If the clone fails or `score.final` < 35: keep the stem as audio on that track's place and
      mark it "audio" in the summary (don't retry more than once).
   Without Chatmu Synth: `local_audio_to_midi { path, instrument_hint }` (new MIDI track) and the
   stem as audio; the user picks an instrument.
4. **Group**: `local_ableton_group_tracks` with the new tracks ("<Song> — rehecha"). It's
   experimental (needs «Organizar pistas en Live»); if unavailable, color them with
   `local_ableton_color` instead and say so.

## Phase 4 — Summary (always)

A short table, one row per stem:

| Track | Type | Detail |
|---|---|---|
| Bajo | MIDI + Chatmu Synth | preset "Song Bass Clone (play)", parecido 61/100, 142 notas |
| Guitarra | MIDI + Chatmu Synth | parecido 48/100 — MIDI aproximado (acordes) |
| Batería | audio | stem original |
| Voz | audio (guía) | regrábala para hacerla tuya |

Then: score scale (50–70 good clone, > 70 very close, < 45 rough approximation — say why:
chords, mixed instruments, reverb), where the stems and presets are saved, what to tweak next
(`chatmu-studio-clone-sound` Phase 4: brillo, ataque, aire…), and that `expression.mid` has the
pitch bends/vibrato Live's API can't write.

## Known limits (say when relevant, never hide)

- Separation leaves some bleed; synths/strings/brass all come together in "other".
- MIDI is monophonic per track: chords come out as their strongest line or rhythm.
- Drums stay audio in v1 (no kick/snare/hat transcription).
- Vocals are not resynthesized.
- Not in v1: text-queried separation of specific instruments, MIDI with expression in Live,
  automatic EQ/reverb matching.

## Don'ts

- Don't touch Live before the confirmation. Don't delete or replace existing tracks.
- Don't upload the song anywhere (everything runs on the Mac; only `chatmu-studio-verify-ai`
  sends audio out, and only with the user's OK).
- Don't name the project Chatmu Synth derives from.
