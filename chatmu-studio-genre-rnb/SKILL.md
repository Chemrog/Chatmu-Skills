---
name: chatmu-studio-genre-rnb
description: >
  Produces contemporary R&B and neo-soul in the user's Ableton Live set:
  extended chords (maj7, m9, 11, 13) in drop-2 voicings, ii–V and IV–iii–vi
  motion, a laid-back swung 16th groove behind the beat, sparse drums with
  rimshots and snaps, a sub or finger bass with slides, and a melismatic,
  pentatonic topline with space around it. Trigger phrases: "R&B", "rnb",
  "neo soul", "slow jam", "soulful beat", "smooth R&B", "alt R&B",
  "Rhodes chords", "beat de R&B", "hazme un R&B", "neo soul", "algo
  sensual", "rola lenta", "acordes jazzeros", "beat suave".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Contemporary R&B / neo-soul: 7ths-9ths in drop-2, laid-back swing, sparse drums, melismatic topline"
version: "1.0"
tags: [studio, ableton, genre, rnb, neo-soul, slow-jam, alt-rnb, rhodes, swing]
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
  - local_harmony_map
  - local_ears_track_levels
  - local_ears_listen
---

# Chatmu Studio — Contemporary R&B and neo-soul

R&B lives in **the chords and the pocket**. The harmony is jazz-derived (7ths, 9ths, 11ths,
13ths) but voiced warm and low-mid, the drums are sparse and late, and the vocal floats with
lots of air between phrases. It sounds "AI-made" when the chords are block root-position
7ths, the drums are quantized with hats on every 16th at one velocity, and the topline sings
every beat.

Related: `chatmu-studio-harmony` (voicings), `chatmu-studio-hook-melody`,
`chatmu-studio-harmonize-melody`, `chatmu-studio-bass-lines`, `chatmu-studio-humanize`,
`chatmu-studio-drum-rack`, `chatmu-studio-counter-melody`, `chatmu-mix-by-genre`.

## 1. Brief (ask only what is missing; propose defaults)
| Sub-style | BPM | Signature |
|---|---|---|
| Contemporary / alt R&B | 60–80 (or 120–160 double time) | trap-ish hats, dark pads, 808 or sub |
| Neo-soul | 75–95 | Rhodes, live-feel drums, heavy swing, finger bass |
| Slow jam / 90s R&B | 60–72 | lush pads, 6/8 or swung 4/4, strings |
| Upbeat R&B / funk-soul | 95–110 | clav/guitar 16ths, slap/finger bass |
Default: contemporary R&B 70 BPM, D♭ major / B♭ minor (flat keys suit Rhodes and singers).

## 2. BPM & feel
- Swing 55–62 % on 16ths (neo-soul up to 66 %). Apply with `local_music_theory`
  `action: humanize`.
- **Behind the beat**: snare/clap 10–25 ms late, hats ±8 ms, kick ±5 ms; keys chords
  rolled (strum 10–30 ms bottom to top) and placed 5–15 ms late.
- If the set is at double tempo (140 for a 70 feel), the snare is on step 9 (half-time).

## 3. Groove grid (16 steps, step 1 = beat 1; beats = (step−1)/4)
```
R&B — 60–80 BPM
Kick    X . . . . . . X . . X . . . . .   steps 1 8 11            vel 100–115
Snare   . . . . X . . . . . . . X . . .   steps 5 13 (rim/snaps)  vel 90–110
Hat     16ths swung 55–62 %, vel 50–80 accented on 8ths; occasional 1/32 or triplet runs
Ghosts  snare/rim steps 7 15 vel 25–45
NEO-SOUL — 80–95: kick 1 4 11 (lazy), snare 5 13 behind, hats 8ths with open hat step 15
ALT R&B (double time 140): kick 1 8 11, snare 9, hats 8ths with triplet rolls into bar 4
```
- Sparse: often only kick + snare/rim + one hat pattern; shaker or snaps (39) on 2 and 4 for
  verses. Fills are minimal: one triplet hat roll or a reverse cymbal into the chorus.
- Velocity is the groove: hats alternate strong/weak; never more than two identical
  velocities in a row.
- `local_music_theory` `action: drum_pattern` with `lofi` or `boombap` gives a close base at
  70–90; `trap` for alt R&B. Then swing and push the snare late.

## 4. Harmony
- Every chord has a 7th; colour tones 9, 11, 13. One chord per bar, or two (beats 1 and 3)
  in turnarounds. `local_music_theory` `action: progression` preset `rnb`.
- Moves: ii9–V13–Imaj9 · IVmaj9–iii7–vi9 (–ii9–V) · Imaj7–vi9–ii9–V7♭9 · iim9–♭IImaj7 (tritone
  sub)–Imaj9 · minor: i9–iv9–♭VImaj7–V7♯9 · Dorian vamp i9–IV9 (neo-soul).
- Borrowed: ivm9 in a major key (the "soul" sigh), ♭VII9, backdoor ♭VII9–Imaj7.
- **Voicings**: drop-2 (take the 2nd-highest note of a close voicing down an octave) or
  rootless (3-7-9 / 7-3-13). Left hand/bass plays the root; keys play 3rd/7th/9th/13th in
  MIDI 52–74. Example Dbmaj9 rootless: F Ab C Eb (MIDI 53 56 60 63). Top voice moves by step.
- Anticipation: chord hits on the "and" of 4 (step 15) of the previous bar ~half the time.
- Avoid: plain triads, power chords, root-position stacks with the 3rd in MIDI < 48 (mud),
  more than one tritone sub per loop, 13♭9♯11 clusters on every chord.
- Write voicings with `local_music_theory` `action: chords`, then re-voice by hand; check
  with `local_harmony_map`.

## 5. Melody / hook (on top of `chatmu-studio-hook-melody`)
- Pentatonic + chord extensions: target the 9th and the 7th on strong beats (not the root)
  — that's the R&B colour.
- **Melisma**: on held syllables write runs of 3–7 notes in 16th/32nd/triplet values down the
  pentatonic (e.g. 9–1–6–5–3), velocity lower than the target (60–80 vs 90–100). One run per
  phrase, mostly at phrase ends; the hook itself stays simple and singable.
- Phrases start late (the "and" of 1 or beat 2), leave 1–2 beats of air; call-and-response
  with keys fills.
- Range: verse MIDI 60–69, chorus 65–76 (falsetto peaks up to 79 for male voices).
- Hook = a short repeated phrase in the chorus with stacked harmonies (3rds and 6ths, close
  voicing, −6 to −10 dB) under the lead.
- Ad-libs: high, sparse, panned ±30–60 %, in the gaps.

## 6. Bass
- Contemporary: sub/808 (MIDI 24–40) on the root, long notes, slides faked as short
  chromatic 32nd approach notes (no pitch bend) or portamento on the synth.
- Neo-soul: finger bass, chord tones + chromatic approach notes on step 15–16, ghost notes
  vel 40–55, laid back 10–20 ms. Lots of rests; plays with the kick on step 1 and 11.
- Bass plays the root even when keys are rootless; move to the 3rd/5th for inversions only on
  passing chords. Details in `chatmu-studio-bass-lines`.

## 7. Sounds
- `local_synth_find_preset` `query`: `"rnb keys warm"`, `"rnb bass"`, `"rnb 808"`,
  `"rnb strings"`, `"rnb pad dark"`, `"rnb bell"`; if `fallback: true`, say it.
- Palette: Rhodes/Wurli electric piano (with tremolo/chorus), warm pad, soft lead or flute,
  picked clean guitar (neo-soul), strings for slow jams, finger snaps, rim, soft kick.
- Browser fallbacks (`local_ableton_browser` → `local_ableton_load_device`): `Electric
  Piano`, `Rhodes`, `Wurli`, `Lounge`, kits `soul`, `lofi`, `808`; devices Chorus-Ensemble,
  Auto Pan (tremolo), Saturator.

## 8. Arrangement (bars at 70 BPM; ≈ 3:15)
| Section | Bars | What plays |
|---|---|---|
| Intro | 4 | keys alone (rolled chords), filtered, or vocal ad-lib |
| Verse 1 | 8 | kick + rim + hats, bass, keys sparse; vocal low |
| Pre-chorus | 4 | add pad, turnaround ii–V, drums thin out |
| Chorus | 8 | full drums, stacked harmonies, strings/pad |
| Verse 2 | 8 | + counter-line (guitar/flute) and hat variations |
| Pre / Chorus 2 | 4 / 8 | |
| Bridge | 8 | new key area (♭VI or relative minor), drums drop, melisma |
| Final chorus | 8 | + ad-libs, maybe modulate up a half step |
| Outro | 4–8 | vamp on two chords with ad-libs, fade |
Name scenes with `local_ableton_scene_name`.

## 9. Mix targets
- Vocal on top and intimate; kick and bass next (−3 to −5 dB under vocal), keys −6 to −9,
  hats quiet (−12 or lower).
- Low end: sub/808 30–60 Hz; kick 60–90 Hz (sidechain or EQ split); keys HPF 100–150 Hz,
  cut 250–400 Hz 2–3 dB; warm the keys with saturation not boosts.
- Space: lush hall/plate on vocal (2–3 s, pre-delay 30–60 ms) via return; 1/4 dotted delay on
  ad-libs; keys in stereo chorus; drums dry and close.
- Loudness: −11 to −9 LUFS (contemporary), −13 to −10 (neo-soul/slow jam); true peak ≤ −1
  dBTP. Don't over-compress: keep the groove's velocity dynamics. Check with
  `local_ears_track_levels` (keys vs vocal 1–4 kHz) and `local_ears_listen`.

## 10. What ruins it
- Quantized drums on the grid; snare on time; dense 16th hats at one velocity.
- Block chords with no voice leading, or triads with no 7ths.
- Topline filling every beat, or melisma on every word.
- Too many layers: R&B is 4–6 parts playing at once, max.
- Bright, compressed EDM-style mix; harsh hats.

## Workflow with the tools
1. `local_ableton_snapshot`; `local_ableton_set_tempo`.
2. Tracks (`local_ableton_edit_track` `create_midi`): Keys, Drums, Bass, Pad, Topline,
   Counter.
3. Chords first: progression → drop-2/rootless voicings → rolled and late
   (`local_ableton_create_clip`, `local_ableton_write_notes`); fire (`local_ableton_fire`).
4. Drums sparse with swing and late snare; then bass. Fire after each layer.
5. Topline with targeted extensions and one melisma per phrase; check with
   `local_harmony_map`; levels with `local_ears_track_levels`.
6. Tell the user and propose next (vocal stacks, arrangement, mix).

## Hard rules
- Every chord gets a 7th (or 6/9); voice-led drop-2 or rootless voicings in MIDI 52–74.
- Swing 55–62 % and snare behind the beat; never on the grid.
- Drums sparse; velocity variation on every hat.
- Melisma at phrase ends only; the hook stays simple.
- Leave air: at least 1 beat of silence between vocal phrases.

## Tell the user (short)
`Contemporary R&B · 70 BPM · D♭ major · G♭maj9–Fm7–B♭m9–E♭13 in drop-2 Rhodes, rolled and
15 ms late · kick 1/8/11, rim on 2 and 4 pushed 20 ms back, hats swung 58 % · sub bass with
chromatic slides · topline lands on the 9th, one pentatonic run at each phrase end. Tracks:
Keys, Drums, Bass, Pad, Topline.`
