---
name: chatmu-studio-genre-regional-mx
description: >
  Produces Regional Mexican music in the user's Ableton Live set: corridos
  tumbados, sierreño, norteño, banda and corrido bélico. Sets the 6/8-in-3/4
  or 2-feel groove, writes the requinto lines, the tololoche / electric bass or
  tuba part, the I–IV–V harmony with secondary dominants, the lead melody and
  the segunda voz in parallel thirds, and loads the factory's Regional Mexican
  presets. Trigger phrases: "corridos tumbados", "corrido", "regional mexican",
  "sierreño", "norteño", "banda", "requinto", "tololoche", "tuba", "bélico",
  "corridos", "regional mexicano", "música de banda", "estilo Peso Pluma",
  "norteña", "sierreña", "segunda voz", "hazme un corrido".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Corridos tumbados, sierreño, norteño, banda: requinto, tololoche/tuba, I–IV–V, segunda voz in thirds"
version: "1.0"
tags: [studio, ableton, genre, regional-mexican, corridos, sierreno, norteno, banda, requinto, latin]
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

# Chatmu Studio — Regional Mexican (corridos tumbados, sierreño, norteño, banda)

Regional Mexican is played by bands of acoustic players, not programmed loops. The feel comes
from three things: the **requinto** (12-string or 6-string lead guitar) answering the singer, a
**bass voice that walks between root and fifth** (tololoche, electric bass or tuba), and a
**two-voice vocal in thirds**. Harmony is simple and diatonic; the skill is in the voicing,
the pickups and the strum. Treat every part as a player: humanize everything.

Related: `chatmu-studio-hook-melody`, `chatmu-studio-harmonize-melody` (segunda voz),
`chatmu-studio-bass-lines`, `chatmu-studio-humanize`, `chatmu-studio-arrangement`,
`chatmu-studio-genre-fusion` (corrido + trap/reggaetón), `chatmu-mix-by-genre`.

## 1. Brief (ask only what is missing; propose defaults)
| Decision | Options | Default |
|---|---|---|
| Style | corrido tumbado · sierreño (2 guitars + tololoche) · norteño (accordion + bajo sexto) · banda (brass + tuba + tambora) · bélico | corrido tumbado |
| Meter | 6/8 felt (written 3/4 or 6/8) · 2/4 polka (norteño/banda fast) · 4/4 ballad | 6/8 |
| Key | minor (tumbado, bélico) · major (norteño, banda romántica) | A minor |
| Mood | sad/romantic · street/bravado · party | street |

## 2. BPM and feel
| Style | BPM (dotted-quarter or quarter) | Feel |
|---|---|---|
| Corrido tumbado | Live tempo 130–165 with 3-beat bars (6 eighths per bar; e.g. 148) | lazy, behind the beat |
| Sierreño | 3/4 at 140–180 or 2/4 at 100–120 | bright strum, busy requinto |
| Norteño polka | 2/4, 110–130 (quarter) | "oom-pah", accordion fills |
| Banda / quebradita | 2/4, 120–150 | tuba + tambora drive |
| Romantic / ranchera vals | 3/4, 90–110 | rubato, big vocal |
In Live set the time signature in the clip lengths: a 6/8 bar = 3 beats (6 eighths). Use 3-beat
clips for 6/8, 2-beat bars for 2/4.

## 3. Groove grid
**6/8 tumbado (one bar = 6 eighths = 3 beats; positions in beats):**
- Guitar strum (armonía / 12-string): bass note on 0, chord "chuck" on 1.0 and 2.0, ghost upstrokes
  on 1.5 and 2.5 at velocity 45–60; downstrokes 85–100. Roll each chord: offset the 4–6 notes by
  0.01–0.02 beat low→high (down) or high→low (up).
- Bass: root on 0 (vel 100), fifth on 1.5 or 2.0 (vel 85); approach note on 2.5 into the next
  chord (chromatic or scale step).
- Percussion (tumbado, light): no full kit. A soft kick (36) on 0 at vel 80–90, rim (37) on
  1.0 / 2.0 at 50–65, shaker (70) on every eighth 40–70 with an accent on 0 and 1.5. Trap-hybrid
  tumbados add an 808 and hats — then follow the hemiola below, not a 4/4 trap pattern.
- **Hemiola**: every 2 bars of 6/8 can be felt as 3 bars of 2/4 (accents on 0, 1, 2 instead of
  0, 1.5). Use it at phrase ends and in requinto runs.

**2/4 norteño / banda (one bar = 2 beats):** bass/tuba on 0 and 1 (root, fifth), chord
off-beats on 0.5 and 1.5 (accordion/guitar chuck or tarola), tambora/bass drum on 0 and 1 at
vel 100–115, cymbal choke on the last off-beat of 4- or 8-bar phrases.

## 4. Harmony
- Core: I – IV – V7 (major) or i – iv – V7 (minor, V is **major** with the leading tone:
  Am – Dm – E7). Use `local_music_theory` `action: progression` with preset `corridos`, then
  adjust.
- Common moves: I – I7 – IV (secondary dominant into IV); V/V (D7 in G) before V; ♭VI – V7 in
  minor (F – E7 in Am); relative major (C) for the chorus of a minor song.
- Harmonic rhythm: 1–2 bars per chord in 6/8; chords change on the downbeat, often with a
  requinto pickup across the bar line.
- Voicing: guitar open-position shapes (root, 5th, root, 3rd, 5th, root) in MIDI 40–67. Tumbado
  guitars add 9ths and maj7/m9 colours (Am9, Fmaj7) — that is the "tumbado" modern sound.
- **Avoid**: modal vamps without a V7 (erases the genre), jazz ii–V chains, sus chords that never
  resolve, EDM supersaw pads.

## 5. Melody, hook and segunda voz
Build the hook with `chatmu-studio-hook-melody`. Genre specifics:
- Narrative verses (corrido = a story): syllabic, one note per syllable, eighth notes, range
  ≤ a 6th; the hook/chorus opens to an octave and lands on a held note on 3 or 5.
- Phrases start with an **anacrusis** (pickup) of 1–3 eighths before the downbeat.
- Lead voice range: male tenor MIDI 52–69 (E2–A3 in Live naming). Hold the last note of the
  chorus 1–2 bars ("grito" moment in banda/ranchera).
- **Segunda voz**: a diatonic 3rd **above** the lead (sometimes below), moving in parallel,
  switching to a 6th below when the 3rd would leave the chord. Same rhythm, same syllables,
  velocity 10 lower. Use `chatmu-studio-harmonize-melody` for the exact notes; never a 4th/5th.
- **Requinto**: answers each vocal phrase in the gap (call-and-response), never under the
  sung words. Runs in 16th triplets or 16ths, in thirds/sixths (double stops) from the scale,
  MIDI 59–86. Ornaments: hammer-on (grace note 0.06 beat before, vel −20), slides written as a
  2-note chromatic approach. Intro: a 4–8 bar requinto solo stating the hook.
- Accordion (norteño) fills the same gaps with thirds; trumpets/clarinets (banda) play the
  hook in unison or thirds.

## 6. Bass
- **Tololoche** (upright, sierreño/tumbado): root–fifth with chromatic walk-ups; short notes
  (0.4–0.8 beat), MIDI 28–48. Slap feel: velocity 95–110 on downbeats.
- **Electric bass** (modern tumbado): same lines, a touch more sustain; occasional 808 layered
  an octave below in trap hybrids (tune it to the same notes, never a separate line).
- **Tuba** (banda): root on 0, fifth on 1 (2/4), walking scale runs of 8ths into each chord
  change, MIDI 28–55. Tuba is the loudest low element; no other sub.

## 7. Sounds
**Chatmu Sound first (house rule).** Every bass and melodic part (bass/808, keys, pads, plucks,
leads, brass, strings…) gets **Chatmu Sound with a factory preset of this genre**, not Live's
stock instruments (Operator, Grand Piano, Electric…), which sound like generic MIDI:
1. `local_sound_find_preset` with `genre: "Regional Mexican"`, the `instrument` and a `character`. If it
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

- `local_sound_find_preset` with `genre: "Regional Mexican"` (or query `corridos`), then the
  instrument: `Guitar` (requinto/armonía), `Bass` (tololoche), `Accordion`, `Brass`
  (trumpet/tuba), `Vocal`. Characters: `Warm` for armonía and tololoche, `Bright` for requinto,
  `Short` for plucked bass. Load with `local_sound_set_preset`.
- Browser fallbacks (`local_ableton_browser`): search `nylon`, `acoustic guitar`, `12 string`,
  `upright bass`, `accordion`, `tuba`, `trumpet`, `clarinet`, `bass drum`. Real recorded guitar
  always beats a synth for the requinto: suggest the user record it (`chatmu-studio-record`).

## 8. Arrangement (bars of 6/8 unless noted)
| Section | Bars | What plays |
|---|---|---|
| Intro | 4–8 | requinto solo states the hook (+ armonía strum) |
| Verse 1 | 16 | vocal + armonía + bass; requinto fills only in gaps |
| Chorus | 8 | segunda voz enters, fuller strum, percussion up |
| Requinto interlude | 4–8 | solo over the verse chords |
| Verse 2 → Chorus | 16 + 8 | as above, add accordion/brass answers |
| Outro | 4 | requinto tag, final chord with tremolo/roll on the last downbeat |
Classic corridos repeat verse melody with new lyrics (strophic); keep the melody, vary the
fills. Name scenes with `local_ableton_scene_name`.

## 9. Mix targets
- Vocal on top and dry-ish (short plate, 0.8–1.2 s, 20–40 ms pre-delay), segunda voz 3–5 dB
  under and slightly wider (±15).
- Requinto: centre-left ±20, bright (presence 3–5 kHz), level just under the vocal; armonía
  opposite side ±25, cut below 100 Hz.
- Low end: tololoche/bass or tuba owns 50–120 Hz; kick sits under it, lighter. In trap hybrids
  808 owns < 60 Hz and the bass is high-passed to 70 Hz.
- No big reverbs on percussion; room 0.4–0.6 s.
- Loudness: −9 to −11 LUFS integrated for tumbado streaming; banda −8 to −10. Check per-track
  balance and masking with `local_ears_track_levels`.

## 10. What ruins it
- 4/4 quantized straight eighths instead of 6/8 lilt.
- Requinto playing over the lyrics.
- Segunda voz in 4ths/5ths or with different rhythm.
- Minor songs with a minor v (must be V7).
- Programmed guitar with every note at the same time and velocity (roll it, vary 60–110).
- Over-produced pads and sidechain pumping.

## Workflow with the tools
1. `local_ableton_snapshot`; `local_ableton_set_tempo` from the brief.
2. Tracks (`local_ableton_edit_track` `create_midi`): Armonia, Bass (Tololoche/Tuba), Requinto,
   Perc, Vocal Guide, Segunda Voz.
3. `local_music_theory` `progression` preset `corridos` in the key → armonía strum clip
   (`local_ableton_create_clip`, `local_ableton_write_notes`) → fire (`local_ableton_fire`).
4. Bass line → fire. Light percussion → fire.
5. Melody guide + segunda voz; requinto fills in the gaps; intro solo. Check chords against the
   melody with `local_harmony_map`.
6. Balance check with `local_ears_track_levels`; then suggest arrangement and mix next.

## Hard rules
- Say style, meter (6/8, 2/4 or 3/4), BPM and key.
- Minor keys use a major V7.
- Segunda voz moves in parallel 3rds (6ths when needed), same rhythm.
- Requinto and accordion fill only the gaps between sung phrases.
- Humanize every part: strum rolls, velocity 45–110, timing ±10 ms (`chatmu-studio-humanize`).
- Bass/tuba is the only low-mid owner; no pad below 200 Hz.

## Tell the user (short)
`Corrido tumbado · 6/8 at 148 (3-beat bars) · A minor · Am9 – Dm9 – E7 – Am, F – E7 in the
chorus · tololoche root–fifth with chromatic walk-ups · requinto intro states the hook and
answers each line · segunda voz a 3rd above in the chorus. Tracks: Armonia, Tololoche,
Requinto, Perc, Vocal Guide, Segunda Voz.`
