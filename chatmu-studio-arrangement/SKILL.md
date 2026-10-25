---
name: chatmu-studio-arrangement
description: >
  Use in Co-Producer (Chatmu Desktop + Ableton Live) to read and improve the
  structure of a song in the Arrangement: reads the clips per track and the
  locators, proposes the section map (intro, verso, pre-coro, coro, puente,
  drop, outro) in bars, measures the energy curve per section (loudness with
  Chatmu Ears + density of active tracks), and suggests transitions (risers,
  fills, quitar elementos, drops, cambios) where the energy doesn't move. Only
  proposes; applies (locators, fills, risers) with the user's OK. Trigger
  phrases: "cómo está la estructura", "¿cómo está la estructura de mi
  canción?", "revisa el arreglo", "arreglo", "estructura", "secciones", "mapa
  de la canción", "pon los locators", "marca las secciones", "se siente plana",
  "no crece", "le falta un cambio", "el coro no explota", "es muy larga",
  "transiciones", "song structure", "arrangement review", "sections", "the
  song feels flat", "Arrangement", "Ableton".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Song structure in Live's Arrangement: section map in bars, energy curve per section, transition ideas"
version: "1.0"
tags: ["studio", "ableton", "arrangement", "arreglo", "estructura", "structure", "sections", "energy", "co-producer"]
requiresTools: ["local_ableton_snapshot", "local_ableton_arrangement", "local_ableton_tempo_map", "local_ableton_status", "local_ableton_transport", "local_ableton_song", "local_ears_listen", "local_ears_analyze_file", "local_ears_render", "local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_undo", "local_ableton_lom"]
---

# Chatmu Studio — Arrangement structure
**Version:** 1.0
**Requires:** Chatmu Desktop bridge + Ableton Live + Chatmu Ears.
**Uses:** `chatmu-studio-genre-templates` (typical lengths per genre), `chatmu-studio-drop-buildup` (risers, drops), `chatmu-studio-automation`, `chatmu-studio-drums-by-genre` (fills), `chatmu-studio-session-vs-arrangement`, `chatmu-studio-listen-troubleshooting`.

## What does this Skill do?

"¿Cómo está la estructura?" → a map of the song in bars, an energy curve you can explain,
and 2–4 concrete ideas where the song stays flat. **It proposes; it never rewrites the
arrangement without an OK.**

Answer in the user's language (usually Spanish). A table for the map, short lines for ideas.

## HARD RULES

1. **Bars, not seconds.** Tempo may change (`local_ableton_tempo_map`). In 4/4, bar N starts
   at beat `(N − 1) × 4`. Show bars ("coro: compases 33–48").
2. **The music must be in the Arrangement.** If it lives only in Session, say so and offer
   `chatmu-studio-session-vs-arrangement` first.
3. **Energy = numbers + density, never a guess.** Loudness per section from Ears (relative,
   same method for every section) + count of tracks with clips in that section.
4. **Propose, then OK, then apply.** Writes here are few and visible: locators, a fill or
   riser clip on a NEW or empty track. Never delete or overwrite the user's clips without an
   explicit OK and approval.
5. **Live's API limits, said once:** arrangement clips can't be moved or split by the tools
   (Live's `start_time` is read-only and there is no split), and track automation in the
   Arrangement can't be written (see `chatmu-studio-automation`). "Quitar elementos" in the
   timeline is the user's cut (Cmd+E) or a muted copy — say it, don't pretend.
6. **Never say something "is not exposed"** without `local_ableton_lom describe` on the
   object first.

---

## Phase 0 — Read (no writes)

1. `local_ableton_snapshot` → tracks, arrangement summary, locators, tempo, time signature.
2. For tracks whose summary isn't enough: `local_ableton_arrangement { action: "get_clips",
   trackIndex }` → clip names, start/end in beats.
3. `local_ableton_tempo_map` → tempo changes (reads the last saved .als; ask for Cmd+S if
   `unsavedChanges`).
4. Ask the genre if it isn't obvious (it sets typical lengths; `chatmu-studio-genre-templates`).

## Phase 1 — Section map

Build sections from: existing locators (trust their names), clip boundaries that many tracks
share, entries/exits of the drums, bass and vocals, repeated clip names.

| # | Sección | Compases | Largo | Pistas activas | Entra / sale |
|---|---|---|---|---|---|
| 1 | Intro | 1–8 | 8 | 3 | pad, FX |
| 2 | Verso 1 | 9–24 | 16 | 6 | + batería, bajo, voz |
| 3 | Coro 1 | 25–40 | 16 | 9 | + synths, coros |

Mark doubts with "?" and ask; don't name a section "puente" because it's in the middle.
Compare lengths with the genre (e.g. reggaetón verse 16 / chorus 8–16; house intro 16–32
for DJs; pop chorus by ~0:45–1:00). Flag: an intro longer than the genre allows, a first
chorus after ~1:15 in pop, sections of odd length that don't feel intentional.

## Phase 2 — Energy curve (Ears)

Pick ONE method and use it for every section:

- **From a file (preferred if a full export exists):** `local_ears_analyze_file
  { path, tool: "loudness" }` + `local_ears_render { captureId, view: "loudness" }` for the
  curve; read the level inside each section's time range (convert bars to seconds with the
  tempo map).
- **From the stream (no export):** for each section, `local_ableton_transport { action:
  "play", fromBeat: <section start + 4 beats> }` → `local_ears_listen { seconds: 6–8 }`, one
  at a time. Indicative values, valid for comparing sections with each other. Stop playback
  at the end and restore the playhead/loop if you changed them.

Energy table: section · LUFS (relative) · active tracks · low end present? · verdict.
Rules of thumb: the chorus/drop should be ~2–4 LU above the verse and have more (or
different) elements; a pre-chorus/build should rise; the section after a peak should drop.
**Flat** = two consecutive contrasting sections within ~1 LU and the same tracks.

## Phase 3 — Proposals (2–4, biggest impact first)

Each: where (bars) · what's wrong (number) · idea · how it would be done.

| Problema | Ideas |
|---|---|
| Verse → chorus doesn't lift | remove kick/bass the last bar before the chorus; riser + white-noise sweep over 4–8 bars; add a layer (coros, octave synth) only in the chorus |
| Chorus 2 = chorus 1 | add a counter-melody or percussion layer; double the vocal |
| Long intro | cut to 4–8 bars (radio) or keep 16–32 (DJ edit): ask what it's for |
| No contrast before the end | a bridge/break of 8 bars with half the elements |
| Abrupt section change | a drum fill in the last bar (`chatmu-studio-drums-by-genre`), a crash on bar 1 |
| Electronic drop without impact | `chatmu-studio-drop-buildup` |

## Phase 4 — Apply (with OK)

- **Locators:** `local_ableton_arrangement { action: "create_locator", beats, name }` for
  every section (non-destructive; offer it first — it helps the user and every other skill).
- **Fills / risers as MIDI:** write them in a Session clip on a NEW track
  (`local_ableton_create_clip` + `local_ableton_write_notes`), then place it with
  `local_ableton_arrangement { action: "duplicate_from_session", trackIndex, clipIndex,
  beats }` (approval: it replaces that range on that track — use an empty track).
- **Removing elements, automation sweeps:** tell the user exactly what to cut where
  (rule 5), or use the clip-envelope routes in `chatmu-studio-automation`.
- Undo: `local_ableton_undo` (say what is undone).

## Ears verification

After applying, measure the changed transition again with the same method as Phase 2 (same
sections, same seconds) and report "verso → coro: +0.6 → +2.8 LU". If you couldn't listen
(nothing playing, Ears unavailable, plugin missing — see
`chatmu-studio-listen-troubleshooting`), say **"no verificado"** and keep the proposal as a
proposal.

## Don'ts

- Don't rename sections by position alone; ask when unsure.
- Don't move or delete the user's clips.
- Don't give energy claims without measuring every section the same way.
