---
name: chatmu-studio-guide-vocal
description: >
  Use in Co-Producer (Chatmu Desktop + Ableton Live) when the user wants to
  HEAR lyrics sung on a melody before recording them: a rough guide vocal
  (voz guía) made on the user's Mac with the system voice and Chatmu Synth,
  put on a new audio track in Live. The melody comes from a MIDI clip in Live,
  a .mid file, or notes the agent writes. It is a sketch to try an idea, not a
  final vocal, and never the agent's own voice in the mix. Trigger phrases:
  "cántame esta letra", "cántame esta letra con esta melodía", "voz guía",
  "haz una voz guía", "que el sinte cante", "pon la letra en la melodía",
  "quiero oír cómo queda la letra", "canta esto", "guide vocal", "sing this",
  "sing these lyrics", "sing it on this melody", "scratch vocal", "melodía",
  "melody".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Guide vocal: hear lyrics sung on a melody (system voice + Chatmu Synth) on a new track in Live"
version: "1.0"
tags: ["studio", "ableton", "guide-vocal", "voz-guia", "lyrics", "letra", "melody", "chatmu-synth", "co-producer"]
requiresTools: ["local_sing", "local_ableton_snapshot", "local_ableton_get_notes", "local_ableton_arrangement", "local_music_theory", "local_ableton_transport", "local_doctor", "local_repair"]
---

# Chatmu Studio — Guide vocal ("el sinte canta")
**Version:** 1.0
**Requires:** Chatmu Desktop bridge + Chatmu Ears installed (its Python) + Chatmu Synth's renderer (ships with the app; beta: Apple silicon) + Ableton Live with «Permitir control» for the track. Without Live the WAV is still made.
**Related:** `chatmu-studio-melody-over-chords` and `chatmu-studio-compose-core` (write the melody first), `chatmu-studio-record` (record the real vocal over the guide), `chatmu-studio-synth`.

## What does this Skill do?

"Cántame esta letra con esta melodía" → `local_sing` makes a sung guide (one syllable per
note, the Mac's system voice shaped onto the melody played by Chatmu Synth, fully local) and
puts it on a NEW audio track called "Guide vocal" at the melody's start. The user hears how
the words sit on the melody, then records the real vocal.

Answer in the user's language. Short messages.

## HARD RULES

1. **It is a guide, not a vocal.** Robotic, recognisable syllables; say it plainly the first
   time ("es una voz guía para oír la idea, no una voz final; luego la grabas tú"). Never
   present it as a finished or releasable vocal, and never say it "stops being AI" or "isn't
   AI". Chatmu doesn't write the song: the lyrics and the melody are the user's.
2. **Never your own voice.** `local_sing` is not a way to talk to the user: your spoken
   replies in Chatmu Desktop stay out of the mix. Only sing lyrics the user gave or asked for.
3. **One syllable per note.** Count before calling: too few notes is an error that lists the
   syllables; extra notes are left out (no melisma yet). Chords sing their top note.
4. **Nothing is overwritten.** The WAV goes to the workspace's `Exports/Guide vocals/` with a
   new name; the track is new (the user approves it on screen).
5. **Never invent a cause.** Errors come with a code; use the table in Phase 4.

---

## Phase 0 — Find the melody (read only)

| Where the melody is | What to pass |
|---|---|
| A MIDI clip in Session | `track` + `clip` (read indexes with `local_ableton_snapshot`) |
| A MIDI clip on the Arrangement | `track` + `arrangement_clip` (index from `local_ableton_arrangement { action: "get_clips" }`) |
| A .mid file | `midi_path` (an ungranted folder → the app asks once) |
| Only in words ("do re mi…", "sube y baja") | write `notes` [{pitch, start_beats, duration_beats}] in the song's key (`local_music_theory` for the scale); confirm the melody with the user first |

Check the clip's notes with `local_ableton_get_notes` if unsure it is a single line. Count the
syllables (Spanish/English rules: "la-lu-na-se-fue", "you-are-my-sun-shine") against the notes.

## Phase 1 — Sing

`local_sing { lyrics, <melody>, lang?, bpm?, voice?, track_name?, at_beats? }`
- `lang`: "es" / "en" (guessed from the lyrics when left out).
- `bpm`: leave it out to use Live's tempo.
- `voice`: leave it out — it picks the best installed system voice (Premium/Enhanced first).
  If the user wants a better voice: macOS System Settings → Accessibility → Spoken Content →
  System voice → Manage voices, download a Premium/Enhanced Spanish or English voice.
- Takes ~5–30 s; one progress line to the user ("Preparando la voz guía…").

## Phase 2 — Explain the result (short)

| Field | Say |
|---|---|
| `wav` | where the guide is saved |
| `live.placed: true` | "Está en la pista **Guide vocal**, en el compás donde empieza la melodía. Dale play." |
| `live.placed: false` + `reason` | the WAV is saved; say why it isn't in Live (control off → «Permitir control»; Live closed) and offer to retry |
| `syllables` | how the lyrics were split, so the user can spot a wrong split |
| `melody.extra_notes_ignored` | notes left over at the end |
| `match.identified` | how many syllables the check recognised; don't present it as a quality grade |

## Phase 3 — Iterate

- Wrong split or stress → rewrite the lyrics the way they're sung (e.g. join or separate
  words) and sing again; a new WAV and a new track are made each time (old ones stay).
- Melody changes → edit the MIDI clip, then sing again.
- Play it with `local_ableton_transport` from the guide's start.

## Phase 4 — Errors

| Code | Meaning | Do |
|---|---|---|
| `too_few_notes` | fewer notes than syllables | add notes or shorten the lyrics; the message lists the syllables |
| `ears_missing` / `ears_incomplete` | Chatmu Ears' Python is not installed | `local_repair { action: "install_ears" }` (on-screen approval, ~260 MB) |
| `renderer_missing` | Chatmu Synth's renderer is missing | `local_repair { action: "install_synth" }`; if `local_doctor` doesn't offer it, this Mac's build has no synth and the guide isn't available |
| `sing_missing` | the app doesn't ship the guide-vocal script | Chatmu Desktop needs updating (not the user's fault) |
| `voice_not_found` | the `voice` given isn't installed | call again without `voice` |
| `timeout` | very long line | sing it by phrase or section |

## Don'ts

- Don't call it a final vocal, a clone of a singer, or "not AI".
- Don't sing your own replies or anything the user didn't ask to hear.
- Don't put the guide over an existing vocal track: it always goes on its own new track.
