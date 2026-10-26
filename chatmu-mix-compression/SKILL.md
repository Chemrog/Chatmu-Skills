---
name: chatmu-mix-compression
description: >
  Use in Co-Producer (Ableton Live) whenever you add or adjust compression on a
  track, a bus or the mix: vocals, kick, snare, drum bus, bass, 808, keys, pads,
  guitars, brass, parallel and glue compression. How an audio engineer sets a
  compressor (threshold first, ratio by goal, attack/release by source, a target
  gain reduction, makeup to equal loudness) and how to do it in Ableton's
  Compressor and Glue Compressor with real values, then verify by measuring.
  Trigger phrases: "comprime", "compresión", "compresor", "ponle compresor",
  "que suene más pegado", "glue", "más punch", "controla la voz", "aplasta",
  "compresión paralela", "compress", "compressor", "glue the drums", "parallel
  compression", and inside chatmu-mixing-progressive phase 4.
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Set compressors like an engineer: threshold first, ratio by goal, attack/release by source, target gain reduction, verified"
version: "1.0"
tags: [studio, ableton, mixing, mezcla, compression, compresión, compressor, glue, co-producer]
requiresTools: ["local_ableton_snapshot", "local_ableton_devices", "local_ableton_device_params", "local_ableton_set_device_param", "local_ableton_apply", "local_ableton_load_devices", "local_ableton_undo", "local_ears_track_levels", "local_ears_listen", "local_ableton_transport"]
---

# Chatmu — Compression
**Version:** 1.0
**Requires:** Chatmu Desktop ≥ 0.1.59 (parameters in real units: `display: "-18 dB"`, `"2:1"`), Ableton Live, Chatmu Ears.
**Related:** chatmu-mixing-progressive (when in the mix flow), chatmu-mix-eq (EQ before/after), chatmu-session-prep (gain staging first).

## What does this Skill do?

Compression only works if the signal crosses the threshold. Ableton's Compressor loads at
**Threshold 0 dB and Ratio 4:1**: with a normal level nothing reaches 0 dB, so it is on the
track and does almost nothing; an engineer opening that session sees "4:1 everywhere" and
knows nobody set it. This skill sets each compressor for a reason, with numbers, and checks
the result.

## HARD RULES

1. **Every compressor has a goal**, said to the user in one line: control the peaks of a
   vocal, add punch to the kick, glue the drum bus… No goal = no compressor.
2. **Threshold first, then ratio.** Lower the threshold until the loudest parts get the
   target gain reduction (table below). Never leave Threshold at 0 dB.
3. **Ratio by goal, not 4:1 by default.** Gentle control / glue 1.5:1–2:1; normal control
   2:1–3:1; firm control 4:1; peak catching / aggressive 6:1–10:1 (only short peaks).
4. **Gain reduction targets** (on the loud parts): glue 1–2 dB, gentle 2–4 dB, firm 4–6 dB,
   aggressive 6–10 dB. More than ~10 dB on a single compressor: use two in series (each 3–5 dB)
   or parallel compression instead.
5. **Makeup to equal loudness.** After compressing, add makeup so the track is as loud as it
   was bypassed, and compare at equal loudness. Louder always "sounds better": don't fool
   yourself or the user.
6. **Real units only.** `local_ableton_set_device_param { …, param: "Ratio", display: "2:1" }`;
   answer with the value Live reports back (`display_value`). Never write internal 0–1 numbers.
7. **Not everything gets compressed.** Pads, most synths, reverb returns and already-compressed
   samples/loops usually don't need it. Kick/bass/vocal/drum bus usually do.
8. **Measure before and after** (Verification). If it got worse or the user doesn't like it:
   `local_ableton_undo`.

## The four controls (what they do, in words the user understands)

| Control | Does | Rule of thumb |
|---|---|---|
| Threshold | level above which it starts to compress | set it for the target gain reduction |
| Ratio | how hard: 4:1 = 4 dB over the threshold come out as 1 dB | by goal (rule 3) |
| Attack | how fast it grabs | slow (10–30 ms) lets the transient through = **punch**; fast (0.1–3 ms) **controls/flattens** |
| Release | how fast it lets go | fast = more energy/pumping; slow = smoother; follow the groove: it should recover before the next hit |
| Knee | soft knee = starts gradually (vocals, buses); hard = precise (drums) | 6–10 dB soft for vocals/buses |
| Makeup / Output | gain after compression | equal loudness (rule 5) |
| Dry/Wet | parallel compression inside the device | 30–50 % wet for drums/vocals in parallel |

## Starting points by source (then adjust by ear and by the measurement)

| Source | Device | Ratio | Attack | Release | GR target | Notes |
|---|---|---|---|---|---|---|
| Lead vocal | Compressor, RMS or Peak, soft knee | 2:1–4:1 | 3–10 ms | 50–150 ms (or Auto) | 3–6 dB | Urban/reggaetón/trap vocal: 2 in series (fast peak catcher 4:1 –2..3 dB + 2:1 –3 dB). Ballad: lighter. |
| Backing vocals | Compressor | 3:1–4:1 | 5 ms | 80 ms | 4–6 dB | more controlled than the lead so they sit behind |
| Kick | Compressor, Peak, hard knee | 3:1–4:1 | 10–30 ms | 50–100 ms | 2–4 dB | slow attack keeps the click; skip it if the sample already punches |
| Snare / clap | Compressor, Peak | 3:1–4:1 | 5–20 ms | 80–150 ms | 3–5 dB | longer release = more body |
| Drum bus | Glue Compressor | 2:1 (4:1 for hip-hop) | 10–30 ms | 0.2–0.4 s or Auto | 1–3 dB | glue; Dry/Wet 100 % or parallel 50 % |
| Parallel drums | Compressor/Glue on a return or Dry/Wet | 4:1–10:1 | 1–5 ms | 50–100 ms | 8–12 dB on the wet | blend 20–40 % under the dry |
| Electric/synth bass | Compressor, RMS | 3:1–4:1 | 10–20 ms | 80–150 ms | 3–6 dB | steady level under the kick; sidechain from kick is separate (chatmu-studio-sidechain) |
| 808 | Compressor (or none) | 2:1–4:1 | 20–30 ms | 100–200 ms | 2–3 dB | keep the punch; level mostly via saturation + fader |
| Acoustic guitar | Compressor, RMS, soft | 2:1–3:1 | 10–20 ms | 100–200 ms | 2–4 dB | strumming peaks |
| Piano / keys | Compressor, RMS, soft | 2:1 | 10–30 ms | 100–200 ms | 1–3 dB | often none |
| Brass / horns | Compressor | 3:1 | 5–15 ms | 80–150 ms | 3–5 dB | brass is very dynamic |
| Pads / strings | usually none | 1.5:1–2:1 | 30 ms | 300 ms | 1–2 dB | only if they jump around |
| Mix bus (glue) | Glue Compressor | 2:1 | 10–30 ms | Auto | 1–2 dB | gentle; last check with the user |

Genre: **lo-fi / hip-hop** tolerate more (parallel drums, 6 dB on the vocal); **reggaetón /
trap** vocals very controlled and forward (series compression); **jazz / acoustic / regional**
lighter (keep the dynamics: 1–3 dB).

## Ableton devices (parameter names; check them first with local_ableton_device_params)

- **Compressor:** `Threshold` (dB), `Ratio` ("2:1"…"inf:1"), `Attack` (ms), `Release` (ms) and
  `Auto Release` (On/Off), `Knee` (dB), `Model` ("Peak", "RMS", "Expand"), `Output Gain` / makeup,
  `Dry/Wet`, `Lookahead`. Sidechain: `local_ableton_device_routing`.
- **Glue Compressor** (bus glue, SSL-style; stepped values): `Threshold`, `Ratio` ("2", "4", "10"),
  `Attack` (0.01 / 0.1 / 0.3 / 1 / 3 / 10 / 30 ms), `Release` (0.1 / 0.2 / 0.4 / 0.6 / 0.8 / 1.2 s,
  "Auto"), `Makeup`, `Range`, `Dry/Wet`, `Soft Clip`.
- **Limiter**: only on the Master for the final ceiling (chatmu-master-chain), not as a mix compressor.
- Parameter names can differ slightly between Live versions: read the device first and use the
  names it returns. A partial unique name works (`"Thresh"`).

## Procedure (per compressor)

1. **Goal** (rule 1) and **source** → starting row of the table.
2. **Load** if needed: `local_ableton_load_devices` (Compressor after the EQ that cleans,
   before the EQ that colours: see chatmu-mix-eq).
3. **Set everything in one call** with `local_ableton_apply` (or one by one with
   `local_ableton_set_device_param`), in real units: Model, Ratio, Attack, Release/Auto,
   Knee, **Threshold last**.
4. **Threshold for the target GR.** Live does not expose the gain-reduction meter through the
   API, so estimate it: the threshold must sit **below the track's loud parts**. Measure the
   track (`local_ears_track_levels` with that track, or `local_ears_listen` soloed):
   threshold ≈ the track's short-term peak level − (GR target × ratio / (ratio − 1)).
   Example: peaks at −10 dBFS, target 4 dB at 4:1 → threshold ≈ −10 − 5.3 ≈ −15 dB.
5. **Makeup** = roughly GR × 0.5–0.8 (then match loudness by measurement).
6. **Verify** (below). Report: "Compressor en Voz: 3:1, ataque 5 ms, release auto, umbral −18 dB,
   ~4 dB de compresión en las partes fuertes, +3 dB de makeup".

## Verification

- Before and after, same bars, same track: `local_ears_track_levels { tracks: [track], bars }`.
  - The **dynamic range of the track should shrink** by about the GR target (short-term max − momentary
    min or the crest factor in Ears' dynamics); if it barely changed, the threshold is too high.
  - Loudness (`lufs_s`) back within ±1 LU of the bypassed track (rule 5).
- Listen in context (`local_ears_listen` on the mix): no audible pumping unless asked; transients
  still there on drums (if the kick lost its click, the attack is too fast).
- If you cannot measure (Ears/plugin missing), say "no verificado" and give the user the settings
  to check by ear (and the gain-reduction meter in Live's Compressor).

## Don'ts

- Don't leave a compressor at its default (0 dB threshold, 4:1): that's decoration, not compression.
- Don't put the same 4:1 on every track; don't compress pads/returns "because".
- Don't push one compressor beyond ~10 dB of gain reduction; use series or parallel.
- Don't compare compressed vs bypassed at different loudness.
- Don't compress the mix bus hard to "make it loud": that's mastering (chatmu-master-chain).
