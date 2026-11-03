---
name: chatmu-studio-genre-reggaeton
description: >
  Produces reggaetón in the user's Ableton Live set: straight dembow (3-3-2
  tresillo feel) at 88–100 BPM, minor-key i–♭VI–♭III–♭VII loops and variants,
  tresillo 808/sub bass, plucked or piano chords, Latin-urban vocal pockets,
  and the three flavours — perreo, romántico/pop and moombahton-leaning.
  Trigger phrases: "reggaeton beat", "make a reggaeton", "dembow", "perreo",
  "Latin urban", "romantic reggaeton", "moombahton", "hazme un reggaetón",
  "beat de reggaetón", "dembow", "perreo duro", "reggaetón romántico",
  "música urbana", "algo tipo Bad Bunny", "ritmo de reggaetón".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Reggaetón: straight dembow, i–♭VI–♭III–♭VII loops, tresillo bass, perreo / romántico / moombahton flavours"
version: "1.0"
tags: [studio, ableton, genre, reggaeton, dembow, perreo, latin, urbano, moombahton]
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
  - local_ears_track_levels
  - local_harmony_map
---

# Chatmu Studio — Reggaetón

Reggaetón is a **hypnotic loop under a voice**: the dembow never stops, the 4-bar progression
repeats the whole song, and interest comes from the vocal, drops, percussion layers and
filter moves. It sounds fake when the dembow is quantized at one velocity with no timbal/perc
layer, when the bass ignores the tresillo, when the chords are bright pop changes, or when the
producer fills every pocket the singer needs.

Related: `chatmu-studio-hook-melody`, `chatmu-studio-afro-cuban-rhythms` (tresillo, clave
background), `chatmu-studio-bass-lines`, `chatmu-studio-drum-rack`, `chatmu-studio-humanize`,
`chatmu-studio-lyrics-prosody`, `chatmu-studio-arrangement`, `chatmu-mix-by-genre`.

## 1. Brief (ask only what is missing; propose defaults)
| Decision | Options | Default |
|---|---|---|
| Flavour | perreo (hard, club) · romántico/pop (melodic, softer) · old-school (2000s, sparse synth) · moombahton-leaning (108–112, house-ish synths) | perreo |
| Tempo | 88–100 (most hits 90–96) · moombahton 105–112 | 94 |
| Key | natural minor; harmonic minor if the hook wants a V | A minor or C# minor |
| Chord voice | pluck · piano · guitar (nylon/acoustic) · pad · bell | pluck |
| Vocal | rapped/flowed (needs space) · sung (melodic hook) | sung hook + flowed verse |

## 2. Tempo & feel
- **Straight 16ths, no swing.** The feel is the dembow's 3-3-2 accent pattern (tresillo) against a
  four-on-the-floor kick.
- Each bar = two "dembow cells"; each cell of 2 beats accents 0, 0.75, 1.5 (3+3+2 sixteenths).
- Romántico sits at 88–92, perreo 92–100, old-school up to 100, moombahton 108–112 (it grew from
  slowing Dutch house to ~108 with a dembow-like kick).

## 3. Groove grid (1 bar; beats from bar start; steps 1–16)
Drum Rack: 36 kick, 38 snare, 37 rim, 39 clap, 42 closed hat, 46 open hat, 70 shaker.
`local_music_theory` `action: drum_pattern` `genre: reggaeton` returns this skeleton.

| Element | Positions (beats) | Steps | Velocity |
|---|---|---|---|
| Kick (36) | 0, 1, 2, 3 | 1 5 9 13 | 105–120, beat 1 hardest |
| Snare (38) | 0.75, 1.5, 2.75, 3.5 | 4 7 12 15 | 95–115, accents on 0.75/2.75 |
| Rim or clap (37/39) | same as snare | 4 7 12 15 | 70–90, layered timbal colour |
| Closed hat (42) | 8ths 0, 0.5 … 3.5 (or 16ths) | odd steps | 60–80 (16ths: 45–70, on-beats louder) |
| Shaker (70) | 16ths | all | 35–60, accent the "&"s |
| Open hat (46) | 1.5 or 3.5, every 2 bars | 7 / 15 | 65–80 |
- **Timbal/perc layer** on its own track: high tom/timbale hits on 0.75, 2.75 and fills of 16ths
  in the last beat of every 4th bar (velocity 50–90 rising). This layer is what makes it Latin
  and not a preset loop.
- Variations every 4–8 bars: drop the kick on beat 1 (just snare cell), a snare roll in 16ths
  across beat 4 (velocity 60→110), or a half-bar with only kick.
- **Perreo**: harder kick, snare layered with a clap, louder rim, more drops (1 bar of only vocal +
  808 before the chorus).
- **Romántico**: softer snare (velocity 85–100), shaker/guitar carry the motion, fewer fills.
- **Old-school**: "Pounder" kit sound — brighter, drier snare, square-wave
  lead stabs, fewer layers.
- **Moombahton-leaning**: same dembow on top of the 4/4 kick at 108–112; bigger snare reverb,
  wobbly mid bass and house synths.
- Humanize the snare/rim layers ±5 ms and velocity ±6 (`local_music_theory` `action: humanize`);
  keep the kick on grid.

## 4. Harmony
- Default **i – ♭VI – ♭III – ♭VII** (Am – F – C – G), 1 chord per bar, 4-bar loop for the whole song.
  `local_music_theory` `action: progression` `genre: reggaeton`.
- Variants: **i – iv – ♭VII – ♭III** (Am – Dm – G – C); **i – ♭VII – ♭VI – ♭VII**; **♭VI – ♭VII – i – i**
  (start on the lift); **i – iv – v – i** (Am – Dm – Em – Am) old-school; harmonic minor
  **i – ♭VI – V** with E major for the hook's leading tone.
- Romántico allows add9 / maj7 colours (Fmaj7, Cadd9) and suspended chords; perreo uses plain
  triads or just a 2-note riff.
- Rhythm of chords: plucks/piano follow the dembow (stabs on 0, 0.75, 1.5, 2, 2.75, 3.5) or a 16th
  arpeggio; pads hold whole bars. Voicing MIDI 55–76, no notes under 50 (the bass owns that).
- **Avoid**: bright major I–IV–V, jazz ii–V, chords changing twice per bar, dense 7th voicings in
  perreo.

## 5. Hook / melody specifics
Build the motif with `chatmu-studio-hook-melody`; in reggaetón:
- **The hook is the vocal.** The instrumental riff (pluck, flute, bell, guitar) is a 1–2-bar motif
  that sets up the topline and then gets out of its way.
- **Syncopation from the tresillo**: melody notes on 0.75 and 1.5 within each 2-beat cell, often
  anticipating the bar by a 16th (start at 3.75 of the previous bar).
- **Vocal pockets**: Latin-urban flows ride 16ths with pickups; sung hooks use repeated notes on
  the 5th and 3rd, falling to the root at the cadence. Leave 4–8 kHz and 300 Hz–3 kHz clear for
  the voice; the riff sits above (MIDI 72–90) or answers between lines.
- Scale-tone choices: natural minor; ♭6–5 and 2–♭3 for the melancholic romántico colour; the
  raised 7th only when the chord is V.
- Call-and-response: vocal line (2 bars) → riff answer (1 bar) → vocal → riff.
- Spanish prosody: stressed syllables (aguda/llana) on strong 16ths — see
  `chatmu-studio-lyrics-prosody`.

## 6. Bass
- **Tresillo per 2 beats**: starts 0, 0.75, 1.5, 2, 2.75, 3.5; durations 0.75, 0.75, 0.5 (repeat);
  root of the bar's chord; octave on the 2nd hit optional.
- Example Am–F–C–G, roots A=45, F=41, C=48 (or 36 for a lower sub), G=43; bar 1: (45, 0, 0.75),
  (45, 0.75, 0.75), (45, 1.5, 0.5), (45, 2, 0.75), (57, 2.75, 0.75), (45, 3.5, 0.5); velocity 100–115.
- Sub/808 range MIDI 33–48; tonic around 33–45. Short notes in perreo for punch; longer sustained
  808 in romántico with an occasional glide into the next chord's root (overlap 0.125 beat +
  glide enabled on the device).
- The kick hits every beat: kick short (≤ 120 ms) and the bass sidechained 2–4 dB, or tune the kick
  to the key.

## 7. Sounds
- `local_synth_find_preset` with `query: "reggaeton pluck"`, `"reggaeton 808"`,
  `"guitar warm"`, `"keys"`, `"flute"`, `"bell"`, `"synth bright"`, `"brass"`. If the genre returns
  `fallback: true`, say so.
- Browser fallbacks (`local_ableton_browser`): `reggaeton kit`, `dembow`, `timbale`, `perc`,
  `nylon guitar`, `marimba`. Load with `local_ableton_load_device`.
- Old-school: square/saw lead with short decay. Romántico: nylon guitar, Rhodes-ish keys, soft pad.
  Moombahton: detuned saws, horns-like synth stabs.

## 8. Arrangement (bars at 94 BPM; 1 bar ≈ 2.55 s; ~3 min ≈ 70 bars)
| Section | Bars | What plays |
|---|---|---|
| Intro | 4–8 | riff + pad, filtered (low-pass 800 Hz → open), no kick; artist/producer tag |
| Verse 1 | 16 | dembow + bass, chords reduced; vocal flow |
| Pre-chorus | 4–8 | drop kick or bass, risers of snare 16ths, filter opens |
| Chorus | 8–16 | everything + perc layer + riff answers |
| Verse 2 | 16 | variation: different perc, half-bar drops |
| Chorus | 8–16 | full |
| Bridge | 8 | strip to chords + voice, or a perreo break (only drums + bass) |
| Chorus | 8–16 | full, extra layer |
| Outro | 4–8 | riff + vocal tags, filter closes |
- The main transition is the **drop-out**: 1 beat to 1 bar of silence or vocal only, then the
  dembow slams back on beat 1. Name scenes with `local_ableton_scene_name`.

## 9. Mix targets
- Low end: sub/808 at 40–80 Hz, kick punch 60–100 Hz, everything else high-passed (chords 150 Hz,
  hats/perc 300 Hz+).
- Relative levels (bass = 0 dB): kick -1 to -3, snare -2 to -4, rim -6 to -9, hats -12 to -15,
  shaker -16 to -20, chords -8 to -12, riff -6 to -9 (drops under the vocal).
- Space: short plate on the snare (0.6–1.2 s), delay throws (1/8 dotted) on the riff and vocal ends;
  bass and kick mono and dry.
- Loudness: master **-8 to -6 LUFS** integrated, true peak ≤ -1 dBTP; mixdown at -14 to -10 LUFS
  before mastering (`chatmu-master-chain`).
- Check `local_ears_track_levels` for kick/bass masking and the riff vs vocal band; `local_ears_listen`
  for the full mix.

## 10. What ruins it
- Swing on the dembow, or the snare on 2 & 4 instead of 0.75/1.5/2.75/3.5.
- No percussion layer: a bare 3-element loop sounds like a demo preset.
- Bass on straight 8ths or holding whole notes in perreo.
- Major pop progressions; chord changes every 2 beats.
- A riff that plays over every vocal line.
- Over-long reverb on the dembow; a kick with a long boomy tail fighting the bass every beat.

## Workflow with the tools
1. `local_ableton_snapshot`; `local_ableton_set_tempo` (94 default).
2. Tracks (`local_ableton_edit_track` `create_midi`): Dembow, Perc, Bass, Chords, Riff;
   `local_ableton_tracks` to confirm indices.
3. Dembow: `local_music_theory` `drum_pattern` `reggaeton` → add rim layer, shaker, velocities →
   `local_ableton_create_clip` (4 bars) → `local_ableton_write_notes` → `local_ableton_fire`.
4. Perc layer (timbal fills) → bass tresillo on the chord roots → fire with drums.
5. Chords from `progression` `reggaeton`, rhythm following the dembow; check with `local_harmony_map`.
6. Riff last, leaving vocal space. Fire after each layer so the user can stop you.
7. Rough levels with `local_ableton_mixer`; `local_ears_track_levels` for masking; name scenes.

## Hard rules
- Straight grid; snare at 0.75, 1.5, 2.75, 3.5; kick on every beat.
- Bass follows the tresillo and the chord root.
- One 4-bar loop for the song; variation by arrangement, not by new chords.
- Always add a perc/timbal or shaker layer with real velocity movement.
- Leave the vocal's pockets; the riff answers, it doesn't duet.
- Say the flavour, key, tempo and progression.

## Tell the user (short)
`Reggaetón perreo · 94 BPM · A minor · Am–F–C–G one bar each · dembow (kick every beat, snare +
rim on 0.75/1.5/2.75/3.5) + shaker 16ths + timbal fill every 4 bars · tresillo sub on the roots ·
pluck stabs on the dembow, 1-bar riff answering the vocal. Tracks: Dembow, Perc, Bass, Chords,
Riff. Next: arrange intro/verse/chorus, or make it romántico at 90?`
