---
name: chatmu-studio-song-structure
description: >
  Use in Co-Producer whenever a song needs a FORM: planning the sections of a
  new track (intro, verse, pre-chorus, chorus, bridge, drop, outro), building
  it in Ableton Live as named scenes (Session) or locators (Arrangement),
  reading where each section of an existing song is, and moving to a section
  to play or record ("from the chorus, one bar early, with click"). Also the
  storytelling: energy per section and what enters or leaves. Trigger phrases:
  "estructura", "estructura de la canción", "song structure", "arma la
  canción", "hazme una canción completa", "intro", "verso", "pre-coro",
  "precoro", "coro", "puente", "drop", "outro", "secciones", "partes de la
  canción", "córrela desde el coro", "desde el verso", "graba desde el coro",
  "locators", "marcadores", "escenas", "Session", "Arrangement", "arrangement".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Plan and build song form in Ableton: sections, bars, energy, scenes, locators, jump/record from a section"
version: "1.0"
tags: [studio, ableton, structure, estructura, arrangement, arreglo, session, scenes, locators, co-producer]
requiresTools: ["local_ableton_snapshot", "local_ableton_edit_track", "local_ableton_scene_name", "local_ableton_fire", "local_ableton_arrangement", "local_ableton_transport", "local_ableton_song", "local_ableton_record"]
---

# Chatmu Studio — Song structure
**Version:** 1.0
**Requires:** Chatmu Desktop (Co-Producer) bridge + Ableton Live.
**Related:** `chatmu-studio-genre-templates` (bar counts per genre), `chatmu-studio-session-vs-arrangement`
(where clips live, moving them to the timeline), `chatmu-studio-record` (count-in, quantization),
`chatmu-studio-melody-over-chords` (what to write inside each section).

## Why this skill exists

"Hazme un trap" is not a loop. A song is a sequence of sections with a story: something
is presented, repeated, varied, lifted and resolved. If you write 8 bars and stop, you made
an idea, not a song. **Plan the form before writing notes**, build it so the user (and you,
later) can see it in Live, and use it to navigate.

## 1. Vocabulary (say it in the user's language)

| ES | EN | Job |
|---|---|---|
| Intro | Intro | Sets tempo, sound world and expectation. Often the chorus chords or hook, thinned out |
| Verso | Verse | Tells the story; lower energy, room for the vocal; lyrics change, music repeats |
| Pre-coro / Pre | Pre-chorus / Build | Tension: new chord or harmonic rhythm speeds up, elements drop out, risers |
| Coro / Hook | Chorus / Hook | The point of the song: highest energy, the melody people remember, repeats unchanged |
| Post-coro | Post-chorus | Instrumental or vocal-chop answer to the chorus (pop, reggaetón, EDM) |
| Puente | Bridge | Contrast once, late in the song: new chords, half-time, stripped, or a key change |
| Drop | Drop | EDM/house/dubstep "chorus": the full groove after a build |
| Break / Breakdown | Breakdown | Energy dip before a build/drop |
| Interludio | Interlude | Short instrumental bridge between sections |
| Outro | Outro | Exit: chorus fading, intro mirror, or a DJ-friendly drum tail |

## 2. The math of form

- **Sections are made of phrases of 4 bars**; sections are 4, 8 or 16 bars (sometimes 2, 12,
  24 or 32). Odd lengths are deliberate effects (a 2-bar pickup, one extra bar of silence
  before the drop) — never accidents.
- This holds in any meter: in **3/4** (waltz, some corridos and ballads) bars still group
  in 2, 4, 8 and 16; in 6/8 likewise.
- **Beats per bar** = `numerator × 4 / denominator` (4/4 → 4, 3/4 → 3, 6/8 → 3, 7/8 → 3.5).
- **Bar N starts at beat** `(N − 1) × beatsPerBar`. Section starts are cumulative: if the
  Intro is 8 bars in 4/4, Verso 1 starts at beat 32 (bar 9).
- **Duration:** seconds per bar = `beatsPerBar × 60 / BPM`. A 3-minute song at 90 BPM in 4/4
  is ≈ 67 bars; at 128 BPM ≈ 96 bars. Use it to check a plan against the length the user wants.
- Read tempo and time signature from `local_ableton_snapshot` (`song.tempo`, `song.sig`)
  before computing anything.

## 3. Forms by genre (starting points, adapt)

Bar counts per section come from `chatmu-studio-genre-templates`. The shape:

| Genre | Typical form |
|---|---|
| Pop | Intro · V1 · Pre · Coro · V2 · Pre · Coro · Puente · Coro (×2) · Outro |
| Reggaetón | Intro (hook) · Coro · V1 · Pre · Coro · V2 · Coro · Puente · Coro · Outro |
| Trap / hip-hop | Intro · Hook · V1 · Hook · V2 · Hook · Outro |
| R&B | Intro · V1 · Pre · Hook · V2 · Pre · Hook · Puente · Hook · Outro |
| Lo-fi (instrumental) | Intro · A · B · A · (B') · Outro |
| House / techno | Intro (DJ, drums only) · Groove · Break · Build · Drop · Break · Build · Drop · Outro (DJ) |
| EDM / future bass | Intro · V · Build · Drop · V2 · Build · Drop 2 · Outro |
| Regional (corridos, banda) | Intro instrumental · V1 · V2 · Coro · Interludio (requinto/metales) · V3 · Coro · Outro |
| Balada | Intro · V1 · V2 · Coro · V3 · Coro · Puente (modula) · Coro · Outro |

**Ways to open (pick one on purpose and say why):**
1. **Intro = chorus material, thinned** (filtered chords or the hook on one instrument) — the
   most common; the chorus then feels like "arriving".
2. **Cold open on the chorus / hook** — reggaetón, pop and trap that need the hook in the first
   10 seconds (streaming, short-form video).
3. **Straight into the verse** with a 1–2 bar pickup — storytelling genres, regional, rap.
4. **Atmospheric intro** (pad, texture, no drums) — lo-fi, R&B, cinematic.
5. **DJ intro** (16–32 bars of drums only) — house and techno for mixing.

## 4. Storytelling: energy per section

Give each section an **energy level 1–10** and decide what enters and leaves. Rules that work:

- **The chorus is the peak until the last chorus.** It is fuller (more layers, wider), higher
  (melody sits a 3rd to an octave above the verse) and has the most rhythmic drive.
- **Verse 2 ≠ Verse 1.** Same chords, but add or change one element (a counter-melody,
  hats in 16ths, a new percussion) so the song moves forward.
- **The pre-chorus builds by subtraction and speed:** drop the kick or the bass, double the
  harmonic rhythm (chord every 2 beats), add a riser or snare roll in the last bar.
- **The hole:** remove everything (or all but the vocal) for the last beat or the last bar
  before the chorus/drop. The re-entry is the impact.
- **The bridge is contrast, once:** new chords (start on IV or ♭VI), half-time drums,
  stripped arrangement, or a key change.
- **The last chorus is the biggest:** double it, add a layer, or modulate up 1–2 semitones.
- **Outro:** mirror the intro, or let the chorus fade by removing layers one by one.

## 5. Plan first (always, for a new song or "make it a full song")

Before writing any notes, show the plan as a table and get an OK:

```
Sección    Compases  Empieza (compás · beat)  Energía  Entra / sale                   Acordes
Intro      8         1 · 0                    3        pad + hook filtrado            i–♭VI–♭III–♭VII
Coro       8         9 · 32                   8        todo, bajo y 808 entran        i–♭VI–♭III–♭VII
Verso 1    16        17 · 64                  5        sale el lead, hats a corcheas   i–♭VI (2 c/u)
...
```

Keep it short; if the user only said a genre, propose ONE form from section 3 and ask
"¿te late o la quieres más corta / que empiece con el coro?".

## 6. Building it in Live

### Session view (ideas, sketching) — one scene per section
1. `local_ableton_snapshot` → see existing scenes (`scenes`, e.g. `["0:Intro","1:"]`) and
   clips. Never rename a scene that already has a user name without asking.
2. Create the missing rows: `local_ableton_edit_track` `{ action: "create_scene" }` (asks for
   approval; it appends at the end unless you pass `index`).
3. Name every row in order with `local_ableton_scene_name`
   `{ action: "set", sceneIndex, name }`: "Intro", "Coro", "Verso 1", "Pre", "Coro 2", ...
   Put the bar count in brackets so the row is self-describing: **"Verso 1 [16]"**.
4. Fill each section's clips in its row (`chatmu-studio-compose-core`). Repeated sections
   reuse the same clips (copy them to the new row), varied sections get their own.
5. Audition: `local_ableton_fire` `{ action: "scene", sceneIndex }`.

### Arrangement view (the song on the timeline) — one locator per section
1. Place clips on the timeline (`local_ableton_arrangement` `duplicate_from_session`, see
   `chatmu-studio-session-vs-arrangement`).
2. Mark every section start: `local_ableton_arrangement`
   `{ action: "create_locator", beats, name: "Verso 1" }`. Beats from section 2's math.
3. `local_ableton_arrangement` `{ action: "show" }` so the user sees the markers.

Always name sections the same way in scenes and locators, so "el coro" means one thing.

## 7. Reading the structure of an existing song

1. `local_ableton_snapshot` returns `cues` as `"beat:name"` (locators) and `scenes` as
   `"index:name"`.
2. Locators exist → that is the map. Convert to bars for the user ("el Coro empieza en el
   compás 25").
3. No locators but named scenes → the form lives in Session.
4. Nothing named → infer from the arrangement clips (where clips start/stop, where tracks
   enter) and **propose** names; create locators only after the user agrees.
5. Keep this map in mind for the whole conversation; re-read it if the user edits the song.

## 8. Moving around: "córrela desde…", "graba desde…"

| User says | Do |
|---|---|
| "Córrela desde el coro" | find the cue named like "Coro" → `local_ableton_transport` `{ action: "play", fromBeat: cueBeat }` |
| "Desde el coro pero un compás antes" / "cuéntame 4 antes" | `fromBeat: max(0, cueBeat − beatsPerBar)` (4 beats in 4/4) |
| "Desde el segundo verso" | the 2nd cue whose name starts with "Verso", or "Verso 2" |
| "Loopea el coro" | `local_ableton_song` `{ property: "loopStart", beats: cueBeat }`, `{ property: "loopLength", beats: sectionBeats }`, `{ property: "loop", on: true }`; then play fromBeat |
| "Graba desde el coro con click" | see below |

**Recording at a section** (`chatmu-studio-record` for the details): `local_ableton_record`
`{ action: "start", mode: "arrangement", countInBars: 1, trackIndex }` records from the
**current playhead** and pre-rolls the count-in before it with the metronome. It has no
"from beat" option, and Live ignores playhead moves while stopped. So:
1. Move the playhead to the section: `local_ableton_arrangement` `{ action: "jump_cue",
   direction: "next" | "prev" }` until you reach the section's locator.
2. Verify with `local_ableton_snapshot` that `song.position` equals the locator's beat.
3. If it did not move, ask the user for one click: "dale clic al marcador del Coro en Live
   y te grabo". Never start recording in the wrong place.
4. Then `start` (it asks for approval every time). Say what will happen: "un compás de
   cuenta con click y grabo desde el Coro en la pista 3".

## Don'ts

- Don't deliver a loop when the user asked for a song; offer the form first.
- Don't make a section a length that breaks the 4-bar grouping without saying it's on purpose.
- Don't rename or reorder the user's scenes or locators without asking.
- Don't assume scene index = section order in time; read the names.
- Don't record before confirming the playhead is at the section.
