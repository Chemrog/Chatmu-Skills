---
name: chatmu-studio-genre-latin-tropical
description: >
  Produces Latin tropical music in the user's Ableton Live set: salsa, son,
  cumbia (colombiana, sonidera, villera, digital), bachata and merengue. Builds
  each groove on the right timeline (son clave 2-3 / 3-2, cumbia güiro and
  off-beat, bachata bongo and güira, merengue tambora), writes the montuno or
  guitar pattern, the tumbao or anticipated bass, the coro-pregón form and the
  horn mambos. Trigger phrases: "salsa", "cumbia", "bachata", "merengue",
  "tropical", "son cubano", "montuno", "tumbao", "clave", "güira", "güiro",
  "salsa romántica", "cumbia sonidera", "cumbia villera", "música tropical",
  "hazme una salsa", "ritmo de cumbia", "bachata romántica", "merengue típico".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Salsa, cumbia, bachata, merengue on the right timeline: clave, montuno, tumbao, güira, tambora"
version: "1.0"
tags: [studio, ableton, genre, latin, tropical, salsa, cumbia, bachata, merengue, clave]
requiresTools:
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

# Chatmu Studio — Latin tropical (salsa, cumbia, bachata, merengue)

Four genres, four different engines. Salsa is governed by the **clave**; cumbia by the
**güiro/guacharaca + off-beat**; bachata by the **bongo, güira and arpeggiated requinto**;
merengue by the **tambora and güira in a fast 2**. Pick one engine and keep it; mixing them
produces "generic Latin". Clave math and the full Afro-Cuban vocabulary (cascara, mambo bell,
songo, rumba clave) live in `chatmu-studio-afro-cuban-rhythms` — this skill uses it.

Related: `chatmu-studio-afro-cuban-rhythms`, `chatmu-studio-hook-melody`,
`chatmu-studio-bass-lines`, `chatmu-studio-humanize`, `chatmu-studio-counter-melody` (horn
lines), `chatmu-studio-genre-reggaeton`, `chatmu-mix-by-genre`.

## 1. Brief
| Decision | Options | Default |
|---|---|---|
| Genre | salsa (dura/romántica) · son · cumbia (colombiana/sonidera/villera/digital) · bachata · merengue | salsa |
| Key/mode | minor (salsa dura, cumbia) · major (romántica, merengue) | A minor |
| Lead | vocal + coro · horns · accordion (cumbia/merengue típico) · requinto (bachata) | vocal + coro |

## 2. BPM and timeline per genre (positions in beats of a 4/4 bar, 0 = downbeat)
| Genre | BPM | Timeline |
|---|---|---|
| Salsa | 160–210 (romántica 160–180, dura 180–210) | son clave 2-3: bar A = 1.0, 2.0; bar B = 0, 1.5, 3.0 |
| Son | 90–120 | son clave 3-2: bar A = 0, 1.5, 3.0; bar B = 1.0, 2.0 |
| Cumbia | 85–105 (sonidera 80–95; digital 95–110) | güiro: long-short-short (0 long, 0.5, 0.75) every beat |
| Bachata | 120–140 (moderna 125–135) | bongo martillo 8ths; güira 8ths, accent beat 3 |
| Merengue | 130–170 (típico up to 180) | tambora + güira, 2-feel |
State the clave direction for salsa/son. The direction follows the melody: if the vocal phrase
starts on beat 2 with weight, it is 2-3.

## 3. Groove grids
**Salsa (2 bars, son clave 2-3):**
- Clave (75, claves sound or rim 37) on its own track, vel 90.
- Cascara on timbale shell / closed hat (42) in verses, 2-3: bar A (2-side) 0, 1.0, 2.0, 2.5,
  3.5 · bar B (3-side) 0, 1.0, 1.5, 2.5, 3.5. Vel 70–95, accents where it coincides with the clave.
- Mambo bell (cowbell, 56) in coros: quarters on 0, 1, 2, 3 with extra 8ths at 1.5 and 3.5; vel
  90–110 on quarters.
- Congas tumbao: open tones (high conga) on 3.0 and 3.5 (vel 100), slap on 1.0 (vel 95), heel/tip
  on the other 8ths at 40–55.
- Bongó martillo in verses: 8ths, accent beat 1 and 3 with the open tone on 3.5.
- Güiro: quarter long + 8th short (0, 0.5) per beat, vel 60–80.

**Cumbia (1 bar):**
- Güiro/guacharaca (or shaker 70): long on each beat, two shorts on 0.5 and 0.75. Vel 85 / 60 / 55.
- Bass drum (tambora/kick 36) on 0 and 2 (vel 100); "llamador" on the off-beats 0.5, 1.5, 2.5, 3.5
  (rim/conga, vel 75–90). Snare/timbal accent on 3.5 for sonidera.
- Guitar/accordion/keys "chuck" on the off-beats.
- Cumbia digital/villera: add a drum-machine kick on 0, 1, 2, 3 and keep the güiro on top.

**Bachata (1 bar):**
- Bongo: martillo 8ths, open tone on 3.5 (and 1.5 in derecho), vel 60–100; in the mambo section
  switch to tambora drum on 0, 1.75, 2, 3.
- Güira: 8ths at vel 55–75 with accents on 0 and 2; scrape (two 16ths) into beat 3.
- Bass on 0 (root), 1.5 (anticipation), 2.0, 3.5 (pickup into next bar). Beat 3.0 is often silent.

**Merengue (1 bar, in 2):**
- Tambora: slap on 0 and 2 (vel 110), "rim" roll on 1.5–1.75 (two 16ths, vel 70) and 3.5.
- Güira: steady 8ths with a 16th pair on each beat ("ch-chk-ch"), vel 55–85.
- Bass: root on 0, fifth on 2, anticipated 8th on 3.5.

## 4. Harmony
- Salsa/son: i – iv – V7 – i, ii–V–i (Bm7♭5 – E7 – Am), I – IV – V7 cycles; montuno section often
  a 2-chord vamp (i – V7 or I – IV – V – IV). Use `local_music_theory` `action: progression` or
  `chords` with explicit symbols; preset `andalusian` (i – ♭VII – ♭VI – V) works for salsa and
  flamenco-tinged bachata.
- Cumbia: I – V7 (or i – V7) two-chord, I – IV – V7. Andean/peruvian cumbia uses minor with ♭VII.
- Bachata: i – iv – V7 or I – vi – IV – V; romantic minor 4-chord cycles; mostly diatonic triads.
- Merengue: I – V7 vamps, I – IV – V7.
- Harmonic rhythm: 1 or 2 bars per chord; changes anticipate the bar (on 3.5 of the previous bar).
- **Avoid**: house pads and long sustained chords; extended jazz voicings in cumbia/merengue;
  dropping the V7 to a minor v.

## 5. Melody, hook and coro
Build with `chatmu-studio-hook-melody`. Genre specifics:
- **Coro–pregón** (salsa/son): in the montuno the coro repeats a 2- or 4-bar hook; the lead
  improvises a "pregón" answer between. The coro is the song's hook — write it in 2–3 part
  harmony (3rds and 6ths), syllabic, landing with the clave.
- Salsa horn **mambo**: 2–4 trumpets/trombones in close voicing, 4- or 8-bar riff, rhythmically
  locked to the 3-side; contrasting moña (layered riffs) at the climax. Trumpets MIDI 64–84,
  trombones 52–72.
- Piano **montuno** (guajeo): 2-bar pattern in 8ths, octave-doubled hands (right hand chord
  tones in octaves, MIDI 60–84), syncopated and aligned with the clave; anticipations on the
  "&" of 4.
- Cumbia lead: accordion or synth (sonidera) playing scalar 8ths/16ths answers with thirds;
  vocal phrases short, chant-like.
- Bachata requinto: arpeggios in 8ths and 16ths on chord tones, MIDI 64–88, answering the
  voice; the segunda guitar strums/arpeggiates mid register.
- Merengue: sax section riffs in fast 16ths (jaleo section), accordion in típico.

## 6. Bass
- **Tumbao** (salsa/son): bar = note on 1.5 (the "&" of 2) and 3.0 (beat 4) — downbeat silent;
  the 4 note anticipates the next chord's root. MIDI 28–50, vel 90–105, notes 0.5–1 beat.
- Cumbia: root on 0, fifth on 2 (or root–fifth–octave in 8th walking), very regular.
- Bachata: electric bass, syncopated per §3 with slides as chromatic grace notes.
- Merengue: root/fifth in 2 with 8th pickups.

## 7. Sounds
- `local_synth_find_preset` queries: `"Brass Bright"` (horns), `"Keys"` (montuno piano),
  `"Guitar"` (bachata requinto), `"Accordion"` (cumbia/merengue), `"Bass Warm"`. The factory has
  no salsa/cumbia genre: expect `fallback: true` and say so; try `genre: "Reggaeton"` for
  modern cumbia digital basses.
- Percussion from the browser (`local_ableton_browser`): `conga`, `bongo`, `timbale`, `cowbell`,
  `guiro`, `guira`, `claves`, `tambora`, `latin percussion`. Load with `local_ableton_load_device`.
  If no Latin kit exists, map conga to toms and say a real kit would sound better.

## 8. Arrangement (bars)
| Genre | Form |
|---|---|
| Salsa | Intro 8 (horns/piano) · Verse (cuerpo) 16–32 · Montuno coro–pregón 16–32 · Mambo 8–16 · Montuno 16 · Coda 4 |
| Cumbia | Intro 8 (lead riff) · Verse 16 · Chorus 8 · Instrumental 8 · Verse/Chorus · Outro 8 |
| Bachata | Intro 8 (requinto) · Verse 16 · Chorus 8 · **Mambo** 8 (tambora, güira louder) · Verse/Chorus · Outro |
| Merengue | Intro 8 · Merengue (verse) 16 · Jaleo 16–32 (call-response, sax riffs) · Outro |
Name scenes with `local_ableton_scene_name`.

## 9. Mix targets
- Percussion carries the energy: congas ±30 L/R, bongó/güira off-centre, timbales/cowbell
  slight right; clave low in the mix (felt more than heard).
- Bass owns 60–150 Hz; there is usually no sub/808 — keep kick light in salsa/bachata.
- Horns bright and forward (2–5 kHz), short room/plate reverb 0.8–1.2 s; piano montuno mid-left.
- Vocal and coro on top; coro 3–4 dB under the lead, wider.
- Loudness: −10 to −12 LUFS for salsa/bachata (dynamics matter), −8 to −10 for cumbia digital
  and merengue. Check with `local_ears_track_levels`.

## 10. What ruins it
- Clave missing, doubled or flipped mid-section (see `chatmu-studio-afro-cuban-rhythms`).
- Bass on the downbeat in salsa (kills the tumbao).
- Four-on-the-floor house kick under salsa.
- Quantized, flat-velocity percussion; congas without open-tone accents.
- Pads and long reverbs filling the space the percussion needs.

## Workflow with the tools
1. `local_ableton_snapshot`; `local_ableton_set_tempo`.
2. Tracks (`local_ableton_edit_track` `create_midi`): Clave/Timeline, Perc, Bass, Piano/Guitar,
   Horns or Accordion, Vocal Guide, Coro.
3. Timeline first (clave, güiro or güira) → fire (`local_ableton_fire`).
4. Percussion → bass → montuno/guitar, firing after each (`local_ableton_create_clip`,
   `local_ableton_write_notes`).
5. Hook/coro and horns; verify chords with `local_harmony_map`.
6. Balance with `local_ears_track_levels`; humanize (`chatmu-studio-humanize`).

## Hard rules
- Name the genre, BPM, key and (salsa/son) clave direction.
- Write the timeline first, on its own track.
- Salsa bass is tumbao (1.5 and 3.0), never the downbeat.
- One genre engine per section; don't layer cumbia güiro over salsa clave.
- Horns and coro align with the clave; anticipate chord changes on 3.5.

## Tell the user (short)
`Salsa · 190 BPM · A minor · son clave 2-3 · cuerpo: Am – Dm – E7 – Am, montuno vamp Dm – E7 ·
tumbao bass on 2& and 4 · piano guajeo in octaves · cascara verse, mambo bell + coro in the
montuno, 8-bar trumpet mambo. Tracks: Clave, Perc, Bass, Piano, Horns, Vocal Guide, Coro.`
