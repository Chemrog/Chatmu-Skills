---
name: chatmu-studio-genre-hiphop
description: >
  Produces hip hop in the user's Ableton Live set — boom bap, lo-fi hip hop
  and modern (non-trap) hip hop: backbeat drums at 70–98 BPM with Dilla-style
  swing and ghost notes, a sample-style or keys loop with 7th/9th chords, a
  round bass that locks with the kick, vinyl texture and space for the rapper.
  Trigger phrases: "boom bap", "hip hop beat", "lo-fi", "lofi hip hop",
  "chill beat", "study beat", "Dilla swing", "old school hip hop", "jazzy
  beat", "hazme un boom bap", "beat de hip hop", "beat lo-fi", "beat chill",
  "hip hop clásico", "beat noventero", "beat jazzy", "swing tipo Dilla".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Boom bap, lo-fi and modern hip hop: backbeat with Dilla swing, ghost notes, 7th-chord loop, round bass"
version: "1.0"
tags: [studio, ableton, genre, hip-hop, boom-bap, lofi, lo-fi, dilla, breakbeat, jazz]
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

# Chatmu Studio — Hip hop (boom bap, lo-fi, modern)

This skill covers the **backbeat** family of hip hop: snare on 2 & 4, a loop that feels sampled,
swing that lives between straight and triplet, and a bass that sits under the kick. (Half-time
trap/drill at 130–150 is `chatmu-studio-genre-dark-trap`.) It sounds AI-made when the drums are
quantized to the grid at fixed velocities, the chords are plain triads, the loop has no
imperfection, or the beat is too busy for a rapper.

Related: `chatmu-studio-breakbeats` (ghost notes, break anatomy), `chatmu-studio-humanize`,
`chatmu-studio-sampling`, `chatmu-studio-hook-melody`, `chatmu-studio-harmony`,
`chatmu-studio-bass-lines`, `chatmu-studio-drum-rack`, `chatmu-mix-by-genre`.

## 1. Brief (ask only what is missing; propose defaults)
| Decision | Options | Default |
|---|---|---|
| Style | boom bap (90s NY, hard drums) · lo-fi (soft, dusty, instrumental/study) · modern hip hop (cleaner, 85–98, R&B-adjacent) · jazz rap | boom bap |
| Tempo | boom bap 85–95 · lo-fi 70–90 · modern 85–98 | 90 boom bap, 82 lo-fi |
| Key/colour | minor/dorian (dark, soulful) · major 7ths (warm lo-fi) | D minor / F major |
| Loop voice | keys (Rhodes/EP) · piano · guitar · strings/horn stabs · vocal chop | Rhodes |
| Purpose | for a rapper (needs space) · instrumental (melody can lead) | for a rapper |

## 2. Tempo & feel
- **Backbeat**: snare on beats 2 & 4 (steps 5, 13). NOT half-time.
- **Swing**: 16th swing 54–62 % (Live groove "Swing 16ths" 55–60 or MPC 16 Swing 58). Lo-fi
  55–62 %, boom bap 54–60 %, modern 50–55 %.
- **Dilla feel** (unquantized, "drunk"): leave the kick slightly early and loose (-5 to -15 ms,
  some hits ±20 ms), the snare a touch late (+10 to +25 ms), hats swung hard (~60–66 %) while the
  kick stays near-straight. Different elements on different swing amounts is the point. Apply via
  `local_music_theory` `action: humanize` per track, not to the whole kit at once.

## 3. Groove grid (1 bar; beats from bar start; steps 1–16)
Drum Rack: 36 kick, 38 snare, 37 rim, 39 clap, 42 closed hat, 46 open hat, 70 shaker.
`local_music_theory` `action: drum_pattern` with `genre: boombap` or `lofi` gives a skeleton.

**Boom bap (85–95)**
| Element | Positions | Steps | Velocity |
|---|---|---|---|
| Kick (36) | 0, 1.75, 2.5 | 1 8 11 | 100–120 |
| Snare (38) | 1, 3 | 5 13 | 110–125 (layer rim 37 at 70 for crack) |
| Ghost snares (38) | 0.75, 2.25, 3.75 (pick 1–3) | 4 10 16 | 20–40 |
| Hat (42) | 8ths or 16ths | — | on-beats 80–95, off-beats 50–70; 16th variant 40–90 |
| Open hat (46) | 3.5 every 2 bars | 15 | 70 |
- Bar 2 variant: kick at 0, 0.5, 2.5, 2.75 (steps 1, 3, 11, 12) — a double kick into beat 3.

**Lo-fi (70–90)**
| Element | Positions | Steps | Velocity |
|---|---|---|---|
| Kick (36) | 0, 2.5 (+1.75 variation) | 1 11 (8) | 80–100, soft attack |
| Snare/rim (38/37) | 1, 3 | 5 13 | 75–95 dusty; rim often instead of snare |
| Hat (42) | 8ths swung 55–62 % | odd steps | 55–85 |
| Shaker (70) | 16ths optional | all | 30–50 |

**Modern hip hop (85–98)**: boom-bap skeleton with tighter quantize (swing ≤ 55 %), clap layered on
the snare, 16th hats with occasional 32nd pairs, an 808-ish sub instead of a bass guitar.

Break anatomy for richer drums (`chatmu-studio-breakbeats`): add, in order, a doubled kick, ghost
snares (velocity 20–40), a 16th hat with accented on-beats, an open hat before the snare. Stop when
it starts to crowd the vocal. Drop the kick for the first beat of every 8th bar.

## 4. Harmony
- **Lo-fi / jazzy**: ii7 – V7 – Imaj7 (Gm7 – C7 – Fmaj7), Imaj7 – vi7 – ii7 – V7, or minor
  i9 – iv9 (Dm9 – Gm9) two-chord vamps. One chord per bar; `local_music_theory` `action: progression`
  `preset: lofi` or `jazz`.
- **Boom bap**: a 1–2-bar minor loop — i7 – ♭VImaj7 (Dm7 – B♭maj7), i – iv7, or a dorian
  i7 – IV7 (Dm7 – G7) vamp. Soul samples often sit on one chord with a moving inner line.
- **Modern**: i – ♭VI – ♭VII or R&B-ish iv9 – v7 – i9.
- Voicings: rootless or shell voicings in MIDI 52–76 (3rd + 7th + 9th), roll the chord (each note
  10–25 ms later, top note softer), play slightly behind the beat (+10–20 ms). Use
  `chatmu-studio-harmony` for extensions.
- **Avoid**: plain root-position triads (sounds like a MIDI demo), bright major I–V–vi–IV, chords on
  every 8th note, harmony moving under every rap bar.

## 5. Hook / melody specifics
Build the motif with `chatmu-studio-hook-melody`; in this family:
- The "hook" is usually the **loop itself**: a 2- or 4-bar phrase that a listener can hum, with one
  memorable top note or a falling inner line (e.g. 9 → 8 → ♭7 across bars).
- Sample feel: a phrase that ends early and repeats exactly; a slight pitch-down character
  (tune instruments -1 to -3 semitones and low-pass at 6–9 kHz) gives the "chopped record" vibe.
- Chorus: add a counter line (horn, flute, vocal chop) for 8 bars only; verses keep the bare loop.
- Lo-fi instrumental: a sparse melody on top (EP/guitar, MIDI 64–84), pentatonic or dorian, lots
  of rests, notes late by 10–30 ms.
- For a real sample flip, use `chatmu-studio-sampling` and `chatmu-studio-vocal-chops`.

## 6. Bass
- Range MIDI 28–48; root mostly MIDI 33–43.
- **Lock with the kick**: bass notes start with the kick hits (0, 1.75, 2.5), root of the chord,
  passing notes (chromatic or 5th) on 3.5–3.75 into the next bar.
- Boom bap: short-ish upright/electric bass (duration 0.4–0.9 beat), or a sine sub following the
  kick. Lo-fi: round, low velocity (70–90), longer notes with slides. Modern: sustained sub/808
  with occasional glide (overlap 0.125 beat + glide on the device).
- Bass velocity follows the kick's: loud on beat 1, softer on syncopations.

## 7. Sounds
- `local_synth_find_preset`: `query: "keys warm"`, `"lofi keys"`, `"hiphop bass"`, `"guitar warm"`,
  `"strings warm"`, `"brass"`, `"flute"`, `"lofi bass"`. Say so when it returns `fallback: true`.
- Browser fallbacks (`local_ableton_browser`): `boom bap kit`, `lofi kit`, `vinyl`, `crackle`,
  `electric piano`, `upright bass`, `break`. Load with `local_ableton_load_device`.
- Texture: vinyl crackle/tape hiss on its own track at -24 to -30 dB; saturation and gentle wow on
  the keys for lo-fi; boom bap drums slightly crunchy (bit-depth/sample-rate reduction 12-bit-ish).

## 8. Arrangement
| Section | Bars | What plays |
|---|---|---|
| Intro | 4–8 | loop alone, filtered (low-pass ~1 kHz) or with crackle |
| Verse 1 | 16 | drums + bass + loop; small drum changes every 4 bars |
| Hook | 8 | loop + counter line + fuller drums (open hat, extra kick) |
| Verse 2 | 16 | variation: drop the loop for 2 bars, change the chop |
| Hook | 8 | full |
| Verse 3 / bridge | 8–16 | stripped (drums only or loop only) for contrast |
| Hook + outro | 8 + 4–8 | loop fades or filters down |
- Boom bap at 90 BPM: 1 bar ≈ 2.67 s, 16 bars ≈ 43 s; a 3-minute song ≈ 68 bars.
- Lo-fi instrumentals: 2–3 min, A (8) – A′ (8) – B (8) – A (8), with gentle drops of the drums.
- Name scenes with `local_ableton_scene_name`; full structure in `chatmu-studio-arrangement`.

## 9. Mix targets
- Low end: kick 50–100 Hz, bass/sub 40–120 Hz; decide which leads under 60 Hz (boom bap: kick;
  modern: sub). High-pass keys at 120–180 Hz, crackle at 300 Hz.
- Relative levels (kick = 0 dB): snare -1 to -3, bass -2 to -5, hats -12 to -16, loop -6 to -10,
  crackle -24 to -30.
- Space: short room on drums (0.4–0.8 s), plate or spring on keys; lo-fi rolls the top end off
  above 10–12 kHz. Vocal centre and present (2–5 kHz) — the loop gets a dip there if it masks.
- Loudness: boom bap/modern master **-10 to -8 LUFS**; lo-fi **-14 to -11 LUFS** (dynamics are the
  vibe); true peak ≤ -1 dBTP (`chatmu-master-chain`).
- Check `local_ears_track_levels` for kick/bass and loop/vocal masking; `local_ears_listen` for the mix.

## 10. What ruins it
- Snare on beat 3 only (that's half-time trap) or perfectly straight grid with fixed velocities.
- The same swing on every element; Dilla feel without the snare/kick offsets.
- Root-position triads, no 7ths/9ths, chords perfectly on the grid.
- Too many elements in the verse; melody over every rap bar.
- Lo-fi so muffled the kick disappears; crackle louder than the hats.

## Workflow with the tools
1. `local_ableton_snapshot`; `local_ableton_set_tempo` (90 boom bap / 82 lo-fi).
2. Tracks (`local_ableton_edit_track` `create_midi`): Drums, Bass, Keys, Texture, (Counter);
   `local_ableton_tracks` for indices.
3. Drums: `drum_pattern` `boombap` or `lofi` → ghost notes, velocities, swing via `humanize` →
   `local_ableton_create_clip` (2–4 bars) → `local_ableton_write_notes` → `local_ableton_fire`.
4. Keys loop from `progression` (`lofi`/`jazz`) with rolled, late voicings; check with
   `local_harmony_map`; fire with the drums.
5. Bass locked to the kick; texture track; counter line only for the hook.
6. Rough levels with `local_ableton_mixer`; `local_ears_track_levels`; name scenes; propose next step.

## Hard rules
- Backbeat: snare on 2 & 4 (steps 5, 13).
- Swing or humanize every element differently; never leave the drums dead-quantized.
- 7th/9th chords, rolled and slightly late; no root-position triad pads.
- Bass starts with the kick.
- Keep the verse sparse for the rapper.
- Say the style, tempo, swing amount and key.

## Tell the user (short)
`Boom bap · 90 BPM · swing 58 % (kick early, snare late, Dilla-style) · D minor · Dm7 – B♭maj7 loop,
rolled Rhodes pitched -2 st and low-passed · kick 1/1.75/2.5, snare 2 & 4 with ghost notes · upright
bass on the kicks · crackle at -27 dB. Tracks: Drums, Bass, Keys, Texture. Next: hook counter line or
arrange 16-bar verses?`
