---
name: chatmu-master-check
description: >
  Use in Co-Producer (Chatmu Desktop + Ableton Live) to check whether an
  exported master is ready to distribute: measures the exported WAV (never the
  live stream) with Chatmu Ears — integrated LUFS, true peak, dynamic range
  (crest, LRA), clipping and other defects — against what each platform asks
  (Spotify, Apple Music, YouTube, SoundCloud, club/DJ), and gives a clear
  verdict "listo para distribuir: sí / no" plus what to fix. Runs right after
  chatmu-studio-export; hands off to chatmu-distribution. Trigger phrases:
  "¿está listo para Spotify?", "¿está listo para distribuir?", "revisa el
  máster", "revisa mi master", "checa el master", "¿cuántos LUFS tiene?",
  "¿suena fuerte?", "¿está muy bajo?", "¿está saturado?", "true peak",
  "loudness", "LUFS", "¿lo puedo subir?", "listo para Apple Music", "listo
  para YouTube", "para el club", "master check", "is my master ready", "ready
  for Spotify", "check my master", "loudness check", "Ableton".
compatibility: chatmu
category: creative
subcategory: studio
shortDesc: "Is the exported master ready to distribute? LUFS, true peak, dynamics and defects vs each platform"
version: "1.1"
tags: ["studio", "ableton", "master", "mastering", "loudness", "lufs", "true-peak", "distribution", "co-producer"]
requiresTools: ["local_ableton_export", "local_ears_analyze_file", "local_ears_render", "local_list_access", "local_ableton_status", "local_ableton_snapshot"]
---

# Chatmu Studio — Master check (ready to distribute?)
**Version:** 1.0
**Requires:** Chatmu Desktop bridge + Chatmu Ears. An exported file (from `chatmu-studio-export` or one the user gives).
**Related:** `chatmu-studio-export` (make the file), `chatmu-master-chain` (fix the master), `chatmu-studio-reference` (compare with a song they like), `chatmu-distribution` (next step).

## What does this Skill do?

It answers one question with numbers: **"¿Este archivo está listo para distribuir?"**
It measures the real file, compares it with what each platform does to it, and gives a
yes/no verdict with the 1–3 things to fix. It never changes the session.

Answer in the user's language (usually Spanish). Short: a table and a verdict.

## HARD RULES

1. **Measure the FILE, never the stream.** `local_ears_listen` is captured before the
   Master fader (and before anything the plugin position skips): its LUFS / true peak are
   indicative only. Delivery numbers come only from `local_ears_analyze_file` on the
   exported file.
2. **The right file.** The file must be the final export of the whole song (or the exact
   range the user wants to release), 24-bit or 32-bit float WAV preferred. A 16-bit MP3
   from WhatsApp is not the master: say so and measure it only as "referencia".
3. **No file yet → export first** with `chatmu-studio-export` (whole song, `bit_depth: 32`
   if they will master from it). Never estimate a verdict from the stream.
4. **Platforms normalize, they don't reject.** Spotify / Apple / YouTube turn a loud master
   down; nothing is "rejected" for being loud. What really fails is: clipping / true peak
   above about −1 dBTP (encoder overs), digital silence or gaps, wrong length, and a master
   so crushed that it sounds worse after normalization. Explain it this way; don't scare.
5. **Never say "suena bien" from numbers alone.** Numbers say whether it is technically
   deliverable; the artist's ears decide the sound.
6. **Never invent where a setting lives.** Fixes are done with `chatmu-master-chain` or in
   the user's own mastering chain.

## Phase 0 — Find the file

| Situation | What to do |
|---|---|
| Just exported in this chat | use the path from the export result |
| "el que exporté ayer" | look in `~/Music/Chatmu Exports` (default export folder) or where they say; `local_list_access` shows the granted folders |
| A file they attach or name (Descargas…) | use that path (wav, aiff, flac, mp3, m4a) |
| No file | offer `chatmu-studio-export` first (rule 3) |

If the folder isn't granted, the app asks the user once; tell them "te va a salir un
permiso para leer esa carpeta, acéptalo".

## Phase 1 — Measure (one file, a few calls)

1. `local_ears_analyze_file { path, tool: "diagnose" }` → ranked issues + summary.
2. `local_ears_analyze_file { path, tool: "loudness" }` → `integrated_lufs`,
   `true_peak_dbtp`, `loudness_range_lu`, short-term / momentary max.
3. `local_ears_analyze_file { path, tool: "dynamics" }` → `crest_factor_db`.
4. `local_ears_analyze_file { path, tool: "defects" }` → clipping, DC, silence, dropouts.
5. Optional, if something looks odd: `local_ears_render { captureId, view: "loudness" }`
   or `"waveform"` (the capture id comes in the analyze result).

Also check the basics: duration (vs what the user expects), sample rate, bit depth, no
silence at the start longer than ~1 s, the tail is not cut.

## Phase 2 — Compare with the platforms

| Destination | Plays at (normalization) | True peak max | Note |
|---|---|---|---|
| Spotify (default "Normal") | −14 LUFS | −1 dBTP (−2 if master is louder than −14) | louder masters are turned down |
| Apple Music (Sound Check) | −16 LUFS | −1 dBTP | |
| YouTube | −14 LUFS | −1 dBTP | only turned down, never up |
| Amazon / Deezer / Tidal | about −14 LUFS | −1 dBTP | |
| SoundCloud | no normalization | −1 dBTP | loudness is what listeners hear |
| Club / DJ promo | −9 to −6 LUFS typical | −1 to −0.3 dBTP | no normalization; dynamics still matter |

**How much will it be turned down?** `gain = target − integrated_lufs` (only if negative).
A master at −8 LUFS plays on Spotify 6 dB quieter: if its crest factor is very low it will
sound flatter than a −12 LUFS master that kept its punch. That's the useful message.

Genre context (competitive integrated loudness, see chatmu-master-chain Phase 0): lo-fi /
acoustic / regional −13..−11, pop / R&B / rock −10..−8, hip-hop / trap −9..−7, reggaetón /
urbano / EDM −8..−6. A master at −14 is not "wrong", but it will sound quieter than its
neighbours wherever there is no normalization: say so if the user expects a commercial level.

## Phase 3 — Verdict

One table + one line:

| Medida | Valor | Objetivo | Estado |
|---|---|---|---|
| LUFS integrado | −9.8 | streaming −14 (se baja 4.2 dB) | ok (alto) |
| True peak | +0.4 dBTP | ≤ −1 dBTP | ❌ |
| Crest factor | 6.1 dB | ≥ 8 dB (pop) | ⚠️ muy comprimido |
| LRA | 4 LU | — | info |
| Defectos | 3 clips en 2:41 | 0 | ❌ |

**Listo para distribuir: NO** — baja el techo del limitador a −1 dBTP y re-exporta.

Verdict rules:
- **NO** if: true peak > −1 dBTP for streaming (> −0.3 for club), any clipping/dropout/
  silence defect, wrong length, or a lossy file presented as the master.
- **SÍ, con notas** if only taste items remain (very loud / very dynamic for the genre).
- **SÍ** otherwise.

Fixes, in producer words (max 3): "baja el techo (ceiling) del limitador a −1 dB",
"quita 2–3 dB de ganancia al limitador: está aplastando la batería", "re-exporta: hay un
corte en 1:12". Offer `chatmu-master-chain` to apply them, then export again
(`chatmu-studio-export`) and **run this check again on the new file**.

## Phase 4 — Next step

If the verdict is SÍ: offer `chatmu-distribution` ("¿lo subimos?"). If they want to compare
with a song they like first: `chatmu-studio-reference`.

## Ears verification

This whole skill IS the verification: every number comes from `local_ears_analyze_file` on
the real file. If Ears can't analyze it (not installed, file not readable, format error),
say **"no verificado"** with the reason and don't give a verdict.

## Don'ts

- Don't measure the stream and call it the master.
- Don't say a platform "rejects" a loud master.
- Don't change the session here; fixes go through `chatmu-master-chain`.
- Don't give a SÍ with a true peak above −1 dBTP for streaming.
