---
name: chatmu-studio-genre-afrobeats-amapiano
description: >
  Produces afrobeats / afropop (Nigerian and Ghanaian style) and amapiano
  (South African) in the user's Ableton Live set: the swung 16th "African
  swing", the 3+3+2 kick and conga cross-rhythms, shakers and rim patterns,
  the amapiano log drum bass, jazzy piano chords and the call-and-response
  vocal hooks. Trigger phrases: "afrobeats", "afrobeat", "afropop", "afro
  swing", "amapiano", "log drum", "piano house sudafricano", "Burna Boy style",
  "Wizkid type beat", "Asake style", "afro fusion", "afro house", "beat
  afro", "ritmo africano", "tipo amapiano", "hazme un afrobeat".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Afrobeats and amapiano: African swing, 3+3+2 cross-rhythms, shakers, log drum, jazzy keys"
version: "1.0"
tags: [studio, ableton, genre, afrobeats, afropop, amapiano, log-drum, african, groove]
requiresTools:
  - local_sound_status
  - local_ableton_snapshot
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
---

# Chatmu Studio — Afrobeats / afropop and amapiano

Two related but distinct genres. **Afrobeats** (Nigeria/Ghana, 95–115 BPM) is a mid-tempo
pop groove built from interlocking percussion with a swung 16th feel and a syncopated
"3+3+2" kick. **Amapiano** (South Africa, 110–115 BPM) is a slow house derivative: steady
shakers, sparse kick, jazzy piano and the **log drum** — a pitched, percussive bass that
carries the melody of the low end. Neither is "Fela afrobeat" (70s, long horn jams); say so
if the user means that.

Related: `chatmu-studio-hook-melody`, `chatmu-studio-drum-rack`, `chatmu-studio-humanize`,
`chatmu-studio-bass-lines`, `chatmu-studio-sound-design` (log drum), `chatmu-studio-genre-fusion`,
`chatmu-mix-by-genre`.

## 1. Brief
| Decision | Options | Default |
|---|---|---|
| Genre | afrobeats/afropop · afro-swing (UK) · amapiano (private-school/soulful or log-drum heavy) · afro house | afrobeats |
| Mood | romantic/mid · street/energetic · spiritual/soulful | romantic |
| Key | minor (most) · major (feel-good afropop) | F# minor |

## 2. BPM and feel
| Genre | BPM | Feel |
|---|---|---|
| Afrobeats | 98–112 (sweet spot 104–108) | 16ths swung 54–60% |
| Afro-swing | 95–105 | heavier swing, UK rap cadence |
| Amapiano | 110–115 (often 112–113) | straight 16ths on shakers, lazy (late) log drum |
| Afro house | 118–124 | four-on-floor, tribal percussion |
Apply swing by moving every off 16th (positions x.25 and x.75) later by 0.02–0.04 beat
(≈ 55–58%), or with `local_music_theory` `action: humanize`. Never fully straight in afrobeats.

## 3. Groove grid (one 4/4 bar, positions in beats)
**Afrobeats:**
- Kick (36): **3+3+2** = 0, 0.75, 1.5 (dotted-8th spacing) then 2, 2.75, 3.5 — or the lighter
  verse kick 0, 1.5, 2.0 (+ 3.5 pickup). Vel 100–115.
- Snare / clap (38/39) on 1.0 and 3.0 (vel 95–105), often a rim (37) instead in verses.
- Rim/stick cross pattern: 0.5, 1.25, 2.5, 3.25, 3.75 (vel 60–85) — the "tresillo" against the
  kick.
- Shaker (70): all 16ths, accents on x.0 and x.5 (85–95), ghosts on x.25/x.75 (45–60), swung.
- Hat (42): 8ths or off-beat 8ths (0.5, 1.5, 2.5, 3.5), vel 60–80.
- Congas/talking drum layer: open tones on 1.75 and 3.25, slaps on 2.5; vel 70–100.
- Percussive "log/tom" fills at the end of 4-bar phrases (16ths, toms descending).

**Amapiano:**
- Kick (36): sparse — 0 and 2.0, or just 0 with ghost on 2.5; often **no kick on every beat**.
  Vel 95–110, short (80–150 ms).
- Clap/snare on 1.0 and 3.0 with a second, softer clap 1/16 later (vel 70) — the flam clap.
- Shakers (70): continuous 16ths, accents on off-beat 8ths (x.5) at 85–95, others 45–65; layer
  a second shaker panned opposite with triplet-ish timing for "drag".
- Hats (42/46): open hat on the off-beats 0.5, 1.5, 2.5, 3.5 (vel 70–85).
- Wood/rim percussion in 3-against-4: notes every 0.75 beat (0, 0.75, 1.5, 2.25, 3.0, 3.75).
- **Log drum** as described in §6 — it is both bass and percussion.

## 4. Harmony
- Afrobeats: 2- to 4-chord loops, often diatonic minor with 7ths/9ths: i9 – iv9 (F#m9 – Bm9),
  vi – IV – I – V in major, ii7 – V7sus – I. Highlife-influenced guitars use major triads
  I – IV – V. One loop for the whole song is normal; variation comes from arrangement.
- Amapiano: jazz/gospel-derived — m9, maj7, 11ths, ii–V–I fragments, chromatic planing (move the
  same voicing up/down a semitone). E.g. Ebmaj9 – Dm7 – Gm9 – Cm11 (4 bars). Voicings mid
  register MIDI 55–79, spread, no root in the right hand.
- `local_music_theory` `action: chords` with explicit symbols (e.g. `F#m9`, `Bm9`) or
  `progression` preset `rnb` / `deep_house` as a starting point.
- **Avoid**: EDM I–V–vi–IV supersaws; power chords; trap minor-triad drones; changing chord
  every beat.

## 5. Melody and hook
Build with `chatmu-studio-hook-melody`. Genre specifics:
- **Short, chant-like, syncopated** hooks: 2–4 bar phrases repeated with tiny variations;
  pentatonic (major or minor) dominates, range a 5th–6th. Phrases start off-beat (x.25, x.5,
  x.75) and ride the swing.
- **Call-and-response**: lead line answered by a group vocal or a 1-bar instrumental riff
  (guitar, flute, sax).
- Afrobeats guitar: highlife-style picked lines in 16ths, two guitars interlocking (one on
  chord tones, one on 3rds/6ths), MIDI 60–84, clean tone.
- Amapiano: the hook is often a **vocal chop or whistled/sung refrain** over the piano; piano
  plays syncopated stabs (x.75, x.25 pushes) rather than sustained pads. Saxophone/flute
  improvisation at the climax.
- Pidgin/Yoruba/Zulu lyrics: never invent words in a language you don't know; leave placeholder
  syllables and say so (`chatmu-studio-lyrics-prosody`).

## 6. Bass
- **Afrobeats bass**: round, short, syncopated, following the kick partially: 0, 0.75, 1.5, 2.5,
  3.25 on root/5th/octave, MIDI 28–48, vel 90–105, notes 0.25–0.6 beat. Leaves space on 1.0/3.0
  for the snare.
- **Log drum** (amapiano): pitched percussive bass with fast pitch drop and slight distortion
  (sound design: sine/triangle body, pitch envelope down ~1 octave in 30–60 ms, decay 200–500 ms).
  Plays **melodic syncopated phrases** across 1–2 bars, e.g. 0.75, 1.25, 2.0, 2.5, 3.25, 3.75
  with leaps of octaves and 5ths, MIDI 33–57. Often lags 10–20 ms behind the grid. Vel 85–115;
  accent notes carry the riff. No pitch bend in the bridge: create the "slide" with a grace
  note 0.06 beat before the target, or by the preset's pitch envelope.
- Amapiano also uses a sub layer only under long log notes; never a separate competing bass line.

## 7. Sounds
**Chatmu Sound first (house rule).** Every bass and melodic part (bass/808, keys, pads, plucks,
leads, brass, strings…) gets **Chatmu Sound with a factory preset of this genre**, not Live's
stock instruments (Operator, Grand Piano, Electric…), which sound like generic MIDI:
1. `local_sound_find_preset` with `genre: "Afro"`, the `instrument` and a `character`. If it
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

- `local_sound_find_preset`: `"Bass Short"` / `"808 Short"` for log drum (then shape decay),
  `"Keys Warm"` (Rhodes-like amapiano piano), `"Guitar Bright"` (highlife guitar),
  `"Flute"`, `"Brass"` (sax hits), `"Vocal"` for chops. The factory lists no afro genre: expect
  `fallback: true`, say so.
- Browser (`local_ableton_browser`): `shaker`, `conga`, `talking drum`, `djembe`, `log drum`,
  `rimshot`, `wood block`, `cabasa`, `rhodes`. Load with `local_ableton_load_device`.

## 8. Arrangement (bars)
| Afrobeats | Bars | Amapiano | Bars |
|---|---|---|---|
| Intro (perc + guitar) | 4–8 | Intro (shakers + piano) | 16 |
| Verse 1 | 16 | Build (add kick, hats) | 16 |
| Hook | 8 | **Log drum drop** | 16–32 |
| Verse 2 | 16 | Break (drums out, piano/vocal) | 8–16 |
| Hook | 8 | Second drop (new log riff) | 16–32 |
| Bridge / perc break | 8 | Outro (strip back) | 16 |
| Hook ×2, Outro | 16 + 4 | | |
Amapiano tracks run long (5–7 min); afrobeats 2:40–3:30. Name scenes with
`local_ableton_scene_name`.

## 9. Mix targets
- Afrobeats: kick and bass share 50–120 Hz — sidechain bass lightly to kick or carve 2–3 dB;
  percussion wide (shakers ±40, congas ±25), vocal centre, upfront, plate 1.0–1.5 s.
- Amapiano: **log drum owns the low end** (40–150 Hz) and is the loudest low element; kick short
  and high-passed at 40 Hz under it; shakers bright and wide (8–12 kHz), piano mid with a
  2–2.5 s reverb send.
- Loudness: afrobeats −8 to −10 LUFS; amapiano −8 to −9 (club) — keep log drum transients.
- Check masking between log drum and kick with `local_ears_track_levels`.

## 10. What ruins it
- Straight, quantized 16ths in afrobeats (no swing).
- Trap hats rolls and 808 glides over an afro groove.
- Amapiano with a four-on-the-floor kick (that is afro house).
- Log drum used as a sustained sub (it must be percussive and melodic).
- Busy chord changes; long sustained pads covering the percussion.

## Workflow with the tools
1. `local_ableton_snapshot`; `local_ableton_set_tempo`.
2. Tracks (`local_ableton_edit_track` `create_midi`): Drums, Shakers/Perc, Bass or Log Drum,
   Keys/Guitar, Hook, Vocal Guide.
3. Drums + shakers (`local_ableton_create_clip`, `local_ableton_write_notes`), swing applied →
   fire (`local_ableton_fire`).
4. Bass/log drum → fire. Chords (`local_music_theory` `chords`) → fire.
5. Hook/call-and-response; check with `local_harmony_map`.
6. Balance and masking with `local_ears_track_levels`.

## Hard rules
- Name genre, BPM, key and swing amount.
- Afrobeats is swung; amapiano shakers stay steady and the log drum lags slightly.
- Only one low-end owner: bass (afrobeats) or log drum (amapiano).
- Keep loops; change energy by layers, not chords.
- Never fake lyrics in African languages.

## Tell the user (short)
`Amapiano · 113 BPM · Eb major/C minor · Ebmaj9 – Dm7 – Gm9 – Cm11 Rhodes stabs · sparse kick,
flam clap on 2 and 4, 16th shakers accented off-beat · log drum riff in octaves lagging ~15 ms ·
16-bar drop. Tracks: Drums, Shakers, Log Drum, Keys, Hook.`
