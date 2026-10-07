---
name: chatmu-studio-listen-troubleshooting
description: >
  Use in Co-Producer (Chatmu Desktop + Ableton Live) BEFORE and AFTER listening
  to the user's session with Chatmu Ears, and whenever a capture comes back
  silent. Checklist: is Live playing, where is the playhead vs where the clips
  are, is the music in Session or Arrangement, mute/solo, is the Co-Producer
  Audio plugin on the Master. Trigger phrases: "escucha", "escuchar", "escucha
  mi sesión", "qué suena", "no suena", "no se escucha", "silencio", "no oigo
  nada", "dale play", "listen", "listen to my track", "it's silent", "nothing
  plays", "silent_capture", "Session", "Arrangement", "Ableton".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Listen to the Ableton session reliably: play from the music, Session vs Arrangement, silent captures"
version: "1.0"
tags: [studio, ableton, ears, listen, escuchar, troubleshooting, co-producer]
requiresTools: ["local_ableton_status", "local_ableton_snapshot", "local_ableton_transport", "local_ears_listen", "local_ears_ensure_plugin"]
---

# Chatmu Studio — Listen & Troubleshoot
**Version:** 1.0
**Requires:** Chatmu Desktop (Co-Producer) with the local bridge, Ableton Live, Chatmu Ears.

## What does this Skill do?

It makes "listen to my session" work the first time, and stops you from inventing
explanations when it does not. Ears only hears what Live is actually outputting to
the Master, through the **Co-Producer Audio** plugin. Silence almost always means one
of five boring things: Live is stopped, the playhead is past the music, the music is
in the other view, tracks are muted/soloed, or the plugin is missing.

Answer the user in their language (usually Spanish). Keep it short.

## HARD RULES

1. **Never invent a cause.** No "version error", "protocol mismatch", "bridge bug",
   "incompatible Live version" unless a tool literally returned that text. A
   `silent_capture` result is a VALID result: Ears worked and heard silence.
2. **Diagnose with tools, then retry ONCE.** If the second capture is still silent,
   stop and tell the user what you checked and what you need from them.
3. **One listen at a time.** Never call `local_ears_listen` in parallel.
4. Do not change mute/solo, load devices or move clips without saying so first;
   loading the plugin needs the user's on-screen approval anyway.

## CHECKLIST BEFORE LISTENING (run it every time)

1. **Read the set in one call:** `local_ableton_snapshot` (default options). From it note:
   - per track: mute / solo / arm, and which Session clip slots have clips and which
     are `is_playing`;
   - the **arrangement clips** (start/end in beats) — the first and last beat with music;
   - tempo and time signature (to convert bars to beats: in 4/4, bar N starts at
     beat `(N - 1) * 4`).
2. **Where does the music live?** (details in `chatmu-studio-session-vs-arrangement`)
   - Arrangement clips exist and no Session clip is playing → plan to play the Arrangement.
   - Only Session clips exist → you must fire a clip or scene (`local_ableton_fire`).
   - Both → ask, or prefer what the user just worked on. If a Session clip is
     playing on a track, that track ignores its Arrangement until
     `local_ableton_arrangement` action `back_to_arranger`.
3. **Mute / solo:** if any track is soloed, only soloed tracks sound. If the tracks
   with music are muted, tell the user and offer to unmute (`local_ableton_mixer`
   property `mute`, `on: false`).
4. **Plugin on the Master:** `local_ears_ensure_plugin` with `install: false` (check
   only). If missing, explain and offer to load it (`install: true` asks for approval).
5. **Start playback WHERE THE MUSIC IS:**
   - Arrangement: `local_ableton_transport` `{ action: "play", fromBeat: <first beat with music, usually 0> }`.
     A plain `play` starts from Live's start marker / current playhead, which may be
     past the end of the song (e.g. playhead at bar 42, music ends at bar 21 → silence).
   - Session: `local_ableton_fire` `{ action: "scene", sceneIndex }` or
     `{ action: "clip", trackIndex, clipIndex }`.
6. **Confirm it is playing:** `local_ableton_status` → `isPlaying: true` and
   `currentSongTimeBeats` inside the range that has clips.
7. **Listen:** `local_ears_listen` `{ seconds: 8–20 }`. Keep the capture shorter than
   the remaining music (if the music ends 6 s after fromBeat, listen 6 s or loop it).

## AFTER A `silent_capture`

Run these in order, stop at the first one that explains it, fix it, retry ONCE:

| Check | Tool | Fix |
|---|---|---|
| Live stopped | `local_ableton_status` (`isPlaying`) | play / fire (step 5) |
| Playhead outside the music | `local_ableton_status` (`currentSongTimeBeats`) vs arrangement clip ranges from the snapshot | `local_ableton_transport` play with `fromBeat` at the first clip |
| Music only in Session, nothing launched | snapshot clip slots | `local_ableton_fire` scene/clip |
| Session clip overriding Arrangement | snapshot `is_playing` on Session slots | `local_ableton_arrangement` `back_to_arranger`, then play fromBeat |
| Muted / other track soloed | snapshot or `local_ableton_tracks` | ask, then `local_ableton_mixer` |
| Plugin missing / not streaming | `local_ears_ensure_plugin` `install:false` | offer `install:true` (approval) |
| Clip is empty (no notes) | `local_ableton_get_notes` | write notes or pick another clip |
| Instrument missing on a MIDI track | snapshot devices per track | offer `local_ableton_load_device` |

If everything checks out and it is still silent, say exactly that: "Live is playing
at bar X, tracks A/B have clips there, the plugin is on the Master, but Ears hears
silence. Can you check the Master volume / that you hear sound in your speakers?"

If a `plugin_not_streaming` error comes back: the plugin is missing or Live is not
playing — use step 4 and step 6.

## Reporting what you heard

Describe the music from the Ears analysis (loudness, spectrum, stereo, defects) in
plain words, and name the section you played ("bars 1–8 of the Arrangement"). Do not
claim you heard instruments the analysis cannot identify; say what the numbers show.
