---
name: chatmu-studio-record
description: >
  Use in Co-Producer when the user wants to record in Ableton Live: count-in,
  arm a track, record into Session or Arrangement, MIDI record quantization,
  overdub, stop recording, or Capture MIDI ("I just played something good").
  Trigger phrases: "graba", "grabar", "record", "cuenta y graba", "count in",
  "cuenta 4", "arma la pista", "arm the track", "deja de grabar", "stop
  recording", "capture MIDI", "captura lo que toqué", "overdub", "Session",
  "Arrangement".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Record in Ableton with count-in, arming, quantization and Capture MIDI"
version: "1.0"
tags: [studio, ableton, record, grabar, co-producer]
requiresTools: ["local_ableton_record", "local_ableton_tracks", "local_ableton_snapshot"]
---

# Chatmu Studio — Record
**Version:** 1.0
**Requires:** Chatmu Desktop (Co-Producer) bridge + Ableton Live (AbletonOSC).

## The tool

`local_ableton_record` with `action`:

| action | What it does | Approval |
|---|---|---|
| `start` | optional arm of `trackIndex`, optional MIDI record `quantization`, metronome during a count-in of `countInBars` (0–4, default 1), then records | **every call** (destructive: new material) |
| `stop` | stops recording; `stopTransport` (default true) also stops playback; restores arm / quantization / overdub the bridge changed | no |
| `capture_midi` | Live's Capture MIDI: turns what the user just played on an armed/monitored MIDI track into a clip; `mode` picks the destination | no |

Parameters for `start`: `mode` `"session"` (default: records a new clip in the armed
track's slot) or `"arrangement"` (records on the timeline; count-in pre-rolls before the
playhead when there is room), `trackIndex`, `countInBars`, `quantization`
(`none`, `1/4`, `1/8`, `1/8T`, `1/8+1/8T`, `1/16`, `1/16T`, `1/16+1/16T`, `1/32`),
`overdub` (arrangement only, MIDI Arrangement Overdub), `metronome` (default true; it is
put back to its previous state when recording starts).

## Flow

1. **Ask the essentials in one line:** which track, Session or Arrangement, count-in bars,
   quantize or not. Defaults: Session, 1 bar count-in, no quantization.
2. **Find the track:** `local_ableton_tracks` (index, name, arm state). For MIDI, make
   sure the track has an instrument (snapshot devices); for audio, that the input is set
   (the user does that in Live — the tools cannot change track inputs).
3. **Session mode:** the clip goes into the slot Live picks for the armed track (the
   selected or first empty one). If the user wants a specific scene row, ask them to select
   it, or tell them where it landed afterwards (snapshot).
4. **Arrangement mode:** recording starts at the playhead. To record from bar N, tell the
   user, and use `overdub: true` only if they want to add to existing MIDI there.
5. **Start:** `local_ableton_record` `{ action: "start", mode, trackIndex, countInBars, quantization }`.
   The user approves on screen; tell them "aprueba en la app y toca después de la cuenta".
6. **Stop** when the user says so: `{ action: "stop" }` (or `stopTransport: false` to
   keep playing).
7. **Check the take:** snapshot or `local_ableton_get_notes` on the new clip; offer to
   humanize/quantize (`chatmu-studio-humanize`), loop it, or listen
   (`chatmu-studio-listen-troubleshooting`).

## Capture MIDI ("what I just played")

If the user played something without recording: `{ action: "capture_midi" }`. It only
works if the MIDI track was armed or monitoring while they played. If nothing is captured,
say so plainly — don't invent a cause.

## Cancel / mistakes

- To abort: `{ action: "stop" }`, then offer `local_ableton_undo` `{ action: "undo" }` to
  remove the take (say what will be undone).
- If the start fails (approval denied, control disabled, Live stopped during the count-in),
  the bridge restores what it changed and stops the transport if it started it. Report the
  error text as returned.

## Don'ts

- Don't arm several tracks unless asked.
- Don't start recording without the user knowing it's about to happen.
- Don't leave recording running: always confirm it was stopped.
