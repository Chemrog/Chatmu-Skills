---
name: chatmu-studio-genre-dark-trap
description: >
  Produces dark trap and drill-adjacent beats in the user's Ableton Live set:
  minor / phrygian / harmonic-minor harmony on a tonic pedal, half-time drums
  with hat triplets and rolls, a long tuned 808 with glides, a bell, flute or
  pluck hook that leaves space for the vocal, plus UK drill and NY/Brooklyn
  drill variants. Trigger phrases: "dark trap", "trap beat", "make a trap
  beat", "drill beat", "UK drill", "NY drill", "Brooklyn drill", "808 slides",
  "hi-hat rolls", "menacing beat", "trap oscuro", "beat de trap", "hazme un
  trap", "beat de drill", "drill inglés", "808 con glide", "rolls de hats",
  "beat oscuro", "trap duro".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Dark trap and drill: minor/phrygian pedal, half-time drums, hat rolls, gliding 808, sparse hook"
version: "1.0"
tags: [studio, ableton, genre, trap, dark-trap, drill, uk-drill, ny-drill, 808, hip-hop]
requiresTools:
  - local_ableton_snapshot
  - local_ableton_tracks
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
  - local_ableton_mixer
  - local_ableton_device_params
  - local_ears_track_levels
  - local_harmony_map
---

# Chatmu Studio — Dark trap & drill

Dark trap is **space, weight and tension**: a half-time pocket, an 808 that is the bass AND the
melody of the low end, hats that carry the motion, and a short, eerie hook that repeats while the
rapper owns the middle. It sounds AI-made when everything plays all the time, the hats are a flat
machine-gun of 16ths at one velocity, the 808 is untuned to the key, or the chords change every bar.

Related: `chatmu-studio-hook-melody` (motif method), `chatmu-studio-bass-lines` (808 detail),
`chatmu-studio-drum-rack`, `chatmu-studio-humanize`, `chatmu-studio-sidechain`,
`chatmu-studio-arrangement`, `chatmu-mix-by-genre`, `chatmu-studio-genre-oriental-hiphop`
(when the user wants Arabic colour on top of this).

## 1. Brief (ask only what is missing; propose defaults)
| Decision | Options | Default |
|---|---|---|
| Style | dark trap (Atlanta/Memphis lineage) · UK drill · NY/Brooklyn drill · melodic/rage-leaning | dark trap |
| Tempo | trap 130–150 · UK drill 140–144 · NY drill 140–146 | 140 |
| Key | minor keys whose tonic puts the 808 at MIDI 25–31 (C#–G) | F# minor or C# minor |
| Scale | natural minor · harmonic minor · phrygian | natural minor, harmonic minor for the hook's V |
| Hook voice | bell · flute · pluck · choir/vocal pad · piano (detuned) · strings (staccato) | bell |
| Vocal | rap (needs pockets) · melodic/sung (more harmony allowed) | rap |

## 2. Tempo & feel
- Set the project at **130–150 BPM** but think **half-time**: the snare/clap lands once per bar
  on beat 3 (step 9), so it feels like 65–75 BPM. Snare on 2 & 4 at 140 is NOT trap.
- **Straight grid**, no global swing. The bounce comes from hat subdivisions (8ths, 16ths,
  16th-triplets, 32nds) and velocity, not from swing.
- Drill: same half-time skeleton but **triplet-feel hats and a displaced 2nd snare**; feels
  more skippy and nervous.

## 3. Groove grid (1 bar, beats from bar start; steps 1–16 = 16ths)
Drum Rack: 36 kick, 38 snare, 39 clap, 42 closed hat, 46 open hat, 37 rim, 70 shaker.
`local_music_theory` `action: drum_pattern` `genre: trap` gives a skeleton; then edit it.

**Dark trap (2-bar phrase)**
| Element | Bar 1 | Bar 2 | Velocity |
|---|---|---|---|
| Kick (36) | 0, 2.5 (steps 1, 11) | 0, 0.75, 2.75 (steps 1, 4, 12) | 110–127 |
| Clap+snare (39+38) | 2 (step 9) | 2 | 115–125, layered same start |
| Closed hat (42) | 8ths 0, 0.5 … 3.5 | 8ths + one roll | 70–95, downbeats louder |
| Open hat (46) | 3.5 (once, choke with next closed hat) | — | 70–85 |
- Hat rolls: **one or two per bar, never every beat**. Types: 16th-triplets (step 1/6 = 0.1667
  beat, 3 notes per 8th) leading into beat 3 or 4; 32nds (0.125 beat) for 2–4 hits before a
  downbeat; a 1/64 "buzz" (0.0625) only for a fill before a section change.
- Roll velocity ramps (e.g. 55 → 90) or dips (90 → 55 → 85); flat-velocity rolls sound robotic.
- Every 4th bar, change something: drop the kick on beat 1 of the next bar, add a 16th kick
  pickup at 3.75, or mute hats for half a bar before the hook.

**UK drill (2-bar phrase, 140–144)**
- Snares: bar 1 at **2.0 (step 9)**; bar 2 at **2.0** and a displaced hit at **3.5
  (step 15)** or 1.75 — this off-grid second snare is the drill signature.
- Hats: 16th-triplet clusters, e.g. 0, 0.333, 0.667 · 1.5 · 2, 2.333 · 3, 3.167, 3.333 — gaps
  matter as much as hits. Rim/perc on the "a"s (0.75, 2.75) at velocity 60.
- Kicks: few, often only bar 1 beat 1 and syncopated hits under 808 slides.

**NY / Brooklyn drill (140–146)**
- Same snare placement as UK drill, harder kicks, more 808 movement (slides every bar),
  sampled/choir/vocal-chop hooks, louder and more distorted 808. Hats less dense than UK.

Humanize: hats ±5–10 ms and velocity ±8 (`local_music_theory` `action: humanize`); keep kick and
clap on grid. Detail: `chatmu-studio-humanize`.

## 4. Harmony: pedal and a couple of colours
The tonic carries 70–80 % of the time. Chords are moments, often just a dyad or the hook itself.
- **i – ♭VI** (F#m – D): the default, 2 bars each.
- **i – ♭VI – iv – V** (F#m – D – Bm – C#): harmonic minor, V major for the leading tone; good
  for melodic trap.
- **i – ♭II** (F#m – G): phrygian dread; ♭II for 1 bar in 4.
- **i – ♭VII – ♭VI – V** descending: epic/dramatic.
- `local_music_theory` `action: progression` `preset: trap` returns a usable i–♭VI-type loop.
- Voicings: sparse — root + 5th low, minor 3rd or 9th an octave up; pads ≥ MIDI 55 so they don't
  mud the 808. Diminished or minor-add9 stabs work; full 7th-chord jazz voicings do not.
- **Avoid**: major-key I–V–vi–IV, bright IV chords, ii–V–I, a new chord every bar.

## 5. Hook / melody specifics
Build the motif with `chatmu-studio-hook-melody`; in this genre:
- **Short and repetitive**: 1- or 2-bar motif, 3–6 notes, repeated across the 8-bar hook with
  only the last bar varied. Range ≤ a 6th.
- **Dark intervals**: ♭2→1, ♭6→5, minor 3rd, tritone as a passing note; harmonic-minor 7→1.
- **Rhythm against the half-time**: notes on 16th off-beats and triplets (0.333, 0.667) that dodge
  the clap on beat 3.
- Register: bell/pluck MIDI 72–96, flute 72–91, choir pad 60–79, piano 60–84. Keep the lead out of
  the 200–500 Hz zone where the vocal's body sits.
- **Counter-gesture**: a second high texture (reversed bell, sparse arp) only in the hook, -8 to
  -12 dB under the lead (`chatmu-studio-counter-melody`).
- In the verse the hook drops to a filtered 1-bar fragment every 4 bars, or out entirely.

## 6. 808
- The 808 is tuned to the song: root at MIDI **25–31** (C#0–G0 in Live naming; ~35–49 Hz
  fundamental). If the tonic is higher (A, B), play it an octave lower only if the 808 still
  has audible harmonics; otherwise saturate it.
- Pattern: one note per kick hit, held until the next kick (trap). Length decides the groove:
  cut short (0.25–0.5 beat) for bounce, long for weight.
- **Glides**: overlap the next note by ~0.125–0.25 beat AND enable portamento/glide on the
  instrument (`local_ableton_device_params`, glide 40–120 ms, mono/legato). Slide to the octave,
  5th, ♭7 or ♭2. One or two slides per 2 bars in trap; in drill, slides on most bars, often
  octave-down drops at bar ends.
- Drill 808 lines move more: root – ♭3 – 4 – ♭2 – root phrases across 2 bars.
- The 808 and kick hit together: kick short and clicky (≤ 150 ms), 808 attack slightly softer,
  or sidechain the 808 by 2–4 dB to the kick (`chatmu-studio-sidechain`).

## 7. Sounds
- `local_synth_find_preset` with genre words: `query: "808 dark"`, `"bell dark"`, `"flute"`,
  `"pluck short"`, `"vocal"`, `"strings"`, `"keys dark"`. The factory covers trap/drill
  well; if `fallback: true`, say so. Load with `local_synth_set_preset`.
- Browser fallbacks (`local_ableton_browser`): search `808`, `trap kit`, `drill`, `bell`,
  `music box`, `choir`. Load with `local_ableton_load_device`.
- Character: bells with long release + slight detune; flutes breathy; plucks short with
  reverb; 808 with a touch of distortion so it reads on phones (harmonics at 100–300 Hz).

## 8. Arrangement (bars at 140 BPM; 1 bar ≈ 1.71 s)
| Section | Bars | What plays |
|---|---|---|
| Intro | 4–8 | hook alone, filtered or with pad; producer tag here; no 808 |
| Hook | 8 or 16 | full drums, 808, hook, counter texture |
| Verse 1 | 16 | drums + 808 + pad/fragment; hats change every 4 bars |
| Hook | 8–16 | full |
| Verse 2 | 16 | variation: different hat pattern, 808 rhythm, drop the kick for 2 bars |
| Bridge / breakdown | 4–8 | no drums, hook reversed or on pad, 808 one long note |
| Hook | 8–16 | full, maybe extra layer |
| Outro | 4–8 | hook alone or fading |
- 2-to-3-minute songs are normal (≈ 70–100 bars). Drop-outs (1 beat or 1 bar of silence/only
  vocal) right before the hook are the genre's main transition — not risers.
- Name scenes with `local_ableton_scene_name`. Full structure: `chatmu-studio-arrangement`.

## 9. Mix targets
- Low end: **808 owns 30–80 Hz**, kick owns 50–100 Hz click/punch; high-pass everything else at
  100–150 Hz (pads, bells, flutes at 200 Hz+).
- Relative levels (pre-vocal, 808 = 0 dB reference): kick -1 to -3, clap -3 to -5, hats -10 to -14,
  hook -6 to -9, pads -14 to -18.
- Space: hook and pads wide and wet (reverb 2–4 s, pre-delay 20–40 ms via send); drums and 808
  dry and mono below 120 Hz. Vocal centre, dry-ish, on top.
- Loudness: master around **-8 to -6 LUFS integrated** for release, true peak ≤ -1 dBTP; leave
  the mixdown at -14 to -10 LUFS before mastering (`chatmu-master-chain`).
- Check with `local_ears_track_levels` (808/kick masking, hook vs vocal zone) and
  `local_ears_listen` for the whole mix. Details: `chatmu-mix-by-genre`, `chatmu-mix-eq`.

## 10. What ruins it
- Snare on 2 & 4 at 140 BPM (that's not half-time).
- Constant 16th hats at one velocity, or rolls every beat.
- An 808 in a different key than the hook, or two 808 notes overlapping without glide set.
- Chords changing every bar with bright major colours.
- A hook that plays non-stop over the verse.
- Reverb on the 808 or kick; stereo-widened low end.
- Sidechain pumping like EDM (keep it 2–4 dB, fast release).

## Workflow with the tools
1. `local_ableton_snapshot` → see what exists; `local_ableton_set_tempo` (140 default).
2. Create MIDI tracks (`local_ableton_edit_track` `create_midi`): Drums, 808, Hook, Pad (and
   Counter if needed). `local_ableton_tracks` to confirm indices.
3. Drums: `local_music_theory` `drum_pattern` `trap` → edit rolls/drill snares → clip with
   `local_ableton_create_clip` (2 or 4 bars) → `local_ableton_write_notes` → `local_ableton_fire`.
4. 808: find/load preset, write the root line on kick hits with 1–2 glides; fire with drums.
5. Harmony: `local_music_theory` `progression`/`chords`; write a sparse pad; check with
   `local_harmony_map`.
6. Hook last; fire after each layer so the user hears it build and can stop you.
7. `local_ableton_mixer` for rough levels from §9; `local_ears_track_levels` to check masking.
8. Name scenes; tell the user what you made and propose the next step (arrangement, vocal, mix).

## Hard rules
- Half-time: clap/snare on beat 3 of every bar (drill: plus the displaced 2nd-bar snare).
- 808 tuned to the key, root at MIDI 25–31; glides only with overlap + glide set on the device.
- At most 2 hat rolls per bar; vary roll velocity.
- Hook ≤ 2-bar motif, ≤ a 6th range, out of the verse or reduced.
- Never add reverb or stereo width below 120 Hz.
- Say the key, scale and tempo you chose.

## Tell the user (short)
`Dark trap · 140 BPM (half-time) · F# minor, harmonic minor in the hook · F#m 2 bars, D 2 bars ·
clap on 3, 8th hats with a 16th-triplet roll into beat 4 every other bar · 808 on F#0 (MIDI 30)
gliding to the octave at bar 2 · bell hook ♭6–5 sigh, 2-bar motif. Tracks: Drums, 808, Hook, Pad.
Next: arrange 16-bar verse + 8-bar hook, or switch the drums to UK drill?`
