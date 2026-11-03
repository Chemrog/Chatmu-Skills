---
name: chatmu-studio-genre-cinematic
description: >
  Produces cinematic music in the user's Ableton Live set: orchestral score,
  epic/trailer, tension/suspense underscore and emotional piano-and-strings.
  Orchestrates by section with correct registers and doublings (strings,
  brass, woodwinds, percussion), builds ostinatos, pedal points and modal
  progressions, writes the trailer three-act build with hits, risers and
  braams, and mixes with depth. Trigger phrases: "cinematic", "orchestral",
  "epic", "trailer music", "film score", "soundtrack", "tension", "suspense",
  "underscore", "Hans Zimmer style", "música épica", "orquestal", "banda
  sonora", "música de película", "tráiler", "tensión", "música de suspenso".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Orchestral, epic/trailer, tension underscore: registers, doublings, ostinatos, three-act build"
version: "1.0"
tags: [studio, ableton, genre, cinematic, orchestral, trailer, epic, score, orchestration]
requiresTools:
  - local_synth_status
  - local_ableton_snapshot
  - local_ableton_set_tempo
  - local_ableton_edit_track
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_fire
  - local_ableton_scene_name
  - local_music_theory
  - local_synth_find_preset
  - local_synth_set_preset
  - local_ableton_browser
  - local_ableton_load_device
  - local_harmony_map
  - local_ears_track_levels
---

# Chatmu Studio — Cinematic (orchestral, epic/trailer, tension)

Cinematic music serves a picture or an emotion arc, not a loop. The difference between
"orchestral preset demo" and real score is **orchestration**: each section in its strong
register, lines doubled the way an orchestra doubles them, dynamics shaped over time, and
silence used. Think in voices (melody, counter-line, harmony, bass, rhythm), then assign them
to instruments.

Related: `chatmu-studio-hook-melody` (themes), `chatmu-studio-counter-melody`,
`chatmu-studio-harmony`, `chatmu-studio-arrangement` (builds and drops),
`chatmu-studio-sound-design` (risers, braams), `chatmu-studio-spatial-panning`,
`chatmu-mix-by-genre`.

## 1. Brief
| Decision | Options | Default |
|---|---|---|
| Type | epic/trailer · emotional (piano + strings) · tension/suspense underscore · adventure/heroic · dark ambient score | epic |
| Length | 30 s · 60 s · 2 min · custom to picture (ask for hit points in seconds) | 2 min |
| Palette | full orchestra · hybrid (orchestra + synths + big drums) · chamber (strings + piano) | hybrid |
| Mood | heroic · tragic · mysterious · menacing · hopeful | heroic |

## 2. BPM and meter
| Type | BPM | Notes |
|---|---|---|
| Epic/trailer | 120–140 (felt half-time 60–70) | 4/4; ostinato in 8ths/16ths |
| Emotional | 60–80, rubato | 4/4 or 3/4; tempo changes via `local_ableton_set_tempo` per section |
| Tension | 70–100 or no pulse | pulses in odd groupings (5/8, 7/8 feel) |
| Adventure | 100–130 | 4/4 or 6/8 gallop |
Hit points: seconds × BPM / 60 = beat. Move tempo slightly (±3 BPM) so major hits land on a
downbeat.

## 3. Orchestration: registers (MIDI, 60 = C3 in Live)
| Instrument | Full range | Strong / expressive register |
|---|---|---|
| Violins I/II | 55–100 | 64–91 (melody), 88–100 = shimmering, thin |
| Violas | 48–84 | 55–76 (warm inner voice) |
| Cellos | 36–76 | 48–67 singing; 36–48 bass weight |
| Basses | 28–55 (sounds) | 28–43; double cellos an octave below |
| Horns (4) | 34–77 | 53–72 heroic; above 72 strained |
| Trumpets | 54–82 | 62–79 fanfare |
| Trombones | 40–72 | 45–65 power |
| Tuba | 26–53 | 28–46 |
| Flute | 60–96 | 72–93 (bright); low 60–67 breathy, weak |
| Oboe | 58–91 | 62–81 plaintive solo |
| Clarinet | 50–91 | 52–60 dark chalumeau; 72–84 clear |
| Bassoon | 34–75 | 40–60 |
| Choir | S 60–79, A 55–74, T 48–67, B 40–60 | ooh/aah pads |
Keep the lowest voices spaced: intervals below MIDI 48 should be octaves/fifths only (a third
low in the bass is mud).

## 4. Doublings that work
- **Melody**: violins I + flute at the octave above (bright); violins + violas + cellos in
  octaves (epic unison, "big theme"); horns in unison for heroic; cellos alone (MIDI 50–67) for
  intimate/tragic.
- **Bass**: cellos + basses an octave apart; add tuba/bass trombone or a low synth sub for
  hybrid weight.
- **Harmony pads**: horns in close position (mid), or divisi strings; woodwinds blend best in
  pairs (2 flutes, 2 clarinets) in thirds.
- Brass power chord in trailers: trombones + tuba open 5ths/octaves low, horns on 3rd/5th
  mid, trumpets on top.
- Never double the melody in the same octave across many sections: it sounds like a preset.
  Change colour on repeats (flute → oboe → strings octaves → tutti).

## 5. Harmony
- Modal and pedal-based: i – ♭VI – ♭III – ♭VII (Am – F – C – G) epic minor; i – ♭VI – iv –
  V; I – ♭VI – ♭VII – I (heroic, Lydian/Mixolydian borrow); chromatic mediants (C → Ab → E) for
  wonder/drama. `local_music_theory` `progression` preset `cinematic` is a starting point.
- **Pedal point**: hold the tonic in basses/low synth while chords move above (tension, epic).
- Tension: clusters (m2/M2 stacked), tritone, minor with ♭2 (phrygian), the "minor-major" chord
  (mMaj7), sustained chromatic rise, string harmonics. Avoid resolving until the picture says so.
- Emotional: suspensions (sus4 → 3, 9 → 8), I – V/7 – vi – IV with inversions for stepwise bass.
- Harmonic rhythm: 1–2 bars per chord in epic; 2–4 bars or static in tension.
- **Avoid**: pop I–V–vi–IV loops in root position for 2 minutes; dense close voicings below
  MIDI 48; every instrument playing all the time.

## 6. Themes, ostinatos and motion
- Theme (use `chatmu-studio-hook-melody`): 4–8 bars, strong rhythmic identity, leaps of 4th/5th
  then stepwise answer; it returns 2–3 times re-orchestrated and bigger.
- **Ostinato**: string spiccato/staccato 8ths or 16ths on 2–3 notes (1–5–1–♭6), vel 70–100,
  accents every 3 16ths over 4/4 (3+3+2 grouping) for drive. Low strings and pianos double it.
- Counter-line in horns or celli moving against the theme (contrary motion).
- Dynamics: no CC/automation tool for expression here — shape with **velocity** (crescendo
  across a bar: 50 → 110) and by adding instruments; for long notes suggest the user draw
  modwheel/expression automation.

## 7. Percussion and hybrid elements
- Taiko / big drums: low hits on 0 and 2.5 (vel 110–127), toms in 16th rolls building 1–2 bars
  before hits. Epic pattern (1 bar): 0, 0.75, 1.5, 2.0, 3.0, 3.5 with snare/ensemble hit on 1.0
  and 3.0.
- Timpani: tonic and 5th, rolls as 32nds with velocity ramp 40 → 120 into the downbeat.
- Trailer hits: impact on the downbeat of each act change (sub boom + cymbal + brass stab).
- **Braam**: low brass + distorted synth, 1–2 bar sustained cluster (root + 5th + ♭9 low);
  riser (noise/strings glissando written as chromatic 16ths) 2–4 bars before a hit.
- Silence: one beat to one bar of total silence before the final hit.

## 8. Sounds
**Chatmu Synth first (house rule).** Every bass and melodic part (bass/808, keys, pads, plucks,
leads, brass, strings…) gets **Chatmu Synth with a factory preset of this genre**, not Live's
stock instruments (Operator, Grand Piano, Electric…), which sound like generic MIDI:
1. `local_synth_find_preset` with `genre: "Cinematic"`, the `instrument` and a `character`. If it
   returns `fallback: true`, say it's the closest genre.
2. Load the plugin on the track: searching the browser by name does NOT find plugins, so use
   `local_ableton_browser` `path: "plugins"` (then its VST3 folder) to get Chatmu Synth's `uri`,
   and `local_ableton_load_device` with that `uri`.
3. Right after loading, `local_synth_set_preset { file }` (it goes to the newest instance), then
   `local_synth_status`: that track's instance must show the `preset_name`. An empty
   `preset_name` means no preset is loaded yet — never tweak or write on top of that.
Load every synth track first, then write notes. Live's instruments only when the library has
nothing for that part (say so). **Drums are not Chatmu Synth** (no noise source, no percussion
presets): use a Live Drum Rack / kit or samples; a Chatmu Synth 808 can sit under it as the low end.

- `local_synth_find_preset` with `genre: "Cinematic"` if present (else `fallback: true`):
  `Strings` (Warm/Dark), `Brass` (Bright for fanfare, Dark for braam), `Flute`, `Vocal`
  (choir pads), `Bell` (celesta/glock colour), `Synth Dark` (drones, pulses).
- Browser (`local_ableton_browser`): `orchestra`, `strings`, `spiccato`, `horn`, `trombone`,
  `taiko`, `timpani`, `choir`, `piano`, `celesta`, `cinematic`, `impact`, `riser`. Prefer
  orchestral sample libraries the user owns over synths; say when synth strings are a
  compromise. Load with `local_ableton_load_device`.

## 9. Arrangement (trailer three-act, 120 BPM ≈ 2 bars per 4 s)
| Act | Bars | What plays |
|---|---|---|
| Act 1 — setup | 8–16 | piano/celesta motif, sustained strings pp, low pedal; sparse pulse |
| Hit + Act 2 — build | 16 | ostinato enters, percussion every 4 bars, theme in celli/horns |
| Riser + silence | 2–4 | rising strings/noise, 1 beat silence |
| Act 3 — climax | 16 | tutti theme in octaves, brass chords, full taiko, choir |
| Button / tail | 2–4 | final hit, ring-out 3–6 s |
Emotional cue: A (piano + solo cello) 8 · A' (strings join) 8 · B (theme up a 4th, full) 8 ·
coda 4. Name scenes with `local_ableton_scene_name`.

## 10. Mix targets
- Depth with reverb, not EQ alone: one hall send (2.5–4 s, pre-delay 20–40 ms); front
  (percussion, solo) less send, back (horns, choir) more send.
- Orchestral seating panning: violins I −30, violins II −10, violas +10, cellos +25, basses
  +35, horns −15 (back), trumpets +15, trombones/tuba +30, timpani centre-back, percussion wide.
- Low end: basses/cellos + taiko/sub share 30–120 Hz; cut synths below 150 Hz unless they are
  the sub.
- Dynamics are the point: score −16 to −20 LUFS (film/TV stems), trailer −10 to −12. Never
  crush the climax. Check balance with `local_ears_track_levels`.

## 11. What ruins it
- All sections at the same velocity from start to finish.
- Melody in instruments' weak registers (low flute, high horn).
- Close chords in the bass register.
- Loops with no arc; no silence before the climax.
- Synth-string presets exposed in a solo line with no humanized velocity.

## Workflow with the tools
1. `local_ableton_snapshot`; `local_ableton_set_tempo` (and hit-point maths).
2. Tracks (`local_ableton_edit_track` `create_midi`): Low Strings, High Strings, Brass,
   Woodwinds, Perc, Hybrid/Synth, Piano or Choir.
3. Pedal + harmony (`local_music_theory` `chords`/`progression`) → fire (`local_ableton_fire`).
4. Ostinato → percussion → theme → counter-line, writing with `local_ableton_create_clip` and
   `local_ableton_write_notes`, firing after each layer.
5. Verify harmony with `local_harmony_map`; balance with `local_ears_track_levels`.

## Hard rules
- State type, BPM, key/mode, palette and the act/hit plan.
- Every line in its strong register (§3); octaves/fifths only below MIDI 48.
- Re-orchestrate each return of the theme; build by adding instruments and velocity.
- Leave silence or space before the biggest hit.
- Never master a score loud; keep dynamics.

## Tell the user (short)
`Epic hybrid trailer · 128 BPM · D minor · Dm – Bb – F – C over a D pedal · 3+3+2 string
ostinato · theme in celli + horns, then tutti octaves in Act 3 · taiko on 1 and 3&, braam at
bar 25, one beat of silence before the final hit. Tracks: Low Strings, High Strings, Brass,
Woodwinds, Perc, Hybrid, Choir.`
