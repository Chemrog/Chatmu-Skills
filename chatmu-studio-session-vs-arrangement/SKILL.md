---
name: chatmu-studio-session-vs-arrangement
description: >
  Use in Co-Producer when you need to know WHERE the music is in Ableton Live
  (Session view clips vs Arrangement timeline) and how to play it, move it or
  put it on the timeline. Trigger phrases: "Session", "Arrangement", "vista
  Session", "vista Arrangement", "arreglo", "línea de tiempo", "timeline",
  "dónde está la música", "dónde están los clips", "lanza la escena", "pasa los
  clips al arreglo", "Back to Arrangement", "no suena el arreglo", "where are
  my clips", "launch the scene".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Tell Session from Arrangement in Ableton and play, launch or move the music correctly"
version: "1.0"
tags: [studio, ableton, session, arrangement, co-producer]
requiresTools: ["local_ableton_snapshot", "local_ableton_fire", "local_ableton_transport", "local_ableton_arrangement"]
---

# Chatmu Studio — Session vs Arrangement
**Version:** 1.0
**Requires:** Chatmu Desktop (Co-Producer) bridge + Ableton Live.

## The two places music can live

| | Session view | Arrangement view |
|---|---|---|
| What | Grid of **clip slots**: tracks are columns, **scenes** are rows | A **timeline** per track, positions in beats/bars |
| How it plays | You **launch** a clip or a scene; it loops | The **transport** plays from a position |
| Tools | `local_ableton_fire` (`clip` / `scene` / `stop_all_clips`), `local_ableton_stop_clip` | `local_ableton_transport` (`play` + `fromBeat`, `stop`, `continue`), `local_ableton_song` (loop, loopStart, loopLength) |
| Read | snapshot → clip slots (name, length, `is_playing`) | snapshot → arrangement clips, or `local_ableton_arrangement` `get_clips` (start/end beats) |

Key facts:
- **Everything the agent composes lands in Session.** `local_ableton_create_clip` and
  `local_ableton_write_notes` work on Session clip slots (`trackIndex` + `clipIndex`
  = scene row). To hear it: fire the clip or its scene.
- **A launched Session clip overrides that track's Arrangement.** Live then shows the
  "Back to Arrangement" button lit. To hear the timeline again use
  `local_ableton_arrangement` `{ action: "back_to_arranger" }`.
- **Firing a clip starts the transport**; stopping the transport stops clips.
- `local_ableton_song` `position` is ignored while Live is stopped; to start at a
  position always use `local_ableton_transport` `{ action: "play", fromBeat }`.
- Beats vs bars (4/4): bar N starts at beat `(N - 1) * 4`. Bar 1 = beat 0, bar 9 = beat 32.

## How to decide where the music is

1. `local_ableton_snapshot`.
2. Count Session clips (slots with `has_clip`) and arrangement clips per track.
3. Decide:
   - Only arrangement clips → "your song is on the timeline (bars X–Y)". Play with fromBeat.
   - Only Session clips → "your ideas are in Session, scene rows N…". Fire the scene.
   - Both → say both, ask which one the user means if it matters.
   - A Session slot with `is_playing` while the user expects the Arrangement →
     that is why the timeline is not heard: `back_to_arranger`.

## Moving Session ideas onto the timeline

`local_ableton_arrangement` `{ action: "duplicate_from_session", trackIndex, clipIndex, beats }`
copies one Session clip to the same track's timeline at `beats`. It **replaces**
whatever is in that range and asks the user for approval. Before calling it:
- read `get_clips` for that track to see what would be overwritten;
- tell the user the plan ("Chords → bars 1–8, Drums → bars 1–8").

Use `create_locator` to mark sections ("Intro" at beat 0, "Drop" at beat 64) and
`show` to bring the Arrangement view to the front for the user.

## Don'ts

- Don't say "the song is empty" because the Arrangement is empty — check Session.
- Don't fire `stop_all_clips` to "reset" without telling the user; it stops their jam.
- Don't assume scene index = bar number. Scenes are rows, not time.
