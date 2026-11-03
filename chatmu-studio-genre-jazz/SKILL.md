---
name: chatmu-studio-genre-jazz
description: >
  Produces jazz in the user's Ableton Live set: swing standards, ballads,
  bossa nova, jazz waltz, modal and neo-soul/lo-fi jazz. Writes ii–V–I and
  turnaround harmony with guide tones, shell and rootless (A/B) voicings,
  comping rhythms, a walking bass line by chord tones and approach notes, the
  swing ride pattern with hi-hat on 2 and 4, and heads with bebop
  vocabulary. Trigger phrases: "jazz", "swing", "ii-V-I", "two five one",
  "walking bass", "rootless voicings", "comping", "jazz standard", "bebop",
  "bossa nova", "jazz waltz", "modal jazz", "neo soul jazz", "jazz chords",
  "acordes de jazz", "bajo caminante", "dos cinco uno", "hazme un jazz",
  "estilo jazz", "swing de jazz".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Jazz: ii–V–I, guide tones, rootless voicings, comping, walking bass, swing ride on 2 and 4"
version: "1.0"
tags: [studio, ableton, genre, jazz, swing, ii-v-i, voicings, walking-bass, bossa, harmony]
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

# Chatmu Studio — Jazz

Jazz is a conversation between players over a chord form. A convincing programmed jazz track
needs: **voice-led chords** (guide tones moving by step, not root-position blocks), a
**walking bass** that outlines the changes and connects them, a **ride cymbal** that swings,
and a melody with real phrasing. Everything is swung and dynamically alive; nothing is on a
grid at one velocity.

Related: `chatmu-studio-harmony` (functional harmony), `chatmu-studio-harmonize-melody`,
`chatmu-studio-melody-over-chords`, `chatmu-studio-bass-lines`, `chatmu-studio-humanize`,
`chatmu-studio-afro-cuban-rhythms` (Latin jazz), `chatmu-mix-by-genre`.

## 1. Brief
| Decision | Options | Default |
|---|---|---|
| Style | medium swing · up-tempo bebop · ballad · bossa nova · jazz waltz · modal · neo-soul/lo-fi jazz | medium swing |
| Form | 32-bar AABA · 12-bar blues · 16-bar · ii–V vamp | 32-bar AABA |
| Group | piano trio · quartet (+ sax/trumpet) · guitar trio · organ trio | piano trio |
| Key | F, B♭, E♭, C, G (horn-friendly) | F |

## 2. BPM and feel
| Style | BPM | Feel |
|---|---|---|
| Ballad | 50–75 | straight or soft swing 8ths, brushes |
| Medium swing | 110–160 | swing 8ths ≈ 62–66% (triplet feel) |
| Up-tempo bebop | 200–300 | swing flattens toward 55–58% |
| Bossa nova | 120–145 | straight 8ths |
| Jazz waltz | 140–180 (3/4) | swing 8ths |
| Neo-soul jazz | 75–95 | heavy 16th swing, laid back |
Swing in MIDI: off-beat 8ths (x.5) move to x.66 at medium tempo (0.62–0.66 beat), x.58 when
fast. Use `local_music_theory` `action: humanize` or write the positions directly.

## 3. Harmony: ii–V–I and guide tones
- Major ii–V–I: Dm7 – G7 – Cmaj7. Minor: Dm7♭5 – G7♭9 – Cm6 (or Cm(maj7)).
- **Guide tones** = 3rds and 7ths. In ii–V–I the 7th of each chord falls a half/whole step to
  the 3rd of the next: Dm7 (F, C) → G7 (F, B) → Cmaj7 (E, B). Build every voicing around this
  line.
- Common forms: I – vi – ii – V turnaround (Cmaj7 – A7 – Dm7 – G7, with secondary dominant VI7);
  iii – VI – ii – V; tritone substitution (D♭7 for G7 → chromatic bass D – D♭ – C); backdoor
  ii–V (Fm7 – B♭7 – Cmaj7); rhythm changes; 12-bar jazz blues (F7 B♭7 F7 Cm7 F7 | B♭7 B♭°7 F7
  D7 | Gm7 C7 F7 D7 | Gm7 C7).
- `local_music_theory` `progression` preset `jazz` as a seed; then write real changes with
  `action: chords` and explicit symbols (`Dm9`, `G13`, `Cmaj9`, `G7alt`).
- Extensions: on maj7 add 9 (and #11 on Lydian); on m7 add 9/11; on dominant 9/13 (natural) or
  ♭9/#9/♭13 (altered) when resolving to minor or for tension. Never the natural 11 on a
  major or dominant chord (clashes with the 3rd) — use #11.
- **Avoid**: root-position triads; parallel block chords with the root on top; ignoring the
  V's resolution.

## 4. Voicings (MIDI; keep the left hand above ~MIDI 48)
- **Shell** (bebop, guitar, left hand): root + 3 + 7 or root + 7 + 3. Root MIDI 36–47, 3/7 in
  48–60.
- **Rootless A/B voicings** (piano trio — bass has the root):
  - A form: 3 – 5 – 7 – 9 (Dm9: F A C E). B form: 7 – 9 – 3 – 5 (Dm9: C E F A).
  - Dominant: A = 7 – 9 – 3 – 13 (G13: F A B E); B = 3 – 13 – 7 – 9 (B E F A).
  - Alternate A and B through a ii–V–I so voices move by step: Dm9 (A: F A C E) → G13 (B: F A
    B E) → Cmaj9 (A: E G B D). Lowest note between MIDI 50 and 60.
- **So What / quartal** (modal): stacked 4ths + a major 3rd on top (E A D G B over Dm).
- **Drop 2** (guitar/ensemble): close 4-note voicing with the 2nd voice from the top dropped an
  octave.
- Horn section: 4-way close under the melody, or melody + guide tones.

## 5. Comping
- Charleston: hits on 0 and 1.5 (swung "&" of 2); reverse Charleston 0.5(swung) and 2.0.
- Anticipations: chord on the "&" of 4 (3.66 swung) belonging to the next bar.
- Leave space: 2–4 hits per bar, durations 0.3–1 beat; react to melody gaps; tacet under
  busy melody. Vel 55–85, top note slightly louder.
- Bossa comping (guitar/piano), 2-bar pattern, straight 8ths: bar 1 = 0, 1.5, 3.0 · bar 2 =
  0.5, 2.0, 3.5. Bass on 0 and 2 (root, fifth) with pickups on 1.5 and 3.5.

## 6. Walking bass
- Quarter notes on every beat, MIDI 28–55 (upright), vel 85–100, accents slightly on 2 and 4.
- Per chord (2 beats): beat 1 = root, beat 2 = chord tone or **approach** to the next root.
  Per chord (4 beats): root – 3 – 5 – approach (or root – scale step – step – approach).
- Approach note on the last beat before a change: a half step above or below the next root,
  or the next chord's 5th (dominant approach).
- Ghost/skip notes: occasional swung 8th triplet pickup (vel 50–60) on the "&" of 4.
- Example Dm7 – G7 (2 beats each) → Cmaj7: D, A♭ (half step above G) | G, D♭ (half step above
  C) | C … every approach resolves by half step into the next root.
- Ballads: half notes (2-feel) in A sections, walk in the bridge. Bossa: root–fifth.

## 7. Drums (Drum Rack: ride = 51, closed hat 42 / pedal hat 44, snare 38, kick 36)
- **Swing ride**: "ding, ding-a-ding": quarters on 0, 1, 2, 3 + skip notes on 1.66 and 3.66
  (swung). Accent 2 and 4 (vel 95), 1 and 3 at 80, skips 60–70.
- **Hi-hat foot** (44) on 1.0 and 3.0 (beats 2 and 4), vel 70–85.
- Kick "feathered" on all four quarters at vel 30–45 (felt, not heard); occasional bombs
  (vel 90) on off-beats.
- Snare comping: ghost notes 30–55 on swung 8ths, accents with the horns; fills last 2 beats of
  8-bar sections.
- Ballad: brushes (snare sweeps as long notes, vel 40–60, ride or snare taps on 2 and 4).
- Bossa: cross-stick (37) on the 2-bar pattern bar 1 = 0, 0.75, 1.5, 2.5, 3.25 · bar 2 = 0.5,
  1.5, 2.25, 3.0; closed hat steady 8ths; kick 0, 1.5, 2, 3.5.
- No `local_music_theory` `drum_pattern` genre for jazz: write it yourself.

## 8. Melody and heads
Use `chatmu-studio-melody-over-chords` and `chatmu-studio-hook-melody`. Jazz specifics:
- Target guide tones (3rds/7ths) on strong beats; chromatic **enclosures** (above + below the
  target, then the target); bebop scale (add the chromatic passing note between 5 and 6 in
  major, ♭7–7 on dominants) so chord tones land on beats.
- Phrases of 2–4 bars, start off the downbeat, end on an upbeat with an accent; leave bars of
  space.
- Horn/lead register: tenor sax MIDI 44–75 (sounding), trumpet 54–82, alto 49–80; piano RH
  60–84.
- Swing 8ths in lines; vel ghosting on low-function notes (−15).

## 9. Sounds
**Chatmu Synth first (house rule).** Every bass and melodic part (bass/808, keys, pads, plucks,
leads, brass, strings…) gets **Chatmu Synth with a factory preset of this genre**, not Live's
stock instruments (Operator, Grand Piano, Electric…), which sound like generic MIDI:
1. `local_synth_find_preset` with `genre: "Jazz"`, the `instrument` and a `character`. If it
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

- `local_synth_find_preset` with `genre: "Jazz"` if listed (else `fallback: true`): `Keys Warm`
  (Rhodes/piano), `Bass Warm` (upright), `Brass` (trumpet/sax), `Guitar Warm` (archtop).
- Browser (`local_ableton_browser`): `grand piano`, `upright bass`, `jazz kit`, `brushes`,
  `ride`, `rhodes`, `organ`, `tenor sax`, `trumpet`, `vibraphone`. Load with
  `local_ableton_load_device`. Real upright/brushes samples matter more than any effect.

## 10. Arrangement (32-bar AABA, chorus = 32 bars)
| Section | Choruses | What plays |
|---|---|---|
| Intro | 4–8 bars | piano alone or last 4 bars of the form / turnaround vamp |
| Head | 1 | melody (A A B A), trio comps lightly |
| Solos | 1–3 | piano/horn solo; bass walks; drums more active; 2nd solo chorus builds |
| Trading 4s (optional) | 1 | soloist 4 bars, drums 4 bars |
| Head out | 1 | melody; tag the last 4 bars ×3 |
| Ending | 2–4 bars | ritardando, final chord with 6/9 or maj9#11 |
Name scenes with `local_ableton_scene_name` (`Head`, `Solo 1`, `Head Out`).

## 11. Mix targets
- Natural and dynamic: a room/hall send 1.5–2.2 s, light compression (2–3 dB GR max).
- Panning (audience view): drums spread overheads, ride right +30, bass centre, piano wide
  stereo slightly left, horn centre or +15.
- Bass owns 50–200 Hz with string definition 700 Hz–1.5 kHz; kick is not a low-end owner.
- Loudness: −14 to −18 LUFS integrated (keep the dynamics); lo-fi/neo-soul jazz −10 to −12.
  Check balance with `local_ears_track_levels`.

## 12. What ruins it
- Straight 8ths in swing; quantized ride with no accents on 2 and 4.
- Root-position block chords; left hand voicings below MIDI 48 (mud).
- Bass playing roots only on beat 1 and holding.
- Constant comping that leaves no space.
- Melody that ignores chord tones on strong beats.

## Workflow with the tools
1. `local_ableton_snapshot`; `local_ableton_set_tempo`.
2. Tracks (`local_ableton_edit_track` `create_midi`): Drums, Bass, Piano (comp), Lead/Head.
3. Changes: `local_music_theory` `chords` with explicit symbols; verify with `local_harmony_map`.
4. Drums (ride + hat) → fire (`local_ableton_fire`); walking bass → fire; rootless comping
   (`local_ableton_create_clip`, `local_ableton_write_notes`) → fire.
5. Head melody last; humanize all (`chatmu-studio-humanize`), swing applied.
6. Balance with `local_ears_track_levels`.

## Hard rules
- State style, BPM, swing %, form and key.
- Voice-lead guide tones; rootless voicings when a bass is present.
- Walking bass in quarters with approach notes into every chord change.
- Ride accents on 2 and 4 with hi-hat foot on 2 and 4.
- Never quantize to straight 8ths in swing; velocities always vary.

## Tell the user (short)
`Medium swing · 140 BPM · 64% swing · F major · 32-bar AABA with ii–V–I and I–VI–ii–V
turnarounds · rootless A/B voicings · walking bass with chromatic approaches · ride
ding-ding-a-ding, hat on 2 and 4 · head then a piano solo chorus. Tracks: Drums, Bass, Piano,
Head.`
