---
name: chatmu-studio-genre-pop
description: >
  Produces modern pop in the user's Ableton Live set: topline-first, hook in
  the first 10 seconds, a pre-chorus that lifts, a chorus sung in the high
  register, four-chord loops with real voice leading, a tight kick/bass pocket
  and a loud, clean, vocal-forward mix. Covers dance-pop, synth-pop, pop
  ballad and acoustic/bedroom pop. Trigger phrases: "pop song", "make it pop",
  "radio song", "catchy song", "dance pop", "synth pop", "pop ballad",
  "chorus that hits", "canción pop", "hazme un pop", "algo comercial",
  "canción de radio", "pop bailable", "balada pop", "coro pegajoso",
  "que suene a radio".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Modern pop: hook in 10 s, pre-chorus lift, high-register chorus, four-chord loop, vocal-forward loud mix"
version: "1.0"
tags: [studio, ableton, genre, pop, dance-pop, synth-pop, ballad, topline, hook]
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

# Chatmu Studio — Modern pop

Pop is **topline-driven**: the beat exists to frame one melody and one lyric line. Everything
is judged by "does the chorus land harder than anything before it?". The production is simple
on paper (four chords, backbeat, eighth-note bass) — the craft is in contrast between sections,
register, and leaving the vocal band (1–5 kHz) for the voice. What makes pop sound "AI-made":
every section the same density, a chorus no higher than the verse, chords that jump in root
position, quantized MIDI at velocity 100.

Related: `chatmu-studio-hook-melody` (motif, repetition, peak — this skill gives the pop
specifics), `chatmu-studio-harmonize-melody`, `chatmu-studio-lyrics-prosody`,
`chatmu-studio-drum-rack`, `chatmu-studio-bass-lines`, `chatmu-studio-humanize`,
`chatmu-studio-sidechain`, `chatmu-studio-arrangement`, `chatmu-mix-by-genre`.

## 1. Brief (ask only what is missing; propose defaults)
| Decision | Options | Default |
|---|---|---|
| Sub-style | dance-pop 118–126 · synth-pop 100–120 · mid-tempo pop 95–110 · ballad 65–80 · bedroom/acoustic 80–100 | mid-tempo 104 |
| Mood | bright/euphoric · bittersweet · dark/moody · intimate | bittersweet |
| Key | major or minor; pick for the singer's range (chorus peak ≈ top of their comfortable belt) | A♭ major / F minor |
| Vocal | user sings · guide vocal later · instrumental topline (synth/piano) | topline on a lead synth |

## 2. BPM & feel
- Straight 16ths, swing 0–8 % (dance-pop 0 %, mid-tempo 5 %, bedroom pop up to 12 % on hats).
- Half-time verse / full-time chorus is a pop staple at 140–160 BPM (snare on beat 3 in verse,
  on 2 and 4 in chorus) — the tempo doesn't change, the felt pulse doubles.
- Ballad: 8ths on piano, drums enter at chorus 1 or verse 2, never from bar 1.

## 3. Groove grid (16 steps per bar, step 1 = beat 1; beats = (step−1)/4)
```
POP — 100–125 BPM
Kick    X . . . . . . . X . X . . . . .   steps 1 9 11          vel 110–120
Snare   . . . . X . . . . . . . X . . .   steps 5 13 (+clap)     vel 105–115
C. hat  X . X . X . X . X . X . X . X .   8ths                   vel 70–90, offbeats −10
Shaker  16ths in chorus only                                     vel 45–65
DANCE-POP — 118–126: kick four-on-floor steps 1 5 9 13, clap 5 13, open hat steps 3 7 11 15
HALF-TIME VERSE: kick 1 8 11, snare step 9 only
```
- Pre-chorus: drop the kick for the last 1–2 bars, snare 8ths → 16ths roll (vel 60 → 110) in
  the final bar, or full silence on the last beat (the "pre-chorus gap") so the chorus downbeat
  hits.
- Chorus adds: shaker/tambourine 16ths, crash on bar 1 (vel 100), clap layer, sometimes an
  extra kick on step 15 every 2nd bar.
- Fills only into sections: 1 beat of snare/tom 16ths, vel ramp 70 → 110.
- `local_music_theory` `action: drum_pattern` has no pop preset: use `house` for dance-pop and
  write the grid above for everything else. Humanize: timing ±8 ms, velocity ±8
  (`action: humanize` or `chatmu-studio-humanize`); kick stays tight (±3 ms).

## 4. Harmony
- Four chords, one per bar (or two per bar in pre-chorus to accelerate). `local_music_theory`
  `action: progression` presets `pop` and `sad` give the base.
- Workhorses: I–V–vi–IV · vi–IV–I–V · I–vi–IV–V · IV–I–V–vi · minor i–♭VI–♭III–♭VII.
- **Pre-chorus** changes the loop: start on IV or ii and end on V (or ♭VII/IVsus) so it leans
  into the chorus I. Rising bass line (e.g. 4–5–6) under the pre-chorus = lift.
- **Chorus** can reuse the verse chords — the melody and arrangement provide contrast — or
  start on IV for a "soaring" open.
- Colour: add9, sus2/sus4, IV/5 slash chords; minor iv borrowed in a major key for the
  bittersweet bar. Max one or two colour chords per loop.
- Voice leading: keep pads/keys in MIDI 55–72, move by common tones (inversions), top note
  stepwise. Never four root-position triads jumping in parallel.
- Avoid: jazz ii–V–I chains, chords changing every beat in the chorus, dominant 7ths on every
  V, more than 5 distinct chords in the song's main loop.

## 5. The hook (pop specifics on top of `chatmu-studio-hook-melody`)
- **Hook within the first 10 s**: either the chorus hook as the intro (instrumental or
  chopped) or a 1-bar post-chorus riff/vocal chop that recurs. At 104 BPM, 10 s ≈ 4 bars.
- **Register map** (sung): verse MIDI 57–67 (low, talky), pre-chorus climbs 60–70, chorus
  peaks 67–76 — the chorus's top note is the song's highest sustained note, a 4th to an octave
  above the verse's top note.
- Chorus melody: short title phrase (2–5 syllables) on a strong downbeat, repeated 2–4 times;
  phrases start on beat 1 or the "and" of 4 (anticipation).
- Verse melody: more syllables, 16th-note rhythm, narrow range (a 5th); contrast = chorus has
  longer notes (quarters/halves) and fewer words.
- Pre-chorus: rising sequence, rhythm accelerates or stalls on one repeated note, ends on an
  unresolved scale degree (2 or 5) over V.
- Post-chorus: wordless or one-word vocal chop / synth riff (`chatmu-studio-vocal-chops`),
  often a 1-bar repeated motif in MIDI 72–84.
- Rhythm of the hook = lyric prosody (`chatmu-studio-lyrics-prosody`); stressed syllables on
  beats 1 and 3.
- Doubles: chorus lead doubled in unison (2nd take/voice −6 dB, panned 0) plus octave above
  at −12 dB; harmony a 3rd above only on the title line.

## 6. Bass
- Root notes in 8ths locked to the chord, MIDI 28–43 (E0–G1 in Live's naming = E1–G2
  standard). Synth-pop: 8th pulse with octave jumps on offbeats. Mid-tempo: follow the kick
  (steps 1 9 11) with a passing note on step 15 into the next chord.
- Dance-pop: offbeat bass (steps 3 7 11 15) or rolling 16ths sidechained to the kick
  (`chatmu-studio-sidechain`, 3–6 dB duck).
- Ballad: whole/half notes, enters at chorus 1. Details in `chatmu-studio-bass-lines`.

## 7. Sounds
- `local_synth_find_preset` with `query` like `"pop keys warm"`, `"pop synth bright"`,
  `"pop bass short"`, `"pop pluck"`, `"pop strings"`, `"pop vocal"`. If `fallback: true`,
  say so and load the nearest with `local_synth_set_preset`.
- Core palette: piano or Rhodes-style keys, pluck/arp for the post-chorus, wide pad, short
  synth or picked bass, acoustic or clean electric guitar (browser: `acoustic guitar`,
  `clean guitar`), claps + snare layer, finger snaps for verses.
- Browser fallbacks (`local_ableton_browser` → `local_ableton_load_device`): `Grand Piano`,
  `Electric Piano`, `Drift`/`Wavetable` presets with `pluck`, `pad`; drum kits `pop`,
  `909`, `acoustic`.

## 8. Arrangement (bars at 104 BPM; total ≈ 3:00)
| Section | Bars | What plays |
|---|---|---|
| Intro | 4 | hook/post-chorus riff, filtered or piano only |
| Verse 1 | 8–16 | kick+snaps, bass, one keys layer; vocal low |
| Pre-chorus | 4–8 | add pad/risers, kick drops last bar, rising bass |
| Chorus 1 | 8 | everything; crash; doubles; widest |
| Post-chorus | 4 | riff/chop over drums+bass |
| Verse 2 | 8 | as verse 1 + one new element (counter-line, hats 16ths) |
| Pre-chorus 2 | 4–8 | |
| Chorus 2 | 8 | + extra layer |
| Bridge | 8 | new chords (start on vi or IV), strip drums, or half-time |
| Final chorus | 8–16 | biggest; optional key change up a whole step (sparingly) or drop-out first 4 bars |
| Outro | 4 | post-chorus riff, cut clean |
First chorus by 0:50 at latest. Name scenes with `local_ableton_scene_name`. Full form:
`chatmu-studio-arrangement`.

## 9. Mix targets
- Vocal/topline is the loudest element; kick and snare next (−2 to −4 dB under the vocal),
  bass −4 to −6, keys/pads −8 to −12.
- Low end: kick fundamental 50–70 Hz, bass 70–120 Hz; HPF everything else at 120–200 Hz.
  Cut 2–4 kHz on keys/guitars 2–3 dB where the vocal sits.
- Space: short plate on vocal (1.2–1.8 s, pre-delay 20–40 ms) via return; 1/4 or 1/8 dotted
  delay at −18 dB on chorus lead; verses drier than choruses.
- Width: verse narrow, chorus wide (pads/doubled guitars L/R ±60–100 %).
- Loudness: −9 to −7 LUFS integrated for dance-pop, −10 to −8 for mid-tempo, −12 to −10 for
  ballads; true peak ≤ −1 dBTP. Check with `local_ears_track_levels` (masking vocal vs keys)
  and `local_ears_listen` (indicative).

## 10. What ruins it
- Chorus not higher/louder/wider than the verse.
- Intro longer than 8 bars before anything memorable.
- Pads, guitar and keys all in 300 Hz–3 kHz at once — mud that buries the vocal.
- Same drum pattern in every section; no pre-chorus gap.
- Melody that follows chord roots (sounds like a demo); toplines with no repetition.
- Too many hooks competing: one vocal hook + one instrumental riff max.

## Workflow with the tools
1. `local_ableton_snapshot`; `local_ableton_set_tempo` from the brief.
2. Tracks (`local_ableton_edit_track` `create_midi`): Drums, Bass, Keys, Pad, Lead/Topline,
   Post-chorus riff.
3. Chords first (`local_music_theory` `progression` → voice-lead → `local_ableton_create_clip`
   + `local_ableton_write_notes`), then drums, bass. `local_ableton_fire` after each so the
   user hears it.
4. Topline over the loop (chorus first, then verse/pre-chorus down from it). Check the
   bars with `local_harmony_map`.
5. Build section clips/scenes, name them; check levels with `local_ears_track_levels`.
6. Tell the user what you did and propose next (vocal, arrangement, mix).

## Hard rules
- Hook audible within the first 4–8 bars (≤10 s).
- Chorus top note higher than anything in the verse.
- Pre-chorus must change something (chords, rhythm, or density) and set up the downbeat.
- One chord per bar max in the chorus; voice-led inversions.
- Humanize every MIDI part; nothing at a flat velocity.
- Leave 1–5 kHz to the vocal/topline.

## Tell the user (short)
`Mid-tempo pop · 104 BPM · A♭ major · verse I–V–vi–IV, pre-chorus IV–V–vi–V with rising bass,
chorus back to I · hook "stay" on C5 at the chorus downbeat, a 6th above the verse · pluck riff
opens the song (hook at 0:05) · kick drops the last bar of the pre-chorus. Tracks: Drums, Bass,
Keys, Pad, Topline, Riff.`
