---
name: chatmu-mix-eq
description: >
  Use in Co-Producer (Ableton Live) whenever you EQ a track, a bus or the mix:
  high-pass where it helps, cut mud/boxiness/harshness, make room between kick
  and bass or vocal and synths, add air or presence. Engineer's method (listen in
  context, cut before boosting, narrow cuts / wide boosts, small moves) with a
  frequency map, starting points by source, EQ Eight parameter names in real
  units, and verification with Chatmu Ears' masking measurement. Trigger phrases:
  "ecualiza", "EQ", "ecualización", "suena embarrado", "suena opaco", "suena
  chillón", "le sobra grave", "que se escuche la voz", "limpia los graves",
  "quítale lodo", "más brillo", "más aire", "kick y bajo chocan", "equalize",
  "muddy", "harsh", "boomy", and inside chatmu-mixing-progressive phase 4.
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "EQ like an engineer: cut before boost, frequency map, starting points by source, EQ Eight in real units, verified"
version: "1.0"
tags: [studio, ableton, mixing, mezcla, eq, ecualización, eq-eight, masking, co-producer]
requiresTools: ["local_ableton_snapshot", "local_ableton_devices", "local_ableton_device_params", "local_ableton_set_device_param", "local_ableton_apply", "local_ableton_load_devices", "local_ableton_undo", "local_ears_track_levels", "local_ears_listen"]
---

# Chatmu — EQ
**Version:** 1.0
**Requires:** Chatmu Desktop ≥ 0.1.59 (parameters in real units), Ableton Live, Chatmu Ears.
**Related:** chatmu-mix-compression, chatmu-mixing-progressive, chatmu-studio-sidechain (kick vs bass in time).

## What does this Skill do?

EQ fixes problems and makes room; it doesn't make a bad sound good. This skill decides
**what** to change from a measured reason (masking, mud, harshness), does it in EQ Eight with
real values, and keeps the change only if it measured better and the user likes it.

## HARD RULES

1. **In context.** Decide with the mix playing; a track soloed can sound thin and still be right.
2. **Cut before boosting.** Most moves are cuts; boosts are small and wide.
3. **Narrow cuts, wide boosts.** Problem resonance: Q 4–8, −3..−8 dB. Tone: Q 0.7–1.4, ±1..3 dB.
   Shelves for broad tilt.
4. **Small moves.** Typical cuts −2..−4 dB; boosts ≤ +3 dB. Bigger than ±6 dB means the source or
   the arrangement is the problem: say so.
5. **High-pass only where nothing useful lives below.** Not on kick, 808/bass or a full piano/
   guitar low end. Don't high-pass every track by default.
6. **Real units** (`display: "250 Hz"`, `"-3 dB"`, `"Bell"`, `"Low Cut 48"`), report what Live read back.
7. **Measure, keep or undo.** Use `local_ears_track_levels` masking/bands before and after; keep a
   change only if it improved and the user agrees, else `local_ableton_undo`.

## Frequency map (what lives where)

| Range | Name | Too much = | Too little = |
|---|---|---|---|
| 20–60 Hz | sub | rumble, eats headroom | no weight (808/kick) |
| 60–120 Hz | bass / kick body | boomy | thin |
| 200–500 Hz | low mids | **mud**, cloudy mix | thin, cold |
| 400–800 Hz | box | boxy, "cardboard" | hollow |
| 800 Hz–1.5 kHz | honk / nasal | honky, telephone | lacks presence |
| 2–5 kHz | presence / bite | **harsh**, tiring | dull, far away |
| 5–9 kHz | sibilance / crisp | sss, piercing cymbals | dull |
| 10–16 kHz | air | brittle, hiss | closed, dark |

## Starting points by source (only if the measurement or the ear says so)

| Source | High-pass | Typical cuts | Typical boosts |
|---|---|---|---|
| Kick | none (or ~25–30 Hz rumble) | 300–500 Hz box −2..−4 | 50–80 Hz body or 2–5 kHz click, small |
| 808 / sub bass | ~25 Hz | 200–400 Hz if muddy | harmonics 100–200 Hz to read on phones (or saturation) |
| Bass (electric/synth) | ~30–40 Hz | 200–300 Hz mud | 700 Hz–1.5 kHz definition, small |
| Snare / clap | 80–120 Hz | 400–800 Hz box | 150–250 Hz body, 5 kHz snap |
| Hi-hats / cymbals | 300–500 Hz | harsh 3–6 kHz if piercing | air 10 kHz small |
| Lead vocal | 80–100 Hz (male), 100–120 Hz (female) | 200–400 Hz mud, harsh 2–4 kHz narrow | presence 3–5 kHz, air 10–12 kHz shelf, small |
| Backing vocals | 150–250 Hz | low mids | — (sit them behind the lead) |
| Piano / keys | 60–100 Hz in a busy mix | 250–400 Hz mud | 2–4 kHz presence |
| Acoustic guitar | 80–100 Hz | 200–300 Hz boom, 800 Hz box | 5–10 kHz sparkle |
| Electric guitar | 80–100 Hz | 300–500 Hz | 2–4 kHz bite |
| Pads / strings | 100–200 Hz | low mids so they don't cloud | — (often a low-pass 8–12 kHz to sit back) |
| Brass | 100–150 Hz | 2–3 kHz if harsh | 1–2 kHz presence |
| Reverb / delay returns | 200–300 Hz | — | low-pass 6–10 kHz so they sit behind |

**Making room (masking):** kick vs bass → decide who owns 50–80 Hz; cut the other there (2–3 dB,
Q ~1.5) or sidechain (time). Vocal vs synths/guitars → cut the instruments 2–4 kHz a little where the
vocal lives. The measurement gives the pair and a concrete cut (below).

## EQ Eight (parameter names; check them first with local_ableton_device_params)

Bands 1–8, each: `"N Filter On A"` ("On"/"Off"), `"N Filter Type A"` ("Low Cut 48", "Low Cut 12",
"Low Shelf", "Bell", "Notch", "High Shelf", "High Cut 12", "High Cut 48"), `"N Frequency A"`
("250 Hz", "3.2 kHz"), `"N Gain A"` ("-3 dB"), `"N Resonance A"` (Q, e.g. "1.4"). Also `Output Gain`,
`Adaptive Q`. Use band 1 for the high-pass, 2–3 for cuts, 4 for a gentle boost, 8 for an air shelf
or low-pass. Several bands at once: `local_ableton_apply`.

EQ Three (DJ style, low/mid/high kills) is not for mixing; use EQ Eight.

## Procedure

1. **Reason first:** the user's words ("embarrado", "chillón") or the measurement:
   `local_ears_track_levels` (bands per track + `masking` pairs with a concrete `eq_eight` cut).
2. **Load EQ Eight** if the track has none (before the compressor when cleaning mud/high-pass;
   after it when colouring).
3. **Apply** the cut/boost in real units (rules 3–6). For masking, use the suggested cut as given.
4. **Re-measure the same bars** (`tracks` = the pair): keep it if the overlap dropped and the bands
   moved the intended way, otherwise undo.
5. **Report** in producer words: "Le quité 3 dB a 300 Hz al piano para que el bajo respire; la
   voz quedó más clara (solapamiento 0.62 → 0.41)".

## Don'ts

- Don't high-pass everything by default, and never the kick/808/bass fundamentals.
- Don't boost big narrow bands; don't stack EQs that undo each other.
- Don't EQ in solo only.
- Don't fix with EQ what is an arrangement problem (two parts in the same register: move one).
