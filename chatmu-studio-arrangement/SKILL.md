---
name: chatmu-studio-arrangement
description: >
  Song form and arrangement in the user's Ableton Live set, end to end: plans
  the sections of a new song (intro, verse, pre-chorus, chorus, bridge, drop,
  outro) with bars and an energy story, builds them as scenes or locators,
  jumps/records from a section, reviews an existing arrangement (section map,
  energy curve measured with Chatmu Ears, transitions where it doesn't move),
  and builds electronic build-ups and drops. Merges song-structure,
  arrangement and drop-buildup. Trigger phrases: "song structure", "arrange",
  "full song", "the song feels flat", "energy curve", "transitions", "make a
  drop", "build-up", "riser", "estructura", "estructura de la canción", "arma
  la canción", "revisa el arreglo", "se siente plana", "no crece", "el coro no
  explota", "transiciones", "intro", "verso", "pre-coro", "coro", "puente", "drop", "outro",
  "córrela desde el coro", "graba desde el coro", "hazme un drop", "subida",
  "redoble", "Session", "Arrangement".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Song form end to end: plan sections and energy, build scenes/locators, review the arrangement, build-ups and drops"
version: "2.0"
tags: ["studio", "ableton", "arrangement", "arreglo", "estructura", "structure", "sections", "energy", "drop", "build-up"]
requiresTools: ["local_ableton_snapshot", "local_ableton_edit_track", "local_ableton_scene_name", "local_ableton_fire", "local_ableton_arrangement", "local_ableton_transport", "local_ableton_song", "local_ableton_record", "local_ableton_tempo_map", "local_ableton_status", "local_ears_listen", "local_ears_analyze_file", "local_ears_render", "local_ableton_create_clip", "local_ableton_write_notes", "local_ableton_undo", "local_ableton_lom", "local_ableton_load_devices", "local_synth_list_params", "local_synth_set_params"]
---

# Chatmu Studio — Arrangement (form, review, build-ups and drops)

One skill for everything about the shape of a song. Three parts:
- **Part A — Plan and build the form** of a new song (sections, bars, energy story, scenes and
  locators, jumping/recording from a section).
- **Part B — Review an existing arrangement** (section map, energy curve with Ears,
  transition proposals; applies only with the user's OK).
- **Part C — Build-up and drop** for electronic sections.

Genre forms and lengths also live in each `chatmu-studio-genre-*` skill; when one is active,
its form wins over the generic tables here. Full-song workflow: `chatmu-studio-make-song`.

## Part A — Plan and build the form

**Requires:** Chatmu Desktop (Co-Producer) bridge + Ableton Live.
**Related:** the `chatmu-studio-genre-*` skills (bar counts per genre), `chatmu-studio-session-vs-arrangement`
(where clips live, moving them to the timeline), `chatmu-studio-record` (count-in, quantization),
`chatmu-studio-melody-over-chords` (what to write inside each section).

### Why this skill exists

"Hazme un trap" is not a loop. A song is a sequence of sections with a story: something
is presented, repeated, varied, lifted and resolved. If you write 8 bars and stop, you made
an idea, not a song. **Plan the form before writing notes**, build it so the user (and you,
later) can see it in Live, and use it to navigate.

### 1. Vocabulary (say it in the user's language)

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

### 2. The math of form

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

### 3. Forms by genre (starting points, adapt)

Bar counts per section come from the `chatmu-studio-genre-*` skills. The shape:

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

### 4. Storytelling: energy per section

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

### 5. Plan first (always, for a new song or "make it a full song")

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

### 6. Building it in Live

#### Session view (ideas, sketching) — one scene per section
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

#### Arrangement view (the song on the timeline) — one locator per section
1. Place clips on the timeline (`local_ableton_arrangement` `duplicate_from_session`, see
   `chatmu-studio-session-vs-arrangement`).
2. Mark every section start: `local_ableton_arrangement`
   `{ action: "create_locator", beats, name: "Verso 1" }`. Beats from section 2's math.
3. `local_ableton_arrangement` `{ action: "show" }` so the user sees the markers.

Always name sections the same way in scenes and locators, so "el coro" means one thing.

### 7. Reading the structure of an existing song

1. `local_ableton_snapshot` returns `cues` as `"beat:name"` (locators) and `scenes` as
   `"index:name"`.
2. Locators exist → that is the map. Convert to bars for the user ("el Coro empieza en el
   compás 25").
3. No locators but named scenes → the form lives in Session.
4. Nothing named → infer from the arrangement clips (where clips start/stop, where tracks
   enter) and **propose** names; create locators only after the user agrees.
5. Keep this map in mind for the whole conversation; re-read it if the user edits the song.

### 8. Moving around: "córrela desde…", "graba desde…"

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

### Don'ts

- Don't deliver a loop when the user asked for a song; offer the form first.
- Don't make a section a length that breaks the 4-bar grouping without saying it's on purpose.
- Don't rename or reorder the user's scenes or locators without asking.
- Don't assume scene index = section order in time; read the names.
- Don't record before confirming the playhead is at the section.

## Part B — Review an existing arrangement

**Requires:** Chatmu Desktop bridge + Ableton Live + Chatmu Ears.
**Uses:** Part A (planning or building the form, jumping to a section), the `chatmu-studio-genre-*` skills (typical lengths per genre), Part C (risers, drops), `chatmu-studio-automation`, the `chatmu-studio-genre-*` skills (fills), `chatmu-studio-session-vs-arrangement`, `chatmu-studio-listen-troubleshooting`.

### What does this Skill do?

"¿Cómo está la estructura?" → a map of the song in bars, an energy curve you can explain,
and 2–4 concrete ideas where the song stays flat. **It proposes; it never rewrites the
arrangement without an OK.**

Answer in the user's language (usually Spanish). A table for the map, short lines for ideas.

### HARD RULES

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

### Phase 0 — Read (no writes)

1. `local_ableton_snapshot` → tracks, arrangement summary, locators, tempo, time signature.
2. For tracks whose summary isn't enough: `local_ableton_arrangement { action: "get_clips",
   trackIndex }` → clip names, start/end in beats.
3. `local_ableton_tempo_map` → tempo changes (reads the last saved .als; ask for Cmd+S if
   `unsavedChanges`).
4. Ask the genre if it isn't obvious (it sets typical lengths; the `chatmu-studio-genre-*` skills).

### Phase 1 — Section map

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

### Phase 2 — Energy curve (Ears)

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

### Phase 3 — Proposals (2–4, biggest impact first)

Each: where (bars) · what's wrong (number) · idea · how it would be done.

| Problema | Ideas |
|---|---|
| Verse → chorus doesn't lift | remove kick/bass the last bar before the chorus; riser + white-noise sweep over 4–8 bars; add a layer (coros, octave synth) only in the chorus |
| Chorus 2 = chorus 1 | add a counter-melody or percussion layer; double the vocal |
| Long intro | cut to 4–8 bars (radio) or keep 16–32 (DJ edit): ask what it's for |
| No contrast before the end | a bridge/break of 8 bars with half the elements |
| Abrupt section change | a drum fill in the last bar (the `chatmu-studio-genre-*` skills), a crash on bar 1 |
| Electronic drop without impact | Part C |

### Phase 4 — Apply (with OK)

- **Locators:** `local_ableton_arrangement { action: "create_locator", beats, name }` for
  every section (non-destructive; offer it first — it helps the user and every other skill).
- **Fills / risers as MIDI:** write them in a Session clip on a NEW track
  (`local_ableton_create_clip` + `local_ableton_write_notes`), then place it with
  `local_ableton_arrangement { action: "duplicate_from_session", trackIndex, clipIndex,
  beats }` (approval: it replaces that range on that track — use an empty track).
- **Removing elements, automation sweeps:** tell the user exactly what to cut where
  (rule 5), or use the clip-envelope routes in `chatmu-studio-automation`.
- Undo: `local_ableton_undo` (say what is undone).

### Ears verification

After applying, measure the changed transition again with the same method as Phase 2 (same
sections, same seconds) and report "verso → coro: +0.6 → +2.8 LU". If you couldn't listen
(nothing playing, Ears unavailable, plugin missing — see
`chatmu-studio-listen-troubleshooting`), say **"no verificado"** and keep the proposal as a
proposal.

### Don'ts

- Don't rename sections by position alone; ask when unsure.
- Don't move or delete the user's clips.
- Don't give energy claims without measuring every section the same way.

## Part C — Build-up and drop

**Requires:** Chatmu Desktop bridge + Ableton Live + Chatmu Ears.
**Uses:** the `chatmu-studio-genre-*` skills (lengths/tempos), the `chatmu-studio-genre-*` skills (patterns), `chatmu-studio-automation` (filter/volume moves), Part B (where it sits), `chatmu-studio-sidechain` (the drop's pump), `chatmu-studio-sound-design` (riser/noise sounds).

### What does this Skill do?

A drop only hits if what comes before it takes energy away and builds tension. This skill
designs the last 8–16 bars before the drop and the first bar of it, writes what can be
written, and measures the contrast.

Answer in the user's language (usually Spanish). Show the plan as a bar-by-bar table.

### HARD RULES

1. **Contrast > loudness.** The drop must have more low end and density than the end of the
   build — not just be louder. The last 1–2 bars of the build lose kick and bass.
2. **New material on NEW tracks** ("Build Snare", "Riser", "Impact"), never inside the
   user's clips. Placing a Session clip in the Arrangement replaces that range on that track
   (`duplicate_from_session`, approval) — use those new tracks.
3. **Bars:** build = bars before the drop's bar 1 (e.g. drop at bar 65 → 16-bar build = 49–64).
4. Arrangement edits the tools can't do (cut the kick clip, split): tell the user exactly
   where (Cmd+E at bar X on track Y), or put the cut in the new material instead.
5. Plan → OK → write → Ears check → keep or `local_ableton_undo`.

### Phase 0 — Read

`local_ableton_snapshot` (+ `local_ableton_arrangement get_clips` on kick/bass/main
synths): tempo, genre, where the drop is (locator or ask), what plays in the build now.

### Phase 1 — The plan (8 or 16 bars)

| Compases (16-bar build) | Batería | Música | FX |
|---|---|---|---|
| 1–8 | kick on, snare on quarters | filter starts closing / music thins | noise riser starts low |
| 9–12 | snare in 8ths, kick may drop | filter opening, pitch riser starts | riser rising |
| 13–14 | snare in 16ths | bass out | riser + reverb growing |
| 15 | snare 32nds / triplets, velocity rising | kick and bass OUT | peak |
| 16 (last beat) | stop — 1 beat of silence or a vocal/FX tail | | reverse cymbal into the drop |
| Drop bar 1 | kick + bass + full chords | everything in | impact (crash + sub boom) |

8-bar build: compress the same arc (quarters 1–4, 8ths 5–6, 16ths 7, 32nds/stop 8).
Genre: house/techno builds are subtler (filter + percussion, rarely a full stop); EDM/future
bass go big (full roll, silence, impact); trap drops often use a vocal tag + 808 hit.

### Phase 2 — Write it

1. Tracks: `local_ableton_edit_track { action: "create_midi" }` (approval each) and rename.
   Load sounds in ONE `local_ableton_load_devices` call (a drum kit — not a bare
   "Drum Rack", see `chatmu-studio-drum-rack`; a Chatmu Sound for the riser if the user
   has it).
2. **Snare roll:** a 16-bar Session clip (`local_ableton_create_clip`) with notes from the
   table — quarters → 8ths → 16ths → 32nds, velocity ramping ~60 → 120
   (`local_ableton_write_notes`; pitch per kit, MIDI 38/40 = snare on GM-style kits; check
   the kit's pads).
3. **Riser:** on a Chatmu Sound track, one long note (or a slow upward line) for the build's
   length; noise + rising filter/pitch with `local_synth_list_params` → `local_synth_set_params`
   (or a riser sample the user has). Movement: `chatmu-studio-automation`.
4. **Impact:** a crash + low hit on bar 1 of the drop (one-bar clip).
5. Audition in Session first (`local_ableton_fire`), then with OK place each clip:
   `local_ableton_arrangement { action: "duplicate_from_session", trackIndex, clipIndex,
   beats }`.
6. Kick/bass out in the last bars: rule 4.

### Ears verification

Play from 4 bars before the end of the build through 4 bars of the drop
(`local_ableton_transport { action: "play", fromBeat }`), `local_ears_listen` for that length
(one call), then `local_ears_render { captureId, view: "loudness" }` and `"spectrogram"`.
Pass if: the low end (sub/low bands) is nearly gone in the last build bar and returns on the
drop, and the drop is ≥ 2–3 LU above the build's last bars (electronic: often more).
Report the numbers. If not, adjust one thing and re-measure; if you couldn't listen, say
**"no verificado"**.

### Don'ts

- Don't make the build louder than the drop.
- Don't write into the user's existing clips.
- Don't leave the drop without low end "for contrast" — the contrast is the build.
