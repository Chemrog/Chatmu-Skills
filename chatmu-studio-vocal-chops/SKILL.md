---
name: chatmu-studio-vocal-chops
description: >
  Use in Co-Producer (Chatmu Desktop + Ableton Live) to make vocal chops: cut
  a vocal take into syllables or short phrases, tune each piece to the song's
  key, build a melody or rhythmic hook from them and write the MIDI that
  triggers them (or place the pieces as audio clips). Finds the cut points and
  each piece's pitch with Chatmu Ears (audio → MIDI), sets clip markers and
  transpose in Live, and checks clicks and levels with Ears. Trigger phrases:
  "vocal chops", "haz chops de la voz", "corta la voz en pedazos", "trocea la
  voz", "chops de voz", "sílabas", "hazme un hook con la voz", "melodía con
  pedazos de voz", "samplea la voz", "chop the vocal", "vocal chop melody",
  "slice the vocal", "Simpler", "Drum Rack", "Ableton".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Vocal chops in Live: cut a take into syllables, tune each piece, write the MIDI melody that triggers them"
version: "1.0"
tags: ["studio", "ableton", "vocal-chops", "chops", "voz", "vocals", "sampling", "simpler", "co-producer"]
requiresTools: ["local_ableton_snapshot", "local_ableton_arrangement", "local_ableton_lom", "local_audio_to_midi", "local_ableton_get_notes", "local_ableton_delete_clip", "local_ableton_edit_track", "local_ableton_create_audio_clip", "local_ableton_clip", "local_ableton_rack", "local_ableton_device_params", "local_ableton_set_device_param", "local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_fire", "local_ableton_undo", "local_music_theory", "local_ears_listen"]
---

# Chatmu Studio — Vocal chops
**Version:** 1.0
**Requires:** Chatmu Desktop bridge + Ableton Live 12 (AbletonMCP patched Remote Script 1.10.0-chatmu; audio clips from files need Live 12.0.5+) + Chatmu Ears.
**Related:** `chatmu-studio-clone-sound` (audio → MIDI), `chatmu-studio-drum-rack` (pads), `chatmu-studio-compose-core` + `chatmu-studio-harmony-voicing` (the melody), `chatmu-studio-humanize`.

## What does this Skill do?

Takes a vocal take and turns it into an instrument: pieces (syllables, "ah", "hey", short
words), each tuned, played by MIDI notes or arranged as clips.

Answer in the user's language (usually Spanish). Show the chop list as a table.

## HARD RULES

1. **Live's API can't slice audio to a MIDI track.** Live's own "Slice to New MIDI Track" is
   a one-click user action (right-click the clip). Route A below uses it; route B needs no
   click. Say which one before starting.
2. **Find cut points with Ears, not by guessing:** `local_audio_to_midi` on the vocal gives
   one note per sung syllable (start, length, pitch). Monophonic vocals only; a stacked or
   very wet vocal gives approximate points — say so.
3. **The user's take is never modified.** Chops are new clips/tracks; work on copies.
4. **Tune with the key:** song key from the user or `local_music_theory { action:
   "detect_key" }`; target notes from `local_music_theory { action: "scale" }`. Transpose
   = target − detected pitch (semitones), keep within ±7 st or it sounds chipmunk-like
   (unless that's the effect).
5. **Never say slicing/markers/pads "are not exposed"** without `local_ableton_lom
   describe` on the clip / Simpler / pad first.

## Phase 0 — The take

- File (Descargas, attachment) → its `path`.
- A clip in Live → `local_ableton_lom { action: "get", path: "live_set tracks N clip_slots M
  clip", props: ["file_path", "name", "warping"] }` (Arrangement clips: `local_ableton_arrangement
  get_clips` for its index, then `local_audio_to_midi` can read it with `arrangement_clip`).
- Tempo/key: `local_ableton_snapshot`.

## Phase 1 — Find the syllables (Ears)

1. `local_audio_to_midi { path | track + clip/arrangement_clip, quantize: "off",
   instrument_hint: "voice", name: "Chop map" }` → a MIDI clip whose notes are the
   syllables (new MIDI track: on-screen approval).
2. `local_ableton_get_notes` on that clip → table: # · start (beats) · length · pitch (note
   name). Mark the 4–12 best pieces with the user (clear vowels, strong attacks, no breaths).
3. The "Chop map" clip is a helper: delete it when done
   (`local_ableton_delete_clip`, approval + clip name) or leave it muted — ask.

## Phase 2A — MIDI-triggered chops (one click by the user, recommended)

1. Put the take in a Session slot if it isn't (`local_ableton_create_audio_clip` on an
   audio track, empty slot). Ask the user: "clic derecho en el clip **<name>** → **Slice to
   New MIDI Track**, elige *Transient* o *1/8*". Live creates a MIDI track with a Drum Rack:
   one pad per slice, starting at C1 (MIDI 36).
2. `local_ableton_rack { action: "inspect" }` on that Drum Rack → which pad is which slice;
   match pads to the chop map by order.
3. Tune each chosen pad: `local_ableton_device_params { devicePath: "live_set tracks N
   devices 0 drum_pads <note> chains 0 devices 0" }` → set `Transpose` (or the name the read
   shows) with `local_ableton_set_device_param { devicePath, param, display: "+3 st" }`.
   Also shorten tails (decay/release in ms) and fade-ins if they click.
4. Write the melody/hook: `local_ableton_create_clip` + `local_ableton_write_notes` with the
   PAD notes (36 + slice index) in rhythm; the pitch comes from each pad's transpose. Humanize
   lightly.

## Phase 2B — Chops as audio clips (no click)

1. New audio track (`local_ableton_edit_track create_audio`, approval). For each chosen
   piece, `local_ableton_create_audio_clip` the same file into the next empty slot.
2. Per clip, `local_ableton_clip { action: "set" }`: `startMarker` / `endMarker` (beats from
   the chop map, warped to the Set's tempo: `warping: true`, `warpMode: "complex"` or
   `"beats"`), `looping: false`, `pitchCoarse` (the transpose), `name` ("Chop 3 · A4").
3. The "melody" is the order you fire/place them: audition with `local_ableton_fire`; to
   put them on the timeline use `chatmu-studio-session-vs-arrangement`.

## Ears verification

Play the hook (fire the clip, Live playing), solo the chops track,
`local_ears_listen { seconds: 6–8 }`: check defects (clicks at cut points), level jumps
between chops (short-term loudness), and that nothing is clipping. Fix tails/fades and
re-listen once. Pitch: the transposes come from Ears's note detection (Phase 1); the user's
ear confirms the melody — don't claim "afinado" from the numbers alone. If you couldn't
listen, say **"no verificado"**.

## Don'ts

- Don't edit the original vocal clip.
- Don't transpose pieces far beyond ±7 st without saying it changes the character.
- Don't claim the agent sliced to a MIDI track: that click is the user's.
