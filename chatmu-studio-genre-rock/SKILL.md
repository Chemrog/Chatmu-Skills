---
name: chatmu-studio-genre-rock
description: >
  Produces rock in the user's Ableton Live set, riff first: a guitar riff on
  power chords or open strings, double-tracked guitars hard L/R, humanized
  live-feel drums with ghost notes and real fills, a bass that locks to the
  kick and a mix that is loud by density, not by limiting. Covers classic
  rock, alt/indie, pop-punk and hard rock. Trigger phrases: "rock song",
  "guitar riff", "power chords", "indie rock", "alt rock", "pop punk",
  "hard rock", "classic rock", "live drums", "canción de rock", "hazme un
  rock", "riff de guitarra", "rock alternativo", "pop punk", "rock pesado",
  "batería en vivo", "que suene a banda".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Rock, riff first: power chords, double-tracked guitars L/R, humanized live drums; classic, indie, pop-punk, hard"
version: "1.0"
tags: [studio, ableton, genre, rock, indie, alt-rock, pop-punk, hard-rock, guitar, riff]
requiresTools:
  - local_sound_status
  - local_ableton_snapshot
  - local_ableton_tracks
  - local_ableton_set_tempo
  - local_ableton_edit_track
  - local_ableton_create_clip
  - local_ableton_write_notes
  - local_ableton_fire
  - local_ableton_scene_name
  - local_music_theory
  - local_sound_find_preset
  - local_sound_set_preset
  - local_ableton_browser
  - local_ableton_load_device
  - local_harmony_map
  - local_ears_track_levels
  - local_ears_listen
---

# Chatmu Studio — Rock

Rock is a **band in a room**: drums, bass, two guitars, a voice. The song starts from a riff,
not a chord loop. MIDI rock sounds fake for three reasons: drums quantized at one velocity with
no ghost notes or fills, one mono guitar instead of two performances panned apart, and chords
voiced like a piano (full triads with thirds under distortion = mud). Fix those three and the
rest is arrangement and dynamics.

Related: `chatmu-studio-hook-melody`, `chatmu-studio-drum-rack`, `chatmu-studio-humanize`,
`chatmu-studio-bass-lines`, `chatmu-studio-spatial-panning`, `chatmu-studio-record` (real
guitar takes beat MIDI every time), `chatmu-studio-arrangement`, `chatmu-mix-by-genre`.

## 1. Brief (ask only what is missing; propose defaults)
| Subgenre | BPM | Feel | Signature |
|---|---|---|---|
| Classic rock | 100–130 | straight 8ths, slight shuffle allowed | open-chord riffs, blues pentatonic, I–♭VII–IV |
| Alt / indie | 110–140 | 8ths or driving 16th hats | jangly or fuzzy guitars, add9/sus chords, quiet-loud |
| Pop-punk | 160–200 | fast 8th downstrokes, snare 2&4 or "skate beat" | power chords, I–V–vi–IV fast, gang vocals |
| Hard rock | 90–130 | heavy, half-time breakdowns | palm-muted riffs on low E/D, drop D, big toms |
Default: alt rock 128 BPM, E minor (guitar-friendly keys: E, A, D, G; drop D for heavy).
Ask: user plays guitar? (if yes, record real takes — `chatmu-studio-record`).

## 2. BPM & feel
- Straight 8ths; humanize hard: hats ±10 ms, snare ±6 ms, kick ±5 ms, velocity ±12.
- Drummer push/pull: chorus 0–5 ms ahead (urgency), verse on or 5 ms behind.
- Classic rock shuffle: swing 58–62 % on 8ths. Pop-punk: no swing.
- Use `local_music_theory` `action: humanize`; never leave drums on the grid.

## 3. Groove grid (16 steps, step 1 = beat 1; beats = (step−1)/4)
Drum Rack: 36 kick, 38 snare, 37 rim/cross-stick, 42 closed hat, 46 open hat, toms 41/45/48,
crash 49, ride 51.
```
ROCK BACKBEAT — 100–140
Kick    X . . . . . . . X . X . . . . .   steps 1 9 11 (vary: 1 8 9)  vel 105–120
Snare   . . . . X . . . . . . . X . . .   steps 5 13                  vel 110–125
Ghosts  . . . . . . . X . . . . . . . X   steps 8 16 (verse)          vel 30–50
Hat     8ths (or ride in chorus)                                      vel 75–95 down, 55–70 up
PUNK / SKATE — 160–200: kick 1 5 9 13 (or 1 9), snare on every offbeat 8th (3 7 11 15)
  for the skate beat, or 5 13 for the standard; crash/ride 8ths in chorus
HALF-TIME BREAKDOWN: kick 1 4 11, snare 9, crash/china on 1
```
- Verse: closed hat or cross-stick (37) instead of snare; chorus: open hat/ride + crash on
  bar 1 of every 4 (vel 100–115).
- Fills every 4 or 8 bars, last 1–2 beats: snare 16ths → toms 48/45/41 descending, vel
  ramp 85 → 120, crash + kick on the next downbeat. Vary fills; never the same one twice in a
  row.
- Hat velocity accent: downbeat 8ths louder than upbeats (the real hand pattern).
- No preset: `drum_pattern` has no rock genre — write the grid.

## 4. The riff and harmony
- **Riff first**: 1–2 bars, built on the minor pentatonic / blues scale (0 3 5 6 7 10) or
  mixolydian/aeolian, using the low strings (MIDI 40–55; low E string = MIDI 40, which Live names E1).
  Rhythm matters more than pitch: syncopation on the "and" of 2 and 4, rests that breathe.
- **Power chords**: root + 5th (+ octave): e.g. E5 = 40 47 52. Thirds only on clean or lightly
  driven parts. Palm-muted 8ths = short notes (0.25–0.35 beat) at vel 80–95; open accents =
  long notes vel 110–127.
- Progressions (numerals in the key): I–♭VII–IV (mixolydian) · i–♭VI–♭III–♭VII · i–♭VII–♭VI–♭VII
  · I–V–vi–IV (pop-punk) · I–IV–V (classic) · i–iv–♭VI–V. Chords change on the bar or the
  "and" of 4 (push).
- Alt/indie colour: add9, sus2, open strings ringing against moving chords (keep a high E/B
  drone note on top).
- Avoid: 7th/9th jazz chords under distortion, piano-style close triads on the guitar, more
  than 4 chords in the riff, chord changes on every beat.
- `local_music_theory` `action: chords` for symbols like `E5`, `Asus2`; check with
  `local_harmony_map`.

## 5. Melody / hook
- Rock has **two hooks**: the riff (instrumental) and the vocal chorus. The riff appears in
  the intro and between sections; the chorus vocal sits a 4th–octave above the verse
  (`chatmu-studio-hook-melody`).
- Vocal melodies are pentatonic, stepwise with 4th/5th leaps; chorus long notes on the 5th or
  root, shouted range MIDI 64–74 (male) / 69–79 (female).
- Guitar lead/solo: 8 bars, pentatonic + bends faked as grace notes (no pitch bend: a 32nd
  note one step below into the target), repeated motif rising an octave by the end.
- Pop-punk: chorus melody in unison with power-chord roots + gang "whoa" an octave below.

## 6. Bass
- Locks to the kick: root 8ths (pick-style, vel 95–110) in MIDI 28–43; octave jumps on
  offbeats in disco-rock; follows the riff in unison/octave in hard rock.
- Approach notes into chord changes on step 15–16 (chromatic or diatonic).
- Pop-punk: driving 8th roots, no gaps. Classic: walking passing tones on I–IV–V.
- Details in `chatmu-studio-bass-lines`.

## 7. Sounds
**Chatmu Sound first (house rule).** Every bass and melodic part (bass/808, keys, pads, plucks,
leads, brass, strings…) gets **Chatmu Sound with a factory preset of this genre**, not Live's
stock instruments (Operator, Grand Piano, Electric…), which sound like generic MIDI:
1. `local_sound_find_preset` with `genre: "Indie"`, the `instrument` and a `character`. If it
   returns `fallback: true`, say it's the closest genre.
2. Load the plugin on the track: searching the browser by name does NOT find plugins, so use
   `local_ableton_browser` `path: "plugins"` (then its VST3 folder) to get Chatmu Sound's `uri`,
   and `local_ableton_load_device` with that `uri`.
3. Right after loading, `local_sound_set_preset { file }` (it goes to the newest instance), then
   `local_sound_status`: that track's instance must show the `preset_name`. An empty
   `preset_name` means no preset is loaded yet — never tweak or write on top of that.
Load every synth track first, then write notes. Live's instruments only when the library has
nothing for that part (say so). **Drums are not Chatmu Sound** (no noise source, no percussion
presets): use a Live Drum Rack / kit or samples; a Chatmu Sound 808 can sit under it as the low end.

- Guitars: browser first (`local_ableton_browser` search `electric guitar`, `guitar`,
  `amp`, `cabinet`); load an instrument + Amp/Cabinet/Overdrive devices with
  `local_ableton_load_device`. If only synth: `local_sound_find_preset` `query: "rock guitar"`,
  `"guitar bright"`, `"rock bass"`; report `fallback: true`.
- **Double-tracking**: two separate guitar tracks playing the same part, panned −100 / +100,
  different presets/amp settings, and humanized separately (timing ±10–15 ms each). Copying
  one clip and panning it is not a double — it collapses to mono.
- Drums: acoustic kit (`kit`, `acoustic drum`, `rock kit`); never 808/909 for rock.
- Bass: picked electric (`bass`, `rock bass`) + light overdrive.
- Keys optional: organ (classic), synth pad/Mellotron-style strings (indie).

## 8. Arrangement (bars at 128 BPM; ≈ 3:20)
| Section | Bars | What plays |
|---|---|---|
| Intro | 4–8 | riff alone (one guitar) → full band on bar 5 |
| Verse 1 | 8–16 | drums (hats/cross-stick), bass, one guitar palm-muted or clean |
| Pre-chorus | 4 | build: toms/ride, guitars open up, snare 8ths last bar |
| Chorus 1 | 8 | both guitars L/R, crash, open hat/ride, vocal up |
| Riff break | 4 | intro riff returns |
| Verse 2 / Pre / Chorus 2 | 8 / 4 / 8 | + extra guitar line or harmony vocals |
| Bridge / solo | 8 | new chords (♭VI–♭VII) or half-time; lead guitar |
| Breakdown | 4 | drop to one guitar or drums only (quiet-loud) |
| Final chorus | 8–16 | everything, +1 octave lead, crash every 2 bars |
| Outro | 4 | riff, hold last chord, crash + ring out |
Name scenes with `local_ableton_scene_name`.

## 9. Mix targets
- Balance: vocal on top; snare ≈ kick, −2 to −3 dB under the vocal; guitars as a wall at −4
  to −6; bass −5.
- Low end: kick 60–80 Hz punch + 3–5 kHz beater; bass 80–200 Hz with growl at 700–1 kHz;
  guitars HPF 80–100 Hz, scoop 300–500 Hz 2–3 dB, presence 2–4 kHz.
- Guitars wide (L/R hard), bass/kick/snare/vocal centre, overheads/hats slightly spread.
- Space: room reverb on drums (0.8–1.2 s), short plate on snare, vocal slap delay 90–130 ms.
  Rock is drier and closer than pop.
- Loudness: −9 to −7 LUFS (hard rock/pop-punk), −11 to −9 (classic/indie); true peak ≤ −1
  dBTP. Keep crest: don't kill the snare transient. Check with `local_ears_track_levels`
  (guitars vs vocal masking) and `local_ears_listen`.

## 10. What ruins it
- Drum machine feel: flat velocities, no ghosts, no fills, perfect grid.
- One guitar copied and panned (fake double); or guitars in the centre fighting the vocal.
- Thirds in distorted chords; chords voiced above MIDI 64 for rhythm parts.
- No dynamics between verse and chorus; endless wall from bar 1.
- Synth/808 sounds in a "rock" track without asking.

## Workflow with the tools
1. `local_ableton_snapshot`; `local_ableton_set_tempo`.
2. Tracks (`local_ableton_edit_track` `create_midi`): Drums, Bass, Gtr L, Gtr R, Lead Gtr,
   Vocal guide.
3. Riff first on Gtr L → fire (`local_ableton_fire`) → drums with ghosts and fills → bass →
   Gtr R as a separate humanized take. Clips via `local_ableton_create_clip` +
   `local_ableton_write_notes`.
4. Load instruments/amps (`local_ableton_browser`, `local_ableton_load_device`); pan L/R.
5. Sections + scenes; verify harmony (`local_harmony_map`) and levels
   (`local_ears_track_levels`).
6. Suggest recording real guitar/bass if the user plays (`chatmu-studio-record`).

## Hard rules
- Riff before chords. Power chords (root-5-8) under distortion.
- Two different guitar performances, hard L/R — never a copied clip.
- Drums always humanized, with ghost notes, fills every 4–8 bars and crashes on section
  downbeats.
- Verse quieter/thinner than the chorus.
- Acoustic drum kit and amp'd guitars; no electronic drums unless the user asks.

## Tell the user (short)
`Alt rock · 128 BPM · E minor · 2-bar riff on low E pentatonic (syncopated on the "and" of 2) ·
verse i–♭VI–♭III–♭VII palm-muted, chorus opens to power chords with both guitars hard L/R ·
drums humanized with ghosts on steps 8/16 and a tom fill every 8 bars. Tracks: Drums, Bass,
Gtr L, Gtr R, Lead Gtr.`
